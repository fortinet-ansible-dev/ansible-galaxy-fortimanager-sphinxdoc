:source: fmgr_firewall_gtp.py

:orphan:

.. _fmgr_firewall_gtp:

fmgr_firewall_gtp -- Configure GTP.
+++++++++++++++++++++++++++++++++++

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
 <td>firewall_gtp</td>
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
 <li><span class="li-head">firewall_gtp</span> - Configure GTP. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">addr-notify</span> - overbilling notify address <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">apn</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">apnmember</span> - APN member. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">selection-mode</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ms, net, vrf]</span> </li>
 </ul>
 <li><span class="li-head">apn-filter</span> - apn filter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">authorized-ggsns</span> - Authorized GGSN group <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">authorized-sgsns</span> - Authorized SGSN group <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">context-id</span> - Overbilling context. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">control-plane-message-rate-limit</span> - control plane message rate limit <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">default-apn-action</span> - default apn action <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">default-imsi-action</span> - default imsi action <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">default-ip-action</span> - default action for encapsulated IP traffic <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">default-noip-action</span> - default action for encapsulated non-IP traffic <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">default-policy-action</span> - default advanced policy action <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">denied-log</span> - log denied <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">echo-request-interval</span> - echo request interval (in seconds) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">extension-log</span> - log in extension format <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">forwarded-log</span> - log forwarded <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">global-tunnel-limit</span> - Global tunnel limit. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gtp-in-gtp</span> - gtp in gtp <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">gtpu-denied-log</span> - Enable/disable logging of denied GTP-U packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gtpu-forwarded-log</span> - Enable/disable logging of forwarded GTP-U packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gtpu-log-freq</span> - Logging of frequency of GTP-U packets. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">half-close-timeout</span> - Half-close tunnel timeout (in seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">half-open-timeout</span> - Half-open tunnel timeout (in seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">handover-group</span> - Handover SGSN group <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ie-remove-policy</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">remove-ies</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [apn-restriction, rat-type, rai, uli, imei]</span> </li>
 <li><span class="li-head">sgsn-addr</span> - SGSN address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sgsn-addr6</span> - SGSN IPv6 address name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ie-remover</span> - IE removal policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ie-white-list-v0v1</span> - IE white list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ie-white-list-v2</span> - IE white list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">imsi</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">apnmember</span> - APN member. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mcc-mnc</span> - MCC MNC. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msisdn-prefix</span> - MSISDN prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">selection-mode</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ms, net, vrf]</span> </li>
 </ul>
 <li><span class="li-head">imsi-filter</span> - imsi filter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">interface-notify</span> - overbilling interface <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">invalid-reserved-field</span> - Invalid reserved field in GTP header <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">invalid-sgsns-to-log</span> - Invalid SGSN group to be logged <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-filter</span> - IP filter for encapsulted traffic <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip-policy</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr6</span> - Destination IPv6 address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr6</span> - Source IPv6 address name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log-freq</span> - Logging of frequency of GTP-C packets. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log-gtpu-limit</span> - the user data log limit (0-512 bytes) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log-imsi-prefix</span> - IMSI prefix for selective logging. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">log-msisdn-prefix</span> - the msisdn prefix for selective logging <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-message-length</span> - max message length <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">message-filter-v0v1</span> - Message filter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message-filter-v2</span> - Message filter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">min-message-length</span> - min message length <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">miss-must-ie</span> - Missing mandatory information element <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">monitor-mode</span> - GTP monitor mode <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vdom]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">noip-filter</span> - non-IP filter for encapsulted traffic <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">noip-policy</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">end</span> - End of protocol range (0 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start</span> - Start of protocol range (0 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">type</span> - Protocol field type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [etsi, ietf]</span> </li>
 </ul>
 <li><span class="li-head">out-of-state-ie</span> - Out of state information element. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">out-of-state-message</span> - Out of state GTP message <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">per-apn-shaper</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">apn</span> - APN name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-limit</span> - Rate limit (packets/s) for create PDP context request. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">version</span> - GTP version number: 0 or 1. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">policy</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">apn-sel-mode</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ms, net, vrf]</span> </li>
 <li><span class="li-head">apnmember</span> - APN member. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">imei</span> - IMEI(SV) pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">imsi</span> - IMSI prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-apn-restriction</span> - Maximum APN restriction value. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [all, public-1, public-2, private-1, private-2]</span> </li>
 <li><span class="li-head">messages</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [create-req, create-res, update-req, update-res]</span> </li>
 <li><span class="li-head">msisdn</span> - MSISDN prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rai</span> - RAI pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rat-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot]</span> </li>
 <li><span class="li-head">uli</span> - ULI pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">imsi-prefix</span> - IMSI prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msisdn-prefix</span> - MSISDN prefix. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">policy-filter</span> - Advanced policy filter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port-notify</span> - overbilling notify port <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-limit-mode</span> - GTP rate limit mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [per-profile, per-stream, per-apn]</span> </li>
 <li><span class="li-head">rate-limited-log</span> - log rate limited <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-sampling-interval</span> - rate sampling interval (1-3600 seconds) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">remove-if-echo-expires</span> - remove if echo response expires <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">remove-if-recovery-differ</span> - remove upon different Recovery IE <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">reserved-ie</span> - reserved information element <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">send-delete-when-timeout</span> - send DELETE request to path endpoints when GTPv0/v1 tunnel timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">send-delete-when-timeout-v2</span> - send DELETE request to path endpoints when GTPv2 tunnel timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spoof-src-addr</span> - Spoofed source address for Mobile Station. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">state-invalid-log</span> - log state invalid <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">traffic-count-log</span> - log tunnel traffic counter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tunnel-limit</span> - tunnel limit <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tunnel-limit-log</span> - tunnel limit <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tunnel-timeout</span> - Established tunnel timeout (in seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">unknown-version-action</span> - action for unknown gtp version <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">user-plane-message-rate-limit</span> - user plane message rate limit <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">warning-threshold</span> - Warning threshold for rate limiting (0 - 99 percent). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">policy-v2</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">apn-sel-mode</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ms, net, vrf]</span> </li>
 <li><span class="li-head">apnmember</span> - APN member. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">imsi-prefix</span> - IMSI prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-apn-restriction</span> - Maximum APN restriction value. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [all, public-1, public-2, private-1, private-2]</span> </li>
 <li><span class="li-head">mei</span> - MEI pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">messages</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [create-ses-req, create-ses-res, modify-bearer-req, modify-bearer-res]</span> </li>
 <li><span class="li-head">msisdn-prefix</span> - MSISDN prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rat-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, any, utran, geran, wlan, gan, hspa, eutran, virtual, nbiot, ltem, nr]</span> </li>
 <li><span class="li-head">uli</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">sub-second-interval</span> - Sub-second interval (0. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [0.1, 0.25, 0.5]</span> </li>
 <li><span class="li-head">sub-second-sampling</span> - Enable/disable sub-second sampling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">authorized-ggsns6</span> - Authorized GGSN/PGW IPv6 group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">authorized-sgsns6</span> - Authorized SGSN/SGW IPv6 group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">handover-group6</span> - Handover SGSN/SGW IPv6 group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ie-allow-list-v0v1</span> - IE allow list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ie-allow-list-v2</span> - IE allow list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ie-validation</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">apn-restriction</span> - Validate APN restriction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charging-ID</span> - Validate charging ID. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charging-gateway-addr</span> - Validate charging gateway address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">end-user-addr</span> - Validate end user address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gsn-addr</span> - Validate GSN address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">imei</span> - Validate IMEI(SV). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">imsi</span> - Validate IMSI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm-context</span> - Validate MM context. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ms-tzone</span> - Validate MS time zone. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ms-validated</span> - Validate MS validated. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">msisdn</span> - Validate MSISDN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nsapi</span> - Validate NSAPI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdp-context</span> - Validate PDP context. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">qos-profile</span> - Validate Quality of Service(QoS) profile. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rai</span> - Validate RAI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rat-type</span> - Validate RAT type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">reordering-required</span> - Validate re-ordering required. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">selection-mode</span> - Validate selection mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uli</span> - Validate user location information. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">invalid-sgsns6-to-log</span> - Invalid SGSN IPv6 group to be logged. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message-rate-limit</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">create-aa-pdp-request</span> - Rate limit for create AA PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-aa-pdp-response</span> - Rate limit for create AA PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-mbms-request</span> - Rate limit for create MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-mbms-response</span> - Rate limit for create MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-pdp-request</span> - Rate limit for create PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-pdp-response</span> - Rate limit for create PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-aa-pdp-request</span> - Rate limit for delete AA PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-aa-pdp-response</span> - Rate limit for delete AA PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-mbms-request</span> - Rate limit for delete MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-mbms-response</span> - Rate limit for delete MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-request</span> - Rate limit for delete PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-response</span> - Rate limit for delete PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-reponse</span> - Rate limit for echo response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-request</span> - Rate limit for echo requests (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">error-indication</span> - Rate limit for error indication (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">failure-report-request</span> - Rate limit for failure report request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">failure-report-response</span> - Rate limit for failure report response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-reloc-complete-ack</span> - Rate limit for forward relocation complete acknowledge (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-complete</span> - Rate limit for forward relocation complete (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-request</span> - Rate limit for forward relocation request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-response</span> - Rate limit for forward relocation response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-srns-context</span> - Rate limit for forward SRNS context (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-srns-context-ack</span> - Rate limit for forward SRNS context acknowledge (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">g-pdu</span> - Rate limit for G-PDU (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">identification-request</span> - Rate limit for identification request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">identification-response</span> - Rate limit for identification response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-de-reg-request</span> - Rate limit for MBMS de-registration request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-de-reg-response</span> - Rate limit for MBMS de-registration response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-rej-request</span> - Rate limit for MBMS notification reject request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-rej-response</span> - Rate limit for MBMS notification reject response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-request</span> - Rate limit for MBMS notification request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-response</span> - Rate limit for MBMS notification response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-reg-request</span> - Rate limit for MBMS registration request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-reg-response</span> - Rate limit for MBMS registration response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-start-request</span> - Rate limit for MBMS session start request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-start-response</span> - Rate limit for MBMS session start response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-stop-request</span> - Rate limit for MBMS session stop request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-stop-response</span> - Rate limit for MBMS session stop response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">note-ms-request</span> - Rate limit for note MS GPRS present request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">note-ms-response</span> - Rate limit for note MS GPRS present response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-rej-request</span> - Rate limit for PDU notify reject request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-rej-response</span> - Rate limit for PDU notify reject response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-request</span> - Rate limit for PDU notify request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-response</span> - Rate limit for PDU notify response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ran-info</span> - Rate limit for RAN information relay (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">relocation-cancel-request</span> - Rate limit for relocation cancel request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">relocation-cancel-response</span> - Rate limit for relocation cancel response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">send-route-request</span> - Rate limit for send routing information for GPRS request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">send-route-response</span> - Rate limit for send routing information for GPRS response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-ack</span> - Rate limit for SGSN context acknowledgement (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-request</span> - Rate limit for SGSN context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-response</span> - Rate limit for SGSN context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">support-ext-hdr-notify</span> - Rate limit for support extension headers notification (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-mbms-request</span> - Rate limit for update MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-mbms-response</span> - Rate limit for update MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-pdp-request</span> - Rate limit for update PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-pdp-response</span> - Rate limit for update PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">version-not-support</span> - Rate limit for version not supported (packets per second). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">message-rate-limit-v0</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">create-pdp-request</span> - Rate limit (packets/s) for create PDP context request. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-request</span> - Rate limit (packets/s) for delete PDP context request. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-request</span> - Rate limit (packets/s) for echo request. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">message-rate-limit-v1</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">create-pdp-request</span> - Rate limit (packets/s) for create PDP context request. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-request</span> - Rate limit (packets/s) for delete PDP context request. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-request</span> - Rate limit (packets/s) for echo request. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">message-rate-limit-v2</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">create-session-request</span> - Rate limit (packets/s) for create session request. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-session-request</span> - Rate limit (packets/s) for delete session request. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-request</span> - Rate limit (packets/s) for echo request. <span class="li-normal">type: int</span> </li>
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
    - name: Configure GTP.
      fmgr_firewall_gtp:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_gtp:
            addr-notify: <value of string>
            apn:
              -
                  action: <value in [allow, deny]>
                  apnmember: <value of string>
                  id: <value of integer>
                  selection-mode:
                    - ms
                    - net
                    - vrf
            apn-filter: <value in [disable, enable]>
            authorized-ggsns: <value of string>
            authorized-sgsns: <value of string>
            comment: <value of string>
            context-id: <value of integer>
            control-plane-message-rate-limit: <value of integer>
            default-apn-action: <value in [allow, deny]>
            default-imsi-action: <value in [allow, deny]>
            default-ip-action: <value in [allow, deny]>
            default-noip-action: <value in [allow, deny]>
            default-policy-action: <value in [allow, deny]>
            denied-log: <value in [disable, enable]>
            echo-request-interval: <value of integer>
            extension-log: <value in [disable, enable]>
            forwarded-log: <value in [disable, enable]>
            global-tunnel-limit: <value of string>
            gtp-in-gtp: <value in [allow, deny]>
            gtpu-denied-log: <value in [disable, enable]>
            gtpu-forwarded-log: <value in [disable, enable]>
            gtpu-log-freq: <value of integer>
            half-close-timeout: <value of integer>
            half-open-timeout: <value of integer>
            handover-group: <value of string>
            ie-remove-policy:
              -
                  id: <value of integer>
                  remove-ies:
                    - apn-restriction
                    - rat-type
                    - rai
                    - uli
                    - imei
                  sgsn-addr: <value of string>
                  sgsn-addr6: <value of string>
            ie-remover: <value in [disable, enable]>
            ie-white-list-v0v1: <value of string>
            ie-white-list-v2: <value of string>
            imsi:
              -
                  action: <value in [allow, deny]>
                  apnmember: <value of string>
                  id: <value of integer>
                  mcc-mnc: <value of string>
                  msisdn-prefix: <value of string>
                  selection-mode:
                    - ms
                    - net
                    - vrf
            imsi-filter: <value in [disable, enable]>
            interface-notify: <value of string>
            invalid-reserved-field: <value in [allow, deny]>
            invalid-sgsns-to-log: <value of string>
            ip-filter: <value in [disable, enable]>
            ip-policy:
              -
                  action: <value in [allow, deny]>
                  dstaddr: <value of string>
                  id: <value of integer>
                  srcaddr: <value of string>
                  dstaddr6: <value of string>
                  srcaddr6: <value of string>
            log-freq: <value of integer>
            log-gtpu-limit: <value of integer>
            log-imsi-prefix: <value of string>
            log-msisdn-prefix: <value of string>
            max-message-length: <value of integer>
            message-filter-v0v1: <value of string>
            message-filter-v2: <value of string>
            min-message-length: <value of integer>
            miss-must-ie: <value in [allow, deny]>
            monitor-mode: <value in [disable, enable, vdom]>
            name: <value of string>
            noip-filter: <value in [disable, enable]>
            noip-policy:
              -
                  action: <value in [allow, deny]>
                  end: <value of integer>
                  id: <value of integer>
                  start: <value of integer>
                  type: <value in [etsi, ietf]>
            out-of-state-ie: <value in [allow, deny]>
            out-of-state-message: <value in [allow, deny]>
            per-apn-shaper:
              -
                  apn: <value of string>
                  id: <value of integer>
                  rate-limit: <value of integer>
                  version: <value of integer>
            policy:
              -
                  action: <value in [allow, deny]>
                  apn-sel-mode:
                    - ms
                    - net
                    - vrf
                  apnmember: <value of string>
                  id: <value of integer>
                  imei: <value of string>
                  imsi: <value of string>
                  max-apn-restriction: <value in [all, public-1, public-2, ...]>
                  messages:
                    - create-req
                    - create-res
                    - update-req
                    - update-res
                  msisdn: <value of string>
                  rai: <value of string>
                  rat-type:
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                  uli: <value of string>
                  imsi-prefix: <value of string>
                  msisdn-prefix: <value of string>
            policy-filter: <value in [disable, enable]>
            port-notify: <value of integer>
            rate-limit-mode: <value in [per-profile, per-stream, per-apn]>
            rate-limited-log: <value in [disable, enable]>
            rate-sampling-interval: <value of integer>
            remove-if-echo-expires: <value in [disable, enable]>
            remove-if-recovery-differ: <value in [disable, enable]>
            reserved-ie: <value in [allow, deny]>
            send-delete-when-timeout: <value in [disable, enable]>
            send-delete-when-timeout-v2: <value in [disable, enable]>
            spoof-src-addr: <value in [allow, deny]>
            state-invalid-log: <value in [disable, enable]>
            traffic-count-log: <value in [disable, enable]>
            tunnel-limit: <value of integer>
            tunnel-limit-log: <value in [disable, enable]>
            tunnel-timeout: <value of integer>
            unknown-version-action: <value in [allow, deny]>
            user-plane-message-rate-limit: <value of integer>
            warning-threshold: <value of integer>
            policy-v2:
              -
                  action: <value in [deny, allow]>
                  apn-sel-mode:
                    - ms
                    - net
                    - vrf
                  apnmember: <value of string>
                  id: <value of integer>
                  imsi-prefix: <value of string>
                  max-apn-restriction: <value in [all, public-1, public-2, ...]>
                  mei: <value of string>
                  messages:
                    - create-ses-req
                    - create-ses-res
                    - modify-bearer-req
                    - modify-bearer-res
                  msisdn-prefix: <value of string>
                  rat-type:
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - any
                    - utran
                    - geran
                    - wlan
                    - gan
                    - hspa
                    - eutran
                    - virtual
                    - nbiot
                    - ltem
                    - nr
                  uli: <value of string>
            sub-second-interval: <value in [0.1, 0.25, 0.5]>
            sub-second-sampling: <value in [disable, enable]>
            authorized-ggsns6: <value of string>
            authorized-sgsns6: <value of string>
            handover-group6: <value of string>
            ie-allow-list-v0v1: <value of string>
            ie-allow-list-v2: <value of string>
            ie-validation:
               apn-restriction: <value in [disable, enable]>
               charging-ID: <value in [disable, enable]>
               charging-gateway-addr: <value in [disable, enable]>
               end-user-addr: <value in [disable, enable]>
               gsn-addr: <value in [disable, enable]>
               imei: <value in [disable, enable]>
               imsi: <value in [disable, enable]>
               mm-context: <value in [disable, enable]>
               ms-tzone: <value in [disable, enable]>
               ms-validated: <value in [disable, enable]>
               msisdn: <value in [disable, enable]>
               nsapi: <value in [disable, enable]>
               pdp-context: <value in [disable, enable]>
               qos-profile: <value in [disable, enable]>
               rai: <value in [disable, enable]>
               rat-type: <value in [disable, enable]>
               reordering-required: <value in [disable, enable]>
               selection-mode: <value in [disable, enable]>
               uli: <value in [disable, enable]>
            invalid-sgsns6-to-log: <value of string>
            message-rate-limit:
               create-aa-pdp-request: <value of integer>
               create-aa-pdp-response: <value of integer>
               create-mbms-request: <value of integer>
               create-mbms-response: <value of integer>
               create-pdp-request: <value of integer>
               create-pdp-response: <value of integer>
               delete-aa-pdp-request: <value of integer>
               delete-aa-pdp-response: <value of integer>
               delete-mbms-request: <value of integer>
               delete-mbms-response: <value of integer>
               delete-pdp-request: <value of integer>
               delete-pdp-response: <value of integer>
               echo-reponse: <value of integer>
               echo-request: <value of integer>
               error-indication: <value of integer>
               failure-report-request: <value of integer>
               failure-report-response: <value of integer>
               fwd-reloc-complete-ack: <value of integer>
               fwd-relocation-complete: <value of integer>
               fwd-relocation-request: <value of integer>
               fwd-relocation-response: <value of integer>
               fwd-srns-context: <value of integer>
               fwd-srns-context-ack: <value of integer>
               g-pdu: <value of integer>
               identification-request: <value of integer>
               identification-response: <value of integer>
               mbms-de-reg-request: <value of integer>
               mbms-de-reg-response: <value of integer>
               mbms-notify-rej-request: <value of integer>
               mbms-notify-rej-response: <value of integer>
               mbms-notify-request: <value of integer>
               mbms-notify-response: <value of integer>
               mbms-reg-request: <value of integer>
               mbms-reg-response: <value of integer>
               mbms-ses-start-request: <value of integer>
               mbms-ses-start-response: <value of integer>
               mbms-ses-stop-request: <value of integer>
               mbms-ses-stop-response: <value of integer>
               note-ms-request: <value of integer>
               note-ms-response: <value of integer>
               pdu-notify-rej-request: <value of integer>
               pdu-notify-rej-response: <value of integer>
               pdu-notify-request: <value of integer>
               pdu-notify-response: <value of integer>
               ran-info: <value of integer>
               relocation-cancel-request: <value of integer>
               relocation-cancel-response: <value of integer>
               send-route-request: <value of integer>
               send-route-response: <value of integer>
               sgsn-context-ack: <value of integer>
               sgsn-context-request: <value of integer>
               sgsn-context-response: <value of integer>
               support-ext-hdr-notify: <value of integer>
               update-mbms-request: <value of integer>
               update-mbms-response: <value of integer>
               update-pdp-request: <value of integer>
               update-pdp-response: <value of integer>
               version-not-support: <value of integer>
            message-rate-limit-v0:
               create-pdp-request: <value of integer>
               delete-pdp-request: <value of integer>
               echo-request: <value of integer>
            message-rate-limit-v1:
               create-pdp-request: <value of integer>
               delete-pdp-request: <value of integer>
               echo-request: <value of integer>
            message-rate-limit-v2:
               create-session-request: <value of integer>
               delete-session-request: <value of integer>
               echo-request: <value of integer>



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



