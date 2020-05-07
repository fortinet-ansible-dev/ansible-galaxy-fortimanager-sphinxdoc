:source: fmgr_securityconsole_install_package.py

:orphan:

.. _fmgr_securityconsole_install_package:

fmgr_securityconsole_install_package -- Copy and install a policy package to devices.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[exec]** the following FortiManager json-rpc urls.
- `/securityconsole/install/package`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">parameters for method: [exec]</span> - Copy and install a policy package to devices.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - Source ADOM name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">adom_rev_comments</span> - If "generate_rev" flag is set, the comment for the new ADOM revision. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">adom_rev_name</span> - If "generate_rev" flag is set, the name for the new ADOM revision. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dev_rev_comments</span> - Comments for the device configuration revision that will be generated during install. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, cp_all_objs, preview, generate_rev, copy_assigned_pkg, unassign, ifpolicy_only, no_ifpolicy, objs_only, auto_lock_ws, check_pkg_st, copy_only]</span> </li>
 </ul>
 <li><span class="li-head">pkg</span> - Source package path and name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

   - To run in workspace mode, the paremeter workspace_locking_adom must be included in the task

Examples
--------

.. code-block:: yaml+jinja

 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /SECURITYCONSOLE/INSTALL/PACKAGE
      fmgr_securityconsole_install_package:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [exec]>
         params:
            -
               data:
                  adom: <value of string>
                  adom_rev_comments: <value of string>
                  adom_rev_name: <value of string>
                  dev_rev_comments: <value of string>
                  flags:
                    - <value in [none, cp_all_objs, preview, ...]>
                  pkg: <value of string>
                  scope:
                    -
                        name: <value of string>
                        vdom: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [exec]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> task </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /securityconsole/install/package</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



