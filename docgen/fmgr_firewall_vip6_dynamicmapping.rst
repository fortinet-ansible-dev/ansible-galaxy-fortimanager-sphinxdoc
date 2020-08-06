:source: fmgr_firewall_vip6_dynamicmapping.py

:orphan:

.. _fmgr_firewall_vip6_dynamicmapping:

fmgr_firewall_vip6_dynamicmapping
+++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">vip6</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_vip6_dynamicmapping</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">arp-reply</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-age</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-cookie-domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-domain-from-host</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">http-cookie-generation</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-cookie-path</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-share</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, same-ip]</span> </li>
 <li><span class="li-head">http-ip-header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">http-ip-header-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-multiplex</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">https-cookie-secure</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldb-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive, http-host]</span> </li>
 <li><span class="li-head">mappedip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-embryonic-connections</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">outlook-web-access</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">persistence</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http-cookie, ssl-session-id]</span> </li>
 <li><span class="li-head">portforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp, sctp]</span> </li>
 <li><span class="li-head">server-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, https, ssl, tcp, udp, ip, imaps, pop3s, smtps]</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">ssl-algorithm</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, medium, custom]</span> </li>
 <li><span class="li-head">ssl-certificate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-client-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-client-renegotiation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow, secure]</span> </li>
 <li><span class="li-head">ssl-client-session-state-max</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">ssl-dh-bits</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [768, 1024, 1536, 2048, 3072, 4096]</span> </li>
 <li><span class="li-head">ssl-hpkp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, report-only]</span> </li>
 <li><span class="li-head">ssl-hpkp-age</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-hpkp-backup</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hpkp-include-subdomains</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-hpkp-primary</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hpkp-report-uri</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hsts</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-hsts-age</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-hsts-include-subdomains</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-http-location-conversion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-http-match-host</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-max-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-min-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [half, full]</span> </li>
 <li><span class="li-head">ssl-pfs</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [require, deny, allow]</span> </li>
 <li><span class="li-head">ssl-send-empty-frags</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-server-algorithm</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, medium, custom, client]</span> </li>
 <li><span class="li-head">ssl-server-max-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-min-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-session-state-max</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, server-load-balance]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">weblogic-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">websphere-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
      fmgr_firewall_vip6_dynamicmapping:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vip6: <your own value>
         state: <value in [present, absent]>
         firewall_vip6_dynamicmapping:
            _scope:
              -
                  name: <value of string>
                  vdom: <value of string>
            arp-reply: <value in [disable, enable]>
            color: <value of integer>
            comment: <value of string>
            extip: <value of string>
            extport: <value of string>
            http-cookie-age: <value of integer>
            http-cookie-domain: <value of string>
            http-cookie-domain-from-host: <value in [disable, enable]>
            http-cookie-generation: <value of integer>
            http-cookie-path: <value of string>
            http-cookie-share: <value in [disable, same-ip]>
            http-ip-header: <value in [disable, enable]>
            http-ip-header-name: <value of string>
            http-multiplex: <value in [disable, enable]>
            https-cookie-secure: <value in [disable, enable]>
            id: <value of integer>
            ldb-method: <value in [static, round-robin, weighted, ...]>
            mappedip: <value of string>
            mappedport: <value of string>
            max-embryonic-connections: <value of integer>
            monitor: <value of string>
            outlook-web-access: <value in [disable, enable]>
            persistence: <value in [none, http-cookie, ssl-session-id]>
            portforward: <value in [disable, enable]>
            protocol: <value in [tcp, udp, sctp]>
            server-type: <value in [http, https, ssl, ...]>
            src-filter: <value of string>
            ssl-algorithm: <value in [high, low, medium, ...]>
            ssl-certificate: <value of string>
            ssl-client-fallback: <value in [disable, enable]>
            ssl-client-renegotiation: <value in [deny, allow, secure]>
            ssl-client-session-state-max: <value of integer>
            ssl-client-session-state-timeout: <value of integer>
            ssl-client-session-state-type: <value in [disable, time, count, ...]>
            ssl-dh-bits: <value in [768, 1024, 1536, ...]>
            ssl-hpkp: <value in [disable, enable, report-only]>
            ssl-hpkp-age: <value of integer>
            ssl-hpkp-backup: <value of string>
            ssl-hpkp-include-subdomains: <value in [disable, enable]>
            ssl-hpkp-primary: <value of string>
            ssl-hpkp-report-uri: <value of string>
            ssl-hsts: <value in [disable, enable]>
            ssl-hsts-age: <value of integer>
            ssl-hsts-include-subdomains: <value in [disable, enable]>
            ssl-http-location-conversion: <value in [disable, enable]>
            ssl-http-match-host: <value in [disable, enable]>
            ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl-mode: <value in [half, full]>
            ssl-pfs: <value in [require, deny, allow]>
            ssl-send-empty-frags: <value in [disable, enable]>
            ssl-server-algorithm: <value in [high, low, medium, ...]>
            ssl-server-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl-server-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
            ssl-server-session-state-max: <value of integer>
            ssl-server-session-state-timeout: <value of integer>
            ssl-server-session-state-type: <value in [disable, time, count, ...]>
            type: <value in [static-nat, server-load-balance]>
            uuid: <value of string>
            weblogic-server: <value in [disable, enable]>
            websphere-server: <value in [disable, enable]>



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



