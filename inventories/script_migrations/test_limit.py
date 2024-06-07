#!/usr/bin/env python3
import json

# Create hosts and groups
inv = dict(_meta=dict(hostvars={}), hosts=[])
inv["group-0"] = [
    "duplicate_host",
    "host with spaces in name",
    "host-1",
    "host-2",
    "host-3",
]
inv["group-1"] = [
    "duplicate_host",
    "host-4",
    "host-5",
    "host-6",
]
inv["group-2"] = [
    "duplicate_host",
    "host-7",
    "host-8",
    "host-9",
]

# Add _meta hostvars
for grp, hosts in inv.items():
    for host in hosts:
        inv["_meta"]["hostvars"][host] = dict(
            ansible_host="127.0.0.1", ansible_connection="local"
        )

print(json.dumps(inv, indent=2))
