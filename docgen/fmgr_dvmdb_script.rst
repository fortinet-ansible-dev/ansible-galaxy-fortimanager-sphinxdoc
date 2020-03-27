:source: fmgr_dvmdb_script.py

:orphan:

.. _fmgr_dvmdb_script:

fmgr_dvmdb_script -- Script table.
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/dvmdb/adom/{adom}/script`
- `/dvmdb/global/script`
- `/dvmdb/script`
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
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Script table.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-head">parameters for method: [get]</span> - Script table.</li>
 <ul class="ul-self">
 <li><span class="li-head">expand member</span> - Fetch all or selected attributes of object members. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [content, desc, filter_build, filter_device, filter_hostname, filter_ostype, filter_osver, filter_platform, filter_serial, modification_time, name, target, type]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
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

    - name: REQUESTING /DVMDB/SCRIPT
      fmgr_dvmdb_script:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
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

    - name: REQUESTING /DVMDB/SCRIPT
      fmgr_dvmdb_script:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               expand member: <value of string>
               fields:
                 -
                    - <value in [content, desc, filter_build, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, object member, syntax]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script</span>  </li>
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



