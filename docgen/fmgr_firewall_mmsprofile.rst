:source: fmgr_firewall_mmsprofile.py

:orphan:

.. _fmgr_firewall_mmsprofile:

fmgr_firewall_mmsprofile -- Configure MMS profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">firewall_mmsprofile</span> - Configure MMS profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">avnotificationtable</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">bwordtable</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix-range-max</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix-range-min</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix-string</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">carrierendpointbwltable</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extended-utm-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, chunkedbypass, clientcomfort, servercomfort, strict-file, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm1-addr-hdr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mm1-addr-source</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-header, cookie]</span> </li>
 <li><span class="li-head">mm1-convert-hex</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1-outbreak-prevention</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm1-retr-dupe</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1-retrieve-scan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1comfortamount</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm1comfortinterval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm1oversizelimit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, fragmail, splice, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm3-outbreak-prevention</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm3oversizelimit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm4</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, fragmail, splice, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm4-outbreak-prevention</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm4oversizelimit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm7</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, chunkedbypass, clientcomfort, servercomfort, strict-file, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm7-addr-hdr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mm7-addr-source</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-header, cookie]</span> </li>
 <li><span class="li-head">mm7-convert-hex</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm7-outbreak-prevention</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm7comfortamount</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm7comfortinterval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm7oversizelimit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mms-antispam-mass-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-av-block-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-av-oversize-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-av-virus-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-carrier-endpoint-filter-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-checksum-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-checksum-table</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mms-notification-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-web-content-log</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mmsbwordthreshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">notif-msisdn</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">msisdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">threshold</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [flood-thresh-1, flood-thresh-2, flood-thresh-3, dupe-thresh-1, dupe-thresh-2, dupe-thresh-3]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">remove-blocked-const-length</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: Configure MMS profiles.
      fmgr_firewall_mmsprofile:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_mmsprofile:
            avnotificationtable: <value of string>
            bwordtable: <value of string>
            carrier-endpoint-prefix: <value in [disable, enable]>
            carrier-endpoint-prefix-range-max: <value of integer>
            carrier-endpoint-prefix-range-min: <value of integer>
            carrier-endpoint-prefix-string: <value of string>
            carrierendpointbwltable: <value of string>
            comment: <value of string>
            extended-utm-log: <value in [disable, enable]>
            mm1:
              - <value in [avmonitor, block, oversize, ...]>
            mm1-addr-hdr: <value of string>
            mm1-addr-source: <value in [http-header, cookie]>
            mm1-convert-hex: <value in [disable, enable]>
            mm1-outbreak-prevention: <value in [disabled, files, full-archive]>
            mm1-retr-dupe: <value in [disable, enable]>
            mm1-retrieve-scan: <value in [disable, enable]>
            mm1comfortamount: <value of integer>
            mm1comfortinterval: <value of integer>
            mm1oversizelimit: <value of integer>
            mm3:
              - <value in [avmonitor, block, oversize, ...]>
            mm3-outbreak-prevention: <value in [disabled, files, full-archive]>
            mm3oversizelimit: <value of integer>
            mm4:
              - <value in [avmonitor, block, oversize, ...]>
            mm4-outbreak-prevention: <value in [disabled, files, full-archive]>
            mm4oversizelimit: <value of integer>
            mm7:
              - <value in [avmonitor, block, oversize, ...]>
            mm7-addr-hdr: <value of string>
            mm7-addr-source: <value in [http-header, cookie]>
            mm7-convert-hex: <value in [disable, enable]>
            mm7-outbreak-prevention: <value in [disabled, files, full-archive]>
            mm7comfortamount: <value of integer>
            mm7comfortinterval: <value of integer>
            mm7oversizelimit: <value of integer>
            mms-antispam-mass-log: <value in [disable, enable]>
            mms-av-block-log: <value in [disable, enable]>
            mms-av-oversize-log: <value in [disable, enable]>
            mms-av-virus-log: <value in [disable, enable]>
            mms-carrier-endpoint-filter-log: <value in [disable, enable]>
            mms-checksum-log: <value in [disable, enable]>
            mms-checksum-table: <value of string>
            mms-notification-log: <value in [disable, enable]>
            mms-web-content-log: <value in [disable, enable]>
            mmsbwordthreshold: <value of integer>
            name: <value of string>
            notif-msisdn:
              -
                  msisdn: <value of string>
                  threshold:
                    - <value in [flood-thresh-1, flood-thresh-2, flood-thresh-3, ...]>
            remove-blocked-const-length: <value in [disable, enable]>
            replacemsg-group: <value of string>



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



