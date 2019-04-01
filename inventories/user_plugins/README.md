### Custom Inventory Plugins

This contains examples of using source control to maintain and vendor
custom inventory plugins.

Ansible users should place their inventory
plugins inside an `inventory_plugins` folder within the same folder
as their inventory to have it read by AWX in an inventory import.

cd into this directory in order to test manually with these commands:

This should work:

```
ansible-inventory -i cow.yaml --list --export --playbook-dir=.
```

This should raise an exception:

```
ansible-inventory -i fox.yaml --list --export --playbook-dir=.
```

