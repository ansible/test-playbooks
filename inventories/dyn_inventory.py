#!/usr/bin/env python3
from argparse import ArgumentParser
import json

inventory = {'group_one': {'hosts': ['group_one_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_and_two_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_two_and_three_host_0{}'.format(i) for i in range(1, 6)],
                           'vars': {'is_in_group_one': True,
                                    'complex_var': [{"dir": "/opt/gwaf/logs",
                                                     "sourcetype": "gwaf",
                                                     "something_else": [1, 2, 3]}]}},
             'group_two': {'hosts': ['group_two_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_and_two_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_two_and_three_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_two_and_three_host_0{}'.format(i) for i in range(1, 6)],
                           'vars': {'is_in_group_two': True}},
             'group_three': {'hosts': ['group_three_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_two_and_three_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_two_and_three_host_0{}'.format(i) for i in range(1, 6)],
                             'vars': {'is_in_group_three': True}},
             'all': {'vars': {'ansible_connection': 'local',
                              'inventories_var': True}},
             'ungrouped': {'hosts': ['ungrouped_host_0{}'.format(i) for i in range(1, 6)]},
             '_meta': {'hostvars': {'group_one_host_01': {'group_one_host_01_has_this_var': True},
                                    'group_two_host_01': {'group_two_host_01_has_this_var': True},
                                    'group_three_host_01': {'group_three_host_01_has_this_var': True}}}}

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--list', dest='list_instances', action='store_true', default=True,
                        help='List instances (default: True)')
    parser.add_argument('--host', dest='requested_host', help='Get all the variables about a specific instance')
    return parser.parse_args()


def load_inventory():
    args = parse_args()
    if args.list_instances:
        print(json.dumps(inventory, indent=4))


if __name__ == '__main__':
    load_inventory()
