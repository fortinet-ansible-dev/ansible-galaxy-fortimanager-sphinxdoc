:source: fmgr_fsp_vlan_interface_ipv6.py

:orphan:

.. _fmgr_fsp_vlan_interface_ipv6:

fmgr_fsp_vlan_interface_ipv6
++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vlan</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">fsp_vlan_interface_ipv6</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">autoconf</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-client-options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span> </li>
 <li><span class="li-head">dhcp6-information-request</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-delegation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-plt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-vlt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span> </li>
 <li><span class="li-head">ip6-address</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap]</span> </li>
 <li><span class="li-head">ip6-default-life</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-dns-server-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-hop-limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-link-mtu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-manage-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-max-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-min-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span> </li>
 <li><span class="li-head">ip6-other-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-reachable-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-retrans-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-send-adv</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-upstream-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cga-modifier</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [basic, SEND-compatible]</span> </li>
 <li><span class="li-head">nd-security-level</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-delta</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-fuzz</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip6_link_local</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vrrp-virtual-mac6</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
      fmgr_fsp_vlan_interface_ipv6:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vlan: <your own value>
         fsp_vlan_interface_ipv6:
            autoconf: <value in [disable, enable]>
            dhcp6-client-options:
              - rapid
              - iapd
              - iana
              - dns
              - dnsname
            dhcp6-information-request: <value in [disable, enable]>
            dhcp6-prefix-delegation: <value in [disable, enable]>
            dhcp6-prefix-hint: <value of string>
            dhcp6-prefix-hint-plt: <value of integer>
            dhcp6-prefix-hint-vlt: <value of integer>
            dhcp6-relay-ip: <value of string>
            dhcp6-relay-service: <value in [disable, enable]>
            dhcp6-relay-type: <value in [regular]>
            ip6-address: <value of string>
            ip6-allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - capwap
            ip6-default-life: <value of integer>
            ip6-dns-server-override: <value in [disable, enable]>
            ip6-hop-limit: <value of integer>
            ip6-link-mtu: <value of integer>
            ip6-manage-flag: <value in [disable, enable]>
            ip6-max-interval: <value of integer>
            ip6-min-interval: <value of integer>
            ip6-mode: <value in [static, dhcp, pppoe, ...]>
            ip6-other-flag: <value in [disable, enable]>
            ip6-reachable-time: <value of integer>
            ip6-retrans-time: <value of integer>
            ip6-send-adv: <value in [disable, enable]>
            ip6-subnet: <value of string>
            ip6-upstream-interface: <value of string>
            nd-cert: <value of string>
            nd-cga-modifier: <value of string>
            nd-mode: <value in [basic, SEND-compatible]>
            nd-security-level: <value of integer>
            nd-timestamp-delta: <value of integer>
            nd-timestamp-fuzz: <value of integer>
            vrip6_link_local: <value of string>
            vrrp-virtual-mac6: <value in [disable, enable]>



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



