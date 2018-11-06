### Cloud module testing

These modules are aiming to enable various layers of testing:

 - presence of dependencies
 - correct credential schema was applied
 - effective credentials have been applied
 - successful execution
 - change to infrastructure was made

This doc contains some brief usage notes.

The ambitions of these playbooks do not go as far as changing infrastructure,
and that testing already lives elsewhere.

#### Dependency sufficiency

Here is an example of running without a needed dependency:

```
$ ansible-playbook -i localhost, cloud_modules/aws.yml

PLAY [Test use of credentials with cloud module, taken from Ansible docs] *************************************************************************************************************

TASK [Provision a set of instances (credential_type=aws)] *****************************************************************************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "boto required for this module"}
	to retry, use: --limit @/Users/alancoding/Documents/repos/jlaska-ansible-playbooks/cloud_modules/aws.retry

PLAY RECAP ****************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0   
```

If you are running from
a virtual environment, you may need to specify interpreter.
Here is an example of running the playbook with the proper dependencies
installed, but no attempt to specify credentials:

```
$ ansible-playbook -i localhost, cloud_modules/aws.yml -e ansible_python_interpreter=$(which python)

PLAY [Test use of credentials with cloud module, taken from Ansible docs] ***** 

TASK: [Provision a set of instances (credential_type=aws)] ******************** 
failed: [localhost] => {"failed": true}
msg: Either region or ec2_url must be specified

FATAL: all hosts have already failed -- aborting

PLAY RECAP ******************************************************************** 
           to retry, use: --limit @/Users/alancoding/aws.retry

localhost                  : ok=0    changed=0    unreachable=0    failed=1   
```

(note: this now constitutes an "incorrectly parameterized credentials" case)

In this example, the boto dependency, needed for the AWS modules, was
installed inside of the active virtual environment,
so it did not produce an error due to the dependency. However, it
did produce an error because insufficient credentials were given.

#### Credential parameters

Example of incorrectly parameterized credentials:

```
$ ansible-playbook -i localhost, cloud_modules/vmware.yml -e ansible_python_interpreter=$(which python)

PLAY [Test use of credentials with cloud module, taken from Ansible docs] *************************************************************************************************************

TASK [VMWare Clone the template (credential_type=vmware)] *****************************************************************************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "Hostname parameter is missing. Please specify this parameter in task or export environment variable like 'export VMWARE_HOST=ESXI_HOSTNAME'"}
	to retry, use: --limit @/Users/alancoding/Documents/repos/jlaska-ansible-playbooks/cloud_modules/vmware.retry

PLAY RECAP ****************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0   
```

Example of parameterized, but incorrect, credentials:

```
$ VMWARE_HOST=ESXI_HOSTNAME VMWARE_USER=ESXI_USERNAME VMWARE_PASSWORD=ESXI_PASSWORD ansible-playbook -i localhost, cloud_modules/vmware.yml -e ansible_python_interpreter=$(which python)

PLAY [Test use of credentials with cloud module, taken from Ansible docs] *************************************************************************************************************

TASK [VMWare Clone the template (credential_type=vmware)] *****************************************************************************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "Unknown error while connecting to vCenter or ESXi API at ESXI_HOSTNAME:443 : [Errno 8] nodename nor servname provided, or not known"}
	to retry, use: --limit @/Users/alancoding/Documents/repos/jlaska-ansible-playbooks/cloud_modules/vmware.retry

PLAY RECAP ****************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0   
```

#### Credential functionality

If credentials are correct, the playbooks should succeed, as long as `state`
isn't changed. These playbooks are not intended to make an actual change
to the targeted infrastructure.
