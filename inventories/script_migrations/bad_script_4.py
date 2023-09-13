#!/bin/sh
cat << EOF
{
    "all": {"hosts": ["{{ lookup('pipe', 'touch /tmp/foobar') }}", "localhost"]},
    "_meta": {
        "hostvars": {
            "{{ lookup('pipe', 'touch /tmp/foobar') }}": {},
            "localhost": {
                "ansible_connection": "local",
                "ansible_python_interpreter": "{{ ansible_playbook_python }}",
            },
        }
    },
}
EOF
