:source: fmgr_devprof_system_snmp_user.py

:orphan:

.. _fmgr_devprof_system_snmp_user:

fmgr_devprof_system_snmp_user -- SNMP user configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof_system_snmp_user</span> - SNMP user configuration. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">auth-proto</span> - Authentication protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [md5, sha]</span> </li>
 <li><span class="li-head">auth-pwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">events</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [cpu-high, mem-low, log-full, intf-ip, vpn-tun-up, vpn-tun-down, ha-switch, fm-conf-change, ips-signature, ips-anomaly, temperature-high, voltage-alert, av-virus, av-oversize, av-pattern, av-fragmented, ha-hb-failure, fan-failure, ha-member-up, ha-member-down, ent-conf-change, av-conserve, av-bypass, av-oversize-passed, av-oversize-blocked, ips-pkg-update, fm-if-change, power-supply-failure, amc-bypass, faz-disconnect, bgp-established, bgp-backward-transition, wc-ap-up, wc-ap-down, fswctl-session-up, fswctl-session-down, ips-fail-open, load-balance-real-server-down, device-new, enter-intf-bypass, exit-intf-bypass, per-cpu-high, power-blade-down, confsync_failure]</span> </li>
 <li><span class="li-head">ha-direct</span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - SNMP user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">notify-hosts</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">notify-hosts6</span> - IPv6 SNMP managers to send notifications (traps) to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priv-proto</span> - Privacy (encryption) protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aes, des, aes256, aes256cisco]</span> </li>
 <li><span class="li-head">priv-pwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">queries</span> - Enable/disable SNMP queries for this user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">query-port</span> - SNMPv3 query port (default = 161). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-level</span> - Security level for message authentication and encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no-auth-no-priv, auth-no-priv, auth-priv]</span> </li>
 <li><span class="li-head">source-ip</span> - Source IP for SNMP trap. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ipv6</span> - Source IPv6 for SNMP trap. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this SNMP user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">trap-lport</span> - SNMPv3 local trap port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-rport</span> - SNMPv3 trap remote port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-status</span> - Enable/disable traps for this SNMP user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: SNMP user configuration.
      fmgr_devprof_system_snmp_user:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         state: <value in [present, absent]>
         devprof_system_snmp_user:
            auth-proto: <value in [md5, sha]>
            auth-pwd: <value of string>
            events:
              - cpu-high
              - mem-low
              - log-full
              - intf-ip
              - vpn-tun-up
              - vpn-tun-down
              - ha-switch
              - fm-conf-change
              - ips-signature
              - ips-anomaly
              - temperature-high
              - voltage-alert
              - av-virus
              - av-oversize
              - av-pattern
              - av-fragmented
              - ha-hb-failure
              - fan-failure
              - ha-member-up
              - ha-member-down
              - ent-conf-change
              - av-conserve
              - av-bypass
              - av-oversize-passed
              - av-oversize-blocked
              - ips-pkg-update
              - fm-if-change
              - power-supply-failure
              - amc-bypass
              - faz-disconnect
              - bgp-established
              - bgp-backward-transition
              - wc-ap-up
              - wc-ap-down
              - fswctl-session-up
              - fswctl-session-down
              - ips-fail-open
              - load-balance-real-server-down
              - device-new
              - enter-intf-bypass
              - exit-intf-bypass
              - per-cpu-high
              - power-blade-down
              - confsync_failure
            ha-direct: <value in [disable, enable]>
            name: <value of string>
            notify-hosts: <value of string>
            notify-hosts6: <value of string>
            priv-proto: <value in [aes, des, aes256, ...]>
            priv-pwd: <value of string>
            queries: <value in [disable, enable]>
            query-port: <value of integer>
            security-level: <value in [no-auth-no-priv, auth-no-priv, auth-priv]>
            source-ip: <value of string>
            source-ipv6: <value of string>
            status: <value in [disable, enable]>
            trap-lport: <value of integer>
            trap-rport: <value of integer>
            trap-status: <value in [disable, enable]>



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



