#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# changes made relative to overwrite1.py:
# - host_1 is removed from parent group (but still present in import)
# - child_group2 is removed from parent group (but still present in import)
# - switch1 and switch2 trade hosts
# - child_switch1 and 2 trade child groups
# - "will remove" host / group are removed

import json

print(
    json.dumps(
        {
            "_meta": {"hostvars": {"host_1": {}, "host_2": {}}},
            "child_group": {"hosts": ["host_of_child"]},
            "child_group2": {"hosts": ["host_of_child"]},
            "not_child": {"hosts": ["host_of_not_child"]},
            "switch1": {"hosts": ["host_switch2"]},
            "switch2": {"hosts": ["host_switch1"]},
            "parent_switch1": {"children": ["switch2"]},
            "parent_switch2": {"children": ["switch1"]},
            "parent_group": {"hosts": ["host_2"], "children": ["child_group"]},
        }
    )
)
