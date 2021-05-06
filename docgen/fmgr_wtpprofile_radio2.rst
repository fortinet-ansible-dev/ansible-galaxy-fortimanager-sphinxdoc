:source: fmgr_wtpprofile_radio2.py

:orphan:

.. _fmgr_wtpprofile_radio2:

fmgr_wtpprofile_radio2 -- Configuration options for radio 2.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">proposed_method</span> - The overridden method of the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wtp-profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wtpprofile_radio2</span> - Configuration options for radio 2. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">amsdu</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-handoff</span> - Enable/disable AP handoff of clients to other APs (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-addr</span> - MAC address to monitor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-sniffer-bufsize</span> - Sniffer buffer size (1 - 32 MB, default = 16). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-chan</span> - Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-ctl</span> - Enable/disable sniffer on WiFi control frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-data</span> - Enable/disable sniffer on WiFi data frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-beacon</span> - Enable/disable sniffer on WiFi management Beacon frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-other</span> - Enable/disable sniffer on WiFi management other frames  (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-probe</span> - Enable/disable sniffer on WiFi management probe frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-high</span> - Automatic transmit power high limit in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-level</span> - Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-low</span> - Automatic transmission power low limit in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">band</span> - WiFi band that Radio 2 operates on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.11b, 802.11a, 802.11g, 802.11n, 802.11ac, 802.11n-5G, 802.11g-only, 802.11n-only, 802.11n,g-only, 802.11ac-only, 802.11ac,n-only, 802.11n-5G-only]</span> </li>
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">beacon-interval</span> - Beacon interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">channel</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">channel-bonding</span> - Channel bandwidth: 80, 40, or 20MHz. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, 80MHz, 40MHz, 20MHz]</span> </li>
 <li><span class="li-head">channel-utilization</span> - Enable/disable measuring channel utilization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">coexistence</span> - Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">darrp</span> - Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dtim</span> - DTIM interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frag-threshold</span> - Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frequency-handoff</span> - Enable/disable frequency handoff of clients to other channels (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) or WiFi clients supported by the radio. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-distance</span> - Maximum expected distance between the AP and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - Mode of radio 2. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, ap, monitor, sniffer]</span> </li>
 <li><span class="li-head">power-level</span> - Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">powersave-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tim, ac-vo, no-obss-scan, no-11b-rate, client-rate-follow]</span> </li>
 <li><span class="li-head">protection-mode</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rtscts, ctsonly, disable]</span> </li>
 <li><span class="li-head">radio-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rts-threshold</span> - Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">short-guard-interval</span> - Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spectrum-analysis</span> - Enable/disable spectrum analysis to find interference that would negatively impact wireless performance. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">transmit-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [disable, power-save, aggr-limit, retry-limit, send-bar]</span> </li>
 <li><span class="li-head">vap-all</span> - Enable/disable the automatic inheritance of all Virtual Access Points (VAPs) (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vaps</span> - Manually selected list of Virtual Access Points (VAPs). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wids-profile</span> - Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. <span class="li-normal">type: str</span> </li>
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
    - name: Configuration options for radio 2.
      fmgr_wtpprofile_radio2:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         wtp-profile: <your own value>
         wtpprofile_radio2:
            amsdu: <value in [disable, enable]>
            ap-handoff: <value in [disable, enable]>
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
            band: <value in [802.11b, 802.11a, 802.11g, ...]>
            bandwidth-admission-control: <value in [disable, enable]>
            bandwidth-capacity: <value of integer>
            beacon-interval: <value of integer>
            call-admission-control: <value in [disable, enable]>
            call-capacity: <value of integer>
            channel: <value of string>
            channel-bonding: <value in [disable, enable, 80MHz, ...]>
            channel-utilization: <value in [disable, enable]>
            coexistence: <value in [disable, enable]>
            darrp: <value in [disable, enable]>
            dtim: <value of integer>
            frag-threshold: <value of integer>
            frequency-handoff: <value in [disable, enable]>
            max-clients: <value of integer>
            max-distance: <value of integer>
            mode: <value in [disabled, ap, monitor, ...]>
            power-level: <value of integer>
            powersave-optimize:
              - tim
              - ac-vo
              - no-obss-scan
              - no-11b-rate
              - client-rate-follow
            protection-mode: <value in [rtscts, ctsonly, disable]>
            radio-id: <value of integer>
            rts-threshold: <value of integer>
            short-guard-interval: <value in [disable, enable]>
            spectrum-analysis: <value in [disable, enable]>
            transmit-optimize:
              - disable
              - power-save
              - aggr-limit
              - retry-limit
              - send-bar
            vap-all: <value in [disable, enable]>
            vaps: <value of string>
            wids-profile: <value of string>



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



