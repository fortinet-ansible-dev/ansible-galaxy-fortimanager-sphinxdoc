:source: fmgr_system_locallog_disk_setting.py

:orphan:

.. _fmgr_system_locallog_disk_setting:

fmgr_system_locallog_disk_setting -- Settings for local disk logging.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">system_locallog_disk_setting</span> - Settings for local disk logging. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">diskfull</span> - Policy to apply when disk is full. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [overwrite, nolog]</span>  <span class="li-normal">default: overwrite</span> </li>
 <li><span class="li-head">log-disk-full-percentage</span> - Consider log disk as full at this usage percentage. <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
 <li><span class="li-head">max-log-file-size</span> - Maximum log file size before rolling. <span class="li-normal">type: int</span>  <span class="li-normal">default: 100</span> </li>
 <li><span class="li-head">roll-day</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> </li>
 <li><span class="li-head">roll-schedule</span> - Frequency to check log file for rolling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, daily, weekly]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">roll-time</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server-type</span> - Server type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [FTP, SFTP, SCP]</span>  <span class="li-normal">default: FTP</span> </li>
 <li><span class="li-head">severity</span> - Least severity level to log. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warning, notification, information, debug]</span>  <span class="li-normal">default: information</span> </li>
 <li><span class="li-head">status</span> - Enable/disable local disk log. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">upload</span> - Upload log file when rolling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">upload-delete-files</span> - Delete log files after uploading (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">upload-time</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">uploaddir</span> - Log file upload remote directory. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uploadip</span> - IP address of log uploading server. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">uploadpass</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">uploadport</span> - Server port (0 = default protocol port). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">uploadsched</span> - Scheduled upload (disable = upload when rolling). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">uploadtype</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [event]</span> </li>
 <li><span class="li-head">uploaduser</span> - User account in upload server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uploadzip</span> - Compress upload logs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
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
    - name: Settings for local disk logging.
      fmgr_system_locallog_disk_setting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_locallog_disk_setting:
            diskfull: <value in [overwrite, nolog]>
            log-disk-full-percentage: <value of integer>
            max-log-file-size: <value of integer>
            roll-day:
              - sunday
              - monday
              - tuesday
              - wednesday
              - thursday
              - friday
              - saturday
            roll-schedule: <value in [none, daily, weekly]>
            roll-time: <value of string>
            server-type: <value in [FTP, SFTP, SCP]>
            severity: <value in [emergency, alert, critical, ...]>
            status: <value in [disable, enable]>
            upload: <value in [disable, enable]>
            upload-delete-files: <value in [disable, enable]>
            upload-time: <value of string>
            uploaddir: <value of string>
            uploadip: <value of string>
            uploadpass: <value of string>
            uploadport: <value of integer>
            uploadsched: <value in [disable, enable]>
            uploadtype:
              - event
            uploaduser: <value of string>
            uploadzip: <value in [disable, enable]>



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



