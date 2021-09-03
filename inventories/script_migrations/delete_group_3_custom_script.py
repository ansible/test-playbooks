#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import uuid

unique_name = str(uuid.uuid4())
host_1 = "host_{}".format(unique_name)
host_2 = "host_2_{}".format(unique_name)
print(
    json.dumps(
        {
            "_meta": {
                "hostvars": {
                    "{}".format(host_1): {"name": "{}".format(host_1)},
                    "{}".format(host_2): {"name": "{}".format(host_2)},
                    "all_have": {"name": "all_have"},
                    "all_have2": {"name": "all_have2"},
                    "all_have3": {"name": "all_have3"},
                }
            },
            "child_group": {"hosts": ["{}".format(host_1), "all_have"]},
            "child_group2": {"hosts": ["{}".format(host_1), "all_have2"]},
        }
    )
)
