import enum


AMENITY_TO_ARTICLE = {
    # https://wiki.openstreetmap.org/wiki/Key:amenity
    # sustenance
    'bar': 'a barar',
    'bbq': 'a barbecue grill',
    'biergarten': 'a beer garden',
    'cafe': 'a cafe',
    'drinking_water': 'a drinking fountain',
    'fast_food': 'a fast food restaurant',
    'food_court': 'a food court',
    'ice_cream': 'an ice cream shop',
    'pub': 'a pub',
    'restaurant': 'a restaurant',

    # education
    'college': 'a college',
    'kindergarten': 'a kindergarten',
    'library': 'a library',
    'public_bookcase': 'a public bookcase',
    'school': 'a school',
    'music_school': 'a music school',
    'driving_school': 'a driving school',
    'language_school': 'a language school',
    'university': 'a university campus',

    # transportation
    'bicycle_parking': 'bicycle parking',
    'bicycle_repair_station': 'a bicycle repair station',
    'bicycle_rental': 'a bicycle rental location',
    'boat_sharing': 'a boat sharing location',
    'bus_station': 'a bus station',
    'car_rental': 'a car rental location',
    'car_sharing': 'a car sharing location',
    'car_wash': 'a car wash',
    'ev_charging': 'an electric vehicle charging station',
    'charging_station': 'an electric vehicle charging station',
    'ferry_terminal': 'a ferry terminal',
    'fuel': 'a gas station',
    'grit_bin': 'a container holding grit',
    'motorcycle_parking': 'motorcycle parking',
    'parking': 'a parking location',
    'parking_entrance': 'a parking complex entrance',
    'parking_space': 'a parking space',
    'taxi': 'a taxi pickup location',

    # financial
    'atm': 'an ATM',
    'bank': 'a bank',
    'bureau_de_change': 'a currency exchange',

    # healthcare
    'baby_hatch': 'a baby hatch',
    'clinic': 'a medical clinic',
    'dentist': 'a dentist\'s office',
    'doctors': 'a doctor\'s office',
    'hospital': 'a hospital',
    'nursing_home': 'a nursing home',
    'pharmacy': 'a pharmacy',
    'social_facility': 'a social facility',
    'veterinary': 'a veterinary clinic',
    'blood_donation': 'a blood donation clinic',

    # entertainment
    'arts_centre': 'an arts center',
    'brothel': 'a brothel',
    'casino': 'a casino',
    'cinema': 'a cinema',
    'community_centre': 'a community center',
    'fountain': 'a fountain',
    'gambling': 'a gambling location',
    'nightclub': 'a nightclub',
    'planetarium': 'a planetarium',
    'social_centre': 'a social center',
    'stripclub': 'a strip club',
    'studio': 'a recording studio',
    'swingerclub': 'a swingerclub',
    'theatre': 'a theater',

    # other
    'animal_boarding': 'an animal boarding facility',
    'animal_shelter': 'an animal shelter',
    'bench': 'a bench',
    'clock': 'a clock',
    'courthouse': 'a courthouse',
    'coworking_space': 'a coworking space',
    'crematorium': 'a crematorium',
    'crypt': 'a crypt',
    'dive_centre': 'a diving center',
    'dojo': 'a dojo',
    'embassy': 'an embassy',
    'fire_station': 'a fire station',
    'firepit': 'a firepit',
    'game_feeding': 'a game feeding place',
    'grave_yard': 'a grave yard',
    'gym': 'a gym',
    'hunting_stand': 'a hunting stand',
    'internet_cafe': 'an internet cafe',
    'kneipp_water_cure': 'a kneipp wature cure',  # TODO: check
    'marketplace': 'a marketplace',
    'photo_booth': 'a photo booth',
    # TODO: attempt to infer a more specific name from religion=*
    'place_of_worship': 'a place of worship',
    'police': 'a police station',
    'post_box': 'a post box',
    'post_office': 'a post office',
    'prison': 'a prison',
    'public_building': 'a public building',
    'ranger_station': 'a national park visitor headquarters',
    'recycling': 'a recycling location',
    'rescue_station': 'a rescue station',
    'sauna': 'a sauna',
    'shelter': 'a shelter',
    'shower': 'a shower',
    'telephone': 'a public telephone',
    'toilets': 'public toilets',
    'townhall': 'a town hall',
    'vending_machine': 'a vending machine',
    'waste_basket': 'a waste basket',
    'waste_disposal': 'a waste disposal location',
    'waste_transfer_station': 'a waste transfer station',
    'watering_place': 'a watering place',
    'water_point': 'a water point',
}

