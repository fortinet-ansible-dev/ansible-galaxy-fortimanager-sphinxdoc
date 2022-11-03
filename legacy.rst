Migrate Legacy Playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~

This document targets incompatible playbooks written for FortiManager
Galaxy collections earlier than ``1.0.5``.

Detect Compatiblity Issue
^^^^^^^^^^^^^^^^^^^^^^^^^

When runninng legacy playbooks with newer FortiManager collection, the
module will fail and an error message will remind you:

::

    failed: [fortimanager01] => {
        "changed": false,
        "module_stderr": "Legacy playbook detected, please revise the playbook or install latest legacy fortimanager galaxy collection: #ansible-galaxy collection install -f fortinet.fortimanager:1.0.5",
        "module_stdout": "",
        "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error",
        "rc": 1
    }

There are two ways to resolve this issue:

 - Continue to use “legacy” playbook format, with a FortiManager Collection <= 1.0.5
 - Convert playbooks to FortiManager Collection 1.0.4+ schema with the newest version of the collection.


Tweak The Playbook
^^^^^^^^^^^^^^^^^^

Legacy FortiManager collection requires the playbook has a parameter ``method``,
with newer FortiManager collection, it's presented with optional
statement: ``state: [present, absent]``.

Lagecy FortiManager collection has explicit declaration: ``url_params``,
it's omitted in newer collection, of course, the parameters themselves
have indentations advanced.

Legacy FortiManager collection has statement: ``params`` ->
``data array`` -> ``body array``. In newer collection, all them are
removed and the module name without prefix ``fmgr_`` is here as the top
level parameter name.

An example is as below:

::

    - name: create policy in the object      |   - name: create policy in the object
      fmgr_pkg_firewall_policy:              |     fmgr_pkg_firewall_policy:
        method: "set"                        |       adom: "{{ policy_adom }}"
        url_params:                          |       pkg: "{{ policy_package_name }}"
            adom: "{{ policy_adom }}"        |       state: 'present'
            pkg: "{{ policy_package_name }}" |       pkg_firewall_policy:
        params:                              |             name: "{{ item.name }}"
          - data:                            |             policyid: "{{ item.id  }}"
            - name: "{{ item.name }}"        |             action: "{{ item.action }}"
              policyid: "{{ item.id  }}"     |             srcintf: "any"
              action: "{{ item.action }}"    |             dstintf: "any"
              srcintf: "any"                 |             srcaddr: "{{ item.src }}"
              dstintf: "any"                 |             dstaddr: "{{ item.dst }}"
              srcaddr: "{{ item.src }}"      |             service: "{{ item.service }}"
              dstaddr: "{{ item.dst }}"      |             schedule: "{{ item.schedule }}"
              service: "{{ item.service }}"  |     register: policyinfo
              schedule: "{{ item.schedule }}"|     ignore_errors: true
      register: policyinfo                   |     with_items: "{{ policy_array }}"
      ignore_errors: true                    |
      with_items: "{{ policy_array }}"       |


