# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: randstr
    author: Chris Meyers <cmeyers@redhat.com>
    version_added: "0.1"
    short_description: generate random string
    description:
        - This lookup returns a random string.
"""
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

import string
import random

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        return [''.join(random.choice(string.ascii_lowercase) for i in range(12))]
