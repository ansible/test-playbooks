#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from ansible.module_utils.basic import * # noqa

DOCUMENTATION = '''
---
module: scan_facts
short_description: Return sample facts into facts namespace.
description:
    - Return sample facts into facts namespace.
version_added: "2.3"
options:
requirements: []
author: Chris Meyers, Christopher Wang
'''

EXAMPLES = '''
# Example fact output:
{
    "ansible_facts": {
        "bool": true,
        "empty_list": [],
        "empty_obj": {},
        "float": 1.0,
        "int": 1,
        "list": ["abc", 1, 1.0, true, null, [], {}],
        "null": null,
        "obj": {
            "bool": true,
            "float": 1.0,
            "int": 1,
            "list": [],
            "null": null,
            "obj": {},
            "string": "abc"
        },
        "string": "abc",
        "unicode_string": "鵟犭酜귃ꔀꈛ竳䙭韽ࠔ"
    },
    "changed": false
}
'''

def main():
    module = AnsibleModule(
        argument_spec = dict())

    string="abc"
    unicode_string="鵟犭酜귃ꔀꈛ竳䙭韽ࠔ"
    int=1
    float=1.0
    bool=True
    null=None
    list=["abc", 1, 1.0, True, None, [], {}]
    obj={"string": "abc",
         "int": 1,
         "float": 1.0,
         "bool": True,
         "null": None,
         "list": [],
         "obj": {}}
    empty_list=[]
    empty_obj={}

    results = dict(ansible_facts=dict(string=string, unicode_string=unicode_string, int=int, float=float, bool=bool,
                                      null=null, list=list, obj=obj, empty_list=empty_list, empty_obj=empty_obj))
    module.exit_json(**results)

main()
