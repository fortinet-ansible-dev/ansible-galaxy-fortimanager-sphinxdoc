:source: fmgr_wanprof_system_sdwan.py

:orphan:

.. _fmgr_wanprof_system_sdwan:

fmgr_wanprof_system_sdwan -- Configure redundant Internet connections with multiple outbound links and health-check profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>wanprof_system_sdwan</td>
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
 <li><span class="li-head">wanprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wanprof_system_sdwan</span> - Configure redundant Internet connections with multiple outbound links and health-check profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">duplication</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dstaddr</span> - Destination address or address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr6</span> - Destination address6 or address6 group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - Outgoing (egress) interfaces or zones. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Duplication rule ID (1 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">packet-de-duplication</span> - Enable/disable discarding of packets that have been duplicated. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">packet-duplication</span> - Configure packet duplication method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, force, on-demand]</span> </li>
 <li><span class="li-head">service</span> - Service and service group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-id</span> - SD-WAN service rule ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address or address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr6</span> - Source address6 or address6 group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - Incoming (ingress) interfaces or zones. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">duplication-max-num</span> - Maximum number of interface members a packet is duplicated in the SD-WAN zone (2 - 4, default = 2; if set to 3, the original packet plus 2 more copies are created). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fail-detect</span> - Enable/disable SD-WAN Internet connection status checking (failure detection). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">health-check</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">detect-mode</span> - The mode determining how to detect the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, passive, prefer-passive]</span> </li>
 <li><span class="li-head">diffservcode</span> - Differentiated services code point (DSCP) in the IP header of the probe packet. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-match-ip</span> - Response IP expected from DNS server if the protocol is DNS. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-request-domain</span> - Fully qualified domain name to resolve for the DNS probe. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">failtime</span> - Number of failures before server is considered lost (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ftp-file</span> - Full path and file name on the FTP server to download for FTP health-check to probe. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ftp-mode</span> - FTP mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [passive, port]</span> </li>
 <li><span class="li-head">ha-priority</span> - HA election priority (1 - 50). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-agent</span> - String in the http-agent field in the HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-get</span> - URL used to communicate with the server if the protocol if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-match</span> - Response string expected from the server if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interval</span> - Status check interval in milliseconds, or the time between attempting to connect to the server (500 - 3600*1000 msec, default = 500). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Status check or health check name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-size</span> - Packet size of a twamp test session, <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">port</span> - Port number used to communicate with the server over the selected protocol (0-65535, default = 0, auto select. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">probe-count</span> - Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">probe-packets</span> - Enable/disable transmission of probe packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">probe-timeout</span> - Time to wait before a probe packet is considered lost (500 - 3600*1000 msec, default = 500). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">protocol</span> - Protocol used to determine if the FortiGate can communicate with the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http, twamp, ping6, dns, tcp-connect, ftp]</span> </li>
 <li><span class="li-head">quality-measured-method</span> - Method to measure the quality of tcp-connect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [half-close, half-open]</span> </li>
 <li><span class="li-head">recoverytime</span> - Number of successful responses received before server is considered recovered (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-mode</span> - Twamp controller security mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, authentication]</span> </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">jitter-threshold</span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-threshold</span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [latency, jitter, packet-loss]</span> </li>
 <li><span class="li-head">packetloss-threshold</span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sla-fail-log-period</span> - Time interval in seconds that SLA fail log messages will be generated (0 - 3600, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sla-pass-log-period</span> - Time interval in seconds that SLA pass log messages will be generated (0 - 3600, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">system-dns</span> - Enable/disable system DNS as the probe server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">threshold-alert-jitter</span> - Alert threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-latency</span> - Alert threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-packetloss</span> - Alert threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-jitter</span> - Warning threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-latency</span> - Warning threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-packetloss</span> - Warning threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-cascade-interface</span> - Enable/disable update cascade interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">update-static-route</span> - Enable/disable updating the static route. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user</span> - The user name to access probe server. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">load-balance-mode</span> - Algorithm or mode to use for load balancing Internet traffic to SD-WAN members. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [source-ip-based, weight-based, usage-based, source-dest-ip-based, measured-volume-based]</span> </li>
 <li><span class="li-head">members</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cost</span> - Cost of this interface for services in SLA mode (0 - 4294967295, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gateway</span> - The default gateway for this interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway6</span> - IPv6 gateway. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - Ingress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - Interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - Priority of the interface for IPv4 (0 - 65535, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority6</span> - Priority of the interface for IPv6 (1 - 65535, default = 1024). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq-num</span> - Sequence number(1-512). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source</span> - Source IP address used in the health-check packet to the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source6</span> - Source IPv6 address used in the health-check packet to the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spillover-threshold</span> - Egress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this interface in the SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">volume-ratio</span> - Measured volume ratio (this value / sum of all values = percentage of link volume, 1 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">weight</span> - Weight of this interface for weighted load balancing. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">zone</span> - Zone name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">neighbor</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">health-check</span> - SD-WAN health-check name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - IP/IPv6 address of neighbor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">member</span> - Member sequence number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">role</span> - Role of neighbor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [primary, secondary, standalone]</span> </li>
 <li><span class="li-head">sla-id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">neighbor-hold-boot-time</span> - Waiting period in seconds when switching from the primary neighbor to the secondary neighbor from the neighbor start. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">neighbor-hold-down</span> - Enable/disable hold switching from the secondary neighbor to the primary neighbor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">neighbor-hold-down-time</span> - Waiting period in seconds when switching from the secondary neighbor to the primary neighbor when hold-down is disabled. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">bandwidth-weight</span> - Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">default</span> - Enable/disable use of SD-WAN as default service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward</span> - Enable/disable forward traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward-tag</span> - Forward traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dscp-reverse</span> - Enable/disable reverse traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-reverse-tag</span> - Reverse traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst</span> - Destination address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst-negate</span> - Enable/disable negation of destination address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dst6</span> - Destination address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-port</span> - End destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gateway</span> - Enable/disable SD-WAN service gateway. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - User groups. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hash-mode</span> - Hash algorithm for selected priority members for load balance mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [round-robin, source-ip-based, source-dest-ip-based, inbandwidth, outbandwidth, bibandwidth]</span> </li>
 <li><span class="li-head">health-check</span> - Health check list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hold-down-time</span> - Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - SD-WAN rule ID (1 - 4000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">input-device</span> - Source interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">input-device-negate</span> - Enable/disable negation of input device match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet service for application-based load balancing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-app-ctrl</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">internet-service-app-ctrl-group</span> - Application control based Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet service name list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom-group</span> - Custom Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-group</span> - Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-name</span> - Internet service name list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">jitter-weight</span> - Coefficient of jitter in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-weight</span> - Coefficient of latency in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - Link cost factor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [latency, jitter, packet-loss, inbandwidth, outbandwidth, bibandwidth, custom-profile-1]</span> </li>
 <li><span class="li-head">link-cost-threshold</span> - Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">minimum-sla-meet-members</span> - Minimum number of members which meet SLA. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - Control how the SD-WAN rule sets the priority of interfaces in the SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, manual, priority, sla, load-balance]</span> </li>
 <li><span class="li-head">name</span> - SD-WAN rule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-loss-weight</span> - Coefficient of packet-loss in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority-members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">protocol</span> - Protocol number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">quality-link</span> - Quality grade. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">role</span> - Service role to work with neighbor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [primary, secondary, standalone]</span> </li>
 <li><span class="li-head">route-tag</span> - IPv4 route map route-tag. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">health-check</span> - SD-WAN health-check. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sla-compare-method</span> - Method to compare SLA value for SLA mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [order, number]</span> </li>
 <li><span class="li-head">src</span> - Source address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">src-negate</span> - Enable/disable negation of source address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">src6</span> - Source address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">standalone-action</span> - Enable/disable service when selected neighbor role is standalone while service role is not standalone. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">start-port</span> - Start destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SD-WAN service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tie-break</span> - Method of selecting member if more than one meets the SLA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [zone, cfg-order, fib-best-match]</span> </li>
 <li><span class="li-head">tos</span> - Type of service bit pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - Type of service evaluated bits. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">use-shortcut-sla</span> - Enable/disable use of ADVPN shortcut for quality comparison. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">users</span> - User name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Enable/disable SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">zone</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Zone name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-sla-tie-break</span> - Method of selecting member if more than one meets the SLA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [cfg-order, fib-best-match]</span> </li>
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
    - name: Configure redundant Internet connections with multiple outbound links and health-check profiles.
      fmgr_wanprof_system_sdwan:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         wanprof: <your own value>
         wanprof_system_sdwan:
            duplication:
              -
                  dstaddr: <value of string>
                  dstaddr6: <value of string>
                  dstintf: <value of string>
                  id: <value of integer>
                  packet-de-duplication: <value in [disable, enable]>
                  packet-duplication: <value in [disable, force, on-demand]>
                  service: <value of string>
                  service-id: <value of string>
                  srcaddr: <value of string>
                  srcaddr6: <value of string>
                  srcintf: <value of string>
            duplication-max-num: <value of integer>
            fail-detect: <value in [disable, enable]>
            health-check:
              -
                  addr-mode: <value in [ipv4, ipv6]>
                  detect-mode: <value in [active, passive, prefer-passive]>
                  diffservcode: <value of string>
                  dns-match-ip: <value of string>
                  dns-request-domain: <value of string>
                  failtime: <value of integer>
                  ftp-file: <value of string>
                  ftp-mode: <value in [passive, port]>
                  ha-priority: <value of integer>
                  http-agent: <value of string>
                  http-get: <value of string>
                  http-match: <value of string>
                  interval: <value of integer>
                  members: <value of string>
                  name: <value of string>
                  packet-size: <value of integer>
                  password: <value of string>
                  port: <value of integer>
                  probe-count: <value of integer>
                  probe-packets: <value in [disable, enable]>
                  probe-timeout: <value of integer>
                  protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                  quality-measured-method: <value in [half-close, half-open]>
                  recoverytime: <value of integer>
                  security-mode: <value in [none, authentication]>
                  server: <value of string>
                  sla:
                    -
                        id: <value of integer>
                        jitter-threshold: <value of integer>
                        latency-threshold: <value of integer>
                        link-cost-factor:
                          - latency
                          - jitter
                          - packet-loss
                        packetloss-threshold: <value of integer>
                  sla-fail-log-period: <value of integer>
                  sla-pass-log-period: <value of integer>
                  system-dns: <value in [disable, enable]>
                  threshold-alert-jitter: <value of integer>
                  threshold-alert-latency: <value of integer>
                  threshold-alert-packetloss: <value of integer>
                  threshold-warning-jitter: <value of integer>
                  threshold-warning-latency: <value of integer>
                  threshold-warning-packetloss: <value of integer>
                  update-cascade-interface: <value in [disable, enable]>
                  update-static-route: <value in [disable, enable]>
                  user: <value of string>
            load-balance-mode: <value in [source-ip-based, weight-based, usage-based, ...]>
            members:
              -
                  comment: <value of string>
                  cost: <value of integer>
                  gateway: <value of string>
                  gateway6: <value of string>
                  ingress-spillover-threshold: <value of integer>
                  interface: <value of string>
                  priority: <value of integer>
                  priority6: <value of integer>
                  seq-num: <value of integer>
                  source: <value of string>
                  source6: <value of string>
                  spillover-threshold: <value of integer>
                  status: <value in [disable, enable]>
                  volume-ratio: <value of integer>
                  weight: <value of integer>
                  zone: <value of string>
            neighbor:
              -
                  health-check: <value of string>
                  ip: <value of string>
                  member: <value of string>
                  role: <value in [primary, secondary, standalone]>
                  sla-id: <value of integer>
            neighbor-hold-boot-time: <value of integer>
            neighbor-hold-down: <value in [disable, enable]>
            neighbor-hold-down-time: <value of integer>
            service:
              -
                  addr-mode: <value in [ipv4, ipv6]>
                  bandwidth-weight: <value of integer>
                  default: <value in [disable, enable]>
                  dscp-forward: <value in [disable, enable]>
                  dscp-forward-tag: <value of string>
                  dscp-reverse: <value in [disable, enable]>
                  dscp-reverse-tag: <value of string>
                  dst: <value of string>
                  dst-negate: <value in [disable, enable]>
                  dst6: <value of string>
                  end-port: <value of integer>
                  gateway: <value in [disable, enable]>
                  groups: <value of string>
                  hash-mode: <value in [round-robin, source-ip-based, source-dest-ip-based, ...]>
                  health-check: <value of string>
                  hold-down-time: <value of integer>
                  id: <value of integer>
                  input-device: <value of string>
                  input-device-negate: <value in [disable, enable]>
                  internet-service: <value in [disable, enable]>
                  internet-service-app-ctrl: <value of integer>
                  internet-service-app-ctrl-group: <value of string>
                  internet-service-custom: <value of string>
                  internet-service-custom-group: <value of string>
                  internet-service-group: <value of string>
                  internet-service-name: <value of string>
                  jitter-weight: <value of integer>
                  latency-weight: <value of integer>
                  link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
                  link-cost-threshold: <value of integer>
                  minimum-sla-meet-members: <value of integer>
                  mode: <value in [auto, manual, priority, ...]>
                  name: <value of string>
                  packet-loss-weight: <value of integer>
                  priority-members: <value of string>
                  protocol: <value of integer>
                  quality-link: <value of integer>
                  role: <value in [primary, secondary, standalone]>
                  route-tag: <value of integer>
                  sla:
                    -
                        health-check: <value of string>
                        id: <value of integer>
                  sla-compare-method: <value in [order, number]>
                  src: <value of string>
                  src-negate: <value in [disable, enable]>
                  src6: <value of string>
                  standalone-action: <value in [disable, enable]>
                  start-port: <value of integer>
                  status: <value in [disable, enable]>
                  tie-break: <value in [zone, cfg-order, fib-best-match]>
                  tos: <value of string>
                  tos-mask: <value of string>
                  use-shortcut-sla: <value in [disable, enable]>
                  users: <value of string>
            status: <value in [disable, enable]>
            zone:
              -
                  name: <value of string>
                  service-sla-tie-break: <value in [cfg-order, fib-best-match]>



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



