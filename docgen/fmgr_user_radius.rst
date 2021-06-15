:source: fmgr_user_radius.py

:orphan:

.. _fmgr_user_radius:

fmgr_user_radius -- Configure RADIUS server entries.
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device.
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0.


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.9.0



FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <br>
 <table>
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>user_radius</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 </tr>
 </table>
 <p>



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">user_radius</span> - Configure RADIUS server entries. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accounting-server</span> - No description for the parameter <span class="li-normal">type: array</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>accounting-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> - ID (0 - 4294967295). <span class="li-normal">type: int</span>  <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">port</span> - RADIUS accounting port number. <span class="li-normal">type: int</span>  <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>port</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">server</span> - {&lt;name_str|ip_str&gt;} Server CN domain name or IP. <span class="li-normal">type: str</span>  <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">source-ip</span> - Source IP address for communications to the RADIUS server. <span class="li-normal">type: str</span>  <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>source-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface</span> - Specify outgoing interface to reach server. <span class="li-normal">type: str</span>  <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface</td>
 <td>True</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface-select-method</span> - Specify how to select outgoing interface to reach server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span>  <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface-select-method</td>
 <td>True</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">acct-all-servers</span> - Enable/disable sending of accounting messages to all configured servers (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>acct-all-servers</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">acct-interim-interval</span> - Time in seconds between each accounting interim update message. <span class="li-normal">type: int</span>  <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>acct-interim-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">all-usergroup</span> - Enable/disable automatically including this RADIUS server in all user groups. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>all-usergroup</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auth-type</span> - Authentication methods/protocols permitted for this RADIUS server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pap, chap, ms_chap, ms_chap_v2, auto]</span>  <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>auth-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>class</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dynamic_mapping</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>_scope</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>name</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>vdom</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">acct-all-servers</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>acct-all-servers</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">acct-interim-interval</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>acct-interim-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">all-usergroup</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>all-usergroup</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auth-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pap, chap, ms_chap, ms_chap_v2, auto]</span>  <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>auth-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>class</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-carrier-endpoint-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-carrier-endpoint-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-carrier-endpoint-block-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-carrier-endpoint-block-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-context-timeout</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-context-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-flush-ip-session</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-flush-ip-session</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-hold-time</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-hold-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-http-header</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-http-header</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-http-header-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ip-header-address, default-profile]</span>  <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-http-header-fallback</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-http-header-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-http-header-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-http-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-http-header-suppress</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-log-dyn_flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span>  <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-log-dyn_flags</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-log-period</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-log-period</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-mem-percent</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-mem-percent</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-profile-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-profile-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-profile-attribute-key</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-profile-attribute-key</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-radius-response</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-radius-response</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-radius-server-port</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-radius-server-port</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dp-validate-request-secret</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dp-validate-request-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dynamic-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dynamic-profile</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">endpoint-translation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>endpoint-translation</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-convert-hex</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-convert-hex</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-header</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-header</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-header-suppress</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-prefix</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-range-max</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-prefix-range-max</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-range-min</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-prefix-range-min</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-string</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-prefix-string</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-carrier-endpoint-source</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-header, cookie]</span>  <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-carrier-endpoint-source</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-ip-header</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-ip-header</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-ip-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-ip-header-suppress</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-missing-header-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session-ip, policy-profile]</span>  <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-missing-header-fallback</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ep-profile-query-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session-ip, extract-ip, extract-carrier-endpoint]</span>  <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ep-profile-query-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">h3c-compatibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>h3c-compatibility</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nas-ip</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>nas-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">password-encoding</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ISO-8859-1, auto]</span>  <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>password-encoding</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">password-renewal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>password-renewal</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">radius-coa</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>radius-coa</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">radius-port</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>radius-port</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-context-timeout</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-context-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-endpoint-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-endpoint-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-endpoint-block-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-endpoint-block-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-ep-one-ip-only</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-ep-one-ip-only</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-flush-ip-session</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-flush-ip-session</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-log-flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span>  <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-log-flags</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-log-period</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-log-period</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-radius-response</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-radius-response</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-radius-server-port</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-radius-server-port</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-validate-request-secret</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-validate-request-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secondary-secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secondary-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secondary-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secondary-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">source-ip</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>source-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sso-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sso-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sso-attribute-key</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sso-attribute-key</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sso-attribute-value-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sso-attribute-value-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tertiary-secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>tertiary-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tertiary-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>tertiary-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">timeout</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">use-group-for-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>use-group-for-profile</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">use-management-vdom</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>use-management-vdom</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">username-case-sensitive</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>username-case-sensitive</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface</td>
 <td>True</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface-select-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span>  <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface-select-method</td>
 <td>True</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">group-override-attr-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [filter-Id, class]</span>  <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>group-override-attr-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-acct-fast-framedip-detect</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-acct-fast-framedip-detect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">accounting-server</span> - No description for the parameter <span class="li-normal">type: array</span>
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>accounting-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface-select-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span>  <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface-select-method</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>port</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">source-ip</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>source-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">switch-controller-service-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [login, framed, callback-login, callback-framed, outbound, administrative, nas-prompt, authenticate-only, callback-nas-prompt, call-check, callback-administrative]</span>  <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-service-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">h3c-compatibility</span> - Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>h3c-compatibility</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">name</span> - RADIUS server entry name. <span class="li-normal">type: str</span>  <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>name</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nas-ip</span> - IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes. <span class="li-normal">type: str</span>  <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>nas-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">password-encoding</span> - Password encoding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ISO-8859-1, auto]</span>  <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>password-encoding</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">password-renewal</span> - Enable/disable password renewal. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>password-renewal</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">radius-coa</span> - Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>radius-coa</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">radius-port</span> - RADIUS service port number. <span class="li-normal">type: int</span>  <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>radius-port</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso</span> - Enable/disable RADIUS based single sign on feature. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-context-timeout</span> - Time in seconds before the logged out user is removed from the "user context list" of logged on users. <span class="li-normal">type: int</span>  <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-context-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-endpoint-attribute</span> - RADIUS attributes used to extract the user end point identifer from the RADIUS Start record. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-endpoint-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-endpoint-block-attribute</span> - RADIUS attributes used to block a user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-endpoint-block-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-ep-one-ip-only</span> - Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-ep-one-ip-only</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-flush-ip-session</span> - Enable/disable flushing user IP sessions on RADIUS accounting Stop messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-flush-ip-session</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-log-flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span>  <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-log-flags</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-log-period</span> - Time interval in seconds that group event log messages will be generated for dynamic profile events. <span class="li-normal">type: int</span>  <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-log-period</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-radius-response</span> - Enable/disable sending RADIUS response packets after receiving Start and Stop records. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-radius-response</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-radius-server-port</span> - UDP port to listen on for RADIUS Start and Stop records. <span class="li-normal">type: int</span>  <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-radius-server-port</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rsso-validate-request-secret</span> - Enable/disable validating the RADIUS request shared secret in the Start or End record. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>rsso-validate-request-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secondary-secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secondary-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secondary-server</span> - {&lt;name_str|ip_str&gt;} secondary RADIUS CN domain name or IP. <span class="li-normal">type: str</span>  <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secondary-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">server</span> - Primary RADIUS server CN domain name or IP address. <span class="li-normal">type: str</span>  <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">source-ip</span> - Source IP address for communications to the RADIUS server. <span class="li-normal">type: str</span>  <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>source-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sso-attribute</span> - RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span>  <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sso-attribute</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sso-attribute-key</span> - Key prefix for SSO group value in the SSO attribute. <span class="li-normal">type: str</span>  <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sso-attribute-key</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sso-attribute-value-override</span> - Enable/disable override old attribute value with new value for the same endpoint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sso-attribute-value-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tertiary-secret</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>tertiary-secret</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tertiary-server</span> - {&lt;name_str|ip_str&gt;} tertiary RADIUS CN domain name or IP. <span class="li-normal">type: str</span>  <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>tertiary-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">timeout</span> - Time in seconds between re-sending authentication requests. <span class="li-normal">type: int</span>  <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">use-management-vdom</span> - Enable/disable using management VDOM to send requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>use-management-vdom</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">username-case-sensitive</span> - Enable/disable case sensitive user names. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>username-case-sensitive</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface</span> - Specify outgoing interface to reach server. <span class="li-normal">type: str</span>  <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface</td>
 <td>True</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface-select-method</span> - Specify how to select outgoing interface to reach server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span>  <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>interface-select-method</td>
 <td>True</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">group-override-attr-type</span> - RADIUS attribute type to override user group information. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [filter-Id, class]</span>  <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>group-override-attr-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-acct-fast-framedip-detect</span> - Switch controller accounting message Framed-IP detection from DHCP snooping (seconds, default=2). <span class="li-normal">type: int</span>  <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-acct-fast-framedip-detect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-service-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [login, framed, callback-login, callback-framed, outbound, administrative, nas-prompt, authenticate-only, callback-nas-prompt, call-check, callback-administrative]</span>  <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-service-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
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

 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Configure RADIUS server entries.
      fmgr_user_radius:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_radius:
            accounting-server:
              -
                  id: <value of integer>
                  port: <value of integer>
                  secret: <value of string>
                  server: <value of string>
                  source-ip: <value of string>
                  status: <value in [disable, enable]>
                  interface: <value of string>
                  interface-select-method: <value in [auto, sdwan, specify]>
            acct-all-servers: <value in [disable, enable]>
            acct-interim-interval: <value of integer>
            all-usergroup: <value in [disable, enable]>
            auth-type: <value in [pap, chap, ms_chap, ...]>
            class: <value of string>
            dynamic_mapping:
              -
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  acct-all-servers: <value in [disable, enable]>
                  acct-interim-interval: <value of integer>
                  all-usergroup: <value in [disable, enable]>
                  auth-type: <value in [pap, chap, ms_chap, ...]>
                  class: <value of string>
                  dp-carrier-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  dp-carrier-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  dp-context-timeout: <value of integer>
                  dp-flush-ip-session: <value in [disable, enable]>
                  dp-hold-time: <value of integer>
                  dp-http-header: <value of string>
                  dp-http-header-fallback: <value in [ip-header-address, default-profile]>
                  dp-http-header-status: <value in [disable, enable]>
                  dp-http-header-suppress: <value in [disable, enable]>
                  dp-log-dyn_flags:
                    - none
                    - protocol-error
                    - profile-missing
                    - context-missing
                    - accounting-stop-missed
                    - accounting-event
                    - radiusd-other
                    - endpoint-block
                  dp-log-period: <value of integer>
                  dp-mem-percent: <value of integer>
                  dp-profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  dp-profile-attribute-key: <value of string>
                  dp-radius-response: <value in [disable, enable]>
                  dp-radius-server-port: <value of integer>
                  dp-secret: <value of string>
                  dp-validate-request-secret: <value in [disable, enable]>
                  dynamic-profile: <value in [disable, enable]>
                  endpoint-translation: <value in [disable, enable]>
                  ep-carrier-endpoint-convert-hex: <value in [disable, enable]>
                  ep-carrier-endpoint-header: <value of string>
                  ep-carrier-endpoint-header-suppress: <value in [disable, enable]>
                  ep-carrier-endpoint-prefix: <value in [disable, enable]>
                  ep-carrier-endpoint-prefix-range-max: <value of integer>
                  ep-carrier-endpoint-prefix-range-min: <value of integer>
                  ep-carrier-endpoint-prefix-string: <value of string>
                  ep-carrier-endpoint-source: <value in [http-header, cookie]>
                  ep-ip-header: <value of string>
                  ep-ip-header-suppress: <value in [disable, enable]>
                  ep-missing-header-fallback: <value in [session-ip, policy-profile]>
                  ep-profile-query-type: <value in [session-ip, extract-ip, extract-carrier-endpoint]>
                  h3c-compatibility: <value in [disable, enable]>
                  nas-ip: <value of string>
                  password-encoding: <value in [ISO-8859-1, auto]>
                  password-renewal: <value in [disable, enable]>
                  radius-coa: <value in [disable, enable]>
                  radius-port: <value of integer>
                  rsso: <value in [disable, enable]>
                  rsso-context-timeout: <value of integer>
                  rsso-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  rsso-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  rsso-ep-one-ip-only: <value in [disable, enable]>
                  rsso-flush-ip-session: <value in [disable, enable]>
                  rsso-log-flags:
                    - none
                    - protocol-error
                    - profile-missing
                    - context-missing
                    - accounting-stop-missed
                    - accounting-event
                    - radiusd-other
                    - endpoint-block
                  rsso-log-period: <value of integer>
                  rsso-radius-response: <value in [disable, enable]>
                  rsso-radius-server-port: <value of integer>
                  rsso-secret: <value of string>
                  rsso-validate-request-secret: <value in [disable, enable]>
                  secondary-secret: <value of string>
                  secondary-server: <value of string>
                  secret: <value of string>
                  server: <value of string>
                  source-ip: <value of string>
                  sso-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  sso-attribute-key: <value of string>
                  sso-attribute-value-override: <value in [disable, enable]>
                  tertiary-secret: <value of string>
                  tertiary-server: <value of string>
                  timeout: <value of integer>
                  use-group-for-profile: <value in [disable, enable]>
                  use-management-vdom: <value in [disable, enable]>
                  username-case-sensitive: <value in [disable, enable]>
                  interface: <value of string>
                  interface-select-method: <value in [auto, sdwan, specify]>
                  group-override-attr-type: <value in [filter-Id, class]>
                  switch-controller-acct-fast-framedip-detect: <value of integer>
                  accounting-server:
                    -
                        id: <value of integer>
                        interface: <value of string>
                        interface-select-method: <value in [auto, sdwan, specify]>
                        port: <value of integer>
                        secret: <value of string>
                        server: <value of string>
                        source-ip: <value of string>
                        status: <value in [disable, enable]>
                  switch-controller-service-type:
                    - login
                    - framed
                    - callback-login
                    - callback-framed
                    - outbound
                    - administrative
                    - nas-prompt
                    - authenticate-only
                    - callback-nas-prompt
                    - call-check
                    - callback-administrative
            h3c-compatibility: <value in [disable, enable]>
            name: <value of string>
            nas-ip: <value of string>
            password-encoding: <value in [ISO-8859-1, auto]>
            password-renewal: <value in [disable, enable]>
            radius-coa: <value in [disable, enable]>
            radius-port: <value of integer>
            rsso: <value in [disable, enable]>
            rsso-context-timeout: <value of integer>
            rsso-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
            rsso-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
            rsso-ep-one-ip-only: <value in [disable, enable]>
            rsso-flush-ip-session: <value in [disable, enable]>
            rsso-log-flags:
              - none
              - protocol-error
              - profile-missing
              - context-missing
              - accounting-stop-missed
              - accounting-event
              - radiusd-other
              - endpoint-block
            rsso-log-period: <value of integer>
            rsso-radius-response: <value in [disable, enable]>
            rsso-radius-server-port: <value of integer>
            rsso-secret: <value of string>
            rsso-validate-request-secret: <value in [disable, enable]>
            secondary-secret: <value of string>
            secondary-server: <value of string>
            secret: <value of string>
            server: <value of string>
            source-ip: <value of string>
            sso-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
            sso-attribute-key: <value of string>
            sso-attribute-value-override: <value in [disable, enable]>
            tertiary-secret: <value of string>
            tertiary-server: <value of string>
            timeout: <value of integer>
            use-management-vdom: <value in [disable, enable]>
            username-case-sensitive: <value in [disable, enable]>
            interface: <value of string>
            interface-select-method: <value in [auto, sdwan, specify]>
            group-override-attr-type: <value in [filter-Id, class]>
            switch-controller-acct-fast-framedip-detect: <value of integer>
            switch-controller-service-type:
              - login
              - framed
              - callback-login
              - callback-framed
              - outbound
              - administrative
              - nas-prompt
              - authenticate-only
              - callback-nas-prompt
              - call-check
              - callback-administrative



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
 <li> <span class="li-return">response_data</span> - The data body of the api response <span class="li-normal">returned: optional</span> <span class="li-normal">type: list or dict</span></li>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



