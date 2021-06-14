:source: fmgr_devprof_log_fortianalyzercloud_setting.py

:orphan:

.. _fmgr_devprof_log_fortianalyzercloud_setting:

fmgr_devprof_log_fortianalyzercloud_setting -- Global FortiAnalyzer Cloud settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>devprof_log_fortianalyzercloud_setting</td>
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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof_log_fortianalyzercloud_setting</span> - Global FortiAnalyzer Cloud settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">__change_ip</span> - Hidden attribute. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">access-config</span> - Enable/disable FortiAnalyzer access to configuration and data. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">certificate</span> - Certificate used to communicate with FortiAnalyzer. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">conn-timeout</span> - FortiAnalyzer connection time-out in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">enc-algorithm</span> - Configure the level of SSL protection for secure communication with FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, high-medium]</span> </li>
 <li><span class="li-head">hmac-algorithm</span> - FortiAnalyzer IPsec tunnel HMAC algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sha256, sha1]</span> </li>
 <li><span class="li-head">ips-archive</span> - Enable/disable IPS packet archive logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">monitor-failure-retry-period</span> - Time between FortiAnalyzer connection retries in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor-keepalive-period</span> - Time between OFTP keepalives in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source-ip</span> - Source IPv4 or IPv6 address used to communicate with FortiAnalyzer. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1-1, TLSv1-2, SSLv3, TLSv1]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable logging to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">upload-day</span> - Day of week (month) to upload logs. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">upload-interval</span> - Frequency to upload log files to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [daily, weekly, monthly]</span> </li>
 <li><span class="li-head">upload-option</span> - Enable/disable logging to hard disk and then uploading to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [store-and-upload, realtime, 1-minute, 5-minute]</span> </li>
 <li><span class="li-head">upload-time</span> - Time to upload logs (hh:mm). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-log-rate</span> - FortiAnalyzer maximum log rate in MBps (0 = unlimited). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority</span> - Set log transmission priority. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, default]</span> </li>
 <li><span class="li-head">interface</span> - Specify outgoing interface to reach server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface-select-method</span> - Specify how to select outgoing interface to reach server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span> </li>
 <li><span class="li-head">preshared-key</span> - Preshared-key used for auto-authorization on FortiAnalyzer. <span class="li-normal">type: str</span> </li>
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
    - name: Global FortiAnalyzer Cloud settings.
      fmgr_devprof_log_fortianalyzercloud_setting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         devprof_log_fortianalyzercloud_setting:
            __change_ip: <value of integer>
            access-config: <value in [disable, enable]>
            certificate: <value of string>
            conn-timeout: <value of integer>
            enc-algorithm: <value in [high, low, high-medium]>
            hmac-algorithm: <value in [sha256, sha1]>
            ips-archive: <value in [disable, enable]>
            monitor-failure-retry-period: <value of integer>
            monitor-keepalive-period: <value of integer>
            source-ip: <value of string>
            ssl-min-proto-version: <value in [default, TLSv1-1, TLSv1-2, ...]>
            status: <value in [disable, enable]>
            upload-day: <value of string>
            upload-interval: <value in [daily, weekly, monthly]>
            upload-option: <value in [store-and-upload, realtime, 1-minute, ...]>
            upload-time: <value of string>
            max-log-rate: <value of integer>
            priority: <value in [low, default]>
            interface: <value of string>
            interface-select-method: <value in [auto, sdwan, specify]>
            preshared-key: <value of string>



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



