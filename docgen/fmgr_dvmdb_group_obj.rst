:source: fmgr_dvmdb_group_obj.py

:orphan:

.. _fmgr_dvmdb_group_obj:

fmgr_dvmdb_group_obj -- Device group table.
+++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update, add]** the following FortiManager json-rpc urls.
- `/dvmdb/adom/{adom}/group/{group}`
- `/dvmdb/group/{group}`
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
 <li><span class="li-head">group</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Device group table.</li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 0</span></li>
 <ul class="ul-self">
 </ul>
 </ul>
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 1</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Device group table.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Device group table.</li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 0</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">desc</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, fos, fsw, foc, fml, faz, fwb, fch, fct, log, fmg, fsa, fdd, fac, fpx]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [normal, default, auto]</span>  <span class="li-normal">default: normal</span> </li>
 </ul>
 </ul>
 </ul>
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 1</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [add]</span> - Device group table.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /DVMDB/GROUP/{GROUP}
      fmgr_dvmdb_group_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [delete]>
         url_params:
            adom: <value in [none, global, custom dom]>
            group: <value of string>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>

    - name: REQUESTING /DVMDB/GROUP/{GROUP}
      fmgr_dvmdb_group_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            group: <value of string>
         params:
            -
               option: <value in [object member, chksum]>

    - name: REQUESTING /DVMDB/GROUP/{GROUP}
      fmgr_dvmdb_group_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            group: <value of string>
         params:
            -
               data:
                  desc: <value of string>
                  meta fields: <value of string>
                  name: <value of string>
                  os_type: <value in [unknown, fos, fsw, ...]>
                  type: <value in [normal, default, auto]>

    - name: REQUESTING /DVMDB/GROUP/{GROUP}
      fmgr_dvmdb_group_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            group: <value of string>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>

    - name: REQUESTING /DVMDB/GROUP/{GROUP}
      fmgr_dvmdb_group_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add]>
         url_params:
            adom: <value in [none, global, custom dom]>
            group: <value of string>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [delete, set, update]</span> </li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-return">return values collection 0</span></li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/group/{group}</span>  </li>
 </ul>
 </ul>
 <ul class="ul-self">
 <li><span class="li-return">return values collection 1</span></li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/group/{group}</span>  </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> desc </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> meta fields </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> os_type </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: normal</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/group/{group}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [add]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/group/{group}</span>  </li>
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



