:source: fmgr_switchcontroller_managedswitch.py

:orphan:

.. _fmgr_switchcontroller_managedswitch:

fmgr_switchcontroller_managedswitch -- Configure FortiSwitch devices that are managed by this FortiGate.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>switchcontroller_managedswitch</td>
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
 <li><span class="li-head">switchcontroller_managedswitch</span> - Configure FortiSwitch devices that are managed by this FortiGate. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_platform</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Managed-switch name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allowed-vlans</span> - Configure switch port tagged vlans <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">allowed-vlans-all</span> - Enable/disable all defined vlans on this port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">arp-inspection-trust</span> - Trusted or untrusted dynamic ARP inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [untrusted, trusted]</span> </li>
 <li><span class="li-head">bundle</span> - Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">description</span> - Description for port. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-snoop-option82-trust</span> - Enable/disable allowance of DHCP with option-82 on untrusted interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-snooping</span> - Trusted or untrusted DHCP-snooping interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [trusted, untrusted]</span> </li>
 <li><span class="li-head">discard-mode</span> - Configure discard mode for port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, all-untagged, all-tagged]</span> </li>
 <li><span class="li-head">edge-port</span> - Enable/disable this interface as an edge port, bridging connections between workstations and/or computers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmp-snooping</span> - Set IGMP snooping mode for the physical port interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-reports</span> - Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-traffic</span> - Enable/disable flooding of IGMP snooping traffic to this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-speed</span> - end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slow, fast]</span> </li>
 <li><span class="li-head">learning-limit</span> - Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lldp-profile</span> - LLDP port TLV profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">lldp-status</span> - LLDP transmit and receive status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, rx-only, tx-only, tx-rx]</span> </li>
 <li><span class="li-head">loop-guard</span> - Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">loop-guard-timeout</span> - Loop-guard timeout (0 - 120 min, default = 45). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-bundle</span> - Maximum size of LAG bundle (1 - 24, default = 24) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mclag</span> - Enable/disable multi-chassis link aggregation (MCLAG). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">member-withdrawal-behavior</span> - Port behavior after it withdraws because of loss of control packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [forward, block]</span> </li>
 <li><span class="li-head">members</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">min-bundle</span> - Minimum size of LAG bundle (1 - 24, default = 1) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - LACP mode: ignore and do not send control messages, or negotiate 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, lacp-passive, lacp-active]</span> </li>
 <li><span class="li-head">poe-pre-standard-detection</span> - Enable/disable PoE pre-standard detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">poe-status</span> - Enable/disable PoE status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port-name</span> - Switch port name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-owner</span> - Switch port name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-security-policy</span> - Switch controller authentication policy to apply to this managed switch from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-selection-criteria</span> - Algorithm for aggregate port selection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [src-mac, dst-mac, src-dst-mac, src-ip, dst-ip, src-dst-ip]</span> </li>
 <li><span class="li-head">qos-policy</span> - Switch controller QoS policy from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sample-direction</span> - sFlow sample direction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rx, tx, both]</span> </li>
 <li><span class="li-head">sflow-counter-interval</span> - sFlow sampler counter polling interval (1 - 255 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sample-rate</span> - sFlow sampler sample rate (0 - 99999 p/sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sampler</span> - Enable/disable sFlow protocol on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard</span> - Enable/disable STP BPDU guard on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard-timeout</span> - BPDU Guard disabling protection (0 - 120 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">stp-root-guard</span> - Enable/disable STP root guard on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-state</span> - Enable/disable Spanning Tree Protocol (STP) on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">type</span> - Interface type: physical or trunk port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [physical, trunk]</span> </li>
 <li><span class="li-head">untagged-vlans</span> - Configure switch port untagged vlans <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan</span> - Assign switch ports to a VLAN. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">export-to-pool-flag</span> - Switch controller export port to pool-list. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mac-addr</span> - Port/Trunk MAC. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-sample-rate</span> - Packet sampling rate (0 - 99999 p/sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">packet-sampler</span> - Enable/disable packet sampling on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">sticky-mac</span> - Enable or disable sticky-mac on the interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">storm-control-policy</span> - Switch controller storm control policy from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">access-mode</span> - Access mode of the port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [normal, nac, dynamic, static]</span> </li>
 <li><span class="li-head">ip-source-guard</span> - Enable/disable IP source guard. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mclag-icl-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">p2p-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">aggregator-mode</span> - LACP member select mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bandwidth, count]</span> </li>
 <li><span class="li-head">fec-capable</span> - FEC capable. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fec-state</span> - State of forward error correction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, cl74, cl91]</span> </li>
 <li><span class="li-head">flow-control</span> - Flow control direction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tx, rx, both]</span> </li>
 <li><span class="li-head">matched-dpp-intf-tags</span> - Matched interface tags in the dynamic port policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">matched-dpp-policy</span> - Matched child policy in the dynamic port policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">media-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pause-meter</span> - Configure ingress pause metering rate, in kbps (default = 0, disabled). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pause-meter-resume</span> - Resume threshold for resuming traffic on ingress port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [25%, 50%, 75%]</span> </li>
 <li><span class="li-head">port-policy</span> - Switch controller dynamic port policy from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rpvst-port</span> - Enable/disable inter-operability with rapid PVST on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">status</span> - Switch port admin status: up or down. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [down, up]</span> </li>
 <li><span class="li-head">trunk-member</span> - Trunk member. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">switch-id</span> - Managed-switch id. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">override-snmp-community</span> - Enable/disable overriding the global SNMP communities. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">override-snmp-sysinfo</span> - Enable/disable overriding the global SNMP system information. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">override-snmp-trap-threshold</span> - Enable/disable overriding the global SNMP trap threshold values. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">override-snmp-user</span> - Enable/disable overriding the global SNMP users. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">poe-detection-type</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">remote-log</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">csv</span> - Enable/disable comma-separated value (CSV) strings. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">facility</span> - Facility to log to remote syslog server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [kernel, user, mail, daemon, auth, syslog, lpr, news, uucp, cron, authpriv, ftp, ntp, audit, alert, clock, local0, local1, local2, local3, local4, local5, local6, local7]</span> </li>
 <li><span class="li-head">name</span> - Remote log name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Remote syslog server listening port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server</span> - IPv4 address of the remote syslog server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">severity</span> - Severity of logs to be transferred to remote log server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warning, notification, information, debug]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable logging by FortiSwitch device to a remote syslog server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">snmp-community</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">events</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [cpu-high, mem-low, log-full, intf-ip, ent-conf-change]</span> </li>
 <li><span class="li-head">hosts</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Host entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the SNMP manager (host). <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">id</span> - SNMP community ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - SNMP community name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">query-v1-port</span> - SNMP v1 query port (default = 161). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">query-v1-status</span> - Enable/disable SNMP v1 queries. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">query-v2c-port</span> - SNMP v2c query port (default = 161). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">query-v2c-status</span> - Enable/disable SNMP v2c queries. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this SNMP community. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">trap-v1-lport</span> - SNMP v2c trap local port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v1-rport</span> - SNMP v2c trap remote port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v1-status</span> - Enable/disable SNMP v1 traps. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">trap-v2c-lport</span> - SNMP v2c trap local port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v2c-rport</span> - SNMP v2c trap remote port (default = 162). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">trap-v2c-status</span> - Enable/disable SNMP v2c traps. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">snmp-user</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">auth-proto</span> - Authentication protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [md5, sha]</span> </li>
 <li><span class="li-head">auth-pwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">name</span> - SNMP user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priv-proto</span> - Privacy (encryption) protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [des, aes]</span> </li>
 <li><span class="li-head">priv-pwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">queries</span> - Enable/disable SNMP queries for this user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">query-port</span> - SNMPv3 query port (default = 161). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-level</span> - Security level for message authentication and encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no-auth-no-priv, auth-no-priv, auth-priv]</span> </li>
 </ul>
 <li><span class="li-head">ip-source-guard</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">binding-entry</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">entry-name</span> - Configure binding pair. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - Source IP for this rule. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mac</span> - MAC address for this rule. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Ingress interface to which source guard is bound. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">l3-discovered</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mclag-igmp-snooping-aware</span> - Enable/disable MCLAG IGMP-snooping awareness. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">qos-drop-policy</span> - Set QoS drop-policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [taildrop, random-early-detection]</span> </li>
 <li><span class="li-head">qos-red-probability</span> - Set QoS RED/WRED drop probability. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">switch-dhcp_opt43_key</span> - DHCP option43 key. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">custom-command</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">command-entry</span> - List of FortiSwitch commands. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">command-name</span> - Names of commands to be pushed to this FortiSwitch device, as configured under config switch-controller custom-command. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">firmware-provision</span> - Enable/disable provisioning of firmware to FortiSwitches on join connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">firmware-provision-version</span> - Firmware version to provision to this FortiSwitch on bootup (major. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tdr-supported</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: Configure FortiSwitch devices that are managed by this FortiGate.
      fmgr_switchcontroller_managedswitch:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         switchcontroller_managedswitch:
            _platform: <value of string>
            description: <value of string>
            name: <value of string>
            ports:
              -
                  allowed-vlans: <value of string>
                  allowed-vlans-all: <value in [disable, enable]>
                  arp-inspection-trust: <value in [untrusted, trusted]>
                  bundle: <value in [disable, enable]>
                  description: <value of string>
                  dhcp-snoop-option82-trust: <value in [disable, enable]>
                  dhcp-snooping: <value in [trusted, untrusted]>
                  discard-mode: <value in [none, all-untagged, all-tagged]>
                  edge-port: <value in [disable, enable]>
                  igmp-snooping: <value in [disable, enable]>
                  igmps-flood-reports: <value in [disable, enable]>
                  igmps-flood-traffic: <value in [disable, enable]>
                  lacp-speed: <value in [slow, fast]>
                  learning-limit: <value of integer>
                  lldp-profile: <value of string>
                  lldp-status: <value in [disable, rx-only, tx-only, ...]>
                  loop-guard: <value in [disabled, enabled]>
                  loop-guard-timeout: <value of integer>
                  max-bundle: <value of integer>
                  mclag: <value in [disable, enable]>
                  member-withdrawal-behavior: <value in [forward, block]>
                  members: <value of string>
                  min-bundle: <value of integer>
                  mode: <value in [static, lacp-passive, lacp-active]>
                  poe-pre-standard-detection: <value in [disable, enable]>
                  poe-status: <value in [disable, enable]>
                  port-name: <value of string>
                  port-owner: <value of string>
                  port-security-policy: <value of string>
                  port-selection-criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
                  qos-policy: <value of string>
                  sample-direction: <value in [rx, tx, both]>
                  sflow-counter-interval: <value of integer>
                  sflow-sample-rate: <value of integer>
                  sflow-sampler: <value in [disabled, enabled]>
                  stp-bpdu-guard: <value in [disabled, enabled]>
                  stp-bpdu-guard-timeout: <value of integer>
                  stp-root-guard: <value in [disabled, enabled]>
                  stp-state: <value in [disabled, enabled]>
                  type: <value in [physical, trunk]>
                  untagged-vlans: <value of string>
                  vlan: <value of string>
                  export-to-pool-flag: <value of integer>
                  mac-addr: <value of string>
                  packet-sample-rate: <value of integer>
                  packet-sampler: <value in [disabled, enabled]>
                  sticky-mac: <value in [disable, enable]>
                  storm-control-policy: <value of string>
                  access-mode: <value in [normal, nac, dynamic, ...]>
                  ip-source-guard: <value in [disable, enable]>
                  mclag-icl-port: <value of integer>
                  p2p-port: <value of integer>
                  aggregator-mode: <value in [bandwidth, count]>
                  fec-capable: <value of integer>
                  fec-state: <value in [disabled, cl74, cl91]>
                  flow-control: <value in [disable, tx, rx, ...]>
                  matched-dpp-intf-tags: <value of string>
                  matched-dpp-policy: <value of string>
                  media-type: <value of string>
                  pause-meter: <value of integer>
                  pause-meter-resume: <value in [25%, 50%, 75%]>
                  port-policy: <value of string>
                  rpvst-port: <value in [disabled, enabled]>
                  status: <value in [down, up]>
                  trunk-member: <value of integer>
            switch-id: <value of string>
            override-snmp-community: <value in [disable, enable]>
            override-snmp-sysinfo: <value in [disable, enable]>
            override-snmp-trap-threshold: <value in [disable, enable]>
            override-snmp-user: <value in [disable, enable]>
            poe-detection-type: <value of integer>
            remote-log:
              -
                  csv: <value in [disable, enable]>
                  facility: <value in [kernel, user, mail, ...]>
                  name: <value of string>
                  port: <value of integer>
                  server: <value of string>
                  severity: <value in [emergency, alert, critical, ...]>
                  status: <value in [disable, enable]>
            snmp-community:
              -
                  events:
                    - cpu-high
                    - mem-low
                    - log-full
                    - intf-ip
                    - ent-conf-change
                  hosts:
                    -
                        id: <value of integer>
                        ip: <value of string>
                  id: <value of integer>
                  name: <value of string>
                  query-v1-port: <value of integer>
                  query-v1-status: <value in [disable, enable]>
                  query-v2c-port: <value of integer>
                  query-v2c-status: <value in [disable, enable]>
                  status: <value in [disable, enable]>
                  trap-v1-lport: <value of integer>
                  trap-v1-rport: <value of integer>
                  trap-v1-status: <value in [disable, enable]>
                  trap-v2c-lport: <value of integer>
                  trap-v2c-rport: <value of integer>
                  trap-v2c-status: <value in [disable, enable]>
            snmp-user:
              -
                  auth-proto: <value in [md5, sha]>
                  auth-pwd: <value of string>
                  name: <value of string>
                  priv-proto: <value in [des, aes]>
                  priv-pwd: <value of string>
                  queries: <value in [disable, enable]>
                  query-port: <value of integer>
                  security-level: <value in [no-auth-no-priv, auth-no-priv, auth-priv]>
            ip-source-guard:
              -
                  binding-entry:
                    -
                        entry-name: <value of string>
                        ip: <value of string>
                        mac: <value of string>
                  description: <value of string>
                  port: <value of string>
            l3-discovered: <value of integer>
            mclag-igmp-snooping-aware: <value in [disable, enable]>
            qos-drop-policy: <value in [taildrop, random-early-detection]>
            qos-red-probability: <value of integer>
            switch-dhcp_opt43_key: <value of string>
            custom-command:
              -
                  command-entry: <value of string>
                  command-name: <value of string>
            firmware-provision: <value in [disable, enable]>
            firmware-provision-version: <value of string>
            tdr-supported: <value of string>



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



