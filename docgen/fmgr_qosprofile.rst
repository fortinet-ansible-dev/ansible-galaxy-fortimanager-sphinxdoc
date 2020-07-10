:source: fmgr_qosprofile.py

:orphan:

.. _fmgr_qosprofile:

fmgr_qosprofile -- Configure WiFi quality of service (QoS) profiles.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">qosprofile</span> - Configure WiFi quality of service (QoS) profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WMM bandwidth admission control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">burst</span> - Enable/disable client rate burst. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WMM call admission control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">downlink</span> - Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">downlink-sta</span> - Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dscp-wmm-be</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">dscp-wmm-bk</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">dscp-wmm-mapping</span> - Enable/disable Differentiated Services Code Point (DSCP) mapping. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-wmm-vi</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">dscp-wmm-vo</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">name</span> - WiFi QoS profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uplink</span> - Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uplink-sta</span> - Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wmm</span> - Enable/disable WiFi multi-media (WMM) control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wmm-uapsd</span> - Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure WiFi quality of service (QoS) profiles.
      fmgr_qosprofile:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         qosprofile:
            bandwidth-admission-control: <value in [disable, enable]>
            bandwidth-capacity: <value of integer>
            burst: <value in [disable, enable]>
            call-admission-control: <value in [disable, enable]>
            call-capacity: <value of integer>
            comment: <value of string>
            downlink: <value of integer>
            downlink-sta: <value of integer>
            dscp-wmm-be: <value of integer>
            dscp-wmm-bk: <value of integer>
            dscp-wmm-mapping: <value in [disable, enable]>
            dscp-wmm-vi: <value of integer>
            dscp-wmm-vo: <value of integer>
            name: <value of string>
            uplink: <value of integer>
            uplink-sta: <value of integer>
            wmm: <value in [disable, enable]>
            wmm-uapsd: <value in [disable, enable]>



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



