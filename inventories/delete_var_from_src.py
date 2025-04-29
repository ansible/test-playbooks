#!/usr/bin/env python3
"""
Sometimes variable `x` is in the update, and sometimes it is not. This is
usefule to test if a variable is deleted from the inventory if it has been
deleted from the source between updates.
"""

import json

from random import random


delete_var: bool = random() < 0.5

vars_dict = {"x_status": "deleted" if delete_var else "not deleted"}
if not delete_var:
    vars_dict["x"] = "testvalue"

print(
    json.dumps(
        {
            "_meta":
            {
                "hostvars": {},
            },
            "all":
            {
                "vars": vars_dict,
            },
        }
    )
)