HIGHWAY_TO_ARTICLE = {
    # https://wiki.openstreetmap.org/wiki/Key:highway
    # roads
    'motorway': 'a motoray',
    'trunk': 'a trunk road',
    'primary': 'a primary road',
    'secondary': 'a secondary road',
    'tertiary': 'a tertiary road',
    'unclassified': 'an unclassified road',
    'residential': 'a residential road',
    'service': 'a service road',

    # link roads
    'motorway_link': 'a link road',
    'trunk_link': 'a trunk link',
    'primary_link': 'a primary link',
    'secondary_link': 'a secondary link',
    'tertiary_link': 'a tertiary link',

    # special road types
    'living_street': 'a living street',
    'pedestrian': 'a pedestrian street',
    'track': 'a track',
    'bus_guideway': 'a busway',
    'raceway': 'a raceway',
    'road': 'a road',

    # paths
    'footway': 'a footway',
    'bridleway': 'a bridleway',
    'steps': 'steps',
    'path': 'a path',

    # cycleway
    'cycleway': 'a cycleway',  # TODO: use logic to fill out extra cases

    # lifecycle
    'proposed': 'a proposed road',
    'construction': 'a road under construction',

    # other highway features
    'bus_stop': 'a bus stop',
    'crossing': 'a crosswalk',
    'elevator': 'an elevator',
    'emergency_access_point': 'an emergency access sign',
    'escape': 'an emergency stop lane',
    'give_way': 'a yield sign',
    'mini_roundabout': 'a mini roundabout',
    'motorway_junction': 'a motorway junction',
    'passing_place': 'a passing place',
    'rest_area': 'a rest area',
    'speed_camera': 'a speed camera',
    'street_lamp': 'a street lamp',
    'services': 'a service station',
    'stop': 'a stop sign',
    'traffic_signals': 'traffic signals',
    'turning_circle': 'a turning circle',
}


def name_node(item):
    tags = item['tag']

    if not tags:
        return 'a node with no tags'

    if 'amenity' in tags and tags['amenity'] in AMENITY_TO_ARTICLE:
        return AMENITY_TO_ARTICLE[tags['amenity']]

    elif 'railway' in tags:
        if tags['railway'] == 'station':
            return 'a railway station'

    elif 'name' in tags:
        return 'a node named "%s"' % tags['name']

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
                elif change['action'] == 'modify':
                    msg = 'Modified {item_name_article} at ({lat}, {lng})'
                    msg = msg.format(
                        item_name_article=name_node(change['data']),
                        lat=change['data']['lat'],
                        lng=change['data']['lon']
                    )
                    messages.append(msg)
                elif change['action'] == 'delete':
                    msg = 'Deleted node #{id}'
                    msg = msg.format(id=change['data']['id'])
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


class Way():

    class DataType(enum.Enum):
        '''
        Describes the format of the data being passed into the function,
        '''
        #: The data is a list of dicts containing the data for all nodes
        #: in the way in addition to data for the way itself.
        full = 1
        #: The data only describes the way as a whole; it does not include
        #: node-level data.
        way_only = 2

    def __init__(self, way_id, way_data):
        self.way_id = way_id
        self.way_data = None
        self.node_data = []

        if isinstance(way_data, dict):
            self.data_type = self.DataType.way_only
            self.way_data = way_data
        elif isinstance(way_data, (list, tuple)):
            self.data_type = self.DataType.full
            self.node_data = [n for n in way_data if n['type'] == 'node']
            for data in way_data:
                if data['type'] == 'way':
                    self.way_data = data['data']
                    return
            raise ValueError('way_data does not include way summary')
        else:
            raise TypeError('Data format is unknown')

    def identify(self):
        tags = self.way_data['tag']

        if 'highway' in tags:
            if tags['highway'] in HIGHWAY_TO_ARTICLE:
                return HIGHWAY_TO_ARTICLE[tags['highway']]
