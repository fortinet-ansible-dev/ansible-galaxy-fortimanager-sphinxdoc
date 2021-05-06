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



