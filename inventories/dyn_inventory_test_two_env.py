#!/usr/bin/env python
from argparse import ArgumentParser
from datetime import datetime
import json
import os

# This is almost the same as dyn_inventory_test_env.py
# but it reads from 2 environment variables so that using multiple
# credentials with inventory sources can be tested

inventory = {
    'all': {'vars': {'ansible_connection': 'local'}},
    'ungrouped': {'hosts': ['localhost']},
    '_meta': {'hostvars': {'localhost': {
        'test_env': os.environ.get('TEST_ENV', False),
        'test_env2': os.environ.get('TEST_ENV2', False),
        'current_time': str(datetime.now())
    }}}
}


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
