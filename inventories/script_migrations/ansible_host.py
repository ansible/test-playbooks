#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

ansible_host = os.environ.get("SCRIPT_HOST", "localhost")

inventory = dict()
inventory["some_group"] = dict()
inventory["some_group"]["hosts"] = [ansible_host]
inventory["some_group"]["vars"] = dict(ansible_connection="local")

print(json.dumps(inventory))
