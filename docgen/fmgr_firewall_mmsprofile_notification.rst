:source: fmgr_firewall_mmsprofile_notification.py

:orphan:

.. _fmgr_firewall_mmsprofile_notification:

fmgr_firewall_mmsprofile_notification -- Notification configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. warning::
   Starting in version 3.0.0, all input arguments will be named using the underscore naming convention (snake_case).
  
   - Argument name before 3.0.0: ``var-name``, ``var name``, ``var.name``
   - New argument name starting in 3.0.0: ``var_name``
  
   FortiManager Ansible v2.4+ supports both previous argument name and new underscore name.
   You will receive deprecation warnings if you keep using the previous argument name.
   You can ignore the warning by setting deprecation_warnings=False in ansible.cfg.

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device.
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v7.x.


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.15.0


FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>



Parameters
----------
.. raw:: html

 <ul>
 <li><span class="li-head">access_token</span> -The token to access FortiManager without using username and password. <span class="li-normal">type: str</span> <span class="li-required">required: false</span></li> <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters. <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task. <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">forticloud_access_token</span> - Access token of forticloud managed API users, this option is available with FortiManager later than 6.4.0. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden. <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden. <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock. <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">mms_profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_mmsprofile_notification</span> - Notification configuration. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">alert_int</span> <b>(Alias name: alert-int)</b>  Alert notification send interval. <span class="li-normal">type: int</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">alert_int_mode</span> <b>(Alias name: alert-int-mode)</b>  Alert notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">alert_src_msisdn</span> <b>(Alias name: alert-src-msisdn)</b>  Specify from address for alert messages. <span class="li-normal">type: str</span>
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">alert_status</span> <b>(Alias name: alert-status)</b>  Alert notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">bword_int</span> <b>(Alias name: bword-int)</b>  Banned word notification send interval. <span class="li-normal">type: int</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">bword_int_mode</span> <b>(Alias name: bword-int-mode)</b>  Banned word notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">bword_status</span> <b>(Alias name: bword-status)</b>  Banned word notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">carrier_endpoint_bwl_int</span> <b>(Alias name: carrier-endpoint-bwl-int)</b>  Carrier end point black/white list notification send interval. <span class="li-normal">type: int</span>
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">carrier_endpoint_bwl_int_mode</span> <b>(Alias name: carrier-endpoint-bwl-int-mode)</b>  Carrier end point black/white list notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">carrier_endpoint_bwl_status</span> <b>(Alias name: carrier-endpoint-bwl-status)</b>  Carrier end point black/white list notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">days_allowed</span> <b>(Alias name: days-allowed)</b>  Weekdays on which notification messages may be sent. <span class="li-normal">type: list</span> <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">detect_server</span> <b>(Alias name: detect-server)</b>  Enable/disable automatic server address determination. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">dupe_int</span> <b>(Alias name: dupe-int)</b>  Duplicate notification send interval. <span class="li-normal">type: int</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">dupe_int_mode</span> <b>(Alias name: dupe-int-mode)</b>  Duplicate notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">dupe_status</span> <b>(Alias name: dupe-status)</b>  Duplicate notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">file_block_int</span> <b>(Alias name: file-block-int)</b>  File block notification send interval. <span class="li-normal">type: int</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">file_block_int_mode</span> <b>(Alias name: file-block-int-mode)</b>  File block notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">file_block_status</span> <b>(Alias name: file-block-status)</b>  File block notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">flood_int</span> <b>(Alias name: flood-int)</b>  Flood notification send interval. <span class="li-normal">type: int</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">flood_int_mode</span> <b>(Alias name: flood-int-mode)</b>  Flood notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">flood_status</span> <b>(Alias name: flood-status)</b>  Flood notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">from_in_header</span> <b>(Alias name: from-in-header)</b>  Enable/disable insertion of from address in http header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mms_checksum_int</span> <b>(Alias name: mms-checksum-int)</b>  Mms checksum notification send interval. <span class="li-normal">type: int</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mms_checksum_int_mode</span> <b>(Alias name: mms-checksum-int-mode)</b>  Mms checksum notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mms_checksum_status</span> <b>(Alias name: mms-checksum-status)</b>  Mms checksum notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mmsc_hostname</span> <b>(Alias name: mmsc-hostname)</b>  Host name or ip address of the mmsc. <span class="li-normal">type: str</span>
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mmsc_password</span> <b>(Alias name: mmsc-password)</b>  Password required for authentication with the mmsc. <span class="li-normal">type: list</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mmsc_port</span> <b>(Alias name: mmsc-port)</b>  Port used on the mmsc for sending mms messages (1 - 65535). <span class="li-normal">type: int</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mmsc_url</span> <b>(Alias name: mmsc-url)</b>  Url used on the mmsc for sending mms messages. <span class="li-normal">type: str</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">mmsc_username</span> <b>(Alias name: mmsc-username)</b>  User name required for authentication with the mmsc. <span class="li-normal">type: str</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">msg_protocol</span> <b>(Alias name: msg-protocol)</b>  Protocol to use for sending notification messages. <span class="li-normal">type: str</span> <span class="li-normal">choices: [mm1, mm3, mm4, mm7]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">msg_type</span> <b>(Alias name: msg-type)</b>  Mm7 message type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [submit-req, deliver-req]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">protocol</span> Protocol. <span class="li-normal">type: str</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">rate_limit</span> <b>(Alias name: rate-limit)</b>  Rate limit for sending notification messages (0 - 250). <span class="li-normal">type: int</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">tod_window_duration</span> <b>(Alias name: tod-window-duration)</b>  Time of day window duration. <span class="li-normal">type: str</span>
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">tod_window_end</span> <b>(Alias name: tod-window-end)</b>  Obsolete. <span class="li-normal">type: str</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">tod_window_start</span> <b>(Alias name: tod-window-start)</b>  Time of day window start. <span class="li-normal">type: str</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">user_domain</span> <b>(Alias name: user-domain)</b>  Domain name to which the user addresses belong. <span class="li-normal">type: str</span>
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">vas_id</span> <b>(Alias name: vas-id)</b>  Vas identifier. <span class="li-normal">type: str</span>
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">vasp_id</span> <b>(Alias name: vasp-id)</b>  Vasp identifier. <span class="li-normal">type: str</span>
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">virus_int</span> <b>(Alias name: virus-int)</b>  Virus notification send interval. <span class="li-normal">type: int</span>
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">virus_int_mode</span> <b>(Alias name: virus-int-mode)</b>  Virus notification interval mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [hours, minutes]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">virus_status</span> <b>(Alias name: virus-status)</b>  Virus notification status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
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

  - name: Example playbook (generated based on argument schema)
    hosts: fortimanagers
    connection: httpapi
    gather_facts: false
    vars:
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_httpapi_port: 443
    tasks:
      - name: Notification configuration.
        fortinet.fortimanager.fmgr_firewall_mmsprofile_notification:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          mms_profile: <your own value>
          firewall_mmsprofile_notification:
            # alert_int: <integer>
            # alert_int_mode: <value in [hours, minutes]>
            # alert_src_msisdn: <string>
            # alert_status: <value in [disable, enable]>
            # bword_int: <integer>
            # bword_int_mode: <value in [hours, minutes]>
            # bword_status: <value in [disable, enable]>
            # carrier_endpoint_bwl_int: <integer>
            # carrier_endpoint_bwl_int_mode: <value in [hours, minutes]>
            # carrier_endpoint_bwl_status: <value in [disable, enable]>
            # days_allowed:
            #   - "sunday"
            #   - "monday"
            #   - "tuesday"
            #   - "wednesday"
            #   - "thursday"
            #   - "friday"
            #   - "saturday"
            # detect_server: <value in [disable, enable]>
            # dupe_int: <integer>
            # dupe_int_mode: <value in [hours, minutes]>
            # dupe_status: <value in [disable, enable]>
            # file_block_int: <integer>
            # file_block_int_mode: <value in [hours, minutes]>
            # file_block_status: <value in [disable, enable]>
            # flood_int: <integer>
            # flood_int_mode: <value in [hours, minutes]>
            # flood_status: <value in [disable, enable]>
            # from_in_header: <value in [disable, enable]>
            # mms_checksum_int: <integer>
            # mms_checksum_int_mode: <value in [hours, minutes]>
            # mms_checksum_status: <value in [disable, enable]>
            # mmsc_hostname: <string>
            # mmsc_password: <list or string>
            # mmsc_port: <integer>
            # mmsc_url: <string>
            # mmsc_username: <string>
            # msg_protocol: <value in [mm1, mm3, mm4, ...]>
            # msg_type: <value in [submit-req, deliver-req]>
            # protocol: <string>
            # rate_limit: <integer>
            # tod_window_duration: <string>
            # tod_window_end: <string>
            # tod_window_start: <string>
            # user_domain: <string>
            # vas_id: <string>
            # vasp_id: <string>
            # virus_int: <integer>
            # virus_int_mode: <value in [hours, minutes]>
            # virus_status: <value in [disable, enable]>


Return Values
-------------

Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:

.. raw:: html

 <ul>
 <li> <span class="li-return">meta</span> - The result of the request.<span class="li-normal">returned: always</span> <span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li> <span class="li-return">request_url</span> - The full url requested. <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request. <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_data</span> - The data body of the api response. <span class="li-normal">returned: optional</span> <span class="li-normal">type: list or dict</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response. <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</span></li>
 <li> <span class="li-return">system_information</span> - The information of the target system. <span class="li-normal">returned: always</span> <span class="li-normal">type: dict</span></li>
 </ul>
 <li> <span class="li-return">rc</span> - The status the request. <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">version_check_warning</span> - Warning if the parameters used in the playbook are not supported by the current FortiManager version. <span class="li-normal">returned: if at least one parameter not supported by the current FortiManager version</span> <span class="li-normal">type: list</span> </li>
 </ul>


Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)
