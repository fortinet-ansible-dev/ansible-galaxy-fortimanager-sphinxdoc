:source: fmgr_system_logfetch_clientprofile.py

:orphan:

.. _fmgr_system_logfetch_clientprofile:

fmgr_system_logfetch_clientprofile -- Log-fetch client profile settings.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">system_logfetch_clientprofile</span> - Log-fetch client profile settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">client-adom</span> - Log-fetch client sides adom name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">data-range</span> - Data-range for fetched logs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [custom]</span>  <span class="li-normal">default: custom</span> </li>
 <li><span class="li-head">data-range-value</span> - Last n days or hours. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">device-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - Adom name. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 <li><span class="li-head">device</span> - Device name or Serial number. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 <li><span class="li-head">id</span> - Add or edit a device filter. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">vdom</span> - Vdom filters. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 </ul>
 <li><span class="li-head">end-time</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">id</span> - Log-fetch client profile ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">index-fetch-logs</span> - Enable/Disable indexing logs automatically after fetching logs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">log-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">field</span> - Field name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Log filter ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">oper</span> - Field filter operator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [=, !=, <, >, <=, >=, contain, not-contain, match]</span>  <span class="li-normal">default: =</span> </li>
 <li><span class="li-head">value</span> - Field filter operand or free-text matching expression. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log-filter-logic</span> - And/Or logic for log-filters. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [and, or]</span>  <span class="li-normal">default: or</span> </li>
 <li><span class="li-head">log-filter-status</span> - Enable/Disable log-filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">name</span> - Name of log-fetch client profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">secure-connection</span> - Enable/Disable protecting log-fetch connection with TLS/SSL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">server-adom</span> - Log-fetch server sides adom name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-ip</span> - Log-fetch server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">start-time</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sync-adom-config</span> - Enable/Disable sync adom related config. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">user</span> - Log-fetch server login username. <span class="li-normal">type: str</span> </li>
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
    - name: Log-fetch client profile settings.
      fmgr_system_logfetch_clientprofile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         state: <value in [present, absent]>
         system_logfetch_clientprofile:
            client-adom: <value of string>
            data-range: <value in [custom]>
            data-range-value: <value of integer>
            device-filter:
              -
                  adom: <value of string>
                  device: <value of string>
                  id: <value of integer>
                  vdom: <value of string>
            end-time: <value of string>
            id: <value of integer>
            index-fetch-logs: <value in [disable, enable]>
            log-filter:
              -
                  field: <value of string>
                  id: <value of integer>
                  oper: <value in [=, !=, <, ...]>
                  value: <value of string>
            log-filter-logic: <value in [and, or]>
            log-filter-status: <value in [disable, enable]>
            name: <value of string>
            password: <value of string>
            secure-connection: <value in [disable, enable]>
            server-adom: <value of string>
            server-ip: <value of string>
            start-time: <value of string>
            sync-adom-config: <value in [disable, enable]>
            user: <value of string>



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



