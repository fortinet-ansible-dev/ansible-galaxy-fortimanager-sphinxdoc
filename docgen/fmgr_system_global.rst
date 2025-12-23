:source: fmgr_system_global.py

:orphan:

.. _fmgr_system_global:

fmgr_system_global -- Global range attributes.
++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>



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
 <li><span class="li-head">system_global</span> - Global range attributes. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">admin_lockout_duration</span> <b>(Alias name: admin-lockout-duration)</b>  Lockout duration(sec) for administration. <span class="li-normal">type: int</span> <span class="li-normal">default: 60</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_lockout_threshold</span> <b>(Alias name: admin-lockout-threshold)</b>  Lockout threshold for administration. <span class="li-normal">type: int</span> <span class="li-normal">default: 3</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adom_mode</span> <b>(Alias name: adom-mode)</b>  Adom mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [normal, advanced]</span>  <span class="li-normal">default: normal</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adom_rev_auto_delete</span> <b>(Alias name: adom-rev-auto-delete)</b>  Auto delete features for old adom revisions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, by-revisions, by-days]</span>  <span class="li-normal">default: by-revisions</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adom_rev_max_backup_revisions</span> <b>(Alias name: adom-rev-max-backup-revisions)</b>  Maximum number of adom revisions to backup. <span class="li-normal">type: int</span> <span class="li-normal">default: 5</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adom_rev_max_days</span> <b>(Alias name: adom-rev-max-days)</b>  Number of days to keep old adom revisions. <span class="li-normal">type: int</span> <span class="li-normal">default: 30</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adom_rev_max_revisions</span> <b>(Alias name: adom-rev-max-revisions)</b>  Maximum number of adom revisions to keep. <span class="li-normal">type: int</span> <span class="li-normal">default: 120</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adom_select</span> <b>(Alias name: adom-select)</b>  Enable/disable select adom after login. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adom_status</span> <b>(Alias name: adom-status)</b>  Adom status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">clt_cert_req</span> <b>(Alias name: clt-cert-req)</b>  Require client certificate for gui login. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, optional]</span>  <span class="li-normal">default: disable</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">console_output</span> <b>(Alias name: console-output)</b>  Console output mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [standard, more]</span>  <span class="li-normal">default: standard</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">country_flag</span> <b>(Alias name: country-flag)</b>  Country flag status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">create_revision</span> <b>(Alias name: create-revision)</b>  Enable/disable create revision by default. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">daylightsavetime</span> Enable/disable daylight saving time. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">default_disk_quota</span> <b>(Alias name: default-disk-quota)</b>  Default disk quota for registered device (mb). <span class="li-normal">type: int</span> <span class="li-normal">default: 1000</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">detect_unregistered_log_device</span> <b>(Alias name: detect-unregistered-log-device)</b>  Detect unregistered logging device from log message. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">device_view_mode</span> <b>(Alias name: device-view-mode)</b>  Set devices/groups view mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular, tree]</span>  <span class="li-normal">default: regular</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dh_params</span> <b>(Alias name: dh-params)</b>  Minimum size of diffie-hellman prime for ssh/https (bits). <span class="li-normal">type: str</span> <span class="li-normal">choices: [1024, 1536, 2048, 3072, 4096, 6144, 8192]</span>  <span class="li-normal">default: 2048</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">disable_module</span> <b>(Alias name: disable-module)</b>  Disable module list. <span class="li-normal">type: list</span> <span class="li-normal">choices: [fortiview-noc, none, fortirecorder, siem, soc, ai, safeguard-mv]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">enc_algorithm</span> <b>(Alias name: enc-algorithm)</b>  Ssl communication encryption algorithms. <span class="li-normal">type: str</span> <span class="li-normal">choices: [low, medium, high, custom]</span>  <span class="li-normal">default: high</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">faz_status</span> <b>(Alias name: faz-status)</b>  Faz status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgfm_local_cert</span> <b>(Alias name: fgfm-local-cert)</b>  Set the fgfm local certificate. <span class="li-normal">type: str</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgfm_ssl_protocol</span> <b>(Alias name: fgfm-ssl-protocol)</b>  Set the lowest ssl protocols for fgfmsd. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3, follow-global-ssl-protocol]</span>  <span class="li-normal">default: tlsv1.2</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ha_member_auto_grouping</span> <b>(Alias name: ha-member-auto-grouping)</b>  Enable/disable automatically group ha members feature <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hitcount_concurrent</span> The number of fortigates that fortimanager polls at one time (10 - 500, default = 100). <span class="li-normal">type: int</span> <span class="li-normal">default: 100</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.4.2</code></p>
 </div>
 </li>
 <li><span class="li-head">hitcount_interval</span> The interval for getting hit count from managed fortigate devices, in seconds (60 - 86400, default = 300). <span class="li-normal">type: int</span> <span class="li-normal">default: 300</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.4.2</code></p>
 </div>
 </li>
 <li><span class="li-head">hostname</span> System hostname. <span class="li-normal">type: str</span> <span class="li-normal">default: FMG-VM64</span> 
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">import_ignore_addr_cmt</span> <b>(Alias name: import-ignore-addr-cmt)</b>  Enable/disable import ignore of address comments. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">language</span> System global language. <span class="li-normal">type: str</span> <span class="li-normal">choices: [english, simch, japanese, korean, spanish, trach]</span>  <span class="li-normal">default: english</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">latitude</span> Fmg location latitude <span class="li-normal">type: str</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldap_cache_timeout</span> <b>(Alias name: ldap-cache-timeout)</b>  Ldap browser cache timeout (seconds). <span class="li-normal">type: int</span> <span class="li-normal">default: 86400</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldapconntimeout</span> Ldap connection timeout (msec). <span class="li-normal">type: int</span> <span class="li-normal">default: 60000</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lock_preempt</span> <b>(Alias name: lock-preempt)</b>  Enable/disable adom lock override. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_checksum</span> <b>(Alias name: log-checksum)</b>  Record log file hash value, timestamp, and authentication code at transmission or rolling. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, md5, md5-auth]</span>  <span class="li-normal">default: none</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_forward_cache_size</span> <b>(Alias name: log-forward-cache-size)</b>  Log forwarding disk cache size (gb). <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">longitude</span> Fmg location longitude <span class="li-normal">type: str</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_log_forward</span> <b>(Alias name: max-log-forward)</b>  Maximum number of log-forward and aggregation settings. <span class="li-normal">type: int</span> <span class="li-normal">default: 5</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_running_reports</span> <b>(Alias name: max-running-reports)</b>  Maximum number of reports generating at one time. <span class="li-normal">type: int</span> <span class="li-normal">default: 1</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">oftp_ssl_protocol</span> <b>(Alias name: oftp-ssl-protocol)</b>  Set the lowest ssl protocols for oftpd. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span>  <span class="li-normal">default: tlsv1.2</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">partial_install</span> <b>(Alias name: partial-install)</b>  Enable/disable partial install (install some objects). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">partial_install_force</span> <b>(Alias name: partial-install-force)</b>  Enable/disable partial install when devdb is modified. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">partial_install_rev</span> <b>(Alias name: partial-install-rev)</b>  Enable/disable auto creating adom revision for partial install. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">perform_improve_by_ha</span> <b>(Alias name: perform-improve-by-ha)</b>  Enable/disable performance improvement by distributing tasks to ha slaves. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">policy_hit_count</span> <b>(Alias name: policy-hit-count)</b>  Show policy hit count. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.4.2</code></p>
 </div>
 </li>
 <li><span class="li-head">policy_object_in_dual_pane</span> <b>(Alias name: policy-object-in-dual-pane)</b>  Show policies and objects in dual pane. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pre_login_banner</span> <b>(Alias name: pre-login-banner)</b>  Enable/disable pre-login banner. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pre_login_banner_message</span> <b>(Alias name: pre-login-banner-message)</b>  Pre-login banner message. <span class="li-normal">type: str</span>
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remoteauthtimeout</span> Remote authentication (radius/ldap) timeout (sec). <span class="li-normal">type: int</span> <span class="li-normal">default: 10</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">search_all_adoms</span> <b>(Alias name: search-all-adoms)</b>  Enable/disable search all adoms for where-used query. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_low_encryption</span> <b>(Alias name: ssl-low-encryption)</b>  Ssl low-grade encryption. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_protocol</span> <b>(Alias name: ssl-protocol)</b>  Ssl protocols. <span class="li-normal">type: list</span> <span class="li-normal">choices: [tlsv1.2, tlsv1.1, tlsv1.0, sslv3, tlsv1.3]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.4.3</code>, <code class="docutils literal notranslate">v7.6.0 -> v7.6.1</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_static_key_ciphers</span> <b>(Alias name: ssl-static-key-ciphers)</b>  Enable/disable ssl static key ciphers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">task_list_size</span> <b>(Alias name: task-list-size)</b>  Maximum number of completed tasks to keep. <span class="li-normal">type: int</span> <span class="li-normal">default: 2000</span> 
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tftp</span> Enable/disable tftp in `exec restore image` command (disabled by default in fips mode) <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">timezone</span> Time zone. <span class="li-normal">type: str</span> <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]</span>  <span class="li-normal">default: 04</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tunnel_mtu</span> <b>(Alias name: tunnel-mtu)</b>  Maximum transportation unit(68 - 9000). <span class="li-normal">type: int</span> <span class="li-normal">default: 1500</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">usg</span> Enable/disable fortiguard server restriction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vdom_mirror</span> <b>(Alias name: vdom-mirror)</b>  Vdom mirror. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webservice_proto</span> <b>(Alias name: webservice-proto)</b>  Web service connection support ssl protocols. <span class="li-normal">type: list</span> <span class="li-normal">choices: [tlsv1.2, tlsv1.1, tlsv1.0, sslv3, sslv2, tlsv1.3]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">workflow_max_sessions</span> <b>(Alias name: workflow-max-sessions)</b>  Maximum number of workflow sessions per adom (minimum 100). <span class="li-normal">type: int</span> <span class="li-normal">default: 500</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">workspace_mode</span> <b>(Alias name: workspace-mode)</b>  Set workspace mode (adom locking). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, normal, workflow, per-adom]</span>  <span class="li-normal">default: disabled</span> 
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">clone_name_option</span> <b>(Alias name: clone-name-option)</b>  Set the clone object names option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, keep]</span>  <span class="li-normal">default: default</span> 
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgfm_ca_cert</span> <b>(Alias name: fgfm-ca-cert)</b>  Set the extra fgfm ca certificates. <span class="li-normal">type: str</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mc_policy_disabled_adoms</span> <b>(Alias name: mc-policy-disabled-adoms)</b>  Mc policy disabled adoms. <span class="li-normal">type: list</span>
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">adom_name</span> <b>(Alias name: adom-name)</b>  Adom names. <span class="li-normal">type: str</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">policy_object_icon</span> <b>(Alias name: policy-object-icon)</b>  Show icons of policy objects. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">private_data_encryption</span> <b>(Alias name: private-data-encryption)</b>  Enable/disable private data encryption using an aes 128-bit key. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">per_policy_lock</span> <b>(Alias name: per-policy-lock)</b>  Enable/disable per policy lock. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">multiple_steps_upgrade_in_autolink</span> <b>(Alias name: multiple-steps-upgrade-in-autolink)</b>  Enable/disable multiple steps upgade in autolink process <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">object_revision_db_max</span> <b>(Alias name: object-revision-db-max)</b>  Maximum revisions for a single database (10,000-1,000,000 default 100,000). <span class="li-normal">type: int</span> <span class="li-normal">default: 100000</span> 
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">object_revision_mandatory_note</span> <b>(Alias name: object-revision-mandatory-note)</b>  Enable/disable mandatory note when create revision. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">object_revision_object_max</span> <b>(Alias name: object-revision-object-max)</b>  Maximum revisions for a single object (10-1000 default 100). <span class="li-normal">type: int</span> <span class="li-normal">default: 100</span> 
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">object_revision_status</span> <b>(Alias name: object-revision-status)</b>  Enable/disable create revision when modify objects. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">normalized_intf_zone_only</span> <b>(Alias name: normalized-intf-zone-only)</b>  Allow normalized interface to be zone only. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.7 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_cipher_suites</span> <b>(Alias name: ssl-cipher-suites)</b>  Ssl cipher suites. <span class="li-normal">type: list</span>
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">cipher</span> Cipher name <span class="li-normal">type: str</span>
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Ssl/tls cipher suites priority. <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">version</span> Ssl/tls version the cipher suite can be used with. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tls1.2-or-below, tls1.3]</span>  <span class="li-normal">default: tls1.2-or-below</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">gui_curl_timeout</span> <b>(Alias name: gui-curl-timeout)</b>  Gui curl timeout in seconds (5-300 default 30). <span class="li-normal">type: int</span> <span class="li-normal">default: 30</span> 
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.11 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.7 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgfm_cert_exclusive</span> <b>(Alias name: fgfm-cert-exclusive)</b>  Set if the local or ca certificates should be used exclusively. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.15 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.12 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgfm_deny_unknown</span> <b>(Alias name: fgfm-deny-unknown)</b>  Set if allow devices with unknown sn actively register as an unauthorized device. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.15 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.12 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgfm_peercert_withoutsn</span> <b>(Alias name: fgfm-peercert-withoutsn)</b>  Set if the subject cn or san of peers ssl certificate sent in fgfm should include the serial number of the device. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.15 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.12 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.3 -> v7.4.5</code>, <code class="docutils literal notranslate">v7.6.0 -> v7.6.1</code></p>
 </div>
 </li>
 <li><span class="li-head">table_entry_blink</span> <b>(Alias name: table-entry-blink)</b>  Enable/disable table entry blink in gui <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.4 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">contentpack_fgt_install</span> <b>(Alias name: contentpack-fgt-install)</b>  Enable/disable outbreak alert auto install for fgt adoms . <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_polling_interval</span> <b>(Alias name: gui-polling-interval)</b>  Gui polling interval in seconds (1-288000 default 5). <span class="li-normal">type: int</span> <span class="li-normal">default: 5</span> 
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">no_copy_permission_check</span> <b>(Alias name: no-copy-permission-check)</b>  Do not perform permission check to block object changes in different adom during copy and install. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.8 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_enc_algo</span> <b>(Alias name: ssh-enc-algo)</b>  Select one or more ssh ciphers. <span class="li-normal">type: list</span> <span class="li-normal">choices: [chacha20-poly1305@openssh.com, aes128-ctr, aes192-ctr, aes256-ctr, arcfour256, arcfour128, aes128-cbc, 3des-cbc, blowfish-cbc, cast128-cbc, aes192-cbc, aes256-cbc, arcfour, rijndael-cbc@lysator.liu.se, aes128-gcm@openssh.com, aes256-gcm@openssh.com]</span> 
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.11 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_hostkey_algo</span> <b>(Alias name: ssh-hostkey-algo)</b>  Select one or more ssh hostkey algorithms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [ssh-rsa, ecdsa-sha2-nistp521, rsa-sha2-256, rsa-sha2-512, ssh-ed25519]</span> 
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.11 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_kex_algo</span> <b>(Alias name: ssh-kex-algo)</b>  Select one or more ssh kex algorithms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [diffie-hellman-group1-sha1, diffie-hellman-group14-sha1, diffie-hellman-group14-sha256, diffie-hellman-group16-sha512, diffie-hellman-group18-sha512, diffie-hellman-group-exchange-sha1, diffie-hellman-group-exchange-sha256, curve25519-sha256@libssh.org, ecdh-sha2-nistp256, ecdh-sha2-nistp384, ecdh-sha2-nistp521]</span> 
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.11 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_mac_algo</span> <b>(Alias name: ssh-mac-algo)</b>  Select one or more ssh mac algorithms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [hmac-md5, hmac-md5-etm@openssh.com, hmac-md5-96, hmac-md5-96-etm@openssh.com, hmac-sha1, hmac-sha1-etm@openssh.com, hmac-sha2-256, hmac-sha2-256-etm@openssh.com, hmac-sha2-512, hmac-sha2-512-etm@openssh.com, hmac-ripemd160, hmac-ripemd160@openssh.com, hmac-ripemd160-etm@openssh.com, umac-64@openssh.com, umac-128@openssh.com, umac-64-etm@openssh.com, umac-128-etm@openssh.com]</span> 
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.11 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_strong_crypto</span> <b>(Alias name: ssh-strong-crypto)</b>  Only allow strong ciphers for ssh when enabled. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.11 -> v7.0.15</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.2 -> v7.6.3</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_lockout_method</span> <b>(Alias name: admin-lockout-method)</b>  Lockout method for administration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ip, user]</span>  <span class="li-normal">default: ip</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">workspace_unlock_after_install</span> <b>(Alias name: workspace-unlock-after-install)</b>  Enable/disable adom auto-unlock after device installation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_checksum_upload</span> <b>(Alias name: log-checksum-upload)</b>  Enable/disable upload log checksum with log files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">apache_mode</span> <b>(Alias name: apache-mode)</b>  Set apache mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [event, prefork]</span>  <span class="li-normal">default: event</span> 
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.4 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">no_vip_value_check</span> <b>(Alias name: no-vip-value-check)</b>  Enable/disable skipping policy instead of throwing error when vip has no default or dynamic mapping during policy copy <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.4 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiservice_port</span> <b>(Alias name: fortiservice-port)</b>  Fortiservice port (1 - 65535, default = 8013). <span class="li-normal">type: int</span> <span class="li-normal">default: 8013</span> 
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">management_ip</span> <b>(Alias name: management-ip)</b>  Management ip address of this fortigate. <span class="li-normal">type: str</span>
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">management_port</span> <b>(Alias name: management-port)</b>  Overriding port for management connection (overrides admin port). <span class="li-normal">type: int</span> <span class="li-normal">default: 443</span> 
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">save_last_hit_in_adomdb</span> <b>(Alias name: save-last-hit-in-adomdb)</b>  Enable/disable save last-hit value in adomdb. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">api_ip_binding</span> <b>(Alias name: api-ip-binding)</b>  Enable/disable source ip check for json api request. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_host</span> <b>(Alias name: admin-host)</b>  Administrative host for http and https. <span class="li-normal">type: str</span>
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_ssh_grace_time</span> <b>(Alias name: admin-ssh-grace-time)</b>  Maximum time in seconds permitted between making an ssh connection to the fortimanager unit and authenticating (10 - 3600 sec (1 hour), default 120). <span class="li-normal">type: int</span> <span class="li-normal">default: 120</span> 
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.6 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fabric_storage_pool_quota</span> <b>(Alias name: fabric-storage-pool-quota)</b>  Disk quota for fabric (mb). <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fabric_storage_pool_size</span> <b>(Alias name: fabric-storage-pool-size)</b>  Max storage pooll size <span class="li-normal">type: int</span> <span class="li-normal">default: 20</span> 
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fcp_cfg_service</span> <b>(Alias name: fcp-cfg-service)</b>  Enable/disable fcp service processing configuration requests <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.6 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">jsonapi_log</span> <b>(Alias name: jsonapi-log)</b>  Enable jsonapi log. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, request, response, all]</span>  <span class="li-normal">default: disable</span> 
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">global_ssl_protocol</span> <b>(Alias name: global-ssl-protocol)</b>  Set the lowest ssl protocol version for all ssl connections. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span>  <span class="li-normal">default: tlsv1.2</span> 
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.4 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">httpd_ssl_protocol</span> <b>(Alias name: httpd-ssl-protocol)</b>  Set ssl protocols for apache daemon (httpd) <span class="li-normal">type: list</span> <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span> 
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.4 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mapclient_ssl_protocol</span> <b>(Alias name: mapclient-ssl-protocol)</b>  Set the lowest ssl protocol version for connection to mapserver. <span class="li-normal">type: str</span> <span class="li-normal">choices: [follow-global-ssl-protocol, sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span>  <span class="li-normal">default: follow-global-ssl-protocol</span> 
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.4 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">apache_wsgi_processes</span> <b>(Alias name: apache-wsgi-processes)</b>  Apache wsgi processes. <span class="li-normal">type: int</span> <span class="li-normal">default: 10</span> 
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.10 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.6 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fmg_fabric_port</span> <b>(Alias name: fmg-fabric-port)</b>  Fmg fabric port. <span class="li-normal">type: int</span> <span class="li-normal">default: 8893</span> 
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_feature_visibility_mode</span> <b>(Alias name: gui-feature-visibility-mode)</b>  Gui feature visibility mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [per-adom, per-admin]</span>  <span class="li-normal">default: per-adom</span> 
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">storage_age_limit</span> <b>(Alias name: storage-age-limit)</b>  Storage age limit. <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgfm_allow_vm</span> <b>(Alias name: fgfm-allow-vm)</b>  Enable/disable vm platform fgfm connect restriction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.10 -> v7.2.11</code>, <code class="docutils literal notranslate">v7.4.7 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hitcount_response_timeout</span> <b>(Alias name: hitcount-response-timeout)</b>  Timeout of waiting for hitcount response (60 - 300 seconds). <span class="li-normal">type: int</span> <span class="li-normal">default: 60</span> 
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rpc_log</span> <b>(Alias name: rpc-log)</b>  Enable/disable incoming/outgoing rpc log. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_dev_restapi_allowlist</span> <b>(Alias name: auth-dev-restapi-allowlist)</b>  Auth dev restapi allowlist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_install_preview_concurrency</span> <b>(Alias name: gui-install-preview-concurrency)</b>  Set the maximum number of devices to be processed in a single gui install preview request (1-100 default 20). <span class="li-normal">type: int</span> <span class="li-normal">default: 20</span> 
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.8 -> v7.4.8</code>, <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
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

  - name: Example playbook
    hosts: fortimanagers
    gather_facts: false
    connection: httpapi
    vars:
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_httpapi_port: 443
    tasks:
      - name: Enable workspace mode
        fortinet.fortimanager.fmgr_system_global:
          system_global:
            adom_status: enable
            workspace_mode: normal
  
      - name: Script table.
        fortinet.fortimanager.fmgr_dvmdb_script:
          bypass_validation: false
          adom: root
          state: present
          workspace_locking_adom: "root"
          dvmdb_script:
            content: "ansiblt-test"
            name: "fooscript000"
            target: device_database
            type: cli
  
      - name: Verify script table
        fortinet.fortimanager.fmgr_fact:
          facts:
            selector: "dvmdb_script"
            params:
              adom: "root"
              script: "fooscript000"
        register: info
        failed_when: info.meta.response_code != 0
  
      - name: Restore workspace mode
        fortinet.fortimanager.fmgr_system_global:
          system_global:
            adom_status: enable
            workspace_mode: disabled


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
