#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


# this is the string "artemis" encrypted with ansible-vault
# direct output from:
# ansible-vault encrypt_string --vault-id alan@prompt 'artemis'
# (on prompt provide "password" for the vault password)
encrypted_content = (
    "$ANSIBLE_VAULT;1.2;AES256;alan\n"  # line break required, non-obvious Ansible-ism
    "61346130303231633133646133646639626338323565396239396633333736653630633938323733"
    "6235323735363362346632353132386466396232343133340a356330376131383637393535376236"
    "31383561616533643835336266366263346630666335336265306139316138666561626531313864"
    "3161633532623966380a333433303064383831613630366137656330353833383233353561626635"
    "3832"
)


print(
    json.dumps(
        {
            "_meta": {
                "hostvars": {
                    "foobar": {"encrypted_var": {"__ansible_vault": encrypted_content}}
                }
            },
            "ungrouped": {"hosts": ["foobar"]},
        }
    )
)
