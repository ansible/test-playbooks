from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    name: blah
    plugin_type: inventory
    short_description: Prints to standard out with data including NUL character
    description: For use in testing processing of that character
    options:
      plugin:
          description: Name of the plugin
          required: true
          choices: ['blah', 'shanemcd.scratch.blah']
'''

from ansible.plugins.inventory import BaseInventoryPlugin


class InventoryModule(BaseInventoryPlugin):
    NAME = 'blah'

    def verify_file(self, path):
        '''
        Return true/false if this is possibly
        a valid file for this plugin to consume
        '''
        for i in range(61):
            print("hi")
            print("\x00\x00\x00")
        return True

    def parse(self, inventory, loader, path, cache):
        '''Return dynamic inventory from source'''
        pass
