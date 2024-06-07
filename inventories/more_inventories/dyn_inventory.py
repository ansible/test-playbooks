#!/usr/bin/env python3
from argparse import ArgumentParser
import json

inventory = {'group_four': {'hosts': ['group_four_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_four_and_five_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_four_five_and_six_host_0{}'.format(i) for i in range(1, 6)],
                           'vars': {'is_in_group_four': True}},
             'group_five': {'hosts': ['group_five_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_four_and_five_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_five_and_six_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_four_five_and_six_host_0{}'.format(i) for i in range(1, 6)],
                           'vars': {'is_in_group_five': True}},
             'group_six': {'hosts': ['group_six_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_five_and_six_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_four_five_and_six_host_0{}'.format(i) for i in range(1, 6)],
                             'vars': {'is_in_group_six': True}},
             'all': {'vars': {'ansible_connection': 'local',
                              'inventories_var': True}},
             'ungrouped': {'hosts': ['ungrouped_host_{}'.format('0{}'.format(i) if len(str(i)) == 1 else i) for i in range(6, 11)]},
             '_meta': {'hostvars': {'group_four_host_01': {'group_four_host_01_has_this_var': True},
                                    'group_five_host_01': {'group_five_host_01_has_this_var': True},
                                    'group_six_host_01': {'group_six_host_01_has_this_var': True}}}}

def dumps(dct):
    return json.dumps(dct, sort_keys=True, indent=4, separators=(',', ': '))

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--list', dest='list_instances', action='store_true', default=True,
                        help='List instances (default: True)')
    parser.add_argument('--host', dest='requested_host', help='Get all the variables about a specific instance')
    return parser.parse_args()


def load_inventory():
    args = parse_args()
    if args.list_instances:
        print(dumps(inventory))


if __name__ == '__main__':
    load_inventory()
