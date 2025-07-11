:source: fmgr_antivirus_profile.py

:orphan:

.. _fmgr_antivirus_profile:

fmgr_antivirus_profile -- Configure AntiVirus profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock. <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">antivirus_profile</span> - Configure AntiVirus profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">analytics_bl_filetype</span> <b>(Alias name: analytics-bl-filetype)</b>  Only submit files matching this dlp file-pattern to fortisandbox. <span class="li-normal">type: str</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">analytics_db</span> <b>(Alias name: analytics-db)</b>  Enable/disable using the fortisandbox signature database to supplement the av signature databases. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">analytics_max_upload</span> <b>(Alias name: analytics-max-upload)</b>  Maximum size of files that can be uploaded to fortisandbox (1 - 395 mbytes, default = 10). <span class="li-normal">type: int</span>
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">analytics_wl_filetype</span> <b>(Alias name: analytics-wl-filetype)</b>  Do not submit files matching this dlp file-pattern to fortisandbox. <span class="li-normal">type: str</span>
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_block_log</span> <b>(Alias name: av-block-log)</b>  Enable/disable logging for antivirus file blocking. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_virus_log</span> <b>(Alias name: av-virus-log)</b>  Enable/disable antivirus logging. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">comment</span> Comment. <span class="li-normal">type: str</span>
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">extended_log</span> <b>(Alias name: extended-log)</b>  Enable/disable extended logging for antivirus. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ftgd_analytics</span> <b>(Alias name: ftgd-analytics)</b>  Settings to control which files are uploaded to fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, suspicious, everything]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">inspection_mode</span> <b>(Alias name: inspection-mode)</b>  Inspection mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [proxy, flow-based]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.1</code></p>
 </div>
 </li>
 <li><span class="li-head">mobile_malware_db</span> <b>(Alias name: mobile-malware-db)</b>  Enable/disable using the mobile malware signature database. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Profile name. <span class="li-normal">type: str</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">replacemsg_group</span> <b>(Alias name: replacemsg-group)</b>  Replacement message group customized for this profile. <span class="li-normal">type: str</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">scan_mode</span> <b>(Alias name: scan-mode)</b>  Choose between full scan mode and quick scan mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [quick, full, legacy, default]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">feature_set</span> <b>(Alias name: feature-set)</b>  Flow/proxy feature set. <span class="li-normal">type: str</span> <span class="li-normal">choices: [proxy, flow]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cifs</span> Cifs. <span class="li-normal">type: dict</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable cifs antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, quarantine, avmonitor]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">content_disarm</span> <b>(Alias name: content-disarm)</b>  Content disarm. <span class="li-normal">type: dict</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">cover_page</span> <b>(Alias name: cover-page)</b>  Enable/disable inserting a cover page into the disarmed document. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">detect_only</span> <b>(Alias name: detect-only)</b>  Enable/disable only detect disarmable files, do not alter content. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">error_action</span> <b>(Alias name: error-action)</b>  Action to be taken if cdr engine encounters an unrecoverable error. <span class="li-normal">type: str</span> <span class="li-normal">choices: [block, log-only, ignore]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">office_action</span> <b>(Alias name: office-action)</b>  Enable/disable stripping of powerpoint action events in microsoft office documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">office_dde</span> <b>(Alias name: office-dde)</b>  Enable/disable stripping of dynamic data exchange events in microsoft office documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">office_embed</span> <b>(Alias name: office-embed)</b>  Enable/disable stripping of embedded objects in microsoft office documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">office_hylink</span> <b>(Alias name: office-hylink)</b>  Enable/disable stripping of hyperlinks in microsoft office documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">office_linked</span> <b>(Alias name: office-linked)</b>  Enable/disable stripping of linked objects in microsoft office documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">office_macro</span> <b>(Alias name: office-macro)</b>  Enable/disable stripping of macros in microsoft office documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">original_file_destination</span> <b>(Alias name: original-file-destination)</b>  Destination to send original file if active content is removed. <span class="li-normal">type: str</span> <span class="li-normal">choices: [fortisandbox, quarantine, discard]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_act_form</span> <b>(Alias name: pdf-act-form)</b>  Enable/disable stripping of pdf document actions that submit data to other targets. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_act_gotor</span> <b>(Alias name: pdf-act-gotor)</b>  Enable/disable stripping of pdf document actions that access other pdf documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_act_java</span> <b>(Alias name: pdf-act-java)</b>  Enable/disable stripping of pdf document actions that execute javascript code. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_act_launch</span> <b>(Alias name: pdf-act-launch)</b>  Enable/disable stripping of pdf document actions that launch other applications. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_act_movie</span> <b>(Alias name: pdf-act-movie)</b>  Enable/disable stripping of pdf document actions that play a movie. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_act_sound</span> <b>(Alias name: pdf-act-sound)</b>  Enable/disable stripping of pdf document actions that play a sound. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_embedfile</span> <b>(Alias name: pdf-embedfile)</b>  Enable/disable stripping of embedded files in pdf documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_hyperlink</span> <b>(Alias name: pdf-hyperlink)</b>  Enable/disable stripping of hyperlinks from pdf documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pdf_javacode</span> <b>(Alias name: pdf-javacode)</b>  Enable/disable stripping of javascript code in pdf documents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">analytics_suspicious</span> <b>(Alias name: analytics-suspicious)</b>  Enable/disable using cdr as a secondary method for determining suspicous files for analytics. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ftp</span> Ftp. <span class="li-normal">type: dict</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable ftp antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> 
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">http</span> Http. <span class="li-normal">type: dict</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">content_disarm</span> <b>(Alias name: content-disarm)</b>  Enable content disarm and reconstruction for this protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable http antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor, strict-file]</span> 
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_optimize</span> <b>(Alias name: av-optimize)</b>  Av optimize. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">unknown_content_encoding</span> <b>(Alias name: unknown-content-encoding)</b>  Configure the action the fortigate unit will take on unknown content-encoding. <span class="li-normal">type: str</span> <span class="li-normal">choices: [block, inspect, bypass]</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">imap</span> Imap. <span class="li-normal">type: dict</span>
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">content_disarm</span> <b>(Alias name: content-disarm)</b>  Enable content disarm and reconstruction for this protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">executables</span> Treat windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, virus]</span> 
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable imap antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> 
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">mapi</span> Mapi. <span class="li-normal">type: dict</span>
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">executables</span> Treat windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, virus]</span> 
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable mapi antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, quarantine, avquery, avmonitor]</span> 
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">nac_quar</span> <b>(Alias name: nac-quar)</b>  Nac quar. <span class="li-normal">type: dict</span>
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">expiry</span> Duration of quarantine. <span class="li-normal">type: str</span>
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">infected</span> Enable/disable quarantining infected hosts to the banned user list. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, quar-src-ip, quar-interface]</span> 
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log</span> Enable/disable antivirus quarantine logging. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">nntp</span> Nntp. <span class="li-normal">type: dict</span>
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable nntp antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> 
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Outbreak prevention. <span class="li-normal">type: dict</span>
 <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable/disable external malware blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ftgd_service</span> <b>(Alias name: ftgd-service)</b>  Enable/disable fortiguard virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">pop3</span> Pop3. <span class="li-normal">type: dict</span>
 <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">content_disarm</span> <b>(Alias name: content-disarm)</b>  Enable content disarm and reconstruction for this protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">executables</span> Treat windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, virus]</span> 
 <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable pop3 antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> 
 <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label276' href="javascript:ContentClick('label277', 'label276');" onmouseover="ContentPreview('label277');" onmouseout="ContentUnpreview('label277');" title="click to collapse or expand..."> more... </a>
 <div id="label277" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label278' href="javascript:ContentClick('label279', 'label278');" onmouseover="ContentPreview('label279');" onmouseout="ContentUnpreview('label279');" title="click to collapse or expand..."> more... </a>
 <div id="label279" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label280' href="javascript:ContentClick('label281', 'label280');" onmouseover="ContentPreview('label281');" onmouseout="ContentUnpreview('label281');" title="click to collapse or expand..."> more... </a>
 <div id="label281" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label282' href="javascript:ContentClick('label283', 'label282');" onmouseover="ContentPreview('label283');" onmouseout="ContentUnpreview('label283');" title="click to collapse or expand..."> more... </a>
 <div id="label283" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">smtp</span> Smtp. <span class="li-normal">type: dict</span>
 <a id='label284' href="javascript:ContentClick('label285', 'label284');" onmouseover="ContentPreview('label285');" onmouseout="ContentUnpreview('label285');" title="click to collapse or expand..."> more... </a>
 <div id="label285" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label286' href="javascript:ContentClick('label287', 'label286');" onmouseover="ContentPreview('label287');" onmouseout="ContentUnpreview('label287');" title="click to collapse or expand..."> more... </a>
 <div id="label287" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label288' href="javascript:ContentClick('label289', 'label288');" onmouseover="ContentPreview('label289');" onmouseout="ContentUnpreview('label289');" title="click to collapse or expand..."> more... </a>
 <div id="label289" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">content_disarm</span> <b>(Alias name: content-disarm)</b>  Enable content disarm and reconstruction for this protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label290' href="javascript:ContentClick('label291', 'label290');" onmouseover="ContentPreview('label291');" onmouseout="ContentUnpreview('label291');" title="click to collapse or expand..."> more... </a>
 <div id="label291" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label292' href="javascript:ContentClick('label293', 'label292');" onmouseover="ContentPreview('label293');" onmouseout="ContentUnpreview('label293');" title="click to collapse or expand..."> more... </a>
 <div id="label293" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">executables</span> Treat windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, virus]</span> 
 <a id='label294' href="javascript:ContentClick('label295', 'label294');" onmouseover="ContentPreview('label295');" onmouseout="ContentUnpreview('label295');" title="click to collapse or expand..."> more... </a>
 <div id="label295" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable smtp antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> 
 <a id='label296' href="javascript:ContentClick('label297', 'label296');" onmouseover="ContentPreview('label297');" onmouseout="ContentUnpreview('label297');" title="click to collapse or expand..."> more... </a>
 <div id="label297" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label298' href="javascript:ContentClick('label299', 'label298');" onmouseover="ContentPreview('label299');" onmouseout="ContentUnpreview('label299');" title="click to collapse or expand..."> more... </a>
 <div id="label299" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label300' href="javascript:ContentClick('label301', 'label300');" onmouseover="ContentPreview('label301');" onmouseout="ContentUnpreview('label301');" title="click to collapse or expand..."> more... </a>
 <div id="label301" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label302' href="javascript:ContentClick('label303', 'label302');" onmouseover="ContentPreview('label303');" onmouseout="ContentUnpreview('label303');" title="click to collapse or expand..."> more... </a>
 <div id="label303" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label304' href="javascript:ContentClick('label305', 'label304');" onmouseover="ContentPreview('label305');" onmouseout="ContentUnpreview('label305');" title="click to collapse or expand..."> more... </a>
 <div id="label305" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label306' href="javascript:ContentClick('label307', 'label306');" onmouseover="ContentPreview('label307');" onmouseout="ContentUnpreview('label307');" title="click to collapse or expand..."> more... </a>
 <div id="label307" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label308' href="javascript:ContentClick('label309', 'label308');" onmouseover="ContentPreview('label309');" onmouseout="ContentUnpreview('label309');" title="click to collapse or expand..."> more... </a>
 <div id="label309" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label310' href="javascript:ContentClick('label311', 'label310');" onmouseover="ContentPreview('label311');" onmouseout="ContentUnpreview('label311');" title="click to collapse or expand..."> more... </a>
 <div id="label311" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label312' href="javascript:ContentClick('label313', 'label312');" onmouseover="ContentPreview('label313');" onmouseout="ContentUnpreview('label313');" title="click to collapse or expand..."> more... </a>
 <div id="label313" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ssh</span> Ssh. <span class="li-normal">type: dict</span>
 <a id='label314' href="javascript:ContentClick('label315', 'label314');" onmouseover="ContentPreview('label315');" onmouseout="ContentUnpreview('label315');" title="click to collapse or expand..."> more... </a>
 <div id="label315" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label316' href="javascript:ContentClick('label317', 'label316');" onmouseover="ContentPreview('label317');" onmouseout="ContentUnpreview('label317');" title="click to collapse or expand..."> more... </a>
 <div id="label317" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label318' href="javascript:ContentClick('label319', 'label318');" onmouseover="ContentPreview('label319');" onmouseout="ContentUnpreview('label319');" title="click to collapse or expand..."> more... </a>
 <div id="label319" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label320' href="javascript:ContentClick('label321', 'label320');" onmouseover="ContentPreview('label321');" onmouseout="ContentUnpreview('label321');" title="click to collapse or expand..."> more... </a>
 <div id="label321" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable sftp and scp antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [avmonitor, quarantine, scan]</span> 
 <a id='label322' href="javascript:ContentClick('label323', 'label322');" onmouseover="ContentPreview('label323');" onmouseout="ContentUnpreview('label323');" title="click to collapse or expand..."> more... </a>
 <div id="label323" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> 
 <a id='label324' href="javascript:ContentClick('label325', 'label324');" onmouseover="ContentPreview('label325');" onmouseout="ContentUnpreview('label325');" title="click to collapse or expand..."> more... </a>
 <div id="label325" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_scan</span> <b>(Alias name: av-scan)</b>  Enable antivirus scan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label326' href="javascript:ContentClick('label327', 'label326');" onmouseover="ContentPreview('label327');" onmouseout="ContentUnpreview('label327');" title="click to collapse or expand..."> more... </a>
 <div id="label327" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  Enable external-blocklist. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label328' href="javascript:ContentClick('label329', 'label328');" onmouseover="ContentPreview('label329');" onmouseout="ContentUnpreview('label329');" title="click to collapse or expand..."> more... </a>
 <div id="label329" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable quarantine for infected files. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label330' href="javascript:ContentClick('label331', 'label330');" onmouseover="ContentPreview('label331');" onmouseout="ContentUnpreview('label331');" title="click to collapse or expand..."> more... </a>
 <div id="label331" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr</span> Enable scanning of files by fortindr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label332' href="javascript:ContentClick('label333', 'label332');" onmouseover="ContentPreview('label333');" onmouseout="ContentUnpreview('label333');" title="click to collapse or expand..."> more... </a>
 <div id="label333" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox</span> Enable scanning of files by fortisandbox. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label334' href="javascript:ContentClick('label335', 'label334');" onmouseover="ContentPreview('label335');" onmouseout="ContentUnpreview('label335');" title="click to collapse or expand..."> more... </a>
 <div id="label335" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai</span> Enable/disable scanning of files by fortiai. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label336' href="javascript:ContentClick('label337', 'label336');" onmouseover="ContentPreview('label337');" onmouseout="ContentUnpreview('label337');" title="click to collapse or expand..."> more... </a>
 <div id="label337" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malware_stream</span> <b>(Alias name: malware-stream)</b>  Enable 0-day malware-stream scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, monitor, block]</span> 
 <a id='label338' href="javascript:ContentClick('label339', 'label338');" onmouseover="ContentPreview('label339');" onmouseout="ContentUnpreview('label339');" title="click to collapse or expand..."> more... </a>
 <div id="label339" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">smb</span> Smb. <span class="li-normal">type: dict</span>
 <a id='label340' href="javascript:ContentClick('label341', 'label340');" onmouseover="ContentPreview('label341');" onmouseout="ContentUnpreview('label341');" title="click to collapse or expand..."> more... </a>
 <div id="label341" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> v7.2.1</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">archive_block</span> <b>(Alias name: archive-block)</b>  Select the archive types to block. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label342' href="javascript:ContentClick('label343', 'label342');" onmouseover="ContentPreview('label343');" onmouseout="ContentUnpreview('label343');" title="click to collapse or expand..."> more... </a>
 <div id="label343" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> v7.2.1</code></p>
 </div>
 </li>
 <li><span class="li-head">archive_log</span> <b>(Alias name: archive-log)</b>  Select the archive types to log. <span class="li-normal">type: list</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> 
 <a id='label344' href="javascript:ContentClick('label345', 'label344');" onmouseover="ContentPreview('label345');" onmouseout="ContentUnpreview('label345');" title="click to collapse or expand..."> more... </a>
 <div id="label345" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> v7.2.1</code></p>
 </div>
 </li>
 <li><span class="li-head">emulator</span> Enable/disable the virus emulator. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label346' href="javascript:ContentClick('label347', 'label346');" onmouseover="ContentPreview('label347');" onmouseout="ContentUnpreview('label347');" title="click to collapse or expand..."> more... </a>
 <div id="label347" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> v7.2.1</code></p>
 </div>
 </li>
 <li><span class="li-head">options</span> Enable/disable smb antivirus scanning, monitoring, and quarantine. <span class="li-normal">type: list</span> <span class="li-normal">choices: [scan, quarantine, avquery, avmonitor]</span> 
 <a id='label348' href="javascript:ContentClick('label349', 'label348');" onmouseover="ContentPreview('label349');" onmouseout="ContentUnpreview('label349');" title="click to collapse or expand..."> more... </a>
 <div id="label349" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> v7.2.1</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention</span> <b>(Alias name: outbreak-prevention)</b>  Enable fortiguard virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, files, full-archive]</span> 
 <a id='label350' href="javascript:ContentClick('label351', 'label350');" onmouseover="ContentPreview('label351');" onmouseout="ContentUnpreview('label351');" title="click to collapse or expand..."> more... </a>
 <div id="label351" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> v7.2.1</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">analytics_accept_filetype</span> <b>(Alias name: analytics-accept-filetype)</b>  Only submit files matching this dlp file-pattern to fortisandbox. <span class="li-normal">type: str</span>
 <a id='label352' href="javascript:ContentClick('label353', 'label352');" onmouseover="ContentPreview('label353');" onmouseout="ContentUnpreview('label353');" title="click to collapse or expand..."> more... </a>
 <div id="label353" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">analytics_ignore_filetype</span> <b>(Alias name: analytics-ignore-filetype)</b>  Do not submit files matching this dlp file-pattern to fortisandbox. <span class="li-normal">type: str</span>
 <a id='label354' href="javascript:ContentClick('label355', 'label354');" onmouseover="ContentPreview('label355');" onmouseout="ContentUnpreview('label355');" title="click to collapse or expand..."> more... </a>
 <div id="label355" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ems_threat_feed</span> <b>(Alias name: ems-threat-feed)</b>  Enable/disable use of ems threat feed when performing antivirus scan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label356' href="javascript:ContentClick('label357', 'label356');" onmouseover="ContentPreview('label357');" onmouseout="ContentUnpreview('label357');" title="click to collapse or expand..."> more... </a>
 <div id="label357" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist</span> <b>(Alias name: external-blocklist)</b>  One or more external malware block lists. <span class="li-normal">type: list or str</span>
 <a id='label358' href="javascript:ContentClick('label359', 'label358');" onmouseover="ContentPreview('label359');" onmouseout="ContentUnpreview('label359');" title="click to collapse or expand..."> more... </a>
 <div id="label359" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist_archive_scan</span> <b>(Alias name: external-blocklist-archive-scan)</b>  Enable/disable external-blocklist archive scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label360' href="javascript:ContentClick('label361', 'label360');" onmouseover="ContentPreview('label361');" onmouseout="ContentUnpreview('label361');" title="click to collapse or expand..."> more... </a>
 <div id="label361" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_blocklist_enable_all</span> <b>(Alias name: external-blocklist-enable-all)</b>  Enable/disable all external blocklists. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label362' href="javascript:ContentClick('label363', 'label362');" onmouseover="ContentPreview('label363');" onmouseout="ContentUnpreview('label363');" title="click to collapse or expand..."> more... </a>
 <div id="label363" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_archive_scan</span> <b>(Alias name: outbreak-prevention-archive-scan)</b>  Enable/disable outbreak-prevention archive scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label364' href="javascript:ContentClick('label365', 'label364');" onmouseover="ContentPreview('label365');" onmouseout="ContentUnpreview('label365');" title="click to collapse or expand..."> more... </a>
 <div id="label365" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr_error_action</span> <b>(Alias name: fortindr-error-action)</b>  Action to take if fortindr encounters an error. <span class="li-normal">type: str</span> <span class="li-normal">choices: [log-only, block, ignore]</span> 
 <a id='label366' href="javascript:ContentClick('label367', 'label366');" onmouseover="ContentPreview('label367');" onmouseout="ContentUnpreview('label367');" title="click to collapse or expand..."> more... </a>
 <div id="label367" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortindr_timeout_action</span> <b>(Alias name: fortindr-timeout-action)</b>  Action to take if fortindr encounters a scan timeout. <span class="li-normal">type: str</span> <span class="li-normal">choices: [log-only, block, ignore]</span> 
 <a id='label368' href="javascript:ContentClick('label369', 'label368');" onmouseover="ContentPreview('label369');" onmouseout="ContentUnpreview('label369');" title="click to collapse or expand..."> more... </a>
 <div id="label369" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox_error_action</span> <b>(Alias name: fortisandbox-error-action)</b>  Action to take if fortisandbox inline scan encounters an error. <span class="li-normal">type: str</span> <span class="li-normal">choices: [log-only, block, ignore]</span> 
 <a id='label370' href="javascript:ContentClick('label371', 'label370');" onmouseover="ContentPreview('label371');" onmouseout="ContentUnpreview('label371');" title="click to collapse or expand..."> more... </a>
 <div id="label371" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox_max_upload</span> <b>(Alias name: fortisandbox-max-upload)</b>  Maximum size of files that can be uploaded to fortisandbox. <span class="li-normal">type: int</span>
 <a id='label372' href="javascript:ContentClick('label373', 'label372');" onmouseover="ContentPreview('label373');" onmouseout="ContentUnpreview('label373');" title="click to collapse or expand..."> more... </a>
 <div id="label373" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox_mode</span> <b>(Alias name: fortisandbox-mode)</b>  Fortisandbox scan modes. <span class="li-normal">type: str</span> <span class="li-normal">choices: [inline, analytics-suspicious, analytics-everything]</span> 
 <a id='label374' href="javascript:ContentClick('label375', 'label374');" onmouseover="ContentPreview('label375');" onmouseout="ContentUnpreview('label375');" title="click to collapse or expand..."> more... </a>
 <div id="label375" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortisandbox_timeout_action</span> <b>(Alias name: fortisandbox-timeout-action)</b>  Action to take if fortisandbox inline scan encounters a scan timeout. <span class="li-normal">type: str</span> <span class="li-normal">choices: [log-only, block, ignore]</span> 
 <a id='label376' href="javascript:ContentClick('label377', 'label376');" onmouseover="ContentPreview('label377');" onmouseout="ContentUnpreview('label377');" title="click to collapse or expand..."> more... </a>
 <div id="label377" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai_error_action</span> <b>(Alias name: fortiai-error-action)</b>  Action to take if fortiai encounters an error. <span class="li-normal">type: str</span> <span class="li-normal">choices: [block, log-only, ignore]</span> 
 <a id='label378' href="javascript:ContentClick('label379', 'label378');" onmouseover="ContentPreview('label379');" onmouseout="ContentUnpreview('label379');" title="click to collapse or expand..."> more... </a>
 <div id="label379" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiai_timeout_action</span> <b>(Alias name: fortiai-timeout-action)</b>  Action to take if fortiai encounters a scan timeout. <span class="li-normal">type: str</span> <span class="li-normal">choices: [block, log-only, ignore]</span> 
 <a id='label380' href="javascript:ContentClick('label381', 'label380');" onmouseover="ContentPreview('label381');" onmouseout="ContentUnpreview('label381');" title="click to collapse or expand..."> more... </a>
 <div id="label381" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
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
      - name: Configure AntiVirus profiles.
        fortinet.fortimanager.fmgr_antivirus_profile:
          adom: ansible
          state: present
          antivirus_profile:
            analytics-db: disable
            analytics-max-upload: 20
            av-block-log: disable
            av-virus-log: disable
            comment: "test comment"
            extended-log: disable
            ftgd-analytics: disable
            inspection-mode: proxy
            mobile-malware-db: disable
            name: "antivirus-profile"
            scan-mode: quick
  
  - name: Gathering fortimanager facts
    hosts: fortimanagers
    gather_facts: false
    connection: httpapi
    vars:
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_httpapi_port: 443
    tasks:
      - name: Retrieve all the antivirus profiles
        fortinet.fortimanager.fmgr_fact:
          facts:
            selector: "antivirus_profile"
            params:
              adom: "ansible"
              profile: "your_value"


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
