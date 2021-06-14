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
 <td>firewall_sslsshprofile</td>
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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_sslsshprofile</span> - Configure SSL/SSH protocol options. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
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
 <li><span class="li-head">ftps-client-certificate</span> - Action based on received client certificate during the FTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">https-client-certificate</span> - Action based on received client certificate during the HTTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">imaps-client-certificate</span> - Action based on received client certificate during the IMAPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">pop3s-client-certificate</span> - Action based on received client certificate during the POP3S handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">smtps-client-certificate</span> - Action based on received client certificate during the SMTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">ssl-other-client-certificate</span> - Action based on received client certificate during an SSL protocol handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 </ul>
 <li><span class="li-head">untrusted-caname</span> - Untrusted CA certificate used by SSL Inspection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">use-ssl-server</span> - Enable/disable the use of SSL server table for SSL offloading. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">whitelist</span> - Enable/disable exempting servers by FortiGuard whitelist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-blacklisted-certificates</span> - Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blacklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-negotiation-log</span> - Enable/disable logging SSL negotiation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">allowlist</span> - Enable/disable exempting servers by FortiGuard allowlist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-blocklisted-certificates</span> - Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dot</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cert-validation-failure</span> - Action based on certificate validation failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">cert-validation-timeout</span> - Action based on certificate validation timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">client-certificate</span> - Action based on received client certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">expired-server-cert</span> - Action based on server certificate is expired. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">revoked-server-cert</span> - Action based on server certificate is revoked. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">sni-server-cert-check</span> - Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, strict, disable]</span> </li>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-ssl-cipher</span> - Action based on the SSL cipher used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, allow]</span> </li>
 <li><span class="li-head">unsupported-ssl-negotiation</span> - Action based on the SSL negotiation used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, allow]</span> </li>
 <li><span class="li-head">untrusted-server-cert</span> - Action based on server certificate is not issued by a trusted CA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 </ul>
 <li><span class="li-head">ftps</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cert-validation-failure</span> - Action based on certificate validation failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">cert-validation-timeout</span> - Action based on certificate validation timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">client-certificate</span> - Action based on received client certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">expired-server-cert</span> - Action based on server certificate is expired. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">revoked-server-cert</span> - Action based on server certificate is revoked. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">sni-server-cert-check</span> - Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, strict]</span> </li>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-ssl-cipher</span> - Action based on the SSL cipher used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">unsupported-ssl-negotiation</span> - Action based on the SSL negotiation used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">untrusted-server-cert</span> - Action based on server certificate is not issued by a trusted CA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 </ul>
 <li><span class="li-head">https</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cert-probe-failure</span> - Action based on certificate probe failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, allow]</span> </li>
 <li><span class="li-head">cert-validation-failure</span> - Action based on certificate validation failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">cert-validation-timeout</span> - Action based on certificate validation timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">client-certificate</span> - Action based on received client certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">expired-server-cert</span> - Action based on server certificate is expired. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">revoked-server-cert</span> - Action based on server certificate is revoked. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">sni-server-cert-check</span> - Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, strict]</span> </li>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, certificate-inspection, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-ssl-cipher</span> - Action based on the SSL cipher used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">unsupported-ssl-negotiation</span> - Action based on the SSL negotiation used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">untrusted-server-cert</span> - Action based on server certificate is not issued by a trusted CA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 </ul>
 <li><span class="li-head">imaps</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cert-validation-failure</span> - Action based on certificate validation failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">cert-validation-timeout</span> - Action based on certificate validation timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">client-certificate</span> - Action based on received client certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">expired-server-cert</span> - Action based on server certificate is expired. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">revoked-server-cert</span> - Action based on server certificate is revoked. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">sni-server-cert-check</span> - Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, strict]</span> </li>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-ssl-cipher</span> - Action based on the SSL cipher used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">unsupported-ssl-negotiation</span> - Action based on the SSL negotiation used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">untrusted-server-cert</span> - Action based on server certificate is not issued by a trusted CA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 </ul>
 <li><span class="li-head">pop3s</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cert-validation-failure</span> - Action based on certificate validation failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">cert-validation-timeout</span> - Action based on certificate validation timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">client-certificate</span> - Action based on received client certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">expired-server-cert</span> - Action based on server certificate is expired. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">revoked-server-cert</span> - Action based on server certificate is revoked. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">sni-server-cert-check</span> - Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, strict]</span> </li>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-ssl-cipher</span> - Action based on the SSL cipher used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">unsupported-ssl-negotiation</span> - Action based on the SSL negotiation used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">untrusted-server-cert</span> - Action based on server certificate is not issued by a trusted CA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 </ul>
 <li><span class="li-head">smtps</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cert-validation-failure</span> - Action based on certificate validation failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">cert-validation-timeout</span> - Action based on certificate validation timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">client-certificate</span> - Action based on received client certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">expired-server-cert</span> - Action based on server certificate is expired. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">revoked-server-cert</span> - Action based on server certificate is revoked. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">sni-server-cert-check</span> - Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, strict]</span> </li>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-ssl-cipher</span> - Action based on the SSL cipher used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">unsupported-ssl-negotiation</span> - Action based on the SSL negotiation used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">untrusted-server-cert</span> - Action based on server certificate is not issued by a trusted CA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 </ul>
 <li><span class="li-head">ssh</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">inspect-all</span> - Level of SSL inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, deep-inspection]</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssh-algorithm</span> - Relative strength of encryption algorithms accepted during negotiation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [compatible, high-encryption]</span> </li>
 <li><span class="li-head">ssh-tun-policy-check</span> - Enable/disable SSH tunnel policy check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-version</span> - Action based on SSH version being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, bypass]</span> </li>
 </ul>
 <li><span class="li-head">ssl</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cert-validation-failure</span> - Action based on certificate validation failure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">cert-validation-timeout</span> - Action based on certificate validation timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">client-certificate</span> - Action based on received client certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">expired-server-cert</span> - Action based on server certificate is expired. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">inspect-all</span> - Level of SSL inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, certificate-inspection, deep-inspection]</span> </li>
 <li><span class="li-head">revoked-server-cert</span> - Action based on server certificate is revoked. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 <li><span class="li-head">sni-server-cert-check</span> - Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, strict]</span> </li>
 <li><span class="li-head">unsupported-ssl-cipher</span> - Action based on the SSL cipher used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">unsupported-ssl-negotiation</span> - Action based on the SSL negotiation used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">untrusted-server-cert</span> - Action based on server certificate is not issued by a trusted CA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
 </ul>
 <li><span class="li-head">supported-alpn</span> - Configure ALPN option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http1-1, http2, all]</span> </li>
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
    - name: Configure SSL/SSH protocol options.
      fmgr_firewall_sslsshprofile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_sslsshprofile:
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
                  ftps-client-certificate: <value in [bypass, inspect, block]>
                  https-client-certificate: <value in [bypass, inspect, block]>
                  imaps-client-certificate: <value in [bypass, inspect, block]>
                  pop3s-client-certificate: <value in [bypass, inspect, block]>
                  smtps-client-certificate: <value in [bypass, inspect, block]>
                  ssl-other-client-certificate: <value in [bypass, inspect, block]>
            untrusted-caname: <value of string>
            use-ssl-server: <value in [disable, enable]>
            whitelist: <value in [disable, enable]>
            block-blacklisted-certificates: <value in [disable, enable]>
            ssl-negotiation-log: <value in [disable, enable]>
            allowlist: <value in [disable, enable]>
            block-blocklisted-certificates: <value in [disable, enable]>
            dot:
               cert-validation-failure: <value in [allow, block, ignore]>
               cert-validation-timeout: <value in [allow, block, ignore]>
               client-certificate: <value in [bypass, inspect, block]>
               expired-server-cert: <value in [allow, block, ignore]>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               revoked-server-cert: <value in [allow, block, ignore]>
               sni-server-cert-check: <value in [enable, strict, disable]>
               status: <value in [disable, deep-inspection]>
               unsupported-ssl-cipher: <value in [block, allow]>
               unsupported-ssl-negotiation: <value in [block, allow]>
               untrusted-server-cert: <value in [allow, block, ignore]>
            ftps:
               cert-validation-failure: <value in [allow, block, ignore]>
               cert-validation-timeout: <value in [allow, block, ignore]>
               client-certificate: <value in [bypass, inspect, block]>
               expired-server-cert: <value in [allow, block, ignore]>
               ports: <value of integer>
               revoked-server-cert: <value in [allow, block, ignore]>
               sni-server-cert-check: <value in [disable, enable, strict]>
               status: <value in [disable, deep-inspection]>
               unsupported-ssl-cipher: <value in [allow, block]>
               unsupported-ssl-negotiation: <value in [allow, block]>
               untrusted-server-cert: <value in [allow, block, ignore]>
            https:
               cert-probe-failure: <value in [block, allow]>
               cert-validation-failure: <value in [allow, block, ignore]>
               cert-validation-timeout: <value in [allow, block, ignore]>
               client-certificate: <value in [bypass, inspect, block]>
               expired-server-cert: <value in [allow, block, ignore]>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               revoked-server-cert: <value in [allow, block, ignore]>
               sni-server-cert-check: <value in [disable, enable, strict]>
               status: <value in [disable, certificate-inspection, deep-inspection]>
               unsupported-ssl-cipher: <value in [allow, block]>
               unsupported-ssl-negotiation: <value in [allow, block]>
               untrusted-server-cert: <value in [allow, block, ignore]>
            imaps:
               cert-validation-failure: <value in [allow, block, ignore]>
               cert-validation-timeout: <value in [allow, block, ignore]>
               client-certificate: <value in [bypass, inspect, block]>
               expired-server-cert: <value in [allow, block, ignore]>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               revoked-server-cert: <value in [allow, block, ignore]>
               sni-server-cert-check: <value in [disable, enable, strict]>
               status: <value in [disable, deep-inspection]>
               unsupported-ssl-cipher: <value in [allow, block]>
               unsupported-ssl-negotiation: <value in [allow, block]>
               untrusted-server-cert: <value in [allow, block, ignore]>
            pop3s:
               cert-validation-failure: <value in [allow, block, ignore]>
               cert-validation-timeout: <value in [allow, block, ignore]>
               client-certificate: <value in [bypass, inspect, block]>
               expired-server-cert: <value in [allow, block, ignore]>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               revoked-server-cert: <value in [allow, block, ignore]>
               sni-server-cert-check: <value in [disable, enable, strict]>
               status: <value in [disable, deep-inspection]>
               unsupported-ssl-cipher: <value in [allow, block]>
               unsupported-ssl-negotiation: <value in [allow, block]>
               untrusted-server-cert: <value in [allow, block, ignore]>
            smtps:
               cert-validation-failure: <value in [allow, block, ignore]>
               cert-validation-timeout: <value in [allow, block, ignore]>
               client-certificate: <value in [bypass, inspect, block]>
               expired-server-cert: <value in [allow, block, ignore]>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               revoked-server-cert: <value in [allow, block, ignore]>
               sni-server-cert-check: <value in [disable, enable, strict]>
               status: <value in [disable, deep-inspection]>
               unsupported-ssl-cipher: <value in [allow, block]>
               unsupported-ssl-negotiation: <value in [allow, block]>
               untrusted-server-cert: <value in [allow, block, ignore]>
            ssh:
               inspect-all: <value in [disable, deep-inspection]>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               ssh-algorithm: <value in [compatible, high-encryption]>
               ssh-tun-policy-check: <value in [disable, enable]>
               status: <value in [disable, deep-inspection]>
               unsupported-version: <value in [block, bypass]>
            ssl:
               cert-validation-failure: <value in [allow, block, ignore]>
               cert-validation-timeout: <value in [allow, block, ignore]>
               client-certificate: <value in [bypass, inspect, block]>
               expired-server-cert: <value in [allow, block, ignore]>
               inspect-all: <value in [disable, certificate-inspection, deep-inspection]>
               revoked-server-cert: <value in [allow, block, ignore]>
               sni-server-cert-check: <value in [disable, enable, strict]>
               unsupported-ssl-cipher: <value in [allow, block]>
               unsupported-ssl-negotiation: <value in [allow, block]>
               untrusted-server-cert: <value in [allow, block, ignore]>
            supported-alpn: <value in [none, http1-1, http2, ...]>



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



