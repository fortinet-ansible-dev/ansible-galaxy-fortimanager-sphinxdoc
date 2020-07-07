:source: fmgr_widsprofile.py

:orphan:

.. _fmgr_widsprofile:

fmgr_widsprofile -- Configure wireless intrusion detection system (WIDS) profiles.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">widsprofile</span> - Configure wireless intrusion detection system (WIDS) profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ap-auto-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-bgscan-disable-day</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> </li>
 </ul>
 <li><span class="li-head">ap-bgscan-disable-end</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-bgscan-disable-start</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-bgscan-duration</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-idle</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-period</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-report-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-fgscan-report-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-scan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-scan-passive</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">asleap-attack</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">assoc-flood-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">assoc-flood-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">assoc-frame-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-flood-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auth-flood-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auth-frame-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deauth-broadcast</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">deauth-unknown-src-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-fail-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-fail-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-fail-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-logoff-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-logoff-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-logoff-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-fail-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-pre-fail-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-fail-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-succ-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-pre-succ-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-succ-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-start-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-start-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-start-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-succ-flood</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-succ-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-succ-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">invalid-mac-oui</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">long-duration-attack</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">long-duration-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">null-ssid-probe-resp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sensor-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, foreign, both]</span> </li>
 <li><span class="li-head">spoofed-deauth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">weak-wep-iv</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wireless-bridge</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure wireless intrusion detection system (WIDS) profiles.
      fmgr_widsprofile:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         widsprofile:
            ap-auto-suppress: <value in [disable, enable]>
            ap-bgscan-disable-day:
              - <value in [sunday, monday, tuesday, ...]>
            ap-bgscan-disable-end: <value of string>
            ap-bgscan-disable-start: <value of string>
            ap-bgscan-duration: <value of integer>
            ap-bgscan-idle: <value of integer>
            ap-bgscan-intv: <value of integer>
            ap-bgscan-period: <value of integer>
            ap-bgscan-report-intv: <value of integer>
            ap-fgscan-report-intv: <value of integer>
            ap-scan: <value in [disable, enable]>
            ap-scan-passive: <value in [disable, enable]>
            asleap-attack: <value in [disable, enable]>
            assoc-flood-thresh: <value of integer>
            assoc-flood-time: <value of integer>
            assoc-frame-flood: <value in [disable, enable]>
            auth-flood-thresh: <value of integer>
            auth-flood-time: <value of integer>
            auth-frame-flood: <value in [disable, enable]>
            comment: <value of string>
            deauth-broadcast: <value in [disable, enable]>
            deauth-unknown-src-thresh: <value of integer>
            eapol-fail-flood: <value in [disable, enable]>
            eapol-fail-intv: <value of integer>
            eapol-fail-thresh: <value of integer>
            eapol-logoff-flood: <value in [disable, enable]>
            eapol-logoff-intv: <value of integer>
            eapol-logoff-thresh: <value of integer>
            eapol-pre-fail-flood: <value in [disable, enable]>
            eapol-pre-fail-intv: <value of integer>
            eapol-pre-fail-thresh: <value of integer>
            eapol-pre-succ-flood: <value in [disable, enable]>
            eapol-pre-succ-intv: <value of integer>
            eapol-pre-succ-thresh: <value of integer>
            eapol-start-flood: <value in [disable, enable]>
            eapol-start-intv: <value of integer>
            eapol-start-thresh: <value of integer>
            eapol-succ-flood: <value in [disable, enable]>
            eapol-succ-intv: <value of integer>
            eapol-succ-thresh: <value of integer>
            invalid-mac-oui: <value in [disable, enable]>
            long-duration-attack: <value in [disable, enable]>
            long-duration-thresh: <value of integer>
            name: <value of string>
            null-ssid-probe-resp: <value in [disable, enable]>
            sensor-mode: <value in [disable, foreign, both]>
            spoofed-deauth: <value in [disable, enable]>
            weak-wep-iv: <value in [disable, enable]>
            wireless-bridge: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
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



