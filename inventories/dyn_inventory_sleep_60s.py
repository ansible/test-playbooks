#!/usr/bin/env python3

from datetime import datetime
import json

import time

inventory = {
    'all': {'vars': {'ansible_connection': 'local'}},
    'ungrouped': {'hosts': ['localhost']},
    '_meta': {'hostvars': {'localhost': {
        'current_time': str(datetime.now())
    }}}
}


if __name__ == '__main__':
    time.sleep(60)
    print(json.dumps(inventory, indent=4))
