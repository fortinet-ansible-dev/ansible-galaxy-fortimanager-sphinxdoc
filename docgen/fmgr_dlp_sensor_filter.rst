:source: fmgr_dlp_sensor_filter.py

:orphan:

.. _fmgr_dlp_sensor_filter:

fmgr_dlp_sensor_filter -- Set up DLP filters for this sensor.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">sensor</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">dlp_sensor_filter</span> - Set up DLP filters for this sensor. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take with content that this DLP sensor matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log-only, block, exempt, ban, ban-sender, quarantine-ip, quarantine-port, none, allow]</span> </li>
 <li><span class="li-head">archive</span> - Enable/disable DLP archiving. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, summary-only]</span> </li>
 <li><span class="li-head">company-identifier</span> - Enter a company identifier watermark to match. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">expiry</span> - Quarantine duration in days, hours, minutes format (dddhhmm). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">file-size</span> - Match files this size or larger (0 - 4294967295 kbytes). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">file-type</span> - Select the number of a DLP file pattern table to match. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter-by</span> - Select the type of content to match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [credit-card, ssn, regexp, file-type, file-size, fingerprint, watermark, encrypted]</span> </li>
 <li><span class="li-head">fp-sensitivity</span> - Select a DLP file pattern sensitivity to match. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">match-percentage</span> - Percentage of fingerprints in the fingerprint databases designated with the selected fp-sensitivity to match. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Filter name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">proto</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post]</span> </li>
 <li><span class="li-head">regexp</span> - Enter a regular expression to match (max. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">severity</span> - Select the severity or threat level that matches this filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [info, low, medium, high, critical]</span> </li>
 <li><span class="li-head">type</span> - Select whether to check the content of messages (an email message) or files (downloaded files or email attachments). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [file, message]</span> </li>
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
    - name: Set up DLP filters for this sensor.
      fmgr_dlp_sensor_filter:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         sensor: <your own value>
         state: <value in [present, absent]>
         dlp_sensor_filter:
            action: <value in [log-only, block, exempt, ...]>
            archive: <value in [disable, enable, summary-only]>
            company-identifier: <value of string>
            expiry: <value of string>
            file-size: <value of integer>
            file-type: <value of string>
            filter-by: <value in [credit-card, ssn, regexp, ...]>
            fp-sensitivity: <value of string>
            id: <value of integer>
            match-percentage: <value of integer>
            name: <value of string>
            proto:
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
            regexp: <value of string>
            severity: <value in [info, low, medium, ...]>
            type: <value in [file, message]>



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



