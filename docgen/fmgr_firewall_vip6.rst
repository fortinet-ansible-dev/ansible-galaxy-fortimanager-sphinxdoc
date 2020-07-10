:source: fmgr_firewall_vip6.py

:orphan:

.. _fmgr_firewall_vip6:

fmgr_firewall_vip6 -- Configure virtual IP for IPv6.
++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_vip6</span> - Configure virtual IP for IPv6. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">arp-reply</span> - Enable to respond to ARP requests for this virtual IP address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-head">extip</span> - IP address or address range on the external interface that you want to map to an address or address range on the destination network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - Incoming port number range that you want to map to a port number range on the destination network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-age</span> - Time in minutes that client web browsers should keep a cookie. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-cookie-domain</span> - Domain that HTTP cookie persistence should apply to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-domain-from-host</span> - Enable/disable use of HTTP cookie domain from host field in HTTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">http-cookie-generation</span> - Generation of HTTP cookie to be accepted. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-cookie-path</span> - Limit HTTP cookie persistence to the specified path. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-share</span> - Control sharing of cookies across virtual servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, same-ip]</span> </li>
 <li><span class="li-head">http-ip-header</span> - For HTTP multiplexing, enable to add the original client IP address in the XForwarded-For HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">http-ip-header-name</span> - For HTTP multiplexing, enter a custom HTTPS header name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-multiplex</span> - Enable/disable HTTP multiplexing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">https-cookie-secure</span> - Enable/disable verification that inserted HTTPS cookies are secure. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - Custom defined ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldb-method</span> - Method used to distribute sessions to real servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive, http-host]</span> </li>
 <li><span class="li-head">mappedip</span> - Mapped IP address range in the format startIP-endIP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedport</span> - Port number range on the destination network to which the external port number range is mapped. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-embryonic-connections</span> - Maximum number of incomplete connections. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Virtual ip6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">outlook-web-access</span> - Enable to add the Front-End-Https header for Microsoft Outlook Web Access. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">persistence</span> - Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http-cookie, ssl-session-id]</span> </li>
 <li><span class="li-head">portforward</span> - Enable port forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">protocol</span> - Protocol to use when forwarding packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp, sctp]</span> </li>
 <li><span class="li-head">realservers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">client-ip</span> - Only clients in this IP range can connect to this real server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">healthcheck</span> - Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vip]</span> </li>
 <li><span class="li-head">holddown-interval</span> - Time in seconds that the health check monitor continues to monitor an unresponsive server that should be active. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-host</span> - HTTP server domain name in HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Real server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - IPv6 address of the real server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - Max number of active connections that can directed to the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Port for communicating with the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, standby, disable]</span> </li>
 <li><span class="li-head">weight</span> - Weight of the real server. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - Protocol to be load balanced by the virtual server (also called the server load balance virtual IP). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, https, ssl, tcp, udp, ip, imaps, pop3s, smtps]</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">ssl-algorithm</span> - Permitted encryption algorithms for SSL sessions according to encryption strength. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, medium, custom]</span> </li>
 <li><span class="li-head">ssl-certificate</span> - The name of the SSL certificate to use for SSL acceleration. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-cipher-suites</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">cipher</span> - Cipher suite name. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, TLS-RSA-WITH-3DES-EDE-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA, TLS-RSA-WITH-AES-256-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA256, TLS-RSA-WITH-AES-256-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-RSA-WITH-SEED-CBC-SHA, TLS-RSA-WITH-ARIA-128-CBC-SHA256, TLS-RSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-RSA-WITH-DES-CBC-SHA, TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA, TLS-DHE-RSA-WITH-AES-256-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA256, TLS-DHE-RSA-WITH-AES-256-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-RSA-WITH-SEED-CBC-SHA, TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-RC4-128-SHA, TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA, TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-AES-128-GCM-SHA256, TLS-DHE-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-AES-128-CBC-SHA, TLS-DHE-DSS-WITH-AES-256-CBC-SHA, TLS-DHE-DSS-WITH-AES-128-CBC-SHA256, TLS-DHE-DSS-WITH-AES-128-GCM-SHA256, TLS-DHE-DSS-WITH-AES-256-CBC-SHA256, TLS-DHE-DSS-WITH-AES-256-GCM-SHA384, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384, TLS-RSA-WITH-AES-128-GCM-SHA256, TLS-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-DSS-WITH-SEED-CBC-SHA, TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA, TLS-DHE-DSS-WITH-DES-CBC-SHA]</span> </li>
 <li><span class="li-head">priority</span> - SSL/TLS cipher suites priority. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">versions</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 </ul>
 <li><span class="li-head">ssl-client-fallback</span> - Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-client-renegotiation</span> - Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow, secure]</span> </li>
 <li><span class="li-head">ssl-client-session-state-max</span> - Maximum number of client to FortiGate SSL session states to keep. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-timeout</span> - Number of minutes to keep client to FortiGate SSL session state. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-type</span> - How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">ssl-dh-bits</span> - Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [768, 1024, 1536, 2048, 3072, 4096]</span> </li>
 <li><span class="li-head">ssl-hpkp</span> - Enable/disable including HPKP header in response. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, report-only]</span> </li>
 <li><span class="li-head">ssl-hpkp-age</span> - Number of minutes the web browser should keep HPKP. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-hpkp-backup</span> - Certificate to generate backup HPKP pin from. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hpkp-include-subdomains</span> - Indicate that HPKP header applies to all subdomains. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-hpkp-primary</span> - Certificate to generate primary HPKP pin from. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hpkp-report-uri</span> - URL to report HPKP violations to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hsts</span> - Enable/disable including HSTS header in response. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-hsts-age</span> - Number of seconds the client should honour the HSTS setting. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-hsts-include-subdomains</span> - Indicate that HSTS header applies to all subdomains. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-http-location-conversion</span> - Enable to replace HTTP with HTTPS in the replys Location HTTP header field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-http-match-host</span> - Enable/disable HTTP host matching for location conversion. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-max-version</span> - Highest SSL/TLS version acceptable from a client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-min-version</span> - Lowest SSL/TLS version acceptable from a client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-mode</span> - Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [half, full]</span> </li>
 <li><span class="li-head">ssl-pfs</span> - Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [require, deny, allow]</span> </li>
 <li><span class="li-head">ssl-send-empty-frags</span> - Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-server-algorithm</span> - Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, medium, custom, client]</span> </li>
 <li><span class="li-head">ssl-server-cipher-suites</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">cipher</span> - Cipher suite name. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, TLS-RSA-WITH-3DES-EDE-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA, TLS-RSA-WITH-AES-256-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA256, TLS-RSA-WITH-AES-256-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-RSA-WITH-SEED-CBC-SHA, TLS-RSA-WITH-ARIA-128-CBC-SHA256, TLS-RSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-RSA-WITH-DES-CBC-SHA, TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA, TLS-DHE-RSA-WITH-AES-256-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA256, TLS-DHE-RSA-WITH-AES-256-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-RSA-WITH-SEED-CBC-SHA, TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-RC4-128-SHA, TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA, TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-AES-128-GCM-SHA256, TLS-DHE-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-AES-128-CBC-SHA, TLS-DHE-DSS-WITH-AES-256-CBC-SHA, TLS-DHE-DSS-WITH-AES-128-CBC-SHA256, TLS-DHE-DSS-WITH-AES-128-GCM-SHA256, TLS-DHE-DSS-WITH-AES-256-CBC-SHA256, TLS-DHE-DSS-WITH-AES-256-GCM-SHA384, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384, TLS-RSA-WITH-AES-128-GCM-SHA256, TLS-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-DSS-WITH-SEED-CBC-SHA, TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA, TLS-DHE-DSS-WITH-DES-CBC-SHA]</span> </li>
 <li><span class="li-head">priority</span> - SSL/TLS cipher suites priority. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">versions</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 </ul>
 <li><span class="li-head">ssl-server-max-version</span> - Highest SSL/TLS version acceptable from a server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-min-version</span> - Lowest SSL/TLS version acceptable from a server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-session-state-max</span> - Maximum number of FortiGate to Server SSL session states to keep. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-timeout</span> - Number of minutes to keep FortiGate to Server SSL session state. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-type</span> - How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">type</span> - Configure a static NAT VIP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, server-load-balance]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">weblogic-server</span> - Enable to add an HTTP header to indicate SSL offloading for a WebLogic server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">websphere-server</span> - Enable to add an HTTP header to indicate SSL offloading for a WebSphere server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure virtual IP for IPv6.
      fmgr_firewall_vip6:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_vip6:
            arp-reply: <value in [disable, enable]>
            color: <value of integer>
            comment: <value of string>
            dynamic_mapping:
              -
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
            name: <value of string>
            outlook-web-access: <value in [disable, enable]>
            persistence: <value in [none, http-cookie, ssl-session-id]>
            portforward: <value in [disable, enable]>
            protocol: <value in [tcp, udp, sctp]>
            realservers:
              -
                  client-ip: <value of string>
                  healthcheck: <value in [disable, enable, vip]>
                  holddown-interval: <value of integer>
                  http-host: <value of string>
                  id: <value of integer>
                  ip: <value of string>
                  max-connections: <value of integer>
                  monitor: <value of string>
                  port: <value of integer>
                  status: <value in [active, standby, disable]>
                  weight: <value of integer>
            server-type: <value in [http, https, ssl, ...]>
            src-filter: <value of string>
            ssl-algorithm: <value in [high, low, medium, ...]>
            ssl-certificate: <value of string>
            ssl-cipher-suites:
              -
                  cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                  priority: <value of integer>
                  versions:
                    - ssl-3.0
                    - tls-1.0
                    - tls-1.1
                    - tls-1.2
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
            ssl-server-cipher-suites:
              -
                  cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                  priority: <value of integer>
                  versions:
                    - ssl-3.0
                    - tls-1.0
                    - tls-1.1
                    - tls-1.2
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



