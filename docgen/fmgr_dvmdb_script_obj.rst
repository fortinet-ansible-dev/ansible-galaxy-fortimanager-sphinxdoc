:source: fmgr_dvmdb_script_obj.py

:orphan:

.. _fmgr_dvmdb_script_obj:

fmgr_dvmdb_script_obj -- Script table.
++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update, add]** the following FortiManager json-rpc urls.
- `/dvmdb/adom/{adom}/script/{script}`
- `/dvmdb/global/script/{script}`
- `/dvmdb/script/{script}`
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
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">script</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Script table.</li>
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
 <li><span class="li-head">parameters for method: [get]</span> - Script table.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Script table.</li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 0</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">content</span> - The full content of the script result log. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">desc</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter_build</span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">filter_device</span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">filter_hostname</span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter_ostype</span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, fos]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">filter_osver</span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 4.00, 5.00]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">filter_platform</span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter_serial</span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">modification_time</span> - It is a read-only attribute indicating the time when the script was created or modified. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">script_schedule</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">datetime</span> - Indicates the date and time of the schedule. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">day_of_week</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, sun, mon, tue, wed, thu, fri, sat]</span>  <span class="li-normal">default: sun</span> </li>
 <li><span class="li-head">device</span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">run_on_db</span> - Indicates if the scheduled script should be executed on device database. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, onetime, daily, weekly, monthly]</span> </li>
 </ul>
 <li><span class="li-head">target</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [device_database, remote_device, adom_database]</span>  <span class="li-normal">default: device_database</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [cli, tcl, cligrp]</span> </li>
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
 <li><span class="li-head">parameters for method: [add]</span> - Script table.</li>
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

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}
      fmgr_dvmdb_script_obj:
         method: <value in [delete]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}
      fmgr_dvmdb_script_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
         params:
            -
               option: <value in [object member, chksum]>

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}
      fmgr_dvmdb_script_obj:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
         params:
            -
               data:
                  content: <value of string>
                  desc: <value of string>
                  filter_build: <value of integer>
                  filter_device: <value of integer>
                  filter_hostname: <value of string>
                  filter_ostype: <value in [unknown, fos] default: 'unknown'>
                  filter_osver: <value in [unknown, 4.00, 5.00] default: 'unknown'>
                  filter_platform: <value of string>
                  filter_serial: <value of string>
                  modification_time: <value of string>
                  name: <value of string>
                  script_schedule:
                    -
                        datetime: <value of string>
                        day_of_week: <value in [unknown, sun, mon, ...] default: 'sun'>
                        device: <value of integer>
                        name: <value of string>
                        run_on_db: <value in [disable, enable] default: 'disable'>
                        type: <value in [auto, onetime, daily, ...]>
                  target: <value in [device_database, remote_device, adom_database] default: 'device_database'>
                  type: <value in [cli, tcl, cligrp]>

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}
      fmgr_dvmdb_script_obj:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}
      fmgr_dvmdb_script_obj:
         method: <value in [add]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script/{script}</span>  </li>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script/{script}</span>  </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> content </span> - The full content of the script result log. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> desc </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter_build </span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> filter_device </span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> filter_hostname </span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter_ostype </span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> filter_osver </span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> filter_platform </span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter_serial </span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> modification_time </span> - It is a read-only attribute indicating the time when the script was created or modified. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> script_schedule </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> datetime </span> - Indicates the date and time of the schedule. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> day_of_week </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: sun</span>  </li>
 <li> <span class="li-return"> device </span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> run_on_db </span> - Indicates if the scheduled script should be executed on device database. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> target </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: device_database</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script/{script}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [add]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script/{script}</span>  </li>
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



