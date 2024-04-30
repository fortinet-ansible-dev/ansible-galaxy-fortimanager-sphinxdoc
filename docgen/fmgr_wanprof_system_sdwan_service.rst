:source: fmgr_wanprof_system_sdwan_service.py

:orphan:

.. _fmgr_wanprof_system_sdwan_service:

fmgr_wanprof_system_sdwan_service -- Create SD-WAN rules (also called services) to control how sessions are distributed to interfaces in the SD-WAN.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
- Tested with FortiManager v6.x and v7.x.


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.15.0


FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>



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
 <li><span class="li-head">wanprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wanprof_system_sdwan_service</span> - Create SD-WAN rules <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">addr_mode</span> <b>(Alias name: addr-mode)</b>  Address mode (ipv4 or ipv6). <span class="li-normal">type: str</span> <span class="li-normal">choices: [ipv4, ipv6]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bandwidth_weight</span> <b>(Alias name: bandwidth-weight)</b>  Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. <span class="li-normal">type: int</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">default</span> Enable/disable use of sd-wan as default service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dscp_forward</span> <b>(Alias name: dscp-forward)</b>  Enable/disable forward traffic dscp tag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dscp_forward_tag</span> <b>(Alias name: dscp-forward-tag)</b>  Forward traffic dscp tag. <span class="li-normal">type: str</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dscp_reverse</span> <b>(Alias name: dscp-reverse)</b>  Enable/disable reverse traffic dscp tag. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dscp_reverse_tag</span> <b>(Alias name: dscp-reverse-tag)</b>  Reverse traffic dscp tag. <span class="li-normal">type: str</span>
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dst</span> Destination address name. <span class="li-normal">type: list or str</span>
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dst_negate</span> <b>(Alias name: dst-negate)</b>  Enable/disable negation of destination address match. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dst6</span> Destination address6 name. <span class="li-normal">type: list or str</span>
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">end_port</span> <b>(Alias name: end-port)</b>  End destination port number. <span class="li-normal">type: int</span>
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gateway</span> Enable/disable sd-wan service gateway. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">groups</span> User groups. <span class="li-normal">type: list or str</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hash_mode</span> <b>(Alias name: hash-mode)</b>  Hash algorithm for selected priority members for load balance mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [round-robin, source-ip-based, source-dest-ip-based, inbandwidth, outbandwidth, bibandwidth]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">health_check</span> <b>(Alias name: health-check)</b>  Health check list. <span class="li-normal">type: list or str</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hold_down_time</span> <b>(Alias name: hold-down-time)</b>  Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0). <span class="li-normal">type: int</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Sd-wan rule id (1 - 4000). <span class="li-normal">type: int</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">input_device</span> <b>(Alias name: input-device)</b>  Source interface name. <span class="li-normal">type: list or str</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">input_device_negate</span> <b>(Alias name: input-device-negate)</b>  Enable/disable negation of input device match. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service</span> <b>(Alias name: internet-service)</b>  Enable/disable use of internet service for application-based load balancing. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_app_ctrl</span> <b>(Alias name: internet-service-app-ctrl)</b>  <span class="li-normal">type: list</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_app_ctrl_group</span> <b>(Alias name: internet-service-app-ctrl-group)</b>  Application control based internet service group list. <span class="li-normal">type: list or str</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_custom</span> <b>(Alias name: internet-service-custom)</b>  Custom internet service name list. <span class="li-normal">type: list or str</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_custom_group</span> <b>(Alias name: internet-service-custom-group)</b>  Custom internet service group list. <span class="li-normal">type: list or str</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_group</span> <b>(Alias name: internet-service-group)</b>  Internet service group list. <span class="li-normal">type: list or str</span>
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_name</span> <b>(Alias name: internet-service-name)</b>  Internet service name list. <span class="li-normal">type: list or str</span>
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">jitter_weight</span> <b>(Alias name: jitter-weight)</b>  Coefficient of jitter in the formula of custom-profile-1. <span class="li-normal">type: int</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">latency_weight</span> <b>(Alias name: latency-weight)</b>  Coefficient of latency in the formula of custom-profile-1. <span class="li-normal">type: int</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">link_cost_factor</span> <b>(Alias name: link-cost-factor)</b>  Link cost factor. <span class="li-normal">type: str</span> <span class="li-normal">choices: [latency, jitter, packet-loss, inbandwidth, outbandwidth, bibandwidth, custom-profile-1]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">link_cost_threshold</span> <b>(Alias name: link-cost-threshold)</b>  Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10). <span class="li-normal">type: int</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">minimum_sla_meet_members</span> <b>(Alias name: minimum-sla-meet-members)</b>  Minimum number of members which meet sla. <span class="li-normal">type: int</span>
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mode</span> Control how the sd-wan rule sets the priority of interfaces in the sd-wan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, manual, priority, sla, load-balance]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Sd-wan rule name. <span class="li-normal">type: str</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">packet_loss_weight</span> <b>(Alias name: packet-loss-weight)</b>  Coefficient of packet-loss in the formula of custom-profile-1. <span class="li-normal">type: int</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority_members</span> <b>(Alias name: priority-members)</b>  Member sequence number list. <span class="li-normal">type: list or str</span>
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">protocol</span> Protocol number. <span class="li-normal">type: int</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quality_link</span> <b>(Alias name: quality-link)</b>  Quality grade. <span class="li-normal">type: int</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">role</span> Service role to work with neighbor. <span class="li-normal">type: str</span> <span class="li-normal">choices: [primary, secondary, standalone]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">route_tag</span> <b>(Alias name: route-tag)</b>  Ipv4 route map route-tag. <span class="li-normal">type: int</span>
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sla</span> <span class="li-normal">type: list</span>
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">health_check</span> <b>(Alias name: health-check)</b>  Sd-wan health-check. <span class="li-normal">type: str</span>
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Sla id. <span class="li-normal">type: int</span>
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">sla_compare_method</span> <b>(Alias name: sla-compare-method)</b>  Method to compare sla value for sla mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [order, number]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">src</span> Source address name. <span class="li-normal">type: list or str</span>
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">src_negate</span> <b>(Alias name: src-negate)</b>  Enable/disable negation of source address match. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">src6</span> Source address6 name. <span class="li-normal">type: list or str</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">standalone_action</span> <b>(Alias name: standalone-action)</b>  Enable/disable service when selected neighbor role is standalone while service role is not standalone. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">start_port</span> <b>(Alias name: start-port)</b>  Start destination port number. <span class="li-normal">type: int</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable/disable sd-wan service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tos</span> Type of service bit pattern. <span class="li-normal">type: str</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tos_mask</span> <b>(Alias name: tos-mask)</b>  Type of service evaluated bits. <span class="li-normal">type: str</span>
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">users</span> User name. <span class="li-normal">type: list or str</span>
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tie_break</span> <b>(Alias name: tie-break)</b>  Method of selecting member if more than one meets the sla. <span class="li-normal">type: str</span> <span class="li-normal">choices: [zone, cfg-order, fib-best-match, input-device]</span> 
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">use_shortcut_sla</span> <b>(Alias name: use-shortcut-sla)</b>  Enable/disable use of advpn shortcut for quality comparison. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">input_zone</span> <b>(Alias name: input-zone)</b>  <span class="li-normal">type: list</span>
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">internet_service_app_ctrl_category</span> <b>(Alias name: internet-service-app-ctrl-category)</b>  <span class="li-normal">type: list</span>
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">passive_measurement</span> <b>(Alias name: passive-measurement)</b>  Enable/disable passive measurement based on the service criteria. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority_zone</span> <b>(Alias name: priority-zone)</b>  <span class="li-normal">type: list or str</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">agent_exclusive</span> <b>(Alias name: agent-exclusive)</b>  Set/unset the service as agent use exclusively. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">shortcut</span> Enable/disable shortcut for this service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">shortcut_stickiness</span> <b>(Alias name: shortcut-stickiness)</b>  Enable/disable shortcut-stickiness of advpn. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> v7.4.1</code></p>
 </div>
 </li>
 <li><span class="li-head">end_src_port</span> <b>(Alias name: end-src-port)</b>  End source port number. <span class="li-normal">type: int</span>
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">load_balance</span> <b>(Alias name: load-balance)</b>  Enable/disable load-balance. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sla_stickiness</span> <b>(Alias name: sla-stickiness)</b>  Enable/disable sla stickiness (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">start_src_port</span> <b>(Alias name: start-src-port)</b>  Start source port number. <span class="li-normal">type: int</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">zone_mode</span> <b>(Alias name: zone-mode)</b>  Enable/disable zone mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">shortcut_priority</span> <b>(Alias name: shortcut-priority)</b>  High priority of advpn shortcut for this service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, auto]</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
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
      - name: Create SD-WAN rules
        fortinet.fortimanager.fmgr_wanprof_system_sdwan_service:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          wanprof: <your own value>
          state: present # <value in [present, absent]>
          wanprof_system_sdwan_service:
            addr_mode: <value in [ipv4, ipv6]>
            bandwidth_weight: <integer>
            default: <value in [disable, enable]>
            dscp_forward: <value in [disable, enable]>
            dscp_forward_tag: <string>
            dscp_reverse: <value in [disable, enable]>
            dscp_reverse_tag: <string>
            dst: <list or string>
            dst_negate: <value in [disable, enable]>
            dst6: <list or string>
            end_port: <integer>
            gateway: <value in [disable, enable]>
            groups: <list or string>
            hash_mode: <value in [round-robin, source-ip-based, source-dest-ip-based, ...]>
            health_check: <list or string>
            hold_down_time: <integer>
            id: <integer>
            input_device: <list or string>
            input_device_negate: <value in [disable, enable]>
            internet_service: <value in [disable, enable]>
            internet_service_app_ctrl: <list or integer>
            internet_service_app_ctrl_group: <list or string>
            internet_service_custom: <list or string>
            internet_service_custom_group: <list or string>
            internet_service_group: <list or string>
            internet_service_name: <list or string>
            jitter_weight: <integer>
            latency_weight: <integer>
            link_cost_factor: <value in [latency, jitter, packet-loss, ...]>
            link_cost_threshold: <integer>
            minimum_sla_meet_members: <integer>
            mode: <value in [auto, manual, priority, ...]>
            name: <string>
            packet_loss_weight: <integer>
            priority_members: <list or string>
            protocol: <integer>
            quality_link: <integer>
            role: <value in [primary, secondary, standalone]>
            route_tag: <integer>
            sla:
              -
                health_check: <string>
                id: <integer>
            sla_compare_method: <value in [order, number]>
            src: <list or string>
            src_negate: <value in [disable, enable]>
            src6: <list or string>
            standalone_action: <value in [disable, enable]>
            start_port: <integer>
            status: <value in [disable, enable]>
            tos: <string>
            tos_mask: <string>
            users: <list or string>
            tie_break: <value in [zone, cfg-order, fib-best-match, ...]>
            use_shortcut_sla: <value in [disable, enable]>
            input_zone: <list or string>
            internet_service_app_ctrl_category: <list or integer>
            passive_measurement: <value in [disable, enable]>
            priority_zone: <list or string>
            agent_exclusive: <value in [disable, enable]>
            shortcut: <value in [disable, enable]>
            shortcut_stickiness: <value in [disable, enable]>
            end_src_port: <integer>
            load_balance: <value in [disable, enable]>
            sla_stickiness: <value in [disable, enable]>
            start_src_port: <integer>
            zone_mode: <value in [disable, enable]>
            shortcut_priority: <value in [disable, enable, auto]>


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
