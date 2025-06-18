:source: fmgr_fmupdate_webspam_fgdsetting.py

:orphan:

.. _fmgr_fmupdate_webspam_fgdsetting:

fmgr_fmupdate_webspam_fgdsetting -- Configure the FortiGuard run parameters.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">fmupdate_webspam_fgdsetting</span> - Configure the FortiGuard run parameters. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">as_cache</span> <b>(Alias name: as-cache)</b>  Antispam service maximum memory usage in megabytes (maximum = physical memory-1024, 0: no limit, default = 300). <span class="li-normal">type: int</span> <span class="li-normal">default: 300</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">as_log</span> <b>(Alias name: as-log)</b>  Antispam log setting (default = nospam). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, nospam, all]</span>  <span class="li-normal">default: nospam</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">as_preload</span> <b>(Alias name: as-preload)</b>  Enable/disable preloading antispam database to memory (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">av_cache</span> <b>(Alias name: av-cache)</b>  Antivirus service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span> <span class="li-normal">default: 300</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">av_log</span> <b>(Alias name: av-log)</b>  Antivirus log setting (default = novirus). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, novirus, all]</span>  <span class="li-normal">default: novirus</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">av_preload</span> <b>(Alias name: av-preload)</b>  Enable/disable preloading antivirus database to memory (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">av2_cache</span> <b>(Alias name: av2-cache)</b>  Antispam service maximum memory usage in megabytes (maximum = physical memory-1024, 0: no limit, default = 800). <span class="li-normal">type: int</span> <span class="li-normal">default: 800</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">av2_log</span> <b>(Alias name: av2-log)</b>  Outbreak prevention log setting (default = noav2). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, noav2, all]</span>  <span class="li-normal">default: noav2</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">av2_preload</span> <b>(Alias name: av2-preload)</b>  Enable/disable preloading outbreak prevention database to memory (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">eventlog_query</span> <b>(Alias name: eventlog-query)</b>  Enable/disable record query to event-log besides fgd-log (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">fgd_pull_interval</span> <b>(Alias name: fgd-pull-interval)</b>  Fgd pull interval setting, in minutes (1 - 1440, default = 10). <span class="li-normal">type: int</span> <span class="li-normal">default: 10</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">fq_cache</span> <b>(Alias name: fq-cache)</b>  File query service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span> <span class="li-normal">default: 300</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">fq_log</span> <b>(Alias name: fq-log)</b>  File query log setting (default = nofilequery). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, nofilequery, all]</span>  <span class="li-normal">default: nofilequery</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">fq_preload</span> <b>(Alias name: fq-preload)</b>  Enable/disable preloading file query database to memory (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">linkd_log</span> <b>(Alias name: linkd-log)</b>  Linkd log setting (default = debug). <span class="li-normal">type: str</span> <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: debug</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">max_client_worker</span> <b>(Alias name: max-client-worker)</b>  Max worker for tcp client connection (0~16: 0 means use cpu number up to 4). <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">max_log_quota</span> <b>(Alias name: max-log-quota)</b>  Maximum log quota setting, in megabytes (100 - 20480, default = 6144). <span class="li-normal">type: int</span> <span class="li-normal">default: 6144</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">max_unrated_site</span> <b>(Alias name: max-unrated-site)</b>  Maximum number of unrated site in memory, in kilobytes(10 - 5120, default = 500). <span class="li-normal">type: int</span> <span class="li-normal">default: 500</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_as1_dbver</span> <b>(Alias name: restrict-as1-dbver)</b>  Restrict system update to indicated antispam(1) database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_as2_dbver</span> <b>(Alias name: restrict-as2-dbver)</b>  Restrict system update to indicated antispam(2) database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_as4_dbver</span> <b>(Alias name: restrict-as4-dbver)</b>  Restrict system update to indicated antispam(4) database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_av_dbver</span> <b>(Alias name: restrict-av-dbver)</b>  Restrict system update to indicated antivirus database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_av2_dbver</span> <b>(Alias name: restrict-av2-dbver)</b>  Restrict system update to indicated outbreak prevention database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_fq_dbver</span> <b>(Alias name: restrict-fq-dbver)</b>  Restrict system update to indicated file query database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_wf_dbver</span> <b>(Alias name: restrict-wf-dbver)</b>  Restrict system update to indicated web filter database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">server_override</span> <b>(Alias name: server-override)</b>  Server override. <span class="li-normal">type: dict</span>
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">servlist</span> Servlist. <span class="li-normal">type: list</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> Override server id (1 - 10). <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ipv4 address of the override server. <span class="li-normal">type: str</span> <span class="li-normal">default: 0.0.0.0</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6</span> Ipv6 address of the override server. <span class="li-normal">type: str</span> <span class="li-normal">default: ::</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Port number to use when contacting fortiguard (1 - 65535, default = 443). <span class="li-normal">type: int</span> <span class="li-normal">default: 443</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">service_type</span> <b>(Alias name: service-type)</b>  Override service type. <span class="li-normal">type: list or str</span> <span class="li-normal">choices: [fgd, fgc, fsa, fgfq, geoip, iot-collect]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">status</span> Override status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">stat_log_interval</span> <b>(Alias name: stat-log-interval)</b>  Statistic log interval setting, in minutes (1 - 1440, default = 60). <span class="li-normal">type: int</span> <span class="li-normal">default: 60</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">stat_sync_interval</span> <b>(Alias name: stat-sync-interval)</b>  Synchronization interval for statistic of unrated site in minutes (1 - 60, default = 60). <span class="li-normal">type: int</span> <span class="li-normal">default: 60</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">update_interval</span> <b>(Alias name: update-interval)</b>  Fortiguard database update wait time if not enough delta files, in hours (2 - 24, default = 6). <span class="li-normal">type: int</span> <span class="li-normal">default: 6</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">update_log</span> <b>(Alias name: update-log)</b>  Enable/disable update log setting (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">wf_cache</span> <b>(Alias name: wf-cache)</b>  Web filter service maximum memory usage, in megabytes (maximum = physical memory-1024, 0 = no limit, default = 600). <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">wf_dn_cache_expire_time</span> <b>(Alias name: wf-dn-cache-expire-time)</b>  Web filter dn cache expire time, in minutes (1 - 1440, 0 = never, default = 30). <span class="li-normal">type: int</span> <span class="li-normal">default: 30</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">wf_dn_cache_max_number</span> <b>(Alias name: wf-dn-cache-max-number)</b>  Maximum number of web filter dn cache (0 = disable, default = 10000). <span class="li-normal">type: int</span> <span class="li-normal">default: 10000</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">wf_log</span> <b>(Alias name: wf-log)</b>  Web filter log setting (default = nour1) <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, nourl, all]</span>  <span class="li-normal">default: nourl</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">wf_preload</span> <b>(Alias name: wf-preload)</b>  Enable/disable preloading the web filter database into memory (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">iot_cache</span> <b>(Alias name: iot-cache)</b>  Iot service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span> <span class="li-normal">default: 300</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.1 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">iot_log</span> <b>(Alias name: iot-log)</b>  Iot log setting (default = nofilequery). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, nofilequery, all, noiot]</span>  <span class="li-normal">default: nofilequery</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.1 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">iot_preload</span> <b>(Alias name: iot-preload)</b>  Enable/disable preloading iot database to memory (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.1 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">restrict_iots_dbver</span> <b>(Alias name: restrict-iots-dbver)</b>  Restrict system update to indicated file query database version (character limit = 127). <span class="li-normal">type: str</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.1 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">stat_log</span> <b>(Alias name: stat-log)</b>  Stat log setting (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.10 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.2 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">iotv_preload</span> <b>(Alias name: iotv-preload)</b>  Enable/disable preloading iot-vulnerability database to memory (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> v7.6.2</code></p>
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
      - name: Configure the FortiGuard run parameters.
        fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          fmupdate_webspam_fgdsetting:
            # as_cache: <integer>
            # as_log: <value in [disable, nospam, all]>
            # as_preload: <value in [disable, enable]>
            # av_cache: <integer>
            # av_log: <value in [disable, novirus, all]>
            # av_preload: <value in [disable, enable]>
            # av2_cache: <integer>
            # av2_log: <value in [disable, noav2, all]>
            # av2_preload: <value in [disable, enable]>
            # eventlog_query: <value in [disable, enable]>
            # fgd_pull_interval: <integer>
            # fq_cache: <integer>
            # fq_log: <value in [disable, nofilequery, all]>
            # fq_preload: <value in [disable, enable]>
            # linkd_log: <value in [emergency, alert, critical, ...]>
            # max_client_worker: <integer>
            # max_log_quota: <integer>
            # max_unrated_site: <integer>
            # restrict_as1_dbver: <string>
            # restrict_as2_dbver: <string>
            # restrict_as4_dbver: <string>
            # restrict_av_dbver: <string>
            # restrict_av2_dbver: <string>
            # restrict_fq_dbver: <string>
            # restrict_wf_dbver: <string>
            # server_override:
            #   servlist:
            #     - id: <integer>
            #       ip: <string>
            #       ip6: <string>
            #       port: <integer>
            #       service_type: # <list or string>
            #         - "fgd"
            #         - "fgc"
            #         - "fsa"
            #         - "fgfq"
            #         - "geoip"
            #         - "iot-collect"
            #   status: <value in [disable, enable]>
            # stat_log_interval: <integer>
            # stat_sync_interval: <integer>
            # update_interval: <integer>
            # update_log: <value in [disable, enable]>
            # wf_cache: <integer>
            # wf_dn_cache_expire_time: <integer>
            # wf_dn_cache_max_number: <integer>
            # wf_log: <value in [disable, nourl, all]>
            # wf_preload: <value in [disable, enable]>
            # iot_cache: <integer>
            # iot_log: <value in [disable, nofilequery, all, ...]>
            # iot_preload: <value in [disable, enable]>
            # restrict_iots_dbver: <string>
            # stat_log: <value in [emergency, alert, critical, ...]>
            # iotv_preload: <value in [disable, enable]>


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
