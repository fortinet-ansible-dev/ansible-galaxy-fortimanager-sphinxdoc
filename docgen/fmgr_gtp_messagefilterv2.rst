:source: fmgr_gtp_messagefilterv2.py

:orphan:

.. _fmgr_gtp_messagefilterv2:

fmgr_gtp_messagefilterv2 -- Message filter for GTPv2 messages.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">gtp_messagefilterv2</span> - Message filter for GTPv2 messages. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">bearer_resource_cmd_fail</span> <b>(Alias name: bearer-resource-cmd-fail)</b>  Bearer resource (command 68, failure indication 69). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">change_notification</span> <b>(Alias name: change-notification)</b>  Change notification (req 38, resp 39). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">create_bearer</span> <b>(Alias name: create-bearer)</b>  Create bearer (req 95, resp 96). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">create_session</span> <b>(Alias name: create-session)</b>  Create session (req 32, resp 33). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_bearer_cmd_fail</span> <b>(Alias name: delete-bearer-cmd-fail)</b>  Delete bearer (command 66, failure indication 67). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_bearer_req_resp</span> <b>(Alias name: delete-bearer-req-resp)</b>  Delete bearer (req 99, resp 100). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_pdn_connection_set</span> <b>(Alias name: delete-pdn-connection-set)</b>  Delete pdn connection set (req 101, resp 102). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_session</span> <b>(Alias name: delete-session)</b>  Delete session (req 36, resp 37). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">echo</span> Echo (req 1, resp 2). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">modify_bearer_cmd_fail</span> <b>(Alias name: modify-bearer-cmd-fail)</b>  Modify bearer (command 64 , failure indication 65). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">modify_bearer_req_resp</span> <b>(Alias name: modify-bearer-req-resp)</b>  Modify bearer (req 34, resp 35). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Message filter name. <span class="li-normal">type: str</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">resume</span> Resume (notify 164 , ack 165). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">suspend</span> Suspend (notify 162, ack 163). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">trace_session</span> <b>(Alias name: trace-session)</b>  Trace session (activation 71, deactivation 72). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">unknown_message</span> <b>(Alias name: unknown-message)</b>  Allow or deny unknown messages. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">unknown_message_white_list</span> <b>(Alias name: unknown-message-white-list)</b>  White list (to allow) of unknown messages. <span class="li-normal">type: list</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_bearer</span> <b>(Alias name: update-bearer)</b>  Update bearer (req 97, resp 98). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_pdn_connection_set</span> <b>(Alias name: update-pdn-connection-set)</b>  Update pdn connection set (req 200, resp 201). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">version_not_support</span> <b>(Alias name: version-not-support)</b>  Version not supported (3). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">context_req_res_ack</span> <b>(Alias name: context-req-res-ack)</b>  Context request/response/acknowledge (req 130, resp 131, ack 132). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forward_relocation_cmp_notif_ack</span> <b>(Alias name: forward-relocation-cmp-notif-ack)</b>  Forward relocation complete notification/acknowledge (notif 135, ack 136). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forward_relocation_req_res</span> <b>(Alias name: forward-relocation-req-res)</b>  Forward relocation request/response (req 133, resp 134). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">alert_mme_notif_ack</span> <b>(Alias name: alert-mme-notif-ack)</b>  Alert mme notification/acknowledge (notif 153, ack 154). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">configuration_transfer_tunnel</span> <b>(Alias name: configuration-transfer-tunnel)</b>  Configuration transfer tunnel (141). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">create_forwarding_tunnel_req_resp</span> <b>(Alias name: create-forwarding-tunnel-req-resp)</b>  Create forwarding tunnel request/response (req 160, resp 161). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">create_indirect_forwarding_tunnel_req_resp</span> <b>(Alias name: create-indirect-forwarding-tunnel-req-resp)</b>  Create indirect data forwarding tunnel request/response (req 166, resp 167). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cs_paging</span> <b>(Alias name: cs-paging)</b>  Cs paging indication (151) <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_indirect_forwarding_tunnel_req_resp</span> <b>(Alias name: delete-indirect-forwarding-tunnel-req-resp)</b>  Delete indirect data forwarding tunnel request/response (req 168, resp 169). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">detach_notif_ack</span> <b>(Alias name: detach-notif-ack)</b>  Detach notification/acknowledge (notif 149, ack 150). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dlink_data_notif_ack</span> <b>(Alias name: dlink-data-notif-ack)</b>  Downlink data notification/acknowledge (notif 176, ack 177). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dlink_notif_failure</span> <b>(Alias name: dlink-notif-failure)</b>  Downlink data notification failure indication (70). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">forward_access_notif_ack</span> <b>(Alias name: forward-access-notif-ack)</b>  Forward access context notification/acknowledge (notif 137, ack 138). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">identification_req_resp</span> <b>(Alias name: identification-req-resp)</b>  Identification request/response (req 128, resp 129). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">isr_status</span> <b>(Alias name: isr-status)</b>  Isr status indication (157). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mbms_session_start_req_resp</span> <b>(Alias name: mbms-session-start-req-resp)</b>  Mbms session start request/response (req 231, resp 232). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mbms_session_stop_req_resp</span> <b>(Alias name: mbms-session-stop-req-resp)</b>  Mbms session stop request/response (req 235, resp 236). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mbms_session_update_req_resp</span> <b>(Alias name: mbms-session-update-req-resp)</b>  Mbms session update request/response (req 233, resp 234). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">modify_access_req_resp</span> <b>(Alias name: modify-access-req-resp)</b>  Modify access bearers request/response (req 211, resp 212). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pgw_dlink_notif_ack</span> <b>(Alias name: pgw-dlink-notif-ack)</b>  Pgw downlink triggering notification/acknowledge (notif 103, ack 104). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">pgw_restart_notif_ack</span> <b>(Alias name: pgw-restart-notif-ack)</b>  Pgw restart notification/acknowledge (notif 179, ack 180). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ran_info_relay</span> <b>(Alias name: ran-info-relay)</b>  Ran information relay (152). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">release_access_bearer_req_resp</span> <b>(Alias name: release-access-bearer-req-resp)</b>  Release access bearers request/response (req 170, resp 171). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">relocation_cancel_req_resp</span> <b>(Alias name: relocation-cancel-req-resp)</b>  Relocation cancel request/response (req 139, resp 140). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">remote_ue_report_notif_ack</span> <b>(Alias name: remote-ue-report-notif-ack)</b>  Remote ue report notification/acknowledge (notif 40, ack 41). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">reserved_for_earlier_version</span> <b>(Alias name: reserved-for-earlier-version)</b>  Reserved for earlier version of the gtp specification (178). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">stop_paging_indication</span> <b>(Alias name: stop-paging-indication)</b>  Stop paging indication (73). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ue_activity_notif_ack</span> <b>(Alias name: ue-activity-notif-ack)</b>  Ue activity notification/acknowledge (notif 155, ack 156). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ue_registration_query_req_resp</span> <b>(Alias name: ue-registration-query-req-resp)</b>  Ue registration query request/response (req 158, resp 159). <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
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
      - name: Message filter for GTPv2 messages.
        fortinet.fortimanager.fmgr_gtp_messagefilterv2:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          state: present # <value in [present, absent]>
          gtp_messagefilterv2:
            name: "your value" # Required variable, string
            # bearer_resource_cmd_fail: <value in [allow, deny]>
            # change_notification: <value in [allow, deny]>
            # create_bearer: <value in [allow, deny]>
            # create_session: <value in [allow, deny]>
            # delete_bearer_cmd_fail: <value in [allow, deny]>
            # delete_bearer_req_resp: <value in [allow, deny]>
            # delete_pdn_connection_set: <value in [allow, deny]>
            # delete_session: <value in [allow, deny]>
            # echo: <value in [allow, deny]>
            # modify_bearer_cmd_fail: <value in [allow, deny]>
            # modify_bearer_req_resp: <value in [allow, deny]>
            # resume: <value in [allow, deny]>
            # suspend: <value in [allow, deny]>
            # trace_session: <value in [allow, deny]>
            # unknown_message: <value in [allow, deny]>
            # unknown_message_white_list: <list or integer>
            # update_bearer: <value in [allow, deny]>
            # update_pdn_connection_set: <value in [allow, deny]>
            # version_not_support: <value in [allow, deny]>
            # context_req_res_ack: <value in [allow, deny]>
            # forward_relocation_cmp_notif_ack: <value in [allow, deny]>
            # forward_relocation_req_res: <value in [allow, deny]>
            # alert_mme_notif_ack: <value in [allow, deny]>
            # configuration_transfer_tunnel: <value in [allow, deny]>
            # create_forwarding_tunnel_req_resp: <value in [allow, deny]>
            # create_indirect_forwarding_tunnel_req_resp: <value in [allow, deny]>
            # cs_paging: <value in [allow, deny]>
            # delete_indirect_forwarding_tunnel_req_resp: <value in [allow, deny]>
            # detach_notif_ack: <value in [allow, deny]>
            # dlink_data_notif_ack: <value in [allow, deny]>
            # dlink_notif_failure: <value in [allow, deny]>
            # forward_access_notif_ack: <value in [allow, deny]>
            # identification_req_resp: <value in [allow, deny]>
            # isr_status: <value in [allow, deny]>
            # mbms_session_start_req_resp: <value in [allow, deny]>
            # mbms_session_stop_req_resp: <value in [allow, deny]>
            # mbms_session_update_req_resp: <value in [allow, deny]>
            # modify_access_req_resp: <value in [allow, deny]>
            # pgw_dlink_notif_ack: <value in [allow, deny]>
            # pgw_restart_notif_ack: <value in [allow, deny]>
            # ran_info_relay: <value in [allow, deny]>
            # release_access_bearer_req_resp: <value in [allow, deny]>
            # relocation_cancel_req_resp: <value in [allow, deny]>
            # remote_ue_report_notif_ack: <value in [allow, deny]>
            # reserved_for_earlier_version: <value in [allow, deny]>
            # stop_paging_indication: <value in [allow, deny]>
            # ue_activity_notif_ack: <value in [allow, deny]>
            # ue_registration_query_req_resp: <value in [allow, deny]>


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
