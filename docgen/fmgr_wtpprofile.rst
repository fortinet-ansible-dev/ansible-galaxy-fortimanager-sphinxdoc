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



Parameters
----------

.. raw:: html

 <ul>
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
 <li><span class="li-head">ap-country</span> - Country in which this WTP, FortiAP or AP will operate (default = NA, automatically use the country configured for the current VDOM). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [AL, DZ, AR, AM, AU, AT, AZ, BH, BD, BY, BE, BZ, BO, BA, BR, BN, BG, CA, CL, CN, CO, CR, HR, CY, CZ, DK, DO, EC, EG, SV, EE, FI, FR, GE, DE, GR, GT, HN, HK, HU, IS, IN, ID, IR, IE, IL, IT, JM, JP, JO, KZ, KE, KP, KR, KW, LV, LB, LI, LT, LU, MO, MK, MY, MT, MX, MC, MA, NP, NL, AN, NZ, NO, OM, PK, PA, PG, PE, PH, PL, PT, PR, QA, RO, RU, SA, SG, SK, SI, ZA, ES, LK, SE, CH, SY, TW, TH, TT, TN, TR, AE, UA, GB, US, PS, UY, UZ, VE, VN, YE, ZW, NA, KH, TZ, SD, AO, RW, MZ, RS, ME, BB, GD, GL, GU, PY, HT, AW, MM, ZB]</span> </li>
 <li><span class="li-head">ble-profile</span> - Bluetooth Low Energy profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">control-message-offload</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health]</span> </li>
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
 <li><span class="li-head">poe-mode</span> - Set the WTP, FortiAP, or APs PoE mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, 8023af, 8023at, power-adapter]</span> </li>
 <li><span class="li-head">split-tunneling-acl</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dest-ip</span> - Destination IP and mask for the split-tunneling subnet. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">split-tunneling-acl-local-ap-subnet</span> - Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">split-tunneling-acl-path</span> - Split tunneling ACL path is local/tunnel. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tunnel, local]</span> </li>
 <li><span class="li-head">tun-mtu-downlink</span> - Downlink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tun-mtu-uplink</span> - Uplink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wan-port-mode</span> - Enable/disable using a WAN port as a LAN port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [wan-lan, wan-only]</span> </li>
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



