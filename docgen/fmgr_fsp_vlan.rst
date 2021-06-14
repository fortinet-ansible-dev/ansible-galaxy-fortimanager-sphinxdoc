:source: fmgr_fsp_vlan.py

:orphan:

.. _fmgr_fsp_vlan:

fmgr_fsp_vlan
+++++++++++++

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
 <td>fsp_vlan</td>
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
 <li><span class="li-head">fsp_vlan</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_dhcp-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [radius, usergroup]</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">portal-message-override-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [open, captive-portal, 8021x]</span> </li>
 <li><span class="li-head">selected-usergroups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">usergroup</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlanid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
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
 <li><span class="li-head">ac-name</span> - PPPoE server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">aggregate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">algorithm</span> - Frame distribution algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [L2, L3, L4]</span> </li>
 <li><span class="li-head">alias</span> - Alias will be displayed with the interface name to make it easier to distinguish. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric]</span> </li>
 <li><span class="li-head">ap-discover</span> - Enable/disable automatic registration of unknown FortiAP devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">arpforward</span> - Enable/disable ARP forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">atm-protocol</span> - ATM protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, ipoa]</span> </li>
 <li><span class="li-head">auth-type</span> - PPP authentication type to use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span> </li>
 <li><span class="li-head">auto-auth-extension-device</span> - Enable/disable automatic authorization of dedicated Fortinet extension device on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-measure-time</span> - Bandwidth measure time <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bfd</span> - Bidirectional Forwarding Detection (BFD) settings. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, enable, disable]</span> </li>
 <li><span class="li-head">bfd-desired-min-tx</span> - BFD desired minimal transmit interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bfd-detect-mult</span> - BFD detection multiplier. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bfd-required-min-rx</span> - BFD required minimal receive interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">broadcast-forticlient-discovery</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">broadcast-forward</span> - Enable/disable broadcast forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">captive-portal</span> - Enable/disable captive portal. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">cli-conn-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
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
 <li><span class="li-head">dedicated-to</span> - Configure interface for single purpose. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, management]</span> </li>
 <li><span class="li-head">defaultgw</span> - Enable to get the gateway IP from the DHCP or PPPoE server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detected-peer-mtu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detectprotocol</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> </li>
 <li><span class="li-head">detectserver</span> - Gateways ping server for this IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-access-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-identification</span> - Enable/disable passively gathering of device identity information about the devices on the network connected to this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">device-identification-active-scan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">device-netscan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">device-user-identification</span> - Enable/disable passive gathering of user identity information about users on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">devindex</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp-client-identifier</span> - DHCP client identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-relay-agent-option</span> - Enable/disable DHCP relay agent option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-interface</span> - Specify outgoing interface to reach server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-relay-interface-select-method</span> - Specify how to select outgoing interface to reach server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span> </li>
 <li><span class="li-head">dhcp-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">dhcp-relay-request-all-server</span> - Enable/disable sending of DHCP requests to all servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-service</span> - Enable/disable allowing this interface to act as a DHCP relay. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-relay-type</span> - DHCP relay type (regular or IPsec). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span> </li>
 <li><span class="li-head">dhcp-renew-time</span> - DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">disc-retry-timeout</span> - Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">disconnect-threshold</span> - Time in milliseconds to wait before sending a notification that this interface is down or disconnected. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">distance</span> - Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dns-query</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, recursive, non-recursive]</span> </li>
 <li><span class="li-head">dns-server-override</span> - Enable/disable use DNS acquired by DHCP or PPPoE. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drop-fragment</span> - Enable/disable drop fragment packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drop-overlapped-fragment</span> - Enable/disable drop overlapped fragment packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">egress-cos</span> - Override outgoing CoS in user VLAN tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span> </li>
 <li><span class="li-head">egress-shaping-profile</span> - Outgoing traffic shaping profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">eip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">endpoint-compliance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">estimated-downstream-bandwidth</span> - Estimated maximum downstream bandwidth (kbps). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">estimated-upstream-bandwidth</span> - Estimated maximum upstream bandwidth (kbps). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">explicit-ftp-proxy</span> - Enable/disable the explicit FTP proxy on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">explicit-web-proxy</span> - Enable/disable the explicit web proxy on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external</span> - Enable/disable identifying the interface as an external interface (which usually means its connected to the Internet). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fail-action-on-extender</span> - Action on extender when interface fail . <span class="li-normal">type: str</span>  <span class="li-normal">choices: [soft-restart, hard-restart, reboot]</span> </li>
 <li><span class="li-head">fail-alert-interfaces</span> - Names of the FortiGate interfaces to which the link failure alert is sent. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fail-alert-method</span> - Select link-failed-signal or link-down method to alert about a failed link. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [link-failed-signal, link-down]</span> </li>
 <li><span class="li-head">fail-detect</span> - Enable/disable fail detection features for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fail-detect-option</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [detectserver, link-down]</span> </li>
 <li><span class="li-head">fdp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortiheartbeat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortilink</span> - Enable FortiLink to dedicate this interface to manage other Fortinet devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortilink-backup-link</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortilink-neighbor-detect</span> - Protocol for FortiGate neighbor discovery. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [lldp, fortilink]</span> </li>
 <li><span class="li-head">fortilink-split-interface</span> - Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortilink-stacking</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">forward-domain</span> - Transparent mode forward domain. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">forward-error-correction</span> - Enable/disable forward error correction (FEC Clause 91). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, rs-fec, base-r-fec, fec-cl91, fec-cl74]</span> </li>
 <li><span class="li-head">fp-anomaly</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [drop_tcp_fin_noack, pass_winnuke, pass_tcpland, pass_udpland, pass_icmpland, pass_ipland, pass_iprr, pass_ipssrr, pass_iplsrr, pass_ipstream, pass_ipsecurity, pass_iptimestamp, pass_ipunknown_option, pass_ipunknown_prot, pass_icmp_frag, pass_tcp_no_flag, pass_tcp_fin_noack, drop_winnuke, drop_tcpland, drop_udpland, drop_icmpland, drop_ipland, drop_iprr, drop_ipssrr, drop_iplsrr, drop_ipstream, drop_ipsecurity, drop_iptimestamp, drop_ipunknown_option, drop_ipunknown_prot, drop_icmp_frag, drop_tcp_no_flag]</span> </li>
 <li><span class="li-head">fp-disable</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [all, ipsec, none]</span> </li>
 <li><span class="li-head">gateway-address</span> - Gateway address <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gi-gk</span> - Enable/disable Gi Gatekeeper. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gwaddr</span> - Gateway address <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gwdetect</span> - Enable/disable detect gateway alive for first. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ha-priority</span> - HA election priority for the PING server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">icmp-accept-redirect</span> - Enable/disable ICMP accept redirect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icmp-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icmp-send-redirect</span> - Enable/disable sending of ICMP redirects. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ident-accept</span> - Enable/disable authentication for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">idle-timeout</span> - PPPoE auto disconnect after idle timeout seconds, 0 means no timeout. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">if-mdix</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, normal, crossover]</span> </li>
 <li><span class="li-head">if-media</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, copper, fiber]</span> </li>
 <li><span class="li-head">in-force-vlan-cos</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">inbandwidth</span> - Bandwidth limit for incoming traffic (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ingress-cos</span> - Override incoming CoS in user VLAN tag on VLAN interface or assign a priority VLAN tag on physical interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span> </li>
 <li><span class="li-head">ingress-shaping-profile</span> - Incoming traffic shaping profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">internal</span> - Implicitly created. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - Interface IPv4 address and subnet mask, syntax: X. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-managed-by-fortiipam</span> - Enable/disable automatic IP address assignment of this interface by FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipmac</span> - Enable/disable IP/MAC binding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sniffer-mode</span> - Enable/disable the use of this interface as a one-armed sniffer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipunnumbered</span> - Unnumbered IP used for PPPoE interfaces for which no unique local address is provided. <span class="li-normal">type: str</span> </li>
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
 <li><span class="li-head">l2forward</span> - Enable/disable l2 forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">l2tp-client</span> - Enable/disable this interface as a Layer 2 Tunnelling Protocol (L2TP) client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-ha-slave</span> - LACP HA slave. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-mode</span> - LACP mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, passive, active]</span> </li>
 <li><span class="li-head">lacp-speed</span> - How often the interface sends LACP messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slow, fast]</span> </li>
 <li><span class="li-head">lcp-echo-interval</span> - Time in seconds between PPPoE Link Control Protocol (LCP) echo requests. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lcp-max-echo-fails</span> - Maximum missed LCP echo messages before disconnect. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-up-delay</span> - Number of milliseconds to wait before considering a link is up. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">listen-forticlient-connection</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lldp-network-policy</span> - LLDP-MED network policy profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">lldp-reception</span> - Enable/disable Link Layer Discovery Protocol (LLDP) reception. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vdom]</span> </li>
 <li><span class="li-head">lldp-transmission</span> - Enable/disable Link Layer Discovery Protocol (LLDP) transmission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable, vdom]</span> </li>
 <li><span class="li-head">log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">macaddr</span> - Change the interfaces MAC address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">managed-subnetwork-size</span> - Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate units DHCP server settings. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]</span> </li>
 <li><span class="li-head">management-ip</span> - High Availability in-band management IP address of this interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-egress-burst-rate</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-egress-rate</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">measured-downstream-bandwidth</span> - Measured downstream bandwidth (kbps). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">measured-upstream-bandwidth</span> - Measured upstream bandwidth (kbps). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mediatype</span> - Select SFP media interface type <span class="li-normal">type: str</span>  <span class="li-normal">choices: [serdes-sfp, sgmii-sfp, cfp2-sr10, cfp2-lr4, serdes-copper-sfp, sr, cr, lr, qsfp28-sr4, qsfp28-lr4, qsfp28-cr4, sr4, cr4, lr4]</span> </li>
 <li><span class="li-head">member</span> - Physical interfaces that belong to the aggregate or redundant interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">min-links</span> - Minimum number of aggregated ports that must be up. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">min-links-down</span> - Action to take when less than the configured minimum number of links are active. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [operational, administrative]</span> </li>
 <li><span class="li-head">mode</span> - Addressing mode (static, DHCP, PPPoE). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, pppoa, ipoa, eoa]</span> </li>
 <li><span class="li-head">monitor-bandwidth</span> - Enable monitoring bandwidth on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mtu</span> - MTU value for this interface. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mtu-override</span> - Enable to set a custom MTU for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mux-type</span> - Multiplexer type <span class="li-normal">type: str</span>  <span class="li-normal">choices: [llc-encaps, vc-encaps]</span> </li>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ndiscforward</span> - Enable/disable NDISC forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">netbios-forward</span> - Enable/disable NETBIOS forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">netflow-sampler</span> - Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tx, rx, both]</span> </li>
 <li><span class="li-head">np-qos-profile</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">npu-fastpath</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nst</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">out-force-vlan-cos</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbandwidth</span> - Bandwidth limit for outgoing traffic (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">padt-retry-timeout</span> - PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">peer-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">phy-mode</span> - DSL physical mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, adsl, vdsl]</span> </li>
 <li><span class="li-head">ping-serv-status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poe</span> - Enable/disable PoE status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">polling-interval</span> - sFlow polling interval (1 - 255 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pppoe-unnumbered-negotiate</span> - Enable/disable PPPoE unnumbered negotiation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pptp-auth-type</span> - PPTP authentication type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span> </li>
 <li><span class="li-head">pptp-client</span> - Enable/disable PPTP client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pptp-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">pptp-server-ip</span> - PPTP server IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pptp-timeout</span> - Idle timer in minutes (0 for disabled). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pptp-user</span> - PPTP user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">preserve-session-route</span> - Enable/disable preservation of session route when dirty. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - Priority of learned routes. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority-override</span> - Enable/disable fail back to higher priority port once recovered. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">proxy-captive-portal</span> - Enable/disable proxy captive portal on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">redundant-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-ip</span> - Remote IP address of tunnel. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - Replacement message override group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">retransmission</span> - Enable/disable DSL retransmission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ring-rx</span> - RX ring size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ring-tx</span> - TX ring size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">role</span> - Interface role. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [lan, wan, dmz, undefined]</span> </li>
 <li><span class="li-head">sample-direction</span> - Data that NetFlow collects (rx, tx, or both). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rx, tx, both]</span> </li>
 <li><span class="li-head">sample-rate</span> - sFlow sample rate (10 - 99999). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">secondary-IP</span> - Enable/disable adding a secondary IP to this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
 <li><span class="li-head">security-8021x-dynamic-vlan-id</span> - VLAN ID for virtual switch. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-8021x-master</span> - 802. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-8021x-mode</span> - 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, dynamic-vlan, fallback, slave]</span> </li>
 <li><span class="li-head">security-exempt-list</span> - Name of security-exempt-list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-external-logout</span> - URL of external authentication logout server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-external-web</span> - URL of external authentication web server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-groups</span> - User groups that can authenticate with the captive portal. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-mac-auth-bypass</span> - Enable/disable MAC authentication bypass. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, mac-auth-only]</span> </li>
 <li><span class="li-head">security-mode</span> - Turn on captive portal authentication for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, captive-portal, 802.1X]</span> </li>
 <li><span class="li-head">security-redirect-url</span> - URL redirection after disclaimer/authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-name</span> - PPPoE service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sflow-sampler</span> - Enable/disable sFlow on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">speed</span> - Interface speed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, 10full, 10half, 100full, 100half, 1000full, 1000half, 10000full, 1000auto, 10000auto, 40000full, 100Gfull, 25000full, 40000auto, 25000auto, 100Gauto]</span> </li>
 <li><span class="li-head">spillover-threshold</span> - Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">src-check</span> - Enable/disable source IP check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Bring the interface up or shut the interface down. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [down, up]</span> </li>
 <li><span class="li-head">stp</span> - Enable/disable STP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">stp-ha-secondary</span> - Control STP behaviour on HA secondary. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, priority-adjust]</span> </li>
 <li><span class="li-head">stp-ha-slave</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, priority-adjust]</span> </li>
 <li><span class="li-head">stpforward</span> - Enable/disable STP forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">stpforward-mode</span> - Configure STP forwarding mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]</span> </li>
 <li><span class="li-head">strip-priority-vlan-tag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">subst</span> - Enable to always send packets from this interface to a destination MAC address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">substitute-dst-mac</span> - Destination MAC address that all packets are sent to from this interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">swc-first-create</span> - Initial create for switch-controller VLANs. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">swc-vlan</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-access-vlan</span> - Block FortiSwitch port-to-port traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-arp-inspection</span> - Enable/disable FortiSwitch ARP inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [radius, usergroup]</span> </li>
 <li><span class="li-head">switch-controller-dhcp-snooping</span> - Switch controller DHCP snooping. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-dhcp-snooping-option82</span> - Switch controller DHCP snooping option82. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-dhcp-snooping-verify-mac</span> - Switch controller DHCP snooping verify MAC. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-dynamic</span> - Integrated FortiLink settings for managed FortiSwitch. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-feature</span> - Interfaces purpose when assigning traffic (read only). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, default-vlan, quarantine, sniffer, voice, camera, rspan, video, nac]</span> </li>
 <li><span class="li-head">switch-controller-igmp-snooping</span> - Switch controller IGMP snooping. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-igmp-snooping-fast-leave</span> - Switch controller IGMP snooping fast-leave. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-igmp-snooping-proxy</span> - Switch controller IGMP snooping proxy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-iot-scanning</span> - Enable/disable managed FortiSwitch IoT scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-learning-limit</span> - Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch-controller-mgmt-vlan</span> - VLAN to use for FortiLink management purposes. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch-controller-nac</span> - Integrated FortiLink settings for managed FortiSwitch. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">switch-controller-rspan-mode</span> - Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switch-controller-source-ip</span> - Source IP address used in FortiLink over L3 connections. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [outbound, fixed]</span> </li>
 <li><span class="li-head">switch-controller-traffic-policy</span> - Switch controller traffic policy for the VLAN. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tc-mode</span> - DSL transfer mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ptm, atm]</span> </li>
 <li><span class="li-head">tcp-mss</span> - TCP maximum segment size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trunk</span> - Enable/disable VLAN trunk. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">trust-ip-1</span> - Trusted host for dedicated management traffic (0. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip-2</span> - Trusted host for dedicated management traffic (0. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip-3</span> - Trusted host for dedicated management traffic (0. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip6-1</span> - Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip6-2</span> - Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trust-ip6-3</span> - Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Interface type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [physical, vlan, aggregate, redundant, tunnel, wireless, vdom-link, loopback, switch, hard-switch, hdlc, vap-switch, wl-mesh, fortilink, switch-vlan, fctrl-trunk, tdm, fext-wan, vxlan, emac-vlan, geneve, ssl]</span> </li>
 <li><span class="li-head">username</span> - Username of the PPPoE account, provided by your ISP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vci</span> - Virtual Channel ID <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vectoring</span> - Enable/disable DSL vectoring. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vindex</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vlan-protocol</span> - Ethernet protocol of VLAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [8021q, 8021ad]</span> </li>
 <li><span class="li-head">vlanforward</span> - Enable/disable traffic forwarding between VLANs on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vlanid</span> - VLAN ID (1 - 4094). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vpi</span> - Virtual Path ID <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrf</span> - Virtual Routing Forwarding ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrrp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - Enable/disable accept mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">adv-interval</span> - Advertisement interval (1 - 255 seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ignore-default-route</span> - Enable/disable ignoring of default route when checking destination. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">preempt</span> - Enable/disable preempt mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - Priority of the virtual router (1 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-time</span> - Startup time (1 - 255 seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this VRRP configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">version</span> - VRRP version. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [2, 3]</span> </li>
 <li><span class="li-head">vrdst</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">vrdst-priority</span> - Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrgrp</span> - VRRP group ID (1 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrid</span> - Virtual router identifier (1 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip</span> - IP address of the virtual router. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">vrrp-virtual-mac</span> - Enable/disable use of virtual MAC for VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wccp</span> - Enable/disable WCCP on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">weight</span> - Default weight for static routes (if route has no weight configured). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-5g-threshold</span> - Minimal signal strength to be considered as a good 5G AP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-acl</span> - Access control for MAC addresses in the MAC list. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">wifi-ap-band</span> - How to select the AP to connect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, 5g-preferred, 5g-only]</span> </li>
 <li><span class="li-head">wifi-auth</span> - WiFi authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [PSK, RADIUS, radius, usergroup]</span> </li>
 <li><span class="li-head">wifi-auto-connect</span> - Enable/disable WiFi network auto connect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-auto-save</span> - Enable/disable WiFi network automatic save. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-broadcast-ssid</span> - Enable/disable SSID broadcast in the beacon. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-encrypt</span> - Data encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TKIP, AES]</span> </li>
 <li><span class="li-head">wifi-fragment-threshold</span> - WiFi fragment threshold (800 - 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-key</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">wifi-keyindex</span> - WEP key index (1 - 4). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-mac-filter</span> - Enable/disable MAC filter status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wifi-passphrase</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">wifi-radius-server</span> - WiFi RADIUS server for WPA. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-rts-threshold</span> - WiFi RTS threshold (256 - 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wifi-security</span> - Wireless access security of SSID. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise]</span> </li>
 <li><span class="li-head">wifi-ssid</span> - IEEE 802. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-usergroup</span> - WiFi user group for WPA. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-ip</span> - WINS server IP. <span class="li-normal">type: str</span> </li>
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
      fmgr_fsp_vlan:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         fsp_vlan:
            _dhcp-status: <value in [disable, enable]>
            auth: <value in [radius, usergroup]>
            color: <value of integer>
            comments: <value of string>
            dynamic_mapping:
              -
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
            name: <value of string>
            portal-message-override-group: <value of string>
            radius-server: <value of string>
            security: <value in [open, captive-portal, 8021x]>
            selected-usergroups: <value of string>
            usergroup: <value of string>
            vdom: <value of string>
            vlanid: <value of integer>
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
                 - fabric
               ap-discover: <value in [disable, enable]>
               arpforward: <value in [disable, enable]>
               atm-protocol: <value in [none, ipoa]>
               auth-type: <value in [auto, pap, chap, ...]>
               auto-auth-extension-device: <value in [disable, enable]>
               bandwidth-measure-time: <value of integer>
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
               dhcp-relay-interface: <value of string>
               dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
               dhcp-relay-ip: <value of string>
               dhcp-relay-request-all-server: <value in [disable, enable]>
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
               eip: <value of string>
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
               fortilink-neighbor-detect: <value in [lldp, fortilink]>
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
               ingress-shaping-profile: <value of string>
               ingress-spillover-threshold: <value of integer>
               internal: <value of integer>
               ip: <value of string>
               ip-managed-by-fortiipam: <value in [disable, enable]>
               ipmac: <value in [disable, enable]>
               ips-sniffer-mode: <value in [disable, enable]>
               ipunnumbered: <value of string>
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
               managed-subnetwork-size: <value in [256, 512, 1024, ...]>
               management-ip: <value of string>
               max-egress-burst-rate: <value of integer>
               max-egress-rate: <value of integer>
               measured-downstream-bandwidth: <value of integer>
               measured-upstream-bandwidth: <value of integer>
               mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
               member: <value of string>
               min-links: <value of integer>
               min-links-down: <value in [operational, administrative]>
               mode: <value in [static, dhcp, pppoe, ...]>
               monitor-bandwidth: <value in [disable, enable]>
               mtu: <value of integer>
               mtu-override: <value in [disable, enable]>
               mux-type: <value in [llc-encaps, vc-encaps]>
               name: <value of string>
               ndiscforward: <value in [disable, enable]>
               netbios-forward: <value in [disable, enable]>
               netflow-sampler: <value in [disable, tx, rx, ...]>
               np-qos-profile: <value of integer>
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
               ring-rx: <value of integer>
               ring-tx: <value of integer>
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
               stp-ha-secondary: <value in [disable, enable, priority-adjust]>
               stp-ha-slave: <value in [disable, enable, priority-adjust]>
               stpforward: <value in [disable, enable]>
               stpforward-mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
               strip-priority-vlan-tag: <value in [disable, enable]>
               subst: <value in [disable, enable]>
               substitute-dst-mac: <value of string>
               swc-first-create: <value of integer>
               swc-vlan: <value of integer>
               switch: <value of string>
               switch-controller-access-vlan: <value in [disable, enable]>
               switch-controller-arp-inspection: <value in [disable, enable]>
               switch-controller-auth: <value in [radius, usergroup]>
               switch-controller-dhcp-snooping: <value in [disable, enable]>
               switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
               switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
               switch-controller-dynamic: <value of string>
               switch-controller-feature: <value in [none, default-vlan, quarantine, ...]>
               switch-controller-igmp-snooping: <value in [disable, enable]>
               switch-controller-igmp-snooping-fast-leave: <value in [disable, enable]>
               switch-controller-igmp-snooping-proxy: <value in [disable, enable]>
               switch-controller-iot-scanning: <value in [disable, enable]>
               switch-controller-learning-limit: <value of integer>
               switch-controller-mgmt-vlan: <value of integer>
               switch-controller-nac: <value of string>
               switch-controller-radius-server: <value of string>
               switch-controller-rspan-mode: <value in [disable, enable]>
               switch-controller-source-ip: <value in [outbound, fixed]>
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
               vlan-protocol: <value in [8021q, 8021ad]>
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



