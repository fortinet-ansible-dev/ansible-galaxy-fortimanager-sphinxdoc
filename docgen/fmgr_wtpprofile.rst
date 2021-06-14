:source: fmgr_wtpprofile.py

:orphan:

.. _fmgr_wtpprofile:

fmgr_wtpprofile -- Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>wtpprofile</td>
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
 <li><span class="li-head">wtpprofile</span> - Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ssh, snmp, http, telnet]</span> </li>
 <li><span class="li-head">ap-country</span> - Country in which this WTP, FortiAP or AP will operate (default = NA, automatically use the country configured for the current VDOM). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [AL, DZ, AR, AM, AU, AT, AZ, BH, BD, BY, BE, BZ, BO, BA, BR, BN, BG, CA, CL, CN, CO, CR, HR, CY, CZ, DK, DO, EC, EG, SV, EE, FI, FR, GE, DE, GR, GT, HN, HK, HU, IS, IN, ID, IR, IE, IL, IT, JM, JP, JO, KZ, KE, KP, KR, KW, LV, LB, LI, LT, LU, MO, MK, MY, MT, MX, MC, MA, NP, NL, AN, NZ, NO, OM, PK, PA, PG, PE, PH, PL, PT, PR, QA, RO, RU, SA, SG, SK, SI, ZA, ES, LK, SE, CH, SY, TW, TH, TT, TN, TR, AE, UA, GB, US, PS, UY, UZ, VE, VN, YE, ZW, NA, KH, TZ, SD, AO, RW, MZ, RS, ME, BB, GD, GL, GU, PY, HT, AW, MM, ZB, CF, BS, VC, MV, AF, ZM, SN, CI, GH, CM, MW, ML, BJ, MG, TD, BW, LY, LS, MU, CG, UG, BF, SL, CD, NE, TG, MR, RE, IQ, MD, KY, BM, TC, VI, PM, MF, IM, FO, GI, TM, VU, FJ, LA, WF, MH, BT, FM, PF, NI, GY, KN, GF, AS, MP, PW, LC, GP, ET, SR, CX, DM, MQ, YT, BL]</span> </li>
 <li><span class="li-head">ble-profile</span> - Bluetooth Low Energy profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">control-message-offload</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis, ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health, spectral-analysis]</span> </li>
 <li><span class="li-head">deny-mac-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mac</span> - A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">dtls-in-kernel</span> - Enable/disable data channel DTLS in kernel. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dtls-policy</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [clear-text, dtls-enabled, ipsec-vpn]</span> </li>
 <li><span class="li-head">energy-efficient-ethernet</span> - Enable/disable use of energy efficient Ethernet on WTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ext-info-enable</span> - Enable/disable station/VAP/radio extension information. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">handoff-roaming</span> - Enable/disable client load balancing during roaming to avoid roaming delay (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">handoff-rssi</span> - Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, default = 25). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">handoff-sta-thresh</span> - Threshold value for AP handoff. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-fragment-preventing</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tcp-mss-adjust, icmp-unreachable]</span> </li>
 <li><span class="li-head">led-schedules</span> - Recurring firewall schedules for illuminating LEDs on the FortiAP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">led-state</span> - Enable/disable use of LEDs on WTP (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lldp</span> - Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">login-passwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">login-passwd-change</span> - Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes, default]</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no client limitation). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - WTP (or FortiAP or AP) profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">poe-mode</span> - Set the WTP, FortiAP, or APs PoE mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, 8023af, 8023at, power-adapter, full, high, low]</span> </li>
 <li><span class="li-head">split-tunneling-acl</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dest-ip</span> - Destination IP and mask for the split-tunneling subnet. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">split-tunneling-acl-local-ap-subnet</span> - Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">split-tunneling-acl-path</span> - Split tunneling ACL path is local/tunnel. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tunnel, local]</span> </li>
 <li><span class="li-head">tun-mtu-downlink</span> - Downlink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tun-mtu-uplink</span> - Uplink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wan-port-mode</span> - Enable/disable using a WAN port as a LAN port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [wan-lan, wan-only]</span> </li>
 <li><span class="li-head">snmp</span> - Enable/disable SNMP for the WTP, FortiAP, or AP (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-handoff</span> - Enable/disable AP handoff of clients to other APs (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">apcfg-profile</span> - AP local configuration profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">frequency-handoff</span> - Enable/disable frequency handoff of clients to other channels (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lan</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">port-esl-mode</span> - ESL port mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port-esl-ssid</span> - Bridge ESL port to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-mode</span> - LAN port mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port-ssid</span> - Bridge LAN port to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port1-mode</span> - LAN port 1 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port1-ssid</span> - Bridge LAN port 1 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port2-mode</span> - LAN port 2 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port2-ssid</span> - Bridge LAN port 2 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port3-mode</span> - LAN port 3 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port3-ssid</span> - Bridge LAN port 3 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port4-mode</span> - LAN port 4 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port4-ssid</span> - Bridge LAN port 4 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port5-mode</span> - LAN port 5 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port5-ssid</span> - Bridge LAN port 5 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port6-mode</span> - LAN port 6 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port6-ssid</span> - Bridge LAN port 6 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port7-mode</span> - LAN port 7 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port7-ssid</span> - Bridge LAN port 7 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port8-mode</span> - LAN port 8 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port8-ssid</span> - Bridge LAN port 8 to SSID. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">lbs</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">aeroscout</span> - Enable/disable AeroScout Real Time Location Service (RTLS) support (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-ap-mac</span> - Use BSSID or board MAC address as AP MAC address in AeroScout AP messages (default = bssid). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bssid, board-mac]</span> </li>
 <li><span class="li-head">aeroscout-mmu-report</span> - Enable/disable compounded AeroScout tag and MU report (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-mu</span> - Enable/disable AeroScout Mobile Unit (MU) support (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-mu-factor</span> - AeroScout MU mode dilution factor (default = 20). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">aeroscout-mu-timeout</span> - AeroScout MU mode timeout (0 - 65535 sec, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">aeroscout-server-ip</span> - IP address of AeroScout server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">aeroscout-server-port</span> - AeroScout server UDP listening port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ekahau-blink-mode</span> - Enable/disable Ekahau blink mode (now known as AiRISTA Flow) to track and locate WiFi tags (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ekahau-tag</span> - WiFi frame MAC address or WiFi Tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">erc-server-ip</span> - IP address of Ekahau RTLS Controller (ERC). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">erc-server-port</span> - Ekahau RTLS Controller (ERC) UDP listening port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence</span> - Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi network (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, enable2, foreign, both]</span> </li>
 <li><span class="li-head">fortipresence-ble</span> - Enable/disable FortiPresence finding and reporting BLE devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortipresence-frequency</span> - FortiPresence report transmit frequency (5 - 65535 sec, default = 30). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence-port</span> - FortiPresence server UDP listening port (default = 3000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence-project</span> - FortiPresence project name (max. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortipresence-rogue</span> - Enable/disable FortiPresence finding and reporting rogue APs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortipresence-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">fortipresence-server</span> - FortiPresence server IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortipresence-unassoc</span> - Enable/disable FortiPresence finding and reporting unassociated stations. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">station-locate</span> - Enable/disable client station locating services for all clients, whether associated or not (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">platform</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">_local_platform_str</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddscan</span> - Enable/disable use of one radio for dedicated dual-band scanning to detect RF characterization and wireless threat management. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mode</span> - Configure operation mode of 5G radios (default = single-5G). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dual-5G, single-5G]</span> </li>
 <li><span class="li-head">type</span> - WTP, FortiAP or AP platform type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [30B-50B, 60B, 80CM-81CM, 220A, 220B, 210B, 60C, 222B, 112B, 320B, 11C, 14C, 223B, 28C, 320C, 221C, 25D, 222C, 224D, 214B, 21D, 24D, 112D, 223C, 321C, C220C, C225C, S321C, S323C, FWF, S311C, S313C, AP-11N, S322C, S321CR, S322CR, S323CR, S421E, S422E, S423E, 421E, 423E, C221E, C226E, C23JD, C24JE, C21D, U421E, U423E, 221E, 222E, 223E, S221E, S223E, U221EV, U223EV, U321EV, U323EV, 224E, U422EV, U24JEV, 321E, U431F, U433F, 231E, 431F, 433F, 231F, 432F, 234F, 23JF, U231F, 831F, U234F, U432F]</span> </li>
 </ul>
 <li><span class="li-head">radio-1</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">airtime-fairness</span> - Enable/disable airtime fairness (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">amsdu</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-addr</span> - MAC address to monitor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-sniffer-bufsize</span> - Sniffer buffer size (1 - 32 MB, default = 16). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-chan</span> - Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-ctl</span> - Enable/disable sniffer on WiFi control frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-data</span> - Enable/disable sniffer on WiFi data frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-beacon</span> - Enable/disable sniffer on WiFi management Beacon frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-other</span> - Enable/disable sniffer on WiFi management other frames  (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-probe</span> - Enable/disable sniffer on WiFi management probe frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-high</span> - The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-level</span> - Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-low</span> - The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-target</span> - The target of automatic transmit power adjustment in dBm. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">band</span> - WiFi band that Radio 1 operates on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.11b, 802.11a, 802.11g, 802.11n, 802.11ac, 802.11n-5G, 802.11ax-5G, 802.11ax, 802.11ac-2G, 802.11g-only, 802.11n-only, 802.11n,g-only, 802.11ac-only, 802.11ac,n-only, 802.11n-5G-only, 802.11ax-5G-only, 802.11ax,ac-only, 802.11ax,ac,n-only, 802.11ax-only, 802.11ax,n-only, 802.11ax,n,g-only]</span> </li>
 <li><span class="li-head">band-5g-type</span> - WiFi 5G band type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [5g-full, 5g-high, 5g-low]</span> </li>
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">beacon-interval</span> - Beacon interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bss-color</span> - BSS color value for this 11ax radio (0 - 63, 0 means disable. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">channel</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">channel-bonding</span> - Channel bandwidth: 160,80, 40, or 20MHz. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, 80MHz, 40MHz, 20MHz, 160MHz]</span> </li>
 <li><span class="li-head">channel-utilization</span> - Enable/disable measuring channel utilization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">coexistence</span> - Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">darrp</span> - Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma</span> - Enable/disable dynamic radio mode assignment (DRMA) (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma-sensitivity</span> - Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">dtim</span> - Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frag-threshold</span> - Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">iperf-protocol</span> - Iperf test protocol (default = "UDP"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [udp, tcp]</span> </li>
 <li><span class="li-head">iperf-server-port</span> - Iperf service port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) or WiFi clients supported by the radio. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-distance</span> - Maximum expected distance between the AP and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - Mode of radio 1. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, ap, monitor, sniffer, sam]</span> </li>
 <li><span class="li-head">power-level</span> - Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">power-mode</span> - Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dBm, percentage]</span> </li>
 <li><span class="li-head">power-value</span> - Radio EIRP power in dBm (1 - 33, default = 27). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">powersave-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tim, ac-vo, no-obss-scan, no-11b-rate, client-rate-follow]</span> </li>
 <li><span class="li-head">protection-mode</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rtscts, ctsonly, disable]</span> </li>
 <li><span class="li-head">radio-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rts-threshold</span> - Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-bssid</span> - BSSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-captive-portal</span> - Enable/disable Captive Portal Authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sam-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sam-report-intv</span> - SAM report interval (sec), 0 for a one-time report. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-security-type</span> - Select WiFi network security type (default = "wpa-personal"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [open, wpa-personal, wpa-enterprise]</span> </li>
 <li><span class="li-head">sam-server</span> - SAM test server IP address or domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-ssid</span> - SSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-test</span> - Select SAM test type (default = "PING"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, iperf]</span> </li>
 <li><span class="li-head">sam-username</span> - Username for WiFi network connection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">short-guard-interval</span> - Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">transmit-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [disable, power-save, aggr-limit, retry-limit, send-bar]</span> </li>
 <li><span class="li-head">vap-all</span> - Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, tunnel, bridge, manual]</span> </li>
 <li><span class="li-head">vap1</span> - Virtual Access Point (VAP) for wlan ID 1 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap2</span> - Virtual Access Point (VAP) for wlan ID 2 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap3</span> - Virtual Access Point (VAP) for wlan ID 3 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap4</span> - Virtual Access Point (VAP) for wlan ID 4 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap5</span> - Virtual Access Point (VAP) for wlan ID 5 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap6</span> - Virtual Access Point (VAP) for wlan ID 6 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap7</span> - Virtual Access Point (VAP) for wlan ID 7 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap8</span> - Virtual Access Point (VAP) for wlan ID 8 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vaps</span> - Manually selected list of Virtual Access Points (VAPs). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wids-profile</span> - Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">zero-wait-dfs</span> - Enable/disable zero wait DFS on radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">radio-2</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">airtime-fairness</span> - Enable/disable airtime fairness (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">amsdu</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-addr</span> - MAC address to monitor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-sniffer-bufsize</span> - Sniffer buffer size (1 - 32 MB, default = 16). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-chan</span> - Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-ctl</span> - Enable/disable sniffer on WiFi control frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-data</span> - Enable/disable sniffer on WiFi data frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-beacon</span> - Enable/disable sniffer on WiFi management Beacon frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-other</span> - Enable/disable sniffer on WiFi management other frames  (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-probe</span> - Enable/disable sniffer on WiFi management probe frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-high</span> - The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-level</span> - Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-low</span> - The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-target</span> - The target of automatic transmit power adjustment in dBm. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">band</span> - WiFi band that Radio 2 operates on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.11b, 802.11a, 802.11g, 802.11n, 802.11ac, 802.11n-5G, 802.11ax-5G, 802.11ax, 802.11ac-2G, 802.11g-only, 802.11n-only, 802.11n,g-only, 802.11ac-only, 802.11ac,n-only, 802.11n-5G-only, 802.11ax-5G-only, 802.11ax,ac-only, 802.11ax,ac,n-only, 802.11ax-only, 802.11ax,n-only, 802.11ax,n,g-only]</span> </li>
 <li><span class="li-head">band-5g-type</span> - WiFi 5G band type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [5g-full, 5g-high, 5g-low]</span> </li>
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">beacon-interval</span> - Beacon interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bss-color</span> - BSS color value for this 11ax radio (0 - 63, 0 means disable. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">channel</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">channel-bonding</span> - Channel bandwidth: 160,80, 40, or 20MHz. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, 80MHz, 40MHz, 20MHz, 160MHz]</span> </li>
 <li><span class="li-head">channel-utilization</span> - Enable/disable measuring channel utilization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">coexistence</span> - Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">darrp</span> - Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma</span> - Enable/disable dynamic radio mode assignment (DRMA) (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma-sensitivity</span> - Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">dtim</span> - Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frag-threshold</span> - Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">iperf-protocol</span> - Iperf test protocol (default = "UDP"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [udp, tcp]</span> </li>
 <li><span class="li-head">iperf-server-port</span> - Iperf service port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) or WiFi clients supported by the radio. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-distance</span> - Maximum expected distance between the AP and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - Mode of radio 2. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, ap, monitor, sniffer, sam]</span> </li>
 <li><span class="li-head">power-level</span> - Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">power-mode</span> - Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dBm, percentage]</span> </li>
 <li><span class="li-head">power-value</span> - Radio EIRP power in dBm (1 - 33, default = 27). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">powersave-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tim, ac-vo, no-obss-scan, no-11b-rate, client-rate-follow]</span> </li>
 <li><span class="li-head">protection-mode</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rtscts, ctsonly, disable]</span> </li>
 <li><span class="li-head">radio-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rts-threshold</span> - Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-bssid</span> - BSSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-captive-portal</span> - Enable/disable Captive Portal Authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sam-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sam-report-intv</span> - SAM report interval (sec), 0 for a one-time report. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-security-type</span> - Select WiFi network security type (default = "wpa-personal"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [open, wpa-personal, wpa-enterprise]</span> </li>
 <li><span class="li-head">sam-server</span> - SAM test server IP address or domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-ssid</span> - SSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-test</span> - Select SAM test type (default = "PING"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, iperf]</span> </li>
 <li><span class="li-head">sam-username</span> - Username for WiFi network connection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">short-guard-interval</span> - Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">transmit-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [disable, power-save, aggr-limit, retry-limit, send-bar]</span> </li>
 <li><span class="li-head">vap-all</span> - Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, tunnel, bridge, manual]</span> </li>
 <li><span class="li-head">vap1</span> - Virtual Access Point (VAP) for wlan ID 1 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap2</span> - Virtual Access Point (VAP) for wlan ID 2 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap3</span> - Virtual Access Point (VAP) for wlan ID 3 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap4</span> - Virtual Access Point (VAP) for wlan ID 4 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap5</span> - Virtual Access Point (VAP) for wlan ID 5 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap6</span> - Virtual Access Point (VAP) for wlan ID 6 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap7</span> - Virtual Access Point (VAP) for wlan ID 7 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap8</span> - Virtual Access Point (VAP) for wlan ID 8 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vaps</span> - Manually selected list of Virtual Access Points (VAPs). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wids-profile</span> - Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">zero-wait-dfs</span> - Enable/disable zero wait DFS on radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">radio-3</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">airtime-fairness</span> - Enable/disable airtime fairness (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">amsdu</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-addr</span> - MAC address to monitor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-sniffer-bufsize</span> - Sniffer buffer size (1 - 32 MB, default = 16). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-chan</span> - Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-ctl</span> - Enable/disable sniffer on WiFi control frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-data</span> - Enable/disable sniffer on WiFi data frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-beacon</span> - Enable/disable sniffer on WiFi management Beacon frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-other</span> - Enable/disable sniffer on WiFi management other frames  (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-probe</span> - Enable/disable sniffer on WiFi management probe frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-high</span> - The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-level</span> - Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-low</span> - The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-target</span> - The target of automatic transmit power adjustment in dBm. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">band</span> - WiFi band that Radio 3 operates on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.11b, 802.11a, 802.11g, 802.11n, 802.11ac, 802.11n-5G, 802.11ax-5G, 802.11ax, 802.11ac-2G, 802.11g-only, 802.11n-only, 802.11n,g-only, 802.11ac-only, 802.11ac,n-only, 802.11n-5G-only, 802.11ax-5G-only, 802.11ax,ac-only, 802.11ax,ac,n-only, 802.11ax-only, 802.11ax,n-only, 802.11ax,n,g-only]</span> </li>
 <li><span class="li-head">band-5g-type</span> - WiFi 5G band type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [5g-full, 5g-high, 5g-low]</span> </li>
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">beacon-interval</span> - Beacon interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bss-color</span> - BSS color value for this 11ax radio (0 - 63, 0 means disable. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">channel</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">channel-bonding</span> - Channel bandwidth: 160,80, 40, or 20MHz. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [80MHz, 40MHz, 20MHz, 160MHz]</span> </li>
 <li><span class="li-head">channel-utilization</span> - Enable/disable measuring channel utilization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">coexistence</span> - Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">darrp</span> - Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma</span> - Enable/disable dynamic radio mode assignment (DRMA) (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma-sensitivity</span> - Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">dtim</span> - Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frag-threshold</span> - Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">iperf-protocol</span> - Iperf test protocol (default = "UDP"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [udp, tcp]</span> </li>
 <li><span class="li-head">iperf-server-port</span> - Iperf service port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) or WiFi clients supported by the radio. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-distance</span> - Maximum expected distance between the AP and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - Mode of radio 3. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, ap, monitor, sniffer, sam]</span> </li>
 <li><span class="li-head">power-level</span> - Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">power-mode</span> - Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dBm, percentage]</span> </li>
 <li><span class="li-head">power-value</span> - Radio EIRP power in dBm (1 - 33, default = 27). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">powersave-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tim, ac-vo, no-obss-scan, no-11b-rate, client-rate-follow]</span> </li>
 <li><span class="li-head">protection-mode</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rtscts, ctsonly, disable]</span> </li>
 <li><span class="li-head">radio-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rts-threshold</span> - Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-bssid</span> - BSSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-captive-portal</span> - Enable/disable Captive Portal Authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sam-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sam-report-intv</span> - SAM report interval (sec), 0 for a one-time report. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-security-type</span> - Select WiFi network security type (default = "wpa-personal"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [open, wpa-personal, wpa-enterprise]</span> </li>
 <li><span class="li-head">sam-server</span> - SAM test server IP address or domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-ssid</span> - SSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-test</span> - Select SAM test type (default = "PING"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, iperf]</span> </li>
 <li><span class="li-head">sam-username</span> - Username for WiFi network connection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">short-guard-interval</span> - Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">transmit-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [disable, power-save, aggr-limit, retry-limit, send-bar]</span> </li>
 <li><span class="li-head">vap-all</span> - Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, tunnel, bridge, manual]</span> </li>
 <li><span class="li-head">vap1</span> - Virtual Access Point (VAP) for wlan ID 1 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap2</span> - Virtual Access Point (VAP) for wlan ID 2 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap3</span> - Virtual Access Point (VAP) for wlan ID 3 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap4</span> - Virtual Access Point (VAP) for wlan ID 4 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap5</span> - Virtual Access Point (VAP) for wlan ID 5 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap6</span> - Virtual Access Point (VAP) for wlan ID 6 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap7</span> - Virtual Access Point (VAP) for wlan ID 7 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap8</span> - Virtual Access Point (VAP) for wlan ID 8 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vaps</span> - Manually selected list of Virtual Access Points (VAPs). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wids-profile</span> - Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">zero-wait-dfs</span> - Enable/disable zero wait DFS on radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">radio-4</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">airtime-fairness</span> - Enable/disable airtime fairness (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">amsdu</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-addr</span> - MAC address to monitor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-sniffer-bufsize</span> - Sniffer buffer size (1 - 32 MB, default = 16). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-chan</span> - Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-ctl</span> - Enable/disable sniffer on WiFi control frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-data</span> - Enable/disable sniffer on WiFi data frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-beacon</span> - Enable/disable sniffer on WiFi management Beacon frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-other</span> - Enable/disable sniffer on WiFi management other frames  (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-probe</span> - Enable/disable sniffer on WiFi management probe frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-high</span> - The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-level</span> - Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-low</span> - The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-target</span> - The target of automatic transmit power adjustment in dBm. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">band</span> - WiFi band that Radio 3 operates on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.11b, 802.11a, 802.11g, 802.11n, 802.11ac, 802.11n-5G, 802.11ax-5G, 802.11ax, 802.11ac-2G, 802.11g-only, 802.11n-only, 802.11n,g-only, 802.11ac-only, 802.11ac,n-only, 802.11n-5G-only, 802.11ax-5G-only, 802.11ax,ac-only, 802.11ax,ac,n-only, 802.11ax-only, 802.11ax,n-only, 802.11ax,n,g-only]</span> </li>
 <li><span class="li-head">band-5g-type</span> - WiFi 5G band type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [5g-full, 5g-high, 5g-low]</span> </li>
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">beacon-interval</span> - Beacon interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bss-color</span> - BSS color value for this 11ax radio (0 - 63, 0 means disable. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">channel</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">channel-bonding</span> - Channel bandwidth: 160,80, 40, or 20MHz. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [80MHz, 40MHz, 20MHz, 160MHz]</span> </li>
 <li><span class="li-head">channel-utilization</span> - Enable/disable measuring channel utilization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">coexistence</span> - Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">darrp</span> - Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma</span> - Enable/disable dynamic radio mode assignment (DRMA) (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">drma-sensitivity</span> - Network Coverage Factor (NCF) percentage required to consider a radio as redundant (default = low). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">dtim</span> - Delivery Traffic Indication Map (DTIM) period (1 - 255, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frag-threshold</span> - Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">iperf-protocol</span> - Iperf test protocol (default = "UDP"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [udp, tcp]</span> </li>
 <li><span class="li-head">iperf-server-port</span> - Iperf service port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) or WiFi clients supported by the radio. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-distance</span> - Maximum expected distance between the AP and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - Mode of radio 3. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ap, monitor, sniffer, disabled, sam]</span> </li>
 <li><span class="li-head">power-level</span> - Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100, default = 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">power-mode</span> - Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP (default = percentage). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dBm, percentage]</span> </li>
 <li><span class="li-head">power-value</span> - Radio EIRP power in dBm (1 - 33, default = 27). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">powersave-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tim, ac-vo, no-obss-scan, no-11b-rate, client-rate-follow]</span> </li>
 <li><span class="li-head">protection-mode</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rtscts, ctsonly, disable]</span> </li>
 <li><span class="li-head">radio-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rts-threshold</span> - Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-bssid</span> - BSSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-captive-portal</span> - Enable/disable Captive Portal Authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sam-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sam-report-intv</span> - SAM report interval (sec), 0 for a one-time report. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sam-security-type</span> - Select WiFi network security type (default = "wpa-personal"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [open, wpa-personal, wpa-enterprise]</span> </li>
 <li><span class="li-head">sam-server</span> - SAM test server IP address or domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-ssid</span> - SSID for WiFi network. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sam-test</span> - Select SAM test type (default = "PING"). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, iperf]</span> </li>
 <li><span class="li-head">sam-username</span> - Username for WiFi network connection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">short-guard-interval</span> - Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">transmit-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [disable, power-save, aggr-limit, retry-limit, send-bar]</span> </li>
 <li><span class="li-head">vap-all</span> - Configure method for assigning SSIDs to this FortiAP (default = automatically assign tunnel SSIDs). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, tunnel, bridge, manual]</span> </li>
 <li><span class="li-head">vap1</span> - Virtual Access Point (VAP) for wlan ID 1 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap2</span> - Virtual Access Point (VAP) for wlan ID 2 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap3</span> - Virtual Access Point (VAP) for wlan ID 3 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap4</span> - Virtual Access Point (VAP) for wlan ID 4 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap5</span> - Virtual Access Point (VAP) for wlan ID 5 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap6</span> - Virtual Access Point (VAP) for wlan ID 6 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap7</span> - Virtual Access Point (VAP) for wlan ID 7 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vap8</span> - Virtual Access Point (VAP) for wlan ID 8 <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vaps</span> - Manually selected list of Virtual Access Points (VAPs). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wids-profile</span> - Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">zero-wait-dfs</span> - Enable/disable zero wait DFS on radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
      fmgr_wtpprofile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         wtpprofile:
            allowaccess:
              - https
              - ssh
              - snmp
              - http
              - telnet
            ap-country: <value in [AL, DZ, AR, ...]>
            ble-profile: <value of string>
            comment: <value of string>
            control-message-offload:
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
              - ebp-frame
              - aeroscout-tag
              - ap-list
              - sta-list
              - sta-cap-list
              - stats
              - aeroscout-mu
              - sta-health
              - spectral-analysis
            deny-mac-list:
              -
                  id: <value of integer>
                  mac: <value of string>
            dtls-in-kernel: <value in [disable, enable]>
            dtls-policy:
              - clear-text
              - dtls-enabled
              - ipsec-vpn
            energy-efficient-ethernet: <value in [disable, enable]>
            ext-info-enable: <value in [disable, enable]>
            handoff-roaming: <value in [disable, enable]>
            handoff-rssi: <value of integer>
            handoff-sta-thresh: <value of integer>
            ip-fragment-preventing:
              - tcp-mss-adjust
              - icmp-unreachable
            led-schedules: <value of string>
            led-state: <value in [disable, enable]>
            lldp: <value in [disable, enable]>
            login-passwd: <value of string>
            login-passwd-change: <value in [no, yes, default]>
            max-clients: <value of integer>
            name: <value of string>
            poe-mode: <value in [auto, 8023af, 8023at, ...]>
            split-tunneling-acl:
              -
                  dest-ip: <value of string>
                  id: <value of integer>
            split-tunneling-acl-local-ap-subnet: <value in [disable, enable]>
            split-tunneling-acl-path: <value in [tunnel, local]>
            tun-mtu-downlink: <value of integer>
            tun-mtu-uplink: <value of integer>
            wan-port-mode: <value in [wan-lan, wan-only]>
            snmp: <value in [disable, enable]>
            ap-handoff: <value in [disable, enable]>
            apcfg-profile: <value of string>
            frequency-handoff: <value in [disable, enable]>
            lan:
               port-esl-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port-esl-ssid: <value of string>
               port-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port-ssid: <value of string>
               port1-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port1-ssid: <value of string>
               port2-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port2-ssid: <value of string>
               port3-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port3-ssid: <value of string>
               port4-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port4-ssid: <value of string>
               port5-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port5-ssid: <value of string>
               port6-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port6-ssid: <value of string>
               port7-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port7-ssid: <value of string>
               port8-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
               port8-ssid: <value of string>
            lbs:
               aeroscout: <value in [disable, enable]>
               aeroscout-ap-mac: <value in [bssid, board-mac]>
               aeroscout-mmu-report: <value in [disable, enable]>
               aeroscout-mu: <value in [disable, enable]>
               aeroscout-mu-factor: <value of integer>
               aeroscout-mu-timeout: <value of integer>
               aeroscout-server-ip: <value of string>
               aeroscout-server-port: <value of integer>
               ekahau-blink-mode: <value in [disable, enable]>
               ekahau-tag: <value of string>
               erc-server-ip: <value of string>
               erc-server-port: <value of integer>
               fortipresence: <value in [disable, enable, enable2, ...]>
               fortipresence-ble: <value in [disable, enable]>
               fortipresence-frequency: <value of integer>
               fortipresence-port: <value of integer>
               fortipresence-project: <value of string>
               fortipresence-rogue: <value in [disable, enable]>
               fortipresence-secret: <value of string>
               fortipresence-server: <value of string>
               fortipresence-unassoc: <value in [disable, enable]>
               station-locate: <value in [disable, enable]>
            platform:
               _local_platform_str: <value of string>
               ddscan: <value in [disable, enable]>
               mode: <value in [dual-5G, single-5G]>
               type: <value in [30B-50B, 60B, 80CM-81CM, ...]>
            radio-1:
               airtime-fairness: <value in [disable, enable]>
               amsdu: <value in [disable, enable]>
               ap-sniffer-addr: <value of string>
               ap-sniffer-bufsize: <value of integer>
               ap-sniffer-chan: <value of integer>
               ap-sniffer-ctl: <value in [disable, enable]>
               ap-sniffer-data: <value in [disable, enable]>
               ap-sniffer-mgmt-beacon: <value in [disable, enable]>
               ap-sniffer-mgmt-other: <value in [disable, enable]>
               ap-sniffer-mgmt-probe: <value in [disable, enable]>
               auto-power-high: <value of integer>
               auto-power-level: <value in [disable, enable]>
               auto-power-low: <value of integer>
               auto-power-target: <value of string>
               band: <value in [802.11b, 802.11a, 802.11g, ...]>
               band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
               bandwidth-admission-control: <value in [disable, enable]>
               bandwidth-capacity: <value of integer>
               beacon-interval: <value of integer>
               bss-color: <value of integer>
               call-admission-control: <value in [disable, enable]>
               call-capacity: <value of integer>
               channel: <value of string>
               channel-bonding: <value in [disable, enable, 80MHz, ...]>
               channel-utilization: <value in [disable, enable]>
               coexistence: <value in [disable, enable]>
               darrp: <value in [disable, enable]>
               drma: <value in [disable, enable]>
               drma-sensitivity: <value in [low, medium, high]>
               dtim: <value of integer>
               frag-threshold: <value of integer>
               iperf-protocol: <value in [udp, tcp]>
               iperf-server-port: <value of integer>
               max-clients: <value of integer>
               max-distance: <value of integer>
               mode: <value in [disabled, ap, monitor, ...]>
               power-level: <value of integer>
               power-mode: <value in [dBm, percentage]>
               power-value: <value of integer>
               powersave-optimize:
                 - tim
                 - ac-vo
                 - no-obss-scan
                 - no-11b-rate
                 - client-rate-follow
               protection-mode: <value in [rtscts, ctsonly, disable]>
               radio-id: <value of integer>
               rts-threshold: <value of integer>
               sam-bssid: <value of string>
               sam-captive-portal: <value in [disable, enable]>
               sam-password: <value of string>
               sam-report-intv: <value of integer>
               sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
               sam-server: <value of string>
               sam-ssid: <value of string>
               sam-test: <value in [ping, iperf]>
               sam-username: <value of string>
               short-guard-interval: <value in [disable, enable]>
               transmit-optimize:
                 - disable
                 - power-save
                 - aggr-limit
                 - retry-limit
                 - send-bar
               vap-all: <value in [disable, enable, tunnel, ...]>
               vap1: <value of string>
               vap2: <value of string>
               vap3: <value of string>
               vap4: <value of string>
               vap5: <value of string>
               vap6: <value of string>
               vap7: <value of string>
               vap8: <value of string>
               vaps: <value of string>
               wids-profile: <value of string>
               zero-wait-dfs: <value in [disable, enable]>
            radio-2:
               airtime-fairness: <value in [disable, enable]>
               amsdu: <value in [disable, enable]>
               ap-sniffer-addr: <value of string>
               ap-sniffer-bufsize: <value of integer>
               ap-sniffer-chan: <value of integer>
               ap-sniffer-ctl: <value in [disable, enable]>
               ap-sniffer-data: <value in [disable, enable]>
               ap-sniffer-mgmt-beacon: <value in [disable, enable]>
               ap-sniffer-mgmt-other: <value in [disable, enable]>
               ap-sniffer-mgmt-probe: <value in [disable, enable]>
               auto-power-high: <value of integer>
               auto-power-level: <value in [disable, enable]>
               auto-power-low: <value of integer>
               auto-power-target: <value of string>
               band: <value in [802.11b, 802.11a, 802.11g, ...]>
               band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
               bandwidth-admission-control: <value in [disable, enable]>
               bandwidth-capacity: <value of integer>
               beacon-interval: <value of integer>
               bss-color: <value of integer>
               call-admission-control: <value in [disable, enable]>
               call-capacity: <value of integer>
               channel: <value of string>
               channel-bonding: <value in [disable, enable, 80MHz, ...]>
               channel-utilization: <value in [disable, enable]>
               coexistence: <value in [disable, enable]>
               darrp: <value in [disable, enable]>
               drma: <value in [disable, enable]>
               drma-sensitivity: <value in [low, medium, high]>
               dtim: <value of integer>
               frag-threshold: <value of integer>
               iperf-protocol: <value in [udp, tcp]>
               iperf-server-port: <value of integer>
               max-clients: <value of integer>
               max-distance: <value of integer>
               mode: <value in [disabled, ap, monitor, ...]>
               power-level: <value of integer>
               power-mode: <value in [dBm, percentage]>
               power-value: <value of integer>
               powersave-optimize:
                 - tim
                 - ac-vo
                 - no-obss-scan
                 - no-11b-rate
                 - client-rate-follow
               protection-mode: <value in [rtscts, ctsonly, disable]>
               radio-id: <value of integer>
               rts-threshold: <value of integer>
               sam-bssid: <value of string>
               sam-captive-portal: <value in [disable, enable]>
               sam-password: <value of string>
               sam-report-intv: <value of integer>
               sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
               sam-server: <value of string>
               sam-ssid: <value of string>
               sam-test: <value in [ping, iperf]>
               sam-username: <value of string>
               short-guard-interval: <value in [disable, enable]>
               transmit-optimize:
                 - disable
                 - power-save
                 - aggr-limit
                 - retry-limit
                 - send-bar
               vap-all: <value in [disable, enable, tunnel, ...]>
               vap1: <value of string>
               vap2: <value of string>
               vap3: <value of string>
               vap4: <value of string>
               vap5: <value of string>
               vap6: <value of string>
               vap7: <value of string>
               vap8: <value of string>
               vaps: <value of string>
               wids-profile: <value of string>
               zero-wait-dfs: <value in [disable, enable]>
            radio-3:
               airtime-fairness: <value in [disable, enable]>
               amsdu: <value in [disable, enable]>
               ap-sniffer-addr: <value of string>
               ap-sniffer-bufsize: <value of integer>
               ap-sniffer-chan: <value of integer>
               ap-sniffer-ctl: <value in [disable, enable]>
               ap-sniffer-data: <value in [disable, enable]>
               ap-sniffer-mgmt-beacon: <value in [disable, enable]>
               ap-sniffer-mgmt-other: <value in [disable, enable]>
               ap-sniffer-mgmt-probe: <value in [disable, enable]>
               auto-power-high: <value of integer>
               auto-power-level: <value in [disable, enable]>
               auto-power-low: <value of integer>
               auto-power-target: <value of string>
               band: <value in [802.11b, 802.11a, 802.11g, ...]>
               band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
               bandwidth-admission-control: <value in [disable, enable]>
               bandwidth-capacity: <value of integer>
               beacon-interval: <value of integer>
               bss-color: <value of integer>
               call-admission-control: <value in [disable, enable]>
               call-capacity: <value of integer>
               channel: <value of string>
               channel-bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
               channel-utilization: <value in [disable, enable]>
               coexistence: <value in [disable, enable]>
               darrp: <value in [disable, enable]>
               drma: <value in [disable, enable]>
               drma-sensitivity: <value in [low, medium, high]>
               dtim: <value of integer>
               frag-threshold: <value of integer>
               iperf-protocol: <value in [udp, tcp]>
               iperf-server-port: <value of integer>
               max-clients: <value of integer>
               max-distance: <value of integer>
               mode: <value in [disabled, ap, monitor, ...]>
               power-level: <value of integer>
               power-mode: <value in [dBm, percentage]>
               power-value: <value of integer>
               powersave-optimize:
                 - tim
                 - ac-vo
                 - no-obss-scan
                 - no-11b-rate
                 - client-rate-follow
               protection-mode: <value in [rtscts, ctsonly, disable]>
               radio-id: <value of integer>
               rts-threshold: <value of integer>
               sam-bssid: <value of string>
               sam-captive-portal: <value in [disable, enable]>
               sam-password: <value of string>
               sam-report-intv: <value of integer>
               sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
               sam-server: <value of string>
               sam-ssid: <value of string>
               sam-test: <value in [ping, iperf]>
               sam-username: <value of string>
               short-guard-interval: <value in [disable, enable]>
               transmit-optimize:
                 - disable
                 - power-save
                 - aggr-limit
                 - retry-limit
                 - send-bar
               vap-all: <value in [disable, enable, tunnel, ...]>
               vap1: <value of string>
               vap2: <value of string>
               vap3: <value of string>
               vap4: <value of string>
               vap5: <value of string>
               vap6: <value of string>
               vap7: <value of string>
               vap8: <value of string>
               vaps: <value of string>
               wids-profile: <value of string>
               zero-wait-dfs: <value in [disable, enable]>
            radio-4:
               airtime-fairness: <value in [disable, enable]>
               amsdu: <value in [disable, enable]>
               ap-sniffer-addr: <value of string>
               ap-sniffer-bufsize: <value of integer>
               ap-sniffer-chan: <value of integer>
               ap-sniffer-ctl: <value in [disable, enable]>
               ap-sniffer-data: <value in [disable, enable]>
               ap-sniffer-mgmt-beacon: <value in [disable, enable]>
               ap-sniffer-mgmt-other: <value in [disable, enable]>
               ap-sniffer-mgmt-probe: <value in [disable, enable]>
               auto-power-high: <value of integer>
               auto-power-level: <value in [disable, enable]>
               auto-power-low: <value of integer>
               auto-power-target: <value of string>
               band: <value in [802.11b, 802.11a, 802.11g, ...]>
               band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
               bandwidth-admission-control: <value in [disable, enable]>
               bandwidth-capacity: <value of integer>
               beacon-interval: <value of integer>
               bss-color: <value of integer>
               call-admission-control: <value in [disable, enable]>
               call-capacity: <value of integer>
               channel: <value of string>
               channel-bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
               channel-utilization: <value in [disable, enable]>
               coexistence: <value in [disable, enable]>
               darrp: <value in [disable, enable]>
               drma: <value in [disable, enable]>
               drma-sensitivity: <value in [low, medium, high]>
               dtim: <value of integer>
               frag-threshold: <value of integer>
               iperf-protocol: <value in [udp, tcp]>
               iperf-server-port: <value of integer>
               max-clients: <value of integer>
               max-distance: <value of integer>
               mode: <value in [ap, monitor, sniffer, ...]>
               power-level: <value of integer>
               power-mode: <value in [dBm, percentage]>
               power-value: <value of integer>
               powersave-optimize:
                 - tim
                 - ac-vo
                 - no-obss-scan
                 - no-11b-rate
                 - client-rate-follow
               protection-mode: <value in [rtscts, ctsonly, disable]>
               radio-id: <value of integer>
               rts-threshold: <value of integer>
               sam-bssid: <value of string>
               sam-captive-portal: <value in [disable, enable]>
               sam-password: <value of string>
               sam-report-intv: <value of integer>
               sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
               sam-server: <value of string>
               sam-ssid: <value of string>
               sam-test: <value in [ping, iperf]>
               sam-username: <value of string>
               short-guard-interval: <value in [disable, enable]>
               transmit-optimize:
                 - disable
                 - power-save
                 - aggr-limit
                 - retry-limit
                 - send-bar
               vap-all: <value in [disable, enable, tunnel, ...]>
               vap1: <value of string>
               vap2: <value of string>
               vap3: <value of string>
               vap4: <value of string>
               vap5: <value of string>
               vap6: <value of string>
               vap7: <value of string>
               vap8: <value of string>
               vaps: <value of string>
               wids-profile: <value of string>
               zero-wait-dfs: <value in [disable, enable]>



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



