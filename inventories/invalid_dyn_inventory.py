#!/usr/bin/env python3
from argparse import ArgumentParser
import json

inventory = {'invalid': True}

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--list', dest='list_instances', action='store_true', default=True,
                        help='List instances (default: True)')
    parser.add_argument('--host', dest='requested_host', help='Get all the variables about a specific instance')
    return parser.parse_args()

def dumps(dct):
    return json.dumps(dct, sort_keys=True, indent=4, separators=(',', ': '))

def load_inventory():
    args = parse_args()
    if args.list_instances:
        print(dumps(inventory))


if __name__ == '__main__':
    load_inventory()
