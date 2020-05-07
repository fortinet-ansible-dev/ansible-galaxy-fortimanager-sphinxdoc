:source: fmgr_pkg_firewall_policy.py

:orphan:

.. _fmgr_pkg_firewall_policy:

fmgr_pkg_firewall_policy -- Configure IPv4 policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy`
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
 <li><span class="li-head">loose_validation</span> - Do parameter validation in a loose way <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal">default: false</span>  </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">pkg</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure IPv4 policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Policy action (allow/deny/ipsec). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept, ipsec, ssl-vpn]</span> </li>
 <li><span class="li-head">app-category</span> - Application category ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">application-list</span> - Name of an existing Application list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auth-cert</span> - HTTPS server certificate for policy authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auth-path</span> - Enable/disable authentication-based routing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-redirect-addr</span> - HTTP-to-HTTPS redirect address for firewall authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auto-asic-offload</span> - Enable/disable offloading security profile processing to CP processors. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-profile</span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">block-notification</span> - Enable/disable block notification. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">captive-portal-exempt</span> - Enable to exempt some users from the captive portal. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">capture-packet</span> - Enable/disable capture packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">custom-log-fields</span> - Custom fields to append to log messages for this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">delay-tcp-npu-session</span> - Enable TCP NPU session delay to guarantee packet order of 3-way handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">devices</span> - Names of devices or device groups that can be matched by the policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffserv-forward</span> - Enable to change packets DiffServ values to the specified diffservcode-forward value. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffserv-reverse</span> - Enable to change packets reverse (reply) DiffServ values to the specified diffservcode-rev value. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffservcode-forward</span> - Change packets DiffServ to this value. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffservcode-rev</span> - Change packets reverse (reply) DiffServ to this value. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">disclaimer</span> - Enable/disable user authentication disclaimer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dlp-sensor</span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dnsfilter-profile</span> - Name of an existing DNS filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dscp-match</span> - Enable DSCP check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-negate</span> - Enable negated DSCP match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-value</span> - DSCP value. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dsri</span> - Enable DSRI to ignore HTTP server responses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr-negate</span> - When enabled dstaddr specifies what the destination address must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstintf</span> - Outgoing (egress) interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">firewall-session-dirty</span> - How to handle sessions if the configuration of this firewall policy changes. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [check-all, check-new]</span> </li>
 <li><span class="li-head">fixedport</span> - Enable to prevent source NAT from changing a sessions source port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fsso</span> - Enable/disable Fortinet Single Sign-On. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fsso-agent-for-ntlm</span> - FSSO agent to use for NTLM authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">global-label</span> - Label for the policy that appears when the GUI is in Global View mode. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - Names of user groups that can authenticate with this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gtp-profile</span> - GTP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">icap-profile</span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">identity-based-route</span> - Name of identity-based routing rule. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">inbound</span> - Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet Service Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-negate</span> - When enabled internet-service specifies what the service must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ippool</span> - Enable to use IP Pools for source NAT. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">label</span> - Label for the policy that appears when the GUI is in Section View mode. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">learning-mode</span> - Enable to allow everything, but log all of the meaningful data for security information gathering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">logtraffic</span> - Enable or disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - Record logs when a session starts and ends. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">match-vip</span> - Enable to match packets that have had their destination addresses changed by a VIP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - Name of an existing MMS profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Policy name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat</span> - Enable/disable source NAT. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">natinbound</span> - Policy-based IPsec VPN: apply destination NAT to inbound traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">natip</span> - Policy-based IPsec VPN: source NAT IP address for outgoing traffic. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">natoutbound</span> - Policy-based IPsec VPN: apply source NAT to outbound traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ntlm</span> - Enable/disable NTLM authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ntlm-enabled-browsers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ntlm-guest</span> - Enable/disable NTLM guest user access. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbound</span> - Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - Per-IP traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">permit-any-host</span> - Accept UDP packets from any host. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">permit-stun-host</span> - Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poolname</span> - IP Pool names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - Name of profile group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">radius-mac-auth-bypass</span> - Enable MAC authentication bypass. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">redirect-url</span> - URL users are directed to after seeing and accepting the disclaimer or authenticating. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - Override the default replacement message group for this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rsso</span> - Enable/disable RADIUS single sign-on (RSSO). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rtp-addr</span> - Address names if this is an RTP NAT policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rtp-nat</span> - Enable Real Time Protocol (RTP) NAT. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - Block or monitor connections to Botnet servers or disable Botnet scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">schedule</span> - Schedule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule-timeout</span> - Enable to force current sessions to end when the schedule object times out. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">send-deny-packet</span> - Enable to send a reply when a session is denied or blocked by a firewall policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service</span> - Service and service group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - When enabled service specifies what the service must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">session-ttl</span> - Session TTL in seconds for sessions accepted by this policy. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr-negate</span> - When enabled srcaddr specifies what the source address must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcintf</span> - Incoming (ingress) interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-mirror</span> - Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-mirror-intf</span> - SSL mirror interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable or disable this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tags</span> - Names of object-tags applied to this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tcp-mss-receiver</span> - Receiver TCP maximum segment size (MSS). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-mss-sender</span> - Sender TCP maximum segment size (MSS). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-session-without-syn</span> - Enable/disable creation of TCP session without SYN flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [all, data-only, disable]</span> </li>
 <li><span class="li-head">timeout-send-rst</span> - Enable/disable sending RST packets when TCP sessions expire. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">traffic-shaper</span> - Traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - Reverse traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-category</span> - URL category ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - Names of individual users that can authenticate with this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - Enable to add one or more security profiles (AV, IPS, etc. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan-cos-fwd</span> - VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vlan-cos-rev</span> - VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">voip-profile</span> - Name of an existing VoIP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpn_dst_node</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">host</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">vpn_src_node</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">host</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">vpntunnel</span> - Policy-based IPsec VPN: name of the IPsec VPN Phase 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">waf-profile</span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wanopt</span> - Enable/disable WAN optimization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wanopt-detection</span> - WAN optimization auto-detection mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, passive, off]</span> </li>
 <li><span class="li-head">wanopt-passive-opt</span> - WAN optimization passive mode options. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, transparent, non-transparent]</span> </li>
 <li><span class="li-head">wanopt-peer</span> - WAN optimization peer. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wanopt-profile</span> - WAN optimization profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wccp</span> - Enable/disable forwarding traffic matching this policy to a configured WCCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webcache</span> - Enable/disable web cache. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webcache-https</span> - Enable/disable web cache for HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, ssl-server, any, enable]</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wsso</span> - Enable/disable WiFi Single Sign On (WSSO). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [action, app-category, application, application-list, auth-cert, auth-path, auth-redirect-addr, auto-asic-offload, av-profile, block-notification, captive-portal-exempt, capture-packet, custom-log-fields, delay-tcp-npu-session, devices, diffserv-forward, diffserv-reverse, diffservcode-forward, diffservcode-rev, disclaimer, dlp-sensor, dnsfilter-profile, dscp-match, dscp-negate, dscp-value, dsri, dstaddr, dstaddr-negate, dstintf, firewall-session-dirty, fixedport, fsso, fsso-agent-for-ntlm, global-label, groups, gtp-profile, icap-profile, identity-based-route, inbound, internet-service, internet-service-custom, internet-service-id, internet-service-negate, ippool, ips-sensor, label, learning-mode, logtraffic, logtraffic-start, match-vip, mms-profile, name, nat, natinbound, natip, natoutbound, ntlm, ntlm-enabled-browsers, ntlm-guest, outbound, per-ip-shaper, permit-any-host, permit-stun-host, policyid, poolname, profile-group, profile-protocol-options, profile-type, radius-mac-auth-bypass, redirect-url, replacemsg-override-group, rsso, rtp-addr, rtp-nat, scan-botnet-connections, schedule, schedule-timeout, send-deny-packet, service, service-negate, session-ttl, spamfilter-profile, srcaddr, srcaddr-negate, srcintf, ssl-mirror, ssl-mirror-intf, ssl-ssh-profile, status, tags, tcp-mss-receiver, tcp-mss-sender, tcp-session-without-syn, timeout-send-rst, traffic-shaper, traffic-shaper-reverse, url-category, users, utm-status, uuid, vlan-cos-fwd, vlan-cos-rev, voip-profile, vpntunnel, waf-profile, wanopt, wanopt-detection, wanopt-passive-opt, wanopt-peer, wanopt-profile, wccp, webcache, webcache-https, webfilter-profile, wsso]</span> </li>
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

   - To run in workspace mode, the paremeter workspace_locking_adom must be included in the task

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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/POLICY
      fmgr_pkg_firewall_policy:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               data:
                 -
                     action: <value in [deny, accept, ipsec, ...]>
                     app-category: <value of string>
                     application:
                       - <value of integer>
                     application-list: <value of string>
                     auth-cert: <value of string>
                     auth-path: <value in [disable, enable]>
                     auth-redirect-addr: <value of string>
                     auto-asic-offload: <value in [disable, enable]>
                     av-profile: <value of string>
                     block-notification: <value in [disable, enable]>
                     captive-portal-exempt: <value in [disable, enable]>
                     capture-packet: <value in [disable, enable]>
                     comments: <value of string>
                     custom-log-fields: <value of string>
                     delay-tcp-npu-session: <value in [disable, enable]>
                     devices: <value of string>
                     diffserv-forward: <value in [disable, enable]>
                     diffserv-reverse: <value in [disable, enable]>
                     diffservcode-forward: <value of string>
                     diffservcode-rev: <value of string>
                     disclaimer: <value in [disable, enable]>
                     dlp-sensor: <value of string>
                     dnsfilter-profile: <value of string>
                     dscp-match: <value in [disable, enable]>
                     dscp-negate: <value in [disable, enable]>
                     dscp-value: <value of string>
                     dsri: <value in [disable, enable]>
                     dstaddr: <value of string>
                     dstaddr-negate: <value in [disable, enable]>
                     dstintf: <value of string>
                     firewall-session-dirty: <value in [check-all, check-new]>
                     fixedport: <value in [disable, enable]>
                     fsso: <value in [disable, enable]>
                     fsso-agent-for-ntlm: <value of string>
                     global-label: <value of string>
                     groups: <value of string>
                     gtp-profile: <value of string>
                     icap-profile: <value of string>
                     identity-based-route: <value of string>
                     inbound: <value in [disable, enable]>
                     internet-service: <value in [disable, enable]>
                     internet-service-custom: <value of string>
                     internet-service-id: <value of string>
                     internet-service-negate: <value in [disable, enable]>
                     ippool: <value in [disable, enable]>
                     ips-sensor: <value of string>
                     label: <value of string>
                     learning-mode: <value in [disable, enable]>
                     logtraffic: <value in [disable, enable, all, ...]>
                     logtraffic-start: <value in [disable, enable]>
                     match-vip: <value in [disable, enable]>
                     mms-profile: <value of string>
                     name: <value of string>
                     nat: <value in [disable, enable]>
                     natinbound: <value in [disable, enable]>
                     natip: <value of string>
                     natoutbound: <value in [disable, enable]>
                     ntlm: <value in [disable, enable]>
                     ntlm-enabled-browsers:
                       - <value of string>
                     ntlm-guest: <value in [disable, enable]>
                     outbound: <value in [disable, enable]>
                     per-ip-shaper: <value of string>
                     permit-any-host: <value in [disable, enable]>
                     permit-stun-host: <value in [disable, enable]>
                     policyid: <value of integer>
                     poolname: <value of string>
                     profile-group: <value of string>
                     profile-protocol-options: <value of string>
                     profile-type: <value in [single, group]>
                     radius-mac-auth-bypass: <value in [disable, enable]>
                     redirect-url: <value of string>
                     replacemsg-override-group: <value of string>
                     rsso: <value in [disable, enable]>
                     rtp-addr: <value of string>
                     rtp-nat: <value in [disable, enable]>
                     scan-botnet-connections: <value in [disable, block, monitor]>
                     schedule: <value of string>
                     schedule-timeout: <value in [disable, enable]>
                     send-deny-packet: <value in [disable, enable]>
                     service: <value of string>
                     service-negate: <value in [disable, enable]>
                     session-ttl: <value of integer>
                     spamfilter-profile: <value of string>
                     srcaddr: <value of string>
                     srcaddr-negate: <value in [disable, enable]>
                     srcintf: <value of string>
                     ssl-mirror: <value in [disable, enable]>
                     ssl-mirror-intf: <value of string>
                     ssl-ssh-profile: <value of string>
                     status: <value in [disable, enable]>
                     tags: <value of string>
                     tcp-mss-receiver: <value of integer>
                     tcp-mss-sender: <value of integer>
                     tcp-session-without-syn: <value in [all, data-only, disable]>
                     timeout-send-rst: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     url-category: <value of string>
                     users: <value of string>
                     utm-status: <value in [disable, enable]>
                     uuid: <value of string>
                     vlan-cos-fwd: <value of integer>
                     vlan-cos-rev: <value of integer>
                     voip-profile: <value of string>
                     vpn_dst_node:
                       -
                           host: <value of string>
                           seq: <value of integer>
                           subnet: <value of string>
                     vpn_src_node:
                       -
                           host: <value of string>
                           seq: <value of integer>
                           subnet: <value of string>
                     vpntunnel: <value of string>
                     waf-profile: <value of string>
                     wanopt: <value in [disable, enable]>
                     wanopt-detection: <value in [active, passive, off]>
                     wanopt-passive-opt: <value in [default, transparent, non-transparent]>
                     wanopt-peer: <value of string>
                     wanopt-profile: <value of string>
                     wccp: <value in [disable, enable]>
                     webcache: <value in [disable, enable]>
                     webcache-https: <value in [disable, ssl-server, any, ...]>
                     webfilter-profile: <value of string>
                     wsso: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/POLICY
      fmgr_pkg_firewall_policy:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, app-category, application, ...]>
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
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Policy action (allow/deny/ipsec). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> app-category </span> - Application category ID list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> application-list </span> - Name of an existing Application list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-cert </span> - HTTPS server certificate for policy authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-path </span> - Enable/disable authentication-based routing. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-redirect-addr </span> - HTTP-to-HTTPS redirect address for firewall authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auto-asic-offload </span> - Enable/disable offloading security profile processing to CP processors. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-notification </span> - Enable/disable block notification. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> captive-portal-exempt </span> - Enable to exempt some users from the captive portal. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> capture-packet </span> - Enable/disable capture packets. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comments </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> custom-log-fields </span> - Custom fields to append to log messages for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delay-tcp-npu-session </span> - Enable TCP NPU session delay to guarantee packet order of 3-way handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> devices </span> - Names of devices or device groups that can be matched by the policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-forward </span> - Enable to change packets DiffServ values to the specified diffservcode-forward value. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-reverse </span> - Enable to change packets reverse (reply) DiffServ values to the specified diffservcode-rev value. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-forward </span> - Change packets DiffServ to this value. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-rev </span> - Change packets reverse (reply) DiffServ to this value. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> disclaimer </span> - Enable/disable user authentication disclaimer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dnsfilter-profile </span> - Name of an existing DNS filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-match </span> - Enable DSCP check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-negate </span> - Enable negated DSCP match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-value </span> - DSCP value. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dsri </span> - Enable DSRI to ignore HTTP server responses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - Destination address and address group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr-negate </span> - When enabled dstaddr specifies what the destination address must NOT be. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - Outgoing (egress) interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> firewall-session-dirty </span> - How to handle sessions if the configuration of this firewall policy changes. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fixedport </span> - Enable to prevent source NAT from changing a sessions source port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fsso </span> - Enable/disable Fortinet Single Sign-On. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fsso-agent-for-ntlm </span> - FSSO agent to use for NTLM authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> global-label </span> - Label for the policy that appears when the GUI is in Global View mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - Names of user groups that can authenticate with this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gtp-profile </span> - GTP profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icap-profile </span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> identity-based-route </span> - Name of identity-based routing rule. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inbound </span> - Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service </span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom </span> - Custom Internet Service Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-id </span> - Internet Service ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-negate </span> - When enabled internet-service specifies what the service must NOT be. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ippool </span> - Enable to use IP Pools for source NAT. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> label </span> - Label for the policy that appears when the GUI is in Section View mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> learning-mode </span> - Enable to allow everything, but log all of the meaningful data for security information gathering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - Enable or disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic-start </span> - Record logs when a session starts and ends. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> match-vip </span> - Enable to match packets that have had their destination addresses changed by a VIP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-profile </span> - Name of an existing MMS profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Policy name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nat </span> - Enable/disable source NAT. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natinbound </span> - Policy-based IPsec VPN: apply destination NAT to inbound traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natip </span> - Policy-based IPsec VPN: source NAT IP address for outgoing traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natoutbound </span> - Policy-based IPsec VPN: apply source NAT to outbound traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntlm </span> - Enable/disable NTLM authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntlm-enabled-browsers </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ntlm-guest </span> - Enable/disable NTLM guest user access. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outbound </span> - Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-ip-shaper </span> - Per-IP traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> permit-any-host </span> - Accept UDP packets from any host. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> permit-stun-host </span> - Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> poolname </span> - IP Pool names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-group </span> - Name of profile group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-protocol-options </span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-type </span> - Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-mac-auth-bypass </span> - Enable MAC authentication bypass. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> redirect-url </span> - URL users are directed to after seeing and accepting the disclaimer or authenticating. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-override-group </span> - Override the default replacement message group for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso </span> - Enable/disable RADIUS single sign-on (RSSO). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rtp-addr </span> - Address names if this is an RTP NAT policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rtp-nat </span> - Enable Real Time Protocol (RTP) NAT. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> scan-botnet-connections </span> - Block or monitor connections to Botnet servers or disable Botnet scanning. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule </span> - Schedule name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule-timeout </span> - Enable to force current sessions to end when the schedule object times out. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> send-deny-packet </span> - Enable to send a reply when a session is denied or blocked by a firewall policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - Service and service group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service-negate </span> - When enabled service specifies what the service must NOT be. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> session-ttl </span> - Session TTL in seconds for sessions accepted by this policy. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> spamfilter-profile </span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - Source address and address group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr-negate </span> - When enabled srcaddr specifies what the source address must NOT be. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcintf </span> - Incoming (ingress) interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mirror </span> - Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mirror-intf </span> - SSL mirror interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-ssh-profile </span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable or disable this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - Names of object-tags applied to this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tcp-mss-receiver </span> - Receiver TCP maximum segment size (MSS). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-mss-sender </span> - Sender TCP maximum segment size (MSS). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-session-without-syn </span> - Enable/disable creation of TCP session without SYN flag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> timeout-send-rst </span> - Enable/disable sending RST packets when TCP sessions expire. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper </span> - Traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper-reverse </span> - Reverse traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url-category </span> - URL category ID list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - Names of individual users that can authenticate with this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> utm-status </span> - Enable to add one or more security profiles (AV, IPS, etc. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vlan-cos-fwd </span> - VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vlan-cos-rev </span> - VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> voip-profile </span> - Name of an existing VoIP profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vpn_dst_node </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> seq </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> subnet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> vpn_src_node </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> seq </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> subnet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> vpntunnel </span> - Policy-based IPsec VPN: name of the IPsec VPN Phase 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> waf-profile </span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt </span> - Enable/disable WAN optimization. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-detection </span> - WAN optimization auto-detection mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-passive-opt </span> - WAN optimization passive mode options. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-peer </span> - WAN optimization peer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-profile </span> - WAN optimization profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wccp </span> - Enable/disable forwarding traffic matching this policy to a configured WCCP server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webcache </span> - Enable/disable web cache. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webcache-https </span> - Enable/disable web cache for HTTPS. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile </span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wsso </span> - Enable/disable WiFi Single Sign On (WSSO). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy</span>  </li>
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



