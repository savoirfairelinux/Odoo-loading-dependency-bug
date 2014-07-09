Odoo-loding-dependency-bug
==========================

4 modules which demonstrate a bug in odoo loading

## Description

Odoo doesn't seem to follow the correct dependency graph when installing and
testing modules which depend on each other. Instead, it seems to install them
in alphabetical order if their dependencies are satisfied.

This causes a problem when trying to write good unittests for project under one
module which depends on two module which will conflict with each-other if
initialized in the wrong order.

This repo has 4 modules:

### **parent_module**

Topmost module, dependency list lists **b_module** and **a_module** in that order

### **b_module** 

Has a unittest which tests the module in **parent_module** and with whatever 
modifications to the model are made in **grandchild_module**.
This model only depends on **grandchild_module** and is meant to be functional 
on its own, independently from **a_module**, but can work with it installed.
The unittest, however do not take into account **a_module** as it is not a 
dependency.

### **a_module**:

Add a required field to the model in **grandchild_module**.
Lists only **grandchild_module** as its dependencies and is meant to be 
functional on its own, independently from **b_module**, but can work with it.

### **grandchild_module** 

Defines an example module. Has no dependencies.

## How to reproduce

Install **parent_module** with tests enabled using

```bash
openerp-server -d test -i parent_module --test-enable --log-level=test
```

## Expected behaviour

Odoo goes down the dependency graph finding that once **grandchild_module** is
installed, **b_module**, **a_module** can be installed and installs them in the
order defined by **parent_module**.

When **b_module** installs, it runs its tests and passes. Then, **a_module**
installs and adds the required field.

## Actual behaviour

Odoo goes down the dependency graph finding that once **grandchild_module** is
installed, **b_module**, **a_module** can be installed and installs them in
alphabetical order.

That means **a_module** is installed first, adding a required field, then 
**b_module** is installed and triggers its tests. The tests run into an 
exception due to the required field being set from **a_module**. 
