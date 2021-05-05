:source: fmgr_vpnmgr_node.py

:orphan:

.. _fmgr_vpnmgr_node:

fmgr_vpnmgr_node -- VPN node for VPN Manager.
+++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vpnmgr_node</span> - VPN node for VPN Manager. Must specify vpntable and scope member. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">add-route</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">assign-ip</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">assign-ip-from</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, usrgrp, dhcp, name]</span> </li>
 <li><span class="li-head">authpasswd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">authusr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">authusrgrp</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auto-configuration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">automatic_routing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">banner</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">default-gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dns-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, manual]</span> </li>
 <li><span class="li-head">dns-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extgw</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extgw_hubip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extgw_p2_per_net</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">extgwip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hub_iface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">iface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipsec-lease-hold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ipv4-dns-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-dns-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-dns-server3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-exclude-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipv4-netmask</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-split-include</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-wins-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-wins-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">local-gw</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">localid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mode-cfg</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mode-cfg-ip-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [4, 6]</span> </li>
 <li><span class="li-head">net-device</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">peer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">peergrp</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">peerid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">peertype</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, one, dialup, peer, peergrp]</span> </li>
 <li><span class="li-head">protected_subnet</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">public-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">role</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hub, spoke]</span> </li>
 <li><span class="li-head">route-overlap</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [use-old, use-new, allow]</span> </li>
 <li><span class="li-head">spoke-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">summary_addr</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">tunnel-search</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [selectors, nexthop]</span> </li>
 <li><span class="li-head">unity-support</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">usrgrp</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpn-interface-priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vpn-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpntable</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">xauthtype</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, client, pap, chap, auto]</span> </li>
 <li><span class="li-head">scope member</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - name of scope member <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - vdom of scope member <span class="li-normal">type: str</span> </li>
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
    - name: VPN node for VPN Manager. Must specify vpntable and scope member.
      fmgr_vpnmgr_node:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         vpnmgr_node:
            add-route: <value in [disable, enable]>
            assign-ip: <value in [disable, enable]>
            assign-ip-from: <value in [range, usrgrp, dhcp, ...]>
            authpasswd: <value of string>
            authusr: <value of string>
            authusrgrp: <value of string>
            auto-configuration: <value in [disable, enable]>
            automatic_routing: <value in [disable, enable]>
            banner: <value of string>
            default-gateway: <value of string>
            dhcp-server: <value in [disable, enable]>
            dns-mode: <value in [auto, manual]>
            dns-service: <value in [default, specify, local]>
            domain: <value of string>
            extgw: <value of string>
            extgw_hubip: <value of string>
            extgw_p2_per_net: <value in [disable, enable]>
            extgwip: <value of string>
            hub_iface: <value of string>
            id: <value of integer>
            iface: <value of string>
            ip-range:
              -
                  end-ip: <value of string>
                  id: <value of integer>
                  start-ip: <value of string>
            ipsec-lease-hold: <value of integer>
            ipv4-dns-server1: <value of string>
            ipv4-dns-server2: <value of string>
            ipv4-dns-server3: <value of string>
            ipv4-end-ip: <value of string>
            ipv4-exclude-range:
              -
                  end-ip: <value of string>
                  id: <value of integer>
                  start-ip: <value of string>
            ipv4-netmask: <value of string>
            ipv4-split-include: <value of string>
            ipv4-start-ip: <value of string>
            ipv4-wins-server1: <value of string>
            ipv4-wins-server2: <value of string>
            local-gw: <value of string>
            localid: <value of string>
            mode-cfg: <value in [disable, enable]>
            mode-cfg-ip-version: <value in [4, 6]>
            net-device: <value in [disable, enable]>
            peer: <value of string>
            peergrp: <value of string>
            peerid: <value of string>
            peertype: <value in [any, one, dialup, ...]>
            protected_subnet:
              -
                  addr: <value of string>
                  seq: <value of integer>
            public-ip: <value of string>
            role: <value in [hub, spoke]>
            route-overlap: <value in [use-old, use-new, allow]>
            spoke-zone: <value of string>
            summary_addr:
              -
                  addr: <value of string>
                  priority: <value of integer>
                  seq: <value of integer>
            tunnel-search: <value in [selectors, nexthop]>
            unity-support: <value in [disable, enable]>
            usrgrp: <value of string>
            vpn-interface-priority: <value of integer>
            vpn-zone: <value of string>
            vpntable: <value of string>
            xauthtype: <value in [disable, client, pap, ...]>
            scope member:
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



