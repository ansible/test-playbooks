#!/usr/bin/env python3
import json
import os


Ng = int(os.environ.get("NUM_GROUPS", 25))
Nh = int(os.environ.get("NUM_HOSTS", 25))


data = {"_meta": {"hostvars": {}}}

for i in range(Nh):
    data.setdefault("ungrouped", []).append("Host-{}".format(i))

for i in range(Ng):
    data["Group-{}".format(i)] = {"vars": {"foo": "bar"}}

print(json.dumps(data, indent=2))
