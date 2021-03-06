:source: fmgr_devprof_system_snmp_community.py

:orphan:

.. _fmgr_devprof_system_snmp_community:

fmgr_devprof_system_snmp_community -- SNMP community configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">devprof_system_snmp_community</span> - SNMP community configuration. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">events</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [cpu-high, mem-low, log-full, intf-ip, vpn-tun-up, vpn-tun-down, ha-switch, ha-hb-failure, ips-signature, ips-anomaly, av-virus, av-oversize, av-pattern, av-fragmented, fm-if-change, fm-conf-change, temperature-high, voltage-alert, ha-member-up, ha-member-down, ent-conf-change, av-conserve, av-bypass, av-oversize-passed, av-oversize-blocked, ips-pkg-update, power-supply-failure, amc-bypass, faz-disconnect, fan-failure, bgp-established, bgp-backward-transition, wc-ap-up, wc-ap-down, fswctl-session-up, fswctl-session-down, ips-fail-open, load-balance-real-server-down, device-new, enter-intf-bypass, exit-intf-bypass, per-cpu-high, power-blade-down, confsync_failure]</span> </li>
 <li><span class="li-head">hosts</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ha-direct</span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">host-type</span> - Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, query, trap]</span> </li>
 <li><span class="li-head">id</span> - Host entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the SNMP manager (host). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IPv4 address for SNMP traps. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">hosts6</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ha-direct</span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">host-type</span> - Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, query, trap]</span> </li>
 <li><span class="li-head">id</span> - Host6 entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ipv6</span> - SNMP manager IPv6 address prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ipv6</span> - Source IPv6 address for SNMP traps. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">id</span> - Community ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Community name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">query-v1-port</span> - SNMP v1 query port (default = 161). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">query-v1-status</span> - Enable/disable SNMP v1 queries. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">query-v2c-port</span> - SNMP v2c query port (default = 161). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">query-v2c-status</span> - Enable/disable SNMP v2c queries. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this SNMP community. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">trap-v1-lport</span> - SNMP v1 trap local port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v1-rport</span> - SNMP v1 trap remote port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v1-status</span> - Enable/disable SNMP v1 traps. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">trap-v2c-lport</span> - SNMP v2c trap local port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v2c-rport</span> - SNMP v2c trap remote port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v2c-status</span> - Enable/disable SNMP v2c traps. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: SNMP community configuration.
      fmgr_devprof_system_snmp_community:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         state: <value in [present, absent]>
         devprof_system_snmp_community:
            events:
              - cpu-high
              - mem-low
              - log-full
              - intf-ip
              - vpn-tun-up
              - vpn-tun-down
              - ha-switch
              - ha-hb-failure
              - ips-signature
              - ips-anomaly
              - av-virus
              - av-oversize
              - av-pattern
              - av-fragmented
              - fm-if-change
              - fm-conf-change
              - temperature-high
              - voltage-alert
              - ha-member-up
              - ha-member-down
              - ent-conf-change
              - av-conserve
              - av-bypass
              - av-oversize-passed
              - av-oversize-blocked
              - ips-pkg-update
              - power-supply-failure
              - amc-bypass
              - faz-disconnect
              - fan-failure
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
            hosts:
              -
                  ha-direct: <value in [disable, enable]>
                  host-type: <value in [any, query, trap]>
                  id: <value of integer>
                  ip: <value of string>
                  source-ip: <value of string>
            hosts6:
              -
                  ha-direct: <value in [disable, enable]>
                  host-type: <value in [any, query, trap]>
                  id: <value of integer>
                  ipv6: <value of string>
                  source-ipv6: <value of string>
            id: <value of integer>
            name: <value of string>
            query-v1-port: <value of integer>
            query-v1-status: <value in [disable, enable]>
            query-v2c-port: <value of integer>
            query-v2c-status: <value in [disable, enable]>
            status: <value in [disable, enable]>
            trap-v1-lport: <value of integer>
            trap-v1-rport: <value of integer>
            trap-v1-status: <value in [disable, enable]>
            trap-v2c-lport: <value of integer>
            trap-v2c-rport: <value of integer>
            trap-v2c-status: <value in [disable, enable]>



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



