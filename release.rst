
Release Notes
==============================




Release Galaxy 2.0.0
~~~~~~~~~~~~~~~~~~~~~~

|


Release Target
---------------

FortiManager version: ``v6.0.x``

Module Category
----------------

+-------------------------------+--------------------------+---------------------------------+
| Module Category               | Supported JPRC methods   | Location                        |
+===============================+==========================+=================================+
| Object Oriented Modules       | add/update(set)/delete   | `ref <modules.html>`__          |
+-------------------------------+--------------------------+---------------------------------+
| Facts Gathering Modules       | get                      | `ref <fact.html>`__             |
+-------------------------------+--------------------------+---------------------------------+
| Object Manipulating Modules   | move/clone               | `ref <objman.html>`__           |
+-------------------------------+--------------------------+---------------------------------+
| Daemon Modules                | exec                     | `ref <daemon_modules.html>`__   |
+-------------------------------+--------------------------+---------------------------------+
| Generic Modules               | (all methods)            | `ref <generic.html>`__          |
+-------------------------------+--------------------------+---------------------------------+

Features
------------

-  Full FortiManager JRPC URLs coverage (more than 700 modules).
-  Smooth migration for legacy playbooks.
-  Flexible error handling mechanism.
-  Multiple workspace modes supported.
-  Module quick workaround technique: ``bypass_validation``
-  Specilized modules: ``fmgr_fact``, ``fmgr_move``, ``fmgr_clone`` and
   ``fmgr_generic``.
-  Runnable examples `repository <example.html>`__.


Release Galaxy 2.0.1
~~~~~~~~~~~~~~~~~~~~~

|

Release Target
---------------

FortiManager version: ``v6.0.x``

Features & Bugfix
------------------

- Fix attribute:type for module: ``fmgr_firewall_addresss`` and ``fmgr_firewall_addresss6``.
- Fix https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues/9
- Fix mantis #0672125
- Fix https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues/11
- Fix https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues/12
- ``fmgr_fact`` module supports full selectors.
- Remove all default value in module argument specification to avoid confusion
- Fix module ``fmgr_templategroup`` attribute: member
