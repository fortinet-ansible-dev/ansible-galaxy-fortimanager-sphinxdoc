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

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/system/snmp/user`
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
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">devprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - SNMP user configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">auth-proto</span> - Authentication protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [md5, sha]</span> </li>
 <li><span class="li-head">auth-pwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">events</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [cpu-high, mem-low, log-full, intf-ip, vpn-tun-up, vpn-tun-down, ha-switch, fm-conf-change, ips-signature, ips-anomaly, temperature-high, voltage-alert, av-virus, av-oversize, av-pattern, av-fragmented, ha-hb-failure, fan-failure, ha-member-up, ha-member-down, ent-conf-change, av-conserve, av-bypass, av-oversize-passed, av-oversize-blocked, ips-pkg-update, fm-if-change, power-supply-failure, amc-bypass, faz-disconnect, bgp-established, bgp-backward-transition, wc-ap-up, wc-ap-down, fswctl-session-up, fswctl-session-down, ips-fail-open, load-balance-real-server-down, device-new, enter-intf-bypass, exit-intf-bypass, per-cpu-high, power-blade-down, confsync_failure]</span> </li>
 </ul>
 <li><span class="li-head">ha-direct</span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - SNMP user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">notify-hosts</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">notify-hosts6</span> - IPv6 SNMP managers to send notifications (traps) to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priv-proto</span> - Privacy (encryption) protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aes, des, aes256, aes256cisco]</span> </li>
 <li><span class="li-head">priv-pwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
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
 <li><span class="li-head">parameters for method: [get]</span> - SNMP user configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auth-proto, auth-pwd, events, ha-direct, name, notify-hosts, notify-hosts6, priv-proto, priv-pwd, queries, query-port, security-level, source-ip, source-ipv6, status, trap-lport, trap-rport, trap-status]</span> </li>
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

Examples
--------

.. code-block:: yaml+jinja

 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/USER
      fmgr_devprof_system_snmp_user:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               data:
                 -
                     auth-proto: <value in [md5, sha]>
                     auth-pwd:
                       - <value of string>
                     events:
                       - <value in [cpu-high, mem-low, log-full, ...]>
                     ha-direct: <value in [disable, enable]>
                     name: <value of string>
                     notify-hosts:
                       - <value of string>
                     notify-hosts6: <value of string>
                     priv-proto: <value in [aes, des, aes256, ...]>
                     priv-pwd:
                       - <value of string>
                     queries: <value in [disable, enable]>
                     query-port: <value of integer>
                     security-level: <value in [no-auth-no-priv, auth-no-priv, auth-priv]>
                     source-ip: <value of string>
                     source-ipv6: <value of string>
                     status: <value in [disable, enable]>
                     trap-lport: <value of integer>
                     trap-rport: <value of integer>
                     trap-status: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/USER
      fmgr_devprof_system_snmp_user:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [auth-proto, auth-pwd, events, ...]>
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
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/user</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> auth-proto </span> - Authentication protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-pwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> events </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ha-direct </span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - SNMP user name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> notify-hosts </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> notify-hosts6 </span> - IPv6 SNMP managers to send notifications (traps) to. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priv-proto </span> - Privacy (encryption) protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priv-pwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> queries </span> - Enable/disable SNMP queries for this user. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> query-port </span> - SNMPv3 query port (default = 161). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> security-level </span> - Security level for message authentication and encryption. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - Source IP for SNMP trap. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ipv6 </span> - Source IPv6 for SNMP trap. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this SNMP user. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> trap-lport </span> - SNMPv3 local trap port (default = 162). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> trap-rport </span> - SNMPv3 trap remote port (default = 162). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> trap-status </span> - Enable/disable traps for this SNMP user. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/user</span>  </li>
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



