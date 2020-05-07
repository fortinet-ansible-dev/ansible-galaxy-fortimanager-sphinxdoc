:source: fmgr_pm_pkg_obj.py

:orphan:

.. _fmgr_pm_pkg_obj:

fmgr_pm_pkg_obj
+++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/pkg/adom/{adom}/{pkg_path}`
- `/pm/pkg/global/{pkg_path}`
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
 <li><span class="li-head">loose_validation</span> - Do parameter validation in a loose way <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal">default: false</span>  </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">pkg_path</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - </li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [name, obj ver, oid, scope member, type]</span> </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj ver</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">oid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">package setting</span> <li><span class="li-head">central-nat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">consolidated-firewall-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fwpolicy-implicit-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fwpolicy6-implicit-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">inspection-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">ngfw-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [profile-based, policy-based]</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">scope member</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pkg, folder]</span> </li>
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

    - name: REQUESTING /PM/PKG/{PKG_PATH}
      fmgr_pm_pkg_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg_path: <value of string>
         params:
            -
               fields:
                 -
                    - <value in [name, obj ver, oid, ...]>

    - name: REQUESTING /PM/PKG/{PKG_PATH}
      fmgr_pm_pkg_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg_path: <value of string>
         params:
            -
               data:
                  name: <value of string>
                  obj ver: <value of integer>
                  oid: <value of integer>
                  package setting:
                     central-nat: <value in [disable, enable]>
                     consolidated-firewall-mode: <value in [disable, enable]>
                     fwpolicy-implicit-log: <value in [disable, enable]>
                     fwpolicy6-implicit-log: <value in [disable, enable]>
                     inspection-mode: <value in [proxy, flow]>
                     ngfw-mode: <value in [profile-based, policy-based]>
                     ssl-ssh-profile: <value of string>
                  scope member:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  type: <value in [pkg, folder]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/pkg/adom/{adom}/{pkg_path}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> obj ver </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> oid </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> package setting </span> <li> <span class="li-return"> central-nat </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> consolidated-firewall-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fwpolicy-implicit-log </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fwpolicy6-implicit-log </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inspection-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ngfw-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-ssh-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> scope member </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/pkg/adom/{adom}/{pkg_path}</span>  </li>
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



