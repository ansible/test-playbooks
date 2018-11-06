### Cloud module testing

These modules enable various layers of testing:

 - presence of dependencies
 - effective credentials have been applied
 - successful execution

This doc contains some brief usage notes. If you are running from
a virtual environment, you may need to specify interpreter, example:

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

In this example, the boto dependency, needed for the AWS modules, was
installed inside of the active virtual environment,
so it did not produce an error due to the dependency. However, it
did produce an error because insufficient credentials were given.
