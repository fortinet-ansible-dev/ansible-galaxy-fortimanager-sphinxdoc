:source: fmgr_fsp_vlan_dynamicmapping_dhcpserver.py

:orphan:

.. _fmgr_fsp_vlan_dynamicmapping_dhcpserver:

fmgr_fsp_vlan_dynamicmapping_dhcpserver
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
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vlan</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">fsp_vlan_dynamicmapping_dhcpserver</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">auto-configuration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">conflicted-ip-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tsig]</span> </li>
 <li><span class="li-head">ddns-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-keyname</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-server-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns-update</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-update-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">default-gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">enable</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">exclude-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">filename</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">forticlient-on-net-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, usrgrp]</span> </li>
 <li><span class="li-head">ip-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipsec-lease-hold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lease-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mac-acl-default-action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block]</span> </li>
 <li><span class="li-head">netmask</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">next-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">option1</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">option2</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">option3</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">option4</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">option5</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">option6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">code</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string, ip, fqdn]</span> </li>
 <li><span class="li-head">value</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">reserved-address</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block, reserved]</span> </li>
 <li><span class="li-head">circuit-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">circuit-id-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-id-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mac, option82]</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tftp-server</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">timezone</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]</span> </li>
 <li><span class="li-head">timezone-option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, default, specify]</span> </li>
 <li><span class="li-head">vci-match</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vci-string</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">wifi-ac1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-ac2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-ac3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: no description
      fmgr_fsp_vlan_dynamicmapping_dhcpserver:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vlan: <your own value>
         dynamic_mapping: <your own value>
         fsp_vlan_dynamicmapping_dhcpserver:
            auto-configuration: <value in [disable, enable]>
            conflicted-ip-timeout: <value of integer>
            ddns-auth: <value in [disable, tsig]>
            ddns-key: <value of string>
            ddns-keyname: <value of string>
            ddns-server-ip: <value of string>
            ddns-ttl: <value of integer>
            ddns-update: <value in [disable, enable]>
            ddns-update-override: <value in [disable, enable]>
            ddns-zone: <value of string>
            default-gateway: <value of string>
            dns-server1: <value of string>
            dns-server2: <value of string>
            dns-server3: <value of string>
            dns-service: <value in [default, specify, local]>
            domain: <value of string>
            enable: <value in [disable, enable]>
            exclude-range:
              -
                  end-ip: <value of string>
                  id: <value of integer>
                  start-ip: <value of string>
            filename: <value of string>
            forticlient-on-net-status: <value in [disable, enable]>
            id: <value of integer>
            interface: <value of string>
            ip-mode: <value in [range, usrgrp]>
            ip-range:
              -
                  end-ip: <value of string>
                  id: <value of integer>
                  start-ip: <value of string>
            ipsec-lease-hold: <value of integer>
            lease-time: <value of integer>
            mac-acl-default-action: <value in [assign, block]>
            netmask: <value of string>
            next-server: <value of string>
            ntp-server1: <value of string>
            ntp-server2: <value of string>
            ntp-server3: <value of string>
            ntp-service: <value in [default, specify, local]>
            option1: <value of string>
            option2: <value of string>
            option3: <value of string>
            option4: <value of string>
            option5: <value of string>
            option6: <value of string>
            options:
              -
                  code: <value of integer>
                  id: <value of integer>
                  ip: <value of string>
                  type: <value in [hex, string, ip, ...]>
                  value: <value of string>
            reserved-address:
              -
                  action: <value in [assign, block, reserved]>
                  circuit-id: <value of string>
                  circuit-id-type: <value in [hex, string]>
                  description: <value of string>
                  id: <value of integer>
                  ip: <value of string>
                  mac: <value of string>
                  remote-id: <value of string>
                  remote-id-type: <value in [hex, string]>
                  type: <value in [mac, option82]>
            server-type: <value in [regular, ipsec]>
            status: <value in [disable, enable]>
            tftp-server: <value of string>
            timezone: <value in [00, 01, 02, ...]>
            timezone-option: <value in [disable, default, specify]>
            vci-match: <value in [disable, enable]>
            vci-string: <value of string>
            wifi-ac1: <value of string>
            wifi-ac2: <value of string>
            wifi-ac3: <value of string>
            wins-server1: <value of string>
            wins-server2: <value of string>



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



