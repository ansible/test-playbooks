#!/usr/bin/env python3
from argparse import ArgumentParser
from datetime import datetime
import json
import os

inventory = {'all': {'vars': {'ansible_connection': 'local'}},
             'ungrouped': {'hosts': ['localhost']},
             '_meta': {'hostvars': {'localhost': {'test_env': os.environ.get('TEST_ENV', False),
                                                  'current_time': str(datetime.now())}}}}


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
