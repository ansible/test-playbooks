#!/usr/bin/env python
from argparse import ArgumentParser
from pprint import pprint

inventory = {'group_one': {'hosts': ['group_one_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_and_two_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_two_and_three_host_0{}'.format(i) for i in range(1, 6)],
                           'vars': {'is_in_group_one': True}},
             'group_two': {'hosts': ['group_two_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_and_two_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_two_and_three_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_two_and_three_host_0{}'.format(i) for i in range(1, 6)],
                           'vars': {'is_in_group_two': True}},
             'group_three': {'hosts': ['group_three_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_two_and_three_host_0{}'.format(i) for i in range(1, 6)]
                                    + ['group_one_two_and_three_host_0{}'.format(i) for i in range(1, 6)],
                             'vars': {'is_in_group_three': True}}}


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--list', dest='list_instances', action='store_true', default=True,
                        help='List instances (default: True)')
    parser.add_argument('--host', dest='requested_host', help='Get all the variables about a specific instance')
    return parser.parse_args()


def load_inventory():
    args = parse_args()
    if args.list_instances:
        pprint(inventory)


if __name__ == '__main__':
    load_inventory()
