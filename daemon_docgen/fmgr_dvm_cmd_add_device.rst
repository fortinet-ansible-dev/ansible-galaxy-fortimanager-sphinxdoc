:source: fmgr_dvm_cmd_add_device.py

:orphan:

.. _fmgr_dvm_cmd_add_device:

fmgr_dvm_cmd_add_device -- Add a device to the Device Manager database.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">dvm_cmd_add_device</span> - Add a device to the Device Manager database. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - Name or ID of the ADOM where the command is to be executed on. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">adm_pass</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">adm_usr</span> - <i>add real and promote device</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">desc</span> - <i>available for all operations</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device action</span> - Specify add device operations, or leave blank to add real device: <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">faz.quota</span> - <i>available for all operations</i>. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - <i>add real device only</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">meta fields</span> - <i>add real and model device</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mgmt_mode</span> - <i>add real and model device</i>. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unreg, fmg, faz, fmgfaz]</span> </li>
 <li><span class="li-head">mr</span> - <i>add model device only</i>. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - <i>required for all operations</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_type</span> - <i>add model device only</i>. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, fos, fsw, foc, fml, faz, fwb, fch, fct, log, fmg, fsa, fdd, fac]</span> </li>
 <li><span class="li-head">os_ver</span> - <i>add model device only</i>. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0]</span> </li>
 <li><span class="li-head">patch</span> - <i>add model device only</i>. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">platform_str</span> - <i>add model device only</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sn</span> - <i>add model device only</i>. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, create_task, nonblocking, log_dev]</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
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
    - name: Add a device to the Device Manager database.
      fmgr_dvm_cmd_add_device:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         dvm_cmd_add_device:
            adom: <value of string>
            device:
               adm_pass: <value of string>
               adm_usr: <value of string>
               desc: <value of string>
               device action: <value of string>
               faz.quota: <value of integer>
               ip: <value of string>
               meta fields: <value of string>
               mgmt_mode: <value in [unreg, fmg, faz, ...]>
               mr: <value of integer>
               name: <value of string>
               os_type: <value in [unknown, fos, fsw, ...]>
               os_ver: <value in [unknown, 0.0, 1.0, ...]>
               patch: <value of integer>
               platform_str: <value of string>
               sn: <value of string>
            flags:
              - none
              - create_task
              - nonblocking
              - log_dev
            groups:
              -
                  name: <value of string>
                  vdom: <value of string>



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



