:source: fmgr_firewall_vip_obj.py

:orphan:

.. _fmgr_firewall_vip_obj:

fmgr_firewall_vip_obj -- Configure virtual IP for IPv4.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/vip/{vip}`
- `/pm/config/global/obj/firewall/vip/{vip}`
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
 <li><span class="li-head">vip</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure virtual IP for IPv4.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">arp-reply</span> - Enable to respond to ARP requests for this virtual IP address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-mapping-ttl</span> - DNS mapping TTL (Set to zero to use TTL in DNS response, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">arp-reply</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-mapping-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">extaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gratuitous-arp-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
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
 <li><span class="li-head">mapped-addr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mappedport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-embryonic-connections</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">nat-source-vip</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outlook-web-access</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">persistence</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http-cookie, ssl-session-id]</span> </li>
 <li><span class="li-head">portforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">portmapping-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1-to-1, m-to-n]</span> </li>
 <li><span class="li-head">protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp, sctp, icmp]</span> </li>
 <li><span class="li-head">realservers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">client-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">healthcheck</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vip]</span> </li>
 <li><span class="li-head">holddown-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-host</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, standby, disable]</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, https, ssl, tcp, udp, ip, imaps, pop3s, smtps]</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">srcintf-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ssl-algorithm</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, medium, low, custom]</span> </li>
 <li><span class="li-head">ssl-certificate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-cipher-suites</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">cipher</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, TLS-RSA-WITH-3DES-EDE-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA, TLS-RSA-WITH-AES-256-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA256, TLS-RSA-WITH-AES-256-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-RSA-WITH-SEED-CBC-SHA, TLS-RSA-WITH-ARIA-128-CBC-SHA256, TLS-RSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-RSA-WITH-DES-CBC-SHA, TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA, TLS-DHE-RSA-WITH-AES-256-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA256, TLS-DHE-RSA-WITH-AES-256-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-RSA-WITH-SEED-CBC-SHA, TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-RC4-128-SHA, TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA, TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-AES-128-GCM-SHA256, TLS-DHE-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-AES-128-CBC-SHA, TLS-DHE-DSS-WITH-AES-256-CBC-SHA, TLS-DHE-DSS-WITH-AES-128-CBC-SHA256, TLS-DHE-DSS-WITH-AES-128-GCM-SHA256, TLS-DHE-DSS-WITH-AES-256-CBC-SHA256, TLS-DHE-DSS-WITH-AES-256-GCM-SHA384, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384, TLS-RSA-WITH-AES-128-GCM-SHA256, TLS-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-DSS-WITH-SEED-CBC-SHA, TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA, TLS-DHE-DSS-WITH-DES-CBC-SHA]</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">versions</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 </ul>
 </ul>
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
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, load-balance, server-load-balance, dns-translation, fqdn]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">weblogic-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">websphere-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">extaddr</span> - External FQDN address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extintf</span> - Interface connected to the source network that receives the packets that will be forwarded to the destination network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extip</span> - IP address or address range on the external interface that you want to map to an address or address range on the destination network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - Incoming port number range that you want to map to a port number range on the destination network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gratuitous-arp-interval</span> - Enable to have the VIP send gratuitous ARPs. <span class="li-normal">type: int</span> </li>
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
 <li><span class="li-head">mapped-addr</span> - Mapped FQDN address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mappedport</span> - Port number range on the destination network to which the external port number range is mapped. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-embryonic-connections</span> - Maximum number of incomplete connections. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Virtual IP name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat-source-vip</span> - Enable/disable forcing the source NAT mapped IP to the external IP for all traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outlook-web-access</span> - Enable to add the Front-End-Https header for Microsoft Outlook Web Access. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">persistence</span> - Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http-cookie, ssl-session-id]</span> </li>
 <li><span class="li-head">portforward</span> - Enable/disable port forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">portmapping-type</span> - Port mapping type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1-to-1, m-to-n]</span> </li>
 <li><span class="li-head">protocol</span> - Protocol to use when forwarding packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp, sctp, icmp]</span> </li>
 <li><span class="li-head">realservers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">client-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">healthcheck</span> - Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vip]</span> </li>
 <li><span class="li-head">holddown-interval</span> - Time in seconds that the health check monitor continues to monitor and unresponsive server that should be active. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-host</span> - HTTP server domain name in HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - IP address of the real server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - Max number of active connections that can be directed to the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Port for communicating with the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, standby, disable]</span> </li>
 <li><span class="li-head">weight</span> - Weight of the real server. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - Protocol to be load balanced by the virtual server (also called the server load balance virtual IP). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, https, ssl, tcp, udp, ip, imaps, pop3s, smtps]</span> </li>
 <li><span class="li-head">service</span> - Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">srcintf-filter</span> - Interfaces to which the VIP applies. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-algorithm</span> - Permitted encryption algorithms for SSL sessions according to encryption strength. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, medium, low, custom]</span> </li>
 <li><span class="li-head">ssl-certificate</span> - The name of the SSL certificate to use for SSL acceleration. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-cipher-suites</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">cipher</span> - Cipher suite name. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, TLS-RSA-WITH-3DES-EDE-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA, TLS-RSA-WITH-AES-256-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA256, TLS-RSA-WITH-AES-256-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-RSA-WITH-SEED-CBC-SHA, TLS-RSA-WITH-ARIA-128-CBC-SHA256, TLS-RSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-RSA-WITH-DES-CBC-SHA, TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA, TLS-DHE-RSA-WITH-AES-256-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA256, TLS-DHE-RSA-WITH-AES-256-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-RSA-WITH-SEED-CBC-SHA, TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-RC4-128-SHA, TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA, TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-AES-128-GCM-SHA256, TLS-DHE-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-AES-128-CBC-SHA, TLS-DHE-DSS-WITH-AES-256-CBC-SHA, TLS-DHE-DSS-WITH-AES-128-CBC-SHA256, TLS-DHE-DSS-WITH-AES-128-GCM-SHA256, TLS-DHE-DSS-WITH-AES-256-CBC-SHA256, TLS-DHE-DSS-WITH-AES-256-GCM-SHA384, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384, TLS-RSA-WITH-AES-128-GCM-SHA256, TLS-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-DSS-WITH-SEED-CBC-SHA, TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA, TLS-DHE-DSS-WITH-DES-CBC-SHA]</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">versions</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">ssl-client-fallback</span> - Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-client-renegotiation</span> - Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow, secure]</span> </li>
 <li><span class="li-head">ssl-client-session-state-max</span> - Maximum number of client to FortiGate SSL session states to keep. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-timeout</span> - Number of minutes to keep client to FortiGate SSL session state. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-type</span> - How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">ssl-dh-bits</span> - Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [768, 1024, 1536, 2048, 3072, 4096]</span> </li>
 <li><span class="li-head">ssl-hpkp</span> - Enable/disable including HPKP header in response. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, report-only]</span> </li>
 <li><span class="li-head">ssl-hpkp-age</span> - Number of seconds the client should honour the HPKP setting. <span class="li-normal">type: int</span> </li>
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
 <li><span class="li-head">versions</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">ssl-server-max-version</span> - Highest SSL/TLS version acceptable from a server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-min-version</span> - Lowest SSL/TLS version acceptable from a server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-session-state-max</span> - Maximum number of FortiGate to Server SSL session states to keep. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-timeout</span> - Number of minutes to keep FortiGate to Server SSL session state. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-type</span> - How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">type</span> - Configure a static NAT, load balance, DNS translation, or FQDN VIP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, load-balance, server-load-balance, dns-translation, fqdn]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">weblogic-server</span> - Enable to add an HTTP header to indicate SSL offloading for a WebLogic server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">websphere-server</span> - Enable to add an HTTP header to indicate SSL offloading for a WebSphere server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure virtual IP for IPv4.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure virtual IP for IPv4.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Configure virtual IP for IPv4.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [before, after]</span> </li>
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP/{VIP}
      fmgr_firewall_vip_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip: <value of string>
         params:
            -
               data:
                  arp-reply: <value in [disable, enable]>
                  color: <value of integer>
                  comment: <value of string>
                  dns-mapping-ttl: <value of integer>
                  dynamic_mapping:
                    -
                        _scope:
                          -
                              name: <value of string>
                              vdom: <value of string>
                        arp-reply: <value in [disable, enable]>
                        color: <value of integer>
                        comment: <value of string>
                        dns-mapping-ttl: <value of integer>
                        extaddr: <value of string>
                        extintf: <value of string>
                        extip: <value of string>
                        extport: <value of string>
                        gratuitous-arp-interval: <value of integer>
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
                        mapped-addr: <value of string>
                        mappedip:
                          - <value of string>
                        mappedport: <value of string>
                        max-embryonic-connections: <value of integer>
                        monitor:
                          - <value of string>
                        nat-source-vip: <value in [disable, enable]>
                        outlook-web-access: <value in [disable, enable]>
                        persistence: <value in [none, http-cookie, ssl-session-id]>
                        portforward: <value in [disable, enable]>
                        portmapping-type: <value in [1-to-1, m-to-n]>
                        protocol: <value in [tcp, udp, sctp, ...]>
                        realservers:
                          -
                              client-ip:
                                - <value of string>
                              healthcheck: <value in [disable, enable, vip]>
                              holddown-interval: <value of integer>
                              http-host: <value of string>
                              ip: <value of string>
                              max-connections: <value of integer>
                              monitor: <value of string>
                              port: <value of integer>
                              seq: <value of integer>
                              status: <value in [active, standby, disable]>
                              weight: <value of integer>
                        server-type: <value in [http, https, ssl, ...]>
                        service: <value of string>
                        src-filter:
                          - <value of string>
                        srcintf-filter:
                          - <value of string>
                        ssl-algorithm: <value in [high, medium, low, ...]>
                        ssl-certificate: <value of string>
                        ssl-cipher-suites:
                          -
                              cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                              id: <value of integer>
                              versions:
                                - <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
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
                        type: <value in [static-nat, load-balance, server-load-balance, ...]>
                        uuid: <value of string>
                        weblogic-server: <value in [disable, enable]>
                        websphere-server: <value in [disable, enable]>
                  extaddr: <value of string>
                  extintf: <value of string>
                  extip: <value of string>
                  extport: <value of string>
                  gratuitous-arp-interval: <value of integer>
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
                  mapped-addr: <value of string>
                  mappedip:
                    - <value of string>
                  mappedport: <value of string>
                  max-embryonic-connections: <value of integer>
                  monitor: <value of string>
                  name: <value of string>
                  nat-source-vip: <value in [disable, enable]>
                  outlook-web-access: <value in [disable, enable]>
                  persistence: <value in [none, http-cookie, ssl-session-id]>
                  portforward: <value in [disable, enable]>
                  portmapping-type: <value in [1-to-1, m-to-n]>
                  protocol: <value in [tcp, udp, sctp, ...]>
                  realservers:
                    -
                        client-ip:
                          - <value of string>
                        healthcheck: <value in [disable, enable, vip]>
                        holddown-interval: <value of integer>
                        http-host: <value of string>
                        ip: <value of string>
                        max-connections: <value of integer>
                        monitor: <value of string>
                        port: <value of integer>
                        seq: <value of integer>
                        status: <value in [active, standby, disable]>
                        weight: <value of integer>
                  server-type: <value in [http, https, ssl, ...]>
                  service: <value of string>
                  src-filter:
                    - <value of string>
                  srcintf-filter: <value of string>
                  ssl-algorithm: <value in [high, medium, low, ...]>
                  ssl-certificate: <value of string>
                  ssl-cipher-suites:
                    -
                        cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                        id: <value of integer>
                        versions:
                          - <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
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
                          - <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-server-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-server-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-server-session-state-max: <value of integer>
                  ssl-server-session-state-timeout: <value of integer>
                  ssl-server-session-state-type: <value in [disable, time, count, ...]>
                  type: <value in [static-nat, load-balance, server-load-balance, ...]>
                  uuid: <value of string>
                  weblogic-server: <value in [disable, enable]>
                  websphere-server: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP/{VIP}
      fmgr_firewall_vip_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP/{VIP}
      fmgr_firewall_vip_obj:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, move, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip/{vip}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> arp-reply </span> - Enable to respond to ARP requests for this virtual IP address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - Color of icon on the GUI. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-mapping-ttl </span> - DNS mapping TTL (Set to zero to use TTL in DNS response, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> arp-reply </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-mapping-ttl </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> extaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extintf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gratuitous-arp-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-age </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-domain </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-domain-from-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-generation </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-path </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-share </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-ip-header </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-ip-header-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-multiplex </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> https-cookie-secure </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldb-method </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mapped-addr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mappedport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-embryonic-connections </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> nat-source-vip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outlook-web-access </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> persistence </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portforward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portmapping-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> realservers </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> client-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> healthcheck </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> holddown-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-connections </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> seq </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weight </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> server-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> srcintf-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ssl-algorithm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-certificate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-cipher-suites </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> cipher </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> versions </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> ssl-client-fallback </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-renegotiation </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-max </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-dh-bits </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-age </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-backup </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-include-subdomains </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-primary </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-report-uri </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hsts </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hsts-age </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-hsts-include-subdomains </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-http-location-conversion </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-http-match-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-max-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-pfs </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-send-empty-frags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-algorithm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-max-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-min-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-max </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weblogic-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> websphere-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> extaddr </span> - External FQDN address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extintf </span> - Interface connected to the source network that receives the packets that will be forwarded to the destination network. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extip </span> - IP address or address range on the external interface that you want to map to an address or address range on the destination network. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extport </span> - Incoming port number range that you want to map to a port number range on the destination network. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gratuitous-arp-interval </span> - Enable to have the VIP send gratuitous ARPs. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-age </span> - Time in minutes that client web browsers should keep a cookie. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-domain </span> - Domain that HTTP cookie persistence should apply to. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-domain-from-host </span> - Enable/disable use of HTTP cookie domain from host field in HTTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-generation </span> - Generation of HTTP cookie to be accepted. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-path </span> - Limit HTTP cookie persistence to the specified path. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-share </span> - Control sharing of cookies across virtual servers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-ip-header </span> - For HTTP multiplexing, enable to add the original client IP address in the XForwarded-For HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-ip-header-name </span> - For HTTP multiplexing, enter a custom HTTPS header name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-multiplex </span> - Enable/disable HTTP multiplexing. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> https-cookie-secure </span> - Enable/disable verification that inserted HTTPS cookies are secure. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Custom defined ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldb-method </span> - Method used to distribute sessions to real servers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mapped-addr </span> - Mapped FQDN address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mappedport </span> - Port number range on the destination network to which the external port number range is mapped. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-embryonic-connections </span> - Maximum number of incomplete connections. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor </span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Virtual IP name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nat-source-vip </span> - Enable/disable forcing the source NAT mapped IP to the external IP for all traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outlook-web-access </span> - Enable to add the Front-End-Https header for Microsoft Outlook Web Access. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> persistence </span> - Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portforward </span> - Enable/disable port forwarding. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portmapping-type </span> - Port mapping type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol to use when forwarding packets. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> realservers </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> client-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> healthcheck </span> - Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> holddown-interval </span> - Time in seconds that the health check monitor continues to monitor and unresponsive server that should be active. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-host </span> - HTTP server domain name in HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - IP address of the real server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-connections </span> - Max number of active connections that can be directed to the real server. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor </span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Port for communicating with the real server. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> seq </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weight </span> - Weight of the real server. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> server-type </span> - Protocol to be load balanced by the virtual server (also called the server load balance virtual IP). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - Service name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> srcintf-filter </span> - Interfaces to which the VIP applies. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-algorithm </span> - Permitted encryption algorithms for SSL sessions according to encryption strength. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-certificate </span> - The name of the SSL certificate to use for SSL acceleration. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-cipher-suites </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> cipher </span> - Cipher suite name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> versions </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> ssl-client-fallback </span> - Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-renegotiation </span> - Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-max </span> - Maximum number of client to FortiGate SSL session states to keep. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-timeout </span> - Number of minutes to keep client to FortiGate SSL session state. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-type </span> - How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-dh-bits </span> - Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp </span> - Enable/disable including HPKP header in response. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-age </span> - Number of seconds the client should honour the HPKP setting. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-backup </span> - Certificate to generate backup HPKP pin from. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-include-subdomains </span> - Indicate that HPKP header applies to all subdomains. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-primary </span> - Certificate to generate primary HPKP pin from. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-report-uri </span> - URL to report HPKP violations to. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hsts </span> - Enable/disable including HSTS header in response. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hsts-age </span> - Number of seconds the client should honour the HSTS setting. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-hsts-include-subdomains </span> - Indicate that HSTS header applies to all subdomains. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-http-location-conversion </span> - Enable to replace HTTP with HTTPS in the replys Location HTTP header field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-http-match-host </span> - Enable/disable HTTP host matching for location conversion. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-max-version </span> - Highest SSL/TLS version acceptable from a client. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-version </span> - Lowest SSL/TLS version acceptable from a client. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mode </span> - Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-pfs </span> - Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-send-empty-frags </span> - Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-algorithm </span> - Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-cipher-suites </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> cipher </span> - Cipher suite name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - SSL/TLS cipher suites priority. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> versions </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> ssl-server-max-version </span> - Highest SSL/TLS version acceptable from a server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-min-version </span> - Lowest SSL/TLS version acceptable from a server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-max </span> - Maximum number of FortiGate to Server SSL session states to keep. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-timeout </span> - Number of minutes to keep FortiGate to Server SSL session state. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-type </span> - How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Configure a static NAT, load balance, DNS translation, or FQDN VIP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weblogic-server </span> - Enable to add an HTTP header to indicate SSL offloading for a WebLogic server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> websphere-server </span> - Enable to add an HTTP header to indicate SSL offloading for a WebSphere server. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip/{vip}</span>  </li>
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



