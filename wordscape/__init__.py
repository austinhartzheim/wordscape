def name_node(item):
    tags = item['tag']

    if 'amenity' in tags:
        if tags['amenity'] == 'waste_basket':
            return 'a waste basket'
        elif tags['amenity'] == 'bicycle_parking':
            return 'bicycle parking'
        elif tags['amenity'] == 'bench':
            return 'a bench'

    return 'an unknown node type'


class Changeset():
    TEMPLATE = ('# Changeset #{changeset_id}\n{summary}\n\n'
                '## Detailed Changes\n{detailed_changes}')
    MSG_STANDARD = ('This changeset included {additions} additions, '
                    '{modifications} modifications, and {deletions} deletions, '
                    'making {total_changes} changes in total.')

    def __init__(self, changeset_id, changeset_data):
        self.cs_id = changeset_id
        self.cs_data = changeset_data

    def describe(self):
        return self.TEMPLATE.format(
            changeset_id=self.cs_id,
            summary=self.summarize(),
            detailed_changes=self.describe_changes()
        )

    def describe_changes(self):
        messages = []

        for change in self.cs_data:
            if change['type'] == 'node':
                if change['action'] == 'create':
                    msg = 'Added {item_name_article} at ({lat}, {lng})'
                    msg = msg.format(
                        item_name_article=name_node(change['data']),
                        lat=change['data']['lat'],
                        lng=change['data']['lon']
                    )
                    messages.append(msg)

        ret = ''
        for message in messages:
            ret += '* %s\n' % message
        return ret

    def summarize(self):
        additions, modifications, deletions = 0, 0, 0
        nodes_added, nodes_modified, nodes_deleted = 0, 0, 0
        ways_added, ways_modified, ways_deleted = 0, 0, 0
        relations_added, relations_modified, relations_deleted = 0, 0, 0

        nodes_touched, ways_touched, relations_touched = set(), set(), set()

        for change in self.cs_data:
            # Collect aggregate "touch" statistics
            if change['type'] == 'node':
                nodes_touched.add(change['data']['id'])
            elif change['type'] == 'way':
                ways_touched.add(change['data']['id'])
            elif change['type'] == 'relation':
                relations_touched.add(change['data']['id'])

            # Collect per-type statistics
            if change['action'] == 'create':
                additions += 1
                if change['type'] == 'node':
                    nodes_added += 1
                elif change['type'] == 'way':
                    nodes_modified += 1
                elif change['type'] == 'relation':
                    nodes_deleted += 1
            elif change['action'] == 'modify':
                modifications += 1
                if change['type'] == 'node':
                    ways_added += 1
                elif change['type'] == 'way':
                    ways_modified += 1
                elif change['type'] == 'relation':
                    ways_deleted += 1
            elif change['action'] == 'delete':
                deletions += 1
                if change['type'] == 'node':
                    relations_added += 1
                elif change['type'] == 'way':
                    relations_modified += 1
                elif change['type'] == 'relation':
                    relations_deleted += 1

        total_changes = sum((additions, modifications, deletions))

        msg_data = {
            'additions': additions,
            'modifications': modifications,
            'deletions': deletions,
            'total_changes': total_changes,

            'nodes_added': nodes_added,
            'nodes_modified': nodes_modified,
            'nodes_deleted': nodes_deleted,
            'ways_added': ways_added,
            'ways_modified': ways_modified,
            'ways_deleted': ways_deleted,
            'relations_added': relations_added,
            'relations_modified': relations_modified,
            'relations_deleted': relations_deleted,

            'nodes_touched': len(nodes_touched),
            'ways_touched': len(ways_touched),
            'relations_touched': len(relations_touched),
        }

        # Generate message
        message = []
        message.append(self.MSG_STANDARD)

        # Temporarily remove: It's unclear what it means for something to be
        #  the majority of an edit
#        if len(nodes_touched) / total_changes > 0.5:
#            message.append('Edits to {nodes_touched} nodes constitute the '
#                           'majority of this edit.')
#        elif len(ways_touched) / total_changes > 0.5:
#            message.append('Edits to {ways_touched} ways constitute the '
#                           'majority of this edit.')
#        elif len(relations_touched) / total_changes > 0.5:
#            message.append('Edits to {relations_touched} relations constitute',
#                           'the majority of this edit.')

        return (' '.join(message)).format(**msg_data)
