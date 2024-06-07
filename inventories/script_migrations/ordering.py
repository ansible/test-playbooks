#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


print(
    json.dumps(
        {
            "_meta": {"hostvars": {"h01": {}, "h02": {}, "h03": {}}},
            "agroup": {"hosts": ["h01", "h02", "h03"]},
        }
    )
)
