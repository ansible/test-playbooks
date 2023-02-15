### Demo Problem for Smart Inventory hostvars Filtering

This hosts the original demo problem for "constructed" inventory.
Original location was at:

https://github.com/AlanCoding/Ansible-inventory-file-examples/tree/master/issues/AWX371

Original related issue is:

https://github.com/ansible/awx/issues/371

The key contents are the `east.ini` and `west.ini` inventories in this folder,
which are intended to be combined by a constructed inventory with the
following parameters:

#### Constructed inventory input (source_vars)

```yaml
plugin: constructed
strict: true
groups:
  shutdown: resolved_state == "shutdown"
  shutdown_in_product_dev: resolved_state == "shutdown" and account_alias == "product_dev"
compose:
  resolved_state: state | default("running")
```

#### Limit value

```
shutdown_in_product_dev
```
