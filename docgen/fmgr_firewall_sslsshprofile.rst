:source: fmgr_firewall_sslsshprofile.py

:orphan:

.. _fmgr_firewall_sslsshprofile:

fmgr_firewall_sslsshprofile -- Configure SSL/SSH protocol options.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile`
- `/pm/config/global/obj/firewall/ssl-ssh-profile`
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
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure SSL/SSH protocol options.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">caname</span> - CA certificate used by SSL Inspection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mapi-over-https</span> - Enable/disable inspection of MAPI over HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rpc-over-https</span> - Enable/disable inspection of RPC over HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">server-cert</span> - Certificate used by SSL Inspection to replace server certificate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-cert-mode</span> - Re-sign or replace the servers certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [re-sign, replace]</span> </li>
 <li><span class="li-head">ssl-anomalies-log</span> - Enable/disable logging SSL anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-exempt</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">address</span> - IPv4 address object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">address6</span> - IPv6 address object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortiguard-category</span> - FortiGuard category ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">regex</span> - Exempt servers by regular expression. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of address object (IPv4 or IPv6) or FortiGuard category. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortiguard-category, address, address6, wildcard-fqdn, regex]</span> </li>
 <li><span class="li-head">wildcard-fqdn</span> - Exempt servers by wildcard FQDN. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ssl-exemptions-log</span> - Enable/disable logging SSL exemptions. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-server</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ftps-client-cert-request</span> - Action based on client certificate request during the FTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">https-client-cert-request</span> - Action based on client certificate request during the HTTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">id</span> - SSL server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">imaps-client-cert-request</span> - Action based on client certificate request during the IMAPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the SSL server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pop3s-client-cert-request</span> - Action based on client certificate request during the POP3S handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">smtps-client-cert-request</span> - Action based on client certificate request during the SMTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">ssl-other-client-cert-request</span> - Action based on client certificate request during an SSL protocol handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 </ul>
 <li><span class="li-head">untrusted-caname</span> - Untrusted CA certificate used by SSL Inspection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">use-ssl-server</span> - Enable/disable the use of SSL server table for SSL offloading. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">whitelist</span> - Enable/disable exempting servers by FortiGuard whitelist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure SSL/SSH protocol options.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [caname, comment, mapi-over-https, name, rpc-over-https, server-cert, server-cert-mode, ssl-anomalies-log, ssl-exemptions-log, untrusted-caname, use-ssl-server, whitelist]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SSL-SSH-PROFILE
      fmgr_firewall_sslsshprofile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     caname: <value of string>
                     comment: <value of string>
                     mapi-over-https: <value in [disable, enable]>
                     name: <value of string>
                     rpc-over-https: <value in [disable, enable]>
                     server-cert: <value of string>
                     server-cert-mode: <value in [re-sign, replace]>
                     ssl-anomalies-log: <value in [disable, enable]>
                     ssl-exempt:
                       -
                           address: <value of string>
                           address6: <value of string>
                           fortiguard-category: <value of string>
                           id: <value of integer>
                           regex: <value of string>
                           type: <value in [fortiguard-category, address, address6, ...]>
                           wildcard-fqdn: <value of string>
                     ssl-exemptions-log: <value in [disable, enable]>
                     ssl-server:
                       -
                           ftps-client-cert-request: <value in [bypass, inspect, block]>
                           https-client-cert-request: <value in [bypass, inspect, block]>
                           id: <value of integer>
                           imaps-client-cert-request: <value in [bypass, inspect, block]>
                           ip: <value of string>
                           pop3s-client-cert-request: <value in [bypass, inspect, block]>
                           smtps-client-cert-request: <value in [bypass, inspect, block]>
                           ssl-other-client-cert-request: <value in [bypass, inspect, block]>
                     untrusted-caname: <value of string>
                     use-ssl-server: <value in [disable, enable]>
                     whitelist: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SSL-SSH-PROFILE
      fmgr_firewall_sslsshprofile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [caname, comment, mapi-over-https, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> caname </span> - CA certificate used by SSL Inspection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Optional comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mapi-over-https </span> - Enable/disable inspection of MAPI over HTTPS. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rpc-over-https </span> - Enable/disable inspection of RPC over HTTPS. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-cert </span> - Certificate used by SSL Inspection to replace server certificate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-cert-mode </span> - Re-sign or replace the servers certificate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-anomalies-log </span> - Enable/disable logging SSL anomalies. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-exempt </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> address </span> - IPv4 address object. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> address6 </span> - IPv6 address object. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fortiguard-category </span> - FortiGuard category ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> regex </span> - Exempt servers by regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Type of address object (IPv4 or IPv6) or FortiGuard category. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wildcard-fqdn </span> - Exempt servers by wildcard FQDN. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ssl-exemptions-log </span> - Enable/disable logging SSL exemptions. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ftps-client-cert-request </span> - Action based on client certificate request during the FTPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> https-client-cert-request </span> - Action based on client certificate request during the HTTPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - SSL server ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> imaps-client-cert-request </span> - Action based on client certificate request during the IMAPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv4 address of the SSL server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pop3s-client-cert-request </span> - Action based on client certificate request during the POP3S handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smtps-client-cert-request </span> - Action based on client certificate request during the SMTPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-other-client-cert-request </span> - Action based on client certificate request during an SSL protocol handshake. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> untrusted-caname </span> - Untrusted CA certificate used by SSL Inspection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> use-ssl-server </span> - Enable/disable the use of SSL server table for SSL offloading. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> whitelist </span> - Enable/disable exempting servers by FortiGuard whitelist. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile</span>  </li>
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



