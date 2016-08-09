#! /usr/bin/env python3
'''
Run wordscape on demo data to show what it can do and facilitate
testing by allowing easy repetition of operations on the same data.
'''
import argparse
import datetime
import wordscape


NODE_BASCOM_HILL = {
    'id': 349451685,
    'tag': {
        'ele': '290',
        'natural': 'peak',
        'wikipedia': 'en:Bascom Hill',
        'gnis:county_id': '025',
        'gnis:state_id': '55',
        'gnis:feature_id': '1842317',
        'name': 'Bascom Hill',
        'wikidata': 'Q4866334',
        'gnis:created': '06/01/1999'},
    'version': 5,
    'lon':-89.4036486,
    'timestamp': datetime.datetime(2015, 6, 29, 7, 4, 33),
    'changeset': 32277662,
    'visible': True,
    'user': 'Austin Hartzheim',
    'uid': 2110132,
    'lat': 43.0752828}

NODE_BUS_STOP = {
    'id': 461449913,
    'tag': {'highway': 'bus_stop', 'name': 'Linden at Henry'},
    'version': 2,
    'lon':-89.4102772,
     'timestamp': datetime.datetime(2009, 8, 11, 1, 32, 40),
     'changeset': 2103789,
     'visible': True,
     'user': 'sim',
     'uid': 35247,
     'lat': 43.0750935}


if __name__ == '__main__':
    node = wordscape.Node(NODE_BASCOM_HILL['id'], NODE_BASCOM_HILL)
    print('Bascom Hill:', node.identify())

    node = wordscape.Node(NODE_BUS_STOP['id'], NODE_BUS_STOP)
    print('Bus stop:', node.identify())
