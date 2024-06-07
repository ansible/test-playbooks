#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

print(
    json.dumps(
        {
            "_meta": {"hostvars": {"old_host": {}}},
            "ungrouped": {"hosts": ["old_host"]},
            "ghost": {"hosts": [], "vars": {"foobar": "hello_world"}},
            "ghost2": {"hosts": []},
            "all": {"children": ["ghost3"]},
        }
    )
)
