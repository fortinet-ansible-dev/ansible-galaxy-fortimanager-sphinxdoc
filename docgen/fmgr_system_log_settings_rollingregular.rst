:source: fmgr_system_log_settings_rollingregular.py

:orphan:

.. _fmgr_system_log_settings_rollingregular:

fmgr_system_log_settings_rollingregular -- Log rolling policy for device logs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>system_log_settings_rollingregular</td>
 <td>yes</td>
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
 <li><span class="li-head">system_log_settings_rollingregular</span> - Log rolling policy for device logs. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">days</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [sun, mon, tue, wed, thu, fri, sat]</span> </li>
 <li><span class="li-head">del-files</span> - Enable/disable log file deletion after uploading. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">directory</span> - Upload server directory, for Unix server, use absolute <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">file-size</span> - Roll log files when they reach this size (MB). <span class="li-normal">type: int</span>  <span class="li-normal">default: 200</span> </li>
 <li><span class="li-head">gzip-format</span> - Enable/disable compression of uploaded log files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">hour</span> - Log files rolling schedule (hour). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - Upload server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip2</span> - Upload server IP2 address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip3</span> - Upload server IP3 address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">log-format</span> - Format of uploaded log files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [native, text, csv]</span>  <span class="li-normal">default: native</span> </li>
 <li><span class="li-head">min</span> - Log files rolling schedule (minutes). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">password2</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">password3</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server-type</span> - Upload server type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ftp, sftp, scp]</span>  <span class="li-normal">default: ftp</span> </li>
 <li><span class="li-head">upload</span> - Enable/disable log file uploads. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">upload-hour</span> - Log files upload schedule (hour). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">upload-mode</span> - Upload mode with multiple servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [backup, mirror]</span>  <span class="li-normal">default: backup</span> </li>
 <li><span class="li-head">upload-trigger</span> - Event triggering log files upload. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [on-roll, on-schedule]</span>  <span class="li-normal">default: on-roll</span> </li>
 <li><span class="li-head">username</span> - Upload server login username. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username2</span> - Upload server login username2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username3</span> - Upload server login username3. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">when</span> - Roll log files periodically. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, daily, weekly]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">port</span> - Upload server IP1 port number. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">port2</span> - Upload server IP2 port number. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">port3</span> - Upload server IP3 port number. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
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
    - name: Log rolling policy for device logs.
      fmgr_system_log_settings_rollingregular:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_log_settings_rollingregular:
            days:
              - sun
              - mon
              - tue
              - wed
              - thu
              - fri
              - sat
            del-files: <value in [disable, enable]>
            directory: <value of string>
            file-size: <value of integer>
            gzip-format: <value in [disable, enable]>
            hour: <value of integer>
            ip: <value of string>
            ip2: <value of string>
            ip3: <value of string>
            log-format: <value in [native, text, csv]>
            min: <value of integer>
            password: <value of string>
            password2: <value of string>
            password3: <value of string>
            server-type: <value in [ftp, sftp, scp]>
            upload: <value in [disable, enable]>
            upload-hour: <value of integer>
            upload-mode: <value in [backup, mirror]>
            upload-trigger: <value in [on-roll, on-schedule]>
            username: <value of string>
            username2: <value of string>
            username3: <value of string>
            when: <value in [none, daily, weekly]>
            port: <value of integer>
            port2: <value of integer>
            port3: <value of integer>



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



