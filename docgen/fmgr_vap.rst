:source: fmgr_vap.py

:orphan:

.. _fmgr_vap:

fmgr_vap -- Configure Virtual Access Points (VAPs).
+++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock. <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vap</span> - Configure Virtual Access Points <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_centmgmt</span> Centmgmt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_dhcp_svr_id</span> Dhcp svr id. <span class="li-normal">type: str</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_allowaccess</span> Intf allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_device_identification</span> <b>(Alias name: _intf_device-identification)</b>  Intf device identification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_device_netscan</span> <b>(Alias name: _intf_device-netscan)</b>  Intf device netscan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp_relay_ip</span> <b>(Alias name: _intf_dhcp-relay-ip)</b>  Intf dhcp relay ip. <span class="li-normal">type: list</span>
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp_relay_service</span> <b>(Alias name: _intf_dhcp-relay-service)</b>  Intf dhcp relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp_relay_type</span> <b>(Alias name: _intf_dhcp-relay-type)</b>  Intf dhcp relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular, ipsec]</span>  <span class="li-normal">default: regular</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp6_relay_ip</span> <b>(Alias name: _intf_dhcp6-relay-ip)</b>  Intf dhcp6 relay ip. <span class="li-normal">type: str</span>
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp6_relay_service</span> <b>(Alias name: _intf_dhcp6-relay-service)</b>  Intf dhcp6 relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp6_relay_type</span> <b>(Alias name: _intf_dhcp6-relay-type)</b>  Intf dhcp6 relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular]</span>  <span class="li-normal">default: regular</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip</span> Intf ip. <span class="li-normal">type: str</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip6_address</span> <b>(Alias name: _intf_ip6-address)</b>  Intf ip6 address. <span class="li-normal">type: str</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip6_allowaccess</span> <b>(Alias name: _intf_ip6-allowaccess)</b>  Intf ip6 allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, any, fgfm, capwap]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_listen_forticlient_connection</span> <b>(Alias name: _intf_listen-forticlient-connection)</b>  Intf listen forticlient connection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">acct_interim_interval</span> <b>(Alias name: acct-interim-interval)</b>  Wifi radius accounting interim interval (60 - 86400 sec, default = 0). <span class="li-normal">type: int</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">alias</span> Alias. <span class="li-normal">type: str</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth</span> Authentication protocol. <span class="li-normal">type: str</span> <span class="li-normal">choices: [PSK, psk, RADIUS, radius, usergroup]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">broadcast_ssid</span> <b>(Alias name: broadcast-ssid)</b>  Enable/disable broadcasting the ssid (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">broadcast_suppression</span> <b>(Alias name: broadcast-suppression)</b>  Optional suppression of broadcast messages. <span class="li-normal">type: list</span> <span class="li-normal">choices: [dhcp, arp, dhcp2, arp2, netbios-ns, netbios-ds, arp3, dhcp-up, dhcp-down, arp-known, arp-unknown, arp-reply, ipv6, dhcp-starvation, arp-poison, all-other-mc, all-other-bc, arp-proxy, dhcp-ucast]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_ac_name</span> <b>(Alias name: captive-portal-ac-name)</b>  Local-bridging captive portal ac-name. <span class="li-normal">type: str</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_macauth_radius_secret</span> <b>(Alias name: captive-portal-macauth-radius-secret)</b>  Secret key to access the macauth radius server. <span class="li-normal">type: list</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_macauth_radius_server</span> <b>(Alias name: captive-portal-macauth-radius-server)</b>  Captive portal external radius server domain name or ip address. <span class="li-normal">type: str</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_radius_secret</span> <b>(Alias name: captive-portal-radius-secret)</b>  Secret key to access the radius server. <span class="li-normal">type: list</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_radius_server</span> <b>(Alias name: captive-portal-radius-server)</b>  Captive portal radius server domain name or ip address. <span class="li-normal">type: str</span>
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_session_timeout_interval</span> <b>(Alias name: captive-portal-session-timeout-interval)</b>  Session timeout interval (0 - 864000 sec, default = 0). <span class="li-normal">type: int</span>
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_lease_time</span> <b>(Alias name: dhcp-lease-time)</b>  Dhcp lease time in seconds for nat ip address. <span class="li-normal">type: int</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option82_circuit_id_insertion</span> <b>(Alias name: dhcp-option82-circuit-id-insertion)</b>  Enable/disable dhcp option 82 circuit-id insert (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, style-1, style-2, style-3]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option82_insertion</span> <b>(Alias name: dhcp-option82-insertion)</b>  Enable/disable dhcp option 82 insert (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option82_remote_id_insertion</span> <b>(Alias name: dhcp-option82-remote-id-insertion)</b>  Enable/disable dhcp option 82 remote-id insert (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, style-1]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dynamic_vlan</span> <b>(Alias name: dynamic-vlan)</b>  Enable/disable dynamic vlan assignment. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dynamic_mapping</span> Dynamic mapping. <span class="li-normal">type: list</span>
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">_centmgmt</span> Centmgmt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_dhcp_svr_id</span> Dhcp svr id. <span class="li-normal">type: str</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_allowaccess</span> Intf allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_device_identification</span> <b>(Alias name: _intf_device-identification)</b>  Intf device identification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_device_netscan</span> <b>(Alias name: _intf_device-netscan)</b>  Intf device netscan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp_relay_ip</span> <b>(Alias name: _intf_dhcp-relay-ip)</b>  Intf dhcp relay ip. <span class="li-normal">type: list</span>
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp_relay_service</span> <b>(Alias name: _intf_dhcp-relay-service)</b>  Intf dhcp relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp_relay_type</span> <b>(Alias name: _intf_dhcp-relay-type)</b>  Intf dhcp relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular, ipsec]</span>  <span class="li-normal">default: regular</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp6_relay_ip</span> <b>(Alias name: _intf_dhcp6-relay-ip)</b>  Intf dhcp6 relay ip. <span class="li-normal">type: str</span>
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp6_relay_service</span> <b>(Alias name: _intf_dhcp6-relay-service)</b>  Intf dhcp6 relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_dhcp6_relay_type</span> <b>(Alias name: _intf_dhcp6-relay-type)</b>  Intf dhcp6 relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular]</span>  <span class="li-normal">default: regular</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip</span> Intf ip. <span class="li-normal">type: str</span>
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip6_address</span> <b>(Alias name: _intf_ip6-address)</b>  Intf ip6 address. <span class="li-normal">type: str</span>
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip6_allowaccess</span> <b>(Alias name: _intf_ip6-allowaccess)</b>  Intf ip6 allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, any, fgfm, capwap]</span> 
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_listen_forticlient_connection</span> <b>(Alias name: _intf_listen-forticlient-connection)</b>  Intf listen forticlient connection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_scope</span> Scope. <span class="li-normal">type: list</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">name</span> Name. <span class="li-normal">type: str</span>
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vdom</span> Vdom. <span class="li-normal">type: str</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">acct_interim_interval</span> <b>(Alias name: acct-interim-interval)</b>  Acct interim interval. <span class="li-normal">type: int</span>
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">address_group</span> <b>(Alias name: address-group)</b>  Address group. <span class="li-normal">type: str</span>
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">alias</span> Alias. <span class="li-normal">type: str</span>
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">atf_weight</span> <b>(Alias name: atf-weight)</b>  Atf weight. <span class="li-normal">type: int</span>
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth</span> Auth. <span class="li-normal">type: str</span> <span class="li-normal">choices: [PSK, psk, RADIUS, radius, usergroup]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">broadcast_ssid</span> <b>(Alias name: broadcast-ssid)</b>  Broadcast ssid. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">broadcast_suppression</span> <b>(Alias name: broadcast-suppression)</b>  Broadcast suppression. <span class="li-normal">type: list</span> <span class="li-normal">choices: [dhcp, arp, dhcp2, arp2, netbios-ns, netbios-ds, arp3, dhcp-up, dhcp-down, arp-known, arp-unknown, arp-reply, ipv6, dhcp-starvation, arp-poison, all-other-mc, all-other-bc, arp-proxy, dhcp-ucast]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_ac_name</span> <b>(Alias name: captive-portal-ac-name)</b>  Captive portal ac name. <span class="li-normal">type: str</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_macauth_radius_secret</span> <b>(Alias name: captive-portal-macauth-radius-secret)</b>  Captive portal macauth radius secret. <span class="li-normal">type: list</span>
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_macauth_radius_server</span> <b>(Alias name: captive-portal-macauth-radius-server)</b>  Captive portal macauth radius server. <span class="li-normal">type: str</span>
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_radius_secret</span> <b>(Alias name: captive-portal-radius-secret)</b>  Captive portal radius secret. <span class="li-normal">type: list</span>
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_radius_server</span> <b>(Alias name: captive-portal-radius-server)</b>  Captive portal radius server. <span class="li-normal">type: str</span>
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_session_timeout_interval</span> <b>(Alias name: captive-portal-session-timeout-interval)</b>  Captive portal session timeout interval. <span class="li-normal">type: int</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">client_count</span> <b>(Alias name: client-count)</b>  Client count. <span class="li-normal">type: int</span>
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_lease_time</span> <b>(Alias name: dhcp-lease-time)</b>  Dhcp lease time. <span class="li-normal">type: int</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option82_circuit_id_insertion</span> <b>(Alias name: dhcp-option82-circuit-id-insertion)</b>  Dhcp option82 circuit id insertion. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, style-1, style-2, style-3]</span> 
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option82_insertion</span> <b>(Alias name: dhcp-option82-insertion)</b>  Dhcp option82 insertion. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option82_remote_id_insertion</span> <b>(Alias name: dhcp-option82-remote-id-insertion)</b>  Dhcp option82 remote id insertion. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, style-1]</span> 
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dynamic_vlan</span> <b>(Alias name: dynamic-vlan)</b>  Dynamic vlan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_reauth</span> <b>(Alias name: eap-reauth)</b>  Eap reauth. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_reauth_intv</span> <b>(Alias name: eap-reauth-intv)</b>  Eap reauth intv. <span class="li-normal">type: int</span>
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eapol_key_retries</span> <b>(Alias name: eapol-key-retries)</b>  Eapol key retries. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">encrypt</span> Encrypt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [TKIP, AES, TKIP-AES]</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_fast_roaming</span> <b>(Alias name: external-fast-roaming)</b>  External fast roaming. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_logout</span> <b>(Alias name: external-logout)</b>  External logout. <span class="li-normal">type: str</span>
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_web</span> <b>(Alias name: external-web)</b>  External web. <span class="li-normal">type: str</span>
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fast_bss_transition</span> <b>(Alias name: fast-bss-transition)</b>  Fast bss transition. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fast_roaming</span> <b>(Alias name: fast-roaming)</b>  Fast roaming. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ft_mobility_domain</span> <b>(Alias name: ft-mobility-domain)</b>  Ft mobility domain. <span class="li-normal">type: int</span>
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ft_over_ds</span> <b>(Alias name: ft-over-ds)</b>  Ft over ds. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ft_r0_key_lifetime</span> <b>(Alias name: ft-r0-key-lifetime)</b>  Ft r0 key lifetime. <span class="li-normal">type: int</span>
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gtk_rekey</span> <b>(Alias name: gtk-rekey)</b>  Gtk rekey. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gtk_rekey_intv</span> <b>(Alias name: gtk-rekey-intv)</b>  Gtk rekey intv. <span class="li-normal">type: int</span>
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hotspot20_profile</span> <b>(Alias name: hotspot20-profile)</b>  Hotspot20 profile. <span class="li-normal">type: str</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">intra_vap_privacy</span> <b>(Alias name: intra-vap-privacy)</b>  Intra vap privacy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ip. <span class="li-normal">type: str</span>
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">key</span> Key. <span class="li-normal">type: list</span>
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">keyindex</span> Keyindex. <span class="li-normal">type: int</span>
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldpc</span> Ldpc. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, tx, rx, rxtx]</span> 
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_authentication</span> <b>(Alias name: local-authentication)</b>  Local authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_bridging</span> <b>(Alias name: local-bridging)</b>  Local bridging. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_lan</span> <b>(Alias name: local-lan)</b>  Local lan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [deny, allow]</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone</span> <b>(Alias name: local-standalone)</b>  Local standalone. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone_nat</span> <b>(Alias name: local-standalone-nat)</b>  Local standalone nat. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_switching</span> <b>(Alias name: local-switching)</b>  Local switching. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_auth_bypass</span> <b>(Alias name: mac-auth-bypass)</b>  Mac auth bypass. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_filter</span> <b>(Alias name: mac-filter)</b>  Mac filter. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_filter_policy_other</span> <b>(Alias name: mac-filter-policy-other)</b>  Mac filter policy other. <span class="li-normal">type: str</span> <span class="li-normal">choices: [deny, allow]</span> 
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_clients</span> <b>(Alias name: max-clients)</b>  Max clients. <span class="li-normal">type: int</span>
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_clients_ap</span> <b>(Alias name: max-clients-ap)</b>  Max clients ap. <span class="li-normal">type: int</span>
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">me_disable_thresh</span> <b>(Alias name: me-disable-thresh)</b>  Me disable thresh. <span class="li-normal">type: int</span>
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mesh_backhaul</span> <b>(Alias name: mesh-backhaul)</b>  Mesh backhaul. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk</span> Mpsk. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk_concurrent_clients</span> <b>(Alias name: mpsk-concurrent-clients)</b>  Mpsk concurrent clients. <span class="li-normal">type: int</span>
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">multicast_enhance</span> <b>(Alias name: multicast-enhance)</b>  Multicast enhance. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">multicast_rate</span> <b>(Alias name: multicast-rate)</b>  Multicast rate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [0, 6000, 12000, 24000]</span> 
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">okc</span> Okc. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">owe_groups</span> <b>(Alias name: owe-groups)</b>  Owe groups. <span class="li-normal">type: list</span> <span class="li-normal">choices: [19, 20, 21]</span> 
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">owe_transition</span> <b>(Alias name: owe-transition)</b>  Owe transition. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">owe_transition_ssid</span> <b>(Alias name: owe-transition-ssid)</b>  Owe transition ssid. <span class="li-normal">type: str</span>
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">passphrase</span> Passphrase. <span class="li-normal">type: list</span>
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pmf</span> Pmf. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, optional]</span> 
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pmf_assoc_comeback_timeout</span> <b>(Alias name: pmf-assoc-comeback-timeout)</b>  Pmf assoc comeback timeout. <span class="li-normal">type: int</span>
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pmf_sa_query_retry_timeout</span> <b>(Alias name: pmf-sa-query-retry-timeout)</b>  Pmf sa query retry timeout. <span class="li-normal">type: int</span>
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">portal_message_override_group</span> <b>(Alias name: portal-message-override-group)</b>  Portal message override group. <span class="li-normal">type: str</span>
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">portal_type</span> <b>(Alias name: portal-type)</b>  Portal type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auth, auth+disclaimer, disclaimer, email-collect, cmcc, cmcc-macauth, auth-mac, external-auth, external-macauth]</span> 
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">probe_resp_suppression</span> <b>(Alias name: probe-resp-suppression)</b>  Probe resp suppression. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">probe_resp_threshold</span> <b>(Alias name: probe-resp-threshold)</b>  Probe resp threshold. <span class="li-normal">type: str</span>
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ptk_rekey</span> <b>(Alias name: ptk-rekey)</b>  Ptk rekey. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ptk_rekey_intv</span> <b>(Alias name: ptk-rekey-intv)</b>  Ptk rekey intv. <span class="li-normal">type: int</span>
 <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qos_profile</span> <b>(Alias name: qos-profile)</b>  Qos profile. <span class="li-normal">type: str</span>
 <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Quarantine. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radio_2g_threshold</span> <b>(Alias name: radio-2g-threshold)</b>  Radio 2g threshold. <span class="li-normal">type: str</span>
 <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radio_5g_threshold</span> <b>(Alias name: radio-5g-threshold)</b>  Radio 5g threshold. <span class="li-normal">type: str</span>
 <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radio_sensitivity</span> <b>(Alias name: radio-sensitivity)</b>  Radio sensitivity. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth</span> <b>(Alias name: radius-mac-auth)</b>  Radius mac auth. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth_server</span> <b>(Alias name: radius-mac-auth-server)</b>  Radius mac auth server. <span class="li-normal">type: str</span>
 <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth_usergroups</span> <b>(Alias name: radius-mac-auth-usergroups)</b>  Radius mac auth usergroups. <span class="li-normal">type: list</span>
 <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_server</span> <b>(Alias name: radius-server)</b>  Radius server. <span class="li-normal">type: str</span>
 <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11a</span> <b>(Alias name: rates-11a)</b>  Rates 11a. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> 
 <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ac_ss12</span> <b>(Alias name: rates-11ac-ss12)</b>  Rates 11ac ss12. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/1, mcs9/1, mcs0/2, mcs1/2, mcs2/2, mcs3/2, mcs4/2, mcs5/2, mcs6/2, mcs7/2, mcs8/2, mcs9/2, mcs10/1, mcs11/1, mcs10/2, mcs11/2]</span> 
 <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ac_ss34</span> <b>(Alias name: rates-11ac-ss34)</b>  Rates 11ac ss34. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/3, mcs1/3, mcs2/3, mcs3/3, mcs4/3, mcs5/3, mcs6/3, mcs7/3, mcs8/3, mcs9/3, mcs0/4, mcs1/4, mcs2/4, mcs3/4, mcs4/4, mcs5/4, mcs6/4, mcs7/4, mcs8/4, mcs9/4, mcs10/3, mcs11/3, mcs10/4, mcs11/4]</span> 
 <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11bg</span> <b>(Alias name: rates-11bg)</b>  Rates 11bg. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> 
 <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11n_ss12</span> <b>(Alias name: rates-11n-ss12)</b>  Rates 11n ss12. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/2, mcs9/2, mcs10/2, mcs11/2, mcs12/2, mcs13/2, mcs14/2, mcs15/2]</span> 
 <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11n_ss34</span> <b>(Alias name: rates-11n-ss34)</b>  Rates 11n ss34. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs16/3, mcs17/3, mcs18/3, mcs19/3, mcs20/3, mcs21/3, mcs22/3, mcs23/3, mcs24/4, mcs25/4, mcs26/4, mcs27/4, mcs28/4, mcs29/4, mcs30/4, mcs31/4]</span> 
 <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_groups</span> <b>(Alias name: sae-groups)</b>  Sae groups. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31]</span> 
 <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_password</span> <b>(Alias name: sae-password)</b>  Sae password. <span class="li-normal">type: list</span>
 <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">schedule</span> Schedule. <span class="li-normal">type: list or str</span>
 <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security</span> Security. <span class="li-normal">type: str</span> <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, captive-portal, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise, wpa-personal+captive-portal, wpa-only-personal+captive-portal, wpa2-only-personal+captive-portal, osen, wpa3-enterprise, sae, sae-transition, owe, wpa3-sae, wpa3-sae-transition, wpa3-only-enterprise, wpa3-enterprise-transition]</span> 
 <a id='label276' href="javascript:ContentClick('label277', 'label276');" onmouseover="ContentPreview('label277');" onmouseout="ContentUnpreview('label277');" title="click to collapse or expand..."> more... </a>
 <div id="label277" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_exempt_list</span> <b>(Alias name: security-exempt-list)</b>  Security exempt list. <span class="li-normal">type: str</span>
 <a id='label278' href="javascript:ContentClick('label279', 'label278');" onmouseover="ContentPreview('label279');" onmouseout="ContentUnpreview('label279');" title="click to collapse or expand..."> more... </a>
 <div id="label279" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_obsolete_option</span> <b>(Alias name: security-obsolete-option)</b>  Security obsolete option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label280' href="javascript:ContentClick('label281', 'label280');" onmouseover="ContentPreview('label281');" onmouseout="ContentUnpreview('label281');" title="click to collapse or expand..."> more... </a>
 <div id="label281" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_redirect_url</span> <b>(Alias name: security-redirect-url)</b>  Security redirect url. <span class="li-normal">type: str</span>
 <a id='label282' href="javascript:ContentClick('label283', 'label282');" onmouseover="ContentPreview('label283');" onmouseout="ContentUnpreview('label283');" title="click to collapse or expand..."> more... </a>
 <div id="label283" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">selected_usergroups</span> <b>(Alias name: selected-usergroups)</b>  Selected usergroups. <span class="li-normal">type: list or str</span>
 <a id='label284' href="javascript:ContentClick('label285', 'label284');" onmouseover="ContentPreview('label285');" onmouseout="ContentUnpreview('label285');" title="click to collapse or expand..."> more... </a>
 <div id="label285" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">split_tunneling</span> <b>(Alias name: split-tunneling)</b>  Split tunneling. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label286' href="javascript:ContentClick('label287', 'label286');" onmouseover="ContentPreview('label287');" onmouseout="ContentUnpreview('label287');" title="click to collapse or expand..."> more... </a>
 <div id="label287" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssid</span> Ssid. <span class="li-normal">type: str</span>
 <a id='label288' href="javascript:ContentClick('label289', 'label288');" onmouseover="ContentPreview('label289');" onmouseout="ContentUnpreview('label289');" title="click to collapse or expand..."> more... </a>
 <div id="label289" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tkip_counter_measure</span> <b>(Alias name: tkip-counter-measure)</b>  Tkip counter measure. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label290' href="javascript:ContentClick('label291', 'label290');" onmouseover="ContentPreview('label291');" onmouseout="ContentUnpreview('label291');" title="click to collapse or expand..."> more... </a>
 <div id="label291" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">usergroup</span> Usergroup. <span class="li-normal">type: list or str</span>
 <a id='label292' href="javascript:ContentClick('label293', 'label292');" onmouseover="ContentPreview('label293');" onmouseout="ContentUnpreview('label293');" title="click to collapse or expand..."> more... </a>
 <div id="label293" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">utm_profile</span> <b>(Alias name: utm-profile)</b>  Utm profile. <span class="li-normal">type: str</span>
 <a id='label294' href="javascript:ContentClick('label295', 'label294');" onmouseover="ContentPreview('label295');" onmouseout="ContentUnpreview('label295');" title="click to collapse or expand..."> more... </a>
 <div id="label295" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vdom</span> Vdom. <span class="li-normal">type: list or str</span>
 <a id='label296' href="javascript:ContentClick('label297', 'label296');" onmouseover="ContentPreview('label297');" onmouseout="ContentUnpreview('label297');" title="click to collapse or expand..."> more... </a>
 <div id="label297" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_auto</span> <b>(Alias name: vlan-auto)</b>  Vlan auto. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label298' href="javascript:ContentClick('label299', 'label298');" onmouseover="ContentPreview('label299');" onmouseout="ContentUnpreview('label299');" title="click to collapse or expand..."> more... </a>
 <div id="label299" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_pooling</span> <b>(Alias name: vlan-pooling)</b>  Vlan pooling. <span class="li-normal">type: str</span> <span class="li-normal">choices: [wtp-group, round-robin, hash, disable]</span> 
 <a id='label300' href="javascript:ContentClick('label301', 'label300');" onmouseover="ContentPreview('label301');" onmouseout="ContentUnpreview('label301');" title="click to collapse or expand..."> more... </a>
 <div id="label301" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlanid</span> Vlanid. <span class="li-normal">type: int</span>
 <a id='label302' href="javascript:ContentClick('label303', 'label302');" onmouseover="ContentPreview('label303');" onmouseout="ContentUnpreview('label303');" title="click to collapse or expand..."> more... </a>
 <div id="label303" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">voice_enterprise</span> <b>(Alias name: voice-enterprise)</b>  Voice enterprise. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label304' href="javascript:ContentClick('label305', 'label304');" onmouseover="ContentPreview('label305');" onmouseout="ContentUnpreview('label305');" title="click to collapse or expand..."> more... </a>
 <div id="label305" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mu_mimo</span> <b>(Alias name: mu-mimo)</b>  Mu mimo. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label306' href="javascript:ContentClick('label307', 'label306');" onmouseover="ContentPreview('label307');" onmouseout="ContentUnpreview('label307');" title="click to collapse or expand..."> more... </a>
 <div id="label307" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_device_access_list</span> <b>(Alias name: _intf_device-access-list)</b>  Intf device access list. <span class="li-normal">type: str</span>
 <a id='label308' href="javascript:ContentClick('label309', 'label308');" onmouseover="ContentPreview('label309');" onmouseout="ContentUnpreview('label309');" title="click to collapse or expand..."> more... </a>
 <div id="label309" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_web_format</span> <b>(Alias name: external-web-format)</b>  External web format. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto-detect, no-query-string, partial-query-string]</span> 
 <a id='label310' href="javascript:ContentClick('label311', 'label310');" onmouseover="ContentPreview('label311');" onmouseout="ContentUnpreview('label311');" title="click to collapse or expand..."> more... </a>
 <div id="label311" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">high_efficiency</span> <b>(Alias name: high-efficiency)</b>  High efficiency. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label312' href="javascript:ContentClick('label313', 'label312');" onmouseover="ContentPreview('label313');" onmouseout="ContentUnpreview('label313');" title="click to collapse or expand..."> more... </a>
 <div id="label313" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">primary_wag_profile</span> <b>(Alias name: primary-wag-profile)</b>  Primary wag profile. <span class="li-normal">type: str</span>
 <a id='label314' href="javascript:ContentClick('label315', 'label314');" onmouseover="ContentPreview('label315');" onmouseout="ContentUnpreview('label315');" title="click to collapse or expand..."> more... </a>
 <div id="label315" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">secondary_wag_profile</span> <b>(Alias name: secondary-wag-profile)</b>  Secondary wag profile. <span class="li-normal">type: str</span>
 <a id='label316' href="javascript:ContentClick('label317', 'label316');" onmouseover="ContentPreview('label317');" onmouseout="ContentUnpreview('label317');" title="click to collapse or expand..."> more... </a>
 <div id="label317" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">target_wake_time</span> <b>(Alias name: target-wake-time)</b>  Target wake time. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label318' href="javascript:ContentClick('label319', 'label318');" onmouseover="ContentPreview('label319');" onmouseout="ContentUnpreview('label319');" title="click to collapse or expand..."> more... </a>
 <div id="label319" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tunnel_echo_interval</span> <b>(Alias name: tunnel-echo-interval)</b>  Tunnel echo interval. <span class="li-normal">type: int</span>
 <a id='label320' href="javascript:ContentClick('label321', 'label320');" onmouseover="ContentPreview('label321');" onmouseout="ContentUnpreview('label321');" title="click to collapse or expand..."> more... </a>
 <div id="label321" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tunnel_fallback_interval</span> <b>(Alias name: tunnel-fallback-interval)</b>  Tunnel fallback interval. <span class="li-normal">type: int</span>
 <a id='label322' href="javascript:ContentClick('label323', 'label322');" onmouseover="ContentPreview('label323');" onmouseout="ContentUnpreview('label323');" title="click to collapse or expand..."> more... </a>
 <div id="label323" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">access_control_list</span> <b>(Alias name: access-control-list)</b>  Access control list. <span class="li-normal">type: str</span>
 <a id='label324' href="javascript:ContentClick('label325', 'label324');" onmouseover="ContentPreview('label325');" onmouseout="ContentUnpreview('label325');" title="click to collapse or expand..."> more... </a>
 <div id="label325" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_auth_timeout</span> <b>(Alias name: captive-portal-auth-timeout)</b>  Captive portal auth timeout. <span class="li-normal">type: int</span>
 <a id='label326' href="javascript:ContentClick('label327', 'label326');" onmouseover="ContentPreview('label327');" onmouseout="ContentUnpreview('label327');" title="click to collapse or expand..."> more... </a>
 <div id="label327" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_rules</span> <b>(Alias name: ipv6-rules)</b>  Ipv6 rules. <span class="li-normal">type: list</span> <span class="li-normal">choices: [drop-icmp6ra, drop-icmp6rs, drop-llmnr6, drop-icmp6mld2, drop-dhcp6s, drop-dhcp6c, ndp-proxy, drop-ns-dad, drop-ns-nondad]</span> 
 <a id='label328' href="javascript:ContentClick('label329', 'label328');" onmouseover="ContentPreview('label329');" onmouseout="ContentUnpreview('label329');" title="click to collapse or expand..."> more... </a>
 <div id="label329" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_remove</span> <b>(Alias name: sticky-client-remove)</b>  Sticky client remove. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label330' href="javascript:ContentClick('label331', 'label330');" onmouseover="ContentPreview('label331');" onmouseout="ContentUnpreview('label331');" title="click to collapse or expand..."> more... </a>
 <div id="label331" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_threshold_2g</span> <b>(Alias name: sticky-client-threshold-2g)</b>  Sticky client threshold 2g. <span class="li-normal">type: str</span>
 <a id='label332' href="javascript:ContentClick('label333', 'label332');" onmouseover="ContentPreview('label333');" onmouseout="ContentUnpreview('label333');" title="click to collapse or expand..."> more... </a>
 <div id="label333" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_threshold_5g</span> <b>(Alias name: sticky-client-threshold-5g)</b>  Sticky client threshold 5g. <span class="li-normal">type: str</span>
 <a id='label334' href="javascript:ContentClick('label335', 'label334');" onmouseover="ContentPreview('label335');" onmouseout="ContentUnpreview('label335');" title="click to collapse or expand..."> more... </a>
 <div id="label335" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bss_color_partial</span> <b>(Alias name: bss-color-partial)</b>  Bss color partial. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label336' href="javascript:ContentClick('label337', 'label336');" onmouseover="ContentPreview('label337');" onmouseout="ContentUnpreview('label337');" title="click to collapse or expand..."> more... </a>
 <div id="label337" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option43_insertion</span> <b>(Alias name: dhcp-option43-insertion)</b>  Dhcp option43 insertion. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label338' href="javascript:ContentClick('label339', 'label338');" onmouseover="ContentPreview('label339');" onmouseout="ContentUnpreview('label339');" title="click to collapse or expand..."> more... </a>
 <div id="label339" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk_profile</span> <b>(Alias name: mpsk-profile)</b>  Mpsk profile. <span class="li-normal">type: str</span>
 <a id='label340' href="javascript:ContentClick('label341', 'label340');" onmouseover="ContentPreview('label341');" onmouseout="ContentUnpreview('label341');" title="click to collapse or expand..."> more... </a>
 <div id="label341" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">igmp_snooping</span> <b>(Alias name: igmp-snooping)</b>  Enable/disable igmp snooping. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label342' href="javascript:ContentClick('label343', 'label342');" onmouseover="ContentPreview('label343');" onmouseout="ContentUnpreview('label343');" title="click to collapse or expand..."> more... </a>
 <div id="label343" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port_macauth</span> <b>(Alias name: port-macauth)</b>  Enable/disable lan port mac authentication (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, radius, address-group]</span> 
 <a id='label344' href="javascript:ContentClick('label345', 'label344');" onmouseover="ContentPreview('label345');" onmouseout="ContentUnpreview('label345');" title="click to collapse or expand..."> more... </a>
 <div id="label345" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port_macauth_reauth_timeout</span> <b>(Alias name: port-macauth-reauth-timeout)</b>  Lan port mac authentication re-authentication timeout value (default = 7200 sec). <span class="li-normal">type: int</span>
 <a id='label346' href="javascript:ContentClick('label347', 'label346');" onmouseover="ContentPreview('label347');" onmouseout="ContentUnpreview('label347');" title="click to collapse or expand..."> more... </a>
 <div id="label347" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port_macauth_timeout</span> <b>(Alias name: port-macauth-timeout)</b>  Lan port mac authentication idle timeout value (default = 600 sec). <span class="li-normal">type: int</span>
 <a id='label348' href="javascript:ContentClick('label349', 'label348');" onmouseover="ContentPreview('label349');" onmouseout="ContentUnpreview('label349');" title="click to collapse or expand..."> more... </a>
 <div id="label349" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">additional_akms</span> <b>(Alias name: additional-akms)</b>  Additional akms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [akm6, akm24]</span> 
 <a id='label350' href="javascript:ContentClick('label351', 'label350');" onmouseover="ContentPreview('label351');" onmouseout="ContentUnpreview('label351');" title="click to collapse or expand..."> more... </a>
 <div id="label351" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bstm_disassociation_imminent</span> <b>(Alias name: bstm-disassociation-imminent)</b>  Enable/disable forcing of disassociation after the bstm request timer has been reached (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label352' href="javascript:ContentClick('label353', 'label352');" onmouseover="ContentPreview('label353');" onmouseout="ContentUnpreview('label353');" title="click to collapse or expand..."> more... </a>
 <div id="label353" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bstm_load_balancing_disassoc_timer</span> <b>(Alias name: bstm-load-balancing-disassoc-timer)</b>  Time interval for client to voluntarily leave ap before forcing a disassociation due to ap load-balancing (0 to 30, default = 10). <span class="li-normal">type: int</span>
 <a id='label354' href="javascript:ContentClick('label355', 'label354');" onmouseover="ContentPreview('label355');" onmouseout="ContentUnpreview('label355');" title="click to collapse or expand..."> more... </a>
 <div id="label355" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bstm_rssi_disassoc_timer</span> <b>(Alias name: bstm-rssi-disassoc-timer)</b>  Time interval for client to voluntarily leave ap before forcing a disassociation due to low rssi (0 to 2000, default = 200). <span class="li-normal">type: int</span>
 <a id='label356' href="javascript:ContentClick('label357', 'label356');" onmouseover="ContentPreview('label357');" onmouseout="ContentUnpreview('label357');" title="click to collapse or expand..."> more... </a>
 <div id="label357" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_address_enforcement</span> <b>(Alias name: dhcp-address-enforcement)</b>  Enable/disable dhcp address enforcement (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label358' href="javascript:ContentClick('label359', 'label358');" onmouseover="ContentPreview('label359');" onmouseout="ContentUnpreview('label359');" title="click to collapse or expand..."> more... </a>
 <div id="label359" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gas_comeback_delay</span> <b>(Alias name: gas-comeback-delay)</b>  Gas comeback delay (0 or 100 - 10000 milliseconds, default = 500). <span class="li-normal">type: int</span>
 <a id='label360' href="javascript:ContentClick('label361', 'label360');" onmouseover="ContentPreview('label361');" onmouseout="ContentUnpreview('label361');" title="click to collapse or expand..."> more... </a>
 <div id="label361" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gas_fragmentation_limit</span> <b>(Alias name: gas-fragmentation-limit)</b>  Gas fragmentation limit (512 - 4096, default = 1024). <span class="li-normal">type: int</span>
 <a id='label362' href="javascript:ContentClick('label363', 'label362');" onmouseover="ContentPreview('label363');" onmouseout="ContentUnpreview('label363');" title="click to collapse or expand..."> more... </a>
 <div id="label363" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_called_station_delimiter</span> <b>(Alias name: mac-called-station-delimiter)</b>  Mac called station delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label364' href="javascript:ContentClick('label365', 'label364');" onmouseover="ContentPreview('label365');" onmouseout="ContentUnpreview('label365');" title="click to collapse or expand..."> more... </a>
 <div id="label365" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_calling_station_delimiter</span> <b>(Alias name: mac-calling-station-delimiter)</b>  Mac calling station delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label366' href="javascript:ContentClick('label367', 'label366');" onmouseover="ContentPreview('label367');" onmouseout="ContentUnpreview('label367');" title="click to collapse or expand..."> more... </a>
 <div id="label367" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_case</span> <b>(Alias name: mac-case)</b>  Mac case (default = uppercase). <span class="li-normal">type: str</span> <span class="li-normal">choices: [uppercase, lowercase]</span> 
 <a id='label368' href="javascript:ContentClick('label369', 'label368');" onmouseover="ContentPreview('label369');" onmouseout="ContentUnpreview('label369');" title="click to collapse or expand..."> more... </a>
 <div id="label369" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_password_delimiter</span> <b>(Alias name: mac-password-delimiter)</b>  Mac authentication password delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label370' href="javascript:ContentClick('label371', 'label370');" onmouseover="ContentPreview('label371');" onmouseout="ContentUnpreview('label371');" title="click to collapse or expand..."> more... </a>
 <div id="label371" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_username_delimiter</span> <b>(Alias name: mac-username-delimiter)</b>  Mac authentication username delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label372' href="javascript:ContentClick('label373', 'label372');" onmouseover="ContentPreview('label373');" onmouseout="ContentUnpreview('label373');" title="click to collapse or expand..."> more... </a>
 <div id="label373" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mbo</span> Enable/disable multiband operation (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label374' href="javascript:ContentClick('label375', 'label374');" onmouseover="ContentPreview('label375');" onmouseout="ContentUnpreview('label375');" title="click to collapse or expand..."> more... </a>
 <div id="label375" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mbo_cell_data_conn_pref</span> <b>(Alias name: mbo-cell-data-conn-pref)</b>  Mbo cell data connection preference (0, 1, or 255, default = 1). <span class="li-normal">type: str</span> <span class="li-normal">choices: [excluded, prefer-not, prefer-use]</span> 
 <a id='label376' href="javascript:ContentClick('label377', 'label376');" onmouseover="ContentPreview('label377');" onmouseout="ContentUnpreview('label377');" title="click to collapse or expand..."> more... </a>
 <div id="label377" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nac</span> Enable/disable network access control. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label378' href="javascript:ContentClick('label379', 'label378');" onmouseover="ContentPreview('label379');" onmouseout="ContentUnpreview('label379');" title="click to collapse or expand..."> more... </a>
 <div id="label379" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nac_profile</span> <b>(Alias name: nac-profile)</b>  Nac profile name. <span class="li-normal">type: str</span>
 <a id='label380' href="javascript:ContentClick('label381', 'label380');" onmouseover="ContentPreview('label381');" onmouseout="ContentUnpreview('label381');" title="click to collapse or expand..."> more... </a>
 <div id="label381" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">neighbor_report_dual_band</span> <b>(Alias name: neighbor-report-dual-band)</b>  Enable/disable dual-band neighbor report (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label382' href="javascript:ContentClick('label383', 'label382');" onmouseover="ContentPreview('label383');" onmouseout="ContentUnpreview('label383');" title="click to collapse or expand..."> more... </a>
 <div id="label383" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">address_group_policy</span> <b>(Alias name: address-group-policy)</b>  Configure mac address filtering policy for mac addresses that are in the address-group. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, allow, deny]</span> 
 <a id='label384' href="javascript:ContentClick('label385', 'label384');" onmouseover="ContentPreview('label385');" onmouseout="ContentUnpreview('label385');" title="click to collapse or expand..."> more... </a>
 <div id="label385" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antivirus_profile</span> <b>(Alias name: antivirus-profile)</b>  Antivirus profile name. <span class="li-normal">type: str</span>
 <a id='label386' href="javascript:ContentClick('label387', 'label386');" onmouseover="ContentPreview('label387');" onmouseout="ContentUnpreview('label387');" title="click to collapse or expand..."> more... </a>
 <div id="label387" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_detection_engine</span> <b>(Alias name: application-detection-engine)</b>  Enable/disable application detection engine (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label388' href="javascript:ContentClick('label389', 'label388');" onmouseover="ContentPreview('label389');" onmouseout="ContentUnpreview('label389');" title="click to collapse or expand..."> more... </a>
 <div id="label389" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_list</span> <b>(Alias name: application-list)</b>  Application control list name. <span class="li-normal">type: str</span>
 <a id='label390' href="javascript:ContentClick('label391', 'label390');" onmouseover="ContentPreview('label391');" onmouseout="ContentUnpreview('label391');" title="click to collapse or expand..."> more... </a>
 <div id="label391" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_report_intv</span> <b>(Alias name: application-report-intv)</b>  Application report interval (30 - 864000 sec, default = 120). <span class="li-normal">type: int</span>
 <a id='label392' href="javascript:ContentClick('label393', 'label392');" onmouseover="ContentPreview('label393');" onmouseout="ContentUnpreview('label393');" title="click to collapse or expand..."> more... </a>
 <div id="label393" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_cert</span> <b>(Alias name: auth-cert)</b>  Https server certificate. <span class="li-normal">type: str</span>
 <a id='label394' href="javascript:ContentClick('label395', 'label394');" onmouseover="ContentPreview('label395');" onmouseout="ContentUnpreview('label395');" title="click to collapse or expand..."> more... </a>
 <div id="label395" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_portal_addr</span> <b>(Alias name: auth-portal-addr)</b>  Address of captive portal. <span class="li-normal">type: str</span>
 <a id='label396' href="javascript:ContentClick('label397', 'label396');" onmouseover="ContentPreview('label397');" onmouseout="ContentUnpreview('label397');" title="click to collapse or expand..."> more... </a>
 <div id="label397" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">beacon_advertising</span> <b>(Alias name: beacon-advertising)</b>  Fortinet beacon advertising ie data   (default = empty). <span class="li-normal">type: list</span> <span class="li-normal">choices: [name, model, serial-number]</span> 
 <a id='label398' href="javascript:ContentClick('label399', 'label398');" onmouseover="ContentPreview('label399');" onmouseout="ContentUnpreview('label399');" title="click to collapse or expand..."> more... </a>
 <div id="label399" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ips_sensor</span> <b>(Alias name: ips-sensor)</b>  Ips sensor name. <span class="li-normal">type: str</span>
 <a id='label400' href="javascript:ContentClick('label401', 'label400');" onmouseover="ContentPreview('label401');" onmouseout="ContentUnpreview('label401');" title="click to collapse or expand..."> more... </a>
 <div id="label401" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">l3_roaming</span> <b>(Alias name: l3-roaming)</b>  Enable/disable layer 3 roaming (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label402' href="javascript:ContentClick('label403', 'label402');" onmouseover="ContentPreview('label403');" onmouseout="ContentUnpreview('label403');" title="click to collapse or expand..."> more... </a>
 <div id="label403" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone_dns</span> <b>(Alias name: local-standalone-dns)</b>  Enable/disable ap local standalone dns. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label404' href="javascript:ContentClick('label405', 'label404');" onmouseover="ContentPreview('label405');" onmouseout="ContentUnpreview('label405');" title="click to collapse or expand..."> more... </a>
 <div id="label405" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone_dns_ip</span> <b>(Alias name: local-standalone-dns-ip)</b>  Ipv4 addresses for the local standalone dns. <span class="li-normal">type: list</span>
 <a id='label406' href="javascript:ContentClick('label407', 'label406');" onmouseover="ContentPreview('label407');" onmouseout="ContentUnpreview('label407');" title="click to collapse or expand..."> more... </a>
 <div id="label407" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">osen</span> Enable/disable osen as part of key management (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label408' href="javascript:ContentClick('label409', 'label408');" onmouseover="ContentPreview('label409');" onmouseout="ContentUnpreview('label409');" title="click to collapse or expand..."> more... </a>
 <div id="label409" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_mpsk_auth</span> <b>(Alias name: radius-mac-mpsk-auth)</b>  Enable/disable radius-based mac authentication of clients for mpsk authentication (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label410' href="javascript:ContentClick('label411', 'label410');" onmouseover="ContentPreview('label411');" onmouseout="ContentUnpreview('label411');" title="click to collapse or expand..."> more... </a>
 <div id="label411" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_mpsk_timeout</span> <b>(Alias name: radius-mac-mpsk-timeout)</b>  Radius mac mpsk cache timeout interval (1800 - 864000, default = 86400). <span class="li-normal">type: int</span>
 <a id='label412' href="javascript:ContentClick('label413', 'label412');" onmouseover="ContentPreview('label413');" onmouseout="ContentUnpreview('label413');" title="click to collapse or expand..."> more... </a>
 <div id="label413" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ax_ss12</span> <b>(Alias name: rates-11ax-ss12)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/1, mcs9/1, mcs10/1, mcs11/1, mcs0/2, mcs1/2, mcs2/2, mcs3/2, mcs4/2, mcs5/2, mcs6/2, mcs7/2, mcs8/2, mcs9/2, mcs10/2, mcs11/2]</span> 
 <a id='label414' href="javascript:ContentClick('label415', 'label414');" onmouseover="ContentPreview('label415');" onmouseout="ContentUnpreview('label415');" title="click to collapse or expand..."> more... </a>
 <div id="label415" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ax_ss34</span> <b>(Alias name: rates-11ax-ss34)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/3, mcs1/3, mcs2/3, mcs3/3, mcs4/3, mcs5/3, mcs6/3, mcs7/3, mcs8/3, mcs9/3, mcs10/3, mcs11/3, mcs0/4, mcs1/4, mcs2/4, mcs3/4, mcs4/4, mcs5/4, mcs6/4, mcs7/4, mcs8/4, mcs9/4, mcs10/4, mcs11/4]</span> 
 <a id='label416' href="javascript:ContentClick('label417', 'label416');" onmouseover="ContentPreview('label417');" onmouseout="ContentUnpreview('label417');" title="click to collapse or expand..."> more... </a>
 <div id="label417" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">scan_botnet_connections</span> <b>(Alias name: scan-botnet-connections)</b>  Block or monitor connections to botnet servers or disable botnet scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label418' href="javascript:ContentClick('label419', 'label418');" onmouseover="ContentPreview('label419');" onmouseout="ContentUnpreview('label419');" title="click to collapse or expand..."> more... </a>
 <div id="label419" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">utm_log</span> <b>(Alias name: utm-log)</b>  Enable/disable utm logging. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label420' href="javascript:ContentClick('label421', 'label420');" onmouseover="ContentPreview('label421');" onmouseout="ContentUnpreview('label421');" title="click to collapse or expand..."> more... </a>
 <div id="label421" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">utm_status</span> <b>(Alias name: utm-status)</b>  Enable to add one or more security profiles (av, ips, etc. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label422' href="javascript:ContentClick('label423', 'label422');" onmouseover="ContentPreview('label423');" onmouseout="ContentUnpreview('label423');" title="click to collapse or expand..."> more... </a>
 <div id="label423" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_profile</span> <b>(Alias name: webfilter-profile)</b>  Webfilter profile name. <span class="li-normal">type: str</span>
 <a id='label424' href="javascript:ContentClick('label425', 'label424');" onmouseover="ContentPreview('label425');" onmouseout="ContentUnpreview('label425');" title="click to collapse or expand..."> more... </a>
 <div id="label425" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_h2e_only</span> <b>(Alias name: sae-h2e-only)</b>  Use hash-to-element-only mechanism for pwe derivation (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label426' href="javascript:ContentClick('label427', 'label426');" onmouseover="ContentPreview('label427');" onmouseout="ContentUnpreview('label427');" title="click to collapse or expand..."> more... </a>
 <div id="label427" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_pk</span> <b>(Alias name: sae-pk)</b>  Enable/disable wpa3 sae-pk (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label428' href="javascript:ContentClick('label429', 'label428');" onmouseover="ContentPreview('label429');" onmouseout="ContentUnpreview('label429');" title="click to collapse or expand..."> more... </a>
 <div id="label429" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_private_key</span> <b>(Alias name: sae-private-key)</b>  Private key used for wpa3 sae-pk authentication. <span class="li-normal">type: str</span>
 <a id='label430' href="javascript:ContentClick('label431', 'label430');" onmouseover="ContentPreview('label431');" onmouseout="ContentUnpreview('label431');" title="click to collapse or expand..."> more... </a>
 <div id="label431" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_threshold_6g</span> <b>(Alias name: sticky-client-threshold-6g)</b>  Minimum signal level/threshold in dbm required for the 6g client to be serviced by the ap (-95 to -20, default = -76). <span class="li-normal">type: str</span>
 <a id='label432' href="javascript:ContentClick('label433', 'label432');" onmouseover="ContentPreview('label433');" onmouseout="ContentUnpreview('label433');" title="click to collapse or expand..."> more... </a>
 <div id="label433" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_dscp_marking</span> <b>(Alias name: application-dscp-marking)</b>  Enable/disable application attribute based dscp marking (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label434' href="javascript:ContentClick('label435', 'label434');" onmouseover="ContentPreview('label435');" onmouseout="ContentUnpreview('label435');" title="click to collapse or expand..."> more... </a>
 <div id="label435" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">l3_roaming_mode</span> <b>(Alias name: l3-roaming-mode)</b>  Select the way that layer 3 roaming traffic is passed (default = direct). <span class="li-normal">type: str</span> <span class="li-normal">choices: [direct, indirect]</span> 
 <a id='label436' href="javascript:ContentClick('label437', 'label436');" onmouseover="ContentPreview('label437');" onmouseout="ContentUnpreview('label437');" title="click to collapse or expand..."> more... </a>
 <div id="label437" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ac_mcs_map</span> <b>(Alias name: rates-11ac-mcs-map)</b>  Comma separated list of max supported vht mcs for spatial streams 1 through 8. <span class="li-normal">type: str</span>
 <a id='label438' href="javascript:ContentClick('label439', 'label438');" onmouseover="ContentPreview('label439');" onmouseout="ContentUnpreview('label439');" title="click to collapse or expand..."> more... </a>
 <div id="label439" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ax_mcs_map</span> <b>(Alias name: rates-11ax-mcs-map)</b>  Comma separated list of max supported he mcs for spatial streams 1 through 8. <span class="li-normal">type: str</span>
 <a id='label440' href="javascript:ContentClick('label441', 'label440');" onmouseover="ContentPreview('label441');" onmouseout="ContentUnpreview('label441');" title="click to collapse or expand..."> more... </a>
 <div id="label441" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_fw_accounting</span> <b>(Alias name: captive-portal-fw-accounting)</b>  Enable/disable radius accounting for captive portal firewall authentication session. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label442' href="javascript:ContentClick('label443', 'label442');" onmouseover="ContentPreview('label443');" onmouseout="ContentUnpreview('label443');" title="click to collapse or expand..."> more... </a>
 <div id="label443" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth_block_interval</span> <b>(Alias name: radius-mac-auth-block-interval)</b>  Dont send radius mac auth request again if the client has been rejected within specific interval (0 or 30 - 864000 seconds, default = 0, 0 to disable blocking). <span class="li-normal">type: int</span>
 <a id='label444' href="javascript:ContentClick('label445', 'label444');" onmouseover="ContentPreview('label445');" onmouseout="ContentUnpreview('label445');" title="click to collapse or expand..."> more... </a>
 <div id="label445" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_is_factory_setting</span> Is factory setting. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, ext]</span>  <span class="li-normal">default: disable</span> 
 <a id='label446' href="javascript:ContentClick('label447', 'label446');" onmouseover="ContentPreview('label447');" onmouseout="ContentUnpreview('label447');" title="click to collapse or expand..."> more... </a>
 <div id="label447" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">d80211k</span> <b>(Alias name: 80211k)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label448' href="javascript:ContentClick('label449', 'label448');" onmouseover="ContentPreview('label449');" onmouseout="ContentUnpreview('label449');" title="click to collapse or expand..."> more... </a>
 <div id="label449" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">d80211v</span> <b>(Alias name: 80211v)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label450' href="javascript:ContentClick('label451', 'label450');" onmouseover="ContentPreview('label451');" onmouseout="ContentUnpreview('label451');" title="click to collapse or expand..."> more... </a>
 <div id="label451" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">roaming_acct_interim_update</span> <b>(Alias name: roaming-acct-interim-update)</b>  Enable/disable using accounting interim update instead of accounting start/stop on roaming for wpa-enterprise security. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label452' href="javascript:ContentClick('label453', 'label452');" onmouseover="ContentPreview('label453');" onmouseout="ContentUnpreview('label453');" title="click to collapse or expand..."> more... </a>
 <div id="label453" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_hnp_only</span> <b>(Alias name: sae-hnp-only)</b>  Use hunting-and-pecking-only mechanism for pwe derivation (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label454' href="javascript:ContentClick('label455', 'label454');" onmouseover="ContentPreview('label455');" onmouseout="ContentUnpreview('label455');" title="click to collapse or expand..."> more... </a>
 <div id="label455" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">akm24_only</span> <b>(Alias name: akm24-only)</b>  Wpa3 sae using group-dependent hash only (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label456' href="javascript:ContentClick('label457', 'label456');" onmouseover="ContentPreview('label457');" onmouseout="ContentUnpreview('label457');" title="click to collapse or expand..."> more... </a>
 <div id="label457" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">beacon_protection</span> <b>(Alias name: beacon-protection)</b>  Enable/disable beacon protection support (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label458' href="javascript:ContentClick('label459', 'label458');" onmouseover="ContentPreview('label459');" onmouseout="ContentUnpreview('label459');" title="click to collapse or expand..."> more... </a>
 <div id="label459" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal</span> <b>(Alias name: captive-portal)</b>  Enable/disable captive portal. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label460' href="javascript:ContentClick('label461', 'label460');" onmouseover="ContentPreview('label461');" onmouseout="ContentUnpreview('label461');" title="click to collapse or expand..."> more... </a>
 <div id="label461" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nas_filter_rule</span> <b>(Alias name: nas-filter-rule)</b>  Enable/disable nas filter rule support (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label462' href="javascript:ContentClick('label463', 'label462');" onmouseover="ContentPreview('label463');" onmouseout="ContentUnpreview('label463');" title="click to collapse or expand..."> more... </a>
 <div id="label463" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11be_mcs_map</span> <b>(Alias name: rates-11be-mcs-map)</b>  Comma separated list of max nss that supports eht-mcs 0-9, 10-11, 12-13 for 20mhz/40mhz/80mhz bandwidth. <span class="li-normal">type: str</span>
 <a id='label464' href="javascript:ContentClick('label465', 'label464');" onmouseover="ContentPreview('label465');" onmouseout="ContentUnpreview('label465');" title="click to collapse or expand..."> more... </a>
 <div id="label465" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11be_mcs_map_160</span> <b>(Alias name: rates-11be-mcs-map-160)</b>  Comma separated list of max nss that supports eht-mcs 0-9, 10-11, 12-13 for 160mhz bandwidth. <span class="li-normal">type: str</span>
 <a id='label466' href="javascript:ContentClick('label467', 'label466');" onmouseover="ContentPreview('label467');" onmouseout="ContentUnpreview('label467');" title="click to collapse or expand..."> more... </a>
 <div id="label467" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11be_mcs_map_320</span> <b>(Alias name: rates-11be-mcs-map-320)</b>  Comma separated list of max nss that supports eht-mcs 0-9, 10-11, 12-13 for 320mhz bandwidth. <span class="li-normal">type: str</span>
 <a id='label468' href="javascript:ContentClick('label469', 'label468');" onmouseover="ContentPreview('label469');" onmouseout="ContentUnpreview('label469');" title="click to collapse or expand..."> more... </a>
 <div id="label469" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip_managed_by_fortiipam</span> <b>(Alias name: _intf_ip-managed-by-fortiipam)</b>  Intf ip managed by fortiipam. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, inherit-global]</span> 
 <a id='label470' href="javascript:ContentClick('label471', 'label470');" onmouseover="ContentPreview('label471');" onmouseout="ContentUnpreview('label471');" title="click to collapse or expand..."> more... </a>
 <div id="label471" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_managed_subnetwork_size</span> <b>(Alias name: _intf_managed-subnetwork-size)</b>  Intf managed subnetwork size. <span class="li-normal">type: str</span> <span class="li-normal">choices: [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]</span>  <span class="li-normal">default: 256</span> 
 <a id='label472' href="javascript:ContentClick('label473', 'label472');" onmouseover="ContentPreview('label473');" onmouseout="ContentUnpreview('label473');" title="click to collapse or expand..."> more... </a>
 <div id="label473" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">domain_name_stripping</span> <b>(Alias name: domain-name-stripping)</b>  Enable/disable stripping domain name from identity (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label474' href="javascript:ContentClick('label475', 'label474');" onmouseover="ContentPreview('label475');" onmouseout="ContentUnpreview('label475');" title="click to collapse or expand..."> more... </a>
 <div id="label475" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_lan_partition</span> <b>(Alias name: local-lan-partition)</b>  Enable/disable segregating client traffic to local lan side (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label476' href="javascript:ContentClick('label477', 'label476');" onmouseover="ContentPreview('label477');" onmouseout="ContentUnpreview('label477');" title="click to collapse or expand..."> more... </a>
 <div id="label477" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_role</span> Intf role. <span class="li-normal">type: str</span> <span class="li-normal">choices: [lan, wan, dmz, undefined]</span>  <span class="li-normal">default: lan</span> 
 <a id='label478' href="javascript:ContentClick('label479', 'label478');" onmouseover="ContentPreview('label479');" onmouseout="ContentUnpreview('label479');" title="click to collapse or expand..."> more... </a>
 <div id="label479" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.6 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">called_station_id_type</span> <b>(Alias name: called-station-id-type)</b>  The format type of radius attribute called-station-id (default = mac). <span class="li-normal">type: str</span> <span class="li-normal">choices: [mac, ip, apname]</span> 
 <a id='label480' href="javascript:ContentClick('label481', 'label480');" onmouseover="ContentPreview('label481');" onmouseout="ContentUnpreview('label481');" title="click to collapse or expand..."> more... </a>
 <div id="label481" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_pre_auth</span> <b>(Alias name: external-pre-auth)</b>  Enable/disable pre-authentication with external aps not managed by the fortigate (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label482' href="javascript:ContentClick('label483', 'label482');" onmouseover="ContentPreview('label483');" onmouseout="ContentUnpreview('label483');" title="click to collapse or expand..."> more... </a>
 <div id="label483" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pre_auth</span> <b>(Alias name: pre-auth)</b>  Enable/disable pre-authentication, where supported by clients (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label484' href="javascript:ContentClick('label485', 'label484');" onmouseover="ContentPreview('label485');" onmouseout="ContentUnpreview('label485');" title="click to collapse or expand..."> more... </a>
 <div id="label485" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip6_send_adv</span> <b>(Alias name: _intf_ip6-send-adv)</b>  Intf ip6 send adv. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label486' href="javascript:ContentClick('label487', 'label486');" onmouseover="ContentPreview('label487');" onmouseout="ContentUnpreview('label487');" title="click to collapse or expand..."> more... </a>
 <div id="label487" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_prefix_list</span> <b>(Alias name: ip6-prefix-list)</b>  Ip6 prefix list. <span class="li-normal">type: list</span>
 <a id='label488' href="javascript:ContentClick('label489', 'label488');" onmouseover="ContentPreview('label489');" onmouseout="ContentUnpreview('label489');" title="click to collapse or expand..."> more... </a>
 <div id="label489" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous_flag</span> <b>(Alias name: autonomous-flag)</b>  Autonomous flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label490' href="javascript:ContentClick('label491', 'label490');" onmouseover="ContentPreview('label491');" onmouseout="ContentUnpreview('label491');" title="click to collapse or expand..."> more... </a>
 <div id="label491" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dnssl</span> Dnssl. <span class="li-normal">type: list</span>
 <a id='label492' href="javascript:ContentClick('label493', 'label492');" onmouseover="ContentPreview('label493');" onmouseout="ContentUnpreview('label493');" title="click to collapse or expand..."> more... </a>
 <div id="label493" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">onlink_flag</span> <b>(Alias name: onlink-flag)</b>  Onlink flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label494' href="javascript:ContentClick('label495', 'label494');" onmouseover="ContentPreview('label495');" onmouseout="ContentUnpreview('label495');" title="click to collapse or expand..."> more... </a>
 <div id="label495" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">preferred_life_time</span> <b>(Alias name: preferred-life-time)</b>  Preferred life time. <span class="li-normal">type: int</span>
 <a id='label496' href="javascript:ContentClick('label497', 'label496');" onmouseover="ContentPreview('label497');" onmouseout="ContentUnpreview('label497');" title="click to collapse or expand..."> more... </a>
 <div id="label497" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">prefix</span> Prefix. <span class="li-normal">type: str</span>
 <a id='label498' href="javascript:ContentClick('label499', 'label498');" onmouseover="ContentPreview('label499');" onmouseout="ContentUnpreview('label499');" title="click to collapse or expand..."> more... </a>
 <div id="label499" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> Rdnss. <span class="li-normal">type: list</span>
 <a id='label500' href="javascript:ContentClick('label501', 'label500');" onmouseover="ContentPreview('label501');" onmouseout="ContentUnpreview('label501');" title="click to collapse or expand..."> more... </a>
 <div id="label501" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">valid_life_time</span> <b>(Alias name: valid-life-time)</b>  Valid life time. <span class="li-normal">type: int</span>
 <a id='label502' href="javascript:ContentClick('label503', 'label502');" onmouseover="ContentPreview('label503');" onmouseout="ContentUnpreview('label503');" title="click to collapse or expand..."> more... </a>
 <div id="label503" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">_intf_vrf</span> Intf vrf. <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label504' href="javascript:ContentClick('label505', 'label504');" onmouseover="ContentPreview('label505');" onmouseout="ContentUnpreview('label505');" title="click to collapse or expand..."> more... </a>
 <div id="label505" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">eap_reauth</span> <b>(Alias name: eap-reauth)</b>  Enable/disable eap re-authentication for wpa-enterprise security. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label506' href="javascript:ContentClick('label507', 'label506');" onmouseover="ContentPreview('label507');" onmouseout="ContentUnpreview('label507');" title="click to collapse or expand..."> more... </a>
 <div id="label507" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eap_reauth_intv</span> <b>(Alias name: eap-reauth-intv)</b>  Eap re-authentication interval (1800 - 864000 sec, default = 86400). <span class="li-normal">type: int</span>
 <a id='label508' href="javascript:ContentClick('label509', 'label508');" onmouseover="ContentPreview('label509');" onmouseout="ContentUnpreview('label509');" title="click to collapse or expand..."> more... </a>
 <div id="label509" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">eapol_key_retries</span> <b>(Alias name: eapol-key-retries)</b>  Enable/disable retransmission of eapol-key frames (message 3/4 and group message 1/2) (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label510' href="javascript:ContentClick('label511', 'label510');" onmouseover="ContentPreview('label511');" onmouseout="ContentUnpreview('label511');" title="click to collapse or expand..."> more... </a>
 <div id="label511" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">encrypt</span> Encryption protocol to use (only available when security is set to a wpa type). <span class="li-normal">type: str</span> <span class="li-normal">choices: [TKIP, AES, TKIP-AES]</span> 
 <a id='label512' href="javascript:ContentClick('label513', 'label512');" onmouseover="ContentPreview('label513');" onmouseout="ContentUnpreview('label513');" title="click to collapse or expand..."> more... </a>
 <div id="label513" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_fast_roaming</span> <b>(Alias name: external-fast-roaming)</b>  Enable/disable fast roaming or pre-authentication with external aps not managed by the fortigate (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label514' href="javascript:ContentClick('label515', 'label514');" onmouseover="ContentPreview('label515');" onmouseout="ContentUnpreview('label515');" title="click to collapse or expand..."> more... </a>
 <div id="label515" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_logout</span> <b>(Alias name: external-logout)</b>  Url of external authentication logout server. <span class="li-normal">type: str</span>
 <a id='label516' href="javascript:ContentClick('label517', 'label516');" onmouseover="ContentPreview('label517');" onmouseout="ContentUnpreview('label517');" title="click to collapse or expand..."> more... </a>
 <div id="label517" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_web</span> <b>(Alias name: external-web)</b>  Url of external authentication web server. <span class="li-normal">type: str</span>
 <a id='label518' href="javascript:ContentClick('label519', 'label518');" onmouseover="ContentPreview('label519');" onmouseout="ContentUnpreview('label519');" title="click to collapse or expand..."> more... </a>
 <div id="label519" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fast_bss_transition</span> <b>(Alias name: fast-bss-transition)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label520' href="javascript:ContentClick('label521', 'label520');" onmouseover="ContentPreview('label521');" onmouseout="ContentUnpreview('label521');" title="click to collapse or expand..."> more... </a>
 <div id="label521" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fast_roaming</span> <b>(Alias name: fast-roaming)</b>  Enable/disable fast-roaming, or pre-authentication, where supported by clients (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label522' href="javascript:ContentClick('label523', 'label522');" onmouseover="ContentPreview('label523');" onmouseout="ContentUnpreview('label523');" title="click to collapse or expand..."> more... </a>
 <div id="label523" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ft_mobility_domain</span> <b>(Alias name: ft-mobility-domain)</b>  Mobility domain identifier in ft (1 - 65535, default = 1000). <span class="li-normal">type: int</span>
 <a id='label524' href="javascript:ContentClick('label525', 'label524');" onmouseover="ContentPreview('label525');" onmouseout="ContentUnpreview('label525');" title="click to collapse or expand..."> more... </a>
 <div id="label525" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ft_over_ds</span> <b>(Alias name: ft-over-ds)</b>  Enable/disable ft over the distribution system (ds). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label526' href="javascript:ContentClick('label527', 'label526');" onmouseover="ContentPreview('label527');" onmouseout="ContentUnpreview('label527');" title="click to collapse or expand..."> more... </a>
 <div id="label527" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ft_r0_key_lifetime</span> <b>(Alias name: ft-r0-key-lifetime)</b>  Lifetime of the pmk-r0 key in ft, 1-65535 minutes. <span class="li-normal">type: int</span>
 <a id='label528' href="javascript:ContentClick('label529', 'label528');" onmouseover="ContentPreview('label529');" onmouseout="ContentUnpreview('label529');" title="click to collapse or expand..."> more... </a>
 <div id="label529" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gtk_rekey</span> <b>(Alias name: gtk-rekey)</b>  Enable/disable gtk rekey for wpa security. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label530' href="javascript:ContentClick('label531', 'label530');" onmouseover="ContentPreview('label531');" onmouseout="ContentUnpreview('label531');" title="click to collapse or expand..."> more... </a>
 <div id="label531" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gtk_rekey_intv</span> <b>(Alias name: gtk-rekey-intv)</b>  Gtk rekey interval (1800 - 864000 sec, default = 86400). <span class="li-normal">type: int</span>
 <a id='label532' href="javascript:ContentClick('label533', 'label532');" onmouseover="ContentPreview('label533');" onmouseout="ContentUnpreview('label533');" title="click to collapse or expand..."> more... </a>
 <div id="label533" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hotspot20_profile</span> <b>(Alias name: hotspot20-profile)</b>  Hotspot 2. <span class="li-normal">type: str</span>
 <a id='label534' href="javascript:ContentClick('label535', 'label534');" onmouseover="ContentPreview('label535');" onmouseout="ContentUnpreview('label535');" title="click to collapse or expand..."> more... </a>
 <div id="label535" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">intra_vap_privacy</span> <b>(Alias name: intra-vap-privacy)</b>  Enable/disable blocking communication between clients on the same ssid (called intra-ssid privacy) (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label536' href="javascript:ContentClick('label537', 'label536');" onmouseover="ContentPreview('label537');" onmouseout="ContentUnpreview('label537');" title="click to collapse or expand..."> more... </a>
 <div id="label537" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ip address and subnet mask for the local standalone nat subnet. <span class="li-normal">type: str</span>
 <a id='label538' href="javascript:ContentClick('label539', 'label538');" onmouseover="ContentPreview('label539');" onmouseout="ContentUnpreview('label539');" title="click to collapse or expand..."> more... </a>
 <div id="label539" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">key</span> Wep key. <span class="li-normal">type: list</span>
 <a id='label540' href="javascript:ContentClick('label541', 'label540');" onmouseover="ContentPreview('label541');" onmouseout="ContentUnpreview('label541');" title="click to collapse or expand..."> more... </a>
 <div id="label541" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">keyindex</span> Wep key index (1 - 4). <span class="li-normal">type: int</span>
 <a id='label542' href="javascript:ContentClick('label543', 'label542');" onmouseover="ContentPreview('label543');" onmouseout="ContentUnpreview('label543');" title="click to collapse or expand..."> more... </a>
 <div id="label543" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldpc</span> Vap low-density parity-check (ldpc) coding configuration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, tx, rx, rxtx]</span> 
 <a id='label544' href="javascript:ContentClick('label545', 'label544');" onmouseover="ContentPreview('label545');" onmouseout="ContentUnpreview('label545');" title="click to collapse or expand..."> more... </a>
 <div id="label545" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_authentication</span> <b>(Alias name: local-authentication)</b>  Enable/disable ap local authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label546' href="javascript:ContentClick('label547', 'label546');" onmouseover="ContentPreview('label547');" onmouseout="ContentUnpreview('label547');" title="click to collapse or expand..."> more... </a>
 <div id="label547" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_bridging</span> <b>(Alias name: local-bridging)</b>  Enable/disable bridging of wireless and ethernet interfaces on the fortiap (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label548' href="javascript:ContentClick('label549', 'label548');" onmouseover="ContentPreview('label549');" onmouseout="ContentUnpreview('label549');" title="click to collapse or expand..."> more... </a>
 <div id="label549" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_lan</span> <b>(Alias name: local-lan)</b>  Allow/deny traffic destined for a class a, b, or c private ip address (default = allow). <span class="li-normal">type: str</span> <span class="li-normal">choices: [deny, allow]</span> 
 <a id='label550' href="javascript:ContentClick('label551', 'label550');" onmouseover="ContentPreview('label551');" onmouseout="ContentUnpreview('label551');" title="click to collapse or expand..."> more... </a>
 <div id="label551" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone</span> <b>(Alias name: local-standalone)</b>  Enable/disable ap local standalone (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label552' href="javascript:ContentClick('label553', 'label552');" onmouseover="ContentPreview('label553');" onmouseout="ContentUnpreview('label553');" title="click to collapse or expand..."> more... </a>
 <div id="label553" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone_nat</span> <b>(Alias name: local-standalone-nat)</b>  Enable/disable ap local standalone nat mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label554' href="javascript:ContentClick('label555', 'label554');" onmouseover="ContentPreview('label555');" onmouseout="ContentUnpreview('label555');" title="click to collapse or expand..."> more... </a>
 <div id="label555" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_auth_bypass</span> <b>(Alias name: mac-auth-bypass)</b>  Enable/disable mac authentication bypass. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label556' href="javascript:ContentClick('label557', 'label556');" onmouseover="ContentPreview('label557');" onmouseout="ContentUnpreview('label557');" title="click to collapse or expand..."> more... </a>
 <div id="label557" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_filter</span> <b>(Alias name: mac-filter)</b>  Enable/disable mac filtering to block wireless clients by mac address. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label558' href="javascript:ContentClick('label559', 'label558');" onmouseover="ContentPreview('label559');" onmouseout="ContentUnpreview('label559');" title="click to collapse or expand..."> more... </a>
 <div id="label559" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_filter_list</span> <b>(Alias name: mac-filter-list)</b>  Mac filter list. <span class="li-normal">type: list</span>
 <a id='label560' href="javascript:ContentClick('label561', 'label560');" onmouseover="ContentPreview('label561');" onmouseout="ContentUnpreview('label561');" title="click to collapse or expand..."> more... </a>
 <div id="label561" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label562' href="javascript:ContentClick('label563', 'label562');" onmouseover="ContentPreview('label563');" onmouseout="ContentUnpreview('label563');" title="click to collapse or expand..."> more... </a>
 <div id="label563" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac</span> Mac address. <span class="li-normal">type: str</span>
 <a id='label564' href="javascript:ContentClick('label565', 'label564');" onmouseover="ContentPreview('label565');" onmouseout="ContentUnpreview('label565');" title="click to collapse or expand..."> more... </a>
 <div id="label565" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_filter_policy</span> <b>(Alias name: mac-filter-policy)</b>  Deny or allow the client with this mac address. <span class="li-normal">type: str</span> <span class="li-normal">choices: [deny, allow]</span> 
 <a id='label566' href="javascript:ContentClick('label567', 'label566');" onmouseover="ContentPreview('label567');" onmouseout="ContentUnpreview('label567');" title="click to collapse or expand..."> more... </a>
 <div id="label567" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">mac_filter_policy_other</span> <b>(Alias name: mac-filter-policy-other)</b>  Allow or block clients with mac addresses that are not in the filter list. <span class="li-normal">type: str</span> <span class="li-normal">choices: [deny, allow]</span> 
 <a id='label568' href="javascript:ContentClick('label569', 'label568');" onmouseover="ContentPreview('label569');" onmouseout="ContentUnpreview('label569');" title="click to collapse or expand..."> more... </a>
 <div id="label569" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_clients</span> <b>(Alias name: max-clients)</b>  Maximum number of clients that can connect simultaneously to the vap (default = 0, meaning no limitation). <span class="li-normal">type: int</span>
 <a id='label570' href="javascript:ContentClick('label571', 'label570');" onmouseover="ContentPreview('label571');" onmouseout="ContentUnpreview('label571');" title="click to collapse or expand..."> more... </a>
 <div id="label571" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_clients_ap</span> <b>(Alias name: max-clients-ap)</b>  Maximum number of clients that can connect simultaneously to each radio (default = 0, meaning no limitation). <span class="li-normal">type: int</span>
 <a id='label572' href="javascript:ContentClick('label573', 'label572');" onmouseover="ContentPreview('label573');" onmouseout="ContentUnpreview('label573');" title="click to collapse or expand..."> more... </a>
 <div id="label573" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">me_disable_thresh</span> <b>(Alias name: me-disable-thresh)</b>  Disable multicast enhancement when this many clients are receiving multicast traffic. <span class="li-normal">type: int</span>
 <a id='label574' href="javascript:ContentClick('label575', 'label574');" onmouseover="ContentPreview('label575');" onmouseout="ContentUnpreview('label575');" title="click to collapse or expand..."> more... </a>
 <div id="label575" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mesh_backhaul</span> <b>(Alias name: mesh-backhaul)</b>  Enable/disable using this vap as a wifi mesh backhaul (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label576' href="javascript:ContentClick('label577', 'label576');" onmouseover="ContentPreview('label577');" onmouseout="ContentUnpreview('label577');" title="click to collapse or expand..."> more... </a>
 <div id="label577" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk</span> Enable/disable multiple pre-shared keys (psks. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label578' href="javascript:ContentClick('label579', 'label578');" onmouseover="ContentPreview('label579');" onmouseout="ContentUnpreview('label579');" title="click to collapse or expand..."> more... </a>
 <div id="label579" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk_concurrent_clients</span> <b>(Alias name: mpsk-concurrent-clients)</b>  Number of pre-shared keys (psks) to allow if multiple pre-shared keys are enabled. <span class="li-normal">type: int</span>
 <a id='label580' href="javascript:ContentClick('label581', 'label580');" onmouseover="ContentPreview('label581');" onmouseout="ContentUnpreview('label581');" title="click to collapse or expand..."> more... </a>
 <div id="label581" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk_key</span> <b>(Alias name: mpsk-key)</b>  Mpsk key. <span class="li-normal">type: list</span>
 <a id='label582' href="javascript:ContentClick('label583', 'label582');" onmouseover="ContentPreview('label583');" onmouseout="ContentUnpreview('label583');" title="click to collapse or expand..."> more... </a>
 <div id="label583" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">comment</span> Comment. <span class="li-normal">type: str</span>
 <a id='label584' href="javascript:ContentClick('label585', 'label584');" onmouseover="ContentPreview('label585');" onmouseout="ContentUnpreview('label585');" title="click to collapse or expand..."> more... </a>
 <div id="label585" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">concurrent_clients</span> <b>(Alias name: concurrent-clients)</b>  Number of clients that can connect using this pre-shared key. <span class="li-normal">type: str</span>
 <a id='label586' href="javascript:ContentClick('label587', 'label586');" onmouseover="ContentPreview('label587');" onmouseout="ContentUnpreview('label587');" title="click to collapse or expand..."> more... </a>
 <div id="label587" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">key_name</span> <b>(Alias name: key-name)</b>  Pre-shared key name. <span class="li-normal">type: str</span>
 <a id='label588' href="javascript:ContentClick('label589', 'label588');" onmouseover="ContentPreview('label589');" onmouseout="ContentUnpreview('label589');" title="click to collapse or expand..."> more... </a>
 <div id="label589" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">passphrase</span> Wpa pre-shared key. <span class="li-normal">type: list</span>
 <a id='label590' href="javascript:ContentClick('label591', 'label590');" onmouseover="ContentPreview('label591');" onmouseout="ContentUnpreview('label591');" title="click to collapse or expand..."> more... </a>
 <div id="label591" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk_schedules</span> <b>(Alias name: mpsk-schedules)</b>  Firewall schedule for mpsk passphrase. <span class="li-normal">type: list or str</span>
 <a id='label592' href="javascript:ContentClick('label593', 'label592');" onmouseover="ContentPreview('label593');" onmouseout="ContentUnpreview('label593');" title="click to collapse or expand..."> more... </a>
 <div id="label593" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">multicast_enhance</span> <b>(Alias name: multicast-enhance)</b>  Enable/disable converting multicast to unicast to improve performance (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label594' href="javascript:ContentClick('label595', 'label594');" onmouseover="ContentPreview('label595');" onmouseout="ContentUnpreview('label595');" title="click to collapse or expand..."> more... </a>
 <div id="label595" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">multicast_rate</span> <b>(Alias name: multicast-rate)</b>  Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0). <span class="li-normal">type: str</span> <span class="li-normal">choices: [0, 6000, 12000, 24000]</span> 
 <a id='label596' href="javascript:ContentClick('label597', 'label596');" onmouseover="ContentPreview('label597');" onmouseout="ContentUnpreview('label597');" title="click to collapse or expand..."> more... </a>
 <div id="label597" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Virtual ap name. <span class="li-normal">type: str</span>
 <a id='label598' href="javascript:ContentClick('label599', 'label598');" onmouseover="ContentPreview('label599');" onmouseout="ContentUnpreview('label599');" title="click to collapse or expand..."> more... </a>
 <div id="label599" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">okc</span> Enable/disable opportunistic key caching (okc) (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label600' href="javascript:ContentClick('label601', 'label600');" onmouseover="ContentPreview('label601');" onmouseout="ContentUnpreview('label601');" title="click to collapse or expand..."> more... </a>
 <div id="label601" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">passphrase</span> Wpa pre-shard key (psk) to be used to authenticate wifi users. <span class="li-normal">type: list</span>
 <a id='label602' href="javascript:ContentClick('label603', 'label602');" onmouseover="ContentPreview('label603');" onmouseout="ContentUnpreview('label603');" title="click to collapse or expand..."> more... </a>
 <div id="label603" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pmf</span> Protected management frames (pmf) support (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, optional]</span> 
 <a id='label604' href="javascript:ContentClick('label605', 'label604');" onmouseover="ContentPreview('label605');" onmouseout="ContentUnpreview('label605');" title="click to collapse or expand..."> more... </a>
 <div id="label605" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pmf_assoc_comeback_timeout</span> <b>(Alias name: pmf-assoc-comeback-timeout)</b>  Protected management frames (pmf) comeback maximum timeout (1-20 sec). <span class="li-normal">type: int</span>
 <a id='label606' href="javascript:ContentClick('label607', 'label606');" onmouseover="ContentPreview('label607');" onmouseout="ContentUnpreview('label607');" title="click to collapse or expand..."> more... </a>
 <div id="label607" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pmf_sa_query_retry_timeout</span> <b>(Alias name: pmf-sa-query-retry-timeout)</b>  Protected management frames (pmf) sa query retry timeout interval (1 - 5 100s of msec). <span class="li-normal">type: int</span>
 <a id='label608' href="javascript:ContentClick('label609', 'label608');" onmouseover="ContentPreview('label609');" onmouseout="ContentUnpreview('label609');" title="click to collapse or expand..."> more... </a>
 <div id="label609" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">portal_message_override_group</span> <b>(Alias name: portal-message-override-group)</b>  Replacement message group for this vap (only available when security is set to a captive portal type). <span class="li-normal">type: str</span>
 <a id='label610' href="javascript:ContentClick('label611', 'label610');" onmouseover="ContentPreview('label611');" onmouseout="ContentUnpreview('label611');" title="click to collapse or expand..."> more... </a>
 <div id="label611" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">portal_type</span> <b>(Alias name: portal-type)</b>  Captive portal functionality. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auth, auth+disclaimer, disclaimer, email-collect, cmcc, cmcc-macauth, auth-mac, external-auth, external-macauth]</span> 
 <a id='label612' href="javascript:ContentClick('label613', 'label612');" onmouseover="ContentPreview('label613');" onmouseout="ContentUnpreview('label613');" title="click to collapse or expand..."> more... </a>
 <div id="label613" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">probe_resp_suppression</span> <b>(Alias name: probe-resp-suppression)</b>  Enable/disable probe response suppression (to ignore weak signals) (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label614' href="javascript:ContentClick('label615', 'label614');" onmouseover="ContentPreview('label615');" onmouseout="ContentUnpreview('label615');" title="click to collapse or expand..."> more... </a>
 <div id="label615" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">probe_resp_threshold</span> <b>(Alias name: probe-resp-threshold)</b>  Minimum signal level/threshold in dbm required for the ap response to probe requests (-95 to -20, default = -80). <span class="li-normal">type: str</span>
 <a id='label616' href="javascript:ContentClick('label617', 'label616');" onmouseover="ContentPreview('label617');" onmouseout="ContentUnpreview('label617');" title="click to collapse or expand..."> more... </a>
 <div id="label617" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ptk_rekey</span> <b>(Alias name: ptk-rekey)</b>  Enable/disable ptk rekey for wpa-enterprise security. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label618' href="javascript:ContentClick('label619', 'label618');" onmouseover="ContentPreview('label619');" onmouseout="ContentUnpreview('label619');" title="click to collapse or expand..."> more... </a>
 <div id="label619" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ptk_rekey_intv</span> <b>(Alias name: ptk-rekey-intv)</b>  Ptk rekey interval (1800 - 864000 sec, default = 86400). <span class="li-normal">type: int</span>
 <a id='label620' href="javascript:ContentClick('label621', 'label620');" onmouseover="ContentPreview('label621');" onmouseout="ContentUnpreview('label621');" title="click to collapse or expand..."> more... </a>
 <div id="label621" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">qos_profile</span> <b>(Alias name: qos-profile)</b>  Quality of service profile name. <span class="li-normal">type: str</span>
 <a id='label622' href="javascript:ContentClick('label623', 'label622');" onmouseover="ContentPreview('label623');" onmouseout="ContentUnpreview('label623');" title="click to collapse or expand..."> more... </a>
 <div id="label623" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quarantine</span> Enable/disable station quarantine (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label624' href="javascript:ContentClick('label625', 'label624');" onmouseover="ContentPreview('label625');" onmouseout="ContentUnpreview('label625');" title="click to collapse or expand..."> more... </a>
 <div id="label625" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radio_2g_threshold</span> <b>(Alias name: radio-2g-threshold)</b>  Minimum signal level/threshold in dbm required for the ap response to receive a packet in 2. <span class="li-normal">type: str</span>
 <a id='label626' href="javascript:ContentClick('label627', 'label626');" onmouseover="ContentPreview('label627');" onmouseout="ContentUnpreview('label627');" title="click to collapse or expand..."> more... </a>
 <div id="label627" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radio_5g_threshold</span> <b>(Alias name: radio-5g-threshold)</b>  Minimum signal level/threshold in dbm required for the ap response to receive a packet in 5g band(-95 to -20, default = -76). <span class="li-normal">type: str</span>
 <a id='label628' href="javascript:ContentClick('label629', 'label628');" onmouseover="ContentPreview('label629');" onmouseout="ContentUnpreview('label629');" title="click to collapse or expand..."> more... </a>
 <div id="label629" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radio_sensitivity</span> <b>(Alias name: radio-sensitivity)</b>  Enable/disable software radio sensitivity (to ignore weak signals) (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label630' href="javascript:ContentClick('label631', 'label630');" onmouseover="ContentPreview('label631');" onmouseout="ContentUnpreview('label631');" title="click to collapse or expand..."> more... </a>
 <div id="label631" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth</span> <b>(Alias name: radius-mac-auth)</b>  Enable/disable radius-based mac authentication of clients (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label632' href="javascript:ContentClick('label633', 'label632');" onmouseover="ContentPreview('label633');" onmouseout="ContentUnpreview('label633');" title="click to collapse or expand..."> more... </a>
 <div id="label633" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth_server</span> <b>(Alias name: radius-mac-auth-server)</b>  Radius-based mac authentication server. <span class="li-normal">type: str</span>
 <a id='label634' href="javascript:ContentClick('label635', 'label634');" onmouseover="ContentPreview('label635');" onmouseout="ContentUnpreview('label635');" title="click to collapse or expand..."> more... </a>
 <div id="label635" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth_usergroups</span> <b>(Alias name: radius-mac-auth-usergroups)</b>  Selective user groups that are permitted for radius mac authentication. <span class="li-normal">type: list</span>
 <a id='label636' href="javascript:ContentClick('label637', 'label636');" onmouseover="ContentPreview('label637');" onmouseout="ContentUnpreview('label637');" title="click to collapse or expand..."> more... </a>
 <div id="label637" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_server</span> <b>(Alias name: radius-server)</b>  Radius server to be used to authenticate wifi users. <span class="li-normal">type: str</span>
 <a id='label638' href="javascript:ContentClick('label639', 'label638');" onmouseover="ContentPreview('label639');" onmouseout="ContentUnpreview('label639');" title="click to collapse or expand..."> more... </a>
 <div id="label639" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11a</span> <b>(Alias name: rates-11a)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> 
 <a id='label640' href="javascript:ContentClick('label641', 'label640');" onmouseover="ContentPreview('label641');" onmouseout="ContentUnpreview('label641');" title="click to collapse or expand..."> more... </a>
 <div id="label641" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ac_ss12</span> <b>(Alias name: rates-11ac-ss12)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/1, mcs9/1, mcs0/2, mcs1/2, mcs2/2, mcs3/2, mcs4/2, mcs5/2, mcs6/2, mcs7/2, mcs8/2, mcs9/2, mcs10/1, mcs11/1, mcs10/2, mcs11/2]</span> 
 <a id='label642' href="javascript:ContentClick('label643', 'label642');" onmouseover="ContentPreview('label643');" onmouseout="ContentUnpreview('label643');" title="click to collapse or expand..."> more... </a>
 <div id="label643" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ac_ss34</span> <b>(Alias name: rates-11ac-ss34)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/3, mcs1/3, mcs2/3, mcs3/3, mcs4/3, mcs5/3, mcs6/3, mcs7/3, mcs8/3, mcs9/3, mcs0/4, mcs1/4, mcs2/4, mcs3/4, mcs4/4, mcs5/4, mcs6/4, mcs7/4, mcs8/4, mcs9/4, mcs10/3, mcs11/3, mcs10/4, mcs11/4]</span> 
 <a id='label644' href="javascript:ContentClick('label645', 'label644');" onmouseover="ContentPreview('label645');" onmouseout="ContentUnpreview('label645');" title="click to collapse or expand..."> more... </a>
 <div id="label645" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11bg</span> <b>(Alias name: rates-11bg)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> 
 <a id='label646' href="javascript:ContentClick('label647', 'label646');" onmouseover="ContentPreview('label647');" onmouseout="ContentUnpreview('label647');" title="click to collapse or expand..."> more... </a>
 <div id="label647" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11n_ss12</span> <b>(Alias name: rates-11n-ss12)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/2, mcs9/2, mcs10/2, mcs11/2, mcs12/2, mcs13/2, mcs14/2, mcs15/2]</span> 
 <a id='label648' href="javascript:ContentClick('label649', 'label648');" onmouseover="ContentPreview('label649');" onmouseout="ContentUnpreview('label649');" title="click to collapse or expand..."> more... </a>
 <div id="label649" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11n_ss34</span> <b>(Alias name: rates-11n-ss34)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs16/3, mcs17/3, mcs18/3, mcs19/3, mcs20/3, mcs21/3, mcs22/3, mcs23/3, mcs24/4, mcs25/4, mcs26/4, mcs27/4, mcs28/4, mcs29/4, mcs30/4, mcs31/4]</span> 
 <a id='label650' href="javascript:ContentClick('label651', 'label650');" onmouseover="ContentPreview('label651');" onmouseout="ContentUnpreview('label651');" title="click to collapse or expand..."> more... </a>
 <div id="label651" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">schedule</span> Vap schedule name. <span class="li-normal">type: list or str</span>
 <a id='label652' href="javascript:ContentClick('label653', 'label652');" onmouseover="ContentPreview('label653');" onmouseout="ContentUnpreview('label653');" title="click to collapse or expand..."> more... </a>
 <div id="label653" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security</span> Security mode for the wireless interface (default = wpa2-only-personal). <span class="li-normal">type: str</span> <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, captive-portal, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise, wpa-personal+captive-portal, wpa-only-personal+captive-portal, wpa2-only-personal+captive-portal, osen, wpa3-enterprise, sae, sae-transition, owe, wpa3-sae, wpa3-sae-transition, wpa3-only-enterprise, wpa3-enterprise-transition]</span> 
 <a id='label654' href="javascript:ContentClick('label655', 'label654');" onmouseover="ContentPreview('label655');" onmouseout="ContentUnpreview('label655');" title="click to collapse or expand..."> more... </a>
 <div id="label655" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_exempt_list</span> <b>(Alias name: security-exempt-list)</b>  Optional security exempt list for captive portal authentication. <span class="li-normal">type: str</span>
 <a id='label656' href="javascript:ContentClick('label657', 'label656');" onmouseover="ContentPreview('label657');" onmouseout="ContentUnpreview('label657');" title="click to collapse or expand..."> more... </a>
 <div id="label657" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_obsolete_option</span> <b>(Alias name: security-obsolete-option)</b>  Enable/disable obsolete security options. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label658' href="javascript:ContentClick('label659', 'label658');" onmouseover="ContentPreview('label659');" onmouseout="ContentUnpreview('label659');" title="click to collapse or expand..."> more... </a>
 <div id="label659" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">security_redirect_url</span> <b>(Alias name: security-redirect-url)</b>  Optional url for redirecting users after they pass captive portal authentication. <span class="li-normal">type: str</span>
 <a id='label660' href="javascript:ContentClick('label661', 'label660');" onmouseover="ContentPreview('label661');" onmouseout="ContentUnpreview('label661');" title="click to collapse or expand..."> more... </a>
 <div id="label661" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">selected_usergroups</span> <b>(Alias name: selected-usergroups)</b>  Selective user groups that are permitted to authenticate. <span class="li-normal">type: list or str</span>
 <a id='label662' href="javascript:ContentClick('label663', 'label662');" onmouseover="ContentPreview('label663');" onmouseout="ContentUnpreview('label663');" title="click to collapse or expand..."> more... </a>
 <div id="label663" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">split_tunneling</span> <b>(Alias name: split-tunneling)</b>  Enable/disable split tunneling (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label664' href="javascript:ContentClick('label665', 'label664');" onmouseover="ContentPreview('label665');" onmouseout="ContentUnpreview('label665');" title="click to collapse or expand..."> more... </a>
 <div id="label665" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssid</span> Ieee 802. <span class="li-normal">type: str</span>
 <a id='label666' href="javascript:ContentClick('label667', 'label666');" onmouseover="ContentPreview('label667');" onmouseout="ContentUnpreview('label667');" title="click to collapse or expand..."> more... </a>
 <div id="label667" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tkip_counter_measure</span> <b>(Alias name: tkip-counter-measure)</b>  Enable/disable tkip counter measure. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label668' href="javascript:ContentClick('label669', 'label668');" onmouseover="ContentPreview('label669');" onmouseout="ContentUnpreview('label669');" title="click to collapse or expand..."> more... </a>
 <div id="label669" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">usergroup</span> Firewall user group to be used to authenticate wifi users. <span class="li-normal">type: list or str</span>
 <a id='label670' href="javascript:ContentClick('label671', 'label670');" onmouseover="ContentPreview('label671');" onmouseout="ContentUnpreview('label671');" title="click to collapse or expand..."> more... </a>
 <div id="label671" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">utm_profile</span> <b>(Alias name: utm-profile)</b>  Utm profile name. <span class="li-normal">type: str</span>
 <a id='label672' href="javascript:ContentClick('label673', 'label672');" onmouseover="ContentPreview('label673');" onmouseout="ContentUnpreview('label673');" title="click to collapse or expand..."> more... </a>
 <div id="label673" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vdom</span> Name of the vdom that the virtual ap has been added to. <span class="li-normal">type: str</span>
 <a id='label674' href="javascript:ContentClick('label675', 'label674');" onmouseover="ContentPreview('label675');" onmouseout="ContentUnpreview('label675');" title="click to collapse or expand..."> more... </a>
 <div id="label675" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.1</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_auto</span> <b>(Alias name: vlan-auto)</b>  Enable/disable automatic management of ssid vlan interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label676' href="javascript:ContentClick('label677', 'label676');" onmouseover="ContentPreview('label677');" onmouseout="ContentUnpreview('label677');" title="click to collapse or expand..."> more... </a>
 <div id="label677" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_pool</span> <b>(Alias name: vlan-pool)</b>  Vlan pool. <span class="li-normal">type: list</span>
 <a id='label678' href="javascript:ContentClick('label679', 'label678');" onmouseover="ContentPreview('label679');" onmouseout="ContentUnpreview('label679');" title="click to collapse or expand..."> more... </a>
 <div id="label679" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">_wtp_group</span> <b>(Alias name: _wtp-group)</b>  Wtp group. <span class="li-normal">type: str</span>
 <a id='label680' href="javascript:ContentClick('label681', 'label680');" onmouseover="ContentPreview('label681');" onmouseout="ContentUnpreview('label681');" title="click to collapse or expand..."> more... </a>
 <div id="label681" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label682' href="javascript:ContentClick('label683', 'label682');" onmouseover="ContentPreview('label683');" onmouseout="ContentUnpreview('label683');" title="click to collapse or expand..."> more... </a>
 <div id="label683" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wtp_group</span> <b>(Alias name: wtp-group)</b>  Wtp group name. <span class="li-normal">type: str</span>
 <a id='label684' href="javascript:ContentClick('label685', 'label684');" onmouseover="ContentPreview('label685');" onmouseout="ContentUnpreview('label685');" title="click to collapse or expand..."> more... </a>
 <div id="label685" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v6.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">vlan_pooling</span> <b>(Alias name: vlan-pooling)</b>  Enable/disable vlan pooling, to allow grouping of multiple wireless controller vlans into vlan pools (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [wtp-group, round-robin, hash, disable]</span> 
 <a id='label686' href="javascript:ContentClick('label687', 'label686');" onmouseover="ContentPreview('label687');" onmouseout="ContentUnpreview('label687');" title="click to collapse or expand..."> more... </a>
 <div id="label687" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlanid</span> Optional vlan id. <span class="li-normal">type: int</span>
 <a id='label688' href="javascript:ContentClick('label689', 'label688');" onmouseover="ContentPreview('label689');" onmouseout="ContentUnpreview('label689');" title="click to collapse or expand..."> more... </a>
 <div id="label689" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">voice_enterprise</span> <b>(Alias name: voice-enterprise)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label690' href="javascript:ContentClick('label691', 'label690');" onmouseover="ContentPreview('label691');" onmouseout="ContentUnpreview('label691');" title="click to collapse or expand..."> more... </a>
 <div id="label691" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">address_group</span> <b>(Alias name: address-group)</b>  Address group id. <span class="li-normal">type: str</span>
 <a id='label692' href="javascript:ContentClick('label693', 'label692');" onmouseover="ContentPreview('label693');" onmouseout="ContentUnpreview('label693');" title="click to collapse or expand..."> more... </a>
 <div id="label693" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">atf_weight</span> <b>(Alias name: atf-weight)</b>  Airtime weight in percentage (default = 20). <span class="li-normal">type: int</span>
 <a id='label694' href="javascript:ContentClick('label695', 'label694');" onmouseover="ContentPreview('label695');" onmouseout="ContentUnpreview('label695');" title="click to collapse or expand..."> more... </a>
 <div id="label695" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mu_mimo</span> <b>(Alias name: mu-mimo)</b>  Enable/disable multi-user mimo (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label696' href="javascript:ContentClick('label697', 'label696');" onmouseover="ContentPreview('label697');" onmouseout="ContentUnpreview('label697');" title="click to collapse or expand..."> more... </a>
 <div id="label697" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">owe_groups</span> <b>(Alias name: owe-groups)</b>  Owe-groups. <span class="li-normal">type: list</span> <span class="li-normal">choices: [19, 20, 21]</span> 
 <a id='label698' href="javascript:ContentClick('label699', 'label698');" onmouseover="ContentPreview('label699');" onmouseout="ContentUnpreview('label699');" title="click to collapse or expand..."> more... </a>
 <div id="label699" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">owe_transition</span> <b>(Alias name: owe-transition)</b>  Enable/disable owe transition mode support. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label700' href="javascript:ContentClick('label701', 'label700');" onmouseover="ContentPreview('label701');" onmouseout="ContentUnpreview('label701');" title="click to collapse or expand..."> more... </a>
 <div id="label701" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">owe_transition_ssid</span> <b>(Alias name: owe-transition-ssid)</b>  Owe transition mode peer ssid. <span class="li-normal">type: str</span>
 <a id='label702' href="javascript:ContentClick('label703', 'label702');" onmouseover="ContentPreview('label703');" onmouseout="ContentUnpreview('label703');" title="click to collapse or expand..."> more... </a>
 <div id="label703" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_groups</span> <b>(Alias name: sae-groups)</b>  Sae-groups. <span class="li-normal">type: list</span> <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31]</span> 
 <a id='label704' href="javascript:ContentClick('label705', 'label704');" onmouseover="ContentPreview('label705');" onmouseout="ContentUnpreview('label705');" title="click to collapse or expand..."> more... </a>
 <div id="label705" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_password</span> <b>(Alias name: sae-password)</b>  Wpa3 sae password to be used to authenticate wifi users. <span class="li-normal">type: list</span>
 <a id='label706' href="javascript:ContentClick('label707', 'label706');" onmouseover="ContentPreview('label707');" onmouseout="ContentUnpreview('label707');" title="click to collapse or expand..."> more... </a>
 <div id="label707" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_device_access_list</span> <b>(Alias name: _intf_device-access-list)</b>  Intf device access list. <span class="li-normal">type: str</span>
 <a id='label708' href="javascript:ContentClick('label709', 'label708');" onmouseover="ContentPreview('label709');" onmouseout="ContentUnpreview('label709');" title="click to collapse or expand..."> more... </a>
 <div id="label709" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_web_format</span> <b>(Alias name: external-web-format)</b>  Url query parameter detection (default = auto-detect). <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto-detect, no-query-string, partial-query-string]</span> 
 <a id='label710' href="javascript:ContentClick('label711', 'label710');" onmouseover="ContentPreview('label711');" onmouseout="ContentUnpreview('label711');" title="click to collapse or expand..."> more... </a>
 <div id="label711" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">high_efficiency</span> <b>(Alias name: high-efficiency)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label712' href="javascript:ContentClick('label713', 'label712');" onmouseover="ContentPreview('label713');" onmouseout="ContentUnpreview('label713');" title="click to collapse or expand..."> more... </a>
 <div id="label713" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">primary_wag_profile</span> <b>(Alias name: primary-wag-profile)</b>  Primary wireless access gateway profile name. <span class="li-normal">type: str</span>
 <a id='label714' href="javascript:ContentClick('label715', 'label714');" onmouseover="ContentPreview('label715');" onmouseout="ContentUnpreview('label715');" title="click to collapse or expand..."> more... </a>
 <div id="label715" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">secondary_wag_profile</span> <b>(Alias name: secondary-wag-profile)</b>  Secondary wireless access gateway profile name. <span class="li-normal">type: str</span>
 <a id='label716' href="javascript:ContentClick('label717', 'label716');" onmouseover="ContentPreview('label717');" onmouseout="ContentUnpreview('label717');" title="click to collapse or expand..."> more... </a>
 <div id="label717" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">target_wake_time</span> <b>(Alias name: target-wake-time)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label718' href="javascript:ContentClick('label719', 'label718');" onmouseover="ContentPreview('label719');" onmouseout="ContentUnpreview('label719');" title="click to collapse or expand..."> more... </a>
 <div id="label719" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tunnel_echo_interval</span> <b>(Alias name: tunnel-echo-interval)</b>  The time interval to send echo to both primary and secondary tunnel peers (1 - 65535 sec, default = 300). <span class="li-normal">type: int</span>
 <a id='label720' href="javascript:ContentClick('label721', 'label720');" onmouseover="ContentPreview('label721');" onmouseout="ContentUnpreview('label721');" title="click to collapse or expand..."> more... </a>
 <div id="label721" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tunnel_fallback_interval</span> <b>(Alias name: tunnel-fallback-interval)</b>  The time interval for secondary tunnel to fall back to primary tunnel (0 - 65535 sec, default = 7200). <span class="li-normal">type: int</span>
 <a id='label722' href="javascript:ContentClick('label723', 'label722');" onmouseover="ContentPreview('label723');" onmouseout="ContentUnpreview('label723');" title="click to collapse or expand..."> more... </a>
 <div id="label723" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">access_control_list</span> <b>(Alias name: access-control-list)</b>  Access-control-list profile name. <span class="li-normal">type: str</span>
 <a id='label724' href="javascript:ContentClick('label725', 'label724');" onmouseover="ContentPreview('label725');" onmouseout="ContentUnpreview('label725');" title="click to collapse or expand..."> more... </a>
 <div id="label725" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_auth_timeout</span> <b>(Alias name: captive-portal-auth-timeout)</b>  Hard timeout - ap will always clear the session after timeout regardless of traffic (0 - 864000 sec, default = 0). <span class="li-normal">type: int</span>
 <a id='label726' href="javascript:ContentClick('label727', 'label726');" onmouseover="ContentPreview('label727');" onmouseout="ContentUnpreview('label727');" title="click to collapse or expand..."> more... </a>
 <div id="label727" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6_rules</span> <b>(Alias name: ipv6-rules)</b>  Optional rules of ipv6 packets. <span class="li-normal">type: list</span> <span class="li-normal">choices: [drop-icmp6ra, drop-icmp6rs, drop-llmnr6, drop-icmp6mld2, drop-dhcp6s, drop-dhcp6c, ndp-proxy, drop-ns-dad, drop-ns-nondad]</span> 
 <a id='label728' href="javascript:ContentClick('label729', 'label728');" onmouseover="ContentPreview('label729');" onmouseout="ContentUnpreview('label729');" title="click to collapse or expand..."> more... </a>
 <div id="label729" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_remove</span> <b>(Alias name: sticky-client-remove)</b>  Enable/disable sticky client remove to maintain good signal level clients in ssid. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label730' href="javascript:ContentClick('label731', 'label730');" onmouseover="ContentPreview('label731');" onmouseout="ContentUnpreview('label731');" title="click to collapse or expand..."> more... </a>
 <div id="label731" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_threshold_2g</span> <b>(Alias name: sticky-client-threshold-2g)</b>  Minimum signal level/threshold in dbm required for the 2g client to be serviced by the ap (-95 to -20, default = -79). <span class="li-normal">type: str</span>
 <a id='label732' href="javascript:ContentClick('label733', 'label732');" onmouseover="ContentPreview('label733');" onmouseout="ContentUnpreview('label733');" title="click to collapse or expand..."> more... </a>
 <div id="label733" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_threshold_5g</span> <b>(Alias name: sticky-client-threshold-5g)</b>  Minimum signal level/threshold in dbm required for the 5g client to be serviced by the ap (-95 to -20, default = -76). <span class="li-normal">type: str</span>
 <a id='label734' href="javascript:ContentClick('label735', 'label734');" onmouseover="ContentPreview('label735');" onmouseout="ContentUnpreview('label735');" title="click to collapse or expand..."> more... </a>
 <div id="label735" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bss_color_partial</span> <b>(Alias name: bss-color-partial)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label736' href="javascript:ContentClick('label737', 'label736');" onmouseover="ContentPreview('label737');" onmouseout="ContentUnpreview('label737');" title="click to collapse or expand..."> more... </a>
 <div id="label737" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_option43_insertion</span> <b>(Alias name: dhcp-option43-insertion)</b>  Enable/disable insertion of dhcp option 43 (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label738' href="javascript:ContentClick('label739', 'label738');" onmouseover="ContentPreview('label739');" onmouseout="ContentUnpreview('label739');" title="click to collapse or expand..."> more... </a>
 <div id="label739" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mpsk_profile</span> <b>(Alias name: mpsk-profile)</b>  Mpsk profile name. <span class="li-normal">type: str</span>
 <a id='label740' href="javascript:ContentClick('label741', 'label740');" onmouseover="ContentPreview('label741');" onmouseout="ContentUnpreview('label741');" title="click to collapse or expand..."> more... </a>
 <div id="label741" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">igmp_snooping</span> <b>(Alias name: igmp-snooping)</b>  Enable/disable igmp snooping. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label742' href="javascript:ContentClick('label743', 'label742');" onmouseover="ContentPreview('label743');" onmouseout="ContentUnpreview('label743');" title="click to collapse or expand..."> more... </a>
 <div id="label743" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port_macauth</span> <b>(Alias name: port-macauth)</b>  Enable/disable lan port mac authentication (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, radius, address-group]</span> 
 <a id='label744' href="javascript:ContentClick('label745', 'label744');" onmouseover="ContentPreview('label745');" onmouseout="ContentUnpreview('label745');" title="click to collapse or expand..."> more... </a>
 <div id="label745" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port_macauth_reauth_timeout</span> <b>(Alias name: port-macauth-reauth-timeout)</b>  Lan port mac authentication re-authentication timeout value (default = 7200 sec). <span class="li-normal">type: int</span>
 <a id='label746' href="javascript:ContentClick('label747', 'label746');" onmouseover="ContentPreview('label747');" onmouseout="ContentUnpreview('label747');" title="click to collapse or expand..."> more... </a>
 <div id="label747" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port_macauth_timeout</span> <b>(Alias name: port-macauth-timeout)</b>  Lan port mac authentication idle timeout value (default = 600 sec). <span class="li-normal">type: int</span>
 <a id='label748' href="javascript:ContentClick('label749', 'label748');" onmouseover="ContentPreview('label749');" onmouseout="ContentUnpreview('label749');" title="click to collapse or expand..."> more... </a>
 <div id="label749" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">portal_message_overrides</span> <b>(Alias name: portal-message-overrides)</b>  Portal message overrides. <span class="li-normal">type: dict</span>
 <a id='label750' href="javascript:ContentClick('label751', 'label750');" onmouseover="ContentPreview('label751');" onmouseout="ContentUnpreview('label751');" title="click to collapse or expand..."> more... </a>
 <div id="label751" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">auth_disclaimer_page</span> <b>(Alias name: auth-disclaimer-page)</b>  Override auth-disclaimer-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>
 <a id='label752' href="javascript:ContentClick('label753', 'label752');" onmouseover="ContentPreview('label753');" onmouseout="ContentUnpreview('label753');" title="click to collapse or expand..."> more... </a>
 <div id="label753" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_login_failed_page</span> <b>(Alias name: auth-login-failed-page)</b>  Override auth-login-failed-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>
 <a id='label754' href="javascript:ContentClick('label755', 'label754');" onmouseover="ContentPreview('label755');" onmouseout="ContentUnpreview('label755');" title="click to collapse or expand..."> more... </a>
 <div id="label755" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_login_page</span> <b>(Alias name: auth-login-page)</b>  Override auth-login-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>
 <a id='label756' href="javascript:ContentClick('label757', 'label756');" onmouseover="ContentPreview('label757');" onmouseout="ContentUnpreview('label757');" title="click to collapse or expand..."> more... </a>
 <div id="label757" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_reject_page</span> <b>(Alias name: auth-reject-page)</b>  Override auth-reject-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>
 <a id='label758' href="javascript:ContentClick('label759', 'label758');" onmouseover="ContentPreview('label759');" onmouseout="ContentUnpreview('label759');" title="click to collapse or expand..."> more... </a>
 <div id="label759" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">additional_akms</span> <b>(Alias name: additional-akms)</b>  Additional akms. <span class="li-normal">type: list</span> <span class="li-normal">choices: [akm6, akm24]</span> 
 <a id='label760' href="javascript:ContentClick('label761', 'label760');" onmouseover="ContentPreview('label761');" onmouseout="ContentUnpreview('label761');" title="click to collapse or expand..."> more... </a>
 <div id="label761" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bstm_disassociation_imminent</span> <b>(Alias name: bstm-disassociation-imminent)</b>  Enable/disable forcing of disassociation after the bstm request timer has been reached (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label762' href="javascript:ContentClick('label763', 'label762');" onmouseover="ContentPreview('label763');" onmouseout="ContentUnpreview('label763');" title="click to collapse or expand..."> more... </a>
 <div id="label763" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bstm_load_balancing_disassoc_timer</span> <b>(Alias name: bstm-load-balancing-disassoc-timer)</b>  Time interval for client to voluntarily leave ap before forcing a disassociation due to ap load-balancing (0 to 30, default = 10). <span class="li-normal">type: int</span>
 <a id='label764' href="javascript:ContentClick('label765', 'label764');" onmouseover="ContentPreview('label765');" onmouseout="ContentUnpreview('label765');" title="click to collapse or expand..."> more... </a>
 <div id="label765" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bstm_rssi_disassoc_timer</span> <b>(Alias name: bstm-rssi-disassoc-timer)</b>  Time interval for client to voluntarily leave ap before forcing a disassociation due to low rssi (0 to 2000, default = 200). <span class="li-normal">type: int</span>
 <a id='label766' href="javascript:ContentClick('label767', 'label766');" onmouseover="ContentPreview('label767');" onmouseout="ContentUnpreview('label767');" title="click to collapse or expand..."> more... </a>
 <div id="label767" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_address_enforcement</span> <b>(Alias name: dhcp-address-enforcement)</b>  Enable/disable dhcp address enforcement (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label768' href="javascript:ContentClick('label769', 'label768');" onmouseover="ContentPreview('label769');" onmouseout="ContentUnpreview('label769');" title="click to collapse or expand..."> more... </a>
 <div id="label769" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gas_comeback_delay</span> <b>(Alias name: gas-comeback-delay)</b>  Gas comeback delay (0 or 100 - 10000 milliseconds, default = 500). <span class="li-normal">type: int</span>
 <a id='label770' href="javascript:ContentClick('label771', 'label770');" onmouseover="ContentPreview('label771');" onmouseout="ContentUnpreview('label771');" title="click to collapse or expand..."> more... </a>
 <div id="label771" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gas_fragmentation_limit</span> <b>(Alias name: gas-fragmentation-limit)</b>  Gas fragmentation limit (512 - 4096, default = 1024). <span class="li-normal">type: int</span>
 <a id='label772' href="javascript:ContentClick('label773', 'label772');" onmouseover="ContentPreview('label773');" onmouseout="ContentUnpreview('label773');" title="click to collapse or expand..."> more... </a>
 <div id="label773" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_called_station_delimiter</span> <b>(Alias name: mac-called-station-delimiter)</b>  Mac called station delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label774' href="javascript:ContentClick('label775', 'label774');" onmouseover="ContentPreview('label775');" onmouseout="ContentUnpreview('label775');" title="click to collapse or expand..."> more... </a>
 <div id="label775" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_calling_station_delimiter</span> <b>(Alias name: mac-calling-station-delimiter)</b>  Mac calling station delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label776' href="javascript:ContentClick('label777', 'label776');" onmouseover="ContentPreview('label777');" onmouseout="ContentUnpreview('label777');" title="click to collapse or expand..."> more... </a>
 <div id="label777" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_case</span> <b>(Alias name: mac-case)</b>  Mac case (default = uppercase). <span class="li-normal">type: str</span> <span class="li-normal">choices: [uppercase, lowercase]</span> 
 <a id='label778' href="javascript:ContentClick('label779', 'label778');" onmouseover="ContentPreview('label779');" onmouseout="ContentUnpreview('label779');" title="click to collapse or expand..."> more... </a>
 <div id="label779" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_password_delimiter</span> <b>(Alias name: mac-password-delimiter)</b>  Mac authentication password delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label780' href="javascript:ContentClick('label781', 'label780');" onmouseover="ContentPreview('label781');" onmouseout="ContentUnpreview('label781');" title="click to collapse or expand..."> more... </a>
 <div id="label781" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mac_username_delimiter</span> <b>(Alias name: mac-username-delimiter)</b>  Mac authentication username delimiter (default = hyphen). <span class="li-normal">type: str</span> <span class="li-normal">choices: [hyphen, single-hyphen, colon, none]</span> 
 <a id='label782' href="javascript:ContentClick('label783', 'label782');" onmouseover="ContentPreview('label783');" onmouseout="ContentUnpreview('label783');" title="click to collapse or expand..."> more... </a>
 <div id="label783" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mbo</span> Enable/disable multiband operation (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label784' href="javascript:ContentClick('label785', 'label784');" onmouseover="ContentPreview('label785');" onmouseout="ContentUnpreview('label785');" title="click to collapse or expand..."> more... </a>
 <div id="label785" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mbo_cell_data_conn_pref</span> <b>(Alias name: mbo-cell-data-conn-pref)</b>  Mbo cell data connection preference (0, 1, or 255, default = 1). <span class="li-normal">type: str</span> <span class="li-normal">choices: [excluded, prefer-not, prefer-use]</span> 
 <a id='label786' href="javascript:ContentClick('label787', 'label786');" onmouseover="ContentPreview('label787');" onmouseout="ContentUnpreview('label787');" title="click to collapse or expand..."> more... </a>
 <div id="label787" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nac</span> Enable/disable network access control. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label788' href="javascript:ContentClick('label789', 'label788');" onmouseover="ContentPreview('label789');" onmouseout="ContentUnpreview('label789');" title="click to collapse or expand..."> more... </a>
 <div id="label789" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nac_profile</span> <b>(Alias name: nac-profile)</b>  Nac profile name. <span class="li-normal">type: str</span>
 <a id='label790' href="javascript:ContentClick('label791', 'label790');" onmouseover="ContentPreview('label791');" onmouseout="ContentUnpreview('label791');" title="click to collapse or expand..."> more... </a>
 <div id="label791" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">neighbor_report_dual_band</span> <b>(Alias name: neighbor-report-dual-band)</b>  Enable/disable dual-band neighbor report (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label792' href="javascript:ContentClick('label793', 'label792');" onmouseover="ContentPreview('label793');" onmouseout="ContentUnpreview('label793');" title="click to collapse or expand..."> more... </a>
 <div id="label793" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">address_group_policy</span> <b>(Alias name: address-group-policy)</b>  Configure mac address filtering policy for mac addresses that are in the address-group. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, allow, deny]</span> 
 <a id='label794' href="javascript:ContentClick('label795', 'label794');" onmouseover="ContentPreview('label795');" onmouseout="ContentUnpreview('label795');" title="click to collapse or expand..."> more... </a>
 <div id="label795" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antivirus_profile</span> <b>(Alias name: antivirus-profile)</b>  Antivirus profile name. <span class="li-normal">type: str</span>
 <a id='label796' href="javascript:ContentClick('label797', 'label796');" onmouseover="ContentPreview('label797');" onmouseout="ContentUnpreview('label797');" title="click to collapse or expand..."> more... </a>
 <div id="label797" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_detection_engine</span> <b>(Alias name: application-detection-engine)</b>  Enable/disable application detection engine (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label798' href="javascript:ContentClick('label799', 'label798');" onmouseover="ContentPreview('label799');" onmouseout="ContentUnpreview('label799');" title="click to collapse or expand..."> more... </a>
 <div id="label799" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_list</span> <b>(Alias name: application-list)</b>  Application control list name. <span class="li-normal">type: str</span>
 <a id='label800' href="javascript:ContentClick('label801', 'label800');" onmouseover="ContentPreview('label801');" onmouseout="ContentUnpreview('label801');" title="click to collapse or expand..."> more... </a>
 <div id="label801" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_report_intv</span> <b>(Alias name: application-report-intv)</b>  Application report interval (30 - 864000 sec, default = 120). <span class="li-normal">type: int</span>
 <a id='label802' href="javascript:ContentClick('label803', 'label802');" onmouseover="ContentPreview('label803');" onmouseout="ContentUnpreview('label803');" title="click to collapse or expand..."> more... </a>
 <div id="label803" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_cert</span> <b>(Alias name: auth-cert)</b>  Https server certificate. <span class="li-normal">type: str</span>
 <a id='label804' href="javascript:ContentClick('label805', 'label804');" onmouseover="ContentPreview('label805');" onmouseout="ContentUnpreview('label805');" title="click to collapse or expand..."> more... </a>
 <div id="label805" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_portal_addr</span> <b>(Alias name: auth-portal-addr)</b>  Address of captive portal. <span class="li-normal">type: str</span>
 <a id='label806' href="javascript:ContentClick('label807', 'label806');" onmouseover="ContentPreview('label807');" onmouseout="ContentUnpreview('label807');" title="click to collapse or expand..."> more... </a>
 <div id="label807" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">beacon_advertising</span> <b>(Alias name: beacon-advertising)</b>  Fortinet beacon advertising ie data   (default = empty). <span class="li-normal">type: list</span> <span class="li-normal">choices: [name, model, serial-number]</span> 
 <a id='label808' href="javascript:ContentClick('label809', 'label808');" onmouseover="ContentPreview('label809');" onmouseout="ContentUnpreview('label809');" title="click to collapse or expand..."> more... </a>
 <div id="label809" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ips_sensor</span> <b>(Alias name: ips-sensor)</b>  Ips sensor name. <span class="li-normal">type: str</span>
 <a id='label810' href="javascript:ContentClick('label811', 'label810');" onmouseover="ContentPreview('label811');" onmouseout="ContentUnpreview('label811');" title="click to collapse or expand..."> more... </a>
 <div id="label811" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">l3_roaming</span> <b>(Alias name: l3-roaming)</b>  Enable/disable layer 3 roaming (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label812' href="javascript:ContentClick('label813', 'label812');" onmouseover="ContentPreview('label813');" onmouseout="ContentUnpreview('label813');" title="click to collapse or expand..."> more... </a>
 <div id="label813" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone_dns</span> <b>(Alias name: local-standalone-dns)</b>  Enable/disable ap local standalone dns. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label814' href="javascript:ContentClick('label815', 'label814');" onmouseover="ContentPreview('label815');" onmouseout="ContentUnpreview('label815');" title="click to collapse or expand..."> more... </a>
 <div id="label815" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_standalone_dns_ip</span> <b>(Alias name: local-standalone-dns-ip)</b>  Ipv4 addresses for the local standalone dns. <span class="li-normal">type: list</span>
 <a id='label816' href="javascript:ContentClick('label817', 'label816');" onmouseover="ContentPreview('label817');" onmouseout="ContentUnpreview('label817');" title="click to collapse or expand..."> more... </a>
 <div id="label817" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">osen</span> Enable/disable osen as part of key management (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label818' href="javascript:ContentClick('label819', 'label818');" onmouseover="ContentPreview('label819');" onmouseout="ContentUnpreview('label819');" title="click to collapse or expand..."> more... </a>
 <div id="label819" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_mpsk_auth</span> <b>(Alias name: radius-mac-mpsk-auth)</b>  Enable/disable radius-based mac authentication of clients for mpsk authentication (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label820' href="javascript:ContentClick('label821', 'label820');" onmouseover="ContentPreview('label821');" onmouseout="ContentUnpreview('label821');" title="click to collapse or expand..."> more... </a>
 <div id="label821" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_mpsk_timeout</span> <b>(Alias name: radius-mac-mpsk-timeout)</b>  Radius mac mpsk cache timeout interval (1800 - 864000, default = 86400). <span class="li-normal">type: int</span>
 <a id='label822' href="javascript:ContentClick('label823', 'label822');" onmouseover="ContentPreview('label823');" onmouseout="ContentUnpreview('label823');" title="click to collapse or expand..."> more... </a>
 <div id="label823" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ax_ss12</span> <b>(Alias name: rates-11ax-ss12)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/1, mcs9/1, mcs10/1, mcs11/1, mcs0/2, mcs1/2, mcs2/2, mcs3/2, mcs4/2, mcs5/2, mcs6/2, mcs7/2, mcs8/2, mcs9/2, mcs10/2, mcs11/2]</span> 
 <a id='label824' href="javascript:ContentClick('label825', 'label824');" onmouseover="ContentPreview('label825');" onmouseout="ContentUnpreview('label825');" title="click to collapse or expand..."> more... </a>
 <div id="label825" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ax_ss34</span> <b>(Alias name: rates-11ax-ss34)</b>  Allowed data rates for 802. <span class="li-normal">type: list</span> <span class="li-normal">choices: [mcs0/3, mcs1/3, mcs2/3, mcs3/3, mcs4/3, mcs5/3, mcs6/3, mcs7/3, mcs8/3, mcs9/3, mcs10/3, mcs11/3, mcs0/4, mcs1/4, mcs2/4, mcs3/4, mcs4/4, mcs5/4, mcs6/4, mcs7/4, mcs8/4, mcs9/4, mcs10/4, mcs11/4]</span> 
 <a id='label826' href="javascript:ContentClick('label827', 'label826');" onmouseover="ContentPreview('label827');" onmouseout="ContentUnpreview('label827');" title="click to collapse or expand..."> more... </a>
 <div id="label827" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">scan_botnet_connections</span> <b>(Alias name: scan-botnet-connections)</b>  Block or monitor connections to botnet servers or disable botnet scanning. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, block, monitor]</span> 
 <a id='label828' href="javascript:ContentClick('label829', 'label828');" onmouseover="ContentPreview('label829');" onmouseout="ContentUnpreview('label829');" title="click to collapse or expand..."> more... </a>
 <div id="label829" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">utm_log</span> <b>(Alias name: utm-log)</b>  Enable/disable utm logging. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label830' href="javascript:ContentClick('label831', 'label830');" onmouseover="ContentPreview('label831');" onmouseout="ContentUnpreview('label831');" title="click to collapse or expand..."> more... </a>
 <div id="label831" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">utm_status</span> <b>(Alias name: utm-status)</b>  Enable to add one or more security profiles (av, ips, etc. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label832' href="javascript:ContentClick('label833', 'label832');" onmouseover="ContentPreview('label833');" onmouseout="ContentUnpreview('label833');" title="click to collapse or expand..."> more... </a>
 <div id="label833" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_name</span> <b>(Alias name: vlan-name)</b>  Vlan name. <span class="li-normal">type: list</span>
 <a id='label834' href="javascript:ContentClick('label835', 'label834');" onmouseover="ContentPreview('label835');" onmouseout="ContentUnpreview('label835');" title="click to collapse or expand..."> more... </a>
 <div id="label835" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">name</span> Vlan name. <span class="li-normal">type: str</span>
 <a id='label836' href="javascript:ContentClick('label837', 'label836');" onmouseover="ContentPreview('label837');" onmouseout="ContentUnpreview('label837');" title="click to collapse or expand..."> more... </a>
 <div id="label837" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vlan_id</span> <b>(Alias name: vlan-id)</b>  Vlan id. <span class="li-normal">type: int</span>
 <a id='label838' href="javascript:ContentClick('label839', 'label838');" onmouseover="ContentPreview('label839');" onmouseout="ContentUnpreview('label839');" title="click to collapse or expand..."> more... </a>
 <div id="label839" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">webfilter_profile</span> <b>(Alias name: webfilter-profile)</b>  Webfilter profile name. <span class="li-normal">type: str</span>
 <a id='label840' href="javascript:ContentClick('label841', 'label840');" onmouseover="ContentPreview('label841');" onmouseout="ContentUnpreview('label841');" title="click to collapse or expand..."> more... </a>
 <div id="label841" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_h2e_only</span> <b>(Alias name: sae-h2e-only)</b>  Use hash-to-element-only mechanism for pwe derivation (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label842' href="javascript:ContentClick('label843', 'label842');" onmouseover="ContentPreview('label843');" onmouseout="ContentUnpreview('label843');" title="click to collapse or expand..."> more... </a>
 <div id="label843" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_pk</span> <b>(Alias name: sae-pk)</b>  Enable/disable wpa3 sae-pk (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label844' href="javascript:ContentClick('label845', 'label844');" onmouseover="ContentPreview('label845');" onmouseout="ContentUnpreview('label845');" title="click to collapse or expand..."> more... </a>
 <div id="label845" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_private_key</span> <b>(Alias name: sae-private-key)</b>  Private key used for wpa3 sae-pk authentication. <span class="li-normal">type: str</span>
 <a id='label846' href="javascript:ContentClick('label847', 'label846');" onmouseover="ContentPreview('label847');" onmouseout="ContentUnpreview('label847');" title="click to collapse or expand..."> more... </a>
 <div id="label847" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sticky_client_threshold_6g</span> <b>(Alias name: sticky-client-threshold-6g)</b>  Minimum signal level/threshold in dbm required for the 6g client to be serviced by the ap (-95 to -20, default = -76). <span class="li-normal">type: str</span>
 <a id='label848' href="javascript:ContentClick('label849', 'label848');" onmouseover="ContentPreview('label849');" onmouseout="ContentUnpreview('label849');" title="click to collapse or expand..."> more... </a>
 <div id="label849" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application_dscp_marking</span> <b>(Alias name: application-dscp-marking)</b>  Enable/disable application attribute based dscp marking (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label850' href="javascript:ContentClick('label851', 'label850');" onmouseover="ContentPreview('label851');" onmouseout="ContentUnpreview('label851');" title="click to collapse or expand..."> more... </a>
 <div id="label851" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">l3_roaming_mode</span> <b>(Alias name: l3-roaming-mode)</b>  Select the way that layer 3 roaming traffic is passed (default = direct). <span class="li-normal">type: str</span> <span class="li-normal">choices: [direct, indirect]</span> 
 <a id='label852' href="javascript:ContentClick('label853', 'label852');" onmouseover="ContentPreview('label853');" onmouseout="ContentUnpreview('label853');" title="click to collapse or expand..."> more... </a>
 <div id="label853" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ac_mcs_map</span> <b>(Alias name: rates-11ac-mcs-map)</b>  Comma separated list of max supported vht mcs for spatial streams 1 through 8. <span class="li-normal">type: str</span>
 <a id='label854' href="javascript:ContentClick('label855', 'label854');" onmouseover="ContentPreview('label855');" onmouseout="ContentUnpreview('label855');" title="click to collapse or expand..."> more... </a>
 <div id="label855" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11ax_mcs_map</span> <b>(Alias name: rates-11ax-mcs-map)</b>  Comma separated list of max supported he mcs for spatial streams 1 through 8. <span class="li-normal">type: str</span>
 <a id='label856' href="javascript:ContentClick('label857', 'label856');" onmouseover="ContentPreview('label857');" onmouseout="ContentUnpreview('label857');" title="click to collapse or expand..."> more... </a>
 <div id="label857" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_fw_accounting</span> <b>(Alias name: captive-portal-fw-accounting)</b>  Enable/disable radius accounting for captive portal firewall authentication session. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label858' href="javascript:ContentClick('label859', 'label858');" onmouseover="ContentPreview('label859');" onmouseout="ContentUnpreview('label859');" title="click to collapse or expand..."> more... </a>
 <div id="label859" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radius_mac_auth_block_interval</span> <b>(Alias name: radius-mac-auth-block-interval)</b>  Dont send radius mac auth request again if the client has been rejected within specific interval (0 or 30 - 864000 seconds, default = 0, 0 to disable blocking). <span class="li-normal">type: int</span>
 <a id='label860' href="javascript:ContentClick('label861', 'label860');" onmouseover="ContentPreview('label861');" onmouseout="ContentUnpreview('label861');" title="click to collapse or expand..."> more... </a>
 <div id="label861" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_is_factory_setting</span> Is factory setting. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, ext]</span>  <span class="li-normal">default: disable</span> 
 <a id='label862' href="javascript:ContentClick('label863', 'label862');" onmouseover="ContentPreview('label863');" onmouseout="ContentUnpreview('label863');" title="click to collapse or expand..."> more... </a>
 <div id="label863" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">d80211k</span> <b>(Alias name: 80211k)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label864' href="javascript:ContentClick('label865', 'label864');" onmouseover="ContentPreview('label865');" onmouseout="ContentUnpreview('label865');" title="click to collapse or expand..."> more... </a>
 <div id="label865" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">d80211v</span> <b>(Alias name: 80211v)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label866' href="javascript:ContentClick('label867', 'label866');" onmouseover="ContentPreview('label867');" onmouseout="ContentUnpreview('label867');" title="click to collapse or expand..."> more... </a>
 <div id="label867" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">roaming_acct_interim_update</span> <b>(Alias name: roaming-acct-interim-update)</b>  Enable/disable using accounting interim update instead of accounting start/stop on roaming for wpa-enterprise security. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label868' href="javascript:ContentClick('label869', 'label868');" onmouseover="ContentPreview('label869');" onmouseout="ContentUnpreview('label869');" title="click to collapse or expand..."> more... </a>
 <div id="label869" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sae_hnp_only</span> <b>(Alias name: sae-hnp-only)</b>  Use hunting-and-pecking-only mechanism for pwe derivation (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label870' href="javascript:ContentClick('label871', 'label870');" onmouseover="ContentPreview('label871');" onmouseout="ContentUnpreview('label871');" title="click to collapse or expand..."> more... </a>
 <div id="label871" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">akm24_only</span> <b>(Alias name: akm24-only)</b>  Wpa3 sae using group-dependent hash only (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label872' href="javascript:ContentClick('label873', 'label872');" onmouseover="ContentPreview('label873');" onmouseout="ContentUnpreview('label873');" title="click to collapse or expand..."> more... </a>
 <div id="label873" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">beacon_protection</span> <b>(Alias name: beacon-protection)</b>  Enable/disable beacon protection support (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label874' href="javascript:ContentClick('label875', 'label874');" onmouseover="ContentPreview('label875');" onmouseout="ContentUnpreview('label875');" title="click to collapse or expand..."> more... </a>
 <div id="label875" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal</span> <b>(Alias name: captive-portal)</b>  Enable/disable captive portal. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label876' href="javascript:ContentClick('label877', 'label876');" onmouseover="ContentPreview('label877');" onmouseout="ContentUnpreview('label877');" title="click to collapse or expand..."> more... </a>
 <div id="label877" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nas_filter_rule</span> <b>(Alias name: nas-filter-rule)</b>  Enable/disable nas filter rule support (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label878' href="javascript:ContentClick('label879', 'label878');" onmouseover="ContentPreview('label879');" onmouseout="ContentUnpreview('label879');" title="click to collapse or expand..."> more... </a>
 <div id="label879" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11be_mcs_map</span> <b>(Alias name: rates-11be-mcs-map)</b>  Comma separated list of max nss that supports eht-mcs 0-9, 10-11, 12-13 for 20mhz/40mhz/80mhz bandwidth. <span class="li-normal">type: str</span>
 <a id='label880' href="javascript:ContentClick('label881', 'label880');" onmouseover="ContentPreview('label881');" onmouseout="ContentUnpreview('label881');" title="click to collapse or expand..."> more... </a>
 <div id="label881" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11be_mcs_map_160</span> <b>(Alias name: rates-11be-mcs-map-160)</b>  Comma separated list of max nss that supports eht-mcs 0-9, 10-11, 12-13 for 160mhz bandwidth. <span class="li-normal">type: str</span>
 <a id='label882' href="javascript:ContentClick('label883', 'label882');" onmouseover="ContentPreview('label883');" onmouseout="ContentUnpreview('label883');" title="click to collapse or expand..."> more... </a>
 <div id="label883" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rates_11be_mcs_map_320</span> <b>(Alias name: rates-11be-mcs-map-320)</b>  Comma separated list of max nss that supports eht-mcs 0-9, 10-11, 12-13 for 320mhz bandwidth. <span class="li-normal">type: str</span>
 <a id='label884' href="javascript:ContentClick('label885', 'label884');" onmouseover="ContentPreview('label885');" onmouseout="ContentUnpreview('label885');" title="click to collapse or expand..."> more... </a>
 <div id="label885" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip_managed_by_fortiipam</span> <b>(Alias name: _intf_ip-managed-by-fortiipam)</b>  Intf ip managed by fortiipam. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, inherit-global]</span> 
 <a id='label886' href="javascript:ContentClick('label887', 'label886');" onmouseover="ContentPreview('label887');" onmouseout="ContentUnpreview('label887');" title="click to collapse or expand..."> more... </a>
 <div id="label887" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_managed_subnetwork_size</span> <b>(Alias name: _intf_managed-subnetwork-size)</b>  Intf managed subnetwork size. <span class="li-normal">type: str</span> <span class="li-normal">choices: [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]</span>  <span class="li-normal">default: 256</span> 
 <a id='label888' href="javascript:ContentClick('label889', 'label888');" onmouseover="ContentPreview('label889');" onmouseout="ContentUnpreview('label889');" title="click to collapse or expand..."> more... </a>
 <div id="label889" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">domain_name_stripping</span> <b>(Alias name: domain-name-stripping)</b>  Enable/disable stripping domain name from identity (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label890' href="javascript:ContentClick('label891', 'label890');" onmouseover="ContentPreview('label891');" onmouseout="ContentUnpreview('label891');" title="click to collapse or expand..."> more... </a>
 <div id="label891" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">local_lan_partition</span> <b>(Alias name: local-lan-partition)</b>  Enable/disable segregating client traffic to local lan side (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label892' href="javascript:ContentClick('label893', 'label892');" onmouseover="ContentPreview('label893');" onmouseout="ContentUnpreview('label893');" title="click to collapse or expand..."> more... </a>
 <div id="label893" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_role</span> Intf role. <span class="li-normal">type: str</span> <span class="li-normal">choices: [lan, wan, dmz, undefined]</span>  <span class="li-normal">default: lan</span> 
 <a id='label894' href="javascript:ContentClick('label895', 'label894');" onmouseover="ContentPreview('label895');" onmouseout="ContentUnpreview('label895');" title="click to collapse or expand..."> more... </a>
 <div id="label895" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.6 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">called_station_id_type</span> <b>(Alias name: called-station-id-type)</b>  The format type of radius attribute called-station-id (default = mac). <span class="li-normal">type: str</span> <span class="li-normal">choices: [mac, ip, apname]</span> 
 <a id='label896' href="javascript:ContentClick('label897', 'label896');" onmouseover="ContentPreview('label897');" onmouseout="ContentUnpreview('label897');" title="click to collapse or expand..."> more... </a>
 <div id="label897" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_pre_auth</span> <b>(Alias name: external-pre-auth)</b>  Enable/disable pre-authentication with external aps not managed by the fortigate (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label898' href="javascript:ContentClick('label899', 'label898');" onmouseover="ContentPreview('label899');" onmouseout="ContentUnpreview('label899');" title="click to collapse or expand..."> more... </a>
 <div id="label899" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pre_auth</span> <b>(Alias name: pre-auth)</b>  Enable/disable pre-authentication, where supported by clients (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label900' href="javascript:ContentClick('label901', 'label900');" onmouseover="ContentPreview('label901');" onmouseout="ContentUnpreview('label901');" title="click to collapse or expand..."> more... </a>
 <div id="label901" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_intf_ip6_send_adv</span> <b>(Alias name: _intf_ip6-send-adv)</b>  Intf ip6 send adv. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label902' href="javascript:ContentClick('label903', 'label902');" onmouseover="ContentPreview('label903');" onmouseout="ContentUnpreview('label903');" title="click to collapse or expand..."> more... </a>
 <div id="label903" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_prefix_list</span> <b>(Alias name: ip6-prefix-list)</b>  Ip6 prefix list. <span class="li-normal">type: list</span>
 <a id='label904' href="javascript:ContentClick('label905', 'label904');" onmouseover="ContentPreview('label905');" onmouseout="ContentUnpreview('label905');" title="click to collapse or expand..."> more... </a>
 <div id="label905" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous_flag</span> <b>(Alias name: autonomous-flag)</b>  Autonomous flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label906' href="javascript:ContentClick('label907', 'label906');" onmouseover="ContentPreview('label907');" onmouseout="ContentUnpreview('label907');" title="click to collapse or expand..."> more... </a>
 <div id="label907" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dnssl</span> Dnssl. <span class="li-normal">type: list</span>
 <a id='label908' href="javascript:ContentClick('label909', 'label908');" onmouseover="ContentPreview('label909');" onmouseout="ContentUnpreview('label909');" title="click to collapse or expand..."> more... </a>
 <div id="label909" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">onlink_flag</span> <b>(Alias name: onlink-flag)</b>  Onlink flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label910' href="javascript:ContentClick('label911', 'label910');" onmouseover="ContentPreview('label911');" onmouseout="ContentUnpreview('label911');" title="click to collapse or expand..."> more... </a>
 <div id="label911" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">preferred_life_time</span> <b>(Alias name: preferred-life-time)</b>  Preferred life time. <span class="li-normal">type: int</span>
 <a id='label912' href="javascript:ContentClick('label913', 'label912');" onmouseover="ContentPreview('label913');" onmouseout="ContentUnpreview('label913');" title="click to collapse or expand..."> more... </a>
 <div id="label913" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">prefix</span> Prefix. <span class="li-normal">type: str</span>
 <a id='label914' href="javascript:ContentClick('label915', 'label914');" onmouseover="ContentPreview('label915');" onmouseout="ContentUnpreview('label915');" title="click to collapse or expand..."> more... </a>
 <div id="label915" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> Rdnss. <span class="li-normal">type: list</span>
 <a id='label916' href="javascript:ContentClick('label917', 'label916');" onmouseover="ContentPreview('label917');" onmouseout="ContentUnpreview('label917');" title="click to collapse or expand..."> more... </a>
 <div id="label917" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">valid_life_time</span> <b>(Alias name: valid-life-time)</b>  Valid life time. <span class="li-normal">type: int</span>
 <a id='label918' href="javascript:ContentClick('label919', 'label918');" onmouseover="ContentPreview('label919');" onmouseout="ContentUnpreview('label919');" title="click to collapse or expand..."> more... </a>
 <div id="label919" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.7 -> v7.4.7</code>, <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">_intf_vrf</span> Intf vrf. <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label920' href="javascript:ContentClick('label921', 'label920');" onmouseover="ContentPreview('label921');" onmouseout="ContentUnpreview('label921');" title="click to collapse or expand..."> more... </a>
 <div id="label921" style="display:none">
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
      - name: Configure Virtual Access Points
        fortinet.fortimanager.fmgr_vap:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          state: present # <value in [present, absent]>
          vap:
            name: "your value" # Required variable, string
            # _centmgmt: <value in [disable, enable]>
            # _dhcp_svr_id: <string>
            # _intf_allowaccess:
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
            # _intf_device_identification: <value in [disable, enable]>
            # _intf_device_netscan: <value in [disable, enable]>
            # _intf_dhcp_relay_ip: <list or string>
            # _intf_dhcp_relay_service: <value in [disable, enable]>
            # _intf_dhcp_relay_type: <value in [regular, ipsec]>
            # _intf_dhcp6_relay_ip: <string>
            # _intf_dhcp6_relay_service: <value in [disable, enable]>
            # _intf_dhcp6_relay_type: <value in [regular]>
            # _intf_ip: <string>
            # _intf_ip6_address: <string>
            # _intf_ip6_allowaccess:
            #   - "https"
            #   - "ping"
            #   - "ssh"
            #   - "snmp"
            #   - "http"
            #   - "telnet"
            #   - "any"
            #   - "fgfm"
            #   - "capwap"
            # _intf_listen_forticlient_connection: <value in [disable, enable]>
            # acct_interim_interval: <integer>
            # alias: <string>
            # auth: <value in [PSK, psk, RADIUS, ...]>
            # broadcast_ssid: <value in [disable, enable]>
            # broadcast_suppression:
            #   - "dhcp"
            #   - "arp"
            #   - "dhcp2"
            #   - "arp2"
            #   - "netbios-ns"
            #   - "netbios-ds"
            #   - "arp3"
            #   - "dhcp-up"
            #   - "dhcp-down"
            #   - "arp-known"
            #   - "arp-unknown"
            #   - "arp-reply"
            #   - "ipv6"
            #   - "dhcp-starvation"
            #   - "arp-poison"
            #   - "all-other-mc"
            #   - "all-other-bc"
            #   - "arp-proxy"
            #   - "dhcp-ucast"
            # captive_portal_ac_name: <string>
            # captive_portal_macauth_radius_secret: <list or string>
            # captive_portal_macauth_radius_server: <string>
            # captive_portal_radius_secret: <list or string>
            # captive_portal_radius_server: <string>
            # captive_portal_session_timeout_interval: <integer>
            # dhcp_lease_time: <integer>
            # dhcp_option82_circuit_id_insertion: <value in [disable, style-1, style-2, ...]>
            # dhcp_option82_insertion: <value in [disable, enable]>
            # dhcp_option82_remote_id_insertion: <value in [disable, style-1]>
            # dynamic_vlan: <value in [disable, enable]>
            # dynamic_mapping:
            #   - _centmgmt: <value in [disable, enable]>
            #     _dhcp_svr_id: <string>
            #     _intf_allowaccess:
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
            #     _intf_device_identification: <value in [disable, enable]>
            #     _intf_device_netscan: <value in [disable, enable]>
            #     _intf_dhcp_relay_ip: <list or string>
            #     _intf_dhcp_relay_service: <value in [disable, enable]>
            #     _intf_dhcp_relay_type: <value in [regular, ipsec]>
            #     _intf_dhcp6_relay_ip: <string>
            #     _intf_dhcp6_relay_service: <value in [disable, enable]>
            #     _intf_dhcp6_relay_type: <value in [regular]>
            #     _intf_ip: <string>
            #     _intf_ip6_address: <string>
            #     _intf_ip6_allowaccess:
            #       - "https"
            #       - "ping"
            #       - "ssh"
            #       - "snmp"
            #       - "http"
            #       - "telnet"
            #       - "any"
            #       - "fgfm"
            #       - "capwap"
            #     _intf_listen_forticlient_connection: <value in [disable, enable]>
            #     _scope:
            #       - name: <string>
            #         vdom: <string>
            #     acct_interim_interval: <integer>
            #     address_group: <string>
            #     alias: <string>
            #     atf_weight: <integer>
            #     auth: <value in [PSK, psk, RADIUS, ...]>
            #     broadcast_ssid: <value in [disable, enable]>
            #     broadcast_suppression:
            #       - "dhcp"
            #       - "arp"
            #       - "dhcp2"
            #       - "arp2"
            #       - "netbios-ns"
            #       - "netbios-ds"
            #       - "arp3"
            #       - "dhcp-up"
            #       - "dhcp-down"
            #       - "arp-known"
            #       - "arp-unknown"
            #       - "arp-reply"
            #       - "ipv6"
            #       - "dhcp-starvation"
            #       - "arp-poison"
            #       - "all-other-mc"
            #       - "all-other-bc"
            #       - "arp-proxy"
            #       - "dhcp-ucast"
            #     captive_portal_ac_name: <string>
            #     captive_portal_macauth_radius_secret: <list or string>
            #     captive_portal_macauth_radius_server: <string>
            #     captive_portal_radius_secret: <list or string>
            #     captive_portal_radius_server: <string>
            #     captive_portal_session_timeout_interval: <integer>
            #     client_count: <integer>
            #     dhcp_lease_time: <integer>
            #     dhcp_option82_circuit_id_insertion: <value in [disable, style-1, style-2, ...]>
            #     dhcp_option82_insertion: <value in [disable, enable]>
            #     dhcp_option82_remote_id_insertion: <value in [disable, style-1]>
            #     dynamic_vlan: <value in [disable, enable]>
            #     eap_reauth: <value in [disable, enable]>
            #     eap_reauth_intv: <integer>
            #     eapol_key_retries: <value in [disable, enable]>
            #     encrypt: <value in [TKIP, AES, TKIP-AES]>
            #     external_fast_roaming: <value in [disable, enable]>
            #     external_logout: <string>
            #     external_web: <string>
            #     fast_bss_transition: <value in [disable, enable]>
            #     fast_roaming: <value in [disable, enable]>
            #     ft_mobility_domain: <integer>
            #     ft_over_ds: <value in [disable, enable]>
            #     ft_r0_key_lifetime: <integer>
            #     gtk_rekey: <value in [disable, enable]>
            #     gtk_rekey_intv: <integer>
            #     hotspot20_profile: <string>
            #     intra_vap_privacy: <value in [disable, enable]>
            #     ip: <string>
            #     key: <list or string>
            #     keyindex: <integer>
            #     ldpc: <value in [disable, tx, rx, ...]>
            #     local_authentication: <value in [disable, enable]>
            #     local_bridging: <value in [disable, enable]>
            #     local_lan: <value in [deny, allow]>
            #     local_standalone: <value in [disable, enable]>
            #     local_standalone_nat: <value in [disable, enable]>
            #     local_switching: <value in [disable, enable]>
            #     mac_auth_bypass: <value in [disable, enable]>
            #     mac_filter: <value in [disable, enable]>
            #     mac_filter_policy_other: <value in [deny, allow]>
            #     max_clients: <integer>
            #     max_clients_ap: <integer>
            #     me_disable_thresh: <integer>
            #     mesh_backhaul: <value in [disable, enable]>
            #     mpsk: <value in [disable, enable]>
            #     mpsk_concurrent_clients: <integer>
            #     multicast_enhance: <value in [disable, enable]>
            #     multicast_rate: <value in [0, 6000, 12000, ...]>
            #     okc: <value in [disable, enable]>
            #     owe_groups:
            #       - "19"
            #       - "20"
            #       - "21"
            #     owe_transition: <value in [disable, enable]>
            #     owe_transition_ssid: <string>
            #     passphrase: <list or string>
            #     pmf: <value in [disable, enable, optional]>
            #     pmf_assoc_comeback_timeout: <integer>
            #     pmf_sa_query_retry_timeout: <integer>
            #     portal_message_override_group: <string>
            #     portal_type: <value in [auth, auth+disclaimer, disclaimer, ...]>
            #     probe_resp_suppression: <value in [disable, enable]>
            #     probe_resp_threshold: <string>
            #     ptk_rekey: <value in [disable, enable]>
            #     ptk_rekey_intv: <integer>
            #     qos_profile: <string>
            #     quarantine: <value in [disable, enable]>
            #     radio_2g_threshold: <string>
            #     radio_5g_threshold: <string>
            #     radio_sensitivity: <value in [disable, enable]>
            #     radius_mac_auth: <value in [disable, enable]>
            #     radius_mac_auth_server: <string>
            #     radius_mac_auth_usergroups: <list or string>
            #     radius_server: <string>
            #     rates_11a:
            #       - "1"
            #       - "1-basic"
            #       - "2"
            #       - "2-basic"
            #       - "5.5"
            #       - "5.5-basic"
            #       - "6"
            #       - "6-basic"
            #       - "9"
            #       - "9-basic"
            #       - "12"
            #       - "12-basic"
            #       - "18"
            #       - "18-basic"
            #       - "24"
            #       - "24-basic"
            #       - "36"
            #       - "36-basic"
            #       - "48"
            #       - "48-basic"
            #       - "54"
            #       - "54-basic"
            #       - "11"
            #       - "11-basic"
            #     rates_11ac_ss12:
            #       - "mcs0/1"
            #       - "mcs1/1"
            #       - "mcs2/1"
            #       - "mcs3/1"
            #       - "mcs4/1"
            #       - "mcs5/1"
            #       - "mcs6/1"
            #       - "mcs7/1"
            #       - "mcs8/1"
            #       - "mcs9/1"
            #       - "mcs0/2"
            #       - "mcs1/2"
            #       - "mcs2/2"
            #       - "mcs3/2"
            #       - "mcs4/2"
            #       - "mcs5/2"
            #       - "mcs6/2"
            #       - "mcs7/2"
            #       - "mcs8/2"
            #       - "mcs9/2"
            #       - "mcs10/1"
            #       - "mcs11/1"
            #       - "mcs10/2"
            #       - "mcs11/2"
            #     rates_11ac_ss34:
            #       - "mcs0/3"
            #       - "mcs1/3"
            #       - "mcs2/3"
            #       - "mcs3/3"
            #       - "mcs4/3"
            #       - "mcs5/3"
            #       - "mcs6/3"
            #       - "mcs7/3"
            #       - "mcs8/3"
            #       - "mcs9/3"
            #       - "mcs0/4"
            #       - "mcs1/4"
            #       - "mcs2/4"
            #       - "mcs3/4"
            #       - "mcs4/4"
            #       - "mcs5/4"
            #       - "mcs6/4"
            #       - "mcs7/4"
            #       - "mcs8/4"
            #       - "mcs9/4"
            #       - "mcs10/3"
            #       - "mcs11/3"
            #       - "mcs10/4"
            #       - "mcs11/4"
            #     rates_11bg:
            #       - "1"
            #       - "1-basic"
            #       - "2"
            #       - "2-basic"
            #       - "5.5"
            #       - "5.5-basic"
            #       - "6"
            #       - "6-basic"
            #       - "9"
            #       - "9-basic"
            #       - "12"
            #       - "12-basic"
            #       - "18"
            #       - "18-basic"
            #       - "24"
            #       - "24-basic"
            #       - "36"
            #       - "36-basic"
            #       - "48"
            #       - "48-basic"
            #       - "54"
            #       - "54-basic"
            #       - "11"
            #       - "11-basic"
            #     rates_11n_ss12:
            #       - "mcs0/1"
            #       - "mcs1/1"
            #       - "mcs2/1"
            #       - "mcs3/1"
            #       - "mcs4/1"
            #       - "mcs5/1"
            #       - "mcs6/1"
            #       - "mcs7/1"
            #       - "mcs8/2"
            #       - "mcs9/2"
            #       - "mcs10/2"
            #       - "mcs11/2"
            #       - "mcs12/2"
            #       - "mcs13/2"
            #       - "mcs14/2"
            #       - "mcs15/2"
            #     rates_11n_ss34:
            #       - "mcs16/3"
            #       - "mcs17/3"
            #       - "mcs18/3"
            #       - "mcs19/3"
            #       - "mcs20/3"
            #       - "mcs21/3"
            #       - "mcs22/3"
            #       - "mcs23/3"
            #       - "mcs24/4"
            #       - "mcs25/4"
            #       - "mcs26/4"
            #       - "mcs27/4"
            #       - "mcs28/4"
            #       - "mcs29/4"
            #       - "mcs30/4"
            #       - "mcs31/4"
            #     sae_groups:
            #       - "1"
            #       - "2"
            #       - "5"
            #       - "14"
            #       - "15"
            #       - "16"
            #       - "17"
            #       - "18"
            #       - "19"
            #       - "20"
            #       - "21"
            #       - "27"
            #       - "28"
            #       - "29"
            #       - "30"
            #       - "31"
            #     sae_password: <list or string>
            #     schedule: <list or string>
            #     security: <value in [None, WEP64, wep64, ...]>
            #     security_exempt_list: <string>
            #     security_obsolete_option: <value in [disable, enable]>
            #     security_redirect_url: <string>
            #     selected_usergroups: <list or string>
            #     split_tunneling: <value in [disable, enable]>
            #     ssid: <string>
            #     tkip_counter_measure: <value in [disable, enable]>
            #     usergroup: <list or string>
            #     utm_profile: <string>
            #     vdom: <list or string>
            #     vlan_auto: <value in [disable, enable]>
            #     vlan_pooling: <value in [wtp-group, round-robin, hash, ...]>
            #     vlanid: <integer>
            #     voice_enterprise: <value in [disable, enable]>
            #     mu_mimo: <value in [disable, enable]>
            #     _intf_device_access_list: <string>
            #     external_web_format: <value in [auto-detect, no-query-string, partial-query-string]>
            #     high_efficiency: <value in [disable, enable]>
            #     primary_wag_profile: <string>
            #     secondary_wag_profile: <string>
            #     target_wake_time: <value in [disable, enable]>
            #     tunnel_echo_interval: <integer>
            #     tunnel_fallback_interval: <integer>
            #     access_control_list: <string>
            #     captive_portal_auth_timeout: <integer>
            #     ipv6_rules:
            #       - "drop-icmp6ra"
            #       - "drop-icmp6rs"
            #       - "drop-llmnr6"
            #       - "drop-icmp6mld2"
            #       - "drop-dhcp6s"
            #       - "drop-dhcp6c"
            #       - "ndp-proxy"
            #       - "drop-ns-dad"
            #       - "drop-ns-nondad"
            #     sticky_client_remove: <value in [disable, enable]>
            #     sticky_client_threshold_2g: <string>
            #     sticky_client_threshold_5g: <string>
            #     bss_color_partial: <value in [disable, enable]>
            #     dhcp_option43_insertion: <value in [disable, enable]>
            #     mpsk_profile: <string>
            #     igmp_snooping: <value in [disable, enable]>
            #     port_macauth: <value in [disable, radius, address-group]>
            #     port_macauth_reauth_timeout: <integer>
            #     port_macauth_timeout: <integer>
            #     additional_akms:
            #       - "akm6"
            #       - "akm24"
            #     bstm_disassociation_imminent: <value in [disable, enable]>
            #     bstm_load_balancing_disassoc_timer: <integer>
            #     bstm_rssi_disassoc_timer: <integer>
            #     dhcp_address_enforcement: <value in [disable, enable]>
            #     gas_comeback_delay: <integer>
            #     gas_fragmentation_limit: <integer>
            #     mac_called_station_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            #     mac_calling_station_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            #     mac_case: <value in [uppercase, lowercase]>
            #     mac_password_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            #     mac_username_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            #     mbo: <value in [disable, enable]>
            #     mbo_cell_data_conn_pref: <value in [excluded, prefer-not, prefer-use]>
            #     nac: <value in [disable, enable]>
            #     nac_profile: <string>
            #     neighbor_report_dual_band: <value in [disable, enable]>
            #     address_group_policy: <value in [disable, allow, deny]>
            #     antivirus_profile: <string>
            #     application_detection_engine: <value in [disable, enable]>
            #     application_list: <string>
            #     application_report_intv: <integer>
            #     auth_cert: <string>
            #     auth_portal_addr: <string>
            #     beacon_advertising:
            #       - "name"
            #       - "model"
            #       - "serial-number"
            #     ips_sensor: <string>
            #     l3_roaming: <value in [disable, enable]>
            #     local_standalone_dns: <value in [disable, enable]>
            #     local_standalone_dns_ip: <list or string>
            #     osen: <value in [disable, enable]>
            #     radius_mac_mpsk_auth: <value in [disable, enable]>
            #     radius_mac_mpsk_timeout: <integer>
            #     rates_11ax_ss12:
            #       - "mcs0/1"
            #       - "mcs1/1"
            #       - "mcs2/1"
            #       - "mcs3/1"
            #       - "mcs4/1"
            #       - "mcs5/1"
            #       - "mcs6/1"
            #       - "mcs7/1"
            #       - "mcs8/1"
            #       - "mcs9/1"
            #       - "mcs10/1"
            #       - "mcs11/1"
            #       - "mcs0/2"
            #       - "mcs1/2"
            #       - "mcs2/2"
            #       - "mcs3/2"
            #       - "mcs4/2"
            #       - "mcs5/2"
            #       - "mcs6/2"
            #       - "mcs7/2"
            #       - "mcs8/2"
            #       - "mcs9/2"
            #       - "mcs10/2"
            #       - "mcs11/2"
            #     rates_11ax_ss34:
            #       - "mcs0/3"
            #       - "mcs1/3"
            #       - "mcs2/3"
            #       - "mcs3/3"
            #       - "mcs4/3"
            #       - "mcs5/3"
            #       - "mcs6/3"
            #       - "mcs7/3"
            #       - "mcs8/3"
            #       - "mcs9/3"
            #       - "mcs10/3"
            #       - "mcs11/3"
            #       - "mcs0/4"
            #       - "mcs1/4"
            #       - "mcs2/4"
            #       - "mcs3/4"
            #       - "mcs4/4"
            #       - "mcs5/4"
            #       - "mcs6/4"
            #       - "mcs7/4"
            #       - "mcs8/4"
            #       - "mcs9/4"
            #       - "mcs10/4"
            #       - "mcs11/4"
            #     scan_botnet_connections: <value in [disable, block, monitor]>
            #     utm_log: <value in [disable, enable]>
            #     utm_status: <value in [disable, enable]>
            #     webfilter_profile: <string>
            #     sae_h2e_only: <value in [disable, enable]>
            #     sae_pk: <value in [disable, enable]>
            #     sae_private_key: <string>
            #     sticky_client_threshold_6g: <string>
            #     application_dscp_marking: <value in [disable, enable]>
            #     l3_roaming_mode: <value in [direct, indirect]>
            #     rates_11ac_mcs_map: <string>
            #     rates_11ax_mcs_map: <string>
            #     captive_portal_fw_accounting: <value in [disable, enable]>
            #     radius_mac_auth_block_interval: <integer>
            #     _is_factory_setting: <value in [disable, enable, ext]>
            #     d80211k: <value in [disable, enable]>
            #     d80211v: <value in [disable, enable]>
            #     roaming_acct_interim_update: <value in [disable, enable]>
            #     sae_hnp_only: <value in [disable, enable]>
            #     akm24_only: <value in [disable, enable]>
            #     beacon_protection: <value in [disable, enable]>
            #     captive_portal: <value in [disable, enable]>
            #     nas_filter_rule: <value in [disable, enable]>
            #     rates_11be_mcs_map: <string>
            #     rates_11be_mcs_map_160: <string>
            #     rates_11be_mcs_map_320: <string>
            #     _intf_ip_managed_by_fortiipam: <value in [disable, enable, inherit-global]>
            #     _intf_managed_subnetwork_size: <value in [32, 64, 128, ...]>
            #     domain_name_stripping: <value in [disable, enable]>
            #     local_lan_partition: <value in [disable, enable]>
            #     _intf_role: <value in [lan, wan, dmz, ...]>
            #     called_station_id_type: <value in [mac, ip, apname]>
            #     external_pre_auth: <value in [disable, enable]>
            #     pre_auth: <value in [disable, enable]>
            #     _intf_ip6_send_adv: <value in [disable, enable]>
            #     ip6_prefix_list:
            #       - autonomous_flag: <value in [disable, enable]>
            #         dnssl: <list or string>
            #         onlink_flag: <value in [disable, enable]>
            #         preferred_life_time: <integer>
            #         prefix: <string>
            #         rdnss: <list or string>
            #         valid_life_time: <integer>
            #     _intf_vrf: <integer>
            # eap_reauth: <value in [disable, enable]>
            # eap_reauth_intv: <integer>
            # eapol_key_retries: <value in [disable, enable]>
            # encrypt: <value in [TKIP, AES, TKIP-AES]>
            # external_fast_roaming: <value in [disable, enable]>
            # external_logout: <string>
            # external_web: <string>
            # fast_bss_transition: <value in [disable, enable]>
            # fast_roaming: <value in [disable, enable]>
            # ft_mobility_domain: <integer>
            # ft_over_ds: <value in [disable, enable]>
            # ft_r0_key_lifetime: <integer>
            # gtk_rekey: <value in [disable, enable]>
            # gtk_rekey_intv: <integer>
            # hotspot20_profile: <string>
            # intra_vap_privacy: <value in [disable, enable]>
            # ip: <string>
            # key: <list or string>
            # keyindex: <integer>
            # ldpc: <value in [disable, tx, rx, ...]>
            # local_authentication: <value in [disable, enable]>
            # local_bridging: <value in [disable, enable]>
            # local_lan: <value in [deny, allow]>
            # local_standalone: <value in [disable, enable]>
            # local_standalone_nat: <value in [disable, enable]>
            # mac_auth_bypass: <value in [disable, enable]>
            # mac_filter: <value in [disable, enable]>
            # mac_filter_list:
            #   - id: <integer>
            #     mac: <string>
            #     mac_filter_policy: <value in [deny, allow]>
            # mac_filter_policy_other: <value in [deny, allow]>
            # max_clients: <integer>
            # max_clients_ap: <integer>
            # me_disable_thresh: <integer>
            # mesh_backhaul: <value in [disable, enable]>
            # mpsk: <value in [disable, enable]>
            # mpsk_concurrent_clients: <integer>
            # mpsk_key:
            #   - comment: <string>
            #     concurrent_clients: <string>
            #     key_name: <string>
            #     passphrase: <list or string>
            #     mpsk_schedules: <list or string>
            # multicast_enhance: <value in [disable, enable]>
            # multicast_rate: <value in [0, 6000, 12000, ...]>
            # okc: <value in [disable, enable]>
            # passphrase: <list or string>
            # pmf: <value in [disable, enable, optional]>
            # pmf_assoc_comeback_timeout: <integer>
            # pmf_sa_query_retry_timeout: <integer>
            # portal_message_override_group: <string>
            # portal_type: <value in [auth, auth+disclaimer, disclaimer, ...]>
            # probe_resp_suppression: <value in [disable, enable]>
            # probe_resp_threshold: <string>
            # ptk_rekey: <value in [disable, enable]>
            # ptk_rekey_intv: <integer>
            # qos_profile: <string>
            # quarantine: <value in [disable, enable]>
            # radio_2g_threshold: <string>
            # radio_5g_threshold: <string>
            # radio_sensitivity: <value in [disable, enable]>
            # radius_mac_auth: <value in [disable, enable]>
            # radius_mac_auth_server: <string>
            # radius_mac_auth_usergroups: <list or string>
            # radius_server: <string>
            # rates_11a:
            #   - "1"
            #   - "1-basic"
            #   - "2"
            #   - "2-basic"
            #   - "5.5"
            #   - "5.5-basic"
            #   - "6"
            #   - "6-basic"
            #   - "9"
            #   - "9-basic"
            #   - "12"
            #   - "12-basic"
            #   - "18"
            #   - "18-basic"
            #   - "24"
            #   - "24-basic"
            #   - "36"
            #   - "36-basic"
            #   - "48"
            #   - "48-basic"
            #   - "54"
            #   - "54-basic"
            #   - "11"
            #   - "11-basic"
            # rates_11ac_ss12:
            #   - "mcs0/1"
            #   - "mcs1/1"
            #   - "mcs2/1"
            #   - "mcs3/1"
            #   - "mcs4/1"
            #   - "mcs5/1"
            #   - "mcs6/1"
            #   - "mcs7/1"
            #   - "mcs8/1"
            #   - "mcs9/1"
            #   - "mcs0/2"
            #   - "mcs1/2"
            #   - "mcs2/2"
            #   - "mcs3/2"
            #   - "mcs4/2"
            #   - "mcs5/2"
            #   - "mcs6/2"
            #   - "mcs7/2"
            #   - "mcs8/2"
            #   - "mcs9/2"
            #   - "mcs10/1"
            #   - "mcs11/1"
            #   - "mcs10/2"
            #   - "mcs11/2"
            # rates_11ac_ss34:
            #   - "mcs0/3"
            #   - "mcs1/3"
            #   - "mcs2/3"
            #   - "mcs3/3"
            #   - "mcs4/3"
            #   - "mcs5/3"
            #   - "mcs6/3"
            #   - "mcs7/3"
            #   - "mcs8/3"
            #   - "mcs9/3"
            #   - "mcs0/4"
            #   - "mcs1/4"
            #   - "mcs2/4"
            #   - "mcs3/4"
            #   - "mcs4/4"
            #   - "mcs5/4"
            #   - "mcs6/4"
            #   - "mcs7/4"
            #   - "mcs8/4"
            #   - "mcs9/4"
            #   - "mcs10/3"
            #   - "mcs11/3"
            #   - "mcs10/4"
            #   - "mcs11/4"
            # rates_11bg:
            #   - "1"
            #   - "1-basic"
            #   - "2"
            #   - "2-basic"
            #   - "5.5"
            #   - "5.5-basic"
            #   - "6"
            #   - "6-basic"
            #   - "9"
            #   - "9-basic"
            #   - "12"
            #   - "12-basic"
            #   - "18"
            #   - "18-basic"
            #   - "24"
            #   - "24-basic"
            #   - "36"
            #   - "36-basic"
            #   - "48"
            #   - "48-basic"
            #   - "54"
            #   - "54-basic"
            #   - "11"
            #   - "11-basic"
            # rates_11n_ss12:
            #   - "mcs0/1"
            #   - "mcs1/1"
            #   - "mcs2/1"
            #   - "mcs3/1"
            #   - "mcs4/1"
            #   - "mcs5/1"
            #   - "mcs6/1"
            #   - "mcs7/1"
            #   - "mcs8/2"
            #   - "mcs9/2"
            #   - "mcs10/2"
            #   - "mcs11/2"
            #   - "mcs12/2"
            #   - "mcs13/2"
            #   - "mcs14/2"
            #   - "mcs15/2"
            # rates_11n_ss34:
            #   - "mcs16/3"
            #   - "mcs17/3"
            #   - "mcs18/3"
            #   - "mcs19/3"
            #   - "mcs20/3"
            #   - "mcs21/3"
            #   - "mcs22/3"
            #   - "mcs23/3"
            #   - "mcs24/4"
            #   - "mcs25/4"
            #   - "mcs26/4"
            #   - "mcs27/4"
            #   - "mcs28/4"
            #   - "mcs29/4"
            #   - "mcs30/4"
            #   - "mcs31/4"
            # schedule: <list or string>
            # security: <value in [None, WEP64, wep64, ...]>
            # security_exempt_list: <string>
            # security_obsolete_option: <value in [disable, enable]>
            # security_redirect_url: <string>
            # selected_usergroups: <list or string>
            # split_tunneling: <value in [disable, enable]>
            # ssid: <string>
            # tkip_counter_measure: <value in [disable, enable]>
            # usergroup: <list or string>
            # utm_profile: <string>
            # vdom: <string>
            # vlan_auto: <value in [disable, enable]>
            # vlan_pool:
            #   - _wtp_group: <string>
            #     id: <integer>
            #     wtp_group: <string>
            # vlan_pooling: <value in [wtp-group, round-robin, hash, ...]>
            # vlanid: <integer>
            # voice_enterprise: <value in [disable, enable]>
            # address_group: <string>
            # atf_weight: <integer>
            # mu_mimo: <value in [disable, enable]>
            # owe_groups:
            #   - "19"
            #   - "20"
            #   - "21"
            # owe_transition: <value in [disable, enable]>
            # owe_transition_ssid: <string>
            # sae_groups:
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
            # sae_password: <list or string>
            # _intf_device_access_list: <string>
            # external_web_format: <value in [auto-detect, no-query-string, partial-query-string]>
            # high_efficiency: <value in [disable, enable]>
            # primary_wag_profile: <string>
            # secondary_wag_profile: <string>
            # target_wake_time: <value in [disable, enable]>
            # tunnel_echo_interval: <integer>
            # tunnel_fallback_interval: <integer>
            # access_control_list: <string>
            # captive_portal_auth_timeout: <integer>
            # ipv6_rules:
            #   - "drop-icmp6ra"
            #   - "drop-icmp6rs"
            #   - "drop-llmnr6"
            #   - "drop-icmp6mld2"
            #   - "drop-dhcp6s"
            #   - "drop-dhcp6c"
            #   - "ndp-proxy"
            #   - "drop-ns-dad"
            #   - "drop-ns-nondad"
            # sticky_client_remove: <value in [disable, enable]>
            # sticky_client_threshold_2g: <string>
            # sticky_client_threshold_5g: <string>
            # bss_color_partial: <value in [disable, enable]>
            # dhcp_option43_insertion: <value in [disable, enable]>
            # mpsk_profile: <string>
            # igmp_snooping: <value in [disable, enable]>
            # port_macauth: <value in [disable, radius, address-group]>
            # port_macauth_reauth_timeout: <integer>
            # port_macauth_timeout: <integer>
            # portal_message_overrides:
            #   auth_disclaimer_page: <string>
            #   auth_login_failed_page: <string>
            #   auth_login_page: <string>
            #   auth_reject_page: <string>
            # additional_akms:
            #   - "akm6"
            #   - "akm24"
            # bstm_disassociation_imminent: <value in [disable, enable]>
            # bstm_load_balancing_disassoc_timer: <integer>
            # bstm_rssi_disassoc_timer: <integer>
            # dhcp_address_enforcement: <value in [disable, enable]>
            # gas_comeback_delay: <integer>
            # gas_fragmentation_limit: <integer>
            # mac_called_station_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            # mac_calling_station_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            # mac_case: <value in [uppercase, lowercase]>
            # mac_password_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            # mac_username_delimiter: <value in [hyphen, single-hyphen, colon, ...]>
            # mbo: <value in [disable, enable]>
            # mbo_cell_data_conn_pref: <value in [excluded, prefer-not, prefer-use]>
            # nac: <value in [disable, enable]>
            # nac_profile: <string>
            # neighbor_report_dual_band: <value in [disable, enable]>
            # address_group_policy: <value in [disable, allow, deny]>
            # antivirus_profile: <string>
            # application_detection_engine: <value in [disable, enable]>
            # application_list: <string>
            # application_report_intv: <integer>
            # auth_cert: <string>
            # auth_portal_addr: <string>
            # beacon_advertising:
            #   - "name"
            #   - "model"
            #   - "serial-number"
            # ips_sensor: <string>
            # l3_roaming: <value in [disable, enable]>
            # local_standalone_dns: <value in [disable, enable]>
            # local_standalone_dns_ip: <list or string>
            # osen: <value in [disable, enable]>
            # radius_mac_mpsk_auth: <value in [disable, enable]>
            # radius_mac_mpsk_timeout: <integer>
            # rates_11ax_ss12:
            #   - "mcs0/1"
            #   - "mcs1/1"
            #   - "mcs2/1"
            #   - "mcs3/1"
            #   - "mcs4/1"
            #   - "mcs5/1"
            #   - "mcs6/1"
            #   - "mcs7/1"
            #   - "mcs8/1"
            #   - "mcs9/1"
            #   - "mcs10/1"
            #   - "mcs11/1"
            #   - "mcs0/2"
            #   - "mcs1/2"
            #   - "mcs2/2"
            #   - "mcs3/2"
            #   - "mcs4/2"
            #   - "mcs5/2"
            #   - "mcs6/2"
            #   - "mcs7/2"
            #   - "mcs8/2"
            #   - "mcs9/2"
            #   - "mcs10/2"
            #   - "mcs11/2"
            # rates_11ax_ss34:
            #   - "mcs0/3"
            #   - "mcs1/3"
            #   - "mcs2/3"
            #   - "mcs3/3"
            #   - "mcs4/3"
            #   - "mcs5/3"
            #   - "mcs6/3"
            #   - "mcs7/3"
            #   - "mcs8/3"
            #   - "mcs9/3"
            #   - "mcs10/3"
            #   - "mcs11/3"
            #   - "mcs0/4"
            #   - "mcs1/4"
            #   - "mcs2/4"
            #   - "mcs3/4"
            #   - "mcs4/4"
            #   - "mcs5/4"
            #   - "mcs6/4"
            #   - "mcs7/4"
            #   - "mcs8/4"
            #   - "mcs9/4"
            #   - "mcs10/4"
            #   - "mcs11/4"
            # scan_botnet_connections: <value in [disable, block, monitor]>
            # utm_log: <value in [disable, enable]>
            # utm_status: <value in [disable, enable]>
            # vlan_name:
            #   - name: <string>
            #     vlan_id: <integer>
            # webfilter_profile: <string>
            # sae_h2e_only: <value in [disable, enable]>
            # sae_pk: <value in [disable, enable]>
            # sae_private_key: <string>
            # sticky_client_threshold_6g: <string>
            # application_dscp_marking: <value in [disable, enable]>
            # l3_roaming_mode: <value in [direct, indirect]>
            # rates_11ac_mcs_map: <string>
            # rates_11ax_mcs_map: <string>
            # captive_portal_fw_accounting: <value in [disable, enable]>
            # radius_mac_auth_block_interval: <integer>
            # _is_factory_setting: <value in [disable, enable, ext]>
            # d80211k: <value in [disable, enable]>
            # d80211v: <value in [disable, enable]>
            # roaming_acct_interim_update: <value in [disable, enable]>
            # sae_hnp_only: <value in [disable, enable]>
            # akm24_only: <value in [disable, enable]>
            # beacon_protection: <value in [disable, enable]>
            # captive_portal: <value in [disable, enable]>
            # nas_filter_rule: <value in [disable, enable]>
            # rates_11be_mcs_map: <string>
            # rates_11be_mcs_map_160: <string>
            # rates_11be_mcs_map_320: <string>
            # _intf_ip_managed_by_fortiipam: <value in [disable, enable, inherit-global]>
            # _intf_managed_subnetwork_size: <value in [32, 64, 128, ...]>
            # domain_name_stripping: <value in [disable, enable]>
            # local_lan_partition: <value in [disable, enable]>
            # _intf_role: <value in [lan, wan, dmz, ...]>
            # called_station_id_type: <value in [mac, ip, apname]>
            # external_pre_auth: <value in [disable, enable]>
            # pre_auth: <value in [disable, enable]>
            # _intf_ip6_send_adv: <value in [disable, enable]>
            # ip6_prefix_list:
            #   - autonomous_flag: <value in [disable, enable]>
            #     dnssl: <list or string>
            #     onlink_flag: <value in [disable, enable]>
            #     preferred_life_time: <integer>
            #     prefix: <string>
            #     rdnss: <list or string>
            #     valid_life_time: <integer>
            # _intf_vrf: <integer>


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
