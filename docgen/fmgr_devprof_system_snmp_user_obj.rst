:source: fmgr_devprof_system_snmp_user_obj.py

:orphan:

.. _fmgr_devprof_system_snmp_user_obj:

fmgr_devprof_system_snmp_user_obj -- SNMP user configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/system/snmp/user/{user}`
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
 <li><span class="li-head">user</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - SNMP user configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 <li><span class="li-head">parameters for method: [delete]</span> - SNMP user configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - SNMP user configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/USER/{USER}
      fmgr_devprof_system_snmp_user_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
            user: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/USER/{USER}
      fmgr_devprof_system_snmp_user_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
            user: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/user/{user}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/user/{user}</span>  </li>
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



