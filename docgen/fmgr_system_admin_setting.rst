:source: fmgr_system_admin_setting.py

:orphan:

.. _fmgr_system_admin_setting:

fmgr_system_admin_setting -- Admin setting.
+++++++++++++++++++++++++++++++++++++++++++

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
 <td>system_admin_setting</td>
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
 <li><span class="li-head">system_admin_setting</span> - Admin setting. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">access-banner</span> - Enable/disable access banner. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">admin-https-redirect</span> - Enable/disable redirection of HTTP admin traffic to HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">admin-login-max</span> - Maximum number admin users logged in at one time (1 - 256). <span class="li-normal">type: int</span>  <span class="li-normal">default: 256</span> </li>
 <li><span class="li-head">admin_server_cert</span> - HTTPS & Web Service server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">default: server.crt</span> </li>
 <li><span class="li-head">allow_register</span> - Enable/disable allowance of register an unregistered device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">auto-update</span> - Enable/disable FortiGate automatic update. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">banner-message</span> - Banner message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">chassis-mgmt</span> - Enable or disable chassis management. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">chassis-update-interval</span> - Chassis background update interval (4 - 1440 mins). <span class="li-normal">type: int</span>  <span class="li-normal">default: 15</span> </li>
 <li><span class="li-head">device_sync_status</span> - Enable/disable device synchronization status indication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">gui-theme</span> - Color scheme to use for the administration GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [blue, green, red, melongene, spring, summer, autumn, winter, space, calla-lily, binary-tunnel, diving, dreamy, technology, landscape, twilight, canyon, northern-light, astronomy, fish, penguin, panda, polar-bear, parrot, cave, circuit-board, mars, blue-sea, mountain, zebra, contrast-dark]</span>  <span class="li-normal">default: blue</span> </li>
 <li><span class="li-head">http_port</span> - HTTP port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
 <li><span class="li-head">https_port</span> - HTTPS port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 443</span> </li>
 <li><span class="li-head">idle_timeout</span> - Idle timeout (1 - 480 min). <span class="li-normal">type: int</span>  <span class="li-normal">default: 15</span> </li>
 <li><span class="li-head">install-ifpolicy-only</span> - Allow install interface policy only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">mgmt-addr</span> - IP of FortiManager used by FGFM. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mgmt-fqdn</span> - FQDN of FortiManager used by FGFM. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">objects-force-deletion</span> - Enable/disable used objects force deletion. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">offline_mode</span> - Enable/disable offline mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">register_passwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sdwan-monitor-history</span> - Enable/disable hostname display in the GUI login page. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">shell-access</span> - Enable/disable shell access. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">shell-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">show-add-multiple</span> - Show add multiple button. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show-adom-devman</span> - Show ADOM device manager tools on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">show-checkbox-in-table</span> - Show checkboxs in tables on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show-device-import-export</span> - Enable/disable import/export of ADOM, device, and group lists. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show-hostname</span> - Enable/disable hostname display in the GUI login page. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show_automatic_script</span> - Enable/disable automatic script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show_grouping_script</span> - Enable/disable grouping script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">show_schedule_script</span> - Enable or disable schedule script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show_tcl_script</span> - Enable/disable TCL script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">unreg_dev_opt</span> - Action to take when unregistered device connects to FortiManager. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [add_no_service, ignore, add_allow_service]</span>  <span class="li-normal">default: add_allow_service</span> </li>
 <li><span class="li-head">webadmin_language</span> - Web admin language. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto_detect, english, simplified_chinese, traditional_chinese, japanese, korean, spanish]</span>  <span class="li-normal">default: auto_detect</span> </li>
 <li><span class="li-head">show-fct-manager</span> - Enable/disable FCT manager. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">auth-addr</span> - IP which is used by FGT to authorize FMG. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auth-port</span> - Port which is used by FGT to authorize FMG. <span class="li-normal">type: int</span>  <span class="li-normal">default: 443</span> </li>
 <li><span class="li-head">idle_timeout_api</span> - Idle timeout for API sessions (1 - 28800 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 900</span> </li>
 <li><span class="li-head">idle_timeout_gui</span> - Idle timeout for GUI sessions (60 - 28800 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 900</span> </li>
 <li><span class="li-head">sdwan-skip-unmapped-input-device</span> - Skip unmapped interface for sdwan/rule/input-device instead of report mapping error. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
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
    - name: Admin setting.
      fmgr_system_admin_setting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_admin_setting:
            access-banner: <value in [disable, enable]>
            admin-https-redirect: <value in [disable, enable]>
            admin-login-max: <value of integer>
            admin_server_cert: <value of string>
            allow_register: <value in [disable, enable]>
            auto-update: <value in [disable, enable]>
            banner-message: <value of string>
            chassis-mgmt: <value in [disable, enable]>
            chassis-update-interval: <value of integer>
            device_sync_status: <value in [disable, enable]>
            gui-theme: <value in [blue, green, red, ...]>
            http_port: <value of integer>
            https_port: <value of integer>
            idle_timeout: <value of integer>
            install-ifpolicy-only: <value in [disable, enable]>
            mgmt-addr: <value of string>
            mgmt-fqdn: <value of string>
            objects-force-deletion: <value in [disable, enable]>
            offline_mode: <value in [disable, enable]>
            register_passwd: <value of string>
            sdwan-monitor-history: <value in [disable, enable]>
            shell-access: <value in [disable, enable]>
            shell-password: <value of string>
            show-add-multiple: <value in [disable, enable]>
            show-adom-devman: <value in [disable, enable]>
            show-checkbox-in-table: <value in [disable, enable]>
            show-device-import-export: <value in [disable, enable]>
            show-hostname: <value in [disable, enable]>
            show_automatic_script: <value in [disable, enable]>
            show_grouping_script: <value in [disable, enable]>
            show_schedule_script: <value in [disable, enable]>
            show_tcl_script: <value in [disable, enable]>
            unreg_dev_opt: <value in [add_no_service, ignore, add_allow_service]>
            webadmin_language: <value in [auto_detect, english, simplified_chinese, ...]>
            show-fct-manager: <value in [disable, enable]>
            auth-addr: <value of string>
            auth-port: <value of integer>
            idle_timeout_api: <value of integer>
            idle_timeout_gui: <value of integer>
            sdwan-skip-unmapped-input-device: <value in [disable, enable]>



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



