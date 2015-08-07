#!/usr/bin/env python

import os
from ansible.module_utils.basic import * # noqa

DOCUMENTATION = '''
---
module: scan_foo
short_description: Return example foo namespace facts.
description:
    - Return example foo namespace made up facts.
version_added: "1.9"
options:
requirements: [ ]
author: Chris Meyers
'''

EXAMPLES = '''
# Example fact output:
# host | success >> {
#    "ansible_facts": {
#        "foo": [
#           {
#               "hello": "world"
#           },
#           {
#               "foo": "bar"
#           }, ... ] } }
'''

def main():
    module = AnsibleModule(
        argument_spec = dict())

    foo = [
      {
        "hello": "world"
      },
      {
        "foo": "bar"
      }
    ]
    results = dict(ansible_facts=dict(foo=foo))
    module.exit_json(**results)

main()
