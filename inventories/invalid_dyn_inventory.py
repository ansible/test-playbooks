#!/usr/bin/env python
from argparse import ArgumentParser
from pprint import pprint

inventory = {'invalid': True}

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
