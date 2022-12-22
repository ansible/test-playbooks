from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    name: blah
    plugin_type: inventory
    short_description: Returns Ansible inventory from CSV
    description: Returns Ansible inventory from CSV
    options:
      plugin:
          description: Name of the plugin
          required: true
          choices: ['blah']
'''



from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleError, AnsibleParserError



class InventoryModule(BaseInventoryPlugin):
    NAME = 'blah'


    def verify_file(self, path):
        '''Return true/false if this is possibly a valid file for this plugin to
consume

        '''
        print("hi")
        print("\x00\x00\x00")
        True

    def parse(self, inventory, loader, path, cache):
       '''Return dynamic inventory from source '''
       pass
