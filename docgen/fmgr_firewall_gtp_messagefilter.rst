:source: fmgr_firewall_gtp_messagefilter.py

:orphan:

.. _fmgr_firewall_gtp_messagefilter:

fmgr_firewall_gtp_messagefilter -- Message filter.
++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.2.0

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>



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
 <li><span class="li-head">revision_note</span> - The change note that can be specified when an object is created or updated. <span class="li-normal">type: string</span> <span class="li-required">required: false</span></li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">gtp</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_gtp_messagefilter</span> - Message filter. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">create_aa_pdp</span> <b>(Alias name: create-aa-pdp)</b>  Create aa pdp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">create_mbms</span> <b>(Alias name: create-mbms)</b>  Create mbms. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">create_pdp</span> <b>(Alias name: create-pdp)</b>  Create pdp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">data_record</span> <b>(Alias name: data-record)</b>  Data record. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_aa_pdp</span> <b>(Alias name: delete-aa-pdp)</b>  Delete aa pdp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_mbms</span> <b>(Alias name: delete-mbms)</b>  Delete mbms. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">delete_pdp</span> <b>(Alias name: delete-pdp)</b>  Delete pdp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">echo</span> Echo. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">error_indication</span> <b>(Alias name: error-indication)</b>  Error indication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">failure_report</span> <b>(Alias name: failure-report)</b>  Failure report. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">fwd_relocation</span> <b>(Alias name: fwd-relocation)</b>  Forward relocation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">fwd_srns_context</span> <b>(Alias name: fwd-srns-context)</b>  Forward srns context. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">gtp_pdu</span> <b>(Alias name: gtp-pdu)</b>  Gtp pdu. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">identification</span> Identification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">mbms_notification</span> <b>(Alias name: mbms-notification)</b>  Mbms notification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">node_alive</span> <b>(Alias name: node-alive)</b>  Node alive. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">note_ms_present</span> <b>(Alias name: note-ms-present)</b>  Note ms present. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">pdu_notification</span> <b>(Alias name: pdu-notification)</b>  Pdu notification. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">ran_info</span> <b>(Alias name: ran-info)</b>  Ran info. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">redirection</span> Redirection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">relocation_cancel</span> <b>(Alias name: relocation-cancel)</b>  Relocation cancel. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">send_route</span> <b>(Alias name: send-route)</b>  Send route. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">sgsn_context</span> <b>(Alias name: sgsn-context)</b>  Sgsn context. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">support_extension</span> <b>(Alias name: support-extension)</b>  Support extension. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">unknown_message_action</span> <b>(Alias name: unknown-message-action)</b>  Unknown message action. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">update_mbms</span> <b>(Alias name: update-mbms)</b>  Update mbms. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">update_pdp</span> <b>(Alias name: update-pdp)</b>  Update pdp. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
 </div>
 </li>
 <li><span class="li-head">version_not_support</span> <b>(Alias name: version-not-support)</b>  Version not supported. <span class="li-normal">type: str</span> <span class="li-normal">choices: [allow, deny]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.2.13</code></p>
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
      - name: Message filter.
        fortinet.fortimanager.fmgr_firewall_gtp_messagefilter:
          # bypass_validation: false
          # workspace_locking_adom: <global or your adom name>
          # workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          gtp: <your own value>
          firewall_gtp_messagefilter:
            # create_aa_pdp: <value in [allow, deny]>
            # create_mbms: <value in [allow, deny]>
            # create_pdp: <value in [allow, deny]>
            # data_record: <value in [allow, deny]>
            # delete_aa_pdp: <value in [allow, deny]>
            # delete_mbms: <value in [allow, deny]>
            # delete_pdp: <value in [allow, deny]>
            # echo: <value in [allow, deny]>
            # error_indication: <value in [allow, deny]>
            # failure_report: <value in [allow, deny]>
            # fwd_relocation: <value in [allow, deny]>
            # fwd_srns_context: <value in [allow, deny]>
            # gtp_pdu: <value in [allow, deny]>
            # identification: <value in [allow, deny]>
            # mbms_notification: <value in [allow, deny]>
            # node_alive: <value in [allow, deny]>
            # note_ms_present: <value in [allow, deny]>
            # pdu_notification: <value in [allow, deny]>
            # ran_info: <value in [allow, deny]>
            # redirection: <value in [allow, deny]>
            # relocation_cancel: <value in [allow, deny]>
            # send_route: <value in [allow, deny]>
            # sgsn_context: <value in [allow, deny]>
            # support_extension: <value in [allow, deny]>
            # unknown_message_action: <value in [allow, deny]>
            # update_mbms: <value in [allow, deny]>
            # update_pdp: <value in [allow, deny]>
            # version_not_support: <value in [allow, deny]>


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
