:source: fmgr_devprof_system_global.py

:orphan:

.. _fmgr_devprof_system_global:

fmgr_devprof_system_global -- Configure global attributes.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>



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
 <li><span class="li-head">devprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof_system_global</span> - Configure global attributes. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">admin_https_redirect</span> <b>(Alias name: admin-https-redirect)</b>  Enable/disable redirection of http administration access to https. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_port</span> <b>(Alias name: admin-port)</b>  Administrative access port for http. <span class="li-normal">type: int</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_scp</span> <b>(Alias name: admin-scp)</b>  Enable/disable using scp to download the system configuration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_sport</span> <b>(Alias name: admin-sport)</b>  Administrative access port for https. <span class="li-normal">type: int</span>
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_ssh_port</span> <b>(Alias name: admin-ssh-port)</b>  Administrative access port for ssh. <span class="li-normal">type: int</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_ssh_v1</span> <b>(Alias name: admin-ssh-v1)</b>  Enable/disable ssh v1 compatibility. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_telnet_port</span> <b>(Alias name: admin-telnet-port)</b>  Administrative access port for telnet. <span class="li-normal">type: int</span>
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> v7.2.4</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.1</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admintimeout</span> Number of minutes before an idle administrator session times out (5 - 480 minutes (8 hours), default = 5). <span class="li-normal">type: int</span>
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_ipv6</span> <b>(Alias name: gui-ipv6)</b>  Enable/disable ipv6 settings on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_lines_per_page</span> <b>(Alias name: gui-lines-per-page)</b>  Number of lines to display per page for web administration. <span class="li-normal">type: int</span>
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_theme</span> <b>(Alias name: gui-theme)</b>  Color scheme for the administration gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [blue, green, melongene, red, mariner, neutrino, jade, graphite, dark-matter, onyx, eclipse, retro, fpx, jet-stream, security-fabric]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">language</span> Gui display language. <span class="li-normal">type: str</span> <span class="li-normal">choices: [english, simch, japanese, korean, spanish, trach, french, portuguese]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller</span> <b>(Alias name: switch-controller)</b>  Enable/disable switch controller feature. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.5</code>, <code class="docutils literal notranslate">v6.2.7 -> v6.4.1</code>, <code class="docutils literal notranslate">v6.4.3 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_device_latitude</span> <b>(Alias name: gui-device-latitude)</b>  Support meta variable <span class="li-normal">type: str</span>
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_device_longitude</span> <b>(Alias name: gui-device-longitude)</b>  Support meta variable <span class="li-normal">type: str</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hostname</span> Support meta variable <span class="li-normal">type: str</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">timezone</span> Support meta variable <span class="li-normal">type: list</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">check_reset_range</span> <b>(Alias name: check-reset-range)</b>  Configure icmp error message verification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, strict]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pmtu_discovery</span> <b>(Alias name: pmtu-discovery)</b>  Enable/disable path mtu discovery. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_allow_incompatible_fabric_fgt</span> <b>(Alias name: gui-allow-incompatible-fabric-fgt)</b>  Enable/disable allow fgt with incompatible firmware to be treated as compatible in security fabric on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_restrict_local</span> <b>(Alias name: admin-restrict-local)</b>  Enable/disable local admin authentication restriction when remote authenticator is up and running (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_workflow_management</span> <b>(Alias name: gui-workflow-management)</b>  Enable/disable workflow management features on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">send_pmtu_icmp</span> <b>(Alias name: send-pmtu-icmp)</b>  Enable/disable sending of path maximum transmission unit (pmtu) - icmp destination unreachable packet and to support pmtud protocol on your network to reduce fragmentation of packets. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_halfclose_timer</span> <b>(Alias name: tcp-halfclose-timer)</b>  Number of seconds the fortigate unit should wait to close a session after one peer has sent a fin packet but the other has not responded (1 - 86400 sec (1 day), default = 120). <span class="li-normal">type: int</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_server_cert</span> <b>(Alias name: admin-server-cert)</b>  Server certificate that the fortigate uses for https administrative connections. <span class="li-normal">type: list</span>
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dnsproxy_worker_count</span> <b>(Alias name: dnsproxy-worker-count)</b>  Dns proxy worker count. <span class="li-normal">type: int</span>
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">show_backplane_intf</span> <b>(Alias name: show-backplane-intf)</b>  Show/hide backplane interfaces <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_custom_language</span> <b>(Alias name: gui-custom-language)</b>  Enable/disable custom languages in gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldapconntimeout</span> Global timeout for connections with remote ldap servers in milliseconds (1 - 300000, default 500). <span class="li-normal">type: int</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_https_port</span> <b>(Alias name: auth-https-port)</b>  User authentication https port. <span class="li-normal">type: int</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">revision_backup_on_logout</span> <b>(Alias name: revision-backup-on-logout)</b>  Enable/disable back-up of the latest configuration revision when an administrator logs out of the cli or gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">arp_max_entry</span> <b>(Alias name: arp-max-entry)</b>  Maximum number of dynamically learned mac addresses that can be added to the arp table (131072 - 2147483647, default = 131072). <span class="li-normal">type: int</span>
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">long_vdom_name</span> <b>(Alias name: long-vdom-name)</b>  Enable/disable long vdom name support. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pre_login_banner</span> <b>(Alias name: pre-login-banner)</b>  Enable/disable displaying the administrator access disclaimer message on the login page before an administrator logs in. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qsfpdd_split8_port</span> <b>(Alias name: qsfpdd-split8-port)</b>  Split qsfpddd port(s) as 8 ports <span class="li-normal">type: list</span>
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_route_cache_size</span> <b>(Alias name: max-route-cache-size)</b>  Maximum number of ip route cache entries (0 - 2147483647). <span class="li-normal">type: int</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortitoken_cloud_push_status</span> <b>(Alias name: fortitoken-cloud-push-status)</b>  Enable/disable ftm push service of fortitoken cloud. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_hostkey_override</span> <b>(Alias name: ssh-hostkey-override)</b>  Enable/disable ssh host key override in ssh daemon. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_hardware_acceleration</span> <b>(Alias name: proxy-hardware-acceleration)</b>  Enable/disable email proxy hardware acceleration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_reserved_network</span> <b>(Alias name: switch-controller-reserved-network)</b>  Configure reserved network subnet for managed switches. <span class="li-normal">type: list</span>
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssd_trim_date</span> <b>(Alias name: ssd-trim-date)</b>  Date within a month to run ssd trim. <span class="li-normal">type: int</span>
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_worker_count</span> <b>(Alias name: wad-worker-count)</b>  Number of explicit proxy wan optimization daemon (wad) processes. <span class="li-normal">type: int</span>
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_hostkey</span> <b>(Alias name: ssh-hostkey)</b>  Config ssh host key. <span class="li-normal">type: str</span>
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wireless_controller_port</span> <b>(Alias name: wireless-controller-port)</b>  Port used for the control channel in wireless controller mode (wireless-mode is ac). <span class="li-normal">type: int</span>
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgd_alert_subscription</span> <b>(Alias name: fgd-alert-subscription)</b>  Type of alert to retrieve from fortiguard. <span class="li-normal">type: list</span> <span class="li-normal">choices: [advisory, latest-threat, latest-virus, latest-attack, new-antivirus-db, new-attack-db]</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forticontroller_proxy_port</span> <b>(Alias name: forticontroller-proxy-port)</b>  Forticontroller proxy port (1024 - 49150). <span class="li-normal">type: int</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dh_params</span> <b>(Alias name: dh-params)</b>  Number of bits to use in the diffie-hellman exchange for https/ssh protocols. <span class="li-normal">type: str</span> <span class="li-normal">choices: [1024, 1536, 2048, 3072, 4096, 6144, 8192]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">memory_use_threshold_green</span> <b>(Alias name: memory-use-threshold-green)</b>  Threshold at which memory usage forces the fortigate to exit conserve mode (% of total ram, default = 82). <span class="li-normal">type: int</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_cert_use_mgmt_vdom</span> <b>(Alias name: proxy-cert-use-mgmt-vdom)</b>  Enable/disable using management vdom to send requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_auth_lifetime_timeout</span> <b>(Alias name: proxy-auth-lifetime-timeout)</b>  Lifetime timeout in minutes for authenticated users (5  - 65535 min, default=480 (8 hours)). <span class="li-normal">type: int</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_auto_upgrade_setup_warning</span> <b>(Alias name: gui-auto-upgrade-setup-warning)</b>  Enable/disable the automatic patch upgrade setup prompt on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_cdn_usage</span> <b>(Alias name: gui-cdn-usage)</b>  Enable/disable load gui static files from a cdn. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">two_factor_email_expiry</span> <b>(Alias name: two-factor-email-expiry)</b>  Email-based two-factor authentication session timeout (30 - 300 seconds (5 minutes), default = 60). <span class="li-normal">type: int</span>
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">udp_idle_timer</span> <b>(Alias name: udp-idle-timer)</b>  Udp connection session timeout. <span class="li-normal">type: int</span>
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">interface_subnet_usage</span> <b>(Alias name: interface-subnet-usage)</b>  Enable/disable allowing use of interface-subnet setting in firewall addresses (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forticontroller_proxy</span> <b>(Alias name: forticontroller-proxy)</b>  Enable/disable forticontroller proxy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_enc_algo</span> <b>(Alias name: ssh-enc-algo)</b>  Select one or more ssh ciphers. <span class="li-normal">type: list</span> <span class="li-normal">choices: [chacha20-poly1305@openssh.com, aes128-ctr, aes192-ctr, aes256-ctr, arcfour256, arcfour128, aes128-cbc, 3des-cbc, blowfish-cbc, cast128-cbc, aes192-cbc, aes256-cbc, arcfour, rijndael-cbc@lysator.liu.se, aes128-gcm@openssh.com, aes256-gcm@openssh.com]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_session_timer</span> <b>(Alias name: block-session-timer)</b>  Duration in seconds for blocked sessions (1 - 300 sec  (5 minutes), default = 30). <span class="li-normal">type: int</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic_pmtud</span> <b>(Alias name: quic-pmtud)</b>  Enable/disable path mtu discovery (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_https_ssl_ciphersuites</span> <b>(Alias name: admin-https-ssl-ciphersuites)</b>  Select one or more tls 1. <span class="li-normal">type: list</span> <span class="li-normal">choices: [TLS-AES-128-GCM-SHA256, TLS-AES-256-GCM-SHA384, TLS-CHACHA20-POLY1305-SHA256, TLS-AES-128-CCM-SHA256, TLS-AES-128-CCM-8-SHA256]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_rating_result_submission</span> <b>(Alias name: security-rating-result-submission)</b>  Enable/disable the submission of security rating results to fortiguard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">user_device_store_max_unified_mem</span> <b>(Alias name: user-device-store-max-unified-mem)</b>  Maximum unified memory allowed in user device store. <span class="li-normal">type: int</span>
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">management_port</span> <b>(Alias name: management-port)</b>  Overriding port for management connection (overrides admin port). <span class="li-normal">type: int</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortigslb_integration</span> <b>(Alias name: fortigslb-integration)</b>  Enable/disable integration with the fortigslb cloud service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_https_ssl_versions</span> <b>(Alias name: admin-https-ssl-versions)</b>  Allowed tls versions for web administration. <span class="li-normal">type: list</span> <span class="li-normal">choices: [tlsv1-0, tlsv1-1, tlsv1-2, sslv3, tlsv1-3]</span> 
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cert_chain_max</span> <b>(Alias name: cert-chain-max)</b>  Maximum number of certificates that can be traversed in a certificate chain. <span class="li-normal">type: int</span>
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qsfp28_40g_port</span> <b>(Alias name: qsfp28-40g-port)</b>  Set port(s) to 40gbps <span class="li-normal">type: list</span>
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">strong_crypto</span> <b>(Alias name: strong-crypto)</b>  Enable to use strong encryption and only allow strong ciphers and digest for https/ssh/tls/ssl functions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">multi_factor_authentication</span> <b>(Alias name: multi-factor-authentication)</b>  Enforce all login methods to require an additional authentication factor (default = optional). <span class="li-normal">type: str</span> <span class="li-normal">choices: [optional, mandatory]</span> 
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fds_statistics</span> <b>(Alias name: fds-statistics)</b>  Enable/disable sending ips, application control, and antivirus data to fortiguard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_display_hostname</span> <b>(Alias name: gui-display-hostname)</b>  Enable/disable displaying the fortigates hostname on the gui login page. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">two_factor_ftk_expiry</span> <b>(Alias name: two-factor-ftk-expiry)</b>  Fortitoken authentication session timeout (60 - 600 sec (10 minutes), default = 60). <span class="li-normal">type: int</span>
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_source_affinity</span> <b>(Alias name: wad-source-affinity)</b>  Enable/disable dispatching traffic to wad workers based on source affinity. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_static_key_ciphers</span> <b>(Alias name: ssl-static-key-ciphers)</b>  Enable/disable static key ciphers in ssl/tls connections (e. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">daily_restart</span> <b>(Alias name: daily-restart)</b>  Enable/disable daily restart of fortigate unit. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">snat_route_change</span> <b>(Alias name: snat-route-change)</b>  Enable/disable the ability to change the source nat route. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_rst_timer</span> <b>(Alias name: tcp-rst-timer)</b>  Length of the tcp close state in seconds (5 - 300 sec, default = 5). <span class="li-normal">type: int</span>
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">anti_replay</span> <b>(Alias name: anti-replay)</b>  Level of checking for packet replay and tcp sequence checking. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, loose, strict]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_min_proto_version</span> <b>(Alias name: ssl-min-proto-version)</b>  Minimum supported protocol version for ssl/tls connections (default = tlsv1. <span class="li-normal">type: str</span> <span class="li-normal">choices: [TLSv1, TLSv1-1, TLSv1-2, SSLv3, TLSv1-3]</span> 
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">speedtestd_server_port</span> <b>(Alias name: speedtestd-server-port)</b>  Speedtest server port number. <span class="li-normal">type: int</span>
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cpu_use_threshold</span> <b>(Alias name: cpu-use-threshold)</b>  Threshold at which cpu usage is reported (% of total cpu, default = 90). <span class="li-normal">type: int</span>
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_host</span> <b>(Alias name: admin-host)</b>  Administrative host for http and https. <span class="li-normal">type: str</span>
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">csr_ca_attribute</span> <b>(Alias name: csr-ca-attribute)</b>  Enable/disable the ca attribute in certificates. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiservice_port</span> <b>(Alias name: fortiservice-port)</b>  Fortiservice port (1 - 65535, default = 8013). <span class="li-normal">type: int</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssd_trim_hour</span> <b>(Alias name: ssd-trim-hour)</b>  Hour of the day on which to run ssd trim (0 - 23, default = 1). <span class="li-normal">type: int</span>
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">purdue_level</span> <b>(Alias name: purdue-level)</b>  Purdue level of this fortigate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [1, 2, 3, 4, 5, 1.5, 2.5, 3.5, 5.5]</span> 
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">management_vdom</span> <b>(Alias name: management-vdom)</b>  Management virtual domain name. <span class="li-normal">type: list</span>
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic_ack_thresold</span> <b>(Alias name: quic-ack-thresold)</b>  Maximum number of unacknowledged packets before sending ack (2 - 5, default = 3). <span class="li-normal">type: int</span>
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qsfpdd_100g_port</span> <b>(Alias name: qsfpdd-100g-port)</b>  Split qsfpddd port(s) as 100g ports <span class="li-normal">type: list</span>
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ips_affinity</span> <b>(Alias name: ips-affinity)</b>  Affinity setting for ips (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx; allowed cpus must be less than total number of ips engine daemons). <span class="li-normal">type: str</span>
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vip_arp_range</span> <b>(Alias name: vip-arp-range)</b>  Controls the number of arps that the fortigate sends for a virtual ip (vip) address range. <span class="li-normal">type: str</span> <span class="li-normal">choices: [restricted, unlimited]</span> 
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_database</span> <b>(Alias name: internet-service-database)</b>  Configure which internet service database size to download from fortiguard and use. <span class="li-normal">type: str</span> <span class="li-normal">choices: [mini, standard, full, on-demand]</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">revision_image_auto_backup</span> <b>(Alias name: revision-image-auto-backup)</b>  Enable/disable back-up of the latest image revision after the firmware is upgraded. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sflowd_max_children_num</span> <b>(Alias name: sflowd-max-children-num)</b>  Maximum number of sflowd child processes allowed to run. <span class="li-normal">type: int</span>
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_https_pki_required</span> <b>(Alias name: admin-https-pki-required)</b>  Enable/disable admin login method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">special_file_23_support</span> <b>(Alias name: special-file-23-support)</b>  Enable/disable detection of those special format files when using data loss prevention. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">npu_neighbor_update</span> <b>(Alias name: npu-neighbor-update)</b>  Enable/disable sending of arp/icmp6 probing packets to update neighbors for offloaded sessions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_single_cpu_high</span> <b>(Alias name: log-single-cpu-high)</b>  Enable/disable logging the event of a single cpu core reaching cpu usage threshold. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">management_ip</span> <b>(Alias name: management-ip)</b>  Management ip address of this fortigate. <span class="li-normal">type: str</span>
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_resource_mode</span> <b>(Alias name: proxy-resource-mode)</b>  Enable/disable use of the maximum memory usage on the fortigate units proxy processing of resources, such as block lists, allow lists, and external resources. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_ble_button</span> <b>(Alias name: admin-ble-button)</b>  Press the ble button can enable ble function <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_firmware_upgrade_warning</span> <b>(Alias name: gui-firmware-upgrade-warning)</b>  Enable/disable the firmware upgrade warning on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dp_tcp_normal_timer</span> <b>(Alias name: dp-tcp-normal-timer)</b>  Dp tcp normal timeout (1 - 65535 sec, default = 3605). <span class="li-normal">type: int</span>
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_allow_traffic_redirect</span> <b>(Alias name: ipv6-allow-traffic-redirect)</b>  Disable to prevent ipv6 traffic with same local ingress and egress interface from being forwarded without policy check. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cli_audit_log</span> <b>(Alias name: cli-audit-log)</b>  Enable/disable cli audit log. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">memory_use_threshold_extreme</span> <b>(Alias name: memory-use-threshold-extreme)</b>  Threshold at which memory usage is considered extreme (new sessions are dropped) (% of total ram, default = 95). <span class="li-normal">type: int</span>
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ha_affinity</span> <b>(Alias name: ha-affinity)</b>  Affinity setting for ha daemons (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). <span class="li-normal">type: str</span>
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">restart_time</span> <b>(Alias name: restart-time)</b>  Daily restart time (hh:mm). <span class="li-normal">type: str</span>
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">speedtestd_ctrl_port</span> <b>(Alias name: speedtestd-ctrl-port)</b>  Speedtest server controller port number. <span class="li-normal">type: int</span>
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_wireless_opensecurity</span> <b>(Alias name: gui-wireless-opensecurity)</b>  Enable/disable wireless open security option on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">memory_use_threshold_red</span> <b>(Alias name: memory-use-threshold-red)</b>  Threshold at which memory usage forces the fortigate to enter conserve mode (% of total ram, default = 88). <span class="li-normal">type: int</span>
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dp_fragment_timer</span> <b>(Alias name: dp-fragment-timer)</b>  Dp fragment session timeout (1 - 65535 sec, default = 120). <span class="li-normal">type: int</span>
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_restart_start_time</span> <b>(Alias name: wad-restart-start-time)</b>  Wad workers daily restart time (hh:mm). <span class="li-normal">type: str</span>
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_re_authentication_time</span> <b>(Alias name: proxy-re-authentication-time)</b>  The time limit that users must re-authenticate if proxy-keep-alive-mode is set to re-authenticate (1  - 86400 sec, default=30s. <span class="li-normal">type: int</span>
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_app_detection_sdwan</span> <b>(Alias name: gui-app-detection-sdwan)</b>  Enable/disable allow app-detection based sd-wan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">scanunit_count</span> <b>(Alias name: scanunit-count)</b>  Number of scanunits. <span class="li-normal">type: int</span>
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tftp</span> Enable/disable tftp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">xstools_update_frequency</span> <b>(Alias name: xstools-update-frequency)</b>  Xenserver tools daemon update frequency (30 - 300 sec, default = 60). <span class="li-normal">type: int</span>
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">clt_cert_req</span> <b>(Alias name: clt-cert-req)</b>  Enable/disable requiring administrators to have a client certificate to log into the gui using https. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiextender_vlan_mode</span> <b>(Alias name: fortiextender-vlan-mode)</b>  Enable/disable fortiextender vlan mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_http_port</span> <b>(Alias name: auth-http-port)</b>  User authentication http port. <span class="li-normal">type: int</span>
 <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">per_user_bal</span> <b>(Alias name: per-user-bal)</b>  Enable/disable per-user block/allow list filter. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_date_format</span> <b>(Alias name: gui-date-format)</b>  Default date format used throughout gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [yyyy/MM/dd, dd/MM/yyyy, MM/dd/yyyy, yyyy-MM-dd, dd-MM-yyyy, MM-dd-yyyy]</span> 
 <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_uuid_address</span> <b>(Alias name: log-uuid-address)</b>  Enable/disable insertion of address uuids to traffic logs. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cloud_communication</span> <b>(Alias name: cloud-communication)</b>  Enable/disable all cloud communication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lldp_reception</span> <b>(Alias name: lldp-reception)</b>  Enable/disable link layer discovery protocol (lldp) reception. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">two_factor_ftm_expiry</span> <b>(Alias name: two-factor-ftm-expiry)</b>  Fortitoken mobile session timeout (1 - 168 hours (7 days), default = 72). <span class="li-normal">type: int</span>
 <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic_udp_payload_size_shaping_per_cid</span> <b>(Alias name: quic-udp-payload-size-shaping-per-cid)</b>  Enable/disable udp payload size shaping per connection id (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">autorun_log_fsck</span> <b>(Alias name: autorun-log-fsck)</b>  Enable/disable automatic log partition check after ungraceful shutdown. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vpn_ems_sn_check</span> <b>(Alias name: vpn-ems-sn-check)</b>  Enable/disable verification of ems serial number in ssl-vpn connection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_ssh_password</span> <b>(Alias name: admin-ssh-password)</b>  Enable/disable password authentication for ssh admin access. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">airplane_mode</span> <b>(Alias name: airplane-mode)</b>  Enable/disable airplane mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">batch_cmdb</span> <b>(Alias name: batch-cmdb)</b>  Enable/disable batch mode, allowing you to enter a series of cli commands that will execute as a group once they are loaded. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip_src_port_range</span> <b>(Alias name: ip-src-port-range)</b>  Ip source port range used for traffic originating from the fortigate unit. <span class="li-normal">type: list</span>
 <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">strict_dirty_session_check</span> <b>(Alias name: strict-dirty-session-check)</b>  Enable to check the session against the original policy when revalidating. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">user_device_store_max_devices</span> <b>(Alias name: user-device-store-max-devices)</b>  Maximum number of devices allowed in user device store. <span class="li-normal">type: int</span>
 <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dp_udp_idle_timer</span> <b>(Alias name: dp-udp-idle-timer)</b>  Dp udp idle timer (0 - 86400 sec, default = 0). <span class="li-normal">type: int</span>
 <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internal_switch_speed</span> <b>(Alias name: internal-switch-speed)</b>  Internal port speed. <span class="li-normal">type: list</span> <span class="li-normal">choices: [auto, 10full, 10half, 100full, 100half, 1000full, 1000auto]</span> 
 <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forticonverter_config_upload</span> <b>(Alias name: forticonverter-config-upload)</b>  Enable/disable config upload to forticonverter. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, once]</span> 
 <a id='label276' href="javascript:ContentClick('label277', 'label276');" onmouseover="ContentPreview('label277');" onmouseout="ContentUnpreview('label277');" title="click to collapse or expand..."> more... </a>
 <div id="label277" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipsec_round_robin</span> <b>(Alias name: ipsec-round-robin)</b>  Enable/disable round-robin redistribution to multiple cpus for ipsec vpn traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label278' href="javascript:ContentClick('label279', 'label278');" onmouseover="ContentPreview('label279');" onmouseout="ContentUnpreview('label279');" title="click to collapse or expand..."> more... </a>
 <div id="label279" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_affinity</span> <b>(Alias name: wad-affinity)</b>  Affinity setting for wad (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). <span class="li-normal">type: str</span>
 <a id='label280' href="javascript:ContentClick('label281', 'label280');" onmouseover="ContentPreview('label281');" onmouseout="ContentUnpreview('label281');" title="click to collapse or expand..."> more... </a>
 <div id="label281" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_ca_certificate</span> <b>(Alias name: wifi-ca-certificate)</b>  Ca certificate that verifies the wifi certificate. <span class="li-normal">type: list</span>
 <a id='label282' href="javascript:ContentClick('label283', 'label282');" onmouseover="ContentPreview('label283');" onmouseout="ContentUnpreview('label283');" title="click to collapse or expand..."> more... </a>
 <div id="label283" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wimax_4g_usb</span> <b>(Alias name: wimax-4g-usb)</b>  Enable/disable comparability with wimax 4g usb devices. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label284' href="javascript:ContentClick('label285', 'label284');" onmouseover="ContentPreview('label285');" onmouseout="ContentUnpreview('label285');" title="click to collapse or expand..."> more... </a>
 <div id="label285" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">miglog_affinity</span> <b>(Alias name: miglog-affinity)</b>  Affinity setting for logging (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). <span class="li-normal">type: str</span>
 <a id='label286' href="javascript:ContentClick('label287', 'label286');" onmouseover="ContentPreview('label287');" onmouseout="ContentUnpreview('label287');" title="click to collapse or expand..."> more... </a>
 <div id="label287" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">faz_disk_buffer_size</span> <b>(Alias name: faz-disk-buffer-size)</b>  Maximum disk buffer size to temporarily store logs destined for fortianalyzer. <span class="li-normal">type: int</span>
 <a id='label288' href="javascript:ContentClick('label289', 'label288');" onmouseover="ContentPreview('label289');" onmouseout="ContentUnpreview('label289');" title="click to collapse or expand..."> more... </a>
 <div id="label289" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_kex_algo</span> <b>(Alias name: ssh-kex-algo)</b>  Select one or more ssh kex algorithms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [diffie-hellman-group1-sha1, diffie-hellman-group14-sha1, diffie-hellman-group-exchange-sha1, diffie-hellman-group-exchange-sha256, curve25519-sha256@libssh.org, ecdh-sha2-nistp256, ecdh-sha2-nistp384, ecdh-sha2-nistp521, diffie-hellman-group14-sha256, diffie-hellman-group16-sha512, diffie-hellman-group18-sha512]</span> 
 <a id='label290' href="javascript:ContentClick('label291', 'label290');" onmouseover="ContentPreview('label291');" onmouseout="ContentUnpreview('label291');" title="click to collapse or expand..."> more... </a>
 <div id="label291" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_auth_extension_device</span> <b>(Alias name: auto-auth-extension-device)</b>  Enable/disable automatic authorization of dedicated fortinet extension devices. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label292' href="javascript:ContentClick('label293', 'label292');" onmouseover="ContentPreview('label293');" onmouseout="ContentUnpreview('label293');" title="click to collapse or expand..."> more... </a>
 <div id="label293" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forticarrier_bypass</span> <b>(Alias name: forticarrier-bypass)</b>  Forticarrier bypass. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label294' href="javascript:ContentClick('label295', 'label294');" onmouseover="ContentPreview('label295');" onmouseout="ContentUnpreview('label295');" title="click to collapse or expand..."> more... </a>
 <div id="label295" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">reset_sessionless_tcp</span> <b>(Alias name: reset-sessionless-tcp)</b>  Action to perform if the fortigate receives a tcp packet but cannot find a corresponding session in its session table. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label296' href="javascript:ContentClick('label297', 'label296');" onmouseover="ContentPreview('label297');" onmouseout="ContentUnpreview('label297');" title="click to collapse or expand..."> more... </a>
 <div id="label297" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">early_tcp_npu_session</span> <b>(Alias name: early-tcp-npu-session)</b>  Enable/disable early tcp npu session. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label298' href="javascript:ContentClick('label299', 'label298');" onmouseover="ContentPreview('label299');" onmouseout="ContentUnpreview('label299');" title="click to collapse or expand..."> more... </a>
 <div id="label299" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_unauthenticated_request_limit</span> <b>(Alias name: http-unauthenticated-request-limit)</b>  Http request body size limit before authentication. <span class="li-normal">type: int</span>
 <a id='label300' href="javascript:ContentClick('label301', 'label300');" onmouseover="ContentPreview('label301');" onmouseout="ContentUnpreview('label301');" title="click to collapse or expand..."> more... </a>
 <div id="label301" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_local_out</span> <b>(Alias name: gui-local-out)</b>  Enable/disable local-out traffic on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label302' href="javascript:ContentClick('label303', 'label302');" onmouseover="ContentPreview('label303');" onmouseout="ContentUnpreview('label303');" title="click to collapse or expand..."> more... </a>
 <div id="label303" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_option</span> <b>(Alias name: tcp-option)</b>  Enable sack, timestamp and mss tcp options. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label304' href="javascript:ContentClick('label305', 'label304');" onmouseover="ContentPreview('label305');" onmouseout="ContentUnpreview('label305');" title="click to collapse or expand..."> more... </a>
 <div id="label305" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_auth_timeout</span> <b>(Alias name: proxy-auth-timeout)</b>  Authentication timeout in minutes for authenticated users (1 - 300 min, default = 10). <span class="li-normal">type: int</span>
 <a id='label306' href="javascript:ContentClick('label307', 'label306');" onmouseover="ContentPreview('label307');" onmouseout="ContentUnpreview('label307');" title="click to collapse or expand..."> more... </a>
 <div id="label307" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiextender_discovery_lockdown</span> <b>(Alias name: fortiextender-discovery-lockdown)</b>  Enable/disable fortiextender capwap lockdown. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label308' href="javascript:ContentClick('label309', 'label308');" onmouseover="ContentPreview('label309');" onmouseout="ContentUnpreview('label309');" title="click to collapse or expand..."> more... </a>
 <div id="label309" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lldp_transmission</span> <b>(Alias name: lldp-transmission)</b>  Enable/disable link layer discovery protocol (lldp) transmission. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label310' href="javascript:ContentClick('label311', 'label310');" onmouseover="ContentPreview('label311');" onmouseout="ContentUnpreview('label311');" title="click to collapse or expand..."> more... </a>
 <div id="label311" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">split_port</span> <b>(Alias name: split-port)</b>  Split port(s) to multiple 10gbps ports. <span class="li-normal">type: list</span>
 <a id='label312' href="javascript:ContentClick('label313', 'label312');" onmouseover="ContentPreview('label313');" onmouseout="ContentUnpreview('label313');" title="click to collapse or expand..."> more... </a>
 <div id="label313" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_certificates</span> <b>(Alias name: gui-certificates)</b>  Enable/disable the system > certificate gui page, allowing you to add and configure certificates from the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label314' href="javascript:ContentClick('label315', 'label314');" onmouseover="ContentPreview('label315');" onmouseout="ContentUnpreview('label315');" title="click to collapse or expand..."> more... </a>
 <div id="label315" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cfg_save</span> <b>(Alias name: cfg-save)</b>  Configuration file save mode for cli changes. <span class="li-normal">type: str</span> <span class="li-normal">choices: [automatic, manual, revert]</span> 
 <a id='label316' href="javascript:ContentClick('label317', 'label316');" onmouseover="ContentPreview('label317');" onmouseout="ContentUnpreview('label317');" title="click to collapse or expand..."> more... </a>
 <div id="label317" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_keepalive</span> <b>(Alias name: auth-keepalive)</b>  Enable to prevent user authentication sessions from timing out when idle. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label318' href="javascript:ContentClick('label319', 'label318');" onmouseover="ContentPreview('label319');" onmouseout="ContentUnpreview('label319');" title="click to collapse or expand..."> more... </a>
 <div id="label319" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">split_port_mode</span> <b>(Alias name: split-port-mode)</b>  Split port mode. <span class="li-normal">type: list</span>
 <a id='label320' href="javascript:ContentClick('label321', 'label320');" onmouseover="ContentPreview('label321');" onmouseout="ContentUnpreview('label321');" title="click to collapse or expand..."> more... </a>
 <div id="label321" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">interface</span> Split port interface. <span class="li-normal">type: str</span>
 <a id='label322' href="javascript:ContentClick('label323', 'label322');" onmouseover="ContentPreview('label323');" onmouseout="ContentUnpreview('label323');" title="click to collapse or expand..."> more... </a>
 <div id="label323" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">split_mode</span> <b>(Alias name: split-mode)</b>  The configuration mode for the split port interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, 4x10G, 4x25G, 4x50G, 8x50G, 4x100G, 2x200G, 8x25G]</span> 
 <a id='label324' href="javascript:ContentClick('label325', 'label324');" onmouseover="ContentPreview('label325');" onmouseout="ContentUnpreview('label325');" title="click to collapse or expand..."> more... </a>
 <div id="label325" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">admin_forticloud_sso_login</span> <b>(Alias name: admin-forticloud-sso-login)</b>  Enable/disable forticloud admin login via sso. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label326' href="javascript:ContentClick('label327', 'label326');" onmouseover="ContentPreview('label327');" onmouseout="ContentUnpreview('label327');" title="click to collapse or expand..."> more... </a>
 <div id="label327" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">post_login_banner</span> <b>(Alias name: post-login-banner)</b>  Enable/disable displaying the administrator access disclaimer message after an administrator successfully logs in. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label328' href="javascript:ContentClick('label329', 'label328');" onmouseover="ContentPreview('label329');" onmouseout="ContentUnpreview('label329');" title="click to collapse or expand..."> more... </a>
 <div id="label329" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">br_fdb_max_entry</span> <b>(Alias name: br-fdb-max-entry)</b>  Maximum number of bridge forwarding database (fdb) entries. <span class="li-normal">type: int</span>
 <a id='label330' href="javascript:ContentClick('label331', 'label330');" onmouseover="ContentPreview('label331');" onmouseout="ContentUnpreview('label331');" title="click to collapse or expand..."> more... </a>
 <div id="label331" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip_fragment_mem_thresholds</span> <b>(Alias name: ip-fragment-mem-thresholds)</b>  Maximum memory (mb) used to reassemble ipv4/ipv6 fragments. <span class="li-normal">type: int</span>
 <a id='label332' href="javascript:ContentClick('label333', 'label332');" onmouseover="ContentPreview('label333');" onmouseout="ContentUnpreview('label333');" title="click to collapse or expand..."> more... </a>
 <div id="label333" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiextender_provision_on_authorization</span> <b>(Alias name: fortiextender-provision-on-authorization)</b>  Enable/disable automatic provisioning of latest fortiextender firmware on authorization. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label334' href="javascript:ContentClick('label335', 'label334');" onmouseover="ContentPreview('label335');" onmouseout="ContentUnpreview('label335');" title="click to collapse or expand..."> more... </a>
 <div id="label335" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">reboot_upon_config_restore</span> <b>(Alias name: reboot-upon-config-restore)</b>  Enable/disable reboot of system upon restoring configuration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label336' href="javascript:ContentClick('label337', 'label336');" onmouseover="ContentPreview('label337');" onmouseout="ContentUnpreview('label337');" title="click to collapse or expand..."> more... </a>
 <div id="label337" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">syslog_affinity</span> <b>(Alias name: syslog-affinity)</b>  Affinity setting for syslog (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). <span class="li-normal">type: str</span>
 <a id='label338' href="javascript:ContentClick('label339', 'label338');" onmouseover="ContentPreview('label339');" onmouseout="ContentUnpreview('label339');" title="click to collapse or expand..."> more... </a>
 <div id="label339" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiextender_data_port</span> <b>(Alias name: fortiextender-data-port)</b>  Fortiextender data port (1024 - 49150, default = 25246). <span class="li-normal">type: int</span>
 <a id='label340' href="javascript:ContentClick('label341', 'label340');" onmouseover="ContentPreview('label341');" onmouseout="ContentUnpreview('label341');" title="click to collapse or expand..."> more... </a>
 <div id="label341" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic_tls_handshake_timeout</span> <b>(Alias name: quic-tls-handshake-timeout)</b>  Time-to-live (ttl) for tls handshake in seconds (1 - 60, default = 5). <span class="li-normal">type: int</span>
 <a id='label342' href="javascript:ContentClick('label343', 'label342');" onmouseover="ContentPreview('label343');" onmouseout="ContentUnpreview('label343');" title="click to collapse or expand..."> more... </a>
 <div id="label343" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forticonverter_integration</span> <b>(Alias name: forticonverter-integration)</b>  Enable/disable forticonverter integration service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label344' href="javascript:ContentClick('label345', 'label344');" onmouseover="ContentPreview('label345');" onmouseout="ContentUnpreview('label345');" title="click to collapse or expand..."> more... </a>
 <div id="label345" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_keep_alive_mode</span> <b>(Alias name: proxy-keep-alive-mode)</b>  Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was authenticated. <span class="li-normal">type: str</span> <span class="li-normal">choices: [session, traffic, re-authentication]</span> 
 <a id='label346' href="javascript:ContentClick('label347', 'label346');" onmouseover="ContentPreview('label347');" onmouseout="ContentUnpreview('label347');" title="click to collapse or expand..."> more... </a>
 <div id="label347" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cmdbsvr_affinity</span> <b>(Alias name: cmdbsvr-affinity)</b>  Affinity setting for cmdbsvr (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). <span class="li-normal">type: str</span>
 <a id='label348' href="javascript:ContentClick('label349', 'label348');" onmouseover="ContentPreview('label349');" onmouseout="ContentUnpreview('label349');" title="click to collapse or expand..."> more... </a>
 <div id="label349" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_memory_change_granularity</span> <b>(Alias name: wad-memory-change-granularity)</b>  Minimum percentage change in system memory usage detected by the wad daemon prior to adjusting tcp window size for any active connection. <span class="li-normal">type: int</span>
 <a id='label350' href="javascript:ContentClick('label351', 'label350');" onmouseover="ContentPreview('label351');" onmouseout="ContentUnpreview('label351');" title="click to collapse or expand..."> more... </a>
 <div id="label351" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_lease_backup_interval</span> <b>(Alias name: dhcp-lease-backup-interval)</b>  Dhcp leases backup interval in seconds (10 - 3600, default = 60). <span class="li-normal">type: int</span>
 <a id='label352' href="javascript:ContentClick('label353', 'label352');" onmouseover="ContentPreview('label353');" onmouseout="ContentUnpreview('label353');" title="click to collapse or expand..."> more... </a>
 <div id="label353" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">check_protocol_header</span> <b>(Alias name: check-protocol-header)</b>  Level of checking performed on protocol headers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [loose, strict]</span> 
 <a id='label354' href="javascript:ContentClick('label355', 'label354');" onmouseover="ContentPreview('label355');" onmouseout="ContentUnpreview('label355');" title="click to collapse or expand..."> more... </a>
 <div id="label355" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_failopen_session</span> <b>(Alias name: av-failopen-session)</b>  When enabled and a proxy for a protocol runs out of room in its session table, that protocol goes into failopen mode and enacts the action specified by av-failopen. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label356' href="javascript:ContentClick('label357', 'label356');" onmouseover="ContentPreview('label357');" onmouseout="ContentUnpreview('label357');" title="click to collapse or expand..."> more... </a>
 <div id="label357" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipsec_ha_seqjump_rate</span> <b>(Alias name: ipsec-ha-seqjump-rate)</b>  Esp jump ahead rate (1g - 10g pps equivalent). <span class="li-normal">type: int</span>
 <a id='label358' href="javascript:ContentClick('label359', 'label358');" onmouseover="ContentPreview('label359');" onmouseout="ContentUnpreview('label359');" title="click to collapse or expand..."> more... </a>
 <div id="label359" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_hsts_max_age</span> <b>(Alias name: admin-hsts-max-age)</b>  Https strict-transport-security header max-age in seconds. <span class="li-normal">type: int</span>
 <a id='label360' href="javascript:ContentClick('label361', 'label360');" onmouseover="ContentPreview('label361');" onmouseout="ContentUnpreview('label361');" title="click to collapse or expand..."> more... </a>
 <div id="label361" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">igmp_state_limit</span> <b>(Alias name: igmp-state-limit)</b>  Maximum number of igmp memberships (96 - 64000, default = 3200). <span class="li-normal">type: int</span>
 <a id='label362' href="javascript:ContentClick('label363', 'label362');" onmouseover="ContentPreview('label363');" onmouseout="ContentUnpreview('label363');" title="click to collapse or expand..."> more... </a>
 <div id="label363" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_login_max</span> <b>(Alias name: admin-login-max)</b>  Maximum number of administrators who can be logged in at the same time (1 - 100, default = 100). <span class="li-normal">type: int</span>
 <a id='label364' href="javascript:ContentClick('label365', 'label364');" onmouseover="ContentPreview('label365');" onmouseout="ContentUnpreview('label365');" title="click to collapse or expand..."> more... </a>
 <div id="label365" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_allow_multicast_probe</span> <b>(Alias name: ipv6-allow-multicast-probe)</b>  Enable/disable ipv6 address probe through multicast. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label366' href="javascript:ContentClick('label367', 'label366');" onmouseover="ContentPreview('label367');" onmouseout="ContentUnpreview('label367');" title="click to collapse or expand..."> more... </a>
 <div id="label367" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">virtual_switch_vlan</span> <b>(Alias name: virtual-switch-vlan)</b>  Enable/disable virtual switch vlan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label368' href="javascript:ContentClick('label369', 'label368');" onmouseover="ContentPreview('label369');" onmouseout="ContentUnpreview('label369');" title="click to collapse or expand..."> more... </a>
 <div id="label369" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_lockout_threshold</span> <b>(Alias name: admin-lockout-threshold)</b>  Number of failed login attempts before an administrator account is locked out for the admin-lockout-duration. <span class="li-normal">type: int</span>
 <a id='label370' href="javascript:ContentClick('label371', 'label370');" onmouseover="ContentPreview('label371');" onmouseout="ContentUnpreview('label371');" title="click to collapse or expand..."> more... </a>
 <div id="label371" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dp_pinhole_timer</span> <b>(Alias name: dp-pinhole-timer)</b>  Dp pinhole session timeout (30 - 120 sec, default = 120). <span class="li-normal">type: int</span>
 <a id='label372' href="javascript:ContentClick('label373', 'label372');" onmouseover="ContentPreview('label373');" onmouseout="ContentUnpreview('label373');" title="click to collapse or expand..."> more... </a>
 <div id="label373" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wireless_controller</span> <b>(Alias name: wireless-controller)</b>  Enable/disable the wireless controller feature to use the fortigate unit to manage fortiaps. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label374' href="javascript:ContentClick('label375', 'label374');" onmouseover="ContentPreview('label375');" onmouseout="ContentUnpreview('label375');" title="click to collapse or expand..."> more... </a>
 <div id="label375" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bfd_affinity</span> <b>(Alias name: bfd-affinity)</b>  Affinity setting for bfd daemon (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). <span class="li-normal">type: str</span>
 <a id='label376' href="javascript:ContentClick('label377', 'label376');" onmouseover="ContentPreview('label377');" onmouseout="ContentUnpreview('label377');" title="click to collapse or expand..."> more... </a>
 <div id="label377" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssd_trim_freq</span> <b>(Alias name: ssd-trim-freq)</b>  How often to run ssd trim (default = weekly). <span class="li-normal">type: str</span> <span class="li-normal">choices: [daily, weekly, monthly, hourly, never]</span> 
 <a id='label378' href="javascript:ContentClick('label379', 'label378');" onmouseover="ContentPreview('label379');" onmouseout="ContentUnpreview('label379');" title="click to collapse or expand..."> more... </a>
 <div id="label379" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">two_factor_sms_expiry</span> <b>(Alias name: two-factor-sms-expiry)</b>  Sms-based two-factor authentication session timeout (30 - 300 sec, default = 60). <span class="li-normal">type: int</span>
 <a id='label380' href="javascript:ContentClick('label381', 'label380');" onmouseover="ContentPreview('label381');" onmouseout="ContentUnpreview('label381');" title="click to collapse or expand..."> more... </a>
 <div id="label381" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">traffic_priority</span> <b>(Alias name: traffic-priority)</b>  Choose type of service (tos) or differentiated services code point (dscp) for traffic prioritization in traffic shaping. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tos, dscp]</span> 
 <a id='label382' href="javascript:ContentClick('label383', 'label382');" onmouseover="ContentPreview('label383');" onmouseout="ContentUnpreview('label383');" title="click to collapse or expand..."> more... </a>
 <div id="label383" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_and_explicit_proxy</span> <b>(Alias name: proxy-and-explicit-proxy)</b>  Proxy and explicit proxy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label384' href="javascript:ContentClick('label385', 'label384');" onmouseover="ContentPreview('label385');" onmouseout="ContentUnpreview('label385');" title="click to collapse or expand..."> more... </a>
 <div id="label385" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sslvpn_web_mode</span> <b>(Alias name: sslvpn-web-mode)</b>  Enable/disable ssl-vpn web mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label386' href="javascript:ContentClick('label387', 'label386');" onmouseover="ContentPreview('label387');" onmouseout="ContentUnpreview('label387');" title="click to collapse or expand..."> more... </a>
 <div id="label387" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_hostkey_password</span> <b>(Alias name: ssh-hostkey-password)</b>  Password for ssh-hostkey. <span class="li-normal">type: list</span>
 <a id='label388' href="javascript:ContentClick('label389', 'label388');" onmouseover="ContentPreview('label389');" onmouseout="ContentUnpreview('label389');" title="click to collapse or expand..."> more... </a>
 <div id="label389" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_csvc_db_count</span> <b>(Alias name: wad-csvc-db-count)</b>  Number of concurrent wad-cache-service byte-cache processes. <span class="li-normal">type: int</span>
 <a id='label390' href="javascript:ContentClick('label391', 'label390');" onmouseover="ContentPreview('label391');" onmouseout="ContentUnpreview('label391');" title="click to collapse or expand..."> more... </a>
 <div id="label391" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_allow_anycast_probe</span> <b>(Alias name: ipv6-allow-anycast-probe)</b>  Enable/disable ipv6 address probe through anycast. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label392' href="javascript:ContentClick('label393', 'label392');" onmouseover="ContentPreview('label393');" onmouseout="ContentUnpreview('label393');" title="click to collapse or expand..."> more... </a>
 <div id="label393" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">honor_df</span> <b>(Alias name: honor-df)</b>  Enable/disable honoring of dont-fragment (df) flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label394' href="javascript:ContentClick('label395', 'label394');" onmouseover="ContentPreview('label395');" onmouseout="ContentUnpreview('label395');" title="click to collapse or expand..."> more... </a>
 <div id="label395" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hyper_scale_vdom_num</span> <b>(Alias name: hyper-scale-vdom-num)</b>  Number of vdoms for hyper scale license. <span class="li-normal">type: int</span>
 <a id='label396' href="javascript:ContentClick('label397', 'label396');" onmouseover="ContentPreview('label397');" onmouseout="ContentUnpreview('label397');" title="click to collapse or expand..."> more... </a>
 <div id="label397" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_csvc_cs_count</span> <b>(Alias name: wad-csvc-cs-count)</b>  Number of concurrent wad-cache-service object-cache processes. <span class="li-normal">type: int</span>
 <a id='label398' href="javascript:ContentClick('label399', 'label398');" onmouseover="ContentPreview('label399');" onmouseout="ContentUnpreview('label399');" title="click to collapse or expand..."> more... </a>
 <div id="label399" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internal_switch_mode</span> <b>(Alias name: internal-switch-mode)</b>  Internal switch mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [switch, interface, hub]</span> 
 <a id='label400' href="javascript:ContentClick('label401', 'label400');" onmouseover="ContentPreview('label401');" onmouseout="ContentUnpreview('label401');" title="click to collapse or expand..."> more... </a>
 <div id="label401" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cfg_revert_timeout</span> <b>(Alias name: cfg-revert-timeout)</b>  Time-out for reverting to the last saved configuration. <span class="li-normal">type: int</span>
 <a id='label402' href="javascript:ContentClick('label403', 'label402');" onmouseover="ContentPreview('label403');" onmouseout="ContentUnpreview('label403');" title="click to collapse or expand..."> more... </a>
 <div id="label403" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_concurrent</span> <b>(Alias name: admin-concurrent)</b>  Enable/disable concurrent administrator logins. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label404' href="javascript:ContentClick('label405', 'label404');" onmouseover="ContentPreview('label405');" onmouseout="ContentUnpreview('label405');" title="click to collapse or expand..."> more... </a>
 <div id="label405" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_allow_local_in_silent_drop</span> <b>(Alias name: ipv6-allow-local-in-silent-drop)</b>  Enable/disable silent drop of ipv6 local-in traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label406' href="javascript:ContentClick('label407', 'label406');" onmouseover="ContentPreview('label407');" onmouseout="ContentUnpreview('label407');" title="click to collapse or expand..."> more... </a>
 <div id="label407" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_halfopen_timer</span> <b>(Alias name: tcp-halfopen-timer)</b>  Number of seconds the fortigate unit should wait to close a session after one peer has sent an open session packet but the other has not responded (1 - 86400 sec (1 day), default = 10). <span class="li-normal">type: int</span>
 <a id='label408' href="javascript:ContentClick('label409', 'label408');" onmouseover="ContentPreview('label409');" onmouseout="ContentUnpreview('label409');" title="click to collapse or expand..."> more... </a>
 <div id="label409" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dp_rsync_timer</span> <b>(Alias name: dp-rsync-timer)</b>  Dp rsync session timeout (1 - 65535 sec, default = 300). <span class="li-normal">type: int</span>
 <a id='label410' href="javascript:ContentClick('label411', 'label410');" onmouseover="ContentPreview('label411');" onmouseout="ContentUnpreview('label411');" title="click to collapse or expand..."> more... </a>
 <div id="label411" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">management_port_use_admin_sport</span> <b>(Alias name: management-port-use-admin-sport)</b>  Enable/disable use of the admin-sport setting for the management port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label412' href="javascript:ContentClick('label413', 'label412');" onmouseover="ContentPreview('label413');" onmouseout="ContentUnpreview('label413');" title="click to collapse or expand..."> more... </a>
 <div id="label413" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_forticare_registration_setup_warning</span> <b>(Alias name: gui-forticare-registration-setup-warning)</b>  Enable/disable the forticare registration setup warning on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label414' href="javascript:ContentClick('label415', 'label414');" onmouseover="ContentPreview('label415');" onmouseout="ContentUnpreview('label415');" title="click to collapse or expand..."> more... </a>
 <div id="label415" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_replacement_message_groups</span> <b>(Alias name: gui-replacement-message-groups)</b>  Enable/disable replacement message groups on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label416' href="javascript:ContentClick('label417', 'label416');" onmouseover="ContentPreview('label417');" onmouseout="ContentUnpreview('label417');" title="click to collapse or expand..."> more... </a>
 <div id="label417" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_rating_run_on_schedule</span> <b>(Alias name: security-rating-run-on-schedule)</b>  Enable/disable scheduled runs of security rating. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label418' href="javascript:ContentClick('label419', 'label418');" onmouseover="ContentPreview('label419');" onmouseout="ContentUnpreview('label419');" title="click to collapse or expand..."> more... </a>
 <div id="label419" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_lockout_duration</span> <b>(Alias name: admin-lockout-duration)</b>  Amount of time in seconds that an administrator account is locked out after reaching the admin-lockout-threshold for repeated failed login attempts. <span class="li-normal">type: int</span>
 <a id='label420' href="javascript:ContentClick('label421', 'label420');" onmouseover="ContentPreview('label421');" onmouseout="ContentUnpreview('label421');" title="click to collapse or expand..."> more... </a>
 <div id="label421" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">optimize_flow_mode</span> <b>(Alias name: optimize-flow-mode)</b>  Flow mode optimization option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label422' href="javascript:ContentClick('label423', 'label422');" onmouseover="ContentPreview('label423');" onmouseout="ContentUnpreview('label423');" title="click to collapse or expand..."> more... </a>
 <div id="label423" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">private_data_encryption</span> <b>(Alias name: private-data-encryption)</b>  Enable/disable private data encryption using an aes 128-bit key or passpharse. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label424' href="javascript:ContentClick('label425', 'label424');" onmouseover="ContentPreview('label425');" onmouseout="ContentUnpreview('label425');" title="click to collapse or expand..."> more... </a>
 <div id="label425" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wireless_mode</span> <b>(Alias name: wireless-mode)</b>  Wireless mode setting. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ac, client, wtp, fwfap]</span> 
 <a id='label426' href="javascript:ContentClick('label427', 'label426');" onmouseover="ContentPreview('label427');" onmouseout="ContentUnpreview('label427');" title="click to collapse or expand..."> more... </a>
 <div id="label427" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">alias</span> Alias for your fortigate unit. <span class="li-normal">type: str</span>
 <a id='label428' href="javascript:ContentClick('label429', 'label428');" onmouseover="ContentPreview('label429');" onmouseout="ContentUnpreview('label429');" title="click to collapse or expand..."> more... </a>
 <div id="label429" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_hostkey_algo</span> <b>(Alias name: ssh-hostkey-algo)</b>  Select one or more ssh hostkey algorithms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [ssh-rsa, ecdsa-sha2-nistp521, rsa-sha2-256, rsa-sha2-512, ssh-ed25519, ecdsa-sha2-nistp384, ecdsa-sha2-nistp256]</span> 
 <a id='label430' href="javascript:ContentClick('label431', 'label430');" onmouseover="ContentPreview('label431');" onmouseout="ContentUnpreview('label431');" title="click to collapse or expand..."> more... </a>
 <div id="label431" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortitoken_cloud</span> <b>(Alias name: fortitoken-cloud)</b>  Enable/disable fortitoken cloud service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label432' href="javascript:ContentClick('label433', 'label432');" onmouseover="ContentPreview('label433');" onmouseout="ContentUnpreview('label433');" title="click to collapse or expand..."> more... </a>
 <div id="label433" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_affinity</span> <b>(Alias name: av-affinity)</b>  Affinity setting for av scanning (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx). <span class="li-normal">type: str</span>
 <a id='label434' href="javascript:ContentClick('label435', 'label434');" onmouseover="ContentPreview('label435');" onmouseout="ContentUnpreview('label435');" title="click to collapse or expand..."> more... </a>
 <div id="label435" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_worker_count</span> <b>(Alias name: proxy-worker-count)</b>  Proxy worker count. <span class="li-normal">type: int</span>
 <a id='label436' href="javascript:ContentClick('label437', 'label436');" onmouseover="ContentPreview('label437');" onmouseout="ContentUnpreview('label437');" title="click to collapse or expand..."> more... </a>
 <div id="label437" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipsec_asic_offload</span> <b>(Alias name: ipsec-asic-offload)</b>  Enable/disable asic offloading (hardware acceleration) for ipsec vpn traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label438' href="javascript:ContentClick('label439', 'label438');" onmouseover="ContentPreview('label439');" onmouseout="ContentUnpreview('label439');" title="click to collapse or expand..."> more... </a>
 <div id="label439" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">miglogd_children</span> <b>(Alias name: miglogd-children)</b>  Number of logging (miglogd) processes to be allowed to run. <span class="li-normal">type: int</span>
 <a id='label440' href="javascript:ContentClick('label441', 'label440');" onmouseover="ContentPreview('label441');" onmouseout="ContentUnpreview('label441');" title="click to collapse or expand..."> more... </a>
 <div id="label441" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sslvpn_max_worker_count</span> <b>(Alias name: sslvpn-max-worker-count)</b>  Maximum number of ssl-vpn processes. <span class="li-normal">type: int</span>
 <a id='label442' href="javascript:ContentClick('label443', 'label442');" onmouseover="ContentPreview('label443');" onmouseout="ContentUnpreview('label443');" title="click to collapse or expand..."> more... </a>
 <div id="label443" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_mac_algo</span> <b>(Alias name: ssh-mac-algo)</b>  Select one or more ssh mac algorithms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [hmac-md5, hmac-md5-etm@openssh.com, hmac-md5-96, hmac-md5-96-etm@openssh.com, hmac-sha1, hmac-sha1-etm@openssh.com, hmac-sha2-256, hmac-sha2-256-etm@openssh.com, hmac-sha2-512, hmac-sha2-512-etm@openssh.com, hmac-ripemd160, hmac-ripemd160@openssh.com, hmac-ripemd160-etm@openssh.com, umac-64@openssh.com, umac-128@openssh.com, umac-64-etm@openssh.com, umac-128-etm@openssh.com]</span> 
 <a id='label444' href="javascript:ContentClick('label445', 'label444');" onmouseover="ContentPreview('label445');" onmouseout="ContentUnpreview('label445');" title="click to collapse or expand..."> more... </a>
 <div id="label445" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">url_filter_count</span> <b>(Alias name: url-filter-count)</b>  Url filter daemon count. <span class="li-normal">type: int</span>
 <a id='label446' href="javascript:ContentClick('label447', 'label446');" onmouseover="ContentPreview('label447');" onmouseout="ContentUnpreview('label447');" title="click to collapse or expand..."> more... </a>
 <div id="label447" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_certificate</span> <b>(Alias name: wifi-certificate)</b>  Certificate to use for wifi authentication. <span class="li-normal">type: list</span>
 <a id='label448' href="javascript:ContentClick('label449', 'label448');" onmouseover="ContentPreview('label449');" onmouseout="ContentUnpreview('label449');" title="click to collapse or expand..."> more... </a>
 <div id="label449" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_port</span> <b>(Alias name: radius-port)</b>  Radius service port number. <span class="li-normal">type: int</span>
 <a id='label450' href="javascript:ContentClick('label451', 'label450');" onmouseover="ContentPreview('label451');" onmouseout="ContentUnpreview('label451');" title="click to collapse or expand..."> more... </a>
 <div id="label451" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sys_perf_log_interval</span> <b>(Alias name: sys-perf-log-interval)</b>  Time in minutes between updates of performance statistics logging. <span class="li-normal">type: int</span>
 <a id='label452' href="javascript:ContentClick('label453', 'label452');" onmouseover="ContentPreview('label453');" onmouseout="ContentUnpreview('label453');" title="click to collapse or expand..."> more... </a>
 <div id="label453" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_fortigate_cloud_sandbox</span> <b>(Alias name: gui-fortigate-cloud-sandbox)</b>  Enable/disable displaying fortigate cloud sandbox on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label454' href="javascript:ContentClick('label455', 'label454');" onmouseover="ContentPreview('label455');" onmouseout="ContentUnpreview('label455');" title="click to collapse or expand..."> more... </a>
 <div id="label455" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_cert</span> <b>(Alias name: auth-cert)</b>  Server certificate that the fortigate uses for https firewall authentication connections. <span class="li-normal">type: list</span>
 <a id='label456' href="javascript:ContentClick('label457', 'label456');" onmouseover="ContentPreview('label457');" onmouseout="ContentUnpreview('label457');" title="click to collapse or expand..."> more... </a>
 <div id="label457" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiextender</span> Enable/disable fortiextender. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label458' href="javascript:ContentClick('label459', 'label458');" onmouseover="ContentPreview('label459');" onmouseout="ContentUnpreview('label459');" title="click to collapse or expand..."> more... </a>
 <div id="label459" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_reset_button</span> <b>(Alias name: admin-reset-button)</b>  Press the reset button can reset to factory default. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label460' href="javascript:ContentClick('label461', 'label460');" onmouseover="ContentPreview('label461');" onmouseout="ContentUnpreview('label461');" title="click to collapse or expand..."> more... </a>
 <div id="label461" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_failopen</span> <b>(Alias name: av-failopen)</b>  Set the action to take if the fortigate is running low on memory or the proxy connection limit has been reached. <span class="li-normal">type: str</span> <span class="li-normal">choices: [off, pass, one-shot, idledrop]</span> 
 <a id='label462' href="javascript:ContentClick('label463', 'label462');" onmouseover="ContentPreview('label463');" onmouseout="ContentUnpreview('label463');" title="click to collapse or expand..."> more... </a>
 <div id="label463" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">user_device_store_max_users</span> <b>(Alias name: user-device-store-max-users)</b>  Maximum number of users allowed in user device store. <span class="li-normal">type: int</span>
 <a id='label464' href="javascript:ContentClick('label465', 'label464');" onmouseover="ContentPreview('label465');" onmouseout="ContentUnpreview('label465');" title="click to collapse or expand..."> more... </a>
 <div id="label465" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_session_limit</span> <b>(Alias name: auth-session-limit)</b>  Action to take when the number of allowed user authenticated sessions is reached. <span class="li-normal">type: str</span> <span class="li-normal">choices: [block-new, logout-inactive]</span> 
 <a id='label466' href="javascript:ContentClick('label467', 'label466');" onmouseover="ContentPreview('label467');" onmouseout="ContentUnpreview('label467');" title="click to collapse or expand..."> more... </a>
 <div id="label467" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_allow_local_in_slient_drop</span> <b>(Alias name: ipv6-allow-local-in-slient-drop)</b>  Enable/disable silent drop of ipv6 local-in traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label468' href="javascript:ContentClick('label469', 'label468');" onmouseover="ContentPreview('label469');" onmouseout="ContentUnpreview('label469');" title="click to collapse or expand..."> more... </a>
 <div id="label469" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic_congestion_control_algo</span> <b>(Alias name: quic-congestion-control-algo)</b>  Quic congestion control algorithm (default = cubic). <span class="li-normal">type: str</span> <span class="li-normal">choices: [cubic, bbr, bbr2, reno]</span> 
 <a id='label470' href="javascript:ContentClick('label471', 'label470');" onmouseover="ContentPreview('label471');" onmouseout="ContentUnpreview('label471');" title="click to collapse or expand..."> more... </a>
 <div id="label471" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_ike_saml_port</span> <b>(Alias name: auth-ike-saml-port)</b>  User ike saml authentication port (0 - 65535, default = 1001). <span class="li-normal">type: int</span>
 <a id='label472' href="javascript:ContentClick('label473', 'label472');" onmouseover="ContentPreview('label473');" onmouseout="ContentUnpreview('label473');" title="click to collapse or expand..."> more... </a>
 <div id="label473" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_restart_end_time</span> <b>(Alias name: wad-restart-end-time)</b>  Wad workers daily restart end time (hh:mm). <span class="li-normal">type: str</span>
 <a id='label474' href="javascript:ContentClick('label475', 'label474');" onmouseover="ContentPreview('label475');" onmouseout="ContentUnpreview('label475');" title="click to collapse or expand..."> more... </a>
 <div id="label475" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_request_limit</span> <b>(Alias name: http-request-limit)</b>  Http request body size limit. <span class="li-normal">type: int</span>
 <a id='label476' href="javascript:ContentClick('label477', 'label476');" onmouseover="ContentPreview('label477');" onmouseout="ContentUnpreview('label477');" title="click to collapse or expand..."> more... </a>
 <div id="label477" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">irq_time_accounting</span> <b>(Alias name: irq-time-accounting)</b>  Configure cpu irq time accounting mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, force]</span> 
 <a id='label478' href="javascript:ContentClick('label479', 'label478');" onmouseover="ContentPreview('label479');" onmouseout="ContentUnpreview('label479');" title="click to collapse or expand..."> more... </a>
 <div id="label479" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remoteauthtimeout</span> Number of seconds that the fortigate waits for responses from remote radius, ldap, or tacacs+ authentication servers. <span class="li-normal">type: int</span>
 <a id='label480' href="javascript:ContentClick('label481', 'label480');" onmouseover="ContentPreview('label481');" onmouseout="ContentUnpreview('label481');" title="click to collapse or expand..."> more... </a>
 <div id="label481" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_https_ssl_banned_ciphers</span> <b>(Alias name: admin-https-ssl-banned-ciphers)</b>  Select one or more cipher technologies that cannot be used in gui https negotiations. <span class="li-normal">type: list</span> <span class="li-normal">choices: [RSA, DHE, ECDHE, DSS, ECDSA, AES, AESGCM, CAMELLIA, 3DES, SHA1, SHA256, SHA384, STATIC, CHACHA20, ARIA, AESCCM]</span> 
 <a id='label482' href="javascript:ContentClick('label483', 'label482');" onmouseover="ContentPreview('label483');" onmouseout="ContentUnpreview('label483');" title="click to collapse or expand..."> more... </a>
 <div id="label483" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">allow_traffic_redirect</span> <b>(Alias name: allow-traffic-redirect)</b>  Disable to prevent traffic with same local ingress and egress interface from being forwarded without policy check. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label484' href="javascript:ContentClick('label485', 'label484');" onmouseover="ContentPreview('label485');" onmouseout="ContentUnpreview('label485');" title="click to collapse or expand..."> more... </a>
 <div id="label485" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">legacy_poe_device_support</span> <b>(Alias name: legacy-poe-device-support)</b>  Enable/disable legacy poe device support. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label486' href="javascript:ContentClick('label487', 'label486');" onmouseover="ContentPreview('label487');" onmouseout="ContentUnpreview('label487');" title="click to collapse or expand..."> more... </a>
 <div id="label487" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wad_restart_mode</span> <b>(Alias name: wad-restart-mode)</b>  Wad worker restart mode (default = none). <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, time, memory]</span> 
 <a id='label488' href="javascript:ContentClick('label489', 'label488');" onmouseover="ContentPreview('label489');" onmouseout="ContentUnpreview('label489');" title="click to collapse or expand..."> more... </a>
 <div id="label489" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fds_statistics_period</span> <b>(Alias name: fds-statistics-period)</b>  Fortiguard statistics collection period in minutes. <span class="li-normal">type: int</span>
 <a id='label490' href="javascript:ContentClick('label491', 'label490');" onmouseover="ContentPreview('label491');" onmouseout="ContentUnpreview('label491');" title="click to collapse or expand..."> more... </a>
 <div id="label491" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_telnet</span> <b>(Alias name: admin-telnet)</b>  Enable/disable telnet service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label492' href="javascript:ContentClick('label493', 'label492');" onmouseover="ContentPreview('label493');" onmouseout="ContentUnpreview('label493');" title="click to collapse or expand..."> more... </a>
 <div id="label493" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_accept_dad</span> <b>(Alias name: ipv6-accept-dad)</b>  Enable/disable acceptance of ipv6 duplicate address detection (dad). <span class="li-normal">type: int</span>
 <a id='label494' href="javascript:ContentClick('label495', 'label494');" onmouseover="ContentPreview('label495');" onmouseout="ContentUnpreview('label495');" title="click to collapse or expand..."> more... </a>
 <div id="label495" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_timewait_timer</span> <b>(Alias name: tcp-timewait-timer)</b>  Length of the tcp time-wait state in seconds (1 - 300 sec, default = 1). <span class="li-normal">type: int</span>
 <a id='label496' href="javascript:ContentClick('label497', 'label496');" onmouseover="ContentPreview('label497');" onmouseout="ContentUnpreview('label497');" title="click to collapse or expand..."> more... </a>
 <div id="label497" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_console_timeout</span> <b>(Alias name: admin-console-timeout)</b>  Console login timeout that overrides the admin timeout value (15 - 300 seconds, default = 0, which disables the timeout). <span class="li-normal">type: int</span>
 <a id='label498' href="javascript:ContentClick('label499', 'label498');" onmouseover="ContentPreview('label499');" onmouseout="ContentUnpreview('label499');" title="click to collapse or expand..."> more... </a>
 <div id="label499" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">default_service_source_port</span> <b>(Alias name: default-service-source-port)</b>  Default service source port range (default = 1 - 65535). <span class="li-normal">type: str</span>
 <a id='label500' href="javascript:ContentClick('label501', 'label500');" onmouseover="ContentPreview('label501');" onmouseout="ContentUnpreview('label501');" title="click to collapse or expand..."> more... </a>
 <div id="label501" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic_max_datagram_size</span> <b>(Alias name: quic-max-datagram-size)</b>  Maximum transmit datagram size (1200 - 1500, default = 1500). <span class="li-normal">type: int</span>
 <a id='label502' href="javascript:ContentClick('label503', 'label502');" onmouseover="ContentPreview('label503');" onmouseout="ContentUnpreview('label503');" title="click to collapse or expand..."> more... </a>
 <div id="label503" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">refresh</span> Statistics refresh interval second(s) in gui. <span class="li-normal">type: int</span>
 <a id='label504' href="javascript:ContentClick('label505', 'label504');" onmouseover="ContentPreview('label505');" onmouseout="ContentUnpreview('label505');" title="click to collapse or expand..."> more... </a>
 <div id="label505" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">extender_controller_reserved_network</span> <b>(Alias name: extender-controller-reserved-network)</b>  Configure reserved network subnet for managed lan extension fortiextender units. <span class="li-normal">type: list</span>
 <a id='label506' href="javascript:ContentClick('label507', 'label506');" onmouseover="ContentPreview('label507');" onmouseout="ContentUnpreview('label507');" title="click to collapse or expand..."> more... </a>
 <div id="label507" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">url_filter_affinity</span> <b>(Alias name: url-filter-affinity)</b>  Url filter cpu affinity. <span class="li-normal">type: str</span>
 <a id='label508' href="javascript:ContentClick('label509', 'label508');" onmouseover="ContentPreview('label509');" onmouseout="ContentUnpreview('label509');" title="click to collapse or expand..."> more... </a>
 <div id="label509" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">policy_auth_concurrent</span> <b>(Alias name: policy-auth-concurrent)</b>  Number of concurrent firewall use logins from the same user (1 - 100, default = 0 means no limit). <span class="li-normal">type: int</span>
 <a id='label510' href="javascript:ContentClick('label511', 'label510');" onmouseover="ContentPreview('label511');" onmouseout="ContentUnpreview('label511');" title="click to collapse or expand..."> more... </a>
 <div id="label511" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipsec_hmac_offload</span> <b>(Alias name: ipsec-hmac-offload)</b>  Enable/disable offloading (hardware acceleration) of hmac processing for ipsec vpn. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label512' href="javascript:ContentClick('label513', 'label512');" onmouseover="ContentPreview('label513');" onmouseout="ContentUnpreview('label513');" title="click to collapse or expand..."> more... </a>
 <div id="label513" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">traffic_priority_level</span> <b>(Alias name: traffic-priority-level)</b>  Default system-wide level of priority for traffic prioritization. <span class="li-normal">type: str</span> <span class="li-normal">choices: [high, medium, low]</span> 
 <a id='label514' href="javascript:ContentClick('label515', 'label514');" onmouseover="ContentPreview('label515');" onmouseout="ContentUnpreview('label515');" title="click to collapse or expand..."> more... </a>
 <div id="label515" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipsec_qat_offload</span> <b>(Alias name: ipsec-qat-offload)</b>  Enable/disable qat offloading (intel quickassist) for ipsec vpn traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label516' href="javascript:ContentClick('label517', 'label516');" onmouseover="ContentPreview('label517');" onmouseout="ContentUnpreview('label517');" title="click to collapse or expand..."> more... </a>
 <div id="label517" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssd_trim_min</span> <b>(Alias name: ssd-trim-min)</b>  Minute of the hour on which to run ssd trim (0 - 59, 60 for random). <span class="li-normal">type: int</span>
 <a id='label518' href="javascript:ContentClick('label519', 'label518');" onmouseover="ContentPreview('label519');" onmouseout="ContentUnpreview('label519');" title="click to collapse or expand..."> more... </a>
 <div id="label519" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_date_time_source</span> <b>(Alias name: gui-date-time-source)</b>  Source from which the fortigate gui uses to display date and time entries. <span class="li-normal">type: str</span> <span class="li-normal">choices: [system, browser]</span> 
 <a id='label520' href="javascript:ContentClick('label521', 'label520');" onmouseover="ContentPreview('label521');" onmouseout="ContentUnpreview('label521');" title="click to collapse or expand..."> more... </a>
 <div id="label521" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_ssl_connection</span> <b>(Alias name: log-ssl-connection)</b>  Enable/disable logging of ssl connection events. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label522' href="javascript:ContentClick('label523', 'label522');" onmouseover="ContentPreview('label523');" onmouseout="ContentUnpreview('label523');" title="click to collapse or expand..."> more... </a>
 <div id="label523" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ndp_max_entry</span> <b>(Alias name: ndp-max-entry)</b>  Maximum number of ndp table entries (set to 65,536 or higher; if set to 0, kernel holds 65,536 entries). <span class="li-normal">type: int</span>
 <a id='label524' href="javascript:ContentClick('label525', 'label524');" onmouseover="ContentPreview('label525');" onmouseout="ContentUnpreview('label525');" title="click to collapse or expand..."> more... </a>
 <div id="label525" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vdom_mode</span> <b>(Alias name: vdom-mode)</b>  Enable/disable support for multiple virtual domains (vdoms). <span class="li-normal">type: str</span> <span class="li-normal">choices: [no-vdom, multi-vdom, split-vdom]</span> 
 <a id='label526' href="javascript:ContentClick('label527', 'label526');" onmouseover="ContentPreview('label527');" onmouseout="ContentUnpreview('label527');" title="click to collapse or expand..."> more... </a>
 <div id="label527" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_download_list</span> <b>(Alias name: internet-service-download-list)</b>  Configure which on-demand internet service ids are to be downloaded. <span class="li-normal">type: list</span>
 <a id='label528' href="javascript:ContentClick('label529', 'label528');" onmouseover="ContentPreview('label529');" onmouseout="ContentUnpreview('label529');" title="click to collapse or expand..."> more... </a>
 <div id="label529" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortitoken_cloud_sync_interval</span> <b>(Alias name: fortitoken-cloud-sync-interval)</b>  Interval in which to clean up remote users in fortitoken cloud (0 - 336 hours (14 days), default = 24, disable = 0). <span class="li-normal">type: int</span>
 <a id='label530' href="javascript:ContentClick('label531', 'label530');" onmouseover="ContentPreview('label531');" onmouseout="ContentUnpreview('label531');" title="click to collapse or expand..."> more... </a>
 <div id="label531" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssd_trim_weekday</span> <b>(Alias name: ssd-trim-weekday)</b>  Day of week to run ssd trim. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> 
 <a id='label532' href="javascript:ContentClick('label533', 'label532');" onmouseover="ContentPreview('label533');" onmouseout="ContentUnpreview('label533');" title="click to collapse or expand..."> more... </a>
 <div id="label533" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">two_factor_fac_expiry</span> <b>(Alias name: two-factor-fac-expiry)</b>  Fortiauthenticator token authentication session timeout (10 - 3600 seconds (1 hour), default = 60). <span class="li-normal">type: int</span>
 <a id='label534' href="javascript:ContentClick('label535', 'label534');" onmouseover="ContentPreview('label535');" onmouseout="ContentUnpreview('label535');" title="click to collapse or expand..."> more... </a>
 <div id="label535" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_rest_api_cache</span> <b>(Alias name: gui-rest-api-cache)</b>  Enable/disable rest api result caching on fortigate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label536' href="javascript:ContentClick('label537', 'label536');" onmouseover="ContentPreview('label537');" onmouseout="ContentUnpreview('label537');" title="click to collapse or expand..."> more... </a>
 <div id="label537" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_forticloud_sso_default_profile</span> <b>(Alias name: admin-forticloud-sso-default-profile)</b>  Override access profile. <span class="li-normal">type: list</span>
 <a id='label538' href="javascript:ContentClick('label539', 'label538');" onmouseover="ContentPreview('label539');" onmouseout="ContentUnpreview('label539');" title="click to collapse or expand..."> more... </a>
 <div id="label539" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_auth_lifetime</span> <b>(Alias name: proxy-auth-lifetime)</b>  Enable/disable authenticated users lifetime control. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label540' href="javascript:ContentClick('label541', 'label540');" onmouseover="ContentPreview('label541');" onmouseout="ContentUnpreview('label541');" title="click to collapse or expand..."> more... </a>
 <div id="label541" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">device_idle_timeout</span> <b>(Alias name: device-idle-timeout)</b>  Time in seconds that a device must be idle to automatically log the device user out. <span class="li-normal">type: int</span>
 <a id='label542' href="javascript:ContentClick('label543', 'label542');" onmouseover="ContentPreview('label543');" onmouseout="ContentUnpreview('label543');" title="click to collapse or expand..."> more... </a>
 <div id="label543" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">login_timestamp</span> <b>(Alias name: login-timestamp)</b>  Enable/disable login time recording. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label544' href="javascript:ContentClick('label545', 'label544');" onmouseover="ContentPreview('label545');" onmouseout="ContentUnpreview('label545');" title="click to collapse or expand..."> more... </a>
 <div id="label545" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">speedtest_server</span> <b>(Alias name: speedtest-server)</b>  Enable/disable speed test server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label546' href="javascript:ContentClick('label547', 'label546');" onmouseover="ContentPreview('label547');" onmouseout="ContentUnpreview('label547');" title="click to collapse or expand..."> more... </a>
 <div id="label547" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">edit_vdom_prompt</span> <b>(Alias name: edit-vdom-prompt)</b>  Enable/disable edit new vdom prompt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label548' href="javascript:ContentClick('label549', 'label548');" onmouseover="ContentPreview('label549');" onmouseout="ContentUnpreview('label549');" title="click to collapse or expand..."> more... </a>
 <div id="label549" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_cdn_domain_override</span> <b>(Alias name: gui-cdn-domain-override)</b>  Domain of cdn server. <span class="li-normal">type: str</span>
 <a id='label550' href="javascript:ContentClick('label551', 'label550');" onmouseover="ContentPreview('label551');" onmouseout="ContentUnpreview('label551');" title="click to collapse or expand..."> more... </a>
 <div id="label551" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_ssh_grace_time</span> <b>(Alias name: admin-ssh-grace-time)</b>  Maximum time in seconds permitted between making an ssh connection to the fortigate unit and authenticating (10 - 3600 sec (1 hour), default 120). <span class="li-normal">type: int</span>
 <a id='label552' href="javascript:ContentClick('label553', 'label552');" onmouseover="ContentPreview('label553');" onmouseout="ContentUnpreview('label553');" title="click to collapse or expand..."> more... </a>
 <div id="label553" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sslvpn_ems_sn_check</span> <b>(Alias name: sslvpn-ems-sn-check)</b>  Enable/disable verification of ems serial number in ssl-vpn connection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label554' href="javascript:ContentClick('label555', 'label554');" onmouseover="ContentPreview('label555');" onmouseout="ContentUnpreview('label555');" title="click to collapse or expand..."> more... </a>
 <div id="label555" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">user_server_cert</span> <b>(Alias name: user-server-cert)</b>  Certificate to use for https user authentication. <span class="li-normal">type: list</span>
 <a id='label556' href="javascript:ContentClick('label557', 'label556');" onmouseover="ContentPreview('label557');" onmouseout="ContentUnpreview('label557');" title="click to collapse or expand..."> more... </a>
 <div id="label557" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_allow_default_hostname</span> <b>(Alias name: gui-allow-default-hostname)</b>  Enable/disable the factory default hostname warning on the gui setup wizard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label558' href="javascript:ContentClick('label559', 'label558');" onmouseover="ContentPreview('label559');" onmouseout="ContentUnpreview('label559');" title="click to collapse or expand..."> more... </a>
 <div id="label559" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_re_authentication_mode</span> <b>(Alias name: proxy-re-authentication-mode)</b>  Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was first created. <span class="li-normal">type: str</span> <span class="li-normal">choices: [session, traffic, absolute]</span> 
 <a id='label560' href="javascript:ContentClick('label561', 'label560');" onmouseover="ContentPreview('label561');" onmouseout="ContentUnpreview('label561');" title="click to collapse or expand..."> more... </a>
 <div id="label561" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipsec_soft_dec_async</span> <b>(Alias name: ipsec-soft-dec-async)</b>  Enable/disable software decryption asynchronization (using multiple cpus to do decryption) for ipsec vpn traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label562' href="javascript:ContentClick('label563', 'label562');" onmouseover="ContentPreview('label563');" onmouseout="ContentUnpreview('label563');" title="click to collapse or expand..."> more... </a>
 <div id="label563" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">admin_maintainer</span> <b>(Alias name: admin-maintainer)</b>  Enable/disable maintainer administrator login. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label564' href="javascript:ContentClick('label565', 'label564');" onmouseover="ContentPreview('label565');" onmouseout="ContentUnpreview('label565');" title="click to collapse or expand..."> more... </a>
 <div id="label565" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dst</span> Enable/disable daylight saving time. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label566' href="javascript:ContentClick('label567', 'label566');" onmouseover="ContentPreview('label567');" onmouseout="ContentUnpreview('label567');" title="click to collapse or expand..."> more... </a>
 <div id="label567" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_port</span> <b>(Alias name: fec-port)</b>  Local udp port for forward error correction (49152 - 65535). <span class="li-normal">type: int</span>
 <a id='label568' href="javascript:ContentClick('label569', 'label568');" onmouseover="ContentPreview('label569');" onmouseout="ContentUnpreview('label569');" title="click to collapse or expand..."> more... </a>
 <div id="label569" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_kex_sha1</span> <b>(Alias name: ssh-kex-sha1)</b>  Enable/disable sha1 key exchange for ssh access. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label570' href="javascript:ContentClick('label571', 'label570');" onmouseover="ContentPreview('label571');" onmouseout="ContentUnpreview('label571');" title="click to collapse or expand..."> more... </a>
 <div id="label571" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_mac_weak</span> <b>(Alias name: ssh-mac-weak)</b>  Enable/disable hmac-sha1 and umac-64-etm for ssh access. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label572' href="javascript:ContentClick('label573', 'label572');" onmouseover="ContentPreview('label573');" onmouseout="ContentUnpreview('label573');" title="click to collapse or expand..."> more... </a>
 <div id="label573" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sslvpn_cipher_hardware_acceleration</span> <b>(Alias name: sslvpn-cipher-hardware-acceleration)</b>  Enable/disable ssl-vpn hardware acceleration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label574' href="javascript:ContentClick('label575', 'label574');" onmouseover="ContentPreview('label575');" onmouseout="ContentUnpreview('label575');" title="click to collapse or expand..."> more... </a>
 <div id="label575" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sys_file_check_interval</span> <b>(Alias name: sys-file-check-interval)</b>  Set scheduled system file checking interval in minutes (10 - 10080 min, default = 60, 0 = disabled). <span class="li-normal">type: int</span>
 <a id='label576' href="javascript:ContentClick('label577', 'label576');" onmouseover="ContentPreview('label577');" onmouseout="ContentUnpreview('label577');" title="click to collapse or expand..."> more... </a>
 <div id="label577" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_hmac_md5</span> <b>(Alias name: ssh-hmac-md5)</b>  Enable/disable hmac-md5 for ssh access. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label578' href="javascript:ContentClick('label579', 'label578');" onmouseover="ContentPreview('label579');" onmouseout="ContentUnpreview('label579');" title="click to collapse or expand..."> more... </a>
 <div id="label579" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_cbc_cipher</span> <b>(Alias name: ssh-cbc-cipher)</b>  Enable/disable cbc cipher for ssh access. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label580' href="javascript:ContentClick('label581', 'label580');" onmouseover="ContentPreview('label581');" onmouseout="ContentUnpreview('label581');" title="click to collapse or expand..."> more... </a>
 <div id="label581" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_fortiguard_resource_fetch</span> <b>(Alias name: gui-fortiguard-resource-fetch)</b>  Enable/disable retrieving static gui resources from fortiguard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label582' href="javascript:ContentClick('label583', 'label582');" onmouseover="ContentPreview('label583');" onmouseout="ContentUnpreview('label583');" title="click to collapse or expand..."> more... </a>
 <div id="label583" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sslvpn_kxp_hardware_acceleration</span> <b>(Alias name: sslvpn-kxp-hardware-acceleration)</b>  Enable/disable ssl-vpn kxp hardware acceleration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label584' href="javascript:ContentClick('label585', 'label584');" onmouseover="ContentPreview('label585');" onmouseout="ContentUnpreview('label585');" title="click to collapse or expand..."> more... </a>
 <div id="label585" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sslvpn_plugin_version_check</span> <b>(Alias name: sslvpn-plugin-version-check)</b>  Enable/disable checking browsers plugin version by ssl-vpn. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label586' href="javascript:ContentClick('label587', 'label586');" onmouseover="ContentPreview('label587');" onmouseout="ContentUnpreview('label587');" title="click to collapse or expand..."> more... </a>
 <div id="label587" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiipam_integration</span> <b>(Alias name: fortiipam-integration)</b>  Enable/disable integration with the fortiipam cloud service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label588' href="javascript:ContentClick('label589', 'label588');" onmouseover="ContentPreview('label589');" onmouseout="ContentUnpreview('label589');" title="click to collapse or expand..."> more... </a>
 <div id="label589" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_firmware_upgrade_setup_warning</span> <b>(Alias name: gui-firmware-upgrade-setup-warning)</b>  Gui firmware upgrade setup warning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label590' href="javascript:ContentClick('label591', 'label590');" onmouseover="ContentPreview('label591');" onmouseout="ContentUnpreview('label591');" title="click to collapse or expand..."> more... </a>
 <div id="label591" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_uuid_policy</span> <b>(Alias name: log-uuid-policy)</b>  Enable/disable insertion of policy uuids to traffic logs. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label592' href="javascript:ContentClick('label593', 'label592');" onmouseover="ContentPreview('label593');" onmouseout="ContentUnpreview('label593');" title="click to collapse or expand..."> more... </a>
 <div id="label593" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">per_user_bwl</span> <b>(Alias name: per-user-bwl)</b>  Enable/disable per-user black/white list filter. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label594' href="javascript:ContentClick('label595', 'label594');" onmouseover="ContentPreview('label595');" onmouseout="ContentUnpreview('label595');" title="click to collapse or expand..."> more... </a>
 <div id="label595" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_fortisandbox_cloud</span> <b>(Alias name: gui-fortisandbox-cloud)</b>  Enable/disable displaying fortisandbox cloud on the gui. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label596' href="javascript:ContentClick('label597', 'label596');" onmouseover="ContentPreview('label597');" onmouseout="ContentUnpreview('label597');" title="click to collapse or expand..."> more... </a>
 <div id="label597" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortitoken_cloud_service</span> <b>(Alias name: fortitoken-cloud-service)</b>  Fortitoken cloud service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label598' href="javascript:ContentClick('label599', 'label598');" onmouseover="ContentPreview('label599');" onmouseout="ContentUnpreview('label599');" title="click to collapse or expand..."> more... </a>
 <div id="label599" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hw_switch_ether_filter</span> <b>(Alias name: hw-switch-ether-filter)</b>  Enable/disable hardware filter for certain ethernet packet types. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label600' href="javascript:ContentClick('label601', 'label600');" onmouseover="ContentPreview('label601');" onmouseout="ContentUnpreview('label601');" title="click to collapse or expand..."> more... </a>
 <div id="label601" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">virtual_server_count</span> <b>(Alias name: virtual-server-count)</b>  Maximum number of virtual server processes to create. <span class="li-normal">type: int</span>
 <a id='label602' href="javascript:ContentClick('label603', 'label602');" onmouseover="ContentPreview('label603');" onmouseout="ContentUnpreview('label603');" title="click to collapse or expand..."> more... </a>
 <div id="label603" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">endpoint_control_fds_access</span> <b>(Alias name: endpoint-control-fds-access)</b>  Endpoint control fds access. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label604' href="javascript:ContentClick('label605', 'label604');" onmouseover="ContentPreview('label605');" onmouseout="ContentUnpreview('label605');" title="click to collapse or expand..."> more... </a>
 <div id="label605" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_cipher_hardware_acceleration</span> <b>(Alias name: proxy-cipher-hardware-acceleration)</b>  Enable/disable using content processor (cp8 or cp9) hardware acceleration to encrypt and decrypt ipsec and ssl traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label606' href="javascript:ContentClick('label607', 'label606');" onmouseover="ContentPreview('label607');" onmouseout="ContentUnpreview('label607');" title="click to collapse or expand..."> more... </a>
 <div id="label607" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_kxp_hardware_acceleration</span> <b>(Alias name: proxy-kxp-hardware-acceleration)</b>  Enable/disable using the content processor to accelerate kxp traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label608' href="javascript:ContentClick('label609', 'label608');" onmouseover="ContentPreview('label609');" onmouseout="ContentUnpreview('label609');" title="click to collapse or expand..."> more... </a>
 <div id="label609" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">virtual_server_hardware_acceleration</span> <b>(Alias name: virtual-server-hardware-acceleration)</b>  Enable/disable virtual server hardware acceleration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label610' href="javascript:ContentClick('label611', 'label610');" onmouseover="ContentPreview('label611');" onmouseout="ContentUnpreview('label611');" title="click to collapse or expand..."> more... </a>
 <div id="label611" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
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
      - name: Configure global attributes.
        fortinet.fortimanager.fmgr_devprof_system_global:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          devprof: <your own value>
          devprof_system_global:
            admin_https_redirect: <value in [disable, enable]>
            admin_port: <integer>
            admin_scp: <value in [disable, enable]>
            admin_sport: <integer>
            admin_ssh_port: <integer>
            admin_ssh_v1: <value in [disable, enable]>
            admin_telnet_port: <integer>
            admintimeout: <integer>
            gui_ipv6: <value in [disable, enable]>
            gui_lines_per_page: <integer>
            gui_theme: <value in [blue, green, melongene, ...]>
            language: <value in [english, simch, japanese, ...]>
            switch_controller: <value in [disable, enable]>
            gui_device_latitude: <string>
            gui_device_longitude: <string>
            hostname: <string>
            timezone: <list or string>
            check_reset_range: <value in [disable, strict]>
            pmtu_discovery: <value in [disable, enable]>
            gui_allow_incompatible_fabric_fgt: <value in [disable, enable]>
            admin_restrict_local: <value in [disable, enable]>
            gui_workflow_management: <value in [disable, enable]>
            send_pmtu_icmp: <value in [disable, enable]>
            tcp_halfclose_timer: <integer>
            admin_server_cert: <list or string>
            dnsproxy_worker_count: <integer>
            show_backplane_intf: <value in [disable, enable]>
            gui_custom_language: <value in [disable, enable]>
            ldapconntimeout: <integer>
            auth_https_port: <integer>
            revision_backup_on_logout: <value in [disable, enable]>
            arp_max_entry: <integer>
            long_vdom_name: <value in [disable, enable]>
            pre_login_banner: <value in [disable, enable]>
            qsfpdd_split8_port: <list or string>
            max_route_cache_size: <integer>
            fortitoken_cloud_push_status: <value in [disable, enable]>
            ssh_hostkey_override: <value in [disable, enable]>
            proxy_hardware_acceleration: <value in [disable, enable]>
            switch_controller_reserved_network: <list or string>
            ssd_trim_date: <integer>
            wad_worker_count: <integer>
            ssh_hostkey: <string>
            wireless_controller_port: <integer>
            fgd_alert_subscription:
              - advisory
              - latest-threat
              - latest-virus
              - latest-attack
              - new-antivirus-db
              - new-attack-db
            forticontroller_proxy_port: <integer>
            dh_params: <value in [1024, 1536, 2048, ...]>
            memory_use_threshold_green: <integer>
            proxy_cert_use_mgmt_vdom: <value in [disable, enable]>
            proxy_auth_lifetime_timeout: <integer>
            gui_auto_upgrade_setup_warning: <value in [disable, enable]>
            gui_cdn_usage: <value in [disable, enable]>
            two_factor_email_expiry: <integer>
            udp_idle_timer: <integer>
            interface_subnet_usage: <value in [disable, enable]>
            forticontroller_proxy: <value in [disable, enable]>
            ssh_enc_algo:
              - chacha20-poly1305@openssh.com
              - aes128-ctr
              - aes192-ctr
              - aes256-ctr
              - arcfour256
              - arcfour128
              - aes128-cbc
              - 3des-cbc
              - blowfish-cbc
              - cast128-cbc
              - aes192-cbc
              - aes256-cbc
              - arcfour
              - rijndael-cbc@lysator.liu.se
              - aes128-gcm@openssh.com
              - aes256-gcm@openssh.com
            block_session_timer: <integer>
            quic_pmtud: <value in [disable, enable]>
            admin_https_ssl_ciphersuites:
              - TLS-AES-128-GCM-SHA256
              - TLS-AES-256-GCM-SHA384
              - TLS-CHACHA20-POLY1305-SHA256
              - TLS-AES-128-CCM-SHA256
              - TLS-AES-128-CCM-8-SHA256
            security_rating_result_submission: <value in [disable, enable]>
            user_device_store_max_unified_mem: <integer>
            management_port: <integer>
            fortigslb_integration: <value in [disable, enable]>
            admin_https_ssl_versions:
              - tlsv1-0
              - tlsv1-1
              - tlsv1-2
              - sslv3
              - tlsv1-3
            cert_chain_max: <integer>
            qsfp28_40g_port: <list or string>
            strong_crypto: <value in [disable, enable]>
            multi_factor_authentication: <value in [optional, mandatory]>
            fds_statistics: <value in [disable, enable]>
            gui_display_hostname: <value in [disable, enable]>
            two_factor_ftk_expiry: <integer>
            wad_source_affinity: <value in [disable, enable]>
            ssl_static_key_ciphers: <value in [disable, enable]>
            daily_restart: <value in [disable, enable]>
            snat_route_change: <value in [disable, enable]>
            tcp_rst_timer: <integer>
            anti_replay: <value in [disable, loose, strict]>
            ssl_min_proto_version: <value in [TLSv1, TLSv1-1, TLSv1-2, ...]>
            speedtestd_server_port: <integer>
            cpu_use_threshold: <integer>
            admin_host: <string>
            csr_ca_attribute: <value in [disable, enable]>
            fortiservice_port: <integer>
            ssd_trim_hour: <integer>
            purdue_level: <value in [1, 2, 3, ...]>
            management_vdom: <list or string>
            quic_ack_thresold: <integer>
            qsfpdd_100g_port: <list or string>
            ips_affinity: <string>
            vip_arp_range: <value in [restricted, unlimited]>
            internet_service_database: <value in [mini, standard, full, ...]>
            revision_image_auto_backup: <value in [disable, enable]>
            sflowd_max_children_num: <integer>
            admin_https_pki_required: <value in [disable, enable]>
            special_file_23_support: <value in [disable, enable]>
            npu_neighbor_update: <value in [disable, enable]>
            log_single_cpu_high: <value in [disable, enable]>
            management_ip: <string>
            proxy_resource_mode: <value in [disable, enable]>
            admin_ble_button: <value in [disable, enable]>
            gui_firmware_upgrade_warning: <value in [disable, enable]>
            dp_tcp_normal_timer: <integer>
            ipv6_allow_traffic_redirect: <value in [disable, enable]>
            cli_audit_log: <value in [disable, enable]>
            memory_use_threshold_extreme: <integer>
            ha_affinity: <string>
            restart_time: <string>
            speedtestd_ctrl_port: <integer>
            gui_wireless_opensecurity: <value in [disable, enable]>
            memory_use_threshold_red: <integer>
            dp_fragment_timer: <integer>
            wad_restart_start_time: <string>
            proxy_re_authentication_time: <integer>
            gui_app_detection_sdwan: <value in [disable, enable]>
            scanunit_count: <integer>
            tftp: <value in [disable, enable]>
            xstools_update_frequency: <integer>
            clt_cert_req: <value in [disable, enable]>
            fortiextender_vlan_mode: <value in [disable, enable]>
            auth_http_port: <integer>
            per_user_bal: <value in [disable, enable]>
            gui_date_format: <value in [yyyy/MM/dd, dd/MM/yyyy, MM/dd/yyyy, ...]>
            log_uuid_address: <value in [disable, enable]>
            cloud_communication: <value in [disable, enable]>
            lldp_reception: <value in [disable, enable]>
            two_factor_ftm_expiry: <integer>
            quic_udp_payload_size_shaping_per_cid: <value in [disable, enable]>
            autorun_log_fsck: <value in [disable, enable]>
            vpn_ems_sn_check: <value in [disable, enable]>
            admin_ssh_password: <value in [disable, enable]>
            airplane_mode: <value in [disable, enable]>
            batch_cmdb: <value in [disable, enable]>
            ip_src_port_range: <list or string>
            strict_dirty_session_check: <value in [disable, enable]>
            user_device_store_max_devices: <integer>
            dp_udp_idle_timer: <integer>
            internal_switch_speed:
              - auto
              - 10full
              - 10half
              - 100full
              - 100half
              - 1000full
              - 1000auto
            forticonverter_config_upload: <value in [disable, once]>
            ipsec_round_robin: <value in [disable, enable]>
            wad_affinity: <string>
            wifi_ca_certificate: <list or string>
            wimax_4g_usb: <value in [disable, enable]>
            miglog_affinity: <string>
            faz_disk_buffer_size: <integer>
            ssh_kex_algo:
              - diffie-hellman-group1-sha1
              - diffie-hellman-group14-sha1
              - diffie-hellman-group-exchange-sha1
              - diffie-hellman-group-exchange-sha256
              - curve25519-sha256@libssh.org
              - ecdh-sha2-nistp256
              - ecdh-sha2-nistp384
              - ecdh-sha2-nistp521
              - diffie-hellman-group14-sha256
              - diffie-hellman-group16-sha512
              - diffie-hellman-group18-sha512
            auto_auth_extension_device: <value in [disable, enable]>
            forticarrier_bypass: <value in [disable, enable]>
            reset_sessionless_tcp: <value in [disable, enable]>
            early_tcp_npu_session: <value in [disable, enable]>
            http_unauthenticated_request_limit: <integer>
            gui_local_out: <value in [disable, enable]>
            tcp_option: <value in [disable, enable]>
            proxy_auth_timeout: <integer>
            fortiextender_discovery_lockdown: <value in [disable, enable]>
            lldp_transmission: <value in [disable, enable]>
            split_port: <list or string>
            gui_certificates: <value in [disable, enable]>
            cfg_save: <value in [automatic, manual, revert]>
            auth_keepalive: <value in [disable, enable]>
            split_port_mode:
              -
                interface: <string>
                split_mode: <value in [disable, 4x10G, 4x25G, ...]>
            admin_forticloud_sso_login: <value in [disable, enable]>
            post_login_banner: <value in [disable, enable]>
            br_fdb_max_entry: <integer>
            ip_fragment_mem_thresholds: <integer>
            fortiextender_provision_on_authorization: <value in [disable, enable]>
            reboot_upon_config_restore: <value in [disable, enable]>
            syslog_affinity: <string>
            fortiextender_data_port: <integer>
            quic_tls_handshake_timeout: <integer>
            forticonverter_integration: <value in [disable, enable]>
            proxy_keep_alive_mode: <value in [session, traffic, re-authentication]>
            cmdbsvr_affinity: <string>
            wad_memory_change_granularity: <integer>
            dhcp_lease_backup_interval: <integer>
            check_protocol_header: <value in [loose, strict]>
            av_failopen_session: <value in [disable, enable]>
            ipsec_ha_seqjump_rate: <integer>
            admin_hsts_max_age: <integer>
            igmp_state_limit: <integer>
            admin_login_max: <integer>
            ipv6_allow_multicast_probe: <value in [disable, enable]>
            virtual_switch_vlan: <value in [disable, enable]>
            admin_lockout_threshold: <integer>
            dp_pinhole_timer: <integer>
            wireless_controller: <value in [disable, enable]>
            bfd_affinity: <string>
            ssd_trim_freq: <value in [daily, weekly, monthly, ...]>
            two_factor_sms_expiry: <integer>
            traffic_priority: <value in [tos, dscp]>
            proxy_and_explicit_proxy: <value in [disable, enable]>
            sslvpn_web_mode: <value in [disable, enable]>
            ssh_hostkey_password: <list or string>
            wad_csvc_db_count: <integer>
            ipv6_allow_anycast_probe: <value in [disable, enable]>
            honor_df: <value in [disable, enable]>
            hyper_scale_vdom_num: <integer>
            wad_csvc_cs_count: <integer>
            internal_switch_mode: <value in [switch, interface, hub]>
            cfg_revert_timeout: <integer>
            admin_concurrent: <value in [disable, enable]>
            ipv6_allow_local_in_silent_drop: <value in [disable, enable]>
            tcp_halfopen_timer: <integer>
            dp_rsync_timer: <integer>
            management_port_use_admin_sport: <value in [disable, enable]>
            gui_forticare_registration_setup_warning: <value in [disable, enable]>
            gui_replacement_message_groups: <value in [disable, enable]>
            security_rating_run_on_schedule: <value in [disable, enable]>
            admin_lockout_duration: <integer>
            optimize_flow_mode: <value in [disable, enable]>
            private_data_encryption: <value in [disable, enable]>
            wireless_mode: <value in [ac, client, wtp, ...]>
            alias: <string>
            ssh_hostkey_algo:
              - ssh-rsa
              - ecdsa-sha2-nistp521
              - rsa-sha2-256
              - rsa-sha2-512
              - ssh-ed25519
              - ecdsa-sha2-nistp384
              - ecdsa-sha2-nistp256
            fortitoken_cloud: <value in [disable, enable]>
            av_affinity: <string>
            proxy_worker_count: <integer>
            ipsec_asic_offload: <value in [disable, enable]>
            miglogd_children: <integer>
            sslvpn_max_worker_count: <integer>
            ssh_mac_algo:
              - hmac-md5
              - hmac-md5-etm@openssh.com
              - hmac-md5-96
              - hmac-md5-96-etm@openssh.com
              - hmac-sha1
              - hmac-sha1-etm@openssh.com
              - hmac-sha2-256
              - hmac-sha2-256-etm@openssh.com
              - hmac-sha2-512
              - hmac-sha2-512-etm@openssh.com
              - hmac-ripemd160
              - hmac-ripemd160@openssh.com
              - hmac-ripemd160-etm@openssh.com
              - umac-64@openssh.com
              - umac-128@openssh.com
              - umac-64-etm@openssh.com
              - umac-128-etm@openssh.com
            url_filter_count: <integer>
            wifi_certificate: <list or string>
            radius_port: <integer>
            sys_perf_log_interval: <integer>
            gui_fortigate_cloud_sandbox: <value in [disable, enable]>
            auth_cert: <list or string>
            fortiextender: <value in [disable, enable]>
            admin_reset_button: <value in [disable, enable]>
            av_failopen: <value in [off, pass, one-shot, ...]>
            user_device_store_max_users: <integer>
            auth_session_limit: <value in [block-new, logout-inactive]>
            ipv6_allow_local_in_slient_drop: <value in [disable, enable]>
            quic_congestion_control_algo: <value in [cubic, bbr, bbr2, ...]>
            auth_ike_saml_port: <integer>
            wad_restart_end_time: <string>
            http_request_limit: <integer>
            irq_time_accounting: <value in [auto, force]>
            remoteauthtimeout: <integer>
            admin_https_ssl_banned_ciphers:
              - RSA
              - DHE
              - ECDHE
              - DSS
              - ECDSA
              - AES
              - AESGCM
              - CAMELLIA
              - 3DES
              - SHA1
              - SHA256
              - SHA384
              - STATIC
              - CHACHA20
              - ARIA
              - AESCCM
            allow_traffic_redirect: <value in [disable, enable]>
            legacy_poe_device_support: <value in [disable, enable]>
            wad_restart_mode: <value in [none, time, memory]>
            fds_statistics_period: <integer>
            admin_telnet: <value in [disable, enable]>
            ipv6_accept_dad: <integer>
            tcp_timewait_timer: <integer>
            admin_console_timeout: <integer>
            default_service_source_port: <string>
            quic_max_datagram_size: <integer>
            refresh: <integer>
            extender_controller_reserved_network: <list or string>
            url_filter_affinity: <string>
            policy_auth_concurrent: <integer>
            ipsec_hmac_offload: <value in [disable, enable]>
            traffic_priority_level: <value in [high, medium, low]>
            ipsec_qat_offload: <value in [disable, enable]>
            ssd_trim_min: <integer>
            gui_date_time_source: <value in [system, browser]>
            log_ssl_connection: <value in [disable, enable]>
            ndp_max_entry: <integer>
            vdom_mode: <value in [no-vdom, multi-vdom, split-vdom]>
            internet_service_download_list: <list or string>
            fortitoken_cloud_sync_interval: <integer>
            ssd_trim_weekday: <value in [sunday, monday, tuesday, ...]>
            two_factor_fac_expiry: <integer>
            gui_rest_api_cache: <value in [disable, enable]>
            admin_forticloud_sso_default_profile: <list or string>
            proxy_auth_lifetime: <value in [disable, enable]>
            device_idle_timeout: <integer>
            login_timestamp: <value in [disable, enable]>
            speedtest_server: <value in [disable, enable]>
            edit_vdom_prompt: <value in [disable, enable]>
            gui_cdn_domain_override: <string>
            admin_ssh_grace_time: <integer>
            sslvpn_ems_sn_check: <value in [disable, enable]>
            user_server_cert: <list or string>
            gui_allow_default_hostname: <value in [disable, enable]>
            proxy_re_authentication_mode: <value in [session, traffic, absolute]>
            ipsec_soft_dec_async: <value in [disable, enable]>
            admin_maintainer: <value in [disable, enable]>
            dst: <value in [disable, enable]>
            fec_port: <integer>
            ssh_kex_sha1: <value in [disable, enable]>
            ssh_mac_weak: <value in [disable, enable]>
            sslvpn_cipher_hardware_acceleration: <value in [disable, enable]>
            sys_file_check_interval: <integer>
            ssh_hmac_md5: <value in [disable, enable]>
            ssh_cbc_cipher: <value in [disable, enable]>
            gui_fortiguard_resource_fetch: <value in [disable, enable]>
            sslvpn_kxp_hardware_acceleration: <value in [disable, enable]>
            sslvpn_plugin_version_check: <value in [disable, enable]>
            fortiipam_integration: <value in [disable, enable]>
            gui_firmware_upgrade_setup_warning: <value in [disable, enable]>
            log_uuid_policy: <value in [disable, enable]>
            per_user_bwl: <value in [disable, enable]>
            gui_fortisandbox_cloud: <value in [disable, enable]>
            fortitoken_cloud_service: <value in [disable, enable]>
            hw_switch_ether_filter: <value in [disable, enable]>
            virtual_server_count: <integer>
            endpoint_control_fds_access: <value in [disable, enable]>
            proxy_cipher_hardware_acceleration: <value in [disable, enable]>
            proxy_kxp_hardware_acceleration: <value in [disable, enable]>
            virtual_server_hardware_acceleration: <value in [disable, enable]>


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
