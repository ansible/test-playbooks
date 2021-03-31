#!/usr/bin/env python3
import json
import os


Ng = int(os.environ.get("NUM_GROUPS", 470))
Nh = int(os.environ.get("NUM_HOSTS", 189))


data = {"_meta": {"hostvars": {}}}

hosts = ["Host-{}".format(i) for i in range(Nh)]

for i in range(Ng):
    data["Group-{}".format(i)] = {"hosts": hosts}

print(json.dumps(data, indent=2))
