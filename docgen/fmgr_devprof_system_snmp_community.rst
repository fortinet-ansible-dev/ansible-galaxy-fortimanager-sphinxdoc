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

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/system/snmp/community`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">devprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - SNMP community configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">events</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [cpu-high, mem-low, log-full, intf-ip, vpn-tun-up, vpn-tun-down, ha-switch, ha-hb-failure, ips-signature, ips-anomaly, av-virus, av-oversize, av-pattern, av-fragmented, fm-if-change, fm-conf-change, temperature-high, voltage-alert, ha-member-up, ha-member-down, ent-conf-change, av-conserve, av-bypass, av-oversize-passed, av-oversize-blocked, ips-pkg-update, power-supply-failure, amc-bypass, faz-disconnect, fan-failure, bgp-established, bgp-backward-transition, wc-ap-up, wc-ap-down, fswctl-session-up, fswctl-session-down, ips-fail-open, load-balance-real-server-down, device-new, enter-intf-bypass, exit-intf-bypass, per-cpu-high, power-blade-down, confsync_failure]</span> </li>
 </ul>
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
 <li><span class="li-head">parameters for method: [get]</span> - SNMP community configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [events, id, name, query-v1-port, query-v1-status, query-v2c-port, query-v2c-status, status, trap-v1-lport, trap-v1-rport, trap-v1-status, trap-v2c-lport, trap-v2c-rport, trap-v2c-status]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">get used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, datasrc, get reserved, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

   - To run in workspace mode, the paremeter workspace_locking_adom must be included in the task

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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/COMMUNITY
      fmgr_devprof_system_snmp_community:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               data:
                 -
                     events:
                       - <value in [cpu-high, mem-low, log-full, ...]>
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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/COMMUNITY
      fmgr_devprof_system_snmp_community:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [events, id, name, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Community ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/community</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> events </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> hosts </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ha-direct </span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-type </span> - Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Host entry ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv4 address of the SNMP manager (host). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - Source IPv4 address for SNMP traps. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> hosts6 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ha-direct </span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-type </span> - Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Host6 entry ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ipv6 </span> - SNMP manager IPv6 address prefix. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ipv6 </span> - Source IPv6 address for SNMP traps. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - Community ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Community name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> query-v1-port </span> - SNMP v1 query port (default = 161). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> query-v1-status </span> - Enable/disable SNMP v1 queries. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> query-v2c-port </span> - SNMP v2c query port (default = 161). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> query-v2c-status </span> - Enable/disable SNMP v2c queries. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this SNMP community. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> trap-v1-lport </span> - SNMP v1 trap local port (default = 162). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> trap-v1-rport </span> - SNMP v1 trap remote port (default = 162). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> trap-v1-status </span> - Enable/disable SNMP v1 traps. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> trap-v2c-lport </span> - SNMP v2c trap local port (default = 162). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> trap-v2c-rport </span> - SNMP v2c trap remote port (default = 162). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> trap-v2c-status </span> - Enable/disable SNMP v2c traps. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/community</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



