:source: fmgr_application_list_entries.py

:orphan:

.. _fmgr_application_list_entries:

fmgr_application_list_entries -- Application list entries.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method of the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">list</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">application_list_entries</span> - Application list entries. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Pass or block traffic, or reset connection for traffic from this application. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block, reset]</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">behavior</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">category</span> - Category ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging for this application list. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-packet</span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">parameters</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Parameter ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">value</span> - Parameter value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">per-ip-shaper</span> - Per-IP traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">popularity</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [1, 2, 3, 4, 5]</span> </li>
 <li><span class="li-head">protocols</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">quarantine</span> - Quarantine method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, attacker]</span> </li>
 <li><span class="li-head">quarantine-expiry</span> - Duration of quarantine. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quarantine-log</span> - Enable/disable quarantine logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-count</span> - Count of the rate. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-duration</span> - Duration (sec) of the rate. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-mode</span> - Rate limit mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [periodical, continuous]</span> </li>
 <li><span class="li-head">rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip, dhcp-client-mac, dns-domain]</span> </li>
 <li><span class="li-head">risk</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">session-ttl</span> - Session TTL (0 = default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">shaper</span> - Traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">shaper-reverse</span> - Reverse traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sub-category</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">technology</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">vendor</span> - No description for the parameter <span class="li-normal">type: str</span></li>
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
    - name: Application list entries.
      fmgr_application_list_entries:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         list: <your own value>
         state: <value in [present, absent]>
         application_list_entries:
            action: <value in [pass, block, reset]>
            application: <value of integer>
            behavior: <value of string>
            category: <value of string>
            id: <value of integer>
            log: <value in [disable, enable]>
            log-packet: <value in [disable, enable]>
            parameters:
              -
                  id: <value of integer>
                  value: <value of string>
            per-ip-shaper: <value of string>
            popularity:
              - 1
              - 2
              - 3
              - 4
              - 5
            protocols: <value of string>
            quarantine: <value in [none, attacker]>
            quarantine-expiry: <value of string>
            quarantine-log: <value in [disable, enable]>
            rate-count: <value of integer>
            rate-duration: <value of integer>
            rate-mode: <value in [periodical, continuous]>
            rate-track: <value in [none, src-ip, dest-ip, ...]>
            risk: <value of integer>
            session-ttl: <value of integer>
            shaper: <value of string>
            shaper-reverse: <value of string>
            sub-category: <value of integer>
            technology: <value of string>
            vendor: <value of string>



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



