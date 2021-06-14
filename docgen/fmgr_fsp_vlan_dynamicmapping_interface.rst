:source: fmgr_fsp_vlan_dynamicmapping_interface.py

:orphan:

.. _fmgr_fsp_vlan_dynamicmapping_interface:

fmgr_fsp_vlan_dynamicmapping_interface
++++++++++++++++++++++++++++++++++++++

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



FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <br>
 <table>
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>fsp_vlan_dynamicmapping_interface</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 </tr>
 </table>
 <p>



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
 <li><span class="li-head">fsp_vlan_dynamicmapping_interface</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlanid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp-relay-agent-option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">dhcp-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span> </li>
 <li><span class="li-head">ipv6</span> <span class="li-normal">type: dict</span> </li>
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
 <li><span class="li-head">ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric]</span> </li>
 <li><span class="li-head">ip6-default-life</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-delegated-prefix-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">onlink-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">prefix-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rdnss</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">rdnss-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [delegated, default, specify]</span> </li>
 <li><span class="li-head">subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">upstream-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ip6-dns-server-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-extra-addr</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">prefix</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ip6-hop-limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-link-mtu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-manage-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-max-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-min-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span> </li>
 <li><span class="li-head">ip6-other-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-prefix-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dnssl</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">onlink-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">preferred-life-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">prefix</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rdnss</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">valid-life-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
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
 <li><span class="li-head">vrrp6</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">adv-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preempt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vrdst6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vrgrp</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">cli-conn6-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">icmp6-send-redirect</span> - Enable/disable sending of ICMPv6 redirects. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">interface-identifier</span> - IPv6 interface identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-prefix-mode</span> - Assigning a prefix from DHCP or RA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhcp6, ra]</span> </li>
 <li><span class="li-head">ra-send-mtu</span> - Enable/disable sending link MTU in RA packet. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">unique-autoconf-addr</span> - Enable/disable unique auto config address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">secondary-IP</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">secondaryip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric]</span> </li>
 <li><span class="li-head">detectprotocol</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> </li>
 <li><span class="li-head">detectserver</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gwdetect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ha-priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ping-serv-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
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
    - name: no description
      fmgr_fsp_vlan_dynamicmapping_interface:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vlan: <your own value>
         dynamic_mapping: <your own value>
         fsp_vlan_dynamicmapping_interface:
            ip: <value of string>
            vlanid: <value of integer>
            dhcp-relay-agent-option: <value in [disable, enable]>
            dhcp-relay-ip: <value of string>
            dhcp-relay-service: <value in [disable, enable]>
            dhcp-relay-type: <value in [regular, ipsec]>
            ipv6:
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
                 - fabric
               ip6-default-life: <value of integer>
               ip6-delegated-prefix-list:
                 -
                     autonomous-flag: <value in [disable, enable]>
                     onlink-flag: <value in [disable, enable]>
                     prefix-id: <value of integer>
                     rdnss: <value of string>
                     rdnss-service: <value in [delegated, default, specify]>
                     subnet: <value of string>
                     upstream-interface: <value of string>
               ip6-dns-server-override: <value in [disable, enable]>
               ip6-extra-addr:
                 -
                     prefix: <value of string>
               ip6-hop-limit: <value of integer>
               ip6-link-mtu: <value of integer>
               ip6-manage-flag: <value in [disable, enable]>
               ip6-max-interval: <value of integer>
               ip6-min-interval: <value of integer>
               ip6-mode: <value in [static, dhcp, pppoe, ...]>
               ip6-other-flag: <value in [disable, enable]>
               ip6-prefix-list:
                 -
                     autonomous-flag: <value in [disable, enable]>
                     dnssl: <value of string>
                     onlink-flag: <value in [disable, enable]>
                     preferred-life-time: <value of integer>
                     prefix: <value of string>
                     rdnss: <value of string>
                     valid-life-time: <value of integer>
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
               vrrp6:
                 -
                     accept-mode: <value in [disable, enable]>
                     adv-interval: <value of integer>
                     preempt: <value in [disable, enable]>
                     priority: <value of integer>
                     start-time: <value of integer>
                     status: <value in [disable, enable]>
                     vrdst6: <value of string>
                     vrgrp: <value of integer>
                     vrid: <value of integer>
                     vrip6: <value of string>
               cli-conn6-status: <value of integer>
               icmp6-send-redirect: <value in [disable, enable]>
               interface-identifier: <value of string>
               ip6-prefix-mode: <value in [dhcp6, ra]>
               ra-send-mtu: <value in [disable, enable]>
               unique-autoconf-addr: <value in [disable, enable]>
            secondary-IP: <value in [disable, enable]>
            secondaryip:
              -
                  allowaccess:
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                  detectprotocol:
                    - ping
                    - tcp-echo
                    - udp-echo
                  detectserver: <value of string>
                  gwdetect: <value in [disable, enable]>
                  ha-priority: <value of integer>
                  id: <value of integer>
                  ip: <value of string>
                  ping-serv-status: <value of integer>
                  seq: <value of integer>



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



