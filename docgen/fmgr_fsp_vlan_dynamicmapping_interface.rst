:source: fmgr_fsp_vlan_dynamicmapping_interface.py

:orphan:

.. _fmgr_fsp_vlan_dynamicmapping_interface:

fmgr_fsp_vlan_dynamicmapping_interface -- Fsp vlan dynamic mapping interface.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>



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
 <li><span class="li-head">dynamic_mapping</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">fsp_vlan_dynamicmapping_interface</span> - Fsp vlan dynamic mapping interface <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ip</span> Ip. <span class="li-normal">type: str</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vlanid</span> Vlanid. <span class="li-normal">type: int</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_agent_option</span> <b>(Alias name: dhcp-relay-agent-option)</b>  Dhcp relay agent option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_ip</span> <b>(Alias name: dhcp-relay-ip)</b>  Dhcp relay ip. <span class="li-normal">type: list</span>
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_service</span> <b>(Alias name: dhcp-relay-service)</b>  Dhcp relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp_relay_type</span> <b>(Alias name: dhcp-relay-type)</b>  Dhcp relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular, ipsec]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ipv6</span> Ipv6. <span class="li-normal">type: dict</span>
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autoconf</span> Autoconf. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_client_options</span> <b>(Alias name: dhcp6-client-options)</b>  Dhcp6 client options. <span class="li-normal">type: list</span> <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_information_request</span> <b>(Alias name: dhcp6-information-request)</b>  Dhcp6 information request. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_delegation</span> <b>(Alias name: dhcp6-prefix-delegation)</b>  Dhcp6 prefix delegation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_hint</span> <b>(Alias name: dhcp6-prefix-hint)</b>  Dhcp6 prefix hint. <span class="li-normal">type: str</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_hint_plt</span> <b>(Alias name: dhcp6-prefix-hint-plt)</b>  Dhcp6 prefix hint plt. <span class="li-normal">type: int</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_prefix_hint_vlt</span> <b>(Alias name: dhcp6-prefix-hint-vlt)</b>  Dhcp6 prefix hint vlt. <span class="li-normal">type: int</span>
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_ip</span> <b>(Alias name: dhcp6-relay-ip)</b>  Dhcp6 relay ip. <span class="li-normal">type: str</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_service</span> <b>(Alias name: dhcp6-relay-service)</b>  Dhcp6 relay service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_type</span> <b>(Alias name: dhcp6-relay-type)</b>  Dhcp6 relay type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [regular]</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_address</span> <b>(Alias name: ip6-address)</b>  Ip6 address. <span class="li-normal">type: str</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_allowaccess</span> <b>(Alias name: ip6-allowaccess)</b>  Ip6 allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_default_life</span> <b>(Alias name: ip6-default-life)</b>  Ip6 default life. <span class="li-normal">type: int</span>
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_delegated_prefix_list</span> <b>(Alias name: ip6-delegated-prefix-list)</b>  Ip6 delegated prefix list. <span class="li-normal">type: list</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous_flag</span> <b>(Alias name: autonomous-flag)</b>  Autonomous flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">onlink_flag</span> <b>(Alias name: onlink-flag)</b>  Onlink flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">prefix_id</span> <b>(Alias name: prefix-id)</b>  Prefix id. <span class="li-normal">type: int</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> Rdnss. <span class="li-normal">type: list</span>
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss_service</span> <b>(Alias name: rdnss-service)</b>  Rdnss service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [delegated, default, specify]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">subnet</span> Subnet. <span class="li-normal">type: str</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">upstream_interface</span> <b>(Alias name: upstream-interface)</b>  Upstream interface. <span class="li-normal">type: str</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">delegated_prefix_iaid</span> <b>(Alias name: delegated-prefix-iaid)</b>  Iaid of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ip6_dns_server_override</span> <b>(Alias name: ip6-dns-server-override)</b>  Ip6 dns server override. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_extra_addr</span> <b>(Alias name: ip6-extra-addr)</b>  Ip6 extra addr. <span class="li-normal">type: list</span>
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">prefix</span> Prefix. <span class="li-normal">type: str</span>
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ip6_hop_limit</span> <b>(Alias name: ip6-hop-limit)</b>  Ip6 hop limit. <span class="li-normal">type: int</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_link_mtu</span> <b>(Alias name: ip6-link-mtu)</b>  Ip6 link mtu. <span class="li-normal">type: int</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_manage_flag</span> <b>(Alias name: ip6-manage-flag)</b>  Ip6 manage flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_max_interval</span> <b>(Alias name: ip6-max-interval)</b>  Ip6 max interval. <span class="li-normal">type: int</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_min_interval</span> <b>(Alias name: ip6-min-interval)</b>  Ip6 min interval. <span class="li-normal">type: int</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_mode</span> <b>(Alias name: ip6-mode)</b>  Ip6 mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_other_flag</span> <b>(Alias name: ip6-other-flag)</b>  Ip6 other flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_prefix_list</span> <b>(Alias name: ip6-prefix-list)</b>  Ip6 prefix list. <span class="li-normal">type: list</span>
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous_flag</span> <b>(Alias name: autonomous-flag)</b>  Autonomous flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dnssl</span> Dnssl. <span class="li-normal">type: list</span>
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">onlink_flag</span> <b>(Alias name: onlink-flag)</b>  Onlink flag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">preferred_life_time</span> <b>(Alias name: preferred-life-time)</b>  Preferred life time. <span class="li-normal">type: int</span>
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">prefix</span> Prefix. <span class="li-normal">type: str</span>
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> Rdnss. <span class="li-normal">type: list</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">valid_life_time</span> <b>(Alias name: valid-life-time)</b>  Valid life time. <span class="li-normal">type: int</span>
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ip6_reachable_time</span> <b>(Alias name: ip6-reachable-time)</b>  Ip6 reachable time. <span class="li-normal">type: int</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_retrans_time</span> <b>(Alias name: ip6-retrans-time)</b>  Ip6 retrans time. <span class="li-normal">type: int</span>
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_send_adv</span> <b>(Alias name: ip6-send-adv)</b>  Ip6 send adv. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_subnet</span> <b>(Alias name: ip6-subnet)</b>  Ip6 subnet. <span class="li-normal">type: str</span>
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_upstream_interface</span> <b>(Alias name: ip6-upstream-interface)</b>  Ip6 upstream interface. <span class="li-normal">type: str</span>
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_cert</span> <b>(Alias name: nd-cert)</b>  Nd cert. <span class="li-normal">type: str</span>
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_cga_modifier</span> <b>(Alias name: nd-cga-modifier)</b>  Nd cga modifier. <span class="li-normal">type: str</span>
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_mode</span> <b>(Alias name: nd-mode)</b>  Nd mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [basic, SEND-compatible]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_security_level</span> <b>(Alias name: nd-security-level)</b>  Nd security level. <span class="li-normal">type: int</span>
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_timestamp_delta</span> <b>(Alias name: nd-timestamp-delta)</b>  Nd timestamp delta. <span class="li-normal">type: int</span>
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">nd_timestamp_fuzz</span> <b>(Alias name: nd-timestamp-fuzz)</b>  Nd timestamp fuzz. <span class="li-normal">type: int</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrip6_link_local</span> Vrip6 link local. <span class="li-normal">type: str</span>
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrrp_virtual_mac6</span> <b>(Alias name: vrrp-virtual-mac6)</b>  Vrrp virtual mac6. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrrp6</span> Vrrp6. <span class="li-normal">type: list</span>
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">accept_mode</span> <b>(Alias name: accept-mode)</b>  Accept mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">adv_interval</span> <b>(Alias name: adv-interval)</b>  Adv interval. <span class="li-normal">type: int</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">preempt</span> Preempt. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Priority. <span class="li-normal">type: int</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">start_time</span> <b>(Alias name: start-time)</b>  Start time. <span class="li-normal">type: int</span>
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrdst6</span> Vrdst6. <span class="li-normal">type: str</span>
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrgrp</span> Vrgrp. <span class="li-normal">type: int</span>
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrid</span> Vrid. <span class="li-normal">type: int</span>
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrip6</span> Vrip6. <span class="li-normal">type: str</span>
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">interface_identifier</span> <b>(Alias name: interface-identifier)</b>  Interface identifier. <span class="li-normal">type: str</span>
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">unique_autoconf_addr</span> <b>(Alias name: unique-autoconf-addr)</b>  Unique autoconf addr. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">icmp6_send_redirect</span> <b>(Alias name: icmp6-send-redirect)</b>  Enable/disable sending of icmpv6 redirects. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.4 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">cli_conn6_status</span> <b>(Alias name: cli-conn6-status)</b>  Cli conn6 status. <span class="li-normal">type: int</span>
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_prefix_mode</span> <b>(Alias name: ip6-prefix-mode)</b>  Assigning a prefix from dhcp or ra. <span class="li-normal">type: str</span> <span class="li-normal">choices: [dhcp6, ra]</span> 
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ra_send_mtu</span> <b>(Alias name: ra-send-mtu)</b>  Enable/disable sending link mtu in ra packet. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.6 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip6_delegated_prefix_iaid</span> <b>(Alias name: ip6-delegated-prefix-iaid)</b>  Iaid of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">dhcp6_relay_source_interface</span> <b>(Alias name: dhcp6-relay-source-interface)</b>  Enable/disable use of address on this interface as the source address of the relay message. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">secondary_IP</span> <b>(Alias name: secondary-IP)</b>  Secondary ip. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">secondaryip</span> Secondaryip. <span class="li-normal">type: list</span>
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> Allowaccess. <span class="li-normal">type: list</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">detectprotocol</span> Detectprotocol. <span class="li-normal">type: list</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">detectserver</span> Detectserver. <span class="li-normal">type: str</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">gwdetect</span> Gwdetect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ha_priority</span> <b>(Alias name: ha-priority)</b>  Ha priority. <span class="li-normal">type: int</span>
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ip. <span class="li-normal">type: str</span>
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ping_serv_status</span> <b>(Alias name: ping-serv-status)</b>  Ping serv status. <span class="li-normal">type: int</span>
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.0</code></p>
 </div>
 </li>
 <li><span class="li-head">seq</span> Seq. <span class="li-normal">type: int</span>
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">secip_relay_ip</span> <b>(Alias name: secip-relay-ip)</b>  Dhcp relay ip address. <span class="li-normal">type: str</span>
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">dhcp_relay_interface_select_method</span> <b>(Alias name: dhcp-relay-interface-select-method)</b>  Dhcp relay interface select method. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, sdwan, specify]</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.4 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrrp</span> Vrrp. <span class="li-normal">type: list</span>
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">accept_mode</span> <b>(Alias name: accept-mode)</b>  Enable/disable accept mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">adv_interval</span> <b>(Alias name: adv-interval)</b>  Advertisement interval (1 - 255 seconds). <span class="li-normal">type: int</span>
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ignore_default_route</span> <b>(Alias name: ignore-default-route)</b>  Enable/disable ignoring of default route when checking destination. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">preempt</span> Enable/disable preempt mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Priority of the virtual router (1 - 255). <span class="li-normal">type: int</span>
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_arp</span> <b>(Alias name: proxy-arp)</b>  Proxy arp. <span class="li-normal">type: list</span>
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> Id. <span class="li-normal">type: int</span>
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Set ip addresses of proxy arp. <span class="li-normal">type: str</span>
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">start_time</span> <b>(Alias name: start-time)</b>  Startup time (1 - 255 seconds). <span class="li-normal">type: int</span>
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable/disable this vrrp configuration. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">version</span> Vrrp version. <span class="li-normal">type: str</span> <span class="li-normal">choices: [2, 3]</span> 
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrdst</span> Monitor the route to this destination. <span class="li-normal">type: list</span>
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrdst_priority</span> <b>(Alias name: vrdst-priority)</b>  Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254). <span class="li-normal">type: int</span>
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrgrp</span> Vrrp group id (1 - 65535). <span class="li-normal">type: int</span>
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrid</span> Virtual router identifier (1 - 255). <span class="li-normal">type: int</span>
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 <li><span class="li-head">vrip</span> Ip address of the virtual router. <span class="li-normal">type: str</span>
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.0</code></p>
 </div>
 </li>
 </ul>
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
      - name: Fsp vlan dynamic mapping interface
        fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          vlan: <your own value>
          dynamic_mapping: <your own value>
          fsp_vlan_dynamicmapping_interface:
            ip: <string>
            vlanid: <integer>
            dhcp_relay_agent_option: <value in [disable, enable]>
            dhcp_relay_ip: <list or string>
            dhcp_relay_service: <value in [disable, enable]>
            dhcp_relay_type: <value in [regular, ipsec]>
            ipv6:
              autoconf: <value in [disable, enable]>
              dhcp6_client_options:
                - "rapid"
                - "iapd"
                - "iana"
                - "dns"
                - "dnsname"
              dhcp6_information_request: <value in [disable, enable]>
              dhcp6_prefix_delegation: <value in [disable, enable]>
              dhcp6_prefix_hint: <string>
              dhcp6_prefix_hint_plt: <integer>
              dhcp6_prefix_hint_vlt: <integer>
              dhcp6_relay_ip: <string>
              dhcp6_relay_service: <value in [disable, enable]>
              dhcp6_relay_type: <value in [regular]>
              ip6_address: <string>
              ip6_allowaccess:
                - "https"
                - "ping"
                - "ssh"
                - "snmp"
                - "http"
                - "telnet"
                - "fgfm"
                - "capwap"
                - "fabric"
              ip6_default_life: <integer>
              ip6_delegated_prefix_list:
                -
                  autonomous_flag: <value in [disable, enable]>
                  onlink_flag: <value in [disable, enable]>
                  prefix_id: <integer>
                  rdnss: <list or string>
                  rdnss_service: <value in [delegated, default, specify]>
                  subnet: <string>
                  upstream_interface: <string>
                  delegated_prefix_iaid: <integer>
              ip6_dns_server_override: <value in [disable, enable]>
              ip6_extra_addr:
                -
                  prefix: <string>
              ip6_hop_limit: <integer>
              ip6_link_mtu: <integer>
              ip6_manage_flag: <value in [disable, enable]>
              ip6_max_interval: <integer>
              ip6_min_interval: <integer>
              ip6_mode: <value in [static, dhcp, pppoe, ...]>
              ip6_other_flag: <value in [disable, enable]>
              ip6_prefix_list:
                -
                  autonomous_flag: <value in [disable, enable]>
                  dnssl: <list or string>
                  onlink_flag: <value in [disable, enable]>
                  preferred_life_time: <integer>
                  prefix: <string>
                  rdnss: <list or string>
                  valid_life_time: <integer>
              ip6_reachable_time: <integer>
              ip6_retrans_time: <integer>
              ip6_send_adv: <value in [disable, enable]>
              ip6_subnet: <string>
              ip6_upstream_interface: <string>
              nd_cert: <string>
              nd_cga_modifier: <string>
              nd_mode: <value in [basic, SEND-compatible]>
              nd_security_level: <integer>
              nd_timestamp_delta: <integer>
              nd_timestamp_fuzz: <integer>
              vrip6_link_local: <string>
              vrrp_virtual_mac6: <value in [disable, enable]>
              vrrp6:
                -
                  accept_mode: <value in [disable, enable]>
                  adv_interval: <integer>
                  preempt: <value in [disable, enable]>
                  priority: <integer>
                  start_time: <integer>
                  status: <value in [disable, enable]>
                  vrdst6: <string>
                  vrgrp: <integer>
                  vrid: <integer>
                  vrip6: <string>
              interface_identifier: <string>
              unique_autoconf_addr: <value in [disable, enable]>
              icmp6_send_redirect: <value in [disable, enable]>
              cli_conn6_status: <integer>
              ip6_prefix_mode: <value in [dhcp6, ra]>
              ra_send_mtu: <value in [disable, enable]>
              ip6_delegated_prefix_iaid: <integer>
              dhcp6_relay_source_interface: <value in [disable, enable]>
            secondary_IP: <value in [disable, enable]>
            secondaryip:
              -
                allowaccess:
                  - "https"
                  - "ping"
                  - "ssh"
                  - "snmp"
                  - "http"
                  - "telnet"
                  - "fgfm"
                  - "auto-ipsec"
                  - "radius-acct"
                  - "probe-response"
                  - "capwap"
                  - "dnp"
                  - "ftm"
                  - "fabric"
                  - "speed-test"
                detectprotocol:
                  - "ping"
                  - "tcp-echo"
                  - "udp-echo"
                detectserver: <string>
                gwdetect: <value in [disable, enable]>
                ha_priority: <integer>
                id: <integer>
                ip: <string>
                ping_serv_status: <integer>
                seq: <integer>
                secip_relay_ip: <string>
            dhcp_relay_interface_select_method: <value in [auto, sdwan, specify]>
            vrrp:
              -
                accept_mode: <value in [disable, enable]>
                adv_interval: <integer>
                ignore_default_route: <value in [disable, enable]>
                preempt: <value in [disable, enable]>
                priority: <integer>
                proxy_arp:
                  -
                    id: <integer>
                    ip: <string>
                start_time: <integer>
                status: <value in [disable, enable]>
                version: <value in [2, 3]>
                vrdst: <list or string>
                vrdst_priority: <integer>
                vrgrp: <integer>
                vrid: <integer>
                vrip: <string>


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
