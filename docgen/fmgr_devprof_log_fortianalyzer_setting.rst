:source: fmgr_devprof_log_fortianalyzer_setting.py

:orphan:

.. _fmgr_devprof_log_fortianalyzer_setting:

fmgr_devprof_log_fortianalyzer_setting -- Global FortiAnalyzer settings.
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
 <li><span class="li-head">devprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof_log_fortianalyzer_setting</span> - Global FortiAnalyzer settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">certificate</span> - Certificate used to communicate with FortiAnalyzer. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">conn-timeout</span> - FortiAnalyzer connection time-out in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">enc-algorithm</span> - Enable/disable sending FortiAnalyzer log data with SSL encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, high, low, disable, high-medium, low-medium]</span> </li>
 <li><span class="li-head">hmac-algorithm</span> - FortiAnalyzer IPsec tunnel HMAC algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sha256, sha1]</span> </li>
 <li><span class="li-head">ips-archive</span> - Enable/disable IPS packet archive logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">monitor-failure-retry-period</span> - Time between FortiAnalyzer connection retries in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor-keepalive-period</span> - Time between OFTP keepalives in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">reliable</span> - Enable/disable reliable logging to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1, TLSv1-1, TLSv1-2, SSLv3]</span> </li>
 <li><span class="li-head">upload-day</span> - Day of week (month) to upload logs. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">upload-interval</span> - Frequency to upload log files to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [daily, weekly, monthly]</span> </li>
 <li><span class="li-head">upload-option</span> - Enable/disable logging to hard disk and then uploading to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [store-and-upload, realtime, 1-minute, 5-minute]</span> </li>
 <li><span class="li-head">upload-time</span> - Time to upload logs (hh:mm). <span class="li-normal">type: str</span> </li>
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
    - name: Global FortiAnalyzer settings.
      fmgr_devprof_log_fortianalyzer_setting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         devprof_log_fortianalyzer_setting:
            certificate: <value of string>
            conn-timeout: <value of integer>
            enc-algorithm: <value in [default, high, low, ...]>
            hmac-algorithm: <value in [sha256, sha1]>
            ips-archive: <value in [disable, enable]>
            monitor-failure-retry-period: <value of integer>
            monitor-keepalive-period: <value of integer>
            reliable: <value in [disable, enable]>
            ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
            upload-day: <value of string>
            upload-interval: <value in [daily, weekly, monthly]>
            upload-option: <value in [store-and-upload, realtime, 1-minute, ...]>
            upload-time: <value of string>



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



