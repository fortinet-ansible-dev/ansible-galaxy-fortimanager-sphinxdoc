:source: fmgr_voip_profile.py

:orphan:

.. _fmgr_voip_profile:

fmgr_voip_profile -- Configure VoIP profiles.
+++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock. <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">voip_profile</span> - Configure VoIP profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">comment</span> Comment. <span class="li-normal">type: str</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Profile name. <span class="li-normal">type: str</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sccp</span> <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">block_mcast</span> <b>(Alias name: block-mcast)</b>  Enable/disable block multicast rtp connections. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_call_summary</span> <b>(Alias name: log-call-summary)</b>  Enable/disable log summary of sccp calls. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_violations</span> <b>(Alias name: log-violations)</b>  Enable/disable logging of sccp violations. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_calls</span> <b>(Alias name: max-calls)</b>  Maximum calls per minute per sccp client (max 65535). <span class="li-normal">type: int</span>
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable/disable sccp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">verify_header</span> <b>(Alias name: verify-header)</b>  Enable/disable verify sccp header content. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">sip</span> <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ack_rate</span> <b>(Alias name: ack-rate)</b>  Ack request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_ack</span> <b>(Alias name: block-ack)</b>  Enable/disable block ack requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_bye</span> <b>(Alias name: block-bye)</b>  Enable/disable block bye requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_cancel</span> <b>(Alias name: block-cancel)</b>  Enable/disable block cancel requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_geo_red_options</span> <b>(Alias name: block-geo-red-options)</b>  Enable/disable block options requests, but options requests still notify for redundancy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_info</span> <b>(Alias name: block-info)</b>  Enable/disable block info requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_invite</span> <b>(Alias name: block-invite)</b>  Enable/disable block invite requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_long_lines</span> <b>(Alias name: block-long-lines)</b>  Enable/disable block requests with headers exceeding max-line-length. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_message</span> <b>(Alias name: block-message)</b>  Enable/disable block message requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_notify</span> <b>(Alias name: block-notify)</b>  Enable/disable block notify requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_options</span> <b>(Alias name: block-options)</b>  Enable/disable block options requests and no options as notifying message for redundancy either. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_prack</span> <b>(Alias name: block-prack)</b>  Enable/disable block prack requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_publish</span> <b>(Alias name: block-publish)</b>  Enable/disable block publish requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_refer</span> <b>(Alias name: block-refer)</b>  Enable/disable block refer requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_register</span> <b>(Alias name: block-register)</b>  Enable/disable block register requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_subscribe</span> <b>(Alias name: block-subscribe)</b>  Enable/disable block subscribe requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_unknown</span> <b>(Alias name: block-unknown)</b>  Block unrecognized sip requests (enabled by default). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">block_update</span> <b>(Alias name: block-update)</b>  Enable/disable block update requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bye_rate</span> <b>(Alias name: bye-rate)</b>  Bye request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">call_keepalive</span> <b>(Alias name: call-keepalive)</b>  Continue tracking calls with no rtp for this many minutes. <span class="li-normal">type: int</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cancel_rate</span> <b>(Alias name: cancel-rate)</b>  Cancel request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">contact_fixup</span> <b>(Alias name: contact-fixup)</b>  Fixup contact anyway even if contacts ip:port doesnt match sessions ip:port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hnt_restrict_source_ip</span> <b>(Alias name: hnt-restrict-source-ip)</b>  Enable/disable restrict rtp source ip to be the same as sip source ip when hnt is enabled. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">hosted_nat_traversal</span> <b>(Alias name: hosted-nat-traversal)</b>  Hosted nat traversal (hnt). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">info_rate</span> <b>(Alias name: info-rate)</b>  Info request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">invite_rate</span> <b>(Alias name: invite-rate)</b>  Invite request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ips_rtp</span> <b>(Alias name: ips-rtp)</b>  Enable/disable allow ips on rtp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_call_summary</span> <b>(Alias name: log-call-summary)</b>  Enable/disable logging of sip call summary. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_violations</span> <b>(Alias name: log-violations)</b>  Enable/disable logging of sip violations. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_allow</span> <b>(Alias name: malformed-header-allow)</b>  Action for malformed allow header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_call_id</span> <b>(Alias name: malformed-header-call-id)</b>  Action for malformed call-id header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_contact</span> <b>(Alias name: malformed-header-contact)</b>  Action for malformed contact header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_content_length</span> <b>(Alias name: malformed-header-content-length)</b>  Action for malformed content-length header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_content_type</span> <b>(Alias name: malformed-header-content-type)</b>  Action for malformed content-type header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_cseq</span> <b>(Alias name: malformed-header-cseq)</b>  Action for malformed cseq header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_expires</span> <b>(Alias name: malformed-header-expires)</b>  Action for malformed expires header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_from</span> <b>(Alias name: malformed-header-from)</b>  Action for malformed from header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_max_forwards</span> <b>(Alias name: malformed-header-max-forwards)</b>  Action for malformed max-forwards header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_p_asserted_identity</span> <b>(Alias name: malformed-header-p-asserted-identity)</b>  Action for malformed p-asserted-identity header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_rack</span> <b>(Alias name: malformed-header-rack)</b>  Action for malformed rack header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_record_route</span> <b>(Alias name: malformed-header-record-route)</b>  Action for malformed record-route header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_route</span> <b>(Alias name: malformed-header-route)</b>  Action for malformed route header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_rseq</span> <b>(Alias name: malformed-header-rseq)</b>  Action for malformed rseq header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_a</span> <b>(Alias name: malformed-header-sdp-a)</b>  Action for malformed sdp a line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_b</span> <b>(Alias name: malformed-header-sdp-b)</b>  Action for malformed sdp b line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_c</span> <b>(Alias name: malformed-header-sdp-c)</b>  Action for malformed sdp c line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_i</span> <b>(Alias name: malformed-header-sdp-i)</b>  Action for malformed sdp i line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_k</span> <b>(Alias name: malformed-header-sdp-k)</b>  Action for malformed sdp k line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_m</span> <b>(Alias name: malformed-header-sdp-m)</b>  Action for malformed sdp m line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_o</span> <b>(Alias name: malformed-header-sdp-o)</b>  Action for malformed sdp o line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_r</span> <b>(Alias name: malformed-header-sdp-r)</b>  Action for malformed sdp r line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_s</span> <b>(Alias name: malformed-header-sdp-s)</b>  Action for malformed sdp s line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_t</span> <b>(Alias name: malformed-header-sdp-t)</b>  Action for malformed sdp t line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_v</span> <b>(Alias name: malformed-header-sdp-v)</b>  Action for malformed sdp v line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_sdp_z</span> <b>(Alias name: malformed-header-sdp-z)</b>  Action for malformed sdp z line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_to</span> <b>(Alias name: malformed-header-to)</b>  Action for malformed to header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_via</span> <b>(Alias name: malformed-header-via)</b>  Action for malformed via header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_request_line</span> <b>(Alias name: malformed-request-line)</b>  Action for malformed request line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_body_length</span> <b>(Alias name: max-body-length)</b>  Maximum sip message body length (0 meaning no limit). <span class="li-normal">type: int</span>
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_dialogs</span> <b>(Alias name: max-dialogs)</b>  Maximum number of concurrent calls/dialogs (per policy). <span class="li-normal">type: int</span>
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_idle_dialogs</span> <b>(Alias name: max-idle-dialogs)</b>  Maximum number established but idle dialogs to retain (per policy). <span class="li-normal">type: int</span>
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_line_length</span> <b>(Alias name: max-line-length)</b>  Maximum sip header line length (78-4096). <span class="li-normal">type: int</span>
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">message_rate</span> <b>(Alias name: message-rate)</b>  Message request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nat_port_range</span> <b>(Alias name: nat-port-range)</b>  Rtp nat port range. <span class="li-normal">type: str</span>
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">nat_trace</span> <b>(Alias name: nat-trace)</b>  Enable/disable preservation of original ip in sdp i line. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">no_sdp_fixup</span> <b>(Alias name: no-sdp-fixup)</b>  Enable/disable no sdp fix-up. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">notify_rate</span> <b>(Alias name: notify-rate)</b>  Notify request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">open_contact_pinhole</span> <b>(Alias name: open-contact-pinhole)</b>  Enable/disable open pinhole for non-register contact port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">open_record_route_pinhole</span> <b>(Alias name: open-record-route-pinhole)</b>  Enable/disable open pinhole for record-route port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">open_register_pinhole</span> <b>(Alias name: open-register-pinhole)</b>  Enable/disable open pinhole for register contact port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">open_via_pinhole</span> <b>(Alias name: open-via-pinhole)</b>  Enable/disable open pinhole for via port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options_rate</span> <b>(Alias name: options-rate)</b>  Options request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">prack_rate</span> <b>(Alias name: prack-rate)</b>  Prack request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">preserve_override</span> <b>(Alias name: preserve-override)</b>  Override i line to preserve original ips (default: append). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">provisional_invite_expiry_time</span> <b>(Alias name: provisional-invite-expiry-time)</b>  Expiry time for provisional invite (10 - 3600 sec). <span class="li-normal">type: int</span>
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">publish_rate</span> <b>(Alias name: publish-rate)</b>  Publish request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">refer_rate</span> <b>(Alias name: refer-rate)</b>  Refer request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">register_contact_trace</span> <b>(Alias name: register-contact-trace)</b>  Enable/disable trace original ip/port within the contact header of register requests. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">register_rate</span> <b>(Alias name: register-rate)</b>  Register request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rfc2543_branch</span> <b>(Alias name: rfc2543-branch)</b>  Enable/disable support via branch compliant with rfc 2543. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rtp</span> Enable/disable create pinholes for rtp traffic to traverse firewall. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_algorithm</span> <b>(Alias name: ssl-algorithm)</b>  Relative strength of encryption algorithms accepted in negotiation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [high, medium, low]</span> 
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_auth_client</span> <b>(Alias name: ssl-auth-client)</b>  Require a client certificate and authenticate it with the peer/peergrp. <span class="li-normal">type: str</span>
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_auth_server</span> <b>(Alias name: ssl-auth-server)</b>  Authenticate the servers certificate with the peer/peergrp. <span class="li-normal">type: str</span>
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_client_certificate</span> <b>(Alias name: ssl-client-certificate)</b>  Name of certificate to offer to server if requested. <span class="li-normal">type: str</span>
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_client_renegotiation</span> <b>(Alias name: ssl-client-renegotiation)</b>  Allow/block client renegotiation by server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny, secure]</span> 
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_max_version</span> <b>(Alias name: ssl-max-version)</b>  Highest ssl/tls version to negotiate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_min_version</span> <b>(Alias name: ssl-min-version)</b>  Lowest ssl/tls version to negotiate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_mode</span> <b>(Alias name: ssl-mode)</b>  Ssl/tls mode for encryption & decryption of traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [off, full]</span> 
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_pfs</span> <b>(Alias name: ssl-pfs)</b>  Ssl perfect forward secrecy. <span class="li-normal">type: str</span> <span class="li-normal">choices: [require, deny, allow]</span> 
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_send_empty_frags</span> <b>(Alias name: ssl-send-empty-frags)</b>  Send empty fragments to avoid attack on cbc iv (ssl 3. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_server_certificate</span> <b>(Alias name: ssl-server-certificate)</b>  Name of certificate return to the client in every ssl connection. <span class="li-normal">type: str</span>
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable/disable sip. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">strict_register</span> <b>(Alias name: strict-register)</b>  Enable/disable only allow the registrar to connect. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">subscribe_rate</span> <b>(Alias name: subscribe-rate)</b>  Subscribe request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">unknown_header</span> <b>(Alias name: unknown-header)</b>  Action for unknown sip header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_rate</span> <b>(Alias name: update-rate)</b>  Update request rate limit (per second, per policy). <span class="li-normal">type: int</span>
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.8 -> v6.2.12</code>, <code class="docutils literal notranslate">v6.4.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ack_rate_track</span> <b>(Alias name: ack-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bye_rate_track</span> <b>(Alias name: bye-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cancel_rate_track</span> <b>(Alias name: cancel-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">info_rate_track</span> <b>(Alias name: info-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">invite_rate_track</span> <b>(Alias name: invite-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_no_proxy_require</span> <b>(Alias name: malformed-header-no-proxy-require)</b>  Action for malformed sip messages without proxy-require header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">malformed_header_no_require</span> <b>(Alias name: malformed-header-no-require)</b>  Action for malformed sip messages without require header. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, discard, respond]</span> 
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">message_rate_track</span> <b>(Alias name: message-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">notify_rate_track</span> <b>(Alias name: notify-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">options_rate_track</span> <b>(Alias name: options-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">prack_rate_track</span> <b>(Alias name: prack-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">publish_rate_track</span> <b>(Alias name: publish-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">refer_rate_track</span> <b>(Alias name: refer-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">register_rate_track</span> <b>(Alias name: register-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">subscribe_rate_track</span> <b>(Alias name: subscribe-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_rate_track</span> <b>(Alias name: update-rate-track)</b>  Track the packet protocol field. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, src-ip, dest-ip]</span> 
 <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">call_id_regex</span> <b>(Alias name: call-id-regex)</b>  Validate pcre regular expression for call-id header value. <span class="li-normal">type: str</span>
 <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">content_type_regex</span> <b>(Alias name: content-type-regex)</b>  Validate pcre regular expression for content-type header value. <span class="li-normal">type: str</span>
 <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.3 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">feature_set</span> <b>(Alias name: feature-set)</b>  Flow or proxy inspection feature set. <span class="li-normal">type: str</span> <span class="li-normal">choices: [flow, proxy, ips, voipd]</span> 
 <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">msrp</span> <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">log_violations</span> <b>(Alias name: log-violations)</b>  Enable/disable logging of msrp violations. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_msg_size</span> <b>(Alias name: max-msg-size)</b>  Maximum allowable msrp message size (1-65535). <span class="li-normal">type: int</span>
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_msg_size_action</span> <b>(Alias name: max-msg-size-action)</b>  Action for violation of max-msg-size. <span class="li-normal">type: str</span> <span class="li-normal">choices: [pass, block, reset, monitor]</span> 
 <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Enable/disable msrp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
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
      - name: Configure VoIP profiles.
        fortinet.fortimanager.fmgr_voip_profile:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          state: present # <value in [present, absent]>
          voip_profile:
            comment: <string>
            name: <string>
            sccp:
              block_mcast: <value in [disable, enable]>
              log_call_summary: <value in [disable, enable]>
              log_violations: <value in [disable, enable]>
              max_calls: <integer>
              status: <value in [disable, enable]>
              verify_header: <value in [disable, enable]>
            sip:
              ack_rate: <integer>
              block_ack: <value in [disable, enable]>
              block_bye: <value in [disable, enable]>
              block_cancel: <value in [disable, enable]>
              block_geo_red_options: <value in [disable, enable]>
              block_info: <value in [disable, enable]>
              block_invite: <value in [disable, enable]>
              block_long_lines: <value in [disable, enable]>
              block_message: <value in [disable, enable]>
              block_notify: <value in [disable, enable]>
              block_options: <value in [disable, enable]>
              block_prack: <value in [disable, enable]>
              block_publish: <value in [disable, enable]>
              block_refer: <value in [disable, enable]>
              block_register: <value in [disable, enable]>
              block_subscribe: <value in [disable, enable]>
              block_unknown: <value in [disable, enable]>
              block_update: <value in [disable, enable]>
              bye_rate: <integer>
              call_keepalive: <integer>
              cancel_rate: <integer>
              contact_fixup: <value in [disable, enable]>
              hnt_restrict_source_ip: <value in [disable, enable]>
              hosted_nat_traversal: <value in [disable, enable]>
              info_rate: <integer>
              invite_rate: <integer>
              ips_rtp: <value in [disable, enable]>
              log_call_summary: <value in [disable, enable]>
              log_violations: <value in [disable, enable]>
              malformed_header_allow: <value in [pass, discard, respond]>
              malformed_header_call_id: <value in [pass, discard, respond]>
              malformed_header_contact: <value in [pass, discard, respond]>
              malformed_header_content_length: <value in [pass, discard, respond]>
              malformed_header_content_type: <value in [pass, discard, respond]>
              malformed_header_cseq: <value in [pass, discard, respond]>
              malformed_header_expires: <value in [pass, discard, respond]>
              malformed_header_from: <value in [pass, discard, respond]>
              malformed_header_max_forwards: <value in [pass, discard, respond]>
              malformed_header_p_asserted_identity: <value in [pass, discard, respond]>
              malformed_header_rack: <value in [pass, discard, respond]>
              malformed_header_record_route: <value in [pass, discard, respond]>
              malformed_header_route: <value in [pass, discard, respond]>
              malformed_header_rseq: <value in [pass, discard, respond]>
              malformed_header_sdp_a: <value in [pass, discard, respond]>
              malformed_header_sdp_b: <value in [pass, discard, respond]>
              malformed_header_sdp_c: <value in [pass, discard, respond]>
              malformed_header_sdp_i: <value in [pass, discard, respond]>
              malformed_header_sdp_k: <value in [pass, discard, respond]>
              malformed_header_sdp_m: <value in [pass, discard, respond]>
              malformed_header_sdp_o: <value in [pass, discard, respond]>
              malformed_header_sdp_r: <value in [pass, discard, respond]>
              malformed_header_sdp_s: <value in [pass, discard, respond]>
              malformed_header_sdp_t: <value in [pass, discard, respond]>
              malformed_header_sdp_v: <value in [pass, discard, respond]>
              malformed_header_sdp_z: <value in [pass, discard, respond]>
              malformed_header_to: <value in [pass, discard, respond]>
              malformed_header_via: <value in [pass, discard, respond]>
              malformed_request_line: <value in [pass, discard, respond]>
              max_body_length: <integer>
              max_dialogs: <integer>
              max_idle_dialogs: <integer>
              max_line_length: <integer>
              message_rate: <integer>
              nat_port_range: <string>
              nat_trace: <value in [disable, enable]>
              no_sdp_fixup: <value in [disable, enable]>
              notify_rate: <integer>
              open_contact_pinhole: <value in [disable, enable]>
              open_record_route_pinhole: <value in [disable, enable]>
              open_register_pinhole: <value in [disable, enable]>
              open_via_pinhole: <value in [disable, enable]>
              options_rate: <integer>
              prack_rate: <integer>
              preserve_override: <value in [disable, enable]>
              provisional_invite_expiry_time: <integer>
              publish_rate: <integer>
              refer_rate: <integer>
              register_contact_trace: <value in [disable, enable]>
              register_rate: <integer>
              rfc2543_branch: <value in [disable, enable]>
              rtp: <value in [disable, enable]>
              ssl_algorithm: <value in [high, medium, low]>
              ssl_auth_client: <string>
              ssl_auth_server: <string>
              ssl_client_certificate: <string>
              ssl_client_renegotiation: <value in [allow, deny, secure]>
              ssl_max_version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
              ssl_min_version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
              ssl_mode: <value in [off, full]>
              ssl_pfs: <value in [require, deny, allow]>
              ssl_send_empty_frags: <value in [disable, enable]>
              ssl_server_certificate: <string>
              status: <value in [disable, enable]>
              strict_register: <value in [disable, enable]>
              subscribe_rate: <integer>
              unknown_header: <value in [pass, discard, respond]>
              update_rate: <integer>
              ack_rate_track: <value in [none, src-ip, dest-ip]>
              bye_rate_track: <value in [none, src-ip, dest-ip]>
              cancel_rate_track: <value in [none, src-ip, dest-ip]>
              info_rate_track: <value in [none, src-ip, dest-ip]>
              invite_rate_track: <value in [none, src-ip, dest-ip]>
              malformed_header_no_proxy_require: <value in [pass, discard, respond]>
              malformed_header_no_require: <value in [pass, discard, respond]>
              message_rate_track: <value in [none, src-ip, dest-ip]>
              notify_rate_track: <value in [none, src-ip, dest-ip]>
              options_rate_track: <value in [none, src-ip, dest-ip]>
              prack_rate_track: <value in [none, src-ip, dest-ip]>
              publish_rate_track: <value in [none, src-ip, dest-ip]>
              refer_rate_track: <value in [none, src-ip, dest-ip]>
              register_rate_track: <value in [none, src-ip, dest-ip]>
              subscribe_rate_track: <value in [none, src-ip, dest-ip]>
              update_rate_track: <value in [none, src-ip, dest-ip]>
              call_id_regex: <string>
              content_type_regex: <string>
            feature_set: <value in [flow, proxy, ips, ...]>
            msrp:
              log_violations: <value in [disable, enable]>
              max_msg_size: <integer>
              max_msg_size_action: <value in [pass, block, reset, ...]>
              status: <value in [disable, enable]>


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
