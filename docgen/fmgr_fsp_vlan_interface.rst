:source: fmgr_fsp_vlan_interface.py

:orphan:

.. _fmgr_fsp_vlan_interface:

fmgr_fsp_vlan_interface -- Configure interfaces.
++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vlan</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">fsp_vlan_interface</span> - Configure interfaces. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ac_name</span> <b>(Alias name: ac-name)</b>  Ac name. <span class="li-normal">type: str</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">aggregate</span> Aggregate. <span class="li-normal">type: str</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">algorithm</span> Algorithm. <span class="li-normal">type: str</span> <span class="li-normal">choices: [L2, L3, L4, LB, Source-MAC]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">alias</span> Alias. <span class="li-normal">type: str</span>
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">allowaccess</span> Allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_discover</span> <b>(Alias name: ap-discover)</b>  Ap discover. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">arpforward</span> Arpforward. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">atm_protocol</span> <b>(Alias name: atm-protocol)</b>  Atm protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, ipoa]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_type</span> <b>(Alias name: auth-type)</b>  Auth type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_auth_extension_device</span> <b>(Alias name: auto-auth-extension-device)</b>  Auto auth extension device. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bfd</span> Bfd. <span class="li-normal">type: str</span> <span class="li-normal">choices: [global, enable, disable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bfd_desired_min_tx</span> <b>(Alias name: bfd-desired-min-tx)</b>  Bfd desired min tx. <span class="li-normal">type: int</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bfd_detect_mult</span> <b>(Alias name: bfd-detect-mult)</b>  Bfd detect mult. <span class="li-normal">type: int</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bfd_required_min_rx</span> <b>(Alias name: bfd-required-min-rx)</b>  Bfd required min rx. <span class="li-normal">type: int</span>
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">broadcast_forticlient_discovery</span> <b>(Alias name: broadcast-forticlient-discovery)</b>  Broadcast forticlient discovery. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">broadcast_forward</span> <b>(Alias name: broadcast-forward)</b>  Broadcast forward. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal</span> <b>(Alias name: captive-portal)</b>  Captive portal. <span class="li-normal">type: int</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cli_conn_status</span> <b>(Alias name: cli-conn-status)</b>  Cli conn status. <span class="li-normal">type: int</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">color</span> Color. <span class="li-normal">type: int</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns</span> Ddns. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_auth</span> <b>(Alias name: ddns-auth)</b>  Ddns auth. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, tsig]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_domain</span> <b>(Alias name: ddns-domain)</b>  Ddns domain. <span class="li-normal">type: str</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_key</span> <b>(Alias name: ddns-key)</b>  Ddns key. <span class="li-normal">type: list or str</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_keyname</span> <b>(Alias name: ddns-keyname)</b>  Ddns keyname. <span class="li-normal">type: str</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_password</span> <b>(Alias name: ddns-password)</b>  Ddns password. <span class="li-normal">type: list</span>
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_server</span> <b>(Alias name: ddns-server)</b>  Ddns server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [dhs.org, dyndns.org, dyns.net, tzo.com, ods.org, vavic.com, now.net.cn, dipdns.net, easydns.com, genericDDNS]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_server_ip</span> <b>(Alias name: ddns-server-ip)</b>  Ddns server ip. <span class="li-normal">type: str</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_sn</span> <b>(Alias name: ddns-sn)</b>  Ddns sn. <span class="li-normal">type: str</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_ttl</span> <b>(Alias name: ddns-ttl)</b>  Ddns ttl. <span class="li-normal">type: int</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_username</span> <b>(Alias name: ddns-username)</b>  Ddns username. <span class="li-normal">type: str</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_zone</span> <b>(Alias name: ddns-zone)</b>  Ddns zone. <span class="li-normal">type: str</span>
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dedicated_to</span> <b>(Alias name: dedicated-to)</b>  Dedicated to. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, management]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">defaultgw</span> Defaultgw. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">description</span> Description. <span class="li-normal">type: str</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">detected_peer_mtu</span> <b>(Alias name: detected-peer-mtu)</b>  Detected peer mtu. <span class="li-normal">type: int</span>
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">detectprotocol</span> Detectprotocol. <span class="li-normal">type: list</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">detectserver</span> Detectserver. <span class="li-normal">type: str</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">device_access_list</span> <b>(Alias name: device-access-list)</b>  Device access list. <span class="li-normal">type: list or str</span>
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">device_identification</span> <b>(Alias name: device-identification)</b>  Device identification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">device_identification_active_scan</span> <b>(Alias name: device-identification-active-scan)</b>  Device identification active scan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">device_netscan</span> <b>(Alias name: device-netscan)</b>  Device netscan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">device_user_identification</span> <b>(Alias name: device-user-identification)</b>  Device user identification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">devindex</span> Devindex. <span class="li-normal">type: int</span>
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_client_identifier</span> <b>(Alias name: dhcp-client-identifier)</b>  Dhcp client identifier. <span class="li-normal">type: str</span>
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_agent_option</span> <b>(Alias name: dhcp-relay-agent-option)</b>  Dhcp relay agent option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_ip</span> <b>(Alias name: dhcp-relay-ip)</b>  Dhcp relay ip. <span class="li-normal">type: list</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_service</span> <b>(Alias name: dhcp-relay-service)</b>  Dhcp relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_type</span> <b>(Alias name: dhcp-relay-type)</b>  Dhcp relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular, ipsec]</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_renew_time</span> <b>(Alias name: dhcp-renew-time)</b>  Dhcp renew time. <span class="li-normal">type: int</span>
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">disc_retry_timeout</span> <b>(Alias name: disc-retry-timeout)</b>  Disc retry timeout. <span class="li-normal">type: int</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">disconnect_threshold</span> <b>(Alias name: disconnect-threshold)</b>  Disconnect threshold. <span class="li-normal">type: int</span>
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">distance</span> Distance. <span class="li-normal">type: int</span>
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dns_query</span> <b>(Alias name: dns-query)</b>  Dns query. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, recursive, non-recursive]</span> 
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dns_server_override</span> <b>(Alias name: dns-server-override)</b>  Dns server override. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">drop_fragment</span> <b>(Alias name: drop-fragment)</b>  Drop fragment. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">drop_overlapped_fragment</span> <b>(Alias name: drop-overlapped-fragment)</b>  Drop overlapped fragment. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">egress_cos</span> <b>(Alias name: egress-cos)</b>  Egress cos. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">egress_shaping_profile</span> <b>(Alias name: egress-shaping-profile)</b>  Egress shaping profile. <span class="li-normal">type: str</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">endpoint_compliance</span> <b>(Alias name: endpoint-compliance)</b>  Endpoint compliance. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">estimated_downstream_bandwidth</span> <b>(Alias name: estimated-downstream-bandwidth)</b>  Estimated downstream bandwidth. <span class="li-normal">type: int</span>
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">estimated_upstream_bandwidth</span> <b>(Alias name: estimated-upstream-bandwidth)</b>  Estimated upstream bandwidth. <span class="li-normal">type: int</span>
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">explicit_ftp_proxy</span> <b>(Alias name: explicit-ftp-proxy)</b>  Explicit ftp proxy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">explicit_web_proxy</span> <b>(Alias name: explicit-web-proxy)</b>  Explicit web proxy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external</span> External. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fail_action_on_extender</span> <b>(Alias name: fail-action-on-extender)</b>  Fail action on extender. <span class="li-normal">type: str</span> <span class="li-normal">choices: [soft-restart, hard-restart, reboot]</span> 
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fail_alert_interfaces</span> <b>(Alias name: fail-alert-interfaces)</b>  Fail alert interfaces. <span class="li-normal">type: list or str</span>
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fail_alert_method</span> <b>(Alias name: fail-alert-method)</b>  Fail alert method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [link-failed-signal, link-down]</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fail_detect</span> <b>(Alias name: fail-detect)</b>  Fail detect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fail_detect_option</span> <b>(Alias name: fail-detect-option)</b>  Fail detect option. <span class="li-normal">type: list</span> <span class="li-normal">choices: [detectserver, link-down]</span> 
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fdp</span> Fdp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiheartbeat</span> Fortiheartbeat. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortilink</span> Fortilink. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortilink_backup_link</span> <b>(Alias name: fortilink-backup-link)</b>  Fortilink backup link. <span class="li-normal">type: int</span>
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortilink_split_interface</span> <b>(Alias name: fortilink-split-interface)</b>  Fortilink split interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortilink_stacking</span> <b>(Alias name: fortilink-stacking)</b>  Fortilink stacking. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forward_domain</span> <b>(Alias name: forward-domain)</b>  Forward domain. <span class="li-normal">type: int</span>
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forward_error_correction</span> <b>(Alias name: forward-error-correction)</b>  Forward error correction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, rs-fec, base-r-fec, fec-cl91, fec-cl74, rs-544, none, cl91-rs-fec, cl74-fc-fec, auto, rs-fec544]</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fp_anomaly</span> <b>(Alias name: fp-anomaly)</b>  Fp anomaly. <span class="li-normal">type: list</span> <span class="li-normal">choices: [drop_tcp_fin_noack, pass_winnuke, pass_tcpland, pass_udpland, pass_icmpland, pass_ipland, pass_iprr, pass_ipssrr, pass_iplsrr, pass_ipstream, pass_ipsecurity, pass_iptimestamp, pass_ipunknown_option, pass_ipunknown_prot, pass_icmp_frag, pass_tcp_no_flag, pass_tcp_fin_noack, drop_winnuke, drop_tcpland, drop_udpland, drop_icmpland, drop_ipland, drop_iprr, drop_ipssrr, drop_iplsrr, drop_ipstream, drop_ipsecurity, drop_iptimestamp, drop_ipunknown_option, drop_ipunknown_prot, drop_icmp_frag, drop_tcp_no_flag]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fp_disable</span> <b>(Alias name: fp-disable)</b>  Fp disable. <span class="li-normal">type: list</span> <span class="li-normal">choices: [all, ipsec, none]</span> 
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gateway_address</span> <b>(Alias name: gateway-address)</b>  Gateway address. <span class="li-normal">type: str</span>
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gi_gk</span> <b>(Alias name: gi-gk)</b>  Gi gk. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gwaddr</span> Gwaddr. <span class="li-normal">type: str</span>
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">gwdetect</span> Gwdetect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ha_priority</span> <b>(Alias name: ha-priority)</b>  Ha priority. <span class="li-normal">type: int</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">icmp_accept_redirect</span> <b>(Alias name: icmp-accept-redirect)</b>  Icmp accept redirect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">icmp_redirect</span> <b>(Alias name: icmp-redirect)</b>  Icmp redirect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">icmp_send_redirect</span> <b>(Alias name: icmp-send-redirect)</b>  Icmp send redirect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ident_accept</span> <b>(Alias name: ident-accept)</b>  Ident accept. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">idle_timeout</span> <b>(Alias name: idle-timeout)</b>  Idle timeout. <span class="li-normal">type: int</span>
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">if_mdix</span> <b>(Alias name: if-mdix)</b>  If mdix. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, normal, crossover]</span> 
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">if_media</span> <b>(Alias name: if-media)</b>  If media. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, copper, fiber]</span> 
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">in_force_vlan_cos</span> <b>(Alias name: in-force-vlan-cos)</b>  In force vlan cos. <span class="li-normal">type: int</span>
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">inbandwidth</span> Inbandwidth. <span class="li-normal">type: int</span>
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ingress_cos</span> <b>(Alias name: ingress-cos)</b>  Ingress cos. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span> 
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ingress_spillover_threshold</span> <b>(Alias name: ingress-spillover-threshold)</b>  Ingress spillover threshold. <span class="li-normal">type: int</span>
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internal</span> Internal. <span class="li-normal">type: int</span>
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ip. <span class="li-normal">type: str</span>
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipmac</span> Ipmac. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ips_sniffer_mode</span> <b>(Alias name: ips-sniffer-mode)</b>  Ips sniffer mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipunnumbered</span> Ipunnumbered. <span class="li-normal">type: str</span>
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6</span> Ipv6. <span class="li-normal">type: dict</span>
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autoconf</span> Autoconf. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_client_options</span> <b>(Alias name: dhcp6-client-options)</b>  Dhcp6 client options. <span class="li-normal">type: list</span> <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span> 
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_information_request</span> <b>(Alias name: dhcp6-information-request)</b>  Dhcp6 information request. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_delegation</span> <b>(Alias name: dhcp6-prefix-delegation)</b>  Dhcp6 prefix delegation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_hint</span> <b>(Alias name: dhcp6-prefix-hint)</b>  Dhcp6 prefix hint. <span class="li-normal">type: str</span>
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_hint_plt</span> <b>(Alias name: dhcp6-prefix-hint-plt)</b>  Dhcp6 prefix hint plt. <span class="li-normal">type: int</span>
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_hint_vlt</span> <b>(Alias name: dhcp6-prefix-hint-vlt)</b>  Dhcp6 prefix hint vlt. <span class="li-normal">type: int</span>
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_ip</span> <b>(Alias name: dhcp6-relay-ip)</b>  Dhcp6 relay ip. <span class="li-normal">type: str</span>
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_service</span> <b>(Alias name: dhcp6-relay-service)</b>  Dhcp6 relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_type</span> <b>(Alias name: dhcp6-relay-type)</b>  Dhcp6 relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular]</span> 
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_address</span> <b>(Alias name: ip6-address)</b>  Ip6 address. <span class="li-normal">type: str</span>
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_allowaccess</span> <b>(Alias name: ip6-allowaccess)</b>  Ip6 allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric]</span> 
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_default_life</span> <b>(Alias name: ip6-default-life)</b>  Ip6 default life. <span class="li-normal">type: int</span>
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_dns_server_override</span> <b>(Alias name: ip6-dns-server-override)</b>  Ip6 dns server override. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_hop_limit</span> <b>(Alias name: ip6-hop-limit)</b>  Ip6 hop limit. <span class="li-normal">type: int</span>
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_link_mtu</span> <b>(Alias name: ip6-link-mtu)</b>  Ip6 link mtu. <span class="li-normal">type: int</span>
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_manage_flag</span> <b>(Alias name: ip6-manage-flag)</b>  Ip6 manage flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_max_interval</span> <b>(Alias name: ip6-max-interval)</b>  Ip6 max interval. <span class="li-normal">type: int</span>
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_min_interval</span> <b>(Alias name: ip6-min-interval)</b>  Ip6 min interval. <span class="li-normal">type: int</span>
 <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_mode</span> <b>(Alias name: ip6-mode)</b>  Ip6 mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span> 
 <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_other_flag</span> <b>(Alias name: ip6-other-flag)</b>  Ip6 other flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_reachable_time</span> <b>(Alias name: ip6-reachable-time)</b>  Ip6 reachable time. <span class="li-normal">type: int</span>
 <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_retrans_time</span> <b>(Alias name: ip6-retrans-time)</b>  Ip6 retrans time. <span class="li-normal">type: int</span>
 <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_send_adv</span> <b>(Alias name: ip6-send-adv)</b>  Ip6 send adv. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_subnet</span> <b>(Alias name: ip6-subnet)</b>  Ip6 subnet. <span class="li-normal">type: str</span>
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_upstream_interface</span> <b>(Alias name: ip6-upstream-interface)</b>  Ip6 upstream interface. <span class="li-normal">type: str</span>
 <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_cert</span> <b>(Alias name: nd-cert)</b>  Nd cert. <span class="li-normal">type: str</span>
 <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_cga_modifier</span> <b>(Alias name: nd-cga-modifier)</b>  Nd cga modifier. <span class="li-normal">type: str</span>
 <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_mode</span> <b>(Alias name: nd-mode)</b>  Nd mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [basic, SEND-compatible]</span> 
 <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_security_level</span> <b>(Alias name: nd-security-level)</b>  Nd security level. <span class="li-normal">type: int</span>
 <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_timestamp_delta</span> <b>(Alias name: nd-timestamp-delta)</b>  Nd timestamp delta. <span class="li-normal">type: int</span>
 <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_timestamp_fuzz</span> <b>(Alias name: nd-timestamp-fuzz)</b>  Nd timestamp fuzz. <span class="li-normal">type: int</span>
 <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrip6_link_local</span> Vrip6 link local. <span class="li-normal">type: str</span>
 <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrrp_virtual_mac6</span> <b>(Alias name: vrrp-virtual-mac6)</b>  Vrrp virtual mac6. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_delegated_prefix_list</span> <b>(Alias name: ip6-delegated-prefix-list)</b>  Ip6 delegated prefix list. <span class="li-normal">type: list</span>
 <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous_flag</span> <b>(Alias name: autonomous-flag)</b>  Autonomous flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">onlink_flag</span> <b>(Alias name: onlink-flag)</b>  Onlink flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">prefix_id</span> <b>(Alias name: prefix-id)</b>  Prefix id. <span class="li-normal">type: int</span>
 <a id='label276' href="javascript:ContentClick('label277', 'label276');" onmouseover="ContentPreview('label277');" onmouseout="ContentUnpreview('label277');" title="click to collapse or expand..."> more... </a>
 <div id="label277" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> Rdnss. <span class="li-normal">type: list</span>
 <a id='label278' href="javascript:ContentClick('label279', 'label278');" onmouseover="ContentPreview('label279');" onmouseout="ContentUnpreview('label279');" title="click to collapse or expand..."> more... </a>
 <div id="label279" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss_service</span> <b>(Alias name: rdnss-service)</b>  Rdnss service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [delegated, default, specify]</span> 
 <a id='label280' href="javascript:ContentClick('label281', 'label280');" onmouseover="ContentPreview('label281');" onmouseout="ContentUnpreview('label281');" title="click to collapse or expand..."> more... </a>
 <div id="label281" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">subnet</span> Subnet. <span class="li-normal">type: str</span>
 <a id='label282' href="javascript:ContentClick('label283', 'label282');" onmouseover="ContentPreview('label283');" onmouseout="ContentUnpreview('label283');" title="click to collapse or expand..."> more... </a>
 <div id="label283" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">upstream_interface</span> <b>(Alias name: upstream-interface)</b>  Upstream interface. <span class="li-normal">type: str</span>
 <a id='label284' href="javascript:ContentClick('label285', 'label284');" onmouseover="ContentPreview('label285');" onmouseout="ContentUnpreview('label285');" title="click to collapse or expand..."> more... </a>
 <div id="label285" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">delegated_prefix_iaid</span> <b>(Alias name: delegated-prefix-iaid)</b>  Iaid of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>
 <a id='label286' href="javascript:ContentClick('label287', 'label286');" onmouseover="ContentPreview('label287');" onmouseout="ContentUnpreview('label287');" title="click to collapse or expand..."> more... </a>
 <div id="label287" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ip6_extra_addr</span> <b>(Alias name: ip6-extra-addr)</b>  Ip6 extra addr. <span class="li-normal">type: list</span>
 <a id='label288' href="javascript:ContentClick('label289', 'label288');" onmouseover="ContentPreview('label289');" onmouseout="ContentUnpreview('label289');" title="click to collapse or expand..."> more... </a>
 <div id="label289" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">prefix</span> Prefix. <span class="li-normal">type: str</span>
 <a id='label290' href="javascript:ContentClick('label291', 'label290');" onmouseover="ContentPreview('label291');" onmouseout="ContentUnpreview('label291');" title="click to collapse or expand..."> more... </a>
 <div id="label291" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ip6_prefix_list</span> <b>(Alias name: ip6-prefix-list)</b>  Ip6 prefix list. <span class="li-normal">type: list</span>
 <a id='label292' href="javascript:ContentClick('label293', 'label292');" onmouseover="ContentPreview('label293');" onmouseout="ContentUnpreview('label293');" title="click to collapse or expand..."> more... </a>
 <div id="label293" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous_flag</span> <b>(Alias name: autonomous-flag)</b>  Autonomous flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label294' href="javascript:ContentClick('label295', 'label294');" onmouseover="ContentPreview('label295');" onmouseout="ContentUnpreview('label295');" title="click to collapse or expand..."> more... </a>
 <div id="label295" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dnssl</span> Dnssl. <span class="li-normal">type: list</span>
 <a id='label296' href="javascript:ContentClick('label297', 'label296');" onmouseover="ContentPreview('label297');" onmouseout="ContentUnpreview('label297');" title="click to collapse or expand..."> more... </a>
 <div id="label297" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">onlink_flag</span> <b>(Alias name: onlink-flag)</b>  Onlink flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label298' href="javascript:ContentClick('label299', 'label298');" onmouseover="ContentPreview('label299');" onmouseout="ContentUnpreview('label299');" title="click to collapse or expand..."> more... </a>
 <div id="label299" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">preferred_life_time</span> <b>(Alias name: preferred-life-time)</b>  Preferred life time. <span class="li-normal">type: int</span>
 <a id='label300' href="javascript:ContentClick('label301', 'label300');" onmouseover="ContentPreview('label301');" onmouseout="ContentUnpreview('label301');" title="click to collapse or expand..."> more... </a>
 <div id="label301" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">prefix</span> Prefix. <span class="li-normal">type: str</span>
 <a id='label302' href="javascript:ContentClick('label303', 'label302');" onmouseover="ContentPreview('label303');" onmouseout="ContentUnpreview('label303');" title="click to collapse or expand..."> more... </a>
 <div id="label303" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> Rdnss. <span class="li-normal">type: list</span>
 <a id='label304' href="javascript:ContentClick('label305', 'label304');" onmouseover="ContentPreview('label305');" onmouseout="ContentUnpreview('label305');" title="click to collapse or expand..."> more... </a>
 <div id="label305" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">valid_life_time</span> <b>(Alias name: valid-life-time)</b>  Valid life time. <span class="li-normal">type: int</span>
 <a id='label306' href="javascript:ContentClick('label307', 'label306');" onmouseover="ContentPreview('label307');" onmouseout="ContentUnpreview('label307');" title="click to collapse or expand..."> more... </a>
 <div id="label307" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">vrrp6</span> Vrrp6. <span class="li-normal">type: list</span>
 <a id='label308' href="javascript:ContentClick('label309', 'label308');" onmouseover="ContentPreview('label309');" onmouseout="ContentUnpreview('label309');" title="click to collapse or expand..."> more... </a>
 <div id="label309" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">accept_mode</span> <b>(Alias name: accept-mode)</b>  Accept mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label310' href="javascript:ContentClick('label311', 'label310');" onmouseover="ContentPreview('label311');" onmouseout="ContentUnpreview('label311');" title="click to collapse or expand..."> more... </a>
 <div id="label311" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adv_interval</span> <b>(Alias name: adv-interval)</b>  Adv interval. <span class="li-normal">type: int</span>
 <a id='label312' href="javascript:ContentClick('label313', 'label312');" onmouseover="ContentPreview('label313');" onmouseout="ContentUnpreview('label313');" title="click to collapse or expand..."> more... </a>
 <div id="label313" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">preempt</span> Preempt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label314' href="javascript:ContentClick('label315', 'label314');" onmouseover="ContentPreview('label315');" onmouseout="ContentUnpreview('label315');" title="click to collapse or expand..."> more... </a>
 <div id="label315" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Priority. <span class="li-normal">type: int</span>
 <a id='label316' href="javascript:ContentClick('label317', 'label316');" onmouseover="ContentPreview('label317');" onmouseout="ContentUnpreview('label317');" title="click to collapse or expand..."> more... </a>
 <div id="label317" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">start_time</span> <b>(Alias name: start-time)</b>  Start time. <span class="li-normal">type: int</span>
 <a id='label318' href="javascript:ContentClick('label319', 'label318');" onmouseover="ContentPreview('label319');" onmouseout="ContentUnpreview('label319');" title="click to collapse or expand..."> more... </a>
 <div id="label319" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label320' href="javascript:ContentClick('label321', 'label320');" onmouseover="ContentPreview('label321');" onmouseout="ContentUnpreview('label321');" title="click to collapse or expand..."> more... </a>
 <div id="label321" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrdst6</span> Vrdst6. <span class="li-normal">type: str</span>
 <a id='label322' href="javascript:ContentClick('label323', 'label322');" onmouseover="ContentPreview('label323');" onmouseout="ContentUnpreview('label323');" title="click to collapse or expand..."> more... </a>
 <div id="label323" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrgrp</span> Vrgrp. <span class="li-normal">type: int</span>
 <a id='label324' href="javascript:ContentClick('label325', 'label324');" onmouseover="ContentPreview('label325');" onmouseout="ContentUnpreview('label325');" title="click to collapse or expand..."> more... </a>
 <div id="label325" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrid</span> Vrid. <span class="li-normal">type: int</span>
 <a id='label326' href="javascript:ContentClick('label327', 'label326');" onmouseover="ContentPreview('label327');" onmouseout="ContentUnpreview('label327');" title="click to collapse or expand..."> more... </a>
 <div id="label327" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrip6</span> Vrip6. <span class="li-normal">type: str</span>
 <a id='label328' href="javascript:ContentClick('label329', 'label328');" onmouseover="ContentPreview('label329');" onmouseout="ContentUnpreview('label329');" title="click to collapse or expand..."> more... </a>
 <div id="label329" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ignore_default_route</span> <b>(Alias name: ignore-default-route)</b>  Enable/disable ignoring of default route when checking destination. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label330' href="javascript:ContentClick('label331', 'label330');" onmouseover="ContentPreview('label331');" onmouseout="ContentUnpreview('label331');" title="click to collapse or expand..."> more... </a>
 <div id="label331" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrdst_priority</span> <b>(Alias name: vrdst-priority)</b>  Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254). <span class="li-normal">type: int</span>
 <a id='label332' href="javascript:ContentClick('label333', 'label332');" onmouseover="ContentPreview('label333');" onmouseout="ContentUnpreview('label333');" title="click to collapse or expand..."> more... </a>
 <div id="label333" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">interface_identifier</span> <b>(Alias name: interface-identifier)</b>  Interface identifier. <span class="li-normal">type: str</span>
 <a id='label334' href="javascript:ContentClick('label335', 'label334');" onmouseover="ContentPreview('label335');" onmouseout="ContentUnpreview('label335');" title="click to collapse or expand..."> more... </a>
 <div id="label335" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">unique_autoconf_addr</span> <b>(Alias name: unique-autoconf-addr)</b>  Unique autoconf addr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label336' href="javascript:ContentClick('label337', 'label336');" onmouseover="ContentPreview('label337');" onmouseout="ContentUnpreview('label337');" title="click to collapse or expand..."> more... </a>
 <div id="label337" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">icmp6_send_redirect</span> <b>(Alias name: icmp6-send-redirect)</b>  Enable/disable sending of icmpv6 redirects. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label338' href="javascript:ContentClick('label339', 'label338');" onmouseover="ContentPreview('label339');" onmouseout="ContentUnpreview('label339');" title="click to collapse or expand..."> more... </a>
 <div id="label339" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cli_conn6_status</span> <b>(Alias name: cli-conn6-status)</b>  Cli conn6 status. <span class="li-normal">type: int</span>
 <a id='label340' href="javascript:ContentClick('label341', 'label340');" onmouseover="ContentPreview('label341');" onmouseout="ContentUnpreview('label341');" title="click to collapse or expand..."> more... </a>
 <div id="label341" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_prefix_mode</span> <b>(Alias name: ip6-prefix-mode)</b>  Assigning a prefix from dhcp or ra. <span class="li-normal">type: str</span> <span class="li-normal">choices: [dhcp6, ra]</span> 
 <a id='label342' href="javascript:ContentClick('label343', 'label342');" onmouseover="ContentPreview('label343');" onmouseout="ContentUnpreview('label343');" title="click to collapse or expand..."> more... </a>
 <div id="label343" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ra_send_mtu</span> <b>(Alias name: ra-send-mtu)</b>  Enable/disable sending link mtu in ra packet. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label344' href="javascript:ContentClick('label345', 'label344');" onmouseover="ContentPreview('label345');" onmouseout="ContentUnpreview('label345');" title="click to collapse or expand..."> more... </a>
 <div id="label345" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_delegated_prefix_iaid</span> <b>(Alias name: ip6-delegated-prefix-iaid)</b>  Iaid of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>
 <a id='label346' href="javascript:ContentClick('label347', 'label346');" onmouseover="ContentPreview('label347');" onmouseout="ContentUnpreview('label347');" title="click to collapse or expand..."> more... </a>
 <div id="label347" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_source_interface</span> <b>(Alias name: dhcp6-relay-source-interface)</b>  Enable/disable use of address on this interface as the source address of the relay message. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label348' href="javascript:ContentClick('label349', 'label348');" onmouseover="ContentPreview('label349');" onmouseout="ContentUnpreview('label349');" title="click to collapse or expand..."> more... </a>
 <div id="label349" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_interface_id</span> <b>(Alias name: dhcp6-relay-interface-id)</b>  Dhcp6 relay interface id. <span class="li-normal">type: str</span>
 <a id='label350' href="javascript:ContentClick('label351', 'label350');" onmouseover="ContentPreview('label351');" onmouseout="ContentUnpreview('label351');" title="click to collapse or expand..."> more... </a>
 <div id="label351" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_source_ip</span> <b>(Alias name: dhcp6-relay-source-ip)</b>  Ipv6 address used by the dhcp6 relay as its source ip. <span class="li-normal">type: str</span>
 <a id='label352' href="javascript:ContentClick('label353', 'label352');" onmouseover="ContentPreview('label353');" onmouseout="ContentUnpreview('label353');" title="click to collapse or expand..."> more... </a>
 <div id="label353" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_adv_rio</span> <b>(Alias name: ip6-adv-rio)</b>  Enable/disable sending advertisements with route information option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label354' href="javascript:ContentClick('label355', 'label354');" onmouseover="ContentPreview('label355');" onmouseout="ContentUnpreview('label355');" title="click to collapse or expand..."> more... </a>
 <div id="label355" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_route_pref</span> <b>(Alias name: ip6-route-pref)</b>  Set route preference to the interface (default = medium). <span class="li-normal">type: str</span> <span class="li-normal">choices: [medium, high, low]</span> 
 <a id='label356' href="javascript:ContentClick('label357', 'label356');" onmouseover="ContentPreview('label357');" onmouseout="ContentUnpreview('label357');" title="click to collapse or expand..."> more... </a>
 <div id="label357" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">l2forward</span> L2forward. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label358' href="javascript:ContentClick('label359', 'label358');" onmouseover="ContentPreview('label359');" onmouseout="ContentUnpreview('label359');" title="click to collapse or expand..."> more... </a>
 <div id="label359" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">l2tp_client</span> <b>(Alias name: l2tp-client)</b>  L2tp client. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label360' href="javascript:ContentClick('label361', 'label360');" onmouseover="ContentPreview('label361');" onmouseout="ContentUnpreview('label361');" title="click to collapse or expand..."> more... </a>
 <div id="label361" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lacp_ha_slave</span> <b>(Alias name: lacp-ha-slave)</b>  Lacp ha slave. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label362' href="javascript:ContentClick('label363', 'label362');" onmouseover="ContentPreview('label363');" onmouseout="ContentUnpreview('label363');" title="click to collapse or expand..."> more... </a>
 <div id="label363" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lacp_mode</span> <b>(Alias name: lacp-mode)</b>  Lacp mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, passive, active]</span> 
 <a id='label364' href="javascript:ContentClick('label365', 'label364');" onmouseover="ContentPreview('label365');" onmouseout="ContentUnpreview('label365');" title="click to collapse or expand..."> more... </a>
 <div id="label365" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lacp_speed</span> <b>(Alias name: lacp-speed)</b>  Lacp speed. <span class="li-normal">type: str</span> <span class="li-normal">choices: [slow, fast]</span> 
 <a id='label366' href="javascript:ContentClick('label367', 'label366');" onmouseover="ContentPreview('label367');" onmouseout="ContentUnpreview('label367');" title="click to collapse or expand..."> more... </a>
 <div id="label367" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lcp_echo_interval</span> <b>(Alias name: lcp-echo-interval)</b>  Lcp echo interval. <span class="li-normal">type: int</span>
 <a id='label368' href="javascript:ContentClick('label369', 'label368');" onmouseover="ContentPreview('label369');" onmouseout="ContentUnpreview('label369');" title="click to collapse or expand..."> more... </a>
 <div id="label369" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lcp_max_echo_fails</span> <b>(Alias name: lcp-max-echo-fails)</b>  Lcp max echo fails. <span class="li-normal">type: int</span>
 <a id='label370' href="javascript:ContentClick('label371', 'label370');" onmouseover="ContentPreview('label371');" onmouseout="ContentUnpreview('label371');" title="click to collapse or expand..."> more... </a>
 <div id="label371" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">link_up_delay</span> <b>(Alias name: link-up-delay)</b>  Link up delay. <span class="li-normal">type: int</span>
 <a id='label372' href="javascript:ContentClick('label373', 'label372');" onmouseover="ContentPreview('label373');" onmouseout="ContentUnpreview('label373');" title="click to collapse or expand..."> more... </a>
 <div id="label373" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">listen_forticlient_connection</span> <b>(Alias name: listen-forticlient-connection)</b>  Listen forticlient connection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label374' href="javascript:ContentClick('label375', 'label374');" onmouseover="ContentPreview('label375');" onmouseout="ContentUnpreview('label375');" title="click to collapse or expand..."> more... </a>
 <div id="label375" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lldp_network_policy</span> <b>(Alias name: lldp-network-policy)</b>  Lldp network policy. <span class="li-normal">type: str</span>
 <a id='label376' href="javascript:ContentClick('label377', 'label376');" onmouseover="ContentPreview('label377');" onmouseout="ContentUnpreview('label377');" title="click to collapse or expand..."> more... </a>
 <div id="label377" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lldp_reception</span> <b>(Alias name: lldp-reception)</b>  Lldp reception. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, vdom]</span> 
 <a id='label378' href="javascript:ContentClick('label379', 'label378');" onmouseover="ContentPreview('label379');" onmouseout="ContentUnpreview('label379');" title="click to collapse or expand..."> more... </a>
 <div id="label379" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lldp_transmission</span> <b>(Alias name: lldp-transmission)</b>  Lldp transmission. <span class="li-normal">type: str</span> <span class="li-normal">choices: [enable, disable, vdom]</span> 
 <a id='label380' href="javascript:ContentClick('label381', 'label380');" onmouseover="ContentPreview('label381');" onmouseout="ContentUnpreview('label381');" title="click to collapse or expand..."> more... </a>
 <div id="label381" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log</span> Log. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label382' href="javascript:ContentClick('label383', 'label382');" onmouseover="ContentPreview('label383');" onmouseout="ContentUnpreview('label383');" title="click to collapse or expand..."> more... </a>
 <div id="label383" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">macaddr</span> Macaddr. <span class="li-normal">type: str</span>
 <a id='label384' href="javascript:ContentClick('label385', 'label384');" onmouseover="ContentPreview('label385');" onmouseout="ContentUnpreview('label385');" title="click to collapse or expand..."> more... </a>
 <div id="label385" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">management_ip</span> <b>(Alias name: management-ip)</b>  Management ip. <span class="li-normal">type: str</span>
 <a id='label386' href="javascript:ContentClick('label387', 'label386');" onmouseover="ContentPreview('label387');" onmouseout="ContentUnpreview('label387');" title="click to collapse or expand..."> more... </a>
 <div id="label387" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_egress_burst_rate</span> <b>(Alias name: max-egress-burst-rate)</b>  Max egress burst rate. <span class="li-normal">type: int</span>
 <a id='label388' href="javascript:ContentClick('label389', 'label388');" onmouseover="ContentPreview('label389');" onmouseout="ContentUnpreview('label389');" title="click to collapse or expand..."> more... </a>
 <div id="label389" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_egress_rate</span> <b>(Alias name: max-egress-rate)</b>  Max egress rate. <span class="li-normal">type: int</span>
 <a id='label390' href="javascript:ContentClick('label391', 'label390');" onmouseover="ContentPreview('label391');" onmouseout="ContentUnpreview('label391');" title="click to collapse or expand..."> more... </a>
 <div id="label391" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mediatype</span> Mediatype. <span class="li-normal">type: str</span> <span class="li-normal">choices: [serdes-sfp, sgmii-sfp, cfp2-sr10, cfp2-lr4, serdes-copper-sfp, sr, cr, lr, qsfp28-sr4, qsfp28-lr4, qsfp28-cr4, sr4, cr4, lr4, none, gmii, sgmii, sr2, lr2, cr2, sr8, lr8, cr8, dr]</span> 
 <a id='label392' href="javascript:ContentClick('label393', 'label392');" onmouseover="ContentPreview('label393');" onmouseout="ContentUnpreview('label393');" title="click to collapse or expand..."> more... </a>
 <div id="label393" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">member</span> Member. <span class="li-normal">type: list or str</span>
 <a id='label394' href="javascript:ContentClick('label395', 'label394');" onmouseover="ContentPreview('label395');" onmouseout="ContentUnpreview('label395');" title="click to collapse or expand..."> more... </a>
 <div id="label395" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">min_links</span> <b>(Alias name: min-links)</b>  Min links. <span class="li-normal">type: int</span>
 <a id='label396' href="javascript:ContentClick('label397', 'label396');" onmouseover="ContentPreview('label397');" onmouseout="ContentUnpreview('label397');" title="click to collapse or expand..."> more... </a>
 <div id="label397" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">min_links_down</span> <b>(Alias name: min-links-down)</b>  Min links down. <span class="li-normal">type: str</span> <span class="li-normal">choices: [operational, administrative]</span> 
 <a id='label398' href="javascript:ContentClick('label399', 'label398');" onmouseover="ContentPreview('label399');" onmouseout="ContentUnpreview('label399');" title="click to collapse or expand..."> more... </a>
 <div id="label399" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mode</span> Mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, dhcp, pppoe, pppoa, ipoa, eoa]</span> 
 <a id='label400' href="javascript:ContentClick('label401', 'label400');" onmouseover="ContentPreview('label401');" onmouseout="ContentUnpreview('label401');" title="click to collapse or expand..."> more... </a>
 <div id="label401" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mtu</span> Mtu. <span class="li-normal">type: int</span>
 <a id='label402' href="javascript:ContentClick('label403', 'label402');" onmouseover="ContentPreview('label403');" onmouseout="ContentUnpreview('label403');" title="click to collapse or expand..."> more... </a>
 <div id="label403" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mtu_override</span> <b>(Alias name: mtu-override)</b>  Mtu override. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label404' href="javascript:ContentClick('label405', 'label404');" onmouseover="ContentPreview('label405');" onmouseout="ContentUnpreview('label405');" title="click to collapse or expand..."> more... </a>
 <div id="label405" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mux_type</span> <b>(Alias name: mux-type)</b>  Mux type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [llc-encaps, vc-encaps]</span> 
 <a id='label406' href="javascript:ContentClick('label407', 'label406');" onmouseover="ContentPreview('label407');" onmouseout="ContentUnpreview('label407');" title="click to collapse or expand..."> more... </a>
 <div id="label407" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Name. <span class="li-normal">type: str</span>
 <a id='label408' href="javascript:ContentClick('label409', 'label408');" onmouseover="ContentPreview('label409');" onmouseout="ContentUnpreview('label409');" title="click to collapse or expand..."> more... </a>
 <div id="label409" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ndiscforward</span> Ndiscforward. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label410' href="javascript:ContentClick('label411', 'label410');" onmouseover="ContentPreview('label411');" onmouseout="ContentUnpreview('label411');" title="click to collapse or expand..."> more... </a>
 <div id="label411" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">netbios_forward</span> <b>(Alias name: netbios-forward)</b>  Netbios forward. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label412' href="javascript:ContentClick('label413', 'label412');" onmouseover="ContentPreview('label413');" onmouseout="ContentUnpreview('label413');" title="click to collapse or expand..."> more... </a>
 <div id="label413" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">netflow_sampler</span> <b>(Alias name: netflow-sampler)</b>  Netflow sampler. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, tx, rx, both]</span> 
 <a id='label414' href="javascript:ContentClick('label415', 'label414');" onmouseover="ContentPreview('label415');" onmouseout="ContentUnpreview('label415');" title="click to collapse or expand..."> more... </a>
 <div id="label415" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">npu_fastpath</span> <b>(Alias name: npu-fastpath)</b>  Npu fastpath. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label416' href="javascript:ContentClick('label417', 'label416');" onmouseover="ContentPreview('label417');" onmouseout="ContentUnpreview('label417');" title="click to collapse or expand..."> more... </a>
 <div id="label417" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nst</span> Nst. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label418' href="javascript:ContentClick('label419', 'label418');" onmouseover="ContentPreview('label419');" onmouseout="ContentUnpreview('label419');" title="click to collapse or expand..."> more... </a>
 <div id="label419" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">out_force_vlan_cos</span> <b>(Alias name: out-force-vlan-cos)</b>  Out force vlan cos. <span class="li-normal">type: int</span>
 <a id='label420' href="javascript:ContentClick('label421', 'label420');" onmouseover="ContentPreview('label421');" onmouseout="ContentUnpreview('label421');" title="click to collapse or expand..."> more... </a>
 <div id="label421" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbandwidth</span> Outbandwidth. <span class="li-normal">type: int</span>
 <a id='label422' href="javascript:ContentClick('label423', 'label422');" onmouseover="ContentPreview('label423');" onmouseout="ContentUnpreview('label423');" title="click to collapse or expand..."> more... </a>
 <div id="label423" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">padt_retry_timeout</span> <b>(Alias name: padt-retry-timeout)</b>  Padt retry timeout. <span class="li-normal">type: int</span>
 <a id='label424' href="javascript:ContentClick('label425', 'label424');" onmouseover="ContentPreview('label425');" onmouseout="ContentUnpreview('label425');" title="click to collapse or expand..."> more... </a>
 <div id="label425" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">password</span> Password. <span class="li-normal">type: list</span>
 <a id='label426' href="javascript:ContentClick('label427', 'label426');" onmouseover="ContentPreview('label427');" onmouseout="ContentUnpreview('label427');" title="click to collapse or expand..."> more... </a>
 <div id="label427" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">peer_interface</span> <b>(Alias name: peer-interface)</b>  Peer interface. <span class="li-normal">type: list or str</span>
 <a id='label428' href="javascript:ContentClick('label429', 'label428');" onmouseover="ContentPreview('label429');" onmouseout="ContentUnpreview('label429');" title="click to collapse or expand..."> more... </a>
 <div id="label429" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">phy_mode</span> <b>(Alias name: phy-mode)</b>  Phy mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, adsl, vdsl, adsl-auto, vdsl2, adsl2+, adsl2, g.dmt, t1.413, g.lite, g-dmt, t1-413, g-lite]</span> 
 <a id='label430' href="javascript:ContentClick('label431', 'label430');" onmouseover="ContentPreview('label431');" onmouseout="ContentUnpreview('label431');" title="click to collapse or expand..."> more... </a>
 <div id="label431" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ping_serv_status</span> <b>(Alias name: ping-serv-status)</b>  Ping serv status. <span class="li-normal">type: int</span>
 <a id='label432' href="javascript:ContentClick('label433', 'label432');" onmouseover="ContentPreview('label433');" onmouseout="ContentUnpreview('label433');" title="click to collapse or expand..."> more... </a>
 <div id="label433" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">poe</span> Poe. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label434' href="javascript:ContentClick('label435', 'label434');" onmouseover="ContentPreview('label435');" onmouseout="ContentUnpreview('label435');" title="click to collapse or expand..."> more... </a>
 <div id="label435" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">polling_interval</span> <b>(Alias name: polling-interval)</b>  Polling interval. <span class="li-normal">type: int</span>
 <a id='label436' href="javascript:ContentClick('label437', 'label436');" onmouseover="ContentPreview('label437');" onmouseout="ContentUnpreview('label437');" title="click to collapse or expand..."> more... </a>
 <div id="label437" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pppoe_unnumbered_negotiate</span> <b>(Alias name: pppoe-unnumbered-negotiate)</b>  Pppoe unnumbered negotiate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label438' href="javascript:ContentClick('label439', 'label438');" onmouseover="ContentPreview('label439');" onmouseout="ContentUnpreview('label439');" title="click to collapse or expand..."> more... </a>
 <div id="label439" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pptp_auth_type</span> <b>(Alias name: pptp-auth-type)</b>  Pptp auth type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span> 
 <a id='label440' href="javascript:ContentClick('label441', 'label440');" onmouseover="ContentPreview('label441');" onmouseout="ContentUnpreview('label441');" title="click to collapse or expand..."> more... </a>
 <div id="label441" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pptp_client</span> <b>(Alias name: pptp-client)</b>  Pptp client. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label442' href="javascript:ContentClick('label443', 'label442');" onmouseover="ContentPreview('label443');" onmouseout="ContentUnpreview('label443');" title="click to collapse or expand..."> more... </a>
 <div id="label443" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pptp_password</span> <b>(Alias name: pptp-password)</b>  Pptp password. <span class="li-normal">type: list</span>
 <a id='label444' href="javascript:ContentClick('label445', 'label444');" onmouseover="ContentPreview('label445');" onmouseout="ContentUnpreview('label445');" title="click to collapse or expand..."> more... </a>
 <div id="label445" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pptp_server_ip</span> <b>(Alias name: pptp-server-ip)</b>  Pptp server ip. <span class="li-normal">type: str</span>
 <a id='label446' href="javascript:ContentClick('label447', 'label446');" onmouseover="ContentPreview('label447');" onmouseout="ContentUnpreview('label447');" title="click to collapse or expand..."> more... </a>
 <div id="label447" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pptp_timeout</span> <b>(Alias name: pptp-timeout)</b>  Pptp timeout. <span class="li-normal">type: int</span>
 <a id='label448' href="javascript:ContentClick('label449', 'label448');" onmouseover="ContentPreview('label449');" onmouseout="ContentUnpreview('label449');" title="click to collapse or expand..."> more... </a>
 <div id="label449" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pptp_user</span> <b>(Alias name: pptp-user)</b>  Pptp user. <span class="li-normal">type: str</span>
 <a id='label450' href="javascript:ContentClick('label451', 'label450');" onmouseover="ContentPreview('label451');" onmouseout="ContentUnpreview('label451');" title="click to collapse or expand..."> more... </a>
 <div id="label451" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">preserve_session_route</span> <b>(Alias name: preserve-session-route)</b>  Preserve session route. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label452' href="javascript:ContentClick('label453', 'label452');" onmouseover="ContentPreview('label453');" onmouseout="ContentUnpreview('label453');" title="click to collapse or expand..."> more... </a>
 <div id="label453" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Priority. <span class="li-normal">type: int</span>
 <a id='label454' href="javascript:ContentClick('label455', 'label454');" onmouseover="ContentPreview('label455');" onmouseout="ContentUnpreview('label455');" title="click to collapse or expand..."> more... </a>
 <div id="label455" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority_override</span> <b>(Alias name: priority-override)</b>  Priority override. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label456' href="javascript:ContentClick('label457', 'label456');" onmouseover="ContentPreview('label457');" onmouseout="ContentUnpreview('label457');" title="click to collapse or expand..."> more... </a>
 <div id="label457" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_captive_portal</span> <b>(Alias name: proxy-captive-portal)</b>  Proxy captive portal. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label458' href="javascript:ContentClick('label459', 'label458');" onmouseover="ContentPreview('label459');" onmouseout="ContentUnpreview('label459');" title="click to collapse or expand..."> more... </a>
 <div id="label459" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">redundant_interface</span> <b>(Alias name: redundant-interface)</b>  Redundant interface. <span class="li-normal">type: str</span>
 <a id='label460' href="javascript:ContentClick('label461', 'label460');" onmouseover="ContentPreview('label461');" onmouseout="ContentUnpreview('label461');" title="click to collapse or expand..."> more... </a>
 <div id="label461" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_ip</span> <b>(Alias name: remote-ip)</b>  Remote ip. <span class="li-normal">type: str</span>
 <a id='label462' href="javascript:ContentClick('label463', 'label462');" onmouseover="ContentPreview('label463');" onmouseout="ContentUnpreview('label463');" title="click to collapse or expand..."> more... </a>
 <div id="label463" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">replacemsg_override_group</span> <b>(Alias name: replacemsg-override-group)</b>  Replacemsg override group. <span class="li-normal">type: str</span>
 <a id='label464' href="javascript:ContentClick('label465', 'label464');" onmouseover="ContentPreview('label465');" onmouseout="ContentUnpreview('label465');" title="click to collapse or expand..."> more... </a>
 <div id="label465" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">retransmission</span> Retransmission. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label466' href="javascript:ContentClick('label467', 'label466');" onmouseover="ContentPreview('label467');" onmouseout="ContentUnpreview('label467');" title="click to collapse or expand..."> more... </a>
 <div id="label467" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">role</span> Role. <span class="li-normal">type: str</span> <span class="li-normal">choices: [lan, wan, dmz, undefined]</span> 
 <a id='label468' href="javascript:ContentClick('label469', 'label468');" onmouseover="ContentPreview('label469');" onmouseout="ContentUnpreview('label469');" title="click to collapse or expand..."> more... </a>
 <div id="label469" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sample_direction</span> <b>(Alias name: sample-direction)</b>  Sample direction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [rx, tx, both]</span> 
 <a id='label470' href="javascript:ContentClick('label471', 'label470');" onmouseover="ContentPreview('label471');" onmouseout="ContentUnpreview('label471');" title="click to collapse or expand..."> more... </a>
 <div id="label471" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sample_rate</span> <b>(Alias name: sample-rate)</b>  Sample rate. <span class="li-normal">type: int</span>
 <a id='label472' href="javascript:ContentClick('label473', 'label472');" onmouseover="ContentPreview('label473');" onmouseout="ContentUnpreview('label473');" title="click to collapse or expand..."> more... </a>
 <div id="label473" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">scan_botnet_connections</span> <b>(Alias name: scan-botnet-connections)</b>  Scan botnet connections. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label474' href="javascript:ContentClick('label475', 'label474');" onmouseover="ContentPreview('label475');" onmouseout="ContentUnpreview('label475');" title="click to collapse or expand..."> more... </a>
 <div id="label475" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">secondary_IP</span> <b>(Alias name: secondary-IP)</b>  Secondary ip. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label476' href="javascript:ContentClick('label477', 'label476');" onmouseover="ContentPreview('label477');" onmouseout="ContentUnpreview('label477');" title="click to collapse or expand..."> more... </a>
 <div id="label477" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">secondaryip</span> Secondaryip. <span class="li-normal">type: list</span>
 <a id='label478' href="javascript:ContentClick('label479', 'label478');" onmouseover="ContentPreview('label479');" onmouseout="ContentUnpreview('label479');" title="click to collapse or expand..."> more... </a>
 <div id="label479" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> Allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test, icond, scim]</span> 
 <a id='label480' href="javascript:ContentClick('label481', 'label480');" onmouseover="ContentPreview('label481');" onmouseout="ContentUnpreview('label481');" title="click to collapse or expand..."> more... </a>
 <div id="label481" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">detectprotocol</span> Detectprotocol. <span class="li-normal">type: list</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> 
 <a id='label482' href="javascript:ContentClick('label483', 'label482');" onmouseover="ContentPreview('label483');" onmouseout="ContentUnpreview('label483');" title="click to collapse or expand..."> more... </a>
 <div id="label483" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">detectserver</span> Detectserver. <span class="li-normal">type: str</span>
 <a id='label484' href="javascript:ContentClick('label485', 'label484');" onmouseover="ContentPreview('label485');" onmouseout="ContentUnpreview('label485');" title="click to collapse or expand..."> more... </a>
 <div id="label485" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">gwdetect</span> Gwdetect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label486' href="javascript:ContentClick('label487', 'label486');" onmouseover="ContentPreview('label487');" onmouseout="ContentUnpreview('label487');" title="click to collapse or expand..."> more... </a>
 <div id="label487" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ha_priority</span> <b>(Alias name: ha-priority)</b>  Ha priority. <span class="li-normal">type: int</span>
 <a id='label488' href="javascript:ContentClick('label489', 'label488');" onmouseover="ContentPreview('label489');" onmouseout="ContentUnpreview('label489');" title="click to collapse or expand..."> more... </a>
 <div id="label489" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label490' href="javascript:ContentClick('label491', 'label490');" onmouseover="ContentPreview('label491');" onmouseout="ContentUnpreview('label491');" title="click to collapse or expand..."> more... </a>
 <div id="label491" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ip. <span class="li-normal">type: str</span>
 <a id='label492' href="javascript:ContentClick('label493', 'label492');" onmouseover="ContentPreview('label493');" onmouseout="ContentUnpreview('label493');" title="click to collapse or expand..."> more... </a>
 <div id="label493" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ping_serv_status</span> <b>(Alias name: ping-serv-status)</b>  Ping serv status. <span class="li-normal">type: int</span>
 <a id='label494' href="javascript:ContentClick('label495', 'label494');" onmouseover="ContentPreview('label495');" onmouseout="ContentUnpreview('label495');" title="click to collapse or expand..."> more... </a>
 <div id="label495" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">seq</span> Seq. <span class="li-normal">type: int</span>
 <a id='label496' href="javascript:ContentClick('label497', 'label496');" onmouseover="ContentPreview('label497');" onmouseout="ContentUnpreview('label497');" title="click to collapse or expand..."> more... </a>
 <div id="label497" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">secip_relay_ip</span> <b>(Alias name: secip-relay-ip)</b>  Dhcp relay ip address. <span class="li-normal">type: str</span>
 <a id='label498' href="javascript:ContentClick('label499', 'label498');" onmouseover="ContentPreview('label499');" onmouseout="ContentUnpreview('label499');" title="click to collapse or expand..."> more... </a>
 <div id="label499" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">security_8021x_dynamic_vlan_id</span> <b>(Alias name: security-8021x-dynamic-vlan-id)</b>  Security 8021x dynamic vlan id. <span class="li-normal">type: int</span>
 <a id='label500' href="javascript:ContentClick('label501', 'label500');" onmouseover="ContentPreview('label501');" onmouseout="ContentUnpreview('label501');" title="click to collapse or expand..."> more... </a>
 <div id="label501" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_8021x_master</span> <b>(Alias name: security-8021x-master)</b>  Security 8021x master. <span class="li-normal">type: str</span>
 <a id='label502' href="javascript:ContentClick('label503', 'label502');" onmouseover="ContentPreview('label503');" onmouseout="ContentUnpreview('label503');" title="click to collapse or expand..."> more... </a>
 <div id="label503" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_8021x_mode</span> <b>(Alias name: security-8021x-mode)</b>  Security 8021x mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, dynamic-vlan, fallback, slave]</span> 
 <a id='label504' href="javascript:ContentClick('label505', 'label504');" onmouseover="ContentPreview('label505');" onmouseout="ContentUnpreview('label505');" title="click to collapse or expand..."> more... </a>
 <div id="label505" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_exempt_list</span> <b>(Alias name: security-exempt-list)</b>  Security exempt list. <span class="li-normal">type: str</span>
 <a id='label506' href="javascript:ContentClick('label507', 'label506');" onmouseover="ContentPreview('label507');" onmouseout="ContentUnpreview('label507');" title="click to collapse or expand..."> more... </a>
 <div id="label507" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_external_logout</span> <b>(Alias name: security-external-logout)</b>  Security external logout. <span class="li-normal">type: str</span>
 <a id='label508' href="javascript:ContentClick('label509', 'label508');" onmouseover="ContentPreview('label509');" onmouseout="ContentUnpreview('label509');" title="click to collapse or expand..."> more... </a>
 <div id="label509" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_external_web</span> <b>(Alias name: security-external-web)</b>  Security external web. <span class="li-normal">type: str</span>
 <a id='label510' href="javascript:ContentClick('label511', 'label510');" onmouseover="ContentPreview('label511');" onmouseout="ContentUnpreview('label511');" title="click to collapse or expand..."> more... </a>
 <div id="label511" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_groups</span> <b>(Alias name: security-groups)</b>  Security groups. <span class="li-normal">type: list or str</span>
 <a id='label512' href="javascript:ContentClick('label513', 'label512');" onmouseover="ContentPreview('label513');" onmouseout="ContentUnpreview('label513');" title="click to collapse or expand..."> more... </a>
 <div id="label513" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_mac_auth_bypass</span> <b>(Alias name: security-mac-auth-bypass)</b>  Security mac auth bypass. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, mac-auth-only]</span> 
 <a id='label514' href="javascript:ContentClick('label515', 'label514');" onmouseover="ContentPreview('label515');" onmouseout="ContentUnpreview('label515');" title="click to collapse or expand..."> more... </a>
 <div id="label515" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_mode</span> <b>(Alias name: security-mode)</b>  Security mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, captive-portal, 802.1X]</span> 
 <a id='label516' href="javascript:ContentClick('label517', 'label516');" onmouseover="ContentPreview('label517');" onmouseout="ContentUnpreview('label517');" title="click to collapse or expand..."> more... </a>
 <div id="label517" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_redirect_url</span> <b>(Alias name: security-redirect-url)</b>  Security redirect url. <span class="li-normal">type: str</span>
 <a id='label518' href="javascript:ContentClick('label519', 'label518');" onmouseover="ContentPreview('label519');" onmouseout="ContentUnpreview('label519');" title="click to collapse or expand..."> more... </a>
 <div id="label519" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">service_name</span> <b>(Alias name: service-name)</b>  Service name. <span class="li-normal">type: str</span>
 <a id='label520' href="javascript:ContentClick('label521', 'label520');" onmouseover="ContentPreview('label521');" onmouseout="ContentUnpreview('label521');" title="click to collapse or expand..."> more... </a>
 <div id="label521" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sflow_sampler</span> <b>(Alias name: sflow-sampler)</b>  Sflow sampler. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label522' href="javascript:ContentClick('label523', 'label522');" onmouseover="ContentPreview('label523');" onmouseout="ContentUnpreview('label523');" title="click to collapse or expand..."> more... </a>
 <div id="label523" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">speed</span> Speed. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, 10full, 10half, 100full, 100half, 1000full, 1000half, 10000full, 1000auto, 10000auto, 40000full, 100Gfull, 25000full, 40000auto, 25000auto, 100Gauto, 400Gfull, 400Gauto, 50000full, 2500auto, 5000auto, 50000auto, 200Gfull, 200Gauto, 100auto]</span> 
 <a id='label524' href="javascript:ContentClick('label525', 'label524');" onmouseover="ContentPreview('label525');" onmouseout="ContentUnpreview('label525');" title="click to collapse or expand..."> more... </a>
 <div id="label525" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">spillover_threshold</span> <b>(Alias name: spillover-threshold)</b>  Spillover threshold. <span class="li-normal">type: int</span>
 <a id='label526' href="javascript:ContentClick('label527', 'label526');" onmouseover="ContentPreview('label527');" onmouseout="ContentUnpreview('label527');" title="click to collapse or expand..."> more... </a>
 <div id="label527" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">src_check</span> <b>(Alias name: src-check)</b>  Src check. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label528' href="javascript:ContentClick('label529', 'label528');" onmouseover="ContentPreview('label529');" onmouseout="ContentUnpreview('label529');" title="click to collapse or expand..."> more... </a>
 <div id="label529" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [down, up]</span> 
 <a id='label530' href="javascript:ContentClick('label531', 'label530');" onmouseover="ContentPreview('label531');" onmouseout="ContentUnpreview('label531');" title="click to collapse or expand..."> more... </a>
 <div id="label531" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">stp</span> Stp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label532' href="javascript:ContentClick('label533', 'label532');" onmouseover="ContentPreview('label533');" onmouseout="ContentUnpreview('label533');" title="click to collapse or expand..."> more... </a>
 <div id="label533" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">stp_ha_slave</span> <b>(Alias name: stp-ha-slave)</b>  Stp ha slave. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, priority-adjust]</span> 
 <a id='label534' href="javascript:ContentClick('label535', 'label534');" onmouseover="ContentPreview('label535');" onmouseout="ContentUnpreview('label535');" title="click to collapse or expand..."> more... </a>
 <div id="label535" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">stpforward</span> Stpforward. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label536' href="javascript:ContentClick('label537', 'label536');" onmouseover="ContentPreview('label537');" onmouseout="ContentUnpreview('label537');" title="click to collapse or expand..."> more... </a>
 <div id="label537" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">stpforward_mode</span> <b>(Alias name: stpforward-mode)</b>  Stpforward mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]</span> 
 <a id='label538' href="javascript:ContentClick('label539', 'label538');" onmouseover="ContentPreview('label539');" onmouseout="ContentUnpreview('label539');" title="click to collapse or expand..."> more... </a>
 <div id="label539" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">strip_priority_vlan_tag</span> <b>(Alias name: strip-priority-vlan-tag)</b>  Strip priority vlan tag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label540' href="javascript:ContentClick('label541', 'label540');" onmouseover="ContentPreview('label541');" onmouseout="ContentUnpreview('label541');" title="click to collapse or expand..."> more... </a>
 <div id="label541" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">subst</span> Subst. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label542' href="javascript:ContentClick('label543', 'label542');" onmouseover="ContentPreview('label543');" onmouseout="ContentUnpreview('label543');" title="click to collapse or expand..."> more... </a>
 <div id="label543" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">substitute_dst_mac</span> <b>(Alias name: substitute-dst-mac)</b>  Substitute dst mac. <span class="li-normal">type: str</span>
 <a id='label544' href="javascript:ContentClick('label545', 'label544');" onmouseover="ContentPreview('label545');" onmouseout="ContentUnpreview('label545');" title="click to collapse or expand..."> more... </a>
 <div id="label545" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch</span> Switch. <span class="li-normal">type: str</span>
 <a id='label546' href="javascript:ContentClick('label547', 'label546');" onmouseover="ContentPreview('label547');" onmouseout="ContentUnpreview('label547');" title="click to collapse or expand..."> more... </a>
 <div id="label547" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_access_vlan</span> <b>(Alias name: switch-controller-access-vlan)</b>  Switch controller access vlan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label548' href="javascript:ContentClick('label549', 'label548');" onmouseover="ContentPreview('label549');" onmouseout="ContentUnpreview('label549');" title="click to collapse or expand..."> more... </a>
 <div id="label549" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_arp_inspection</span> <b>(Alias name: switch-controller-arp-inspection)</b>  Switch controller arp inspection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, monitor]</span> 
 <a id='label550' href="javascript:ContentClick('label551', 'label550');" onmouseover="ContentPreview('label551');" onmouseout="ContentUnpreview('label551');" title="click to collapse or expand..."> more... </a>
 <div id="label551" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_auth</span> <b>(Alias name: switch-controller-auth)</b>  Switch controller auth. <span class="li-normal">type: str</span> <span class="li-normal">choices: [radius, usergroup]</span> 
 <a id='label552' href="javascript:ContentClick('label553', 'label552');" onmouseover="ContentPreview('label553');" onmouseout="ContentUnpreview('label553');" title="click to collapse or expand..."> more... </a>
 <div id="label553" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_dhcp_snooping</span> <b>(Alias name: switch-controller-dhcp-snooping)</b>  Switch controller dhcp snooping. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label554' href="javascript:ContentClick('label555', 'label554');" onmouseover="ContentPreview('label555');" onmouseout="ContentUnpreview('label555');" title="click to collapse or expand..."> more... </a>
 <div id="label555" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_dhcp_snooping_option82</span> <b>(Alias name: switch-controller-dhcp-snooping-option82)</b>  Switch controller dhcp snooping option82. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label556' href="javascript:ContentClick('label557', 'label556');" onmouseover="ContentPreview('label557');" onmouseout="ContentUnpreview('label557');" title="click to collapse or expand..."> more... </a>
 <div id="label557" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_dhcp_snooping_verify_mac</span> <b>(Alias name: switch-controller-dhcp-snooping-verify-mac)</b>  Switch controller dhcp snooping verify mac. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label558' href="javascript:ContentClick('label559', 'label558');" onmouseover="ContentPreview('label559');" onmouseout="ContentUnpreview('label559');" title="click to collapse or expand..."> more... </a>
 <div id="label559" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_igmp_snooping</span> <b>(Alias name: switch-controller-igmp-snooping)</b>  Switch controller igmp snooping. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label560' href="javascript:ContentClick('label561', 'label560');" onmouseover="ContentPreview('label561');" onmouseout="ContentUnpreview('label561');" title="click to collapse or expand..."> more... </a>
 <div id="label561" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_learning_limit</span> <b>(Alias name: switch-controller-learning-limit)</b>  Switch controller learning limit. <span class="li-normal">type: int</span>
 <a id='label562' href="javascript:ContentClick('label563', 'label562');" onmouseover="ContentPreview('label563');" onmouseout="ContentUnpreview('label563');" title="click to collapse or expand..."> more... </a>
 <div id="label563" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_radius_server</span> <b>(Alias name: switch-controller-radius-server)</b>  Switch controller radius server. <span class="li-normal">type: str</span>
 <a id='label564' href="javascript:ContentClick('label565', 'label564');" onmouseover="ContentPreview('label565');" onmouseout="ContentUnpreview('label565');" title="click to collapse or expand..."> more... </a>
 <div id="label565" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_traffic_policy</span> <b>(Alias name: switch-controller-traffic-policy)</b>  Switch controller traffic policy. <span class="li-normal">type: str</span>
 <a id='label566' href="javascript:ContentClick('label567', 'label566');" onmouseover="ContentPreview('label567');" onmouseout="ContentUnpreview('label567');" title="click to collapse or expand..."> more... </a>
 <div id="label567" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tc_mode</span> <b>(Alias name: tc-mode)</b>  Tc mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ptm, atm]</span> 
 <a id='label568' href="javascript:ContentClick('label569', 'label568');" onmouseover="ContentPreview('label569');" onmouseout="ContentUnpreview('label569');" title="click to collapse or expand..."> more... </a>
 <div id="label569" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_mss</span> <b>(Alias name: tcp-mss)</b>  Tcp mss. <span class="li-normal">type: int</span>
 <a id='label570' href="javascript:ContentClick('label571', 'label570');" onmouseover="ContentPreview('label571');" onmouseout="ContentUnpreview('label571');" title="click to collapse or expand..."> more... </a>
 <div id="label571" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trunk</span> Trunk. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label572' href="javascript:ContentClick('label573', 'label572');" onmouseover="ContentPreview('label573');" onmouseout="ContentUnpreview('label573');" title="click to collapse or expand..."> more... </a>
 <div id="label573" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trust_ip_1</span> <b>(Alias name: trust-ip-1)</b>  Trust ip 1. <span class="li-normal">type: str</span>
 <a id='label574' href="javascript:ContentClick('label575', 'label574');" onmouseover="ContentPreview('label575');" onmouseout="ContentUnpreview('label575');" title="click to collapse or expand..."> more... </a>
 <div id="label575" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trust_ip_2</span> <b>(Alias name: trust-ip-2)</b>  Trust ip 2. <span class="li-normal">type: str</span>
 <a id='label576' href="javascript:ContentClick('label577', 'label576');" onmouseover="ContentPreview('label577');" onmouseout="ContentUnpreview('label577');" title="click to collapse or expand..."> more... </a>
 <div id="label577" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trust_ip_3</span> <b>(Alias name: trust-ip-3)</b>  Trust ip 3. <span class="li-normal">type: str</span>
 <a id='label578' href="javascript:ContentClick('label579', 'label578');" onmouseover="ContentPreview('label579');" onmouseout="ContentUnpreview('label579');" title="click to collapse or expand..."> more... </a>
 <div id="label579" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trust_ip6_1</span> <b>(Alias name: trust-ip6-1)</b>  Trust ip6 1. <span class="li-normal">type: str</span>
 <a id='label580' href="javascript:ContentClick('label581', 'label580');" onmouseover="ContentPreview('label581');" onmouseout="ContentUnpreview('label581');" title="click to collapse or expand..."> more... </a>
 <div id="label581" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trust_ip6_2</span> <b>(Alias name: trust-ip6-2)</b>  Trust ip6 2. <span class="li-normal">type: str</span>
 <a id='label582' href="javascript:ContentClick('label583', 'label582');" onmouseover="ContentPreview('label583');" onmouseout="ContentUnpreview('label583');" title="click to collapse or expand..."> more... </a>
 <div id="label583" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trust_ip6_3</span> <b>(Alias name: trust-ip6-3)</b>  Trust ip6 3. <span class="li-normal">type: str</span>
 <a id='label584' href="javascript:ContentClick('label585', 'label584');" onmouseover="ContentPreview('label585');" onmouseout="ContentUnpreview('label585');" title="click to collapse or expand..."> more... </a>
 <div id="label585" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">type</span> Type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [physical, vlan, aggregate, redundant, tunnel, wireless, vdom-link, loopback, switch, hard-switch, hdlc, vap-switch, wl-mesh, fortilink, switch-vlan, fctrl-trunk, tdm, fext-wan, vxlan, emac-vlan, geneve, ssl, lan-extension]</span> 
 <a id='label586' href="javascript:ContentClick('label587', 'label586');" onmouseover="ContentPreview('label587');" onmouseout="ContentUnpreview('label587');" title="click to collapse or expand..."> more... </a>
 <div id="label587" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">username</span> Username. <span class="li-normal">type: str</span>
 <a id='label588' href="javascript:ContentClick('label589', 'label588');" onmouseover="ContentPreview('label589');" onmouseout="ContentUnpreview('label589');" title="click to collapse or expand..."> more... </a>
 <div id="label589" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vci</span> Vci. <span class="li-normal">type: int</span>
 <a id='label590' href="javascript:ContentClick('label591', 'label590');" onmouseover="ContentPreview('label591');" onmouseout="ContentUnpreview('label591');" title="click to collapse or expand..."> more... </a>
 <div id="label591" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vectoring</span> Vectoring. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label592' href="javascript:ContentClick('label593', 'label592');" onmouseover="ContentPreview('label593');" onmouseout="ContentUnpreview('label593');" title="click to collapse or expand..."> more... </a>
 <div id="label593" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vindex</span> Vindex. <span class="li-normal">type: int</span>
 <a id='label594' href="javascript:ContentClick('label595', 'label594');" onmouseover="ContentPreview('label595');" onmouseout="ContentUnpreview('label595');" title="click to collapse or expand..."> more... </a>
 <div id="label595" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlanforward</span> Vlanforward. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label596' href="javascript:ContentClick('label597', 'label596');" onmouseover="ContentPreview('label597');" onmouseout="ContentUnpreview('label597');" title="click to collapse or expand..."> more... </a>
 <div id="label597" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlanid</span> Vlanid. <span class="li-normal">type: int</span>
 <a id='label598' href="javascript:ContentClick('label599', 'label598');" onmouseover="ContentPreview('label599');" onmouseout="ContentUnpreview('label599');" title="click to collapse or expand..."> more... </a>
 <div id="label599" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vpi</span> Vpi. <span class="li-normal">type: int</span>
 <a id='label600' href="javascript:ContentClick('label601', 'label600');" onmouseover="ContentPreview('label601');" onmouseout="ContentUnpreview('label601');" title="click to collapse or expand..."> more... </a>
 <div id="label601" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrf</span> Vrf. <span class="li-normal">type: int</span>
 <a id='label602' href="javascript:ContentClick('label603', 'label602');" onmouseover="ContentPreview('label603');" onmouseout="ContentUnpreview('label603');" title="click to collapse or expand..."> more... </a>
 <div id="label603" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrrp</span> Vrrp. <span class="li-normal">type: list</span>
 <a id='label604' href="javascript:ContentClick('label605', 'label604');" onmouseover="ContentPreview('label605');" onmouseout="ContentUnpreview('label605');" title="click to collapse or expand..."> more... </a>
 <div id="label605" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">accept_mode</span> <b>(Alias name: accept-mode)</b>  Accept mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label606' href="javascript:ContentClick('label607', 'label606');" onmouseover="ContentPreview('label607');" onmouseout="ContentUnpreview('label607');" title="click to collapse or expand..."> more... </a>
 <div id="label607" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">adv_interval</span> <b>(Alias name: adv-interval)</b>  Adv interval. <span class="li-normal">type: int</span>
 <a id='label608' href="javascript:ContentClick('label609', 'label608');" onmouseover="ContentPreview('label609');" onmouseout="ContentUnpreview('label609');" title="click to collapse or expand..."> more... </a>
 <div id="label609" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ignore_default_route</span> <b>(Alias name: ignore-default-route)</b>  Ignore default route. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label610' href="javascript:ContentClick('label611', 'label610');" onmouseover="ContentPreview('label611');" onmouseout="ContentUnpreview('label611');" title="click to collapse or expand..."> more... </a>
 <div id="label611" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">preempt</span> Preempt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label612' href="javascript:ContentClick('label613', 'label612');" onmouseover="ContentPreview('label613');" onmouseout="ContentUnpreview('label613');" title="click to collapse or expand..."> more... </a>
 <div id="label613" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Priority. <span class="li-normal">type: int</span>
 <a id='label614' href="javascript:ContentClick('label615', 'label614');" onmouseover="ContentPreview('label615');" onmouseout="ContentUnpreview('label615');" title="click to collapse or expand..."> more... </a>
 <div id="label615" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">start_time</span> <b>(Alias name: start-time)</b>  Start time. <span class="li-normal">type: int</span>
 <a id='label616' href="javascript:ContentClick('label617', 'label616');" onmouseover="ContentPreview('label617');" onmouseout="ContentUnpreview('label617');" title="click to collapse or expand..."> more... </a>
 <div id="label617" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label618' href="javascript:ContentClick('label619', 'label618');" onmouseover="ContentPreview('label619');" onmouseout="ContentUnpreview('label619');" title="click to collapse or expand..."> more... </a>
 <div id="label619" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">version</span> Version. <span class="li-normal">type: str</span> <span class="li-normal">choices: [2, 3]</span> 
 <a id='label620' href="javascript:ContentClick('label621', 'label620');" onmouseover="ContentPreview('label621');" onmouseout="ContentUnpreview('label621');" title="click to collapse or expand..."> more... </a>
 <div id="label621" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrdst</span> Vrdst. <span class="li-normal">type: list</span>
 <a id='label622' href="javascript:ContentClick('label623', 'label622');" onmouseover="ContentPreview('label623');" onmouseout="ContentUnpreview('label623');" title="click to collapse or expand..."> more... </a>
 <div id="label623" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrdst_priority</span> <b>(Alias name: vrdst-priority)</b>  Vrdst priority. <span class="li-normal">type: int</span>
 <a id='label624' href="javascript:ContentClick('label625', 'label624');" onmouseover="ContentPreview('label625');" onmouseout="ContentUnpreview('label625');" title="click to collapse or expand..."> more... </a>
 <div id="label625" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrgrp</span> Vrgrp. <span class="li-normal">type: int</span>
 <a id='label626' href="javascript:ContentClick('label627', 'label626');" onmouseover="ContentPreview('label627');" onmouseout="ContentUnpreview('label627');" title="click to collapse or expand..."> more... </a>
 <div id="label627" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrid</span> Vrid. <span class="li-normal">type: int</span>
 <a id='label628' href="javascript:ContentClick('label629', 'label628');" onmouseover="ContentPreview('label629');" onmouseout="ContentUnpreview('label629');" title="click to collapse or expand..."> more... </a>
 <div id="label629" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrip</span> Vrip. <span class="li-normal">type: str</span>
 <a id='label630' href="javascript:ContentClick('label631', 'label630');" onmouseover="ContentPreview('label631');" onmouseout="ContentUnpreview('label631');" title="click to collapse or expand..."> more... </a>
 <div id="label631" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_arp</span> <b>(Alias name: proxy-arp)</b>  Proxy arp. <span class="li-normal">type: list</span>
 <a id='label632' href="javascript:ContentClick('label633', 'label632');" onmouseover="ContentPreview('label633');" onmouseout="ContentUnpreview('label633');" title="click to collapse or expand..."> more... </a>
 <div id="label633" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label634' href="javascript:ContentClick('label635', 'label634');" onmouseover="ContentPreview('label635');" onmouseout="ContentUnpreview('label635');" title="click to collapse or expand..."> more... </a>
 <div id="label635" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Set ip addresses of proxy arp. <span class="li-normal">type: str</span>
 <a id='label636' href="javascript:ContentClick('label637', 'label636');" onmouseover="ContentPreview('label637');" onmouseout="ContentUnpreview('label637');" title="click to collapse or expand..."> more... </a>
 <div id="label637" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 </ul>
 </li>
 <li><span class="li-head">vrrp_virtual_mac</span> <b>(Alias name: vrrp-virtual-mac)</b>  Vrrp virtual mac. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label638' href="javascript:ContentClick('label639', 'label638');" onmouseover="ContentPreview('label639');" onmouseout="ContentUnpreview('label639');" title="click to collapse or expand..."> more... </a>
 <div id="label639" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wccp</span> Wccp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label640' href="javascript:ContentClick('label641', 'label640');" onmouseover="ContentPreview('label641');" onmouseout="ContentUnpreview('label641');" title="click to collapse or expand..."> more... </a>
 <div id="label641" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">weight</span> Weight. <span class="li-normal">type: int</span>
 <a id='label642' href="javascript:ContentClick('label643', 'label642');" onmouseover="ContentPreview('label643');" onmouseout="ContentUnpreview('label643');" title="click to collapse or expand..."> more... </a>
 <div id="label643" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_5g_threshold</span> <b>(Alias name: wifi-5g-threshold)</b>  Wifi 5g threshold. <span class="li-normal">type: str</span>
 <a id='label644' href="javascript:ContentClick('label645', 'label644');" onmouseover="ContentPreview('label645');" onmouseout="ContentUnpreview('label645');" title="click to collapse or expand..."> more... </a>
 <div id="label645" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_acl</span> <b>(Alias name: wifi-acl)</b>  Wifi acl. <span class="li-normal">type: str</span> <span class="li-normal">choices: [deny, allow]</span> 
 <a id='label646' href="javascript:ContentClick('label647', 'label646');" onmouseover="ContentPreview('label647');" onmouseout="ContentUnpreview('label647');" title="click to collapse or expand..."> more... </a>
 <div id="label647" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_ap_band</span> <b>(Alias name: wifi-ap-band)</b>  Wifi ap band. <span class="li-normal">type: str</span> <span class="li-normal">choices: [any, 5g-preferred, 5g-only]</span> 
 <a id='label648' href="javascript:ContentClick('label649', 'label648');" onmouseover="ContentPreview('label649');" onmouseout="ContentUnpreview('label649');" title="click to collapse or expand..."> more... </a>
 <div id="label649" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_auth</span> <b>(Alias name: wifi-auth)</b>  Wifi auth. <span class="li-normal">type: str</span> <span class="li-normal">choices: [PSK, RADIUS, radius, usergroup]</span> 
 <a id='label650' href="javascript:ContentClick('label651', 'label650');" onmouseover="ContentPreview('label651');" onmouseout="ContentUnpreview('label651');" title="click to collapse or expand..."> more... </a>
 <div id="label651" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_auto_connect</span> <b>(Alias name: wifi-auto-connect)</b>  Wifi auto connect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label652' href="javascript:ContentClick('label653', 'label652');" onmouseover="ContentPreview('label653');" onmouseout="ContentUnpreview('label653');" title="click to collapse or expand..."> more... </a>
 <div id="label653" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_auto_save</span> <b>(Alias name: wifi-auto-save)</b>  Wifi auto save. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label654' href="javascript:ContentClick('label655', 'label654');" onmouseover="ContentPreview('label655');" onmouseout="ContentUnpreview('label655');" title="click to collapse or expand..."> more... </a>
 <div id="label655" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_broadcast_ssid</span> <b>(Alias name: wifi-broadcast-ssid)</b>  Wifi broadcast ssid. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label656' href="javascript:ContentClick('label657', 'label656');" onmouseover="ContentPreview('label657');" onmouseout="ContentUnpreview('label657');" title="click to collapse or expand..."> more... </a>
 <div id="label657" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_encrypt</span> <b>(Alias name: wifi-encrypt)</b>  Wifi encrypt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [TKIP, AES]</span> 
 <a id='label658' href="javascript:ContentClick('label659', 'label658');" onmouseover="ContentPreview('label659');" onmouseout="ContentUnpreview('label659');" title="click to collapse or expand..."> more... </a>
 <div id="label659" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_fragment_threshold</span> <b>(Alias name: wifi-fragment-threshold)</b>  Wifi fragment threshold. <span class="li-normal">type: int</span>
 <a id='label660' href="javascript:ContentClick('label661', 'label660');" onmouseover="ContentPreview('label661');" onmouseout="ContentUnpreview('label661');" title="click to collapse or expand..."> more... </a>
 <div id="label661" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_key</span> <b>(Alias name: wifi-key)</b>  Wifi key. <span class="li-normal">type: list</span>
 <a id='label662' href="javascript:ContentClick('label663', 'label662');" onmouseover="ContentPreview('label663');" onmouseout="ContentUnpreview('label663');" title="click to collapse or expand..."> more... </a>
 <div id="label663" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_keyindex</span> <b>(Alias name: wifi-keyindex)</b>  Wifi keyindex. <span class="li-normal">type: int</span>
 <a id='label664' href="javascript:ContentClick('label665', 'label664');" onmouseover="ContentPreview('label665');" onmouseout="ContentUnpreview('label665');" title="click to collapse or expand..."> more... </a>
 <div id="label665" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_mac_filter</span> <b>(Alias name: wifi-mac-filter)</b>  Wifi mac filter. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label666' href="javascript:ContentClick('label667', 'label666');" onmouseover="ContentPreview('label667');" onmouseout="ContentUnpreview('label667');" title="click to collapse or expand..."> more... </a>
 <div id="label667" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_passphrase</span> <b>(Alias name: wifi-passphrase)</b>  Wifi passphrase. <span class="li-normal">type: list</span>
 <a id='label668' href="javascript:ContentClick('label669', 'label668');" onmouseover="ContentPreview('label669');" onmouseout="ContentUnpreview('label669');" title="click to collapse or expand..."> more... </a>
 <div id="label669" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_radius_server</span> <b>(Alias name: wifi-radius-server)</b>  Wifi radius server. <span class="li-normal">type: str</span>
 <a id='label670' href="javascript:ContentClick('label671', 'label670');" onmouseover="ContentPreview('label671');" onmouseout="ContentUnpreview('label671');" title="click to collapse or expand..."> more... </a>
 <div id="label671" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_rts_threshold</span> <b>(Alias name: wifi-rts-threshold)</b>  Wifi rts threshold. <span class="li-normal">type: int</span>
 <a id='label672' href="javascript:ContentClick('label673', 'label672');" onmouseover="ContentPreview('label673');" onmouseout="ContentUnpreview('label673');" title="click to collapse or expand..."> more... </a>
 <div id="label673" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_security</span> <b>(Alias name: wifi-security)</b>  Wifi security. <span class="li-normal">type: str</span> <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise]</span> 
 <a id='label674' href="javascript:ContentClick('label675', 'label674');" onmouseover="ContentPreview('label675');" onmouseout="ContentUnpreview('label675');" title="click to collapse or expand..."> more... </a>
 <div id="label675" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_ssid</span> <b>(Alias name: wifi-ssid)</b>  Wifi ssid. <span class="li-normal">type: str</span>
 <a id='label676' href="javascript:ContentClick('label677', 'label676');" onmouseover="ContentPreview('label677');" onmouseout="ContentUnpreview('label677');" title="click to collapse or expand..."> more... </a>
 <div id="label677" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_usergroup</span> <b>(Alias name: wifi-usergroup)</b>  Wifi usergroup. <span class="li-normal">type: str</span>
 <a id='label678' href="javascript:ContentClick('label679', 'label678');" onmouseover="ContentPreview('label679');" onmouseout="ContentUnpreview('label679');" title="click to collapse or expand..."> more... </a>
 <div id="label679" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wins_ip</span> <b>(Alias name: wins-ip)</b>  Wins ip. <span class="li-normal">type: str</span>
 <a id='label680' href="javascript:ContentClick('label681', 'label680');" onmouseover="ContentPreview('label681');" onmouseout="ContentUnpreview('label681');" title="click to collapse or expand..."> more... </a>
 <div id="label681" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eip</span> Eip. <span class="li-normal">type: str</span>
 <a id='label682' href="javascript:ContentClick('label683', 'label682');" onmouseover="ContentPreview('label683');" onmouseout="ContentUnpreview('label683');" title="click to collapse or expand..."> more... </a>
 <div id="label683" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortilink_neighbor_detect</span> <b>(Alias name: fortilink-neighbor-detect)</b>  Fortilink neighbor detect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [lldp, fortilink]</span> 
 <a id='label684' href="javascript:ContentClick('label685', 'label684');" onmouseover="ContentPreview('label685');" onmouseout="ContentUnpreview('label685');" title="click to collapse or expand..."> more... </a>
 <div id="label685" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ingress_shaping_profile</span> <b>(Alias name: ingress-shaping-profile)</b>  Ingress shaping profile. <span class="li-normal">type: str</span>
 <a id='label686' href="javascript:ContentClick('label687', 'label686');" onmouseover="ContentPreview('label687');" onmouseout="ContentUnpreview('label687');" title="click to collapse or expand..."> more... </a>
 <div id="label687" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ring_rx</span> <b>(Alias name: ring-rx)</b>  Ring rx. <span class="li-normal">type: int</span>
 <a id='label688' href="javascript:ContentClick('label689', 'label688');" onmouseover="ContentPreview('label689');" onmouseout="ContentUnpreview('label689');" title="click to collapse or expand..."> more... </a>
 <div id="label689" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ring_tx</span> <b>(Alias name: ring-tx)</b>  Ring tx. <span class="li-normal">type: int</span>
 <a id='label690' href="javascript:ContentClick('label691', 'label690');" onmouseover="ContentPreview('label691');" onmouseout="ContentUnpreview('label691');" title="click to collapse or expand..."> more... </a>
 <div id="label691" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_igmp_snooping_fast_leave</span> <b>(Alias name: switch-controller-igmp-snooping-fast-leave)</b>  Switch controller igmp snooping fast leave. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label692' href="javascript:ContentClick('label693', 'label692');" onmouseover="ContentPreview('label693');" onmouseout="ContentUnpreview('label693');" title="click to collapse or expand..."> more... </a>
 <div id="label693" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_igmp_snooping_proxy</span> <b>(Alias name: switch-controller-igmp-snooping-proxy)</b>  Switch controller igmp snooping proxy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label694' href="javascript:ContentClick('label695', 'label694');" onmouseover="ContentPreview('label695');" onmouseout="ContentUnpreview('label695');" title="click to collapse or expand..."> more... </a>
 <div id="label695" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_rspan_mode</span> <b>(Alias name: switch-controller-rspan-mode)</b>  Switch controller rspan mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label696' href="javascript:ContentClick('label697', 'label696');" onmouseover="ContentPreview('label697');" onmouseout="ContentUnpreview('label697');" title="click to collapse or expand..."> more... </a>
 <div id="label697" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bandwidth_measure_time</span> <b>(Alias name: bandwidth-measure-time)</b>  Bandwidth measure time. <span class="li-normal">type: int</span>
 <a id='label698' href="javascript:ContentClick('label699', 'label698');" onmouseover="ContentPreview('label699');" onmouseout="ContentUnpreview('label699');" title="click to collapse or expand..."> more... </a>
 <div id="label699" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip_managed_by_fortiipam</span> <b>(Alias name: ip-managed-by-fortiipam)</b>  Ip managed by fortiipam. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, inherit-global]</span> 
 <a id='label700' href="javascript:ContentClick('label701', 'label700');" onmouseover="ContentPreview('label701');" onmouseout="ContentUnpreview('label701');" title="click to collapse or expand..."> more... </a>
 <div id="label701" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">managed_subnetwork_size</span> <b>(Alias name: managed-subnetwork-size)</b>  Managed subnetwork size. <span class="li-normal">type: str</span> <span class="li-normal">choices: [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 32, 64, 128, 4, 8, 16, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216]</span> 
 <a id='label702' href="javascript:ContentClick('label703', 'label702');" onmouseover="ContentPreview('label703');" onmouseout="ContentUnpreview('label703');" title="click to collapse or expand..."> more... </a>
 <div id="label703" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">measured_downstream_bandwidth</span> <b>(Alias name: measured-downstream-bandwidth)</b>  Measured downstream bandwidth. <span class="li-normal">type: int</span>
 <a id='label704' href="javascript:ContentClick('label705', 'label704');" onmouseover="ContentPreview('label705');" onmouseout="ContentUnpreview('label705');" title="click to collapse or expand..."> more... </a>
 <div id="label705" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">measured_upstream_bandwidth</span> <b>(Alias name: measured-upstream-bandwidth)</b>  Measured upstream bandwidth. <span class="li-normal">type: int</span>
 <a id='label706' href="javascript:ContentClick('label707', 'label706');" onmouseover="ContentPreview('label707');" onmouseout="ContentUnpreview('label707');" title="click to collapse or expand..."> more... </a>
 <div id="label707" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">monitor_bandwidth</span> <b>(Alias name: monitor-bandwidth)</b>  Monitor bandwidth. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label708' href="javascript:ContentClick('label709', 'label708');" onmouseover="ContentPreview('label709');" onmouseout="ContentUnpreview('label709');" title="click to collapse or expand..."> more... </a>
 <div id="label709" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">swc_vlan</span> <b>(Alias name: swc-vlan)</b>  Swc vlan. <span class="li-normal">type: int</span>
 <a id='label710' href="javascript:ContentClick('label711', 'label710');" onmouseover="ContentPreview('label711');" onmouseout="ContentUnpreview('label711');" title="click to collapse or expand..."> more... </a>
 <div id="label711" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_feature</span> <b>(Alias name: switch-controller-feature)</b>  Switch controller feature. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, default-vlan, quarantine, sniffer, voice, camera, rspan, video, nac, nac-segment]</span> 
 <a id='label712' href="javascript:ContentClick('label713', 'label712');" onmouseover="ContentPreview('label713');" onmouseout="ContentUnpreview('label713');" title="click to collapse or expand..."> more... </a>
 <div id="label713" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_mgmt_vlan</span> <b>(Alias name: switch-controller-mgmt-vlan)</b>  Switch controller mgmt vlan. <span class="li-normal">type: int</span>
 <a id='label714' href="javascript:ContentClick('label715', 'label714');" onmouseover="ContentPreview('label715');" onmouseout="ContentUnpreview('label715');" title="click to collapse or expand..."> more... </a>
 <div id="label715" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_nac</span> <b>(Alias name: switch-controller-nac)</b>  Switch controller nac. <span class="li-normal">type: str</span>
 <a id='label716' href="javascript:ContentClick('label717', 'label716');" onmouseover="ContentPreview('label717');" onmouseout="ContentUnpreview('label717');" title="click to collapse or expand..."> more... </a>
 <div id="label717" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_protocol</span> <b>(Alias name: vlan-protocol)</b>  Vlan protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [8021q, 8021ad]</span> 
 <a id='label718' href="javascript:ContentClick('label719', 'label718');" onmouseover="ContentPreview('label719');" onmouseout="ContentUnpreview('label719');" title="click to collapse or expand..."> more... </a>
 <div id="label719" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_interface</span> <b>(Alias name: dhcp-relay-interface)</b>  Dhcp relay interface. <span class="li-normal">type: str</span>
 <a id='label720' href="javascript:ContentClick('label721', 'label720');" onmouseover="ContentPreview('label721');" onmouseout="ContentUnpreview('label721');" title="click to collapse or expand..."> more... </a>
 <div id="label721" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.6 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_interface_select_method</span> <b>(Alias name: dhcp-relay-interface-select-method)</b>  Dhcp relay interface select method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, sdwan, specify]</span> 
 <a id='label722' href="javascript:ContentClick('label723', 'label722');" onmouseover="ContentPreview('label723');" onmouseout="ContentUnpreview('label723');" title="click to collapse or expand..."> more... </a>
 <div id="label723" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.6 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">np_qos_profile</span> <b>(Alias name: np-qos-profile)</b>  Np qos profile id. <span class="li-normal">type: int</span>
 <a id='label724' href="javascript:ContentClick('label725', 'label724');" onmouseover="ContentPreview('label725');" onmouseout="ContentUnpreview('label725');" title="click to collapse or expand..."> more... </a>
 <div id="label725" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.7 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">swc_first_create</span> <b>(Alias name: swc-first-create)</b>  Initial create for switch-controller vlans. <span class="li-normal">type: int</span>
 <a id='label726' href="javascript:ContentClick('label727', 'label726');" onmouseover="ContentPreview('label727');" onmouseout="ContentUnpreview('label727');" title="click to collapse or expand..."> more... </a>
 <div id="label727" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_iot_scanning</span> <b>(Alias name: switch-controller-iot-scanning)</b>  Enable/disable managed fortiswitch iot scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label728' href="javascript:ContentClick('label729', 'label728');" onmouseover="ContentPreview('label729');" onmouseout="ContentUnpreview('label729');" title="click to collapse or expand..."> more... </a>
 <div id="label729" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_source_ip</span> <b>(Alias name: switch-controller-source-ip)</b>  Source ip address used in fortilink over l3 connections. <span class="li-normal">type: str</span> <span class="li-normal">choices: [outbound, fixed]</span> 
 <a id='label730' href="javascript:ContentClick('label731', 'label730');" onmouseover="ContentPreview('label731');" onmouseout="ContentUnpreview('label731');" title="click to collapse or expand..."> more... </a>
 <div id="label731" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_request_all_server</span> <b>(Alias name: dhcp-relay-request-all-server)</b>  Enable/disable sending of dhcp requests to all servers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label732' href="javascript:ContentClick('label733', 'label732');" onmouseover="ContentPreview('label733');" onmouseout="ContentUnpreview('label733');" title="click to collapse or expand..."> more... </a>
 <div id="label733" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.6 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">stp_ha_secondary</span> <b>(Alias name: stp-ha-secondary)</b>  Control stp behaviour on ha secondary. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, priority-adjust]</span> 
 <a id='label734' href="javascript:ContentClick('label735', 'label734');" onmouseover="ContentPreview('label735');" onmouseout="ContentUnpreview('label735');" title="click to collapse or expand..."> more... </a>
 <div id="label735" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_dynamic</span> <b>(Alias name: switch-controller-dynamic)</b>  Integrated fortilink settings for managed fortiswitch. <span class="li-normal">type: str</span>
 <a id='label736' href="javascript:ContentClick('label737', 'label736');" onmouseover="ContentPreview('label737');" onmouseout="ContentUnpreview('label737');" title="click to collapse or expand..."> more... </a>
 <div id="label737" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_cert</span> <b>(Alias name: auth-cert)</b>  Https server certificate. <span class="li-normal">type: str</span>
 <a id='label738' href="javascript:ContentClick('label739', 'label738');" onmouseover="ContentPreview('label739');" onmouseout="ContentUnpreview('label739');" title="click to collapse or expand..."> more... </a>
 <div id="label739" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_portal_addr</span> <b>(Alias name: auth-portal-addr)</b>  Address of captive portal. <span class="li-normal">type: str</span>
 <a id='label740' href="javascript:ContentClick('label741', 'label740');" onmouseover="ContentPreview('label741');" onmouseout="ContentUnpreview('label741');" title="click to collapse or expand..."> more... </a>
 <div id="label741" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_classless_route_addition</span> <b>(Alias name: dhcp-classless-route-addition)</b>  Enable/disable addition of classless static routes retrieved from dhcp server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label742' href="javascript:ContentClick('label743', 'label742');" onmouseover="ContentPreview('label743');" onmouseout="ContentUnpreview('label743');" title="click to collapse or expand..."> more... </a>
 <div id="label743" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_link_selection</span> <b>(Alias name: dhcp-relay-link-selection)</b>  Dhcp relay link selection. <span class="li-normal">type: str</span>
 <a id='label744' href="javascript:ContentClick('label745', 'label744');" onmouseover="ContentPreview('label745');" onmouseout="ContentUnpreview('label745');" title="click to collapse or expand..."> more... </a>
 <div id="label745" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dns_server_protocol</span> <b>(Alias name: dns-server-protocol)</b>  Dns transport protocols. <span class="li-normal">type: list</span> <span class="li-normal">choices: [cleartext, dot, doh]</span> 
 <a id='label746' href="javascript:ContentClick('label747', 'label746');" onmouseover="ContentPreview('label747');" onmouseout="ContentUnpreview('label747');" title="click to collapse or expand..."> more... </a>
 <div id="label747" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_ca_cert</span> <b>(Alias name: eap-ca-cert)</b>  Eap ca certificate name. <span class="li-normal">type: str</span>
 <a id='label748' href="javascript:ContentClick('label749', 'label748');" onmouseover="ContentPreview('label749');" onmouseout="ContentUnpreview('label749');" title="click to collapse or expand..."> more... </a>
 <div id="label749" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_identity</span> <b>(Alias name: eap-identity)</b>  Eap identity. <span class="li-normal">type: str</span>
 <a id='label750' href="javascript:ContentClick('label751', 'label750');" onmouseover="ContentPreview('label751');" onmouseout="ContentUnpreview('label751');" title="click to collapse or expand..."> more... </a>
 <div id="label751" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_method</span> <b>(Alias name: eap-method)</b>  Eap method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tls, peap]</span> 
 <a id='label752' href="javascript:ContentClick('label753', 'label752');" onmouseover="ContentPreview('label753');" onmouseout="ContentUnpreview('label753');" title="click to collapse or expand..."> more... </a>
 <div id="label753" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_password</span> <b>(Alias name: eap-password)</b>  Eap password. <span class="li-normal">type: list</span>
 <a id='label754' href="javascript:ContentClick('label755', 'label754');" onmouseover="ContentPreview('label755');" onmouseout="ContentUnpreview('label755');" title="click to collapse or expand..."> more... </a>
 <div id="label755" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_supplicant</span> <b>(Alias name: eap-supplicant)</b>  Enable/disable eap-supplicant. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label756' href="javascript:ContentClick('label757', 'label756');" onmouseover="ContentPreview('label757');" onmouseout="ContentUnpreview('label757');" title="click to collapse or expand..."> more... </a>
 <div id="label757" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_user_cert</span> <b>(Alias name: eap-user-cert)</b>  Eap user certificate name. <span class="li-normal">type: str</span>
 <a id='label758' href="javascript:ContentClick('label759', 'label758');" onmouseover="ContentPreview('label759');" onmouseout="ContentUnpreview('label759');" title="click to collapse or expand..."> more... </a>
 <div id="label759" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ike_saml_server</span> <b>(Alias name: ike-saml-server)</b>  Configure ike authentication saml server. <span class="li-normal">type: str</span>
 <a id='label760' href="javascript:ContentClick('label761', 'label760');" onmouseover="ContentPreview('label761');" onmouseout="ContentUnpreview('label761');" title="click to collapse or expand..."> more... </a>
 <div id="label761" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">lacp_ha_secondary</span> <b>(Alias name: lacp-ha-secondary)</b>  Lacp ha secondary. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label762' href="javascript:ContentClick('label763', 'label762');" onmouseover="ContentPreview('label763');" onmouseout="ContentUnpreview('label763');" title="click to collapse or expand..."> more... </a>
 <div id="label763" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_atm_qos</span> <b>(Alias name: pvc-atm-qos)</b>  Sfp-dsl adsl fallback pvc atm qos. <span class="li-normal">type: str</span> <span class="li-normal">choices: [cbr, rt-vbr, nrt-vbr, ubr]</span> 
 <a id='label764' href="javascript:ContentClick('label765', 'label764');" onmouseover="ContentPreview('label765');" onmouseout="ContentUnpreview('label765');" title="click to collapse or expand..."> more... </a>
 <div id="label765" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_chan</span> <b>(Alias name: pvc-chan)</b>  Sfp-dsl adsl fallback pvc channel. <span class="li-normal">type: int</span>
 <a id='label766' href="javascript:ContentClick('label767', 'label766');" onmouseover="ContentPreview('label767');" onmouseout="ContentUnpreview('label767');" title="click to collapse or expand..."> more... </a>
 <div id="label767" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_crc</span> <b>(Alias name: pvc-crc)</b>  Sfp-dsl adsl fallback pvc crc option:  bit0: sar llc preserve, bit1: ream llc preserve, bit2: ream vc-mux has crc. <span class="li-normal">type: int</span>
 <a id='label768' href="javascript:ContentClick('label769', 'label768');" onmouseover="ContentPreview('label769');" onmouseout="ContentUnpreview('label769');" title="click to collapse or expand..."> more... </a>
 <div id="label769" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_pcr</span> <b>(Alias name: pvc-pcr)</b>  Sfp-dsl adsl fallback pvc packet cell rate in cells (0 - 5500). <span class="li-normal">type: int</span>
 <a id='label770' href="javascript:ContentClick('label771', 'label770');" onmouseover="ContentPreview('label771');" onmouseout="ContentUnpreview('label771');" title="click to collapse or expand..."> more... </a>
 <div id="label771" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_scr</span> <b>(Alias name: pvc-scr)</b>  Sfp-dsl adsl fallback pvc sustainable cell rate in cells (0 - 5500). <span class="li-normal">type: int</span>
 <a id='label772' href="javascript:ContentClick('label773', 'label772');" onmouseover="ContentPreview('label773');" onmouseout="ContentUnpreview('label773');" title="click to collapse or expand..."> more... </a>
 <div id="label773" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_vlan_id</span> <b>(Alias name: pvc-vlan-id)</b>  Sfp-dsl adsl fallback pvc vlan id. <span class="li-normal">type: int</span>
 <a id='label774' href="javascript:ContentClick('label775', 'label774');" onmouseover="ContentPreview('label775');" onmouseout="ContentUnpreview('label775');" title="click to collapse or expand..."> more... </a>
 <div id="label775" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_vlan_rx_id</span> <b>(Alias name: pvc-vlan-rx-id)</b>  Sfp-dsl adsl fallback pvc vlanid rx. <span class="li-normal">type: int</span>
 <a id='label776' href="javascript:ContentClick('label777', 'label776');" onmouseover="ContentPreview('label777');" onmouseout="ContentUnpreview('label777');" title="click to collapse or expand..."> more... </a>
 <div id="label777" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_vlan_rx_op</span> <b>(Alias name: pvc-vlan-rx-op)</b>  Sfp-dsl adsl fallback pvc vlan rx op. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass-through, replace, remove]</span> 
 <a id='label778' href="javascript:ContentClick('label779', 'label778');" onmouseover="ContentPreview('label779');" onmouseout="ContentUnpreview('label779');" title="click to collapse or expand..."> more... </a>
 <div id="label779" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_vlan_tx_id</span> <b>(Alias name: pvc-vlan-tx-id)</b>  Sfp-dsl adsl fallback pvc vlan id tx. <span class="li-normal">type: int</span>
 <a id='label780' href="javascript:ContentClick('label781', 'label780');" onmouseover="ContentPreview('label781');" onmouseout="ContentUnpreview('label781');" title="click to collapse or expand..."> more... </a>
 <div id="label781" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pvc_vlan_tx_op</span> <b>(Alias name: pvc-vlan-tx-op)</b>  Sfp-dsl adsl fallback pvc vlan tx op. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass-through, replace, remove]</span> 
 <a id='label782' href="javascript:ContentClick('label783', 'label782');" onmouseover="ContentPreview('label783');" onmouseout="ContentUnpreview('label783');" title="click to collapse or expand..."> more... </a>
 <div id="label783" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">reachable_time</span> <b>(Alias name: reachable-time)</b>  Ipv4 reachable time in milliseconds (30000 - 3600000, default = 30000). <span class="li-normal">type: int</span>
 <a id='label784' href="javascript:ContentClick('label785', 'label784');" onmouseover="ContentPreview('label785');" onmouseout="ContentUnpreview('label785');" title="click to collapse or expand..."> more... </a>
 <div id="label785" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">select_profile_30a_35b</span> <b>(Alias name: select-profile-30a-35b)</b>  Select vdsl profile 30a or 35b. <span class="li-normal">type: str</span> <span class="li-normal">choices: [30A, 35B, 30a, 35b]</span> 
 <a id='label786' href="javascript:ContentClick('label787', 'label786');" onmouseover="ContentPreview('label787');" onmouseout="ContentUnpreview('label787');" title="click to collapse or expand..."> more... </a>
 <div id="label787" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.9 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sfp_dsl</span> <b>(Alias name: sfp-dsl)</b>  Enable/disable sfp dsl. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label788' href="javascript:ContentClick('label789', 'label788');" onmouseover="ContentPreview('label789');" onmouseout="ContentUnpreview('label789');" title="click to collapse or expand..."> more... </a>
 <div id="label789" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sfp_dsl_adsl_fallback</span> <b>(Alias name: sfp-dsl-adsl-fallback)</b>  Enable/disable sfp dsl adsl fallback. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label790' href="javascript:ContentClick('label791', 'label790');" onmouseover="ContentPreview('label791');" onmouseout="ContentUnpreview('label791');" title="click to collapse or expand..."> more... </a>
 <div id="label791" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sfp_dsl_autodetect</span> <b>(Alias name: sfp-dsl-autodetect)</b>  Enable/disable sfp dsl mac address autodetect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label792' href="javascript:ContentClick('label793', 'label792');" onmouseover="ContentPreview('label793');" onmouseout="ContentUnpreview('label793');" title="click to collapse or expand..."> more... </a>
 <div id="label793" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sfp_dsl_mac</span> <b>(Alias name: sfp-dsl-mac)</b>  Sfp dsl mac address. <span class="li-normal">type: str</span>
 <a id='label794' href="javascript:ContentClick('label795', 'label794');" onmouseover="ContentPreview('label795');" onmouseout="ContentUnpreview('label795');" title="click to collapse or expand..."> more... </a>
 <div id="label795" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sw_algorithm</span> <b>(Alias name: sw-algorithm)</b>  Frame distribution algorithm for switch. <span class="li-normal">type: str</span> <span class="li-normal">choices: [l2, l3, eh, default]</span> 
 <a id='label796' href="javascript:ContentClick('label797', 'label796');" onmouseover="ContentPreview('label797');" onmouseout="ContentUnpreview('label797');" title="click to collapse or expand..."> more... </a>
 <div id="label797" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_id</span> <b>(Alias name: system-id)</b>  Define a system id for the aggregate interface. <span class="li-normal">type: str</span>
 <a id='label798' href="javascript:ContentClick('label799', 'label798');" onmouseover="ContentPreview('label799');" onmouseout="ContentUnpreview('label799');" title="click to collapse or expand..."> more... </a>
 <div id="label799" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.7 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">system_id_type</span> <b>(Alias name: system-id-type)</b>  Method in which system id is generated. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, user]</span> 
 <a id='label800' href="javascript:ContentClick('label801', 'label800');" onmouseover="ContentPreview('label801');" onmouseout="ContentUnpreview('label801');" title="click to collapse or expand..."> more... </a>
 <div id="label801" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.7 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_id</span> <b>(Alias name: vlan-id)</b>  Vlan id <span class="li-normal">type: int</span>
 <a id='label802' href="javascript:ContentClick('label803', 'label802');" onmouseover="ContentPreview('label803');" onmouseout="ContentUnpreview('label803');" title="click to collapse or expand..."> more... </a>
 <div id="label803" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.9 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_op_mode</span> <b>(Alias name: vlan-op-mode)</b>  Configure dsl 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tag, untag, passthrough]</span> 
 <a id='label804' href="javascript:ContentClick('label805', 'label804');" onmouseover="ContentPreview('label805');" onmouseout="ContentUnpreview('label805');" title="click to collapse or expand..."> more... </a>
 <div id="label805" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.9 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">generic_receive_offload</span> <b>(Alias name: generic-receive-offload)</b>  Generic receive offload. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label806' href="javascript:ContentClick('label807', 'label806');" onmouseover="ContentPreview('label807');" onmouseout="ContentUnpreview('label807');" title="click to collapse or expand..."> more... </a>
 <div id="label807" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">interconnect_profile</span> <b>(Alias name: interconnect-profile)</b>  Set interconnect profile. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, profile1, profile2]</span> 
 <a id='label808' href="javascript:ContentClick('label809', 'label808');" onmouseover="ContentPreview('label809');" onmouseout="ContentUnpreview('label809');" title="click to collapse or expand..."> more... </a>
 <div id="label809" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">large_receive_offload</span> <b>(Alias name: large-receive-offload)</b>  Large receive offload. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label810' href="javascript:ContentClick('label811', 'label810');" onmouseover="ContentPreview('label811');" onmouseout="ContentUnpreview('label811');" title="click to collapse or expand..."> more... </a>
 <div id="label811" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">annex</span> Set xdsl annex type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [a, b, j, bjm, i, al, m, aijlm, bj]</span> 
 <a id='label812' href="javascript:ContentClick('label813', 'label812');" onmouseover="ContentPreview('label813');" onmouseout="ContentUnpreview('label813');" title="click to collapse or expand..."> more... </a>
 <div id="label813" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.10 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">aggregate_type</span> <b>(Alias name: aggregate-type)</b>  Type of aggregation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [physical, vxlan]</span> 
 <a id='label814' href="javascript:ContentClick('label815', 'label814');" onmouseover="ContentPreview('label815');" onmouseout="ContentUnpreview('label815');" title="click to collapse or expand..."> more... </a>
 <div id="label815" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_netflow_collect</span> <b>(Alias name: switch-controller-netflow-collect)</b>  Netflow collection and processing. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label816' href="javascript:ContentClick('label817', 'label816');" onmouseover="ContentPreview('label817');" onmouseout="ContentUnpreview('label817');" title="click to collapse or expand..."> more... </a>
 <div id="label817" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_dns_server1</span> <b>(Alias name: wifi-dns-server1)</b>  Dns server 1. <span class="li-normal">type: str</span>
 <a id='label818' href="javascript:ContentClick('label819', 'label818');" onmouseover="ContentPreview('label819');" onmouseout="ContentUnpreview('label819');" title="click to collapse or expand..."> more... </a>
 <div id="label819" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_dns_server2</span> <b>(Alias name: wifi-dns-server2)</b>  Dns server 2. <span class="li-normal">type: str</span>
 <a id='label820' href="javascript:ContentClick('label821', 'label820');" onmouseover="ContentPreview('label821');" onmouseout="ContentUnpreview('label821');" title="click to collapse or expand..."> more... </a>
 <div id="label821" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wifi_gateway</span> <b>(Alias name: wifi-gateway)</b>  Ipv4 default gateway ip address. <span class="li-normal">type: str</span>
 <a id='label822' href="javascript:ContentClick('label823', 'label822');" onmouseover="ContentPreview('label823');" onmouseout="ContentUnpreview('label823');" title="click to collapse or expand..."> more... </a>
 <div id="label823" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">default_purdue_level</span> <b>(Alias name: default-purdue-level)</b>  Default purdue level of device detected on this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [1, 2, 3, 4, 5, 1.5, 2.5, 3.5, 5.5]</span> 
 <a id='label824' href="javascript:ContentClick('label825', 'label824');" onmouseover="ContentPreview('label825');" onmouseout="ContentUnpreview('label825');" title="click to collapse or expand..."> more... </a>
 <div id="label825" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_broadcast_flag</span> <b>(Alias name: dhcp-broadcast-flag)</b>  Enable/disable setting of the broadcast flag in messages sent by the dhcp client (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label826' href="javascript:ContentClick('label827', 'label826');" onmouseover="ContentPreview('label827');" onmouseout="ContentUnpreview('label827');" title="click to collapse or expand..."> more... </a>
 <div id="label827" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_smart_relay</span> <b>(Alias name: dhcp-smart-relay)</b>  Enable/disable dhcp smart relay. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label828' href="javascript:ContentClick('label829', 'label828');" onmouseover="ContentPreview('label829');" onmouseout="ContentUnpreview('label829');" title="click to collapse or expand..."> more... </a>
 <div id="label829" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_offloading</span> <b>(Alias name: switch-controller-offloading)</b>  Switch controller offloading. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label830' href="javascript:ContentClick('label831', 'label830');" onmouseover="ContentPreview('label831');" onmouseout="ContentUnpreview('label831');" title="click to collapse or expand..."> more... </a>
 <div id="label831" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_offloading_gw</span> <b>(Alias name: switch-controller-offloading-gw)</b>  Switch controller offloading gw. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label832' href="javascript:ContentClick('label833', 'label832');" onmouseover="ContentPreview('label833');" onmouseout="ContentUnpreview('label833');" title="click to collapse or expand..."> more... </a>
 <div id="label833" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_offloading_ip</span> <b>(Alias name: switch-controller-offloading-ip)</b>  Switch controller offloading ip. <span class="li-normal">type: str</span>
 <a id='label834' href="javascript:ContentClick('label835', 'label834');" onmouseover="ContentPreview('label835');" onmouseout="ContentUnpreview('label835');" title="click to collapse or expand..."> more... </a>
 <div id="label835" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_circuit_id</span> <b>(Alias name: dhcp-relay-circuit-id)</b>  Dhcp relay circuit id. <span class="li-normal">type: str</span>
 <a id='label836' href="javascript:ContentClick('label837', 'label836');" onmouseover="ContentPreview('label837');" onmouseout="ContentUnpreview('label837');" title="click to collapse or expand..."> more... </a>
 <div id="label837" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_source_ip</span> <b>(Alias name: dhcp-relay-source-ip)</b>  Ip address used by the dhcp relay as its source ip. <span class="li-normal">type: str</span>
 <a id='label838' href="javascript:ContentClick('label839', 'label838');" onmouseover="ContentPreview('label839');" onmouseout="ContentUnpreview('label839');" title="click to collapse or expand..."> more... </a>
 <div id="label839" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_offload</span> <b>(Alias name: switch-controller-offload)</b>  Enable/disable managed fortiswitch routing offload. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label840' href="javascript:ContentClick('label841', 'label840');" onmouseover="ContentPreview('label841');" onmouseout="ContentUnpreview('label841');" title="click to collapse or expand..."> more... </a>
 <div id="label841" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_offload_gw</span> <b>(Alias name: switch-controller-offload-gw)</b>  Enable/disable managed fortiswitch routing offload gateway. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label842' href="javascript:ContentClick('label843', 'label842');" onmouseover="ContentPreview('label843');" onmouseout="ContentUnpreview('label843');" title="click to collapse or expand..."> more... </a>
 <div id="label843" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">switch_controller_offload_ip</span> <b>(Alias name: switch-controller-offload-ip)</b>  Ip for routing offload on fortiswitch. <span class="li-normal">type: str</span>
 <a id='label844' href="javascript:ContentClick('label845', 'label844');" onmouseover="ContentPreview('label845');" onmouseout="ContentUnpreview('label845');" title="click to collapse or expand..."> more... </a>
 <div id="label845" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mirroring_direction</span> <b>(Alias name: mirroring-direction)</b>  Port mirroring direction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [rx, tx, both]</span> 
 <a id='label846' href="javascript:ContentClick('label847', 'label846');" onmouseover="ContentPreview('label847');" onmouseout="ContentUnpreview('label847');" title="click to collapse or expand..."> more... </a>
 <div id="label847" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mirroring_port</span> <b>(Alias name: mirroring-port)</b>  Mirroring port. <span class="li-normal">type: str</span>
 <a id='label848' href="javascript:ContentClick('label849', 'label848');" onmouseover="ContentPreview('label849');" onmouseout="ContentUnpreview('label849');" title="click to collapse or expand..."> more... </a>
 <div id="label849" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port_mirroring</span> <b>(Alias name: port-mirroring)</b>  Enable/disable np port mirroring. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label850' href="javascript:ContentClick('label851', 'label850');" onmouseover="ContentPreview('label851');" onmouseout="ContentUnpreview('label851');" title="click to collapse or expand..."> more... </a>
 <div id="label851" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_8021x_member_mode</span> <b>(Alias name: security-8021x-member-mode)</b>  802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, switch]</span> 
 <a id='label852' href="javascript:ContentClick('label853', 'label852');" onmouseover="ContentPreview('label853');" onmouseout="ContentUnpreview('label853');" title="click to collapse or expand..."> more... </a>
 <div id="label853" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">stp_edge</span> <b>(Alias name: stp-edge)</b>  Enable/disable as stp edge port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label854' href="javascript:ContentClick('label855', 'label854');" onmouseover="ContentPreview('label855');" onmouseout="ContentUnpreview('label855');" title="click to collapse or expand..."> more... </a>
 <div id="label855" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_allow_no_end_option</span> <b>(Alias name: dhcp-relay-allow-no-end-option)</b>  Enable/disable relaying dhcp messages with no end option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label856' href="javascript:ContentClick('label857', 'label856');" onmouseover="ContentPreview('label857');" onmouseout="ContentUnpreview('label857');" title="click to collapse or expand..."> more... </a>
 <div id="label857" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">netflow_sample_rate</span> <b>(Alias name: netflow-sample-rate)</b>  Netflow sample rate. <span class="li-normal">type: int</span>
 <a id='label858' href="javascript:ContentClick('label859', 'label858');" onmouseover="ContentPreview('label859');" onmouseout="ContentUnpreview('label859');" title="click to collapse or expand..."> more... </a>
 <div id="label859" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">netflow_sampler_id</span> <b>(Alias name: netflow-sampler-id)</b>  Netflow sampler id. <span class="li-normal">type: int</span>
 <a id='label860' href="javascript:ContentClick('label861', 'label860');" onmouseover="ContentPreview('label861');" onmouseout="ContentUnpreview('label861');" title="click to collapse or expand..."> more... </a>
 <div id="label861" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pppoe_egress_cos</span> <b>(Alias name: pppoe-egress-cos)</b>  Cos in vlan tag for outgoing pppoe/ppp packets. <span class="li-normal">type: str</span> <span class="li-normal">choices: [cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span> 
 <a id='label862' href="javascript:ContentClick('label863', 'label862');" onmouseover="ContentPreview('label863');" onmouseout="ContentUnpreview('label863');" title="click to collapse or expand..."> more... </a>
 <div id="label863" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_ip_auth_bypass</span> <b>(Alias name: security-ip-auth-bypass)</b>  Enable/disable ip authentication bypass. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label864' href="javascript:ContentClick('label865', 'label864');" onmouseover="ContentPreview('label865');" onmouseout="ContentUnpreview('label865');" title="click to collapse or expand..."> more... </a>
 <div id="label865" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">virtual_mac</span> <b>(Alias name: virtual-mac)</b>  Change the interfaces virtual mac address. <span class="li-normal">type: str</span>
 <a id='label866' href="javascript:ContentClick('label867', 'label866');" onmouseover="ContentPreview('label867');" onmouseout="ContentUnpreview('label867');" title="click to collapse or expand..."> more... </a>
 <div id="label867" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_vrf_select</span> <b>(Alias name: dhcp-relay-vrf-select)</b>  Vrf id used for connection to server. <span class="li-normal">type: int</span>
 <a id='label868' href="javascript:ContentClick('label869', 'label868');" onmouseover="ContentPreview('label869');" onmouseout="ContentUnpreview('label869');" title="click to collapse or expand..."> more... </a>
 <div id="label869" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">exclude_signatures</span> <b>(Alias name: exclude-signatures)</b>  Exclude iot or ot application signatures. <span class="li-normal">type: list</span> <span class="li-normal">choices: [iot, ot]</span> 
 <a id='label870' href="javascript:ContentClick('label871', 'label870');" onmouseover="ContentPreview('label871');" onmouseout="ContentUnpreview('label871');" title="click to collapse or expand..."> more... </a>
 <div id="label871" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">profiles</span> Set allowed vdsl profiles. <span class="li-normal">type: list</span> <span class="li-normal">choices: [8a, 8b, 8c, 8d, 12a, 12b, 17a, 30a, 35b]</span> 
 <a id='label872' href="javascript:ContentClick('label873', 'label872');" onmouseover="ContentPreview('label873');" onmouseout="ContentUnpreview('label873');" title="click to collapse or expand..."> more... </a>
 <div id="label873" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">telemetry_discover</span> <b>(Alias name: telemetry-discover)</b>  Enable/disable automatic registration of unknown fortitelemetry agents. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label874' href="javascript:ContentClick('label875', 'label874');" onmouseover="ContentPreview('label875');" onmouseout="ContentUnpreview('label875');" title="click to collapse or expand..."> more... </a>
 <div id="label875" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
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
      - name: Configure interfaces.
        fortinet.fortimanager.fmgr_fsp_vlan_interface:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          vlan: <your own value>
          fsp_vlan_interface:
            # ac_name: <string>
            # aggregate: <string>
            # algorithm: <value in [L2, L3, L4, ...]>
            # alias: <string>
            # allowaccess:
            #   - "https"
            #   - "ping"
            #   - "ssh"
            #   - "snmp"
            #   - "http"
            #   - "telnet"
            #   - "fgfm"
            #   - "auto-ipsec"
            #   - "radius-acct"
            #   - "probe-response"
            #   - "capwap"
            #   - "dnp"
            #   - "ftm"
            #   - "fabric"
            #   - "speed-test"
            # ap_discover: <value in [disable, enable]>
            # arpforward: <value in [disable, enable]>
            # atm_protocol: <value in [none, ipoa]>
            # auth_type: <value in [auto, pap, chap, ...]>
            # auto_auth_extension_device: <value in [disable, enable]>
            # bfd: <value in [global, enable, disable]>
            # bfd_desired_min_tx: <integer>
            # bfd_detect_mult: <integer>
            # bfd_required_min_rx: <integer>
            # broadcast_forticlient_discovery: <value in [disable, enable]>
            # broadcast_forward: <value in [disable, enable]>
            # captive_portal: <integer>
            # cli_conn_status: <integer>
            # color: <integer>
            # ddns: <value in [disable, enable]>
            # ddns_auth: <value in [disable, tsig]>
            # ddns_domain: <string>
            # ddns_key: <list or string>
            # ddns_keyname: <string>
            # ddns_password: <list or string>
            # ddns_server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
            # ddns_server_ip: <string>
            # ddns_sn: <string>
            # ddns_ttl: <integer>
            # ddns_username: <string>
            # ddns_zone: <string>
            # dedicated_to: <value in [none, management]>
            # defaultgw: <value in [disable, enable]>
            # description: <string>
            # detected_peer_mtu: <integer>
            # detectprotocol:
            #   - "ping"
            #   - "tcp-echo"
            #   - "udp-echo"
            # detectserver: <string>
            # device_access_list: <list or string>
            # device_identification: <value in [disable, enable]>
            # device_identification_active_scan: <value in [disable, enable]>
            # device_netscan: <value in [disable, enable]>
            # device_user_identification: <value in [disable, enable]>
            # devindex: <integer>
            # dhcp_client_identifier: <string>
            # dhcp_relay_agent_option: <value in [disable, enable]>
            # dhcp_relay_ip: <list or string>
            # dhcp_relay_service: <value in [disable, enable]>
            # dhcp_relay_type: <value in [regular, ipsec]>
            # dhcp_renew_time: <integer>
            # disc_retry_timeout: <integer>
            # disconnect_threshold: <integer>
            # distance: <integer>
            # dns_query: <value in [disable, recursive, non-recursive]>
            # dns_server_override: <value in [disable, enable]>
            # drop_fragment: <value in [disable, enable]>
            # drop_overlapped_fragment: <value in [disable, enable]>
            # egress_cos: <value in [disable, cos0, cos1, ...]>
            # egress_shaping_profile: <string>
            # endpoint_compliance: <value in [disable, enable]>
            # estimated_downstream_bandwidth: <integer>
            # estimated_upstream_bandwidth: <integer>
            # explicit_ftp_proxy: <value in [disable, enable]>
            # explicit_web_proxy: <value in [disable, enable]>
            # external: <value in [disable, enable]>
            # fail_action_on_extender: <value in [soft-restart, hard-restart, reboot]>
            # fail_alert_interfaces: <list or string>
            # fail_alert_method: <value in [link-failed-signal, link-down]>
            # fail_detect: <value in [disable, enable]>
            # fail_detect_option:
            #   - "detectserver"
            #   - "link-down"
            # fdp: <value in [disable, enable]>
            # fortiheartbeat: <value in [disable, enable]>
            # fortilink: <value in [disable, enable]>
            # fortilink_backup_link: <integer>
            # fortilink_split_interface: <value in [disable, enable]>
            # fortilink_stacking: <value in [disable, enable]>
            # forward_domain: <integer>
            # forward_error_correction: <value in [disable, enable, rs-fec, ...]>
            # fp_anomaly:
            #   - "drop_tcp_fin_noack"
            #   - "pass_winnuke"
            #   - "pass_tcpland"
            #   - "pass_udpland"
            #   - "pass_icmpland"
            #   - "pass_ipland"
            #   - "pass_iprr"
            #   - "pass_ipssrr"
            #   - "pass_iplsrr"
            #   - "pass_ipstream"
            #   - "pass_ipsecurity"
            #   - "pass_iptimestamp"
            #   - "pass_ipunknown_option"
            #   - "pass_ipunknown_prot"
            #   - "pass_icmp_frag"
            #   - "pass_tcp_no_flag"
            #   - "pass_tcp_fin_noack"
            #   - "drop_winnuke"
            #   - "drop_tcpland"
            #   - "drop_udpland"
            #   - "drop_icmpland"
            #   - "drop_ipland"
            #   - "drop_iprr"
            #   - "drop_ipssrr"
            #   - "drop_iplsrr"
            #   - "drop_ipstream"
            #   - "drop_ipsecurity"
            #   - "drop_iptimestamp"
            #   - "drop_ipunknown_option"
            #   - "drop_ipunknown_prot"
            #   - "drop_icmp_frag"
            #   - "drop_tcp_no_flag"
            # fp_disable:
            #   - "all"
            #   - "ipsec"
            #   - "none"
            # gateway_address: <string>
            # gi_gk: <value in [disable, enable]>
            # gwaddr: <string>
            # gwdetect: <value in [disable, enable]>
            # ha_priority: <integer>
            # icmp_accept_redirect: <value in [disable, enable]>
            # icmp_redirect: <value in [disable, enable]>
            # icmp_send_redirect: <value in [disable, enable]>
            # ident_accept: <value in [disable, enable]>
            # idle_timeout: <integer>
            # if_mdix: <value in [auto, normal, crossover]>
            # if_media: <value in [auto, copper, fiber]>
            # in_force_vlan_cos: <integer>
            # inbandwidth: <integer>
            # ingress_cos: <value in [disable, cos0, cos1, ...]>
            # ingress_spillover_threshold: <integer>
            # internal: <integer>
            # ip: <string>
            # ipmac: <value in [disable, enable]>
            # ips_sniffer_mode: <value in [disable, enable]>
            # ipunnumbered: <string>
            # ipv6:
            #   autoconf: <value in [disable, enable]>
            #   dhcp6_client_options:
            #     - "rapid"
            #     - "iapd"
            #     - "iana"
            #     - "dns"
            #     - "dnsname"
            #   dhcp6_information_request: <value in [disable, enable]>
            #   dhcp6_prefix_delegation: <value in [disable, enable]>
            #   dhcp6_prefix_hint: <string>
            #   dhcp6_prefix_hint_plt: <integer>
            #   dhcp6_prefix_hint_vlt: <integer>
            #   dhcp6_relay_ip: <string>
            #   dhcp6_relay_service: <value in [disable, enable]>
            #   dhcp6_relay_type: <value in [regular]>
            #   ip6_address: <string>
            #   ip6_allowaccess:
            #     - "https"
            #     - "ping"
            #     - "ssh"
            #     - "snmp"
            #     - "http"
            #     - "telnet"
            #     - "fgfm"
            #     - "capwap"
            #     - "fabric"
            #   ip6_default_life: <integer>
            #   ip6_dns_server_override: <value in [disable, enable]>
            #   ip6_hop_limit: <integer>
            #   ip6_link_mtu: <integer>
            #   ip6_manage_flag: <value in [disable, enable]>
            #   ip6_max_interval: <integer>
            #   ip6_min_interval: <integer>
            #   ip6_mode: <value in [static, dhcp, pppoe, ...]>
            #   ip6_other_flag: <value in [disable, enable]>
            #   ip6_reachable_time: <integer>
            #   ip6_retrans_time: <integer>
            #   ip6_send_adv: <value in [disable, enable]>
            #   ip6_subnet: <string>
            #   ip6_upstream_interface: <string>
            #   nd_cert: <string>
            #   nd_cga_modifier: <string>
            #   nd_mode: <value in [basic, SEND-compatible]>
            #   nd_security_level: <integer>
            #   nd_timestamp_delta: <integer>
            #   nd_timestamp_fuzz: <integer>
            #   vrip6_link_local: <string>
            #   vrrp_virtual_mac6: <value in [disable, enable]>
            #   ip6_delegated_prefix_list:
            #     - autonomous_flag: <value in [disable, enable]>
            #       onlink_flag: <value in [disable, enable]>
            #       prefix_id: <integer>
            #       rdnss: <list or string>
            #       rdnss_service: <value in [delegated, default, specify]>
            #       subnet: <string>
            #       upstream_interface: <string>
            #       delegated_prefix_iaid: <integer>
            #   ip6_extra_addr:
            #     - prefix: <string>
            #   ip6_prefix_list:
            #     - autonomous_flag: <value in [disable, enable]>
            #       dnssl: <list or string>
            #       onlink_flag: <value in [disable, enable]>
            #       preferred_life_time: <integer>
            #       prefix: <string>
            #       rdnss: <list or string>
            #       valid_life_time: <integer>
            #   vrrp6:
            #     - accept_mode: <value in [disable, enable]>
            #       adv_interval: <integer>
            #       preempt: <value in [disable, enable]>
            #       priority: <integer>
            #       start_time: <integer>
            #       status: <value in [disable, enable]>
            #       vrdst6: <string>
            #       vrgrp: <integer>
            #       vrid: <integer>
            #       vrip6: <string>
            #       ignore_default_route: <value in [disable, enable]>
            #       vrdst_priority: <integer>
            #   interface_identifier: <string>
            #   unique_autoconf_addr: <value in [disable, enable]>
            #   icmp6_send_redirect: <value in [disable, enable]>
            #   cli_conn6_status: <integer>
            #   ip6_prefix_mode: <value in [dhcp6, ra]>
            #   ra_send_mtu: <value in [disable, enable]>
            #   ip6_delegated_prefix_iaid: <integer>
            #   dhcp6_relay_source_interface: <value in [disable, enable]>
            #   dhcp6_relay_interface_id: <string>
            #   dhcp6_relay_source_ip: <string>
            #   ip6_adv_rio: <value in [disable, enable]>
            #   ip6_route_pref: <value in [medium, high, low]>
            # l2forward: <value in [disable, enable]>
            # l2tp_client: <value in [disable, enable]>
            # lacp_ha_slave: <value in [disable, enable]>
            # lacp_mode: <value in [static, passive, active]>
            # lacp_speed: <value in [slow, fast]>
            # lcp_echo_interval: <integer>
            # lcp_max_echo_fails: <integer>
            # link_up_delay: <integer>
            # listen_forticlient_connection: <value in [disable, enable]>
            # lldp_network_policy: <string>
            # lldp_reception: <value in [disable, enable, vdom]>
            # lldp_transmission: <value in [enable, disable, vdom]>
            # log: <value in [disable, enable]>
            # macaddr: <string>
            # management_ip: <string>
            # max_egress_burst_rate: <integer>
            # max_egress_rate: <integer>
            # mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
            # member: <list or string>
            # min_links: <integer>
            # min_links_down: <value in [operational, administrative]>
            # mode: <value in [static, dhcp, pppoe, ...]>
            # mtu: <integer>
            # mtu_override: <value in [disable, enable]>
            # mux_type: <value in [llc-encaps, vc-encaps]>
            # name: <string>
            # ndiscforward: <value in [disable, enable]>
            # netbios_forward: <value in [disable, enable]>
            # netflow_sampler: <value in [disable, tx, rx, ...]>
            # npu_fastpath: <value in [disable, enable]>
            # nst: <value in [disable, enable]>
            # out_force_vlan_cos: <integer>
            # outbandwidth: <integer>
            # padt_retry_timeout: <integer>
            # password: <list or string>
            # peer_interface: <list or string>
            # phy_mode: <value in [auto, adsl, vdsl, ...]>
            # ping_serv_status: <integer>
            # poe: <value in [disable, enable]>
            # polling_interval: <integer>
            # pppoe_unnumbered_negotiate: <value in [disable, enable]>
            # pptp_auth_type: <value in [auto, pap, chap, ...]>
            # pptp_client: <value in [disable, enable]>
            # pptp_password: <list or string>
            # pptp_server_ip: <string>
            # pptp_timeout: <integer>
            # pptp_user: <string>
            # preserve_session_route: <value in [disable, enable]>
            # priority: <integer>
            # priority_override: <value in [disable, enable]>
            # proxy_captive_portal: <value in [disable, enable]>
            # redundant_interface: <string>
            # remote_ip: <string>
            # replacemsg_override_group: <string>
            # retransmission: <value in [disable, enable]>
            # role: <value in [lan, wan, dmz, ...]>
            # sample_direction: <value in [rx, tx, both]>
            # sample_rate: <integer>
            # scan_botnet_connections: <value in [disable, block, monitor]>
            # secondary_IP: <value in [disable, enable]>
            # secondaryip:
            #   - allowaccess:
            #       - "https"
            #       - "ping"
            #       - "ssh"
            #       - "snmp"
            #       - "http"
            #       - "telnet"
            #       - "fgfm"
            #       - "auto-ipsec"
            #       - "radius-acct"
            #       - "probe-response"
            #       - "capwap"
            #       - "dnp"
            #       - "ftm"
            #       - "fabric"
            #       - "speed-test"
            #       - "icond"
            #       - "scim"
            #     detectprotocol:
            #       - "ping"
            #       - "tcp-echo"
            #       - "udp-echo"
            #     detectserver: <string>
            #     gwdetect: <value in [disable, enable]>
            #     ha_priority: <integer>
            #     id: <integer>
            #     ip: <string>
            #     ping_serv_status: <integer>
            #     seq: <integer>
            #     secip_relay_ip: <string>
            # security_8021x_dynamic_vlan_id: <integer>
            # security_8021x_master: <string>
            # security_8021x_mode: <value in [default, dynamic-vlan, fallback, ...]>
            # security_exempt_list: <string>
            # security_external_logout: <string>
            # security_external_web: <string>
            # security_groups: <list or string>
            # security_mac_auth_bypass: <value in [disable, enable, mac-auth-only]>
            # security_mode: <value in [none, captive-portal, 802.1X]>
            # security_redirect_url: <string>
            # service_name: <string>
            # sflow_sampler: <value in [disable, enable]>
            # speed: <value in [auto, 10full, 10half, ...]>
            # spillover_threshold: <integer>
            # src_check: <value in [disable, enable]>
            # status: <value in [down, up]>
            # stp: <value in [disable, enable]>
            # stp_ha_slave: <value in [disable, enable, priority-adjust]>
            # stpforward: <value in [disable, enable]>
            # stpforward_mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
            # strip_priority_vlan_tag: <value in [disable, enable]>
            # subst: <value in [disable, enable]>
            # substitute_dst_mac: <string>
            # switch: <string>
            # switch_controller_access_vlan: <value in [disable, enable]>
            # switch_controller_arp_inspection: <value in [disable, enable, monitor]>
            # switch_controller_auth: <value in [radius, usergroup]>
            # switch_controller_dhcp_snooping: <value in [disable, enable]>
            # switch_controller_dhcp_snooping_option82: <value in [disable, enable]>
            # switch_controller_dhcp_snooping_verify_mac: <value in [disable, enable]>
            # switch_controller_igmp_snooping: <value in [disable, enable]>
            # switch_controller_learning_limit: <integer>
            # switch_controller_radius_server: <string>
            # switch_controller_traffic_policy: <string>
            # tc_mode: <value in [ptm, atm]>
            # tcp_mss: <integer>
            # trunk: <value in [disable, enable]>
            # trust_ip_1: <string>
            # trust_ip_2: <string>
            # trust_ip_3: <string>
            # trust_ip6_1: <string>
            # trust_ip6_2: <string>
            # trust_ip6_3: <string>
            # type: <value in [physical, vlan, aggregate, ...]>
            # username: <string>
            # vci: <integer>
            # vectoring: <value in [disable, enable]>
            # vindex: <integer>
            # vlanforward: <value in [disable, enable]>
            # vlanid: <integer>
            # vpi: <integer>
            # vrf: <integer>
            # vrrp:
            #   - accept_mode: <value in [disable, enable]>
            #     adv_interval: <integer>
            #     ignore_default_route: <value in [disable, enable]>
            #     preempt: <value in [disable, enable]>
            #     priority: <integer>
            #     start_time: <integer>
            #     status: <value in [disable, enable]>
            #     version: <value in [2, 3]>
            #     vrdst: <list or string>
            #     vrdst_priority: <integer>
            #     vrgrp: <integer>
            #     vrid: <integer>
            #     vrip: <string>
            #     proxy_arp:
            #       - id: <integer>
            #         ip: <string>
            # vrrp_virtual_mac: <value in [disable, enable]>
            # wccp: <value in [disable, enable]>
            # weight: <integer>
            # wifi_5g_threshold: <string>
            # wifi_acl: <value in [deny, allow]>
            # wifi_ap_band: <value in [any, 5g-preferred, 5g-only]>
            # wifi_auth: <value in [PSK, RADIUS, radius, ...]>
            # wifi_auto_connect: <value in [disable, enable]>
            # wifi_auto_save: <value in [disable, enable]>
            # wifi_broadcast_ssid: <value in [disable, enable]>
            # wifi_encrypt: <value in [TKIP, AES]>
            # wifi_fragment_threshold: <integer>
            # wifi_key: <list or string>
            # wifi_keyindex: <integer>
            # wifi_mac_filter: <value in [disable, enable]>
            # wifi_passphrase: <list or string>
            # wifi_radius_server: <string>
            # wifi_rts_threshold: <integer>
            # wifi_security: <value in [None, WEP64, wep64, ...]>
            # wifi_ssid: <string>
            # wifi_usergroup: <string>
            # wins_ip: <string>
            # eip: <string>
            # fortilink_neighbor_detect: <value in [lldp, fortilink]>
            # ingress_shaping_profile: <string>
            # ring_rx: <integer>
            # ring_tx: <integer>
            # switch_controller_igmp_snooping_fast_leave: <value in [disable, enable]>
            # switch_controller_igmp_snooping_proxy: <value in [disable, enable]>
            # switch_controller_rspan_mode: <value in [disable, enable]>
            # bandwidth_measure_time: <integer>
            # ip_managed_by_fortiipam: <value in [disable, enable, inherit-global]>
            # managed_subnetwork_size: <value in [256, 512, 1024, ...]>
            # measured_downstream_bandwidth: <integer>
            # measured_upstream_bandwidth: <integer>
            # monitor_bandwidth: <value in [disable, enable]>
            # swc_vlan: <integer>
            # switch_controller_feature: <value in [none, default-vlan, quarantine, ...]>
            # switch_controller_mgmt_vlan: <integer>
            # switch_controller_nac: <string>
            # vlan_protocol: <value in [8021q, 8021ad]>
            # dhcp_relay_interface: <string>
            # dhcp_relay_interface_select_method: <value in [auto, sdwan, specify]>
            # np_qos_profile: <integer>
            # swc_first_create: <integer>
            # switch_controller_iot_scanning: <value in [disable, enable]>
            # switch_controller_source_ip: <value in [outbound, fixed]>
            # dhcp_relay_request_all_server: <value in [disable, enable]>
            # stp_ha_secondary: <value in [disable, enable, priority-adjust]>
            # switch_controller_dynamic: <string>
            # auth_cert: <string>
            # auth_portal_addr: <string>
            # dhcp_classless_route_addition: <value in [disable, enable]>
            # dhcp_relay_link_selection: <string>
            # dns_server_protocol:
            #   - "cleartext"
            #   - "dot"
            #   - "doh"
            # eap_ca_cert: <string>
            # eap_identity: <string>
            # eap_method: <value in [tls, peap]>
            # eap_password: <list or string>
            # eap_supplicant: <value in [disable, enable]>
            # eap_user_cert: <string>
            # ike_saml_server: <string>
            # lacp_ha_secondary: <value in [disable, enable]>
            # pvc_atm_qos: <value in [cbr, rt-vbr, nrt-vbr, ...]>
            # pvc_chan: <integer>
            # pvc_crc: <integer>
            # pvc_pcr: <integer>
            # pvc_scr: <integer>
            # pvc_vlan_id: <integer>
            # pvc_vlan_rx_id: <integer>
            # pvc_vlan_rx_op: <value in [pass-through, replace, remove]>
            # pvc_vlan_tx_id: <integer>
            # pvc_vlan_tx_op: <value in [pass-through, replace, remove]>
            # reachable_time: <integer>
            # select_profile_30a_35b: <value in [30A, 35B, 30a, ...]>
            # sfp_dsl: <value in [disable, enable]>
            # sfp_dsl_adsl_fallback: <value in [disable, enable]>
            # sfp_dsl_autodetect: <value in [disable, enable]>
            # sfp_dsl_mac: <string>
            # sw_algorithm: <value in [l2, l3, eh, ...]>
            # system_id: <string>
            # system_id_type: <value in [auto, user]>
            # vlan_id: <integer>
            # vlan_op_mode: <value in [tag, untag, passthrough]>
            # generic_receive_offload: <value in [disable, enable]>
            # interconnect_profile: <value in [default, profile1, profile2]>
            # large_receive_offload: <value in [disable, enable]>
            # annex: <value in [a, b, j, ...]>
            # aggregate_type: <value in [physical, vxlan]>
            # switch_controller_netflow_collect: <value in [disable, enable]>
            # wifi_dns_server1: <string>
            # wifi_dns_server2: <string>
            # wifi_gateway: <string>
            # default_purdue_level: <value in [1, 2, 3, ...]>
            # dhcp_broadcast_flag: <value in [disable, enable]>
            # dhcp_smart_relay: <value in [disable, enable]>
            # switch_controller_offloading: <value in [disable, enable]>
            # switch_controller_offloading_gw: <value in [disable, enable]>
            # switch_controller_offloading_ip: <string>
            # dhcp_relay_circuit_id: <string>
            # dhcp_relay_source_ip: <string>
            # switch_controller_offload: <value in [disable, enable]>
            # switch_controller_offload_gw: <value in [disable, enable]>
            # switch_controller_offload_ip: <string>
            # mirroring_direction: <value in [rx, tx, both]>
            # mirroring_port: <string>
            # port_mirroring: <value in [disable, enable]>
            # security_8021x_member_mode: <value in [disable, switch]>
            # stp_edge: <value in [disable, enable]>
            # dhcp_relay_allow_no_end_option: <value in [disable, enable]>
            # netflow_sample_rate: <integer>
            # netflow_sampler_id: <integer>
            # pppoe_egress_cos: <value in [cos0, cos1, cos2, ...]>
            # security_ip_auth_bypass: <value in [disable, enable]>
            # virtual_mac: <string>
            # dhcp_relay_vrf_select: <integer>
            # exclude_signatures:
            #   - "iot"
            #   - "ot"
            # profiles:
            #   - "8a"
            #   - "8b"
            #   - "8c"
            #   - "8d"
            #   - "12a"
            #   - "12b"
            #   - "17a"
            #   - "30a"
            #   - "35b"
            # telemetry_discover: <value in [disable, enable]>


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
