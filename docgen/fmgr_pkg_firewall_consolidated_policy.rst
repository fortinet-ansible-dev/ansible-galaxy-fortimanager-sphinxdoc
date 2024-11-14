:source: fmgr_pkg_firewall_consolidated_policy.py

:orphan:

.. _fmgr_pkg_firewall_consolidated_policy:

fmgr_pkg_firewall_consolidated_policy -- Configure consolidated IPv4/IPv6 policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.1.0

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>



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
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_firewall_consolidated_policy</span> - Configure consolidated IPv4/IPv6 policies. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> Policy action (allow/deny/ipsec). <span class="li-normal">type: str</span> <span class="li-normal">choices: [deny, accept, ipsec]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">app_category</span> <b>(Alias name: app-category)</b>  Application category id list. <span class="li-normal">type: list or str</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.2</code></p>
 </div>
 </li>
 <li><span class="li-head">app_group</span> <b>(Alias name: app-group)</b>  Application group names. <span class="li-normal">type: list or str</span>
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.2</code></p>
 </div>
 </li>
 <li><span class="li-head">application</span> Application id list. <span class="li-normal">type: list</span>
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.2</code></p>
 </div>
 </li>
 <li><span class="li-head">application_list</span> <b>(Alias name: application-list)</b>  Name of an existing application list. <span class="li-normal">type: str</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_asic_offload</span> <b>(Alias name: auto-asic-offload)</b>  Enable/disable offloading security profile processing to cp processors. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">av_profile</span> <b>(Alias name: av-profile)</b>  Name of an existing antivirus profile. <span class="li-normal">type: str</span>
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cifs_profile</span> <b>(Alias name: cifs-profile)</b>  Name of an existing cifs profile. <span class="li-normal">type: str</span>
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">comments</span> Comment. <span class="li-normal">type: str</span>
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">diffserv_forward</span> <b>(Alias name: diffserv-forward)</b>  Enable to change packets diffserv values to the specified diffservcode-forward value. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">diffserv_reverse</span> <b>(Alias name: diffserv-reverse)</b>  Enable to change packets reverse (reply) diffserv values to the specified diffservcode-rev value. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">diffservcode_forward</span> <b>(Alias name: diffservcode-forward)</b>  Change packets diffserv to this value. <span class="li-normal">type: str</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">diffservcode_rev</span> <b>(Alias name: diffservcode-rev)</b>  Change packets reverse (reply) diffserv to this value. <span class="li-normal">type: str</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dlp_sensor</span> <b>(Alias name: dlp-sensor)</b>  Name of an existing dlp sensor. <span class="li-normal">type: str</span>
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dnsfilter_profile</span> <b>(Alias name: dnsfilter-profile)</b>  Name of an existing dns filter profile. <span class="li-normal">type: str</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dstaddr4</span> Destination ipv4 address name and address group names. <span class="li-normal">type: list or str</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dstaddr6</span> Destination ipv6 address name and address group names. <span class="li-normal">type: list or str</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dstintf</span> Outgoing (egress) interface. <span class="li-normal">type: list or str</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">emailfilter_profile</span> <b>(Alias name: emailfilter-profile)</b>  Name of an existing email filter profile. <span class="li-normal">type: str</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fixedport</span> Enable to prevent source nat from changing a sessions source port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">groups</span> Names of user groups that can authenticate with this policy. <span class="li-normal">type: list or str</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_policy_redirect</span> <b>(Alias name: http-policy-redirect)</b>  Redirect http(s) traffic to matching transparent web proxy policy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">icap_profile</span> <b>(Alias name: icap-profile)</b>  Name of an existing icap profile. <span class="li-normal">type: str</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">inbound</span> Policy-based ipsec vpn: only traffic from the remote network can initiate a vpn. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">inspection_mode</span> <b>(Alias name: inspection-mode)</b>  Policy inspection mode (flow/proxy). <span class="li-normal">type: str</span> <span class="li-normal">choices: [proxy, flow]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service</span> <b>(Alias name: internet-service)</b>  Enable/disable use of internet services for this policy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_custom</span> <b>(Alias name: internet-service-custom)</b>  Custom internet service name. <span class="li-normal">type: list or str</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_custom_group</span> <b>(Alias name: internet-service-custom-group)</b>  Custom internet service group name. <span class="li-normal">type: list or str</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_group</span> <b>(Alias name: internet-service-group)</b>  Internet service group name. <span class="li-normal">type: list or str</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_id</span> <b>(Alias name: internet-service-id)</b>  Internet service id. <span class="li-normal">type: list or str</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_src</span> <b>(Alias name: internet-service-src)</b>  Enable/disable use of internet services in source for this policy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_src_custom</span> <b>(Alias name: internet-service-src-custom)</b>  Custom internet service source name. <span class="li-normal">type: list or str</span>
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_src_custom_group</span> <b>(Alias name: internet-service-src-custom-group)</b>  Custom internet service source group name. <span class="li-normal">type: list or str</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_src_group</span> <b>(Alias name: internet-service-src-group)</b>  Internet service source group name. <span class="li-normal">type: list or str</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_src_id</span> <b>(Alias name: internet-service-src-id)</b>  Internet service source id. <span class="li-normal">type: list or str</span>
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ippool</span> Enable to use ip pools for source nat. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ips_sensor</span> <b>(Alias name: ips-sensor)</b>  Name of an existing ips sensor. <span class="li-normal">type: str</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">logtraffic</span> Enable or disable logging. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, all, utm]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">logtraffic_start</span> <b>(Alias name: logtraffic-start)</b>  Record logs when a session starts. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mms_profile</span> <b>(Alias name: mms-profile)</b>  Name of an existing mms profile. <span class="li-normal">type: str</span>
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Policy name. <span class="li-normal">type: str</span>
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nat</span> Enable/disable source nat. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbound</span> Policy-based ipsec vpn: only traffic from the internal network can initiate a vpn. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">per_ip_shaper</span> <b>(Alias name: per-ip-shaper)</b>  Per-ip traffic shaper. <span class="li-normal">type: str</span>
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">policyid</span> Policy id (0 - 4294967294). <span class="li-normal">type: int</span>
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">poolname4</span> Ipv4 pool names. <span class="li-normal">type: list or str</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">poolname6</span> Ipv6 pool names. <span class="li-normal">type: list or str</span>
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">profile_group</span> <b>(Alias name: profile-group)</b>  Name of profile group. <span class="li-normal">type: str</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">profile_protocol_options</span> <b>(Alias name: profile-protocol-options)</b>  Name of an existing protocol options profile. <span class="li-normal">type: str</span>
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">profile_type</span> <b>(Alias name: profile-type)</b>  Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span> <span class="li-normal">choices: [single, group]</span> 
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">schedule</span> Schedule name. <span class="li-normal">type: str</span>
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">service</span> Service and service group names. <span class="li-normal">type: list or str</span>
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">session_ttl</span> <b>(Alias name: session-ttl)</b>  Ttl in seconds for sessions accepted by this policy (0 means use the system default session ttl). <span class="li-normal">type: int</span>
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">srcaddr4</span> Source ipv4 address name and address group names. <span class="li-normal">type: list or str</span>
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">srcaddr6</span> Source ipv6 address name and address group names. <span class="li-normal">type: list or str</span>
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">srcintf</span> Incoming (ingress) interface. <span class="li-normal">type: list or str</span>
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_filter_profile</span> <b>(Alias name: ssh-filter-profile)</b>  Name of an existing ssh filter profile. <span class="li-normal">type: str</span>
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_policy_redirect</span> <b>(Alias name: ssh-policy-redirect)</b>  Redirect ssh traffic to matching transparent proxy policy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_ssh_profile</span> <b>(Alias name: ssl-ssh-profile)</b>  Name of an existing ssl ssh profile. <span class="li-normal">type: str</span>
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable or disable this policy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_mss_receiver</span> <b>(Alias name: tcp-mss-receiver)</b>  Receiver tcp maximum segment size (mss). <span class="li-normal">type: int</span>
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tcp_mss_sender</span> <b>(Alias name: tcp-mss-sender)</b>  Sender tcp maximum segment size (mss). <span class="li-normal">type: int</span>
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">traffic_shaper</span> <b>(Alias name: traffic-shaper)</b>  Traffic shaper. <span class="li-normal">type: str</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">traffic_shaper_reverse</span> <b>(Alias name: traffic-shaper-reverse)</b>  Reverse traffic shaper. <span class="li-normal">type: str</span>
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">url_category</span> <b>(Alias name: url-category)</b>  Url category id list. <span class="li-normal">type: list or str</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v7.2.5</code>, <code class="docutils literal notranslate">v7.4.0 -> v7.4.2</code></p>
 </div>
 </li>
 <li><span class="li-head">users</span> Names of individual users that can authenticate with this policy. <span class="li-normal">type: list or str</span>
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">utm_status</span> <b>(Alias name: utm-status)</b>  Enable to add one or more security profiles (av, ips, etc. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">uuid</span> Universally unique identifier (uuid; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">voip_profile</span> <b>(Alias name: voip-profile)</b>  Name of an existing voip profile. <span class="li-normal">type: str</span>
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vpntunnel</span> Policy-based ipsec vpn: name of the ipsec vpn phase 1. <span class="li-normal">type: str</span>
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">waf_profile</span> <b>(Alias name: waf-profile)</b>  Name of an existing web application firewall profile. <span class="li-normal">type: str</span>
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wanopt</span> Enable/disable wan optimization. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wanopt_detection</span> <b>(Alias name: wanopt-detection)</b>  Wan optimization auto-detection mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [active, passive, off]</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wanopt_passive_opt</span> <b>(Alias name: wanopt-passive-opt)</b>  Wan optimization passive mode options. <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, transparent, non-transparent]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wanopt_peer</span> <b>(Alias name: wanopt-peer)</b>  Wan optimization peer. <span class="li-normal">type: str</span>
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wanopt_profile</span> <b>(Alias name: wanopt-profile)</b>  Wan optimization profile. <span class="li-normal">type: str</span>
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webcache</span> Enable/disable web cache. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webcache_https</span> <b>(Alias name: webcache-https)</b>  Enable/disable web cache for https. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> v7.2.0</code>, <code class="docutils literal notranslate">v7.2.6 -> v7.2.8</code>, <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_profile</span> <b>(Alias name: webfilter-profile)</b>  Name of an existing web filter profile. <span class="li-normal">type: str</span>
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webproxy_forward_server</span> <b>(Alias name: webproxy-forward-server)</b>  Webproxy forward server name. <span class="li-normal">type: str</span>
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webproxy_profile</span> <b>(Alias name: webproxy-profile)</b>  Webproxy profile name. <span class="li-normal">type: str</span>
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">captive_portal_exempt</span> <b>(Alias name: captive-portal-exempt)</b>  Enable exemption of some users from the captive portal. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dstaddr_negate</span> <b>(Alias name: dstaddr-negate)</b>  When enabled dstaddr specifies what the destination address must not be. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fsso_groups</span> <b>(Alias name: fsso-groups)</b>  Names of fsso groups. <span class="li-normal">type: list or str</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">global_label</span> <b>(Alias name: global-label)</b>  Label for the policy that appears when the gui is in global view mode. <span class="li-normal">type: str</span>
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_negate</span> <b>(Alias name: internet-service-negate)</b>  When enabled internet-service specifies what the service must not be. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_src_negate</span> <b>(Alias name: internet-service-src-negate)</b>  When enabled internet-service-src specifies what the service must not be. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">service_negate</span> <b>(Alias name: service-negate)</b>  When enabled service specifies what the service must not be. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">srcaddr_negate</span> <b>(Alias name: srcaddr-negate)</b>  When enabled srcaddr specifies what the source address must not be. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">_policy_block</span> Assigned policy block. <span class="li-normal">type: int</span>
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
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
      - name: Configure consolidated IPv4/IPv6 policies.
        fortinet.fortimanager.fmgr_pkg_firewall_consolidated_policy:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          pkg: <your own value>
          state: present # <value in [present, absent]>
          pkg_firewall_consolidated_policy:
            action: <value in [deny, accept, ipsec]>
            app_category: <list or string>
            app_group: <list or string>
            application: <list or integer>
            application_list: <string>
            auto_asic_offload: <value in [disable, enable]>
            av_profile: <string>
            cifs_profile: <string>
            comments: <string>
            diffserv_forward: <value in [disable, enable]>
            diffserv_reverse: <value in [disable, enable]>
            diffservcode_forward: <string>
            diffservcode_rev: <string>
            dlp_sensor: <string>
            dnsfilter_profile: <string>
            dstaddr4: <list or string>
            dstaddr6: <list or string>
            dstintf: <list or string>
            emailfilter_profile: <string>
            fixedport: <value in [disable, enable]>
            groups: <list or string>
            http_policy_redirect: <value in [disable, enable]>
            icap_profile: <string>
            inbound: <value in [disable, enable]>
            inspection_mode: <value in [proxy, flow]>
            internet_service: <value in [disable, enable]>
            internet_service_custom: <list or string>
            internet_service_custom_group: <list or string>
            internet_service_group: <list or string>
            internet_service_id: <list or string>
            internet_service_src: <value in [disable, enable]>
            internet_service_src_custom: <list or string>
            internet_service_src_custom_group: <list or string>
            internet_service_src_group: <list or string>
            internet_service_src_id: <list or string>
            ippool: <value in [disable, enable]>
            ips_sensor: <string>
            logtraffic: <value in [disable, all, utm]>
            logtraffic_start: <value in [disable, enable]>
            mms_profile: <string>
            name: <string>
            nat: <value in [disable, enable]>
            outbound: <value in [disable, enable]>
            per_ip_shaper: <string>
            policyid: <integer>
            poolname4: <list or string>
            poolname6: <list or string>
            profile_group: <string>
            profile_protocol_options: <string>
            profile_type: <value in [single, group]>
            schedule: <string>
            service: <list or string>
            session_ttl: <integer>
            srcaddr4: <list or string>
            srcaddr6: <list or string>
            srcintf: <list or string>
            ssh_filter_profile: <string>
            ssh_policy_redirect: <value in [disable, enable]>
            ssl_ssh_profile: <string>
            status: <value in [disable, enable]>
            tcp_mss_receiver: <integer>
            tcp_mss_sender: <integer>
            traffic_shaper: <string>
            traffic_shaper_reverse: <string>
            url_category: <list or string>
            users: <list or string>
            utm_status: <value in [disable, enable]>
            uuid: <string>
            voip_profile: <string>
            vpntunnel: <string>
            waf_profile: <string>
            wanopt: <value in [disable, enable]>
            wanopt_detection: <value in [active, passive, off]>
            wanopt_passive_opt: <value in [default, transparent, non-transparent]>
            wanopt_peer: <string>
            wanopt_profile: <string>
            webcache: <value in [disable, enable]>
            webcache_https: <value in [disable, enable]>
            webfilter_profile: <string>
            webproxy_forward_server: <string>
            webproxy_profile: <string>
            captive_portal_exempt: <value in [disable, enable]>
            dstaddr_negate: <value in [disable, enable]>
            fsso_groups: <list or string>
            global_label: <string>
            internet_service_negate: <value in [disable, enable]>
            internet_service_src_negate: <value in [disable, enable]>
            service_negate: <value in [disable, enable]>
            srcaddr_negate: <value in [disable, enable]>
            _policy_block: <integer>


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
