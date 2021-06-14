:source: fmgr_fsp_vlan_interface.py

:orphan:

.. _fmgr_fsp_vlan_interface:

fmgr_fsp_vlan_interface -- Configure interfaces.
++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>fsp_vlan_interface</td>
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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vlan</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">fsp_vlan_interface</span> - Configure interfaces. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ac-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">aggregate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">algorithm</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [L2, L3, L4]</span> </li>
 <li><span class="li-head">alias</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric]</span> </li>
 <li><span class="li-head">ap-discover</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">arpforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">atm-protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, ipoa]</span> </li>
 <li><span class="li-head">auth-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span> </li>
 <li><span class="li-head">auto-auth-extension-device</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bfd</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, enable, disable]</span> </li>
 <li><span class="li-head">bfd-desired-min-tx</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bfd-detect-mult</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bfd-required-min-rx</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">broadcast-forticlient-discovery</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">broadcast-forward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">captive-portal</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">cli-conn-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tsig]</span> </li>
 <li><span class="li-head">ddns-domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-keyname</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">ddns-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhs.org, dyndns.org, dyns.net, tzo.com, ods.org, vavic.com, now.net.cn, dipdns.net, easydns.com, genericDDNS]</span> </li>
 <li><span class="li-head">ddns-server-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-sn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns-username</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dedicated-to</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, management]</span> </li>
 <li><span class="li-head">defaultgw</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detected-peer-mtu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detectprotocol</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> </li>
 <li><span class="li-head">detectserver</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-access-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-identification</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">device-identification-active-scan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">device-netscan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">device-user-identification</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">devindex</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp-client-identifier</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-relay-agent-option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">dhcp-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span> </li>
 <li><span class="li-head">dhcp-renew-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">disc-retry-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">disconnect-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">distance</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dns-query</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, recursive, non-recursive]</span> </li>
 <li><span class="li-head">dns-server-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drop-fragment</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drop-overlapped-fragment</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">egress-cos</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span> </li>
 <li><span class="li-head">egress-shaping-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">endpoint-compliance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">estimated-downstream-bandwidth</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">estimated-upstream-bandwidth</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">explicit-ftp-proxy</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">explicit-web-proxy</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fail-action-on-extender</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [soft-restart, hard-restart, reboot]</span> </li>
 <li><span class="li-head">fail-alert-interfaces</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fail-alert-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [link-failed-signal, link-down]</span> </li>
 <li><span class="li-head">fail-detect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fail-detect-option</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [detectserver, link-down]</span> </li>
 <li><span class="li-head">fdp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortiheartbeat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortilink</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortilink-backup-link</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortilink-split-interface</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortilink-stacking</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">forward-domain</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">forward-error-correction</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, rs-fec, base-r-fec, fec-cl91, fec-cl74]</span> </li>
 <li><span class="li-head">fp-anomaly</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [drop_tcp_fin_noack, pass_winnuke, pass_tcpland, pass_udpland, pass_icmpland, pass_ipland, pass_iprr, pass_ipssrr, pass_iplsrr, pass_ipstream, pass_ipsecurity, pass_iptimestamp, pass_ipunknown_option, pass_ipunknown_prot, pass_icmp_frag, pass_tcp_no_flag, pass_tcp_fin_noack, drop_winnuke, drop_tcpland, drop_udpland, drop_icmpland, drop_ipland, drop_iprr, drop_ipssrr, drop_iplsrr, drop_ipstream, drop_ipsecurity, drop_iptimestamp, drop_ipunknown_option, drop_ipunknown_prot, drop_icmp_frag, drop_tcp_no_flag]</span> </li>
 <li><span class="li-head">fp-disable</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [all, ipsec, none]</span> </li>
 <li><span class="li-head">gateway-address</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gi-gk</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gwaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gwdetect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ha-priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">icmp-accept-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icmp-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icmp-send-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ident-accept</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">idle-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">if-mdix</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, normal, crossover]</span> </li>
 <li><span class="li-head">if-media</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, copper, fiber]</span> </li>
 <li><span class="li-head">in-force-vlan-cos</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">inbandwidth</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ingress-cos</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">internal</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipmac</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sniffer-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipunnumbered</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">autoconf</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-client-options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span> </li>
 <li><span class="li-head">dhcp6-information-request</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-delegation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-plt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-vlt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span> </li>
 <li><span class="li-head">ip6-address</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric, https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric]</span> </li>
 <li><span class="li-head">ip6-default-life</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-dns-server-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-hop-limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-link-mtu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-manage-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-max-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-min-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span> </li>
 <li><span class="li-head">ip6-other-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-reachable-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-retrans-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-send-adv</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-upstream-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cga-modifier</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [basic, SEND-compatible]</span> </li>
 <li><span class="li-head">nd-security-level</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-delta</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-fuzz</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip6_link_local</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vrrp-virtual-mac6</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-delegated-prefix-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">onlink-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">prefix-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rdnss</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">rdnss-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [delegated, default, specify]</span> </li>
 <li><span class="li-head">subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">upstream-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ip6-extra-addr</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">prefix</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ip6-prefix-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dnssl</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">onlink-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">preferred-life-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">prefix</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rdnss</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">valid-life-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">vrrp6</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">adv-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preempt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vrdst6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vrgrp</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">cli-conn6-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">icmp6-send-redirect</span> - Enable/disable sending of ICMPv6 redirects. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">interface-identifier</span> - IPv6 interface identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-prefix-mode</span> - Assigning a prefix from DHCP or RA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhcp6, ra]</span> </li>
 <li><span class="li-head">ra-send-mtu</span> - Enable/disable sending link MTU in RA packet. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">unique-autoconf-addr</span> - Enable/disable unique auto config address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">l2forward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">l2tp-client</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-ha-slave</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, passive, active]</span> </li>
 <li><span class="li-head">lacp-speed</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slow, fast]</span> </li>
 <li><span class="li-head">lcp-echo-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lcp-max-echo-fails</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-up-delay</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">listen-forticlient-connection</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lldp-network-policy</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">lldp-reception</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vdom]</span> </li>
 <li><span class="li-head">lldp-transmission</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable, vdom]</span> </li>
 <li><span class="li-head">log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">macaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">management-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-egress-burst-rate</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-egress-rate</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mediatype</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [serdes-sfp, sgmii-sfp, cfp2-sr10, cfp2-lr4, serdes-copper-sfp, sr, cr, lr, qsfp28-sr4, qsfp28-lr4, qsfp28-cr4, sr4, cr4, lr4]</span> </li>
 <li><span class="li-head">member</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">min-links</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">min-links-down</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [operational, administrative]</span> </li>
 <li><span class="li-head">mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, pppoa, ipoa, eoa]</span> </li>
 <li><span class="li-head">mtu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mtu-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mux-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [llc-encaps, vc-encaps]</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ndiscforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">netbios-forward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">netflow-sampler</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tx, rx, both]</span> </li>
 <li><span class="li-head">npu-fastpath</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nst</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">out-force-vlan-cos</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbandwidth</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">padt-retry-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">peer-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">phy-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, adsl, vdsl]</span> </li>
 <li><span class="li-head">ping-serv-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poe</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">polling-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pppoe-unnumbered-negotiate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pptp-auth-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span> </li>
 <li><span class="li-head">pptp-client</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pptp-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">pptp-server-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pptp-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pptp-user</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">preserve-session-route</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">proxy-captive-portal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">redundant-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">retransmission</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">role</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [lan, wan, dmz, undefined]</span> </li>
 <li><span class="li-head">sample-direction</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rx, tx, both]</span> </li>
 <li><span class="li-head">sample-rate</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">secondary-IP</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">secondaryip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric]</span> </li>
 <li><span class="li-head">detectprotocol</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> </li>
 <li><span class="li-head">detectserver</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gwdetect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ha-priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ping-serv-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">security-8021x-dynamic-vlan-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-8021x-master</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-8021x-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, dynamic-vlan, fallback, slave]</span> </li>
 <li><span class="li-head">security-exempt-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-external-logout</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-external-web</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-mac-auth-bypass</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, mac-auth-only]</span> </li>
 <li><span class="li-head">security-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, captive-portal, 802.1X]</span> </li>
 <li><span class="li-head">security-redirect-url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sflow-sampler</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">speed</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, 10full, 10half, 100full, 100half, 1000full, 1000half, 10000full, 1000auto, 10000auto, 40000full, 100Gfull, 25000full, 40000auto, 25000auto, 100Gauto]</span> </li>
 <li><span class="li-head">spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">src-check</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [down, up]</span> </li>
 <li><span class="li-head">stp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">stp-ha-slave</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, priority-adjust]</span> </li>
 <li><span class="li-head">stpforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">stpforward-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]</span> </li>
 <li><span class="li-head">strip-priority-vlan-tag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">subst</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">substitute-dst-mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-access-vlan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-arp-inspection</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [radius, usergroup]</span> </li>
 <li><span class="li-head">switch-controller-dhcp-snooping</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-dhcp-snooping-option82</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-dhcp-snooping-verify-mac</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-igmp-snooping</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-learning-limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch-controller-radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-traffic-policy</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tc-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ptm, atm]</span> </li>
 <li><span class="li-head">tcp-mss</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trunk</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">trust-ip-1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip-2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip-3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip6-1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip6-2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip6-3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [physical, vlan, aggregate, redundant, tunnel, wireless, vdom-link, loopback, switch, hard-switch, hdlc, vap-switch, wl-mesh, fortilink, switch-vlan, fctrl-trunk, tdm, fext-wan, vxlan, emac-vlan, geneve, ssl]</span> </li>
 <li><span class="li-head">username</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vci</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vectoring</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vindex</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vlanforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vlanid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vpi</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrf</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrrp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">adv-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ignore-default-route</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">preempt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [2, 3]</span> </li>
 <li><span class="li-head">vrdst</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">vrdst-priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrgrp</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">vrrp-virtual-mac</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wccp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-5g-threshold</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-acl</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">wifi-ap-band</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, 5g-preferred, 5g-only]</span> </li>
 <li><span class="li-head">wifi-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [PSK, RADIUS, radius, usergroup]</span> </li>
 <li><span class="li-head">wifi-auto-connect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-auto-save</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-broadcast-ssid</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-encrypt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TKIP, AES]</span> </li>
 <li><span class="li-head">wifi-fragment-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-key</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">wifi-keyindex</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-mac-filter</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-passphrase</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">wifi-radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-rts-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-security</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise]</span> </li>
 <li><span class="li-head">wifi-ssid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-usergroup</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">eip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortilink-neighbor-detect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [lldp, fortilink]</span> </li>
 <li><span class="li-head">ingress-shaping-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ring-rx</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ring-tx</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bandwidth-measure-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-managed-by-fortiipam</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">managed-subnetwork-size</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]</span> </li>
 <li><span class="li-head">measured-downstream-bandwidth</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">measured-upstream-bandwidth</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor-bandwidth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">swc-vlan</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch-controller-feature</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, default-vlan, quarantine, sniffer, voice, camera, rspan, video, nac]</span> </li>
 <li><span class="li-head">switch-controller-igmp-snooping-fast-leave</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-igmp-snooping-proxy</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-mgmt-vlan</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch-controller-nac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-rspan-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vlan-protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [8021q, 8021ad]</span> </li>
 <li><span class="li-head">dhcp-relay-interface</span> - Specify outgoing interface to reach server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-relay-interface-select-method</span> - Specify how to select outgoing interface to reach server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span> </li>
 <li><span class="li-head">dhcp-relay-request-all-server</span> - Enable/disable sending of DHCP requests to all servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">np-qos-profile</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">stp-ha-secondary</span> - Control STP behaviour on HA secondary. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, priority-adjust]</span> </li>
 <li><span class="li-head">swc-first-create</span> - Initial create for switch-controller VLANs. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch-controller-dynamic</span> - Integrated FortiLink settings for managed FortiSwitch. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-iot-scanning</span> - Enable/disable managed FortiSwitch IoT scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-source-ip</span> - Source IP address used in FortiLink over L3 connections. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [outbound, fixed]</span> </li>
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
    - name: Configure interfaces.
      fmgr_fsp_vlan_interface:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vlan: <your own value>
         fsp_vlan_interface:
            ac-name: <value of string>
            aggregate: <value of string>
            algorithm: <value in [L2, L3, L4]>
            alias: <value of string>
            allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
              - dnp
              - ftm
              - fabric
            ap-discover: <value in [disable, enable]>
            arpforward: <value in [disable, enable]>
            atm-protocol: <value in [none, ipoa]>
            auth-type: <value in [auto, pap, chap, ...]>
            auto-auth-extension-device: <value in [disable, enable]>
            bfd: <value in [global, enable, disable]>
            bfd-desired-min-tx: <value of integer>
            bfd-detect-mult: <value of integer>
            bfd-required-min-rx: <value of integer>
            broadcast-forticlient-discovery: <value in [disable, enable]>
            broadcast-forward: <value in [disable, enable]>
            captive-portal: <value of integer>
            cli-conn-status: <value of integer>
            color: <value of integer>
            ddns: <value in [disable, enable]>
            ddns-auth: <value in [disable, tsig]>
            ddns-domain: <value of string>
            ddns-key: <value of string>
            ddns-keyname: <value of string>
            ddns-password: <value of string>
            ddns-server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
            ddns-server-ip: <value of string>
            ddns-sn: <value of string>
            ddns-ttl: <value of integer>
            ddns-username: <value of string>
            ddns-zone: <value of string>
            dedicated-to: <value in [none, management]>
            defaultgw: <value in [disable, enable]>
            description: <value of string>
            detected-peer-mtu: <value of integer>
            detectprotocol:
              - ping
              - tcp-echo
              - udp-echo
            detectserver: <value of string>
            device-access-list: <value of string>
            device-identification: <value in [disable, enable]>
            device-identification-active-scan: <value in [disable, enable]>
            device-netscan: <value in [disable, enable]>
            device-user-identification: <value in [disable, enable]>
            devindex: <value of integer>
            dhcp-client-identifier: <value of string>
            dhcp-relay-agent-option: <value in [disable, enable]>
            dhcp-relay-ip: <value of string>
            dhcp-relay-service: <value in [disable, enable]>
            dhcp-relay-type: <value in [regular, ipsec]>
            dhcp-renew-time: <value of integer>
            disc-retry-timeout: <value of integer>
            disconnect-threshold: <value of integer>
            distance: <value of integer>
            dns-query: <value in [disable, recursive, non-recursive]>
            dns-server-override: <value in [disable, enable]>
            drop-fragment: <value in [disable, enable]>
            drop-overlapped-fragment: <value in [disable, enable]>
            egress-cos: <value in [disable, cos0, cos1, ...]>
            egress-shaping-profile: <value of string>
            endpoint-compliance: <value in [disable, enable]>
            estimated-downstream-bandwidth: <value of integer>
            estimated-upstream-bandwidth: <value of integer>
            explicit-ftp-proxy: <value in [disable, enable]>
            explicit-web-proxy: <value in [disable, enable]>
            external: <value in [disable, enable]>
            fail-action-on-extender: <value in [soft-restart, hard-restart, reboot]>
            fail-alert-interfaces: <value of string>
            fail-alert-method: <value in [link-failed-signal, link-down]>
            fail-detect: <value in [disable, enable]>
            fail-detect-option:
              - detectserver
              - link-down
            fdp: <value in [disable, enable]>
            fortiheartbeat: <value in [disable, enable]>
            fortilink: <value in [disable, enable]>
            fortilink-backup-link: <value of integer>
            fortilink-split-interface: <value in [disable, enable]>
            fortilink-stacking: <value in [disable, enable]>
            forward-domain: <value of integer>
            forward-error-correction: <value in [disable, enable, rs-fec, ...]>
            fp-anomaly:
              - drop_tcp_fin_noack
              - pass_winnuke
              - pass_tcpland
              - pass_udpland
              - pass_icmpland
              - pass_ipland
              - pass_iprr
              - pass_ipssrr
              - pass_iplsrr
              - pass_ipstream
              - pass_ipsecurity
              - pass_iptimestamp
              - pass_ipunknown_option
              - pass_ipunknown_prot
              - pass_icmp_frag
              - pass_tcp_no_flag
              - pass_tcp_fin_noack
              - drop_winnuke
              - drop_tcpland
              - drop_udpland
              - drop_icmpland
              - drop_ipland
              - drop_iprr
              - drop_ipssrr
              - drop_iplsrr
              - drop_ipstream
              - drop_ipsecurity
              - drop_iptimestamp
              - drop_ipunknown_option
              - drop_ipunknown_prot
              - drop_icmp_frag
              - drop_tcp_no_flag
            fp-disable:
              - all
              - ipsec
              - none
            gateway-address: <value of string>
            gi-gk: <value in [disable, enable]>
            gwaddr: <value of string>
            gwdetect: <value in [disable, enable]>
            ha-priority: <value of integer>
            icmp-accept-redirect: <value in [disable, enable]>
            icmp-redirect: <value in [disable, enable]>
            icmp-send-redirect: <value in [disable, enable]>
            ident-accept: <value in [disable, enable]>
            idle-timeout: <value of integer>
            if-mdix: <value in [auto, normal, crossover]>
            if-media: <value in [auto, copper, fiber]>
            in-force-vlan-cos: <value of integer>
            inbandwidth: <value of integer>
            ingress-cos: <value in [disable, cos0, cos1, ...]>
            ingress-spillover-threshold: <value of integer>
            internal: <value of integer>
            ip: <value of string>
            ipmac: <value in [disable, enable]>
            ips-sniffer-mode: <value in [disable, enable]>
            ipunnumbered: <value of string>
            ipv6:
               autoconf: <value in [disable, enable]>
               dhcp6-client-options:
                 - rapid
                 - iapd
                 - iana
                 - dns
                 - dnsname
               dhcp6-information-request: <value in [disable, enable]>
               dhcp6-prefix-delegation: <value in [disable, enable]>
               dhcp6-prefix-hint: <value of string>
               dhcp6-prefix-hint-plt: <value of integer>
               dhcp6-prefix-hint-vlt: <value of integer>
               dhcp6-relay-ip: <value of string>
               dhcp6-relay-service: <value in [disable, enable]>
               dhcp6-relay-type: <value in [regular]>
               ip6-address: <value of string>
               ip6-allowaccess:
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - capwap
                 - fabric
               ip6-default-life: <value of integer>
               ip6-dns-server-override: <value in [disable, enable]>
               ip6-hop-limit: <value of integer>
               ip6-link-mtu: <value of integer>
               ip6-manage-flag: <value in [disable, enable]>
               ip6-max-interval: <value of integer>
               ip6-min-interval: <value of integer>
               ip6-mode: <value in [static, dhcp, pppoe, ...]>
               ip6-other-flag: <value in [disable, enable]>
               ip6-reachable-time: <value of integer>
               ip6-retrans-time: <value of integer>
               ip6-send-adv: <value in [disable, enable]>
               ip6-subnet: <value of string>
               ip6-upstream-interface: <value of string>
               nd-cert: <value of string>
               nd-cga-modifier: <value of string>
               nd-mode: <value in [basic, SEND-compatible]>
               nd-security-level: <value of integer>
               nd-timestamp-delta: <value of integer>
               nd-timestamp-fuzz: <value of integer>
               vrip6_link_local: <value of string>
               vrrp-virtual-mac6: <value in [disable, enable]>
               ip6-delegated-prefix-list:
                 -
                     autonomous-flag: <value in [disable, enable]>
                     onlink-flag: <value in [disable, enable]>
                     prefix-id: <value of integer>
                     rdnss: <value of string>
                     rdnss-service: <value in [delegated, default, specify]>
                     subnet: <value of string>
                     upstream-interface: <value of string>
               ip6-extra-addr:
                 -
                     prefix: <value of string>
               ip6-prefix-list:
                 -
                     autonomous-flag: <value in [disable, enable]>
                     dnssl: <value of string>
                     onlink-flag: <value in [disable, enable]>
                     preferred-life-time: <value of integer>
                     prefix: <value of string>
                     rdnss: <value of string>
                     valid-life-time: <value of integer>
               vrrp6:
                 -
                     accept-mode: <value in [disable, enable]>
                     adv-interval: <value of integer>
                     preempt: <value in [disable, enable]>
                     priority: <value of integer>
                     start-time: <value of integer>
                     status: <value in [disable, enable]>
                     vrdst6: <value of string>
                     vrgrp: <value of integer>
                     vrid: <value of integer>
                     vrip6: <value of string>
               cli-conn6-status: <value of integer>
               icmp6-send-redirect: <value in [disable, enable]>
               interface-identifier: <value of string>
               ip6-prefix-mode: <value in [dhcp6, ra]>
               ra-send-mtu: <value in [disable, enable]>
               unique-autoconf-addr: <value in [disable, enable]>
            l2forward: <value in [disable, enable]>
            l2tp-client: <value in [disable, enable]>
            lacp-ha-slave: <value in [disable, enable]>
            lacp-mode: <value in [static, passive, active]>
            lacp-speed: <value in [slow, fast]>
            lcp-echo-interval: <value of integer>
            lcp-max-echo-fails: <value of integer>
            link-up-delay: <value of integer>
            listen-forticlient-connection: <value in [disable, enable]>
            lldp-network-policy: <value of string>
            lldp-reception: <value in [disable, enable, vdom]>
            lldp-transmission: <value in [enable, disable, vdom]>
            log: <value in [disable, enable]>
            macaddr: <value of string>
            management-ip: <value of string>
            max-egress-burst-rate: <value of integer>
            max-egress-rate: <value of integer>
            mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
            member: <value of string>
            min-links: <value of integer>
            min-links-down: <value in [operational, administrative]>
            mode: <value in [static, dhcp, pppoe, ...]>
            mtu: <value of integer>
            mtu-override: <value in [disable, enable]>
            mux-type: <value in [llc-encaps, vc-encaps]>
            name: <value of string>
            ndiscforward: <value in [disable, enable]>
            netbios-forward: <value in [disable, enable]>
            netflow-sampler: <value in [disable, tx, rx, ...]>
            npu-fastpath: <value in [disable, enable]>
            nst: <value in [disable, enable]>
            out-force-vlan-cos: <value of integer>
            outbandwidth: <value of integer>
            padt-retry-timeout: <value of integer>
            password: <value of string>
            peer-interface: <value of string>
            phy-mode: <value in [auto, adsl, vdsl]>
            ping-serv-status: <value of integer>
            poe: <value in [disable, enable]>
            polling-interval: <value of integer>
            pppoe-unnumbered-negotiate: <value in [disable, enable]>
            pptp-auth-type: <value in [auto, pap, chap, ...]>
            pptp-client: <value in [disable, enable]>
            pptp-password: <value of string>
            pptp-server-ip: <value of string>
            pptp-timeout: <value of integer>
            pptp-user: <value of string>
            preserve-session-route: <value in [disable, enable]>
            priority: <value of integer>
            priority-override: <value in [disable, enable]>
            proxy-captive-portal: <value in [disable, enable]>
            redundant-interface: <value of string>
            remote-ip: <value of string>
            replacemsg-override-group: <value of string>
            retransmission: <value in [disable, enable]>
            role: <value in [lan, wan, dmz, ...]>
            sample-direction: <value in [rx, tx, both]>
            sample-rate: <value of integer>
            scan-botnet-connections: <value in [disable, block, monitor]>
            secondary-IP: <value in [disable, enable]>
            secondaryip:
              -
                  allowaccess:
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - auto-ipsec
                    - radius-acct
                    - probe-response
                    - capwap
                    - dnp
                    - ftm
                    - fabric
                  detectprotocol:
                    - ping
                    - tcp-echo
                    - udp-echo
                  detectserver: <value of string>
                  gwdetect: <value in [disable, enable]>
                  ha-priority: <value of integer>
                  id: <value of integer>
                  ip: <value of string>
                  ping-serv-status: <value of integer>
                  seq: <value of integer>
            security-8021x-dynamic-vlan-id: <value of integer>
            security-8021x-master: <value of string>
            security-8021x-mode: <value in [default, dynamic-vlan, fallback, ...]>
            security-exempt-list: <value of string>
            security-external-logout: <value of string>
            security-external-web: <value of string>
            security-groups: <value of string>
            security-mac-auth-bypass: <value in [disable, enable, mac-auth-only]>
            security-mode: <value in [none, captive-portal, 802.1X]>
            security-redirect-url: <value of string>
            service-name: <value of string>
            sflow-sampler: <value in [disable, enable]>
            speed: <value in [auto, 10full, 10half, ...]>
            spillover-threshold: <value of integer>
            src-check: <value in [disable, enable]>
            status: <value in [down, up]>
            stp: <value in [disable, enable]>
            stp-ha-slave: <value in [disable, enable, priority-adjust]>
            stpforward: <value in [disable, enable]>
            stpforward-mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
            strip-priority-vlan-tag: <value in [disable, enable]>
            subst: <value in [disable, enable]>
            substitute-dst-mac: <value of string>
            switch: <value of string>
            switch-controller-access-vlan: <value in [disable, enable]>
            switch-controller-arp-inspection: <value in [disable, enable]>
            switch-controller-auth: <value in [radius, usergroup]>
            switch-controller-dhcp-snooping: <value in [disable, enable]>
            switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
            switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
            switch-controller-igmp-snooping: <value in [disable, enable]>
            switch-controller-learning-limit: <value of integer>
            switch-controller-radius-server: <value of string>
            switch-controller-traffic-policy: <value of string>
            tc-mode: <value in [ptm, atm]>
            tcp-mss: <value of integer>
            trunk: <value in [disable, enable]>
            trust-ip-1: <value of string>
            trust-ip-2: <value of string>
            trust-ip-3: <value of string>
            trust-ip6-1: <value of string>
            trust-ip6-2: <value of string>
            trust-ip6-3: <value of string>
            type: <value in [physical, vlan, aggregate, ...]>
            username: <value of string>
            vci: <value of integer>
            vectoring: <value in [disable, enable]>
            vindex: <value of integer>
            vlanforward: <value in [disable, enable]>
            vlanid: <value of integer>
            vpi: <value of integer>
            vrf: <value of integer>
            vrrp:
              -
                  accept-mode: <value in [disable, enable]>
                  adv-interval: <value of integer>
                  ignore-default-route: <value in [disable, enable]>
                  preempt: <value in [disable, enable]>
                  priority: <value of integer>
                  start-time: <value of integer>
                  status: <value in [disable, enable]>
                  version: <value in [2, 3]>
                  vrdst: <value of string>
                  vrdst-priority: <value of integer>
                  vrgrp: <value of integer>
                  vrid: <value of integer>
                  vrip: <value of string>
            vrrp-virtual-mac: <value in [disable, enable]>
            wccp: <value in [disable, enable]>
            weight: <value of integer>
            wifi-5g-threshold: <value of string>
            wifi-acl: <value in [deny, allow]>
            wifi-ap-band: <value in [any, 5g-preferred, 5g-only]>
            wifi-auth: <value in [PSK, RADIUS, radius, ...]>
            wifi-auto-connect: <value in [disable, enable]>
            wifi-auto-save: <value in [disable, enable]>
            wifi-broadcast-ssid: <value in [disable, enable]>
            wifi-encrypt: <value in [TKIP, AES]>
            wifi-fragment-threshold: <value of integer>
            wifi-key: <value of string>
            wifi-keyindex: <value of integer>
            wifi-mac-filter: <value in [disable, enable]>
            wifi-passphrase: <value of string>
            wifi-radius-server: <value of string>
            wifi-rts-threshold: <value of integer>
            wifi-security: <value in [None, WEP64, wep64, ...]>
            wifi-ssid: <value of string>
            wifi-usergroup: <value of string>
            wins-ip: <value of string>
            eip: <value of string>
            fortilink-neighbor-detect: <value in [lldp, fortilink]>
            ingress-shaping-profile: <value of string>
            ring-rx: <value of integer>
            ring-tx: <value of integer>
            bandwidth-measure-time: <value of integer>
            ip-managed-by-fortiipam: <value in [disable, enable]>
            managed-subnetwork-size: <value in [256, 512, 1024, ...]>
            measured-downstream-bandwidth: <value of integer>
            measured-upstream-bandwidth: <value of integer>
            monitor-bandwidth: <value in [disable, enable]>
            swc-vlan: <value of integer>
            switch-controller-feature: <value in [none, default-vlan, quarantine, ...]>
            switch-controller-igmp-snooping-fast-leave: <value in [disable, enable]>
            switch-controller-igmp-snooping-proxy: <value in [disable, enable]>
            switch-controller-mgmt-vlan: <value of integer>
            switch-controller-nac: <value of string>
            switch-controller-rspan-mode: <value in [disable, enable]>
            vlan-protocol: <value in [8021q, 8021ad]>
            dhcp-relay-interface: <value of string>
            dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
            dhcp-relay-request-all-server: <value in [disable, enable]>
            np-qos-profile: <value of integer>
            stp-ha-secondary: <value in [disable, enable, priority-adjust]>
            swc-first-create: <value of integer>
            switch-controller-dynamic: <value of string>
            switch-controller-iot-scanning: <value in [disable, enable]>
            switch-controller-source-ip: <value in [outbound, fixed]>



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



