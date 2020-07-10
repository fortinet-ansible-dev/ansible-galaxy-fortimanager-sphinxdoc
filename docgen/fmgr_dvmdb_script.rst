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

- This module is able to configure a FortiManager device.
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0.


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.9.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">dvmdb_script</span> - Script table. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">content</span> - The full content of the script result log. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">desc</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter_build</span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">filter_device</span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">filter_hostname</span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter_ostype</span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, fos]</span> </li>
 <li><span class="li-head">filter_osver</span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 4.00, 5.00]</span> </li>
 <li><span class="li-head">filter_platform</span> - The value will be ignored in add/set/update requests if filter_ostype is not set. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter_serial</span> - The value has no effect if target is "adom_database". <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">modification_time</span> - It is a read-only attribute indicating the time when the script was created or modified. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">script_schedule</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">datetime</span> - Indicates the date and time of the schedule. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">day_of_week</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, sun, mon, tue, wed, thu, fri, sat]</span> </li>
 <li><span class="li-head">device</span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">run_on_db</span> - Indicates if the scheduled script should be executed on device database. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, onetime, daily, weekly, monthly]</span> </li>
 </ul>
 <li><span class="li-head">target</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [device_database, remote_device, adom_database]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [cli, tcl, cligrp]</span> </li>
 </ul>
 </ul>






Notes
-----
.. note::

   - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.

   - To create or update an object, use state: present directive.

   - To delete an object, use state: absent directive

   - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

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
    - name: Script table.
      fmgr_dvmdb_script:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         dvmdb_script:
            content: <value of string>
            desc: <value of string>
            filter_build: <value of integer>
            filter_device: <value of integer>
            filter_hostname: <value of string>
            filter_ostype: <value in [unknown, fos]>
            filter_osver: <value in [unknown, 4.00, 5.00]>
            filter_platform: <value of string>
            filter_serial: <value of string>
            modification_time: <value of string>
            name: <value of string>
            script_schedule:
              -
                  datetime: <value of string>
                  day_of_week: <value in [unknown, sun, mon, ...]>
                  device: <value of integer>
                  name: <value of string>
                  run_on_db: <value in [disable, enable]>
                  type: <value in [auto, onetime, daily, ...]>
            target: <value in [device_database, remote_device, adom_database]>
            type: <value in [cli, tcl, cligrp]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
 <li> <span class="li-return">response_data</span> - The data body of the api response <span class="li-normal">returned: optional</span> <span class="li-normal">type: list or dict</span></li>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



