from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    inventory: cow
    version_added: "2.7"
    short_description: Returns string "moooooo" for values of stuff
    description:
        - Ignores whatever you give it
        - Returns inventory containing "moooooo"
'''

EXAMPLES = r'''
    # mooooo
'''

from ansible.plugins.inventory import BaseInventoryPlugin


class InventoryModule(BaseInventoryPlugin):

    NAME = 'cow'

    def parse(self, inventory, loader, host_list, cache=True):
        ''' doesnt parse the inventory file, but claims it did anyway '''
        super(InventoryModule, self).parse(inventory, loader, host_list)
        self.inventory.add_host('moooooo')
