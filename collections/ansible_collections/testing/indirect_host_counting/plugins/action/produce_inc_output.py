from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        self._supports_check_mode = False

        result = super(ActionModule, self).run(tmp, task_vars)

        result['msg'] = 'This is my message, maybe it is structured?'
        result['my_children'] = {
            'child_1': {
                'changed': True,
            },
            'child_2': {
                'changed': False,
            },
            'child_3': {
                'grandchildren': {
                    'grandchild_1': {
                        'changed': True,
                    }
                }
            }
        }
        result['changed'] = False
        return result
