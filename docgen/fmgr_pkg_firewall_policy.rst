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
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_firewall_policy</span> - Configure IPv4 policies. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Policy action (allow/deny/ipsec). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept, ipsec, ssl-vpn]</span> </li>
 <li><span class="li-head">app-category</span> - Application category ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: int</span></li>
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
 <li><span class="li-head">ntlm-enabled-browsers</span> - No description for the parameter <span class="li-normal">type: str</span></li>
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
 <li><span class="li-head">object position</span> - No description for the parameter <span class="li-normal">type: list</span></li>
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
    - name: Configure IPv4 policies.
      fmgr_pkg_firewall_policy:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         pkg: <your own value>
         state: <value in [present, absent]>
         pkg_firewall_policy:
            action: <value in [deny, accept, ipsec, ...]>
            app-category: <value of string>
            application: <value of integer>
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
            ntlm-enabled-browsers: <value of string>
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
            object position: <value of list>



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



