#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

print(
    json.dumps(
        {
            "_meta": {"hostvars": {"host_1": {}, "host_2": {}}},
            "ungrouped": {"hosts": ["will_remove_host"]},
            "child_group": {"hosts": ["host_of_child"]},
            "child_group2": {"hosts": ["host_of_child"]},
            "not_child": {"hosts": ["host_of_not_child"]},
            "switch1": {"hosts": ["host_switch1"]},
            "switch2": {"hosts": ["host_switch2"]},
            "parent_switch1": {"children": ["switch1"]},
            "parent_switch2": {"children": ["switch2"]},
            "will_remove_group": {"hosts": ["host_2"]},
            "parent_group": {
                "hosts": ["host_1", "host_2"],
                "children": ["child_group", "child_group2"],
            },
        }
    )
)
