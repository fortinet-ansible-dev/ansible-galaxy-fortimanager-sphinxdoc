:source: fmgr_system_alertevent.py

:orphan:

.. _fmgr_system_alertevent:

fmgr_system_alertevent -- Alert events.
+++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">system_alertevent</span> - Alert events. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">alert-destination</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">from</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">smtp-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">snmp-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">syslog-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">to</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mail, snmp, syslog]</span> </li>
 </ul>
 <li><span class="li-head">enable-generic-text</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable]</span> </li>
 </ul>
 <li><span class="li-head">enable-severity-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable]</span> </li>
 </ul>
 <li><span class="li-head">event-time-period</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [0.5, 1, 3, 6, 12, 24, 72, 168]</span> </li>
 <li><span class="li-head">generic-text</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">num-events</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 5, 10, 50, 100]</span> </li>
 <li><span class="li-head">severity-filter</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, medium-high, medium, medium-low, low]</span> </li>
 <li><span class="li-head">severity-level-comp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [>=, =, <=]</span> </li>
 </ul>
 <li><span class="li-head">severity-level-logs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no-check, information, notify, warning, error, critical, alert, emergency]</span> </li>
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
    - name: Alert events.
      fmgr_system_alertevent:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         state: <value in [present, absent]>
         system_alertevent:
            alert-destination:
              -
                  from: <value of string>
                  smtp-name: <value of string>
                  snmp-name: <value of string>
                  syslog-name: <value of string>
                  to: <value of string>
                  type: <value in [mail, snmp, syslog]>
            enable-generic-text:
              - <value in [enable, disable]>
            enable-severity-filter:
              - <value in [enable, disable]>
            event-time-period: <value in [0.5, 1, 3, ...]>
            generic-text: <value of string>
            name: <value of string>
            num-events: <value in [1, 5, 10, ...]>
            severity-filter: <value in [high, medium-high, medium, ...]>
            severity-level-comp:
              - <value in [>=, =, <=]>
            severity-level-logs:
              - <value in [no-check, information, notify, ...]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
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



