#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from datetime import datetime


def time_val():
    return datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S.%f')


host_names = [f'change_of_vars_{i}' for i in range(1000)]

hostvars = {}
for host in host_names:
    hostvars[host] = {
        "static_key": "host_dynamic_{}".format(time_val()),
        "dynamic_{}".format(time_val()): "host_static_value"
    }


print(json.dumps({
    "_meta": {
        "hostvars": hostvars
    },
    "ungrouped": {
        "hosts": host_names
    }
}))
