#!/usr/bin/python
# -*- coding: utf-8 -*-

# Simple module to generate Ansible meta events (warning, error, deprecated)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: generate_meta_events
short_description: Generate Ansible meta events for testing
description:
    - This module generates warning, error, and deprecated meta events
options:
    event_type:
        description:
            - Type of meta event to generate
        type: str
        choices: [warning, error, deprecated]
        default: warning
    message:
        description:
            - Message to include in the meta event
        type: str
        default: "Test meta event"
author:
    - Test
"""

EXAMPLES = r"""
- name: Generate warning meta event
  generate_meta_events:
    event_type: warning
    message: "This is a test warning"

- name: Generate error meta event
  generate_meta_events:
    event_type: error
    message: "This is a test error"

- name: Generate deprecated meta event
  generate_meta_events:
    event_type: deprecated
    message: "This feature is deprecated"
"""

RETURN = r"""
message:
    description: The message that was generated
    returned: always
    type: str
event_type:
    description: The type of event that was generated
    returned: always
    type: str
"""

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            event_type=dict(
                type="str",
                choices=["warning", "error", "deprecated"],
                default="warning",
            ),
            message=dict(type="str", default="Test meta event"),
        ),
        supports_check_mode=True,
    )

    event_type = module.params["event_type"]
    message = module.params["message"]

    if event_type == "warning":
        # Generate warning meta event using module.warn()
        module.warn(f"{message}")
        module.exit_json(changed=False, message=message, event_type=event_type)

    elif event_type == "error":
        raise Exception("Not implemented,maybe exception will cause error")

    elif event_type == "deprecated":
        # Generate deprecated meta event
        module.deprecate(msg=f"{message}", version="2.0", collection_name="test")
        module.exit_json(changed=False, message=message, event_type=event_type)


if __name__ == "__main__":
    main()
