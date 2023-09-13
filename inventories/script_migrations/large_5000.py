#!/usr/bin/env python
import json


data = {"_meta": {"hostvars": {}}}

for i in range(5000):
    data.setdefault("ungrouped", []).append("Host-{}".format(i))

print(json.dumps(data, indent=2))
