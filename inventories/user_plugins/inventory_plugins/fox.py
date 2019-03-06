from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    inventory: cow
    version_added: "2.7"
    short_description: What does the fox say? No one knows, error!
    description:
        - Ignores whatever you give it
        - You will never find out what the fox says
'''

EXAMPLES = r'''
    # plugin: fox
'''

from ansible.plugins.inventory import BaseInventoryPlugin


def ancient_mystery():
    raise Exception('Gering-ding-ding-ding-dingeringeding')


class InventoryModule(BaseInventoryPlugin):

    NAME = 'fox'

    def parse(self, inventory, loader, host_list, cache=True):
        ''' doesnt parse the inventory file, but claims it did anyway '''
        super(InventoryModule, self).parse(inventory, loader, host_list)
        self.inventory.add_host('fox')  # could be used to test rollback
        ancient_mystery()
