:source: fmgr_fmupdate_fdssetting.py

:orphan:

.. _fmgr_fmupdate_fdssetting:

fmgr_fmupdate_fdssetting -- Configure FortiGuard settings.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
- Tested with FortiManager v6.x and v7.x.


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
 <li><span class="li-head">fmupdate_fdssetting</span> - Configure FortiGuard settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">User_Agent</span> <b>(Alias name: User-Agent)</b>  Configure the user agent string. <span class="li-normal">type: str</span> <span class="li-normal">default: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fds_clt_ssl_protocol</span> <b>(Alias name: fds-clt-ssl-protocol)</b>  The ssl protocols version for connecting fds server (default = tlsv1. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span>  <span class="li-normal">default: tlsv1.2</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fds_ssl_protocol</span> <b>(Alias name: fds-ssl-protocol)</b>  The ssl protocols version for receiving fgt connection (default = tlsv1. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span>  <span class="li-normal">default: tlsv1.2</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fmtr_log</span> <b>(Alias name: fmtr-log)</b>  Fmtr log level <span class="li-normal">type: str</span> <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">linkd_log</span> <b>(Alias name: linkd-log)</b>  The linkd log level (default = info). <span class="li-normal">type: str</span> <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_av_ips_version</span> <b>(Alias name: max-av-ips-version)</b>  The maximum number of downloadable, full version av/ips packages (1 - 1000, default = 20). <span class="li-normal">type: int</span> <span class="li-normal">default: 20</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_work</span> <b>(Alias name: max-work)</b>  The maximum number of worker processing download requests (1 - 32, default = 1). <span class="li-normal">type: int</span> <span class="li-normal">default: 1</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">push_override</span> <b>(Alias name: push-override)</b>  <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> External or virtual ip address of the nat device that will forward push messages to the fortimanager unit. <span class="li-normal">type: str</span> <span class="li-normal">default: 0.0.0.0</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Receiving port number on the nat device (1 - 65535, default = 9443). <span class="li-normal">type: int</span> <span class="li-normal">default: 9443</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable/disable push updates for clients (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">push_override_to_client</span> <b>(Alias name: push-override-to-client)</b>  <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">announce_ip</span> <b>(Alias name: announce-ip)</b>  Announce-ip. <span class="li-normal">type: list</span>
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> Id of the announce ip address (1 - 10). <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Announce ipv4 address. <span class="li-normal">type: str</span> <span class="li-normal">default: 0.0.0.0</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Announce ip port (1 - 65535, default = 8890). <span class="li-normal">type: int</span> <span class="li-normal">default: 8890</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">status</span> Enable/disable push updates (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">send_report</span> Send report/fssi to fds server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">send_setup</span> Forward setup to fds server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">server_override</span> <b>(Alias name: server-override)</b>  <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">servlist</span> Servlist. <span class="li-normal">type: list</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> Override server id (1 - 10). <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ipv4 address of the override server. <span class="li-normal">type: str</span> <span class="li-normal">default: 0.0.0.0</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6</span> Ipv6 address of the override server. <span class="li-normal">type: str</span> <span class="li-normal">default: ::</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Port number to use when contacting fortiguard (1 - 65535, default = 443). <span class="li-normal">type: int</span> <span class="li-normal">default: 443</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">service_type</span> <b>(Alias name: service-type)</b>  Override service type. <span class="li-normal">type: list or str</span> <span class="li-normal">choices: [fds, fct]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">status</span> Override status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">system_support_fct</span> <b>(Alias name: system-support-fct)</b>  Supported forticlient versions. <span class="li-normal">type: list</span> <span class="li-normal">choices: [4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 6.4, 7.0, 7.2]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_fgt</span> <b>(Alias name: system-support-fgt)</b>  Supported fortios versions. <span class="li-normal">type: list</span> <span class="li-normal">choices: [5.4, 5.6, 6.0, 6.2, 6.4, 7.0, 7.2, 7.4]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_fml</span> <b>(Alias name: system-support-fml)</b>  Supported fortimail versions. <span class="li-normal">type: list</span> <span class="li-normal">choices: [4.x, 5.x, 6.x, 6.0, 6.2, 6.4, 7.0, 7.2, 7.x]</span> 
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_fsa</span> <b>(Alias name: system-support-fsa)</b>  Supported fortisandbox versions. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1.x, 2.x, 3.x, 4.x, 3.0, 3.1, 3.2]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_fsw</span> <b>(Alias name: system-support-fsw)</b>  Supported fortiswitch versions. <span class="li-normal">type: list</span> <span class="li-normal">choices: [5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 6.4]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.4.5</code>, <code class="docutils literal notranslate">v7.0.0 -> v7.0.0</code></p>
 </div>
 </li>
 <li><span class="li-head">umsvc_log</span> <b>(Alias name: umsvc-log)</b>  The um_service log level (default = info). <span class="li-normal">type: str</span> <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">unreg_dev_option</span> <b>(Alias name: unreg-dev-option)</b>  Set the option for unregister devices <span class="li-normal">type: str</span> <span class="li-normal">choices: [ignore, svc-only, add-service]</span>  <span class="li-normal">default: add-service</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_schedule</span> <b>(Alias name: update-schedule)</b>  <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">day</span> Configure the day the update will occur, if the freqnecy is weekly (sunday - saturday, default = monday). <span class="li-normal">type: str</span> <span class="li-normal">choices: [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]</span>  <span class="li-normal">default: Monday</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">frequency</span> Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every). <span class="li-normal">type: str</span> <span class="li-normal">choices: [every, daily, weekly]</span>  <span class="li-normal">default: every</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable/disable scheduled updates. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">time</span> Time interval between updates, or the hour and minute when the update occurs (hh: 0 - 23, mm: 0 - 59 or 60 = random, default = 00:10). <span class="li-normal">type: list</span>
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">wanip_query_mode</span> <b>(Alias name: wanip-query-mode)</b>  Public ip query mode <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, ipify]</span>  <span class="li-normal">default: disable</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiguard_anycast</span> <b>(Alias name: fortiguard-anycast)</b>  Enable/disable use of fortiguards anycast network <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiguard_anycast_source</span> <b>(Alias name: fortiguard-anycast-source)</b>  Configure which of fortinets servers to provide fortiguard services in fortiguards anycast network. <span class="li-normal">type: str</span> <span class="li-normal">choices: [fortinet, aws]</span>  <span class="li-normal">default: fortinet</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_fdc</span> <b>(Alias name: system-support-fdc)</b>  <span class="li-normal">type: list</span> <span class="li-normal">choices: [3.x, 4.x]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> v6.4.14</code>, <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_fts</span> <b>(Alias name: system-support-fts)</b>  <span class="li-normal">type: list</span> <span class="li-normal">choices: [3.x, 4.x, 7.x]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> v6.4.14</code>, <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_faz</span> <b>(Alias name: system-support-faz)</b>  <span class="li-normal">type: list</span> <span class="li-normal">choices: [6.x, 7.x]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.7 -> v7.0.12</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_support_fis</span> <b>(Alias name: system-support-fis)</b>  <span class="li-normal">type: list</span> <span class="li-normal">choices: [1.x, 2.x]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
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
    vars:
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_httpapi_port: 443
    tasks:
      - name: Configure FortiGuard settings.
        fortinet.fortimanager.fmgr_fmupdate_fdssetting:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          fmupdate_fdssetting:
            User_Agent: <string>
            fds_clt_ssl_protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
            fds_ssl_protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
            fmtr_log: <value in [emergency, alert, critical, ...]>
            linkd_log: <value in [emergency, alert, critical, ...]>
            max_av_ips_version: <integer>
            max_work: <integer>
            push_override:
              ip: <string>
              port: <integer>
              status: <value in [disable, enable]>
            push_override_to_client:
              announce_ip:
                -
                  id: <integer>
                  ip: <string>
                  port: <integer>
              status: <value in [disable, enable]>
            send_report: <value in [disable, enable]>
            send_setup: <value in [disable, enable]>
            server_override:
              servlist:
                -
                  id: <integer>
                  ip: <string>
                  ip6: <string>
                  port: <integer>
                  service_type: # <list or string>
                    - fds
                    - fct
              status: <value in [disable, enable]>
            system_support_fct:
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 7.0
              - 7.2
            system_support_fgt:
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 7.0
              - 7.2
              - 7.4
            system_support_fml:
              - 4.x
              - 5.x
              - 6.x
              - 6.0
              - 6.2
              - 6.4
              - 7.0
              - 7.2
              - 7.x
            system_support_fsa:
              - 1.x
              - 2.x
              - 3.x
              - 4.x
              - 3.0
              - 3.1
              - 3.2
            system_support_fsw:
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 6.4
            umsvc_log: <value in [emergency, alert, critical, ...]>
            unreg_dev_option: <value in [ignore, svc-only, add-service]>
            update_schedule:
              day: <value in [Sunday, Monday, Tuesday, ...]>
              frequency: <value in [every, daily, weekly]>
              status: <value in [disable, enable]>
              time: <list or string>
            wanip_query_mode: <value in [disable, ipify]>
            fortiguard_anycast: <value in [disable, enable]>
            fortiguard_anycast_source: <value in [fortinet, aws]>
            system_support_fdc:
              - 3.x
              - 4.x
            system_support_fts:
              - 3.x
              - 4.x
              - 7.x
            system_support_faz:
              - 6.x
              - 7.x
            system_support_fis:
              - 1.x
              - 2.x


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
