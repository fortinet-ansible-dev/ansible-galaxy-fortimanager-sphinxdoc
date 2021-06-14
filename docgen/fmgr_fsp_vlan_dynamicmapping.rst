:source: fmgr_fsp_vlan_dynamicmapping.py

:orphan:

.. _fmgr_fsp_vlan_dynamicmapping:

fmgr_fsp_vlan_dynamicmapping
++++++++++++++++++++++++++++

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
 <td>fsp_vlan_dynamicmapping</td>
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
 <li><span class="li-head">vlan</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">fsp_vlan_dynamicmapping</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_dhcp-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">dhcp-server</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">auto-configuration</span> - Enable/disable auto configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-managed-status</span> - Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">conflicted-ip-timeout</span> - Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns-auth</span> - DDNS authentication mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tsig]</span> </li>
 <li><span class="li-head">ddns-key</span> - DDNS update key (base 64 encoding). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-keyname</span> - DDNS update key name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-server-ip</span> - DDNS server IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-ttl</span> - TTL. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns-update</span> - Enable/disable DDNS update for DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-update-override</span> - Enable/disable DDNS update override for DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-zone</span> - Zone of your domain name (ex. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">default-gateway</span> - Default gateway IP address assigned by the DHCP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-settings-from-fortiipam</span> - Enable/disable populating of DHCP server settings from FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dns-server1</span> - DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server2</span> - DNS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server3</span> - DNS server 3. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server4</span> - DNS server 4. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-service</span> - Options for assigning DNS servers to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">domain</span> - Domain name suffix for the IP addresses that the DHCP server assigns to clients. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">enable</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">exclude-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - End of IP range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - Start of IP range. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">filename</span> - Name of the boot file on the TFTP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">forticlient-on-net-status</span> - Enable/disable FortiClient-On-Net service for this DHCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-mode</span> - Method used to assign client IP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, usrgrp]</span> </li>
 <li><span class="li-head">ip-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - End of IP range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - Start of IP range. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipsec-lease-hold</span> - DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lease-time</span> - Lease time in seconds, 0 means unlimited. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mac-acl-default-action</span> - MAC access control default action (allow or block assigning IP settings). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block]</span> </li>
 <li><span class="li-head">netmask</span> - Netmask assigned by the DHCP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">next-server</span> - IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server1</span> - NTP server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server2</span> - NTP server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server3</span> - NTP server 3. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-service</span> - Options for assigning Network Time Protocol (NTP) servers to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">option1</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">option2</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">option3</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">option4</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">option5</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">option6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">code</span> - DHCP option code. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string, ip, fqdn]</span> </li>
 <li><span class="li-head">value</span> - DHCP option value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">reserved-address</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Options for the DHCP server to configure the client with the reserved MAC address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block, reserved]</span> </li>
 <li><span class="li-head">circuit-id</span> - Option 82 circuit-ID of the client that will get the reserved IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">circuit-id-type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - IP address to be reserved for the MAC address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mac</span> - MAC address of the client that will get the reserved IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-id</span> - Option 82 remote-ID of the client that will get the reserved IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-id-type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span> </li>
 <li><span class="li-head">type</span> - DHCP reserved-address type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mac, option82]</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - DHCP server can be a normal DHCP server or an IPsec DHCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this DHCP configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tftp-server</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">timezone</span> - Select the time zone to be assigned to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]</span> </li>
 <li><span class="li-head">timezone-option</span> - Options for the DHCP server to set the clients time zone. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, default, specify]</span> </li>
 <li><span class="li-head">vci-match</span> - Enable/disable vendor class identifier (VCI) matching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vci-string</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">wifi-ac-service</span> - Options for assigning WiFi Access Controllers to DHCP clients <span class="li-normal">type: str</span>  <span class="li-normal">choices: [specify, local]</span> </li>
 <li><span class="li-head">wifi-ac1</span> - WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-ac2</span> - WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-ac3</span> - WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server1</span> - WINS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server2</span> - WINS server 2. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">interface</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">dhcp-relay-agent-option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">dhcp-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">autoconf</span> - Enable/disable address auto config. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">cli-conn6-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-client-options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span> </li>
 <li><span class="li-head">dhcp6-information-request</span> - Enable/disable DHCPv6 information request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-delegation</span> - Enable/disable DHCPv6 prefix delegation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint</span> - DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-plt</span> - DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-vlt</span> - DHCPv6 prefix hint valid life time (sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-relay-ip</span> - DHCPv6 relay IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-relay-service</span> - Enable/disable DHCPv6 relay. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-relay-type</span> - DHCPv6 relay type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span> </li>
 <li><span class="li-head">icmp6-send-redirect</span> - Enable/disable sending of ICMPv6 redirects. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">interface-identifier</span> - IPv6 interface identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-address</span> - Primary IPv6 address prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric]</span> </li>
 <li><span class="li-head">ip6-default-life</span> - Default life (sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-delegated-prefix-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - Enable/disable the autonomous flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">onlink-flag</span> - Enable/disable the onlink flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">prefix-id</span> - Prefix ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rdnss</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">rdnss-service</span> - Recursive DNS service option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [delegated, default, specify]</span> </li>
 <li><span class="li-head">subnet</span> - Add subnet ID to routing prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">upstream-interface</span> - Name of the interface that provides delegated information. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ip6-dns-server-override</span> - Enable/disable using the DNS server acquired by DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-extra-addr</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">prefix</span> - IPv6 address prefix. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ip6-hop-limit</span> - Hop limit (0 means unspecified). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-link-mtu</span> - IPv6 link MTU. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-manage-flag</span> - Enable/disable the managed flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-max-interval</span> - IPv6 maximum interval (4 to 1800 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-min-interval</span> - IPv6 minimum interval (3 to 1350 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-mode</span> - Addressing mode (static, DHCP, delegated). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span> </li>
 <li><span class="li-head">ip6-other-flag</span> - Enable/disable the other IPv6 flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-prefix-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - Enable/disable the autonomous flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dnssl</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">onlink-flag</span> - Enable/disable the onlink flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">preferred-life-time</span> - Preferred life time (sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">prefix</span> - IPv6 prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rdnss</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">valid-life-time</span> - Valid life time (sec). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">ip6-prefix-mode</span> - Assigning a prefix from DHCP or RA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhcp6, ra]</span> </li>
 <li><span class="li-head">ip6-reachable-time</span> - IPv6 reachable time (milliseconds; 0 means unspecified). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-retrans-time</span> - IPv6 retransmit time (milliseconds; 0 means unspecified). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-send-adv</span> - Enable/disable sending advertisements about the interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-subnet</span> - Subnet to routing prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-upstream-interface</span> - Interface name providing delegated information. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cert</span> - Neighbor discovery certificate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cga-modifier</span> - Neighbor discovery CGA modifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-mode</span> - Neighbor discovery mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [basic, SEND-compatible]</span> </li>
 <li><span class="li-head">nd-security-level</span> - Neighbor discovery security level (0 - 7; 0 = least secure, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-delta</span> - Neighbor discovery timestamp delta value (1 - 3600 sec; default = 300). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-fuzz</span> - Neighbor discovery timestamp fuzz factor (1 - 60 sec; default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ra-send-mtu</span> - Enable/disable sending link MTU in RA packet. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">unique-autoconf-addr</span> - Enable/disable unique auto config address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vrip6_link_local</span> - Link-local IPv6 address of virtual router. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vrrp-virtual-mac6</span> - Enable/disable virtual MAC for VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vrrp6</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - Enable/disable accept mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">adv-interval</span> - Advertisement interval (1 - 255 seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preempt</span> - Enable/disable preempt mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - Priority of the virtual router (1 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-time</span> - Startup time (1 - 255 seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vrdst6</span> - Monitor the route to this destination. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vrgrp</span> - VRRP group ID (1 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrid</span> - Virtual router identifier (1 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip6</span> - IPv6 address of the virtual router. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">secondary-IP</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">secondaryip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric]</span> </li>
 <li><span class="li-head">detectprotocol</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> </li>
 <li><span class="li-head">detectserver</span> - Gateways ping server for this IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gwdetect</span> - Enable/disable detect gateway alive for first. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ha-priority</span> - HA election priority for the PING server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - Secondary IP address of the interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ping-serv-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">vlanid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
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
      fmgr_fsp_vlan_dynamicmapping:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vlan: <your own value>
         state: <value in [present, absent]>
         fsp_vlan_dynamicmapping:
            _dhcp-status: <value in [disable, enable]>
            _scope:
              -
                  name: <value of string>
                  vdom: <value of string>
            dhcp-server:
               auto-configuration: <value in [disable, enable]>
               auto-managed-status: <value in [disable, enable]>
               conflicted-ip-timeout: <value of integer>
               ddns-auth: <value in [disable, tsig]>
               ddns-key: <value of string>
               ddns-keyname: <value of string>
               ddns-server-ip: <value of string>
               ddns-ttl: <value of integer>
               ddns-update: <value in [disable, enable]>
               ddns-update-override: <value in [disable, enable]>
               ddns-zone: <value of string>
               default-gateway: <value of string>
               dhcp-settings-from-fortiipam: <value in [disable, enable]>
               dns-server1: <value of string>
               dns-server2: <value of string>
               dns-server3: <value of string>
               dns-server4: <value of string>
               dns-service: <value in [default, specify, local]>
               domain: <value of string>
               enable: <value in [disable, enable]>
               exclude-range:
                 -
                     end-ip: <value of string>
                     id: <value of integer>
                     start-ip: <value of string>
               filename: <value of string>
               forticlient-on-net-status: <value in [disable, enable]>
               id: <value of integer>
               ip-mode: <value in [range, usrgrp]>
               ip-range:
                 -
                     end-ip: <value of string>
                     id: <value of integer>
                     start-ip: <value of string>
               ipsec-lease-hold: <value of integer>
               lease-time: <value of integer>
               mac-acl-default-action: <value in [assign, block]>
               netmask: <value of string>
               next-server: <value of string>
               ntp-server1: <value of string>
               ntp-server2: <value of string>
               ntp-server3: <value of string>
               ntp-service: <value in [default, specify, local]>
               option1: <value of string>
               option2: <value of string>
               option3: <value of string>
               option4: <value of string>
               option5: <value of string>
               option6: <value of string>
               options:
                 -
                     code: <value of integer>
                     id: <value of integer>
                     ip: <value of string>
                     type: <value in [hex, string, ip, ...]>
                     value: <value of string>
               reserved-address:
                 -
                     action: <value in [assign, block, reserved]>
                     circuit-id: <value of string>
                     circuit-id-type: <value in [hex, string]>
                     description: <value of string>
                     id: <value of integer>
                     ip: <value of string>
                     mac: <value of string>
                     remote-id: <value of string>
                     remote-id-type: <value in [hex, string]>
                     type: <value in [mac, option82]>
               server-type: <value in [regular, ipsec]>
               status: <value in [disable, enable]>
               tftp-server: <value of string>
               timezone: <value in [00, 01, 02, ...]>
               timezone-option: <value in [disable, default, specify]>
               vci-match: <value in [disable, enable]>
               vci-string: <value of string>
               wifi-ac-service: <value in [specify, local]>
               wifi-ac1: <value of string>
               wifi-ac2: <value of string>
               wifi-ac3: <value of string>
               wins-server1: <value of string>
               wins-server2: <value of string>
            interface:
               dhcp-relay-agent-option: <value in [disable, enable]>
               dhcp-relay-ip: <value of string>
               dhcp-relay-service: <value in [disable, enable]>
               dhcp-relay-type: <value in [regular, ipsec]>
               ip: <value of string>
               ipv6:
                  autoconf: <value in [disable, enable]>
                  cli-conn6-status: <value of integer>
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
                  icmp6-send-redirect: <value in [disable, enable]>
                  interface-identifier: <value of string>
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
                    - fabric
                  ip6-default-life: <value of integer>
                  ip6-delegated-prefix-list:
                    -
                        autonomous-flag: <value in [disable, enable]>
                        onlink-flag: <value in [disable, enable]>
                        prefix-id: <value of integer>
                        rdnss: <value of string>
                        rdnss-service: <value in [delegated, default, specify]>
                        subnet: <value of string>
                        upstream-interface: <value of string>
                  ip6-dns-server-override: <value in [disable, enable]>
                  ip6-extra-addr:
                    -
                        prefix: <value of string>
                  ip6-hop-limit: <value of integer>
                  ip6-link-mtu: <value of integer>
                  ip6-manage-flag: <value in [disable, enable]>
                  ip6-max-interval: <value of integer>
                  ip6-min-interval: <value of integer>
                  ip6-mode: <value in [static, dhcp, pppoe, ...]>
                  ip6-other-flag: <value in [disable, enable]>
                  ip6-prefix-list:
                    -
                        autonomous-flag: <value in [disable, enable]>
                        dnssl: <value of string>
                        onlink-flag: <value in [disable, enable]>
                        preferred-life-time: <value of integer>
                        prefix: <value of string>
                        rdnss: <value of string>
                        valid-life-time: <value of integer>
                  ip6-prefix-mode: <value in [dhcp6, ra]>
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
                  ra-send-mtu: <value in [disable, enable]>
                  unique-autoconf-addr: <value in [disable, enable]>
                  vrip6_link_local: <value of string>
                  vrrp-virtual-mac6: <value in [disable, enable]>
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
               vlanid: <value of integer>



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



