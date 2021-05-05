:source: fmgr_wtpprofile_lbs.py

:orphan:

.. _fmgr_wtpprofile_lbs:

fmgr_wtpprofile_lbs -- Set various location based service (LBS) options.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wtp-profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wtpprofile_lbs</span> - Set various location based service (LBS) options. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">aeroscout</span> - Enable/disable AeroScout Real Time Location Service (RTLS) support. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-ap-mac</span> - Use BSSID or board MAC address as AP MAC address in the Aeroscout AP message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bssid, board-mac]</span> </li>
 <li><span class="li-head">aeroscout-mmu-report</span> - Enable/disable MU compounded report. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-mu</span> - Enable/disable AeroScout support. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-mu-factor</span> - AeroScout Mobile Unit (MU) mode dilution factor (default = 20). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">aeroscout-mu-timeout</span> - AeroScout MU mode timeout (0 - 65535 sec, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">aeroscout-server-ip</span> - IP address of AeroScout server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">aeroscout-server-port</span> - AeroScout server UDP listening port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ekahau-blink-mode</span> - Enable/disable Ekahua blink mode (also called AiRISTA Flow Blink Mode) to find the location of devices connected to a wireless LAN (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ekahau-tag</span> - WiFi frame MAC address or WiFi Tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">erc-server-ip</span> - IP address of Ekahua RTLS Controller (ERC). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">erc-server-port</span> - Ekahua RTLS Controller (ERC) UDP listening port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence</span> - Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi network (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, enable2, foreign, both]</span> </li>
 <li><span class="li-head">fortipresence-frequency</span> - FortiPresence report transmit frequency (5 - 65535 sec, default = 30). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence-port</span> - FortiPresence server UDP listening port (default = 3000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence-project</span> - FortiPresence project name (max. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortipresence-rogue</span> - Enable/disable FortiPresence finding and reporting rogue APs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortipresence-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">fortipresence-server</span> - FortiPresence server IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortipresence-unassoc</span> - Enable/disable FortiPresence finding and reporting unassociated stations. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">station-locate</span> - Enable/disable client station locating services for all clients, whether associated or not (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Set various location based service (LBS) options.
      fmgr_wtpprofile_lbs:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         wtp-profile: <your own value>
         wtpprofile_lbs:
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
            fortipresence-frequency: <value of integer>
            fortipresence-port: <value of integer>
            fortipresence-project: <value of string>
            fortipresence-rogue: <value in [disable, enable]>
            fortipresence-secret: <value of string>
            fortipresence-server: <value of string>
            fortipresence-unassoc: <value in [disable, enable]>
            station-locate: <value in [disable, enable]>



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



