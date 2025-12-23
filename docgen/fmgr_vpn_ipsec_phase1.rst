:source: fmgr_vpn_ipsec_phase1.py

:orphan:

.. _fmgr_vpn_ipsec_phase1:

fmgr_vpn_ipsec_phase1 -- Configure VPN remote gateway.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.12.0

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>



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
 <li><span class="li-head">revision_note</span> - The change note that can be specified when an object is created or updated. <span class="li-normal">type: string</span> <span class="li-required">required: false</span></li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vpn_ipsec_phase1</span> - Configure VPN remote gateway. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">acct_verify</span> <b>(Alias name: acct-verify)</b>  Enable/disable verification of radius accounting record. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">add_gw_route</span> <b>(Alias name: add-gw-route)</b>  Enable/disable automatically add a route to the remote gateway. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">add_route</span> <b>(Alias name: add-route)</b>  Enable/disable control addition of a route to peer destination selector. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addke1</span> Addke1 group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [0, 1080, 1081, 1082, 1083, 1084, 1085, 1089, 1090, 1091, 1092, 1093, 1094, 35, 36, 37]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addke2</span> Addke2 group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [0, 1080, 1081, 1082, 1083, 1084, 1085, 1089, 1090, 1091, 1092, 1093, 1094, 35, 36, 37]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addke3</span> Addke3 group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [0, 1080, 1081, 1082, 1083, 1084, 1085, 1089, 1090, 1091, 1092, 1093, 1094, 35, 36, 37]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addke4</span> Addke4 group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [0, 1080, 1081, 1082, 1083, 1084, 1085, 1089, 1090, 1091, 1092, 1093, 1094, 35, 36, 37]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addke5</span> Addke5 group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [0, 1080, 1081, 1082, 1083, 1084, 1085, 1089, 1090, 1091, 1092, 1093, 1094, 35, 36, 37]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addke6</span> Addke6 group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [0, 1080, 1081, 1082, 1083, 1084, 1085, 1089, 1090, 1091, 1092, 1093, 1094, 35, 36, 37]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addke7</span> Addke7 group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [0, 1080, 1081, 1082, 1083, 1084, 1085, 1089, 1090, 1091, 1092, 1093, 1094, 35, 36, 37]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">assign_ip</span> <b>(Alias name: assign-ip)</b>  Enable/disable assignment of ip to ipsec interface via configuration method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">assign_ip_from</span> <b>(Alias name: assign-ip-from)</b>  Method by which the ip address will be assigned. <span class="li-normal">type: str</span> <span class="li-normal">choices: [range, usrgrp, dhcp, name]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">authmethod</span> Authentication method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [psk, signature]</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">authmethod_remote</span> <b>(Alias name: authmethod-remote)</b>  Authentication method (remote side). <span class="li-normal">type: str</span> <span class="li-normal">choices: [psk, signature]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">authpasswd</span> Xauth password (max 35 characters). <span class="li-normal">type: list</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">authusr</span> Xauth user name. <span class="li-normal">type: str</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">authusrgrp</span> Authentication user group. <span class="li-normal">type: list</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_negotiate</span> <b>(Alias name: auto-negotiate)</b>  Enable/disable automatic initiation of ike sa negotiation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_transport_threshold</span> <b>(Alias name: auto-transport-threshold)</b>  Timeout in seconds before falling back to next transport protocol. <span class="li-normal">type: int</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">azure_ad_autoconnect</span> <b>(Alias name: azure-ad-autoconnect)</b>  Enable/disable azure ad auto-connect for forticlient. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">backup_gateway</span> <b>(Alias name: backup-gateway)</b>  Instruct unity clients about the backup gateway address(es). <span class="li-normal">type: list</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">banner</span> Message that unity client should display after connecting. <span class="li-normal">type: str</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cert_id_validation</span> <b>(Alias name: cert-id-validation)</b>  Enable/disable cross validation of peer id and the identity in the peers certificate as specified in rfc 4945. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cert_peer_username_strip</span> <b>(Alias name: cert-peer-username-strip)</b>  Enable/disable domain stripping on certificate identity. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cert_peer_username_validation</span> <b>(Alias name: cert-peer-username-validation)</b>  Enable/disable cross validation of peer username and the identity in the peers certificate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [othername, rfc822name, cn, none]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cert_trust_store</span> <b>(Alias name: cert-trust-store)</b>  Ca certificate trust store. <span class="li-normal">type: str</span> <span class="li-normal">choices: [local, ems]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">certificate</span> Names of up to 4 signed personal certificates. <span class="li-normal">type: list</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">childless_ike</span> <b>(Alias name: childless-ike)</b>  Enable/disable childless ikev2 initiation (rfc 6023). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">client_auto_negotiate</span> <b>(Alias name: client-auto-negotiate)</b>  Enable/disable allowing the vpn client to bring up the tunnel when there is no traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">client_keep_alive</span> <b>(Alias name: client-keep-alive)</b>  Enable/disable allowing the vpn client to keep the tunnel up when there is no traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">client_resume</span> <b>(Alias name: client-resume)</b>  Enable/disable resumption of offline forticlient sessions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">client_resume_interval</span> <b>(Alias name: client-resume-interval)</b>  Maximum time in seconds during which a vpn client may resume using a tunnel after a client pc has entered sleep mode or temporarily lost its network connection (120 - 172800, default = 7200). <span class="li-normal">type: int</span>
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">comments</span> Comment. <span class="li-normal">type: str</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dev_id</span> <b>(Alias name: dev-id)</b>  Device id carried by the device id notification. <span class="li-normal">type: str</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dev_id_notification</span> <b>(Alias name: dev-id-notification)</b>  Enable/disable device id notification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_ra_giaddr</span> <b>(Alias name: dhcp-ra-giaddr)</b>  Relay agent gateway ip address to use in the giaddr field of dhcp requests. <span class="li-normal">type: str</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_ra_linkaddr</span> <b>(Alias name: dhcp6-ra-linkaddr)</b>  Relay agent ipv6 link address to use in dhcp6 requests. <span class="li-normal">type: str</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhgrp</span> Dh group. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31, 32]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">digital_signature_auth</span> <b>(Alias name: digital-signature-auth)</b>  Enable/disable ikev2 digital signature authentication (rfc 7427). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">distance</span> Distance for routes added by ike (1 - 255). <span class="li-normal">type: int</span>
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dns_mode</span> <b>(Alias name: dns-mode)</b>  Dns server mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, manual]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dns_suffix_search</span> <b>(Alias name: dns-suffix-search)</b>  One or more dns domain name suffixes in quotes separated by spaces. <span class="li-normal">type: list</span>
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">domain</span> Instruct unity clients about the single default dns domain. <span class="li-normal">type: str</span>
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dpd</span> Dead peer detection mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, on-idle, on-demand]</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dpd_retrycount</span> <b>(Alias name: dpd-retrycount)</b>  Number of dpd retry attempts. <span class="li-normal">type: int</span>
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dpd_retryinterval</span> <b>(Alias name: dpd-retryinterval)</b>  Dpd retry interval. <span class="li-normal">type: list</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap</span> Enable/disable ikev2 eap authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_cert_auth</span> <b>(Alias name: eap-cert-auth)</b>  Enable/disable peer certificate authentication in addition to eap if peer is a forticlient endpoint. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_exclude_peergrp</span> <b>(Alias name: eap-exclude-peergrp)</b>  Peer group excluded from eap authentication. <span class="li-normal">type: list</span>
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_identity</span> <b>(Alias name: eap-identity)</b>  Ikev2 eap peer identity type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [use-id-payload, send-request]</span> 
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ems_sn_check</span> <b>(Alias name: ems-sn-check)</b>  Enable/disable verification of ems serial number. <span class="li-normal">type: str</span> <span class="li-normal">choices: [enable, disable]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">enforce_unique_id</span> <b>(Alias name: enforce-unique-id)</b>  Enable/disable peer id uniqueness check. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, keep-new, keep-old]</span> 
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">esn</span> Extended sequence number (esn) negotiation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, require, allow]</span> 
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">exchange_fgt_device_id</span> <b>(Alias name: exchange-fgt-device-id)</b>  Enable/disable device identifier exchange with peer fortigate units for use of vpn monitor data by fortimanager. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_base</span> <b>(Alias name: fec-base)</b>  Number of base forward error correction packets (1 - 20). <span class="li-normal">type: int</span>
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_codec</span> <b>(Alias name: fec-codec)</b>  Forward error correction encoding/decoding algorithm. <span class="li-normal">type: str</span> <span class="li-normal">choices: [rs, xor]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_egress</span> <b>(Alias name: fec-egress)</b>  Enable/disable forward error correction for egress ipsec traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_health_check</span> <b>(Alias name: fec-health-check)</b>  Sd-wan health check. <span class="li-normal">type: list</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_ingress</span> <b>(Alias name: fec-ingress)</b>  Enable/disable forward error correction for ingress ipsec traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_mapping_profile</span> <b>(Alias name: fec-mapping-profile)</b>  Forward error correction (fec) mapping profile. <span class="li-normal">type: list</span>
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_receive_timeout</span> <b>(Alias name: fec-receive-timeout)</b>  Timeout in milliseconds before dropping forward error correction packets (1 - 1000). <span class="li-normal">type: int</span>
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_redundant</span> <b>(Alias name: fec-redundant)</b>  Number of redundant forward error correction packets (1 - 5 for reed-solomon, 1 for xor). <span class="li-normal">type: int</span>
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fec_send_timeout</span> <b>(Alias name: fec-send-timeout)</b>  Timeout in milliseconds before sending forward error correction packets (1 - 1000). <span class="li-normal">type: int</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fgsp_sync</span> <b>(Alias name: fgsp-sync)</b>  Enable/disable ipsec syncing of tunnels for fgsp ipsec. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortinet_esp</span> <b>(Alias name: fortinet-esp)</b>  Enable/disable fortinet esp encapsulaton. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fragmentation</span> Enable/disable fragment ike message on re-transmission. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fragmentation_mtu</span> <b>(Alias name: fragmentation-mtu)</b>  Ike fragmentation mtu (500 - 16000). <span class="li-normal">type: int</span>
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">group_authentication</span> <b>(Alias name: group-authentication)</b>  Enable/disable ikev2 idi group authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">group_authentication_secret</span> <b>(Alias name: group-authentication-secret)</b>  Password for ikev2 id group authentication. <span class="li-normal">type: list</span>
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ha_sync_esp_seqno</span> <b>(Alias name: ha-sync-esp-seqno)</b>  Enable/disable sequence number jump ahead for ipsec ha. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">idle_timeout</span> <b>(Alias name: idle-timeout)</b>  Enable/disable ipsec tunnel idle timeout. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">idle_timeoutinterval</span> <b>(Alias name: idle-timeoutinterval)</b>  Ipsec tunnel idle timeout in minutes (5 - 43200). <span class="li-normal">type: int</span>
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ike_version</span> <b>(Alias name: ike-version)</b>  Ike protocol version. <span class="li-normal">type: str</span> <span class="li-normal">choices: [1, 2]</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">inbound_dscp_copy</span> <b>(Alias name: inbound-dscp-copy)</b>  Enable/disable copy the dscp in the esp header to the inner ip header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">include_local_lan</span> <b>(Alias name: include-local-lan)</b>  Enable/disable allow local lan access on unity clients. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">interface</span> Local physical, aggregate, or vlan outgoing interface. <span class="li-normal">type: list</span>
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internal_domain_list</span> <b>(Alias name: internal-domain-list)</b>  One or more internal domain names in quotes separated by spaces. <span class="li-normal">type: list</span>
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip_delay_interval</span> <b>(Alias name: ip-delay-interval)</b>  Ip address reuse delay interval in seconds (0 - 28800). <span class="li-normal">type: int</span>
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_dns_server1</span> <b>(Alias name: ipv4-dns-server1)</b>  Ipv4 dns server 1. <span class="li-normal">type: str</span>
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_dns_server2</span> <b>(Alias name: ipv4-dns-server2)</b>  Ipv4 dns server 2. <span class="li-normal">type: str</span>
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_dns_server3</span> <b>(Alias name: ipv4-dns-server3)</b>  Ipv4 dns server 3. <span class="li-normal">type: str</span>
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_end_ip</span> <b>(Alias name: ipv4-end-ip)</b>  End of ipv4 range. <span class="li-normal">type: str</span>
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_exclude_range</span> <b>(Alias name: ipv4-exclude-range)</b>  Ipv4 exclude range. <span class="li-normal">type: list</span>
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">end_ip</span> <b>(Alias name: end-ip)</b>  End of ipv4 exclusive range. <span class="li-normal">type: str</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">start_ip</span> <b>(Alias name: start-ip)</b>  Start of ipv4 exclusive range. <span class="li-normal">type: str</span>
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ipv4_name</span> <b>(Alias name: ipv4-name)</b>  Ipv4 address name. <span class="li-normal">type: list</span>
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_netmask</span> <b>(Alias name: ipv4-netmask)</b>  Ipv4 netmask. <span class="li-normal">type: str</span>
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_split_exclude</span> <b>(Alias name: ipv4-split-exclude)</b>  Ipv4 subnets that should not be sent over the ipsec tunnel. <span class="li-normal">type: list</span>
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_split_include</span> <b>(Alias name: ipv4-split-include)</b>  Ipv4 split-include subnets. <span class="li-normal">type: list</span>
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_start_ip</span> <b>(Alias name: ipv4-start-ip)</b>  Start of ipv4 range. <span class="li-normal">type: str</span>
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_wins_server1</span> <b>(Alias name: ipv4-wins-server1)</b>  Wins server 1. <span class="li-normal">type: str</span>
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv4_wins_server2</span> <b>(Alias name: ipv4-wins-server2)</b>  Wins server 2. <span class="li-normal">type: str</span>
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_auto_linklocal</span> <b>(Alias name: ipv6-auto-linklocal)</b>  Enable/disable auto generation of ipv6 link-local address using last 8 bytes of mode-cfg assigned ipv6 address. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_dns_server1</span> <b>(Alias name: ipv6-dns-server1)</b>  Ipv6 dns server 1. <span class="li-normal">type: str</span>
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_dns_server2</span> <b>(Alias name: ipv6-dns-server2)</b>  Ipv6 dns server 2. <span class="li-normal">type: str</span>
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_dns_server3</span> <b>(Alias name: ipv6-dns-server3)</b>  Ipv6 dns server 3. <span class="li-normal">type: str</span>
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_end_ip</span> <b>(Alias name: ipv6-end-ip)</b>  End of ipv6 range. <span class="li-normal">type: str</span>
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_exclude_range</span> <b>(Alias name: ipv6-exclude-range)</b>  Ipv6 exclude range. <span class="li-normal">type: list</span>
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">end_ip</span> <b>(Alias name: end-ip)</b>  End of ipv6 exclusive range. <span class="li-normal">type: str</span>
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">start_ip</span> <b>(Alias name: start-ip)</b>  Start of ipv6 exclusive range. <span class="li-normal">type: str</span>
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ipv6_name</span> <b>(Alias name: ipv6-name)</b>  Ipv6 address name. <span class="li-normal">type: list</span>
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_prefix</span> <b>(Alias name: ipv6-prefix)</b>  Ipv6 prefix. <span class="li-normal">type: int</span>
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_split_exclude</span> <b>(Alias name: ipv6-split-exclude)</b>  Ipv6 subnets that should not be sent over the ipsec tunnel. <span class="li-normal">type: list</span>
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_split_include</span> <b>(Alias name: ipv6-split-include)</b>  Ipv6 split-include subnets. <span class="li-normal">type: list</span>
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_start_ip</span> <b>(Alias name: ipv6-start-ip)</b>  Start of ipv6 range. <span class="li-normal">type: str</span>
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">keepalive</span> Nat-t keep alive interval. <span class="li-normal">type: int</span>
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">keylife</span> Time to wait in seconds before phase 1 encryption key expires. <span class="li-normal">type: int</span>
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">kms</span> Key management services server. <span class="li-normal">type: list</span>
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">link_cost</span> <b>(Alias name: link-cost)</b>  Vpn tunnel underlay link cost. <span class="li-normal">type: int</span>
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_gw</span> <b>(Alias name: local-gw)</b>  Local vpn gateway. <span class="li-normal">type: str</span>
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">localid</span> Local id. <span class="li-normal">type: str</span>
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">localid_type</span> <b>(Alias name: localid-type)</b>  Local id type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, fqdn, user-fqdn, keyid, address, asn1dn]</span> 
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">loopback_asymroute</span> <b>(Alias name: loopback-asymroute)</b>  Enable/disable asymmetric routing for ike traffic on loopback interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mesh_selector_type</span> <b>(Alias name: mesh-selector-type)</b>  Add selectors containing subsets of the configuration depending on traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, subnet, host]</span> 
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mode</span> Id protection mode used to establish a secure channel. <span class="li-normal">type: str</span> <span class="li-normal">choices: [main, aggressive]</span> 
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mode_cfg</span> <b>(Alias name: mode-cfg)</b>  Enable/disable configuration method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mode_cfg_allow_client_selector</span> <b>(Alias name: mode-cfg-allow-client-selector)</b>  Enable/disable mode-cfg client to use custom phase2 selectors. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Ipsec remote gateway name. <span class="li-normal">type: str</span>
 <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nattraversal</span> Enable/disable nat traversal. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, forced]</span> 
 <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">negotiate_timeout</span> <b>(Alias name: negotiate-timeout)</b>  Ike sa negotiation timeout in seconds (1 - 300). <span class="li-normal">type: int</span>
 <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">network_id</span> <b>(Alias name: network-id)</b>  Vpn gateway network id. <span class="li-normal">type: int</span>
 <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">network_overlay</span> <b>(Alias name: network-overlay)</b>  Enable/disable network overlays. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">npu_offload</span> <b>(Alias name: npu-offload)</b>  Enable/disable offloading npu. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">peer</span> Accept this peer certificate. <span class="li-normal">type: list</span>
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">peergrp</span> Accept this peer certificate group. <span class="li-normal">type: list</span>
 <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">peerid</span> Accept this peer identity. <span class="li-normal">type: str</span>
 <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">peertype</span> Accept this peer type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [any, one, dialup, peer, peergrp]</span> 
 <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ppk</span> Enable/disable ikev2 postquantum preshared key (ppk). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, allow, require]</span> 
 <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ppk_identity</span> <b>(Alias name: ppk-identity)</b>  Ikev2 postquantum preshared key identity. <span class="li-normal">type: str</span>
 <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ppk_secret</span> <b>(Alias name: ppk-secret)</b>  Ikev2 postquantum preshared key (ascii string or hexadecimal encoded with a leading 0x). <span class="li-normal">type: list</span>
 <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Priority for routes added by ike (1 - 65535). <span class="li-normal">type: int</span>
 <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proposal</span> Phase1 proposal. <span class="li-normal">type: str</span> <span class="li-normal">choices: [des-md5, des-sha1, 3des-md5, 3des-sha1, aes128-md5, aes128-sha1, aes192-md5, aes192-sha1, aes256-md5, aes256-sha1, des-sha256, 3des-sha256, aes128-sha256, aes192-sha256, aes256-sha256, des-sha384, des-sha512, 3des-sha384, 3des-sha512, aes128-sha384, aes128-sha512, aes192-sha384, aes192-sha512, aes256-sha384, aes256-sha512, aria128-md5, aria128-sha1, aria128-sha256, aria128-sha384, aria128-sha512, aria192-md5, aria192-sha1, aria192-sha256, aria192-sha384, aria192-sha512, aria256-md5, aria256-sha1, aria256-sha256, aria256-sha384, aria256-sha512, seed-md5, seed-sha1, seed-sha256, seed-sha384, seed-sha512, aes128gcm-prfsha1, aes128gcm-prfsha256, aes128gcm-prfsha384, aes128gcm-prfsha512, aes256gcm-prfsha1, aes256gcm-prfsha256, aes256gcm-prfsha384, aes256gcm-prfsha512, chacha20poly1305-prfsha1, chacha20poly1305-prfsha256, chacha20poly1305-prfsha384, chacha20poly1305-prfsha512]</span> 
 <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">psksecret</span> Pre-shared secret for psk authentication (ascii string or hexadecimal encoded with a leading 0x). <span class="li-normal">type: list</span>
 <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">psksecret_remote</span> <b>(Alias name: psksecret-remote)</b>  Pre-shared secret for remote side psk authentication (ascii string or hexadecimal encoded with a leading 0x). <span class="li-normal">type: list</span>
 <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qkd</span> Enable/disable use of quantum key distribution (qkd) server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, allow, require]</span> 
 <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qkd_hybrid</span> <b>(Alias name: qkd-hybrid)</b>  Enable/disable use of quantum key distribution (qkd) hybrid keys. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, require, allow]</span> 
 <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qkd_profile</span> <b>(Alias name: qkd-profile)</b>  Quantum key distribution (qkd) server profile. <span class="li-normal">type: list</span>
 <a id='label276' href="javascript:ContentClick('label277', 'label276');" onmouseover="ContentPreview('label277');" onmouseout="ContentUnpreview('label277');" title="click to collapse or expand..."> more... </a>
 <div id="label277" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">reauth</span> Enable/disable re-authentication upon ike sa lifetime expiration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label278' href="javascript:ContentClick('label279', 'label278');" onmouseover="ContentPreview('label279');" onmouseout="ContentUnpreview('label279');" title="click to collapse or expand..."> more... </a>
 <div id="label279" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rekey</span> Enable/disable phase1 rekey. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label280' href="javascript:ContentClick('label281', 'label280');" onmouseover="ContentPreview('label281');" onmouseout="ContentUnpreview('label281');" title="click to collapse or expand..."> more... </a>
 <div id="label281" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw</span> <b>(Alias name: remote-gw)</b>  Remote vpn gateway. <span class="li-normal">type: str</span>
 <a id='label282' href="javascript:ContentClick('label283', 'label282');" onmouseover="ContentPreview('label283');" onmouseout="ContentUnpreview('label283');" title="click to collapse or expand..."> more... </a>
 <div id="label283" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw_country</span> <b>(Alias name: remote-gw-country)</b>  Ipv4 addresses associated to a specific country. <span class="li-normal">type: str</span>
 <a id='label284' href="javascript:ContentClick('label285', 'label284');" onmouseover="ContentPreview('label285');" onmouseout="ContentUnpreview('label285');" title="click to collapse or expand..."> more... </a>
 <div id="label285" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw_end_ip</span> <b>(Alias name: remote-gw-end-ip)</b>  Last ipv4 address in the range. <span class="li-normal">type: str</span>
 <a id='label286' href="javascript:ContentClick('label287', 'label286');" onmouseover="ContentPreview('label287');" onmouseout="ContentUnpreview('label287');" title="click to collapse or expand..."> more... </a>
 <div id="label287" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw_match</span> <b>(Alias name: remote-gw-match)</b>  Set type of ipv4 remote gateway address matching. <span class="li-normal">type: str</span> <span class="li-normal">choices: [any, ipmask, iprange, geography, ztna]</span> 
 <a id='label288' href="javascript:ContentClick('label289', 'label288');" onmouseover="ContentPreview('label289');" onmouseout="ContentUnpreview('label289');" title="click to collapse or expand..."> more... </a>
 <div id="label289" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw_start_ip</span> <b>(Alias name: remote-gw-start-ip)</b>  First ipv4 address in the range. <span class="li-normal">type: str</span>
 <a id='label290' href="javascript:ContentClick('label291', 'label290');" onmouseover="ContentPreview('label291');" onmouseout="ContentUnpreview('label291');" title="click to collapse or expand..."> more... </a>
 <div id="label291" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw_subnet</span> <b>(Alias name: remote-gw-subnet)</b>  Ipv4 address and subnet mask. <span class="li-normal">type: list</span>
 <a id='label292' href="javascript:ContentClick('label293', 'label292');" onmouseover="ContentPreview('label293');" onmouseout="ContentUnpreview('label293');" title="click to collapse or expand..."> more... </a>
 <div id="label293" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw_ztna_tags</span> <b>(Alias name: remote-gw-ztna-tags)</b>  Ipv4 ztna posture tags. <span class="li-normal">type: list</span>
 <a id='label294' href="javascript:ContentClick('label295', 'label294');" onmouseover="ContentPreview('label295');" onmouseout="ContentUnpreview('label295');" title="click to collapse or expand..."> more... </a>
 <div id="label295" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw6_country</span> <b>(Alias name: remote-gw6-country)</b>  Ipv6 addresses associated to a specific country. <span class="li-normal">type: str</span>
 <a id='label296' href="javascript:ContentClick('label297', 'label296');" onmouseover="ContentPreview('label297');" onmouseout="ContentUnpreview('label297');" title="click to collapse or expand..."> more... </a>
 <div id="label297" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw6_end_ip</span> <b>(Alias name: remote-gw6-end-ip)</b>  Last ipv6 address in the range. <span class="li-normal">type: str</span>
 <a id='label298' href="javascript:ContentClick('label299', 'label298');" onmouseover="ContentPreview('label299');" onmouseout="ContentUnpreview('label299');" title="click to collapse or expand..."> more... </a>
 <div id="label299" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw6_match</span> <b>(Alias name: remote-gw6-match)</b>  Set type of ipv6 remote gateway address matching. <span class="li-normal">type: str</span> <span class="li-normal">choices: [any, iprange, geography, ipprefix]</span> 
 <a id='label300' href="javascript:ContentClick('label301', 'label300');" onmouseover="ContentPreview('label301');" onmouseout="ContentUnpreview('label301');" title="click to collapse or expand..."> more... </a>
 <div id="label301" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw6_start_ip</span> <b>(Alias name: remote-gw6-start-ip)</b>  First ipv6 address in the range. <span class="li-normal">type: str</span>
 <a id='label302' href="javascript:ContentClick('label303', 'label302');" onmouseover="ContentPreview('label303');" onmouseout="ContentUnpreview('label303');" title="click to collapse or expand..."> more... </a>
 <div id="label303" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_gw6_subnet</span> <b>(Alias name: remote-gw6-subnet)</b>  Ipv6 address and prefix. <span class="li-normal">type: str</span>
 <a id='label304' href="javascript:ContentClick('label305', 'label304');" onmouseover="ContentPreview('label305');" onmouseout="ContentUnpreview('label305');" title="click to collapse or expand..."> more... </a>
 <div id="label305" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remotegw_ddns</span> <b>(Alias name: remotegw-ddns)</b>  Domain name of remote gateway. <span class="li-normal">type: str</span>
 <a id='label306' href="javascript:ContentClick('label307', 'label306');" onmouseover="ContentPreview('label307');" onmouseout="ContentUnpreview('label307');" title="click to collapse or expand..."> more... </a>
 <div id="label307" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rsa_signature_format</span> <b>(Alias name: rsa-signature-format)</b>  Digital signature authentication rsa signature format. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pkcs1, pss]</span> 
 <a id='label308' href="javascript:ContentClick('label309', 'label308');" onmouseover="ContentPreview('label309');" onmouseout="ContentUnpreview('label309');" title="click to collapse or expand..."> more... </a>
 <div id="label309" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rsa_signature_hash_override</span> <b>(Alias name: rsa-signature-hash-override)</b>  Enable/disable ikev2 rsa signature hash algorithm override. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label310' href="javascript:ContentClick('label311', 'label310');" onmouseover="ContentPreview('label311');" onmouseout="ContentUnpreview('label311');" title="click to collapse or expand..."> more... </a>
 <div id="label311" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">save_password</span> <b>(Alias name: save-password)</b>  Enable/disable saving xauth username and password on vpn clients. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label312' href="javascript:ContentClick('label313', 'label312');" onmouseover="ContentPreview('label313');" onmouseout="ContentUnpreview('label313');" title="click to collapse or expand..."> more... </a>
 <div id="label313" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">send_cert_chain</span> <b>(Alias name: send-cert-chain)</b>  Enable/disable sending certificate chain. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label314' href="javascript:ContentClick('label315', 'label314');" onmouseover="ContentPreview('label315');" onmouseout="ContentUnpreview('label315');" title="click to collapse or expand..."> more... </a>
 <div id="label315" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">shared_idle_timeout</span> <b>(Alias name: shared-idle-timeout)</b>  Enable/disable ipsec tunnel shared idle timeout. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label316' href="javascript:ContentClick('label317', 'label316');" onmouseover="ContentPreview('label317');" onmouseout="ContentUnpreview('label317');" title="click to collapse or expand..."> more... </a>
 <div id="label317" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">signature_hash_alg</span> <b>(Alias name: signature-hash-alg)</b>  Digital signature authentication hash algorithms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [sha1, sha2-256, sha2-384, sha2-512]</span> 
 <a id='label318' href="javascript:ContentClick('label319', 'label318');" onmouseover="ContentPreview('label319');" onmouseout="ContentUnpreview('label319');" title="click to collapse or expand..."> more... </a>
 <div id="label319" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">split_include_service</span> <b>(Alias name: split-include-service)</b>  Split-include services. <span class="li-normal">type: list</span>
 <a id='label320' href="javascript:ContentClick('label321', 'label320');" onmouseover="ContentPreview('label321');" onmouseout="ContentUnpreview('label321');" title="click to collapse or expand..."> more... </a>
 <div id="label321" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">suite_b</span> <b>(Alias name: suite-b)</b>  Use suite-b. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, suite-b-gcm-128, suite-b-gcm-256]</span> 
 <a id='label322' href="javascript:ContentClick('label323', 'label322');" onmouseover="ContentPreview('label323');" onmouseout="ContentUnpreview('label323');" title="click to collapse or expand..."> more... </a>
 <div id="label323" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">transit_gateway</span> <b>(Alias name: transit-gateway)</b>  Ipsec tunnel created by autoscaling to be used as a transit gateway. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label324' href="javascript:ContentClick('label325', 'label324');" onmouseover="ContentPreview('label325');" onmouseout="ContentUnpreview('label325');" title="click to collapse or expand..."> more... </a>
 <div id="label325" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">transport</span> Set ike transport protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [udp, tcp, auto, udp-fallback-tcp]</span> 
 <a id='label326' href="javascript:ContentClick('label327', 'label326');" onmouseover="ContentPreview('label327');" onmouseout="ContentUnpreview('label327');" title="click to collapse or expand..."> more... </a>
 <div id="label327" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">type</span> Remote gateway type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, dynamic, ddns]</span> 
 <a id='label328' href="javascript:ContentClick('label329', 'label328');" onmouseover="ContentPreview('label329');" onmouseout="ContentUnpreview('label329');" title="click to collapse or expand..."> more... </a>
 <div id="label329" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">unity_support</span> <b>(Alias name: unity-support)</b>  Enable/disable support for cisco unity configuration method extensions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label330' href="javascript:ContentClick('label331', 'label330');" onmouseover="ContentPreview('label331');" onmouseout="ContentUnpreview('label331');" title="click to collapse or expand..."> more... </a>
 <div id="label331" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">usrgrp</span> User group name for dialup peers. <span class="li-normal">type: list</span>
 <a id='label332' href="javascript:ContentClick('label333', 'label332');" onmouseover="ContentPreview('label333');" onmouseout="ContentUnpreview('label333');" title="click to collapse or expand..."> more... </a>
 <div id="label333" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wizard_type</span> <b>(Alias name: wizard-type)</b>  Gui vpn wizard type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [custom, dialup-forticlient, dialup-ios, dialup-android, dialup-cisco, static-fortigate, static-cisco, dialup-windows, dialup-fortigate, dialup-cisco-fw, simplified-static-fortigate, hub-fortigate-auto-discovery, spoke-fortigate-auto-discovery, fabric-overlay-orchestrator]</span> 
 <a id='label334' href="javascript:ContentClick('label335', 'label334');" onmouseover="ContentPreview('label335');" onmouseout="ContentUnpreview('label335');" title="click to collapse or expand..."> more... </a>
 <div id="label335" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">xauthtype</span> Xauth type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, client, pap, chap, auto]</span> 
 <a id='label336' href="javascript:ContentClick('label337', 'label336');" onmouseover="ContentPreview('label337');" onmouseout="ContentUnpreview('label337');" title="click to collapse or expand..."> more... </a>
 <div id="label337" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fallback_tcp_threshold</span> <b>(Alias name: fallback-tcp-threshold)</b>  Timeout in seconds before falling back ike/ipsec traffic to tcp. <span class="li-normal">type: int</span>
 <a id='label338' href="javascript:ContentClick('label339', 'label338');" onmouseover="ContentPreview('label339');" onmouseout="ContentUnpreview('label339');" title="click to collapse or expand..."> more... </a>
 <div id="label339" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forticlient_enforcement</span> <b>(Alias name: forticlient-enforcement)</b>  Enable/disable forticlient enforcement. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label340' href="javascript:ContentClick('label341', 'label340');" onmouseover="ContentPreview('label341');" onmouseout="ContentUnpreview('label341');" title="click to collapse or expand..."> more... </a>
 <div id="label341" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.4 -> latest</code></p>
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
      - name: Configure VPN remote gateway.
        fortinet.fortimanager.fmgr_vpn_ipsec_phase1:
          # bypass_validation: false
          # workspace_locking_adom: <global or your adom name>
          # workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          state: present # <value in [present, absent]>
          vpn_ipsec_phase1:
            name: "your value" # Required variable, string
            # acct_verify: <value in [disable, enable]>
            # add_gw_route: <value in [disable, enable]>
            # add_route: <value in [disable, enable]>
            # addke1:
            #   - "0"
            #   - "1080"
            #   - "1081"
            #   - "1082"
            #   - "1083"
            #   - "1084"
            #   - "1085"
            #   - "1089"
            #   - "1090"
            #   - "1091"
            #   - "1092"
            #   - "1093"
            #   - "1094"
            #   - "35"
            #   - "36"
            #   - "37"
            # addke2:
            #   - "0"
            #   - "1080"
            #   - "1081"
            #   - "1082"
            #   - "1083"
            #   - "1084"
            #   - "1085"
            #   - "1089"
            #   - "1090"
            #   - "1091"
            #   - "1092"
            #   - "1093"
            #   - "1094"
            #   - "35"
            #   - "36"
            #   - "37"
            # addke3:
            #   - "0"
            #   - "1080"
            #   - "1081"
            #   - "1082"
            #   - "1083"
            #   - "1084"
            #   - "1085"
            #   - "1089"
            #   - "1090"
            #   - "1091"
            #   - "1092"
            #   - "1093"
            #   - "1094"
            #   - "35"
            #   - "36"
            #   - "37"
            # addke4:
            #   - "0"
            #   - "1080"
            #   - "1081"
            #   - "1082"
            #   - "1083"
            #   - "1084"
            #   - "1085"
            #   - "1089"
            #   - "1090"
            #   - "1091"
            #   - "1092"
            #   - "1093"
            #   - "1094"
            #   - "35"
            #   - "36"
            #   - "37"
            # addke5:
            #   - "0"
            #   - "1080"
            #   - "1081"
            #   - "1082"
            #   - "1083"
            #   - "1084"
            #   - "1085"
            #   - "1089"
            #   - "1090"
            #   - "1091"
            #   - "1092"
            #   - "1093"
            #   - "1094"
            #   - "35"
            #   - "36"
            #   - "37"
            # addke6:
            #   - "0"
            #   - "1080"
            #   - "1081"
            #   - "1082"
            #   - "1083"
            #   - "1084"
            #   - "1085"
            #   - "1089"
            #   - "1090"
            #   - "1091"
            #   - "1092"
            #   - "1093"
            #   - "1094"
            #   - "35"
            #   - "36"
            #   - "37"
            # addke7:
            #   - "0"
            #   - "1080"
            #   - "1081"
            #   - "1082"
            #   - "1083"
            #   - "1084"
            #   - "1085"
            #   - "1089"
            #   - "1090"
            #   - "1091"
            #   - "1092"
            #   - "1093"
            #   - "1094"
            #   - "35"
            #   - "36"
            #   - "37"
            # assign_ip: <value in [disable, enable]>
            # assign_ip_from: <value in [range, usrgrp, dhcp, ...]>
            # authmethod: <value in [psk, signature]>
            # authmethod_remote: <value in [psk, signature]>
            # authpasswd: <list or string>
            # authusr: <string>
            # authusrgrp: <list or string>
            # auto_negotiate: <value in [disable, enable]>
            # auto_transport_threshold: <integer>
            # azure_ad_autoconnect: <value in [disable, enable]>
            # backup_gateway: <list or string>
            # banner: <string>
            # cert_id_validation: <value in [disable, enable]>
            # cert_peer_username_strip: <value in [disable, enable]>
            # cert_peer_username_validation: <value in [othername, rfc822name, cn, ...]>
            # cert_trust_store: <value in [local, ems]>
            # certificate: <list or string>
            # childless_ike: <value in [disable, enable]>
            # client_auto_negotiate: <value in [disable, enable]>
            # client_keep_alive: <value in [disable, enable]>
            # client_resume: <value in [disable, enable]>
            # client_resume_interval: <integer>
            # comments: <string>
            # dev_id: <string>
            # dev_id_notification: <value in [disable, enable]>
            # dhcp_ra_giaddr: <string>
            # dhcp6_ra_linkaddr: <string>
            # dhgrp:
            #   - "1"
            #   - "2"
            #   - "5"
            #   - "14"
            #   - "15"
            #   - "16"
            #   - "17"
            #   - "18"
            #   - "19"
            #   - "20"
            #   - "21"
            #   - "27"
            #   - "28"
            #   - "29"
            #   - "30"
            #   - "31"
            #   - "32"
            # digital_signature_auth: <value in [disable, enable]>
            # distance: <integer>
            # dns_mode: <value in [auto, manual]>
            # dns_suffix_search: <list or string>
            # domain: <string>
            # dpd: <value in [disable, on-idle, on-demand]>
            # dpd_retrycount: <integer>
            # dpd_retryinterval: <list or integer>
            # eap: <value in [disable, enable]>
            # eap_cert_auth: <value in [disable, enable]>
            # eap_exclude_peergrp: <list or string>
            # eap_identity: <value in [use-id-payload, send-request]>
            # ems_sn_check: <value in [enable, disable]>
            # enforce_unique_id: <value in [disable, keep-new, keep-old]>
            # esn: <value in [disable, require, allow]>
            # exchange_fgt_device_id: <value in [disable, enable]>
            # fec_base: <integer>
            # fec_codec: <value in [rs, xor]>
            # fec_egress: <value in [disable, enable]>
            # fec_health_check: <list or string>
            # fec_ingress: <value in [disable, enable]>
            # fec_mapping_profile: <list or string>
            # fec_receive_timeout: <integer>
            # fec_redundant: <integer>
            # fec_send_timeout: <integer>
            # fgsp_sync: <value in [disable, enable]>
            # fortinet_esp: <value in [disable, enable]>
            # fragmentation: <value in [disable, enable]>
            # fragmentation_mtu: <integer>
            # group_authentication: <value in [disable, enable]>
            # group_authentication_secret: <list or string>
            # ha_sync_esp_seqno: <value in [disable, enable]>
            # idle_timeout: <value in [disable, enable]>
            # idle_timeoutinterval: <integer>
            # ike_version: <value in [1, 2]>
            # inbound_dscp_copy: <value in [disable, enable]>
            # include_local_lan: <value in [disable, enable]>
            # interface: <list or string>
            # internal_domain_list: <list or string>
            # ip_delay_interval: <integer>
            # ipv4_dns_server1: <string>
            # ipv4_dns_server2: <string>
            # ipv4_dns_server3: <string>
            # ipv4_end_ip: <string>
            # ipv4_exclude_range:
            #   - end_ip: <string>
            #     id: <integer>
            #     start_ip: <string>
            # ipv4_name: <list or string>
            # ipv4_netmask: <string>
            # ipv4_split_exclude: <list or string>
            # ipv4_split_include: <list or string>
            # ipv4_start_ip: <string>
            # ipv4_wins_server1: <string>
            # ipv4_wins_server2: <string>
            # ipv6_auto_linklocal: <value in [disable, enable]>
            # ipv6_dns_server1: <string>
            # ipv6_dns_server2: <string>
            # ipv6_dns_server3: <string>
            # ipv6_end_ip: <string>
            # ipv6_exclude_range:
            #   - end_ip: <string>
            #     id: <integer>
            #     start_ip: <string>
            # ipv6_name: <list or string>
            # ipv6_prefix: <integer>
            # ipv6_split_exclude: <list or string>
            # ipv6_split_include: <list or string>
            # ipv6_start_ip: <string>
            # keepalive: <integer>
            # keylife: <integer>
            # kms: <list or string>
            # link_cost: <integer>
            # local_gw: <string>
            # localid: <string>
            # localid_type: <value in [auto, fqdn, user-fqdn, ...]>
            # loopback_asymroute: <value in [disable, enable]>
            # mesh_selector_type: <value in [disable, subnet, host]>
            # mode: <value in [main, aggressive]>
            # mode_cfg: <value in [disable, enable]>
            # mode_cfg_allow_client_selector: <value in [disable, enable]>
            # nattraversal: <value in [disable, enable, forced]>
            # negotiate_timeout: <integer>
            # network_id: <integer>
            # network_overlay: <value in [disable, enable]>
            # npu_offload: <value in [disable, enable]>
            # peer: <list or string>
            # peergrp: <list or string>
            # peerid: <string>
            # peertype: <value in [any, one, dialup, ...]>
            # ppk: <value in [disable, allow, require]>
            # ppk_identity: <string>
            # ppk_secret: <list or string>
            # priority: <integer>
            # proposal: <value in [des-md5, des-sha1, 3des-md5, ...]>
            # psksecret: <list or string>
            # psksecret_remote: <list or string>
            # qkd: <value in [disable, allow, require]>
            # qkd_hybrid: <value in [disable, require, allow]>
            # qkd_profile: <list or string>
            # reauth: <value in [disable, enable]>
            # rekey: <value in [disable, enable]>
            # remote_gw: <string>
            # remote_gw_country: <string>
            # remote_gw_end_ip: <string>
            # remote_gw_match: <value in [any, ipmask, iprange, ...]>
            # remote_gw_start_ip: <string>
            # remote_gw_subnet: <list or string>
            # remote_gw_ztna_tags: <list or string>
            # remote_gw6_country: <string>
            # remote_gw6_end_ip: <string>
            # remote_gw6_match: <value in [any, iprange, geography, ...]>
            # remote_gw6_start_ip: <string>
            # remote_gw6_subnet: <string>
            # remotegw_ddns: <string>
            # rsa_signature_format: <value in [pkcs1, pss]>
            # rsa_signature_hash_override: <value in [disable, enable]>
            # save_password: <value in [disable, enable]>
            # send_cert_chain: <value in [disable, enable]>
            # shared_idle_timeout: <value in [disable, enable]>
            # signature_hash_alg:
            #   - "sha1"
            #   - "sha2-256"
            #   - "sha2-384"
            #   - "sha2-512"
            # split_include_service: <list or string>
            # suite_b: <value in [disable, suite-b-gcm-128, suite-b-gcm-256]>
            # transit_gateway: <value in [disable, enable]>
            # transport: <value in [udp, tcp, auto, ...]>
            # type: <value in [static, dynamic, ddns]>
            # unity_support: <value in [disable, enable]>
            # usrgrp: <list or string>
            # wizard_type: <value in [custom, dialup-forticlient, dialup-ios, ...]>
            # xauthtype: <value in [disable, client, pap, ...]>
            # fallback_tcp_threshold: <integer>
            # forticlient_enforcement: <value in [disable, enable]>


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
