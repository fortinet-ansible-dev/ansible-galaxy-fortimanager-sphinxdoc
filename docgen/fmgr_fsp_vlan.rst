:source: fmgr_fsp_vlan.py

:orphan:

.. _fmgr_fsp_vlan:

fmgr_fsp_vlan
+++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device.
- Examples include all parameters and values need to be adjusted to data sources before usage.



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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fsp_vlan</td>
 <td>yes</td>
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
 <li><span class="li-head">forticloud_access_token</span> - Access token of forticloud managed API users, this option is available with FortiManager later than 6.4.0 <span class="li-normal">type: str</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">fsp_vlan</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_dhcp-status</span> - _Dhcp-Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>_dhcp-status</td>
 <td>True</td>
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
 <li><span class="li-head">auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [radius, usergroup]</span>  <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auth</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">color</span> - Color. <span class="li-normal">type: int</span>  <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>color</td>
 <td>True</td>
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
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>comments</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dynamic_mapping</span> - Dynamic_Mapping. <span class="li-normal">type: array</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">_dhcp-status</span> - _Dhcp-Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>_dhcp-status</td>
 <td>True</td>
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
 <li><span class="li-head">_scope</span> - _Scope. <span class="li-normal">type: array</span>
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span>  <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vdom</span> - Vdom. <span class="li-normal">type: str</span>  <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">dhcp-server</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">auto-configuration</span> - Enable/disable auto configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auto-configuration</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auto-managed-status</span> - Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auto-managed-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">conflicted-ip-timeout</span> - Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused. <span class="li-normal">type: int</span>  <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>conflicted-ip-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-auth</span> - DDNS authentication mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tsig]</span>  <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-auth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-key</span> - DDNS update key (base 64 encoding). <span class="li-normal">type: str</span>  <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-key</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-keyname</span> - DDNS update key name. <span class="li-normal">type: str</span>  <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-keyname</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-server-ip</span> - DDNS server IP. <span class="li-normal">type: str</span>  <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-server-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-ttl</span> - TTL. <span class="li-normal">type: int</span>  <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-ttl</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-update</span> - Enable/disable DDNS update for DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-update</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-update-override</span> - Enable/disable DDNS update override for DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-update-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-zone</span> - Zone of your domain name (ex. <span class="li-normal">type: str</span>  <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-zone</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">default-gateway</span> - Default gateway IP address assigned by the DHCP server. <span class="li-normal">type: str</span>  <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>default-gateway</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-settings-from-fortiipam</span> - Enable/disable populating of DHCP server settings from FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-settings-from-fortiipam</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server1</span> - DNS server 1. <span class="li-normal">type: str</span>  <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server2</span> - DNS server 2. <span class="li-normal">type: str</span>  <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server3</span> - DNS server 3. <span class="li-normal">type: str</span>  <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server4</span> - DNS server 4. <span class="li-normal">type: str</span>  <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server4</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-service</span> - Options for assigning DNS servers to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span>  <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">domain</span> - Domain name suffix for the IP addresses that the DHCP server assigns to clients. <span class="li-normal">type: str</span>  <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>domain</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">enable</span> - Enable. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>enable</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">exclude-range</span> - Exclude-Range. <span class="li-normal">type: array</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>exclude-range</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - End of IP range. <span class="li-normal">type: str</span>  <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>end-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">start-ip</span> - Start of IP range. <span class="li-normal">type: str</span>  <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>start-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">filename</span> - Name of the boot file on the TFTP server. <span class="li-normal">type: str</span>  <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>filename</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">forticlient-on-net-status</span> - Enable/disable FortiClient-On-Net service for this DHCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>forticlient-on-net-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip-mode</span> - Method used to assign client IP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, usrgrp]</span>  <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip-range</span> - Ip-Range. <span class="li-normal">type: array</span>
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip-range</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - End of IP range. <span class="li-normal">type: str</span>  <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>end-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">start-ip</span> - Start of IP range. <span class="li-normal">type: str</span>  <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>start-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ipsec-lease-hold</span> - DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry). <span class="li-normal">type: int</span>  <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipsec-lease-hold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lease-time</span> - Lease time in seconds, 0 means unlimited. <span class="li-normal">type: int</span>  <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lease-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mac-acl-default-action</span> - MAC access control default action (allow or block assigning IP settings). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block]</span>  <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mac-acl-default-action</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">netmask</span> - Netmask assigned by the DHCP server. <span class="li-normal">type: str</span>  <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>netmask</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">next-server</span> - IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from. <span class="li-normal">type: str</span>  <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>next-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-server1</span> - NTP server 1. <span class="li-normal">type: str</span>  <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-server1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-server2</span> - NTP server 2. <span class="li-normal">type: str</span>  <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-server2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-server3</span> - NTP server 3. <span class="li-normal">type: str</span>  <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-server3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-service</span> - Options for assigning Network Time Protocol (NTP) servers to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span>  <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option1</span> - Option1. <span class="li-normal">type: str</span> <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option2</span> - Option2. <span class="li-normal">type: str</span> <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option3</span> - Option3. <span class="li-normal">type: str</span> <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option4</span> - Option4. <span class="li-normal">type: str</span>  <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option4</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option5</span> - Option5. <span class="li-normal">type: str</span>  <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option5</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option6</span> - Option6. <span class="li-normal">type: str</span>  <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">options</span> - Options. <span class="li-normal">type: array</span>
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>options</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">code</span> - DHCP option code. <span class="li-normal">type: int</span>  <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>code</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip</span> - DHCP option IPs. <span class="li-normal">type: str</span> <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string, ip, fqdn]</span>  <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">value</span> - DHCP option value. <span class="li-normal">type: str</span>  <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>value</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">reserved-address</span> - Reserved-Address. <span class="li-normal">type: array</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>reserved-address</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Options for the DHCP server to configure the client with the reserved MAC address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block, reserved]</span>  <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>action</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">circuit-id</span> - Option 82 circuit-ID of the client that will get the reserved IP address. <span class="li-normal">type: str</span>  <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>circuit-id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">circuit-id-type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span>  <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>circuit-id-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span>  <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>description</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip</span> - IP address to be reserved for the MAC address. <span class="li-normal">type: str</span>  <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mac</span> - MAC address of the client that will get the reserved IP address. <span class="li-normal">type: str</span>  <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mac</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">remote-id</span> - Option 82 remote-ID of the client that will get the reserved IP address. <span class="li-normal">type: str</span>  <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>remote-id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">remote-id-type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span>  <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>remote-id-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">type</span> - DHCP reserved-address type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mac, option82]</span>  <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">server-type</span> - DHCP server can be a normal DHCP server or an IPsec DHCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span>  <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>server-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Enable/disable this DHCP configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">tftp-server</span> - One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces. <span class="li-normal">type: str</span> <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tftp-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">timezone</span> - Select the time zone to be assigned to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]</span>  <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>timezone</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">timezone-option</span> - Options for the DHCP server to set the clients time zone. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, default, specify]</span>  <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>timezone-option</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vci-match</span> - Enable/disable vendor class identifier (VCI) matching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vci-match</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vci-string</span> - One or more VCI strings in quotes separated by spaces. <span class="li-normal">type: str</span> <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vci-string</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac-service</span> - Options for assigning WiFi Access Controllers to DHCP clients <span class="li-normal">type: str</span>  <span class="li-normal">choices: [specify, local]</span>  <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac1</span> - WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span>  <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac2</span> - WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span>  <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac3</span> - WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span>  <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wins-server1</span> - WINS server 1. <span class="li-normal">type: str</span>  <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wins-server1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wins-server2</span> - WINS server 2. <span class="li-normal">type: str</span>  <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wins-server2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">interface</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">dhcp-relay-agent-option</span> - Dhcp-Relay-Agent-Option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-agent-option</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-ip</span> - Dhcp-Relay-Ip. <span class="li-normal">type: str</span> <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-service</span> - Dhcp-Relay-Service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-type</span> - Dhcp-Relay-Type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span>  <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip</span> - Ip. <span class="li-normal">type: str</span>  <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv6</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">autoconf</span> - Enable/disable address auto config. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>autoconf</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-client-options</span> - Dhcp6-Client-Options. <span class="li-normal">type: array</span> <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span>  <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-client-options</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-information-request</span> - Enable/disable DHCPv6 information request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-information-request</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-delegation</span> - Enable/disable DHCPv6 prefix delegation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-delegation</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-hint</span> - DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server. <span class="li-normal">type: str</span>  <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-hint</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-hint-plt</span> - DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time. <span class="li-normal">type: int</span>  <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-hint-plt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-hint-vlt</span> - DHCPv6 prefix hint valid life time (sec). <span class="li-normal">type: int</span>  <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-hint-vlt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-relay-ip</span> - DHCPv6 relay IP address. <span class="li-normal">type: str</span>  <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-relay-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-relay-service</span> - Enable/disable DHCPv6 relay. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-relay-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-relay-type</span> - DHCPv6 relay type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span>  <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-relay-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">icmp6-send-redirect</span> - Enable/disable sending of ICMPv6 redirects. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>icmp6-send-redirect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface-identifier</span> - IPv6 interface identifier. <span class="li-normal">type: str</span>  <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>interface-identifier</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-address</span> - Primary IPv6 address prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx <span class="li-normal">type: str</span>  <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-address</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-allowaccess</span> - Allow management access to the interface. <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric]</span>  <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-allowaccess</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-default-life</span> - Default life (sec). <span class="li-normal">type: int</span>  <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-default-life</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-delegated-prefix-list</span> - Ip6-Delegated-Prefix-List. <span class="li-normal">type: array</span>
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-delegated-prefix-list</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - Enable/disable the autonomous flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>autonomous-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">onlink-flag</span> - Enable/disable the onlink flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>onlink-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">prefix-id</span> - Prefix ID. <span class="li-normal">type: int</span>  <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>prefix-id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> - Recursive DNS server option. <span class="li-normal">type: str</span> <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>rdnss</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rdnss-service</span> - Recursive DNS service option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [delegated, default, specify]</span>  <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>rdnss-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">subnet</span> - Add subnet ID to routing prefix. <span class="li-normal">type: str</span>  <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>subnet</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">upstream-interface</span> - Name of the interface that provides delegated information. <span class="li-normal">type: str</span>  <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>upstream-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">delegated-prefix-iaid</span> - IAID of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>  <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>delegated-prefix-iaid</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ip6-dns-server-override</span> - Enable/disable using the DNS server acquired by DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-dns-server-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-extra-addr</span> - Ip6-Extra-Addr. <span class="li-normal">type: array</span>
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-extra-addr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">prefix</span> - IPv6 address prefix. <span class="li-normal">type: str</span>  <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>prefix</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ip6-hop-limit</span> - Hop limit (0 means unspecified). <span class="li-normal">type: int</span>  <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-hop-limit</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-link-mtu</span> - IPv6 link MTU. <span class="li-normal">type: int</span>  <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-link-mtu</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-manage-flag</span> - Enable/disable the managed flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-manage-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-max-interval</span> - IPv6 maximum interval (4 to 1800 sec). <span class="li-normal">type: int</span>  <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-max-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-min-interval</span> - IPv6 minimum interval (3 to 1350 sec). <span class="li-normal">type: int</span>  <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-min-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-mode</span> - Addressing mode (static, DHCP, delegated). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span>  <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-other-flag</span> - Enable/disable the other IPv6 flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-other-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-prefix-list</span> - Ip6-Prefix-List. <span class="li-normal">type: array</span>
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-prefix-list</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - Enable/disable the autonomous flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>autonomous-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dnssl</span> - DNS search list option. <span class="li-normal">type: str</span> <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dnssl</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">onlink-flag</span> - Enable/disable the onlink flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>onlink-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">preferred-life-time</span> - Preferred life time (sec). <span class="li-normal">type: int</span>  <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>preferred-life-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">prefix</span> - IPv6 prefix. <span class="li-normal">type: str</span>  <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>prefix</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> - Recursive DNS server option. <span class="li-normal">type: str</span> <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>rdnss</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">valid-life-time</span> - Valid life time (sec). <span class="li-normal">type: int</span>  <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>valid-life-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ip6-reachable-time</span> - IPv6 reachable time (milliseconds; 0 means unspecified). <span class="li-normal">type: int</span>  <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-reachable-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-retrans-time</span> - IPv6 retransmit time (milliseconds; 0 means unspecified). <span class="li-normal">type: int</span>  <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-retrans-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-send-adv</span> - Enable/disable sending advertisements about the interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-send-adv</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-subnet</span> - Subnet to routing prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx <span class="li-normal">type: str</span>  <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-subnet</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-upstream-interface</span> - Interface name providing delegated information. <span class="li-normal">type: str</span>  <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-upstream-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-cert</span> - Neighbor discovery certificate. <span class="li-normal">type: str</span>  <a id='label276' href="javascript:ContentClick('label277', 'label276');" onmouseover="ContentPreview('label277');" onmouseout="ContentUnpreview('label277');" title="click to collapse or expand..."> more... </a>
 <div id="label277" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-cert</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-cga-modifier</span> - Neighbor discovery CGA modifier. <span class="li-normal">type: str</span>  <a id='label278' href="javascript:ContentClick('label279', 'label278');" onmouseover="ContentPreview('label279');" onmouseout="ContentUnpreview('label279');" title="click to collapse or expand..."> more... </a>
 <div id="label279" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-cga-modifier</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-mode</span> - Neighbor discovery mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [basic, SEND-compatible]</span>  <a id='label280' href="javascript:ContentClick('label281', 'label280');" onmouseover="ContentPreview('label281');" onmouseout="ContentUnpreview('label281');" title="click to collapse or expand..."> more... </a>
 <div id="label281" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-security-level</span> - Neighbor discovery security level (0 - 7; 0 = least secure, default = 0). <span class="li-normal">type: int</span>  <a id='label282' href="javascript:ContentClick('label283', 'label282');" onmouseover="ContentPreview('label283');" onmouseout="ContentUnpreview('label283');" title="click to collapse or expand..."> more... </a>
 <div id="label283" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-security-level</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-timestamp-delta</span> - Neighbor discovery timestamp delta value (1 - 3600 sec; default = 300). <span class="li-normal">type: int</span>  <a id='label284' href="javascript:ContentClick('label285', 'label284');" onmouseover="ContentPreview('label285');" onmouseout="ContentUnpreview('label285');" title="click to collapse or expand..."> more... </a>
 <div id="label285" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-timestamp-delta</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-timestamp-fuzz</span> - Neighbor discovery timestamp fuzz factor (1 - 60 sec; default = 1). <span class="li-normal">type: int</span>  <a id='label286' href="javascript:ContentClick('label287', 'label286');" onmouseover="ContentPreview('label287');" onmouseout="ContentUnpreview('label287');" title="click to collapse or expand..."> more... </a>
 <div id="label287" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-timestamp-fuzz</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">unique-autoconf-addr</span> - Enable/disable unique auto config address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label288' href="javascript:ContentClick('label289', 'label288');" onmouseover="ContentPreview('label289');" onmouseout="ContentUnpreview('label289');" title="click to collapse or expand..."> more... </a>
 <div id="label289" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>unique-autoconf-addr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrip6_link_local</span> - Link-local IPv6 address of virtual router. <span class="li-normal">type: str</span>  <a id='label290' href="javascript:ContentClick('label291', 'label290');" onmouseover="ContentPreview('label291');" onmouseout="ContentUnpreview('label291');" title="click to collapse or expand..."> more... </a>
 <div id="label291" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrip6_link_local</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrrp-virtual-mac6</span> - Enable/disable virtual MAC for VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label292' href="javascript:ContentClick('label293', 'label292');" onmouseover="ContentPreview('label293');" onmouseout="ContentUnpreview('label293');" title="click to collapse or expand..."> more... </a>
 <div id="label293" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrrp-virtual-mac6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrrp6</span> - Vrrp6. <span class="li-normal">type: array</span>
 <a id='label294' href="javascript:ContentClick('label295', 'label294');" onmouseover="ContentPreview('label295');" onmouseout="ContentUnpreview('label295');" title="click to collapse or expand..."> more... </a>
 <div id="label295" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrrp6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - Enable/disable accept mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label296' href="javascript:ContentClick('label297', 'label296');" onmouseover="ContentPreview('label297');" onmouseout="ContentUnpreview('label297');" title="click to collapse or expand..."> more... </a>
 <div id="label297" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>accept-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">adv-interval</span> - Advertisement interval (1 - 255 seconds). <span class="li-normal">type: int</span>  <a id='label298' href="javascript:ContentClick('label299', 'label298');" onmouseover="ContentPreview('label299');" onmouseout="ContentUnpreview('label299');" title="click to collapse or expand..."> more... </a>
 <div id="label299" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>adv-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">preempt</span> - Enable/disable preempt mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label300' href="javascript:ContentClick('label301', 'label300');" onmouseover="ContentPreview('label301');" onmouseout="ContentUnpreview('label301');" title="click to collapse or expand..."> more... </a>
 <div id="label301" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>preempt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">priority</span> - Priority of the virtual router (1 - 255). <span class="li-normal">type: int</span>  <a id='label302' href="javascript:ContentClick('label303', 'label302');" onmouseover="ContentPreview('label303');" onmouseout="ContentUnpreview('label303');" title="click to collapse or expand..."> more... </a>
 <div id="label303" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">start-time</span> - Startup time (1 - 255 seconds). <span class="li-normal">type: int</span>  <a id='label304' href="javascript:ContentClick('label305', 'label304');" onmouseover="ContentPreview('label305');" onmouseout="ContentUnpreview('label305');" title="click to collapse or expand..."> more... </a>
 <div id="label305" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>start-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Enable/disable VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label306' href="javascript:ContentClick('label307', 'label306');" onmouseover="ContentPreview('label307');" onmouseout="ContentUnpreview('label307');" title="click to collapse or expand..."> more... </a>
 <div id="label307" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">vrdst6</span> - Monitor the route to this destination. <span class="li-normal">type: str</span>  <a id='label308' href="javascript:ContentClick('label309', 'label308');" onmouseover="ContentPreview('label309');" onmouseout="ContentUnpreview('label309');" title="click to collapse or expand..."> more... </a>
 <div id="label309" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrdst6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrgrp</span> - VRRP group ID (1 - 65535). <span class="li-normal">type: int</span>  <a id='label310' href="javascript:ContentClick('label311', 'label310');" onmouseover="ContentPreview('label311');" onmouseout="ContentUnpreview('label311');" title="click to collapse or expand..."> more... </a>
 <div id="label311" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrgrp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrid</span> - Virtual router identifier (1 - 255). <span class="li-normal">type: int</span>  <a id='label312' href="javascript:ContentClick('label313', 'label312');" onmouseover="ContentPreview('label313');" onmouseout="ContentUnpreview('label313');" title="click to collapse or expand..."> more... </a>
 <div id="label313" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrip6</span> - IPv6 address of the virtual router. <span class="li-normal">type: str</span>  <a id='label314' href="javascript:ContentClick('label315', 'label314');" onmouseover="ContentPreview('label315');" onmouseout="ContentUnpreview('label315');" title="click to collapse or expand..."> more... </a>
 <div id="label315" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrip6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">cli-conn6-status</span> - Cli-Conn6-Status. <span class="li-normal">type: int</span>  <a id='label316' href="javascript:ContentClick('label317', 'label316');" onmouseover="ContentPreview('label317');" onmouseout="ContentUnpreview('label317');" title="click to collapse or expand..."> more... </a>
 <div id="label317" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>cli-conn6-status</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-prefix-mode</span> - Assigning a prefix from DHCP or RA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhcp6, ra]</span>  <a id='label318' href="javascript:ContentClick('label319', 'label318');" onmouseover="ContentPreview('label319');" onmouseout="ContentUnpreview('label319');" title="click to collapse or expand..."> more... </a>
 <div id="label319" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-prefix-mode</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ra-send-mtu</span> - Enable/disable sending link MTU in RA packet. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label320' href="javascript:ContentClick('label321', 'label320');" onmouseover="ContentPreview('label321');" onmouseout="ContentUnpreview('label321');" title="click to collapse or expand..."> more... </a>
 <div id="label321" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ra-send-mtu</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-delegated-prefix-iaid</span> - IAID of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>  <a id='label322' href="javascript:ContentClick('label323', 'label322');" onmouseover="ContentPreview('label323');" onmouseout="ContentUnpreview('label323');" title="click to collapse or expand..."> more... </a>
 <div id="label323" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-delegated-prefix-iaid</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">secondary-IP</span> - Secondary-Ip. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label324' href="javascript:ContentClick('label325', 'label324');" onmouseover="ContentPreview('label325');" onmouseout="ContentUnpreview('label325');" title="click to collapse or expand..."> more... </a>
 <div id="label325" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>secondary-IP</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secondaryip</span> - Secondaryip. <span class="li-normal">type: array</span>
 <a id='label326' href="javascript:ContentClick('label327', 'label326');" onmouseover="ContentPreview('label327');" onmouseout="ContentUnpreview('label327');" title="click to collapse or expand..."> more... </a>
 <div id="label327" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>secondaryip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> - Management access settings for the secondary IP address. <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test]</span>  <a id='label328' href="javascript:ContentClick('label329', 'label328');" onmouseover="ContentPreview('label329');" onmouseout="ContentUnpreview('label329');" title="click to collapse or expand..."> more... </a>
 <div id="label329" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>allowaccess</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">detectprotocol</span> - Protocols used to detect the server. <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span>  <a id='label330' href="javascript:ContentClick('label331', 'label330');" onmouseover="ContentPreview('label331');" onmouseout="ContentUnpreview('label331');" title="click to collapse or expand..."> more... </a>
 <div id="label331" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>detectprotocol</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">detectserver</span> - Gateways ping server for this IP. <span class="li-normal">type: str</span>  <a id='label332' href="javascript:ContentClick('label333', 'label332');" onmouseover="ContentPreview('label333');" onmouseout="ContentUnpreview('label333');" title="click to collapse or expand..."> more... </a>
 <div id="label333" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>detectserver</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">gwdetect</span> - Enable/disable detect gateway alive for first. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label334' href="javascript:ContentClick('label335', 'label334');" onmouseover="ContentPreview('label335');" onmouseout="ContentUnpreview('label335');" title="click to collapse or expand..."> more... </a>
 <div id="label335" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>gwdetect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ha-priority</span> - HA election priority for the PING server. <span class="li-normal">type: int</span>  <a id='label336' href="javascript:ContentClick('label337', 'label336');" onmouseover="ContentPreview('label337');" onmouseout="ContentUnpreview('label337');" title="click to collapse or expand..."> more... </a>
 <div id="label337" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ha-priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label338' href="javascript:ContentClick('label339', 'label338');" onmouseover="ContentPreview('label339');" onmouseout="ContentUnpreview('label339');" title="click to collapse or expand..."> more... </a>
 <div id="label339" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip</span> - Secondary IP address of the interface. <span class="li-normal">type: str</span>  <a id='label340' href="javascript:ContentClick('label341', 'label340');" onmouseover="ContentPreview('label341');" onmouseout="ContentUnpreview('label341');" title="click to collapse or expand..."> more... </a>
 <div id="label341" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ping-serv-status</span> - Ping-Serv-Status. <span class="li-normal">type: int</span>  <a id='label342' href="javascript:ContentClick('label343', 'label342');" onmouseover="ContentPreview('label343');" onmouseout="ContentUnpreview('label343');" title="click to collapse or expand..."> more... </a>
 <div id="label343" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ping-serv-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">seq</span> - Seq. <span class="li-normal">type: int</span>  <a id='label344' href="javascript:ContentClick('label345', 'label344');" onmouseover="ContentPreview('label345');" onmouseout="ContentUnpreview('label345');" title="click to collapse or expand..."> more... </a>
 <div id="label345" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>seq</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">vlanid</span> - Vlanid. <span class="li-normal">type: int</span>  <a id='label346' href="javascript:ContentClick('label347', 'label346');" onmouseover="ContentPreview('label347');" onmouseout="ContentUnpreview('label347');" title="click to collapse or expand..."> more... </a>
 <div id="label347" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vlanid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-interface-select-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span>  <a id='label348' href="javascript:ContentClick('label349', 'label348');" onmouseover="ContentPreview('label349');" onmouseout="ContentUnpreview('label349');" title="click to collapse or expand..."> more... </a>
 <div id="label349" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-interface-select-method</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 </ul>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span>  <a id='label350' href="javascript:ContentClick('label351', 'label350');" onmouseover="ContentPreview('label351');" onmouseout="ContentUnpreview('label351');" title="click to collapse or expand..."> more... </a>
 <div id="label351" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">portal-message-override-group</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label352' href="javascript:ContentClick('label353', 'label352');" onmouseover="ContentPreview('label353');" onmouseout="ContentUnpreview('label353');" title="click to collapse or expand..."> more... </a>
 <div id="label353" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>portal-message-override-group</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">radius-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label354' href="javascript:ContentClick('label355', 'label354');" onmouseover="ContentPreview('label355');" onmouseout="ContentUnpreview('label355');" title="click to collapse or expand..."> more... </a>
 <div id="label355" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>radius-server</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [open, captive-portal, 8021x]</span>  <a id='label356' href="javascript:ContentClick('label357', 'label356');" onmouseover="ContentPreview('label357');" onmouseout="ContentUnpreview('label357');" title="click to collapse or expand..."> more... </a>
 <div id="label357" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">selected-usergroups</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label358' href="javascript:ContentClick('label359', 'label358');" onmouseover="ContentPreview('label359');" onmouseout="ContentUnpreview('label359');" title="click to collapse or expand..."> more... </a>
 <div id="label359" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>selected-usergroups</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">usergroup</span> - No description for the parameter <span class="li-normal">type: str</span>  <a id='label360' href="javascript:ContentClick('label361', 'label360');" onmouseover="ContentPreview('label361');" onmouseout="ContentUnpreview('label361');" title="click to collapse or expand..."> more... </a>
 <div id="label361" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>usergroup</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vdom</span> - Vdom. <span class="li-normal">type: str</span>  <a id='label362' href="javascript:ContentClick('label363', 'label362');" onmouseover="ContentPreview('label363');" onmouseout="ContentUnpreview('label363');" title="click to collapse or expand..."> more... </a>
 <div id="label363" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlanid</span> - Vlanid. <span class="li-normal">type: int</span>  <a id='label364' href="javascript:ContentClick('label365', 'label364');" onmouseover="ContentPreview('label365');" onmouseout="ContentUnpreview('label365');" title="click to collapse or expand..."> more... </a>
 <div id="label365" style="display:none">
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vlanid</td>
 <td>True</td>
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
 <li><span class="li-head">dhcp-server</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">auto-configuration</span> - Enable/disable auto configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label366' href="javascript:ContentClick('label367', 'label366');" onmouseover="ContentPreview('label367');" onmouseout="ContentUnpreview('label367');" title="click to collapse or expand..."> more... </a>
 <div id="label367" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auto-configuration</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auto-managed-status</span> - Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label368' href="javascript:ContentClick('label369', 'label368');" onmouseover="ContentPreview('label369');" onmouseout="ContentUnpreview('label369');" title="click to collapse or expand..."> more... </a>
 <div id="label369" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auto-managed-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">conflicted-ip-timeout</span> - Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused. <span class="li-normal">type: int</span>  <a id='label370' href="javascript:ContentClick('label371', 'label370');" onmouseover="ContentPreview('label371');" onmouseout="ContentUnpreview('label371');" title="click to collapse or expand..."> more... </a>
 <div id="label371" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>conflicted-ip-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-auth</span> - DDNS authentication mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tsig]</span>  <a id='label372' href="javascript:ContentClick('label373', 'label372');" onmouseover="ContentPreview('label373');" onmouseout="ContentUnpreview('label373');" title="click to collapse or expand..."> more... </a>
 <div id="label373" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-auth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-key</span> - DDNS update key (base 64 encoding). <span class="li-normal">type: str</span>  <a id='label374' href="javascript:ContentClick('label375', 'label374');" onmouseover="ContentPreview('label375');" onmouseout="ContentUnpreview('label375');" title="click to collapse or expand..."> more... </a>
 <div id="label375" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-key</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-keyname</span> - DDNS update key name. <span class="li-normal">type: str</span>  <a id='label376' href="javascript:ContentClick('label377', 'label376');" onmouseover="ContentPreview('label377');" onmouseout="ContentUnpreview('label377');" title="click to collapse or expand..."> more... </a>
 <div id="label377" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-keyname</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-server-ip</span> - DDNS server IP. <span class="li-normal">type: str</span>  <a id='label378' href="javascript:ContentClick('label379', 'label378');" onmouseover="ContentPreview('label379');" onmouseout="ContentUnpreview('label379');" title="click to collapse or expand..."> more... </a>
 <div id="label379" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-server-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-ttl</span> - TTL. <span class="li-normal">type: int</span>  <a id='label380' href="javascript:ContentClick('label381', 'label380');" onmouseover="ContentPreview('label381');" onmouseout="ContentUnpreview('label381');" title="click to collapse or expand..."> more... </a>
 <div id="label381" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-ttl</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-update</span> - Enable/disable DDNS update for DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label382' href="javascript:ContentClick('label383', 'label382');" onmouseover="ContentPreview('label383');" onmouseout="ContentUnpreview('label383');" title="click to collapse or expand..."> more... </a>
 <div id="label383" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-update</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-update-override</span> - Enable/disable DDNS update override for DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label384' href="javascript:ContentClick('label385', 'label384');" onmouseover="ContentPreview('label385');" onmouseout="ContentUnpreview('label385');" title="click to collapse or expand..."> more... </a>
 <div id="label385" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-update-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-zone</span> - Zone of your domain name (ex. <span class="li-normal">type: str</span>  <a id='label386' href="javascript:ContentClick('label387', 'label386');" onmouseover="ContentPreview('label387');" onmouseout="ContentUnpreview('label387');" title="click to collapse or expand..."> more... </a>
 <div id="label387" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-zone</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">default-gateway</span> - Default gateway IP address assigned by the DHCP server. <span class="li-normal">type: str</span>  <a id='label388' href="javascript:ContentClick('label389', 'label388');" onmouseover="ContentPreview('label389');" onmouseout="ContentUnpreview('label389');" title="click to collapse or expand..."> more... </a>
 <div id="label389" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>default-gateway</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-settings-from-fortiipam</span> - Enable/disable populating of DHCP server settings from FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label390' href="javascript:ContentClick('label391', 'label390');" onmouseover="ContentPreview('label391');" onmouseout="ContentUnpreview('label391');" title="click to collapse or expand..."> more... </a>
 <div id="label391" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-settings-from-fortiipam</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server1</span> - DNS server 1. <span class="li-normal">type: str</span>  <a id='label392' href="javascript:ContentClick('label393', 'label392');" onmouseover="ContentPreview('label393');" onmouseout="ContentUnpreview('label393');" title="click to collapse or expand..."> more... </a>
 <div id="label393" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server2</span> - DNS server 2. <span class="li-normal">type: str</span>  <a id='label394' href="javascript:ContentClick('label395', 'label394');" onmouseover="ContentPreview('label395');" onmouseout="ContentUnpreview('label395');" title="click to collapse or expand..."> more... </a>
 <div id="label395" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server3</span> - DNS server 3. <span class="li-normal">type: str</span>  <a id='label396' href="javascript:ContentClick('label397', 'label396');" onmouseover="ContentPreview('label397');" onmouseout="ContentUnpreview('label397');" title="click to collapse or expand..."> more... </a>
 <div id="label397" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server4</span> - DNS server 4. <span class="li-normal">type: str</span>  <a id='label398' href="javascript:ContentClick('label399', 'label398');" onmouseover="ContentPreview('label399');" onmouseout="ContentUnpreview('label399');" title="click to collapse or expand..."> more... </a>
 <div id="label399" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server4</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-service</span> - Options for assigning DNS servers to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span>  <a id='label400' href="javascript:ContentClick('label401', 'label400');" onmouseover="ContentPreview('label401');" onmouseout="ContentUnpreview('label401');" title="click to collapse or expand..."> more... </a>
 <div id="label401" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">domain</span> - Domain name suffix for the IP addresses that the DHCP server assigns to clients. <span class="li-normal">type: str</span>  <a id='label402' href="javascript:ContentClick('label403', 'label402');" onmouseover="ContentPreview('label403');" onmouseout="ContentUnpreview('label403');" title="click to collapse or expand..."> more... </a>
 <div id="label403" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>domain</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">enable</span> - Enable. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label404' href="javascript:ContentClick('label405', 'label404');" onmouseover="ContentPreview('label405');" onmouseout="ContentUnpreview('label405');" title="click to collapse or expand..."> more... </a>
 <div id="label405" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>enable</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">exclude-range</span> - Exclude-Range. <span class="li-normal">type: array</span>
 <a id='label406' href="javascript:ContentClick('label407', 'label406');" onmouseover="ContentPreview('label407');" onmouseout="ContentUnpreview('label407');" title="click to collapse or expand..."> more... </a>
 <div id="label407" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>exclude-range</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - End of IP range. <span class="li-normal">type: str</span>  <a id='label408' href="javascript:ContentClick('label409', 'label408');" onmouseover="ContentPreview('label409');" onmouseout="ContentUnpreview('label409');" title="click to collapse or expand..."> more... </a>
 <div id="label409" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>end-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label410' href="javascript:ContentClick('label411', 'label410');" onmouseover="ContentPreview('label411');" onmouseout="ContentUnpreview('label411');" title="click to collapse or expand..."> more... </a>
 <div id="label411" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">start-ip</span> - Start of IP range. <span class="li-normal">type: str</span>  <a id='label412' href="javascript:ContentClick('label413', 'label412');" onmouseover="ContentPreview('label413');" onmouseout="ContentUnpreview('label413');" title="click to collapse or expand..."> more... </a>
 <div id="label413" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>start-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">filename</span> - Name of the boot file on the TFTP server. <span class="li-normal">type: str</span>  <a id='label414' href="javascript:ContentClick('label415', 'label414');" onmouseover="ContentPreview('label415');" onmouseout="ContentUnpreview('label415');" title="click to collapse or expand..."> more... </a>
 <div id="label415" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>filename</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">forticlient-on-net-status</span> - Enable/disable FortiClient-On-Net service for this DHCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label416' href="javascript:ContentClick('label417', 'label416');" onmouseover="ContentPreview('label417');" onmouseout="ContentUnpreview('label417');" title="click to collapse or expand..."> more... </a>
 <div id="label417" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>forticlient-on-net-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label418' href="javascript:ContentClick('label419', 'label418');" onmouseover="ContentPreview('label419');" onmouseout="ContentUnpreview('label419');" title="click to collapse or expand..."> more... </a>
 <div id="label419" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip-mode</span> - Method used to assign client IP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, usrgrp]</span>  <a id='label420' href="javascript:ContentClick('label421', 'label420');" onmouseover="ContentPreview('label421');" onmouseout="ContentUnpreview('label421');" title="click to collapse or expand..."> more... </a>
 <div id="label421" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip-range</span> - Ip-Range. <span class="li-normal">type: array</span>
 <a id='label422' href="javascript:ContentClick('label423', 'label422');" onmouseover="ContentPreview('label423');" onmouseout="ContentUnpreview('label423');" title="click to collapse or expand..."> more... </a>
 <div id="label423" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip-range</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - End of IP range. <span class="li-normal">type: str</span>  <a id='label424' href="javascript:ContentClick('label425', 'label424');" onmouseover="ContentPreview('label425');" onmouseout="ContentUnpreview('label425');" title="click to collapse or expand..."> more... </a>
 <div id="label425" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>end-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label426' href="javascript:ContentClick('label427', 'label426');" onmouseover="ContentPreview('label427');" onmouseout="ContentUnpreview('label427');" title="click to collapse or expand..."> more... </a>
 <div id="label427" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">start-ip</span> - Start of IP range. <span class="li-normal">type: str</span>  <a id='label428' href="javascript:ContentClick('label429', 'label428');" onmouseover="ContentPreview('label429');" onmouseout="ContentUnpreview('label429');" title="click to collapse or expand..."> more... </a>
 <div id="label429" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>start-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ipsec-lease-hold</span> - DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry). <span class="li-normal">type: int</span>  <a id='label430' href="javascript:ContentClick('label431', 'label430');" onmouseover="ContentPreview('label431');" onmouseout="ContentUnpreview('label431');" title="click to collapse or expand..."> more... </a>
 <div id="label431" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipsec-lease-hold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lease-time</span> - Lease time in seconds, 0 means unlimited. <span class="li-normal">type: int</span>  <a id='label432' href="javascript:ContentClick('label433', 'label432');" onmouseover="ContentPreview('label433');" onmouseout="ContentUnpreview('label433');" title="click to collapse or expand..."> more... </a>
 <div id="label433" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lease-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mac-acl-default-action</span> - MAC access control default action (allow or block assigning IP settings). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block]</span>  <a id='label434' href="javascript:ContentClick('label435', 'label434');" onmouseover="ContentPreview('label435');" onmouseout="ContentUnpreview('label435');" title="click to collapse or expand..."> more... </a>
 <div id="label435" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mac-acl-default-action</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">netmask</span> - Netmask assigned by the DHCP server. <span class="li-normal">type: str</span>  <a id='label436' href="javascript:ContentClick('label437', 'label436');" onmouseover="ContentPreview('label437');" onmouseout="ContentUnpreview('label437');" title="click to collapse or expand..."> more... </a>
 <div id="label437" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>netmask</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">next-server</span> - IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from. <span class="li-normal">type: str</span>  <a id='label438' href="javascript:ContentClick('label439', 'label438');" onmouseover="ContentPreview('label439');" onmouseout="ContentUnpreview('label439');" title="click to collapse or expand..."> more... </a>
 <div id="label439" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>next-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-server1</span> - NTP server 1. <span class="li-normal">type: str</span>  <a id='label440' href="javascript:ContentClick('label441', 'label440');" onmouseover="ContentPreview('label441');" onmouseout="ContentUnpreview('label441');" title="click to collapse or expand..."> more... </a>
 <div id="label441" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-server1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-server2</span> - NTP server 2. <span class="li-normal">type: str</span>  <a id='label442' href="javascript:ContentClick('label443', 'label442');" onmouseover="ContentPreview('label443');" onmouseout="ContentUnpreview('label443');" title="click to collapse or expand..."> more... </a>
 <div id="label443" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-server2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-server3</span> - NTP server 3. <span class="li-normal">type: str</span>  <a id='label444' href="javascript:ContentClick('label445', 'label444');" onmouseover="ContentPreview('label445');" onmouseout="ContentUnpreview('label445');" title="click to collapse or expand..."> more... </a>
 <div id="label445" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-server3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ntp-service</span> - Options for assigning Network Time Protocol (NTP) servers to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span>  <a id='label446' href="javascript:ContentClick('label447', 'label446');" onmouseover="ContentPreview('label447');" onmouseout="ContentUnpreview('label447');" title="click to collapse or expand..."> more... </a>
 <div id="label447" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ntp-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option1</span> - Option1. <span class="li-normal">type: str</span> <a id='label448' href="javascript:ContentClick('label449', 'label448');" onmouseover="ContentPreview('label449');" onmouseout="ContentUnpreview('label449');" title="click to collapse or expand..."> more... </a>
 <div id="label449" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option2</span> - Option2. <span class="li-normal">type: str</span> <a id='label450' href="javascript:ContentClick('label451', 'label450');" onmouseover="ContentPreview('label451');" onmouseout="ContentUnpreview('label451');" title="click to collapse or expand..."> more... </a>
 <div id="label451" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option3</span> - Option3. <span class="li-normal">type: str</span> <a id='label452' href="javascript:ContentClick('label453', 'label452');" onmouseover="ContentPreview('label453');" onmouseout="ContentUnpreview('label453');" title="click to collapse or expand..."> more... </a>
 <div id="label453" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option4</span> - Option4. <span class="li-normal">type: str</span>  <a id='label454' href="javascript:ContentClick('label455', 'label454');" onmouseover="ContentPreview('label455');" onmouseout="ContentUnpreview('label455');" title="click to collapse or expand..."> more... </a>
 <div id="label455" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option4</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option5</span> - Option5. <span class="li-normal">type: str</span>  <a id='label456' href="javascript:ContentClick('label457', 'label456');" onmouseover="ContentPreview('label457');" onmouseout="ContentUnpreview('label457');" title="click to collapse or expand..."> more... </a>
 <div id="label457" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option5</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">option6</span> - Option6. <span class="li-normal">type: str</span>  <a id='label458' href="javascript:ContentClick('label459', 'label458');" onmouseover="ContentPreview('label459');" onmouseout="ContentUnpreview('label459');" title="click to collapse or expand..."> more... </a>
 <div id="label459" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>option6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">options</span> - Options. <span class="li-normal">type: array</span>
 <a id='label460' href="javascript:ContentClick('label461', 'label460');" onmouseover="ContentPreview('label461');" onmouseout="ContentUnpreview('label461');" title="click to collapse or expand..."> more... </a>
 <div id="label461" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>options</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">code</span> - DHCP option code. <span class="li-normal">type: int</span>  <a id='label462' href="javascript:ContentClick('label463', 'label462');" onmouseover="ContentPreview('label463');" onmouseout="ContentUnpreview('label463');" title="click to collapse or expand..."> more... </a>
 <div id="label463" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>code</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label464' href="javascript:ContentClick('label465', 'label464');" onmouseover="ContentPreview('label465');" onmouseout="ContentUnpreview('label465');" title="click to collapse or expand..."> more... </a>
 <div id="label465" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip</span> - DHCP option IPs. <span class="li-normal">type: str</span> <a id='label466' href="javascript:ContentClick('label467', 'label466');" onmouseover="ContentPreview('label467');" onmouseout="ContentUnpreview('label467');" title="click to collapse or expand..."> more... </a>
 <div id="label467" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string, ip, fqdn]</span>  <a id='label468' href="javascript:ContentClick('label469', 'label468');" onmouseover="ContentPreview('label469');" onmouseout="ContentUnpreview('label469');" title="click to collapse or expand..."> more... </a>
 <div id="label469" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">value</span> - DHCP option value. <span class="li-normal">type: str</span>  <a id='label470' href="javascript:ContentClick('label471', 'label470');" onmouseover="ContentPreview('label471');" onmouseout="ContentUnpreview('label471');" title="click to collapse or expand..."> more... </a>
 <div id="label471" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>value</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">reserved-address</span> - Reserved-Address. <span class="li-normal">type: array</span>
 <a id='label472' href="javascript:ContentClick('label473', 'label472');" onmouseover="ContentPreview('label473');" onmouseout="ContentUnpreview('label473');" title="click to collapse or expand..."> more... </a>
 <div id="label473" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>reserved-address</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Options for the DHCP server to configure the client with the reserved MAC address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block, reserved]</span>  <a id='label474' href="javascript:ContentClick('label475', 'label474');" onmouseover="ContentPreview('label475');" onmouseout="ContentUnpreview('label475');" title="click to collapse or expand..."> more... </a>
 <div id="label475" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>action</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">circuit-id</span> - Option 82 circuit-ID of the client that will get the reserved IP address. <span class="li-normal">type: str</span>  <a id='label476' href="javascript:ContentClick('label477', 'label476');" onmouseover="ContentPreview('label477');" onmouseout="ContentUnpreview('label477');" title="click to collapse or expand..."> more... </a>
 <div id="label477" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>circuit-id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">circuit-id-type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span>  <a id='label478' href="javascript:ContentClick('label479', 'label478');" onmouseover="ContentPreview('label479');" onmouseout="ContentUnpreview('label479');" title="click to collapse or expand..."> more... </a>
 <div id="label479" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>circuit-id-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span>  <a id='label480' href="javascript:ContentClick('label481', 'label480');" onmouseover="ContentPreview('label481');" onmouseout="ContentUnpreview('label481');" title="click to collapse or expand..."> more... </a>
 <div id="label481" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>description</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label482' href="javascript:ContentClick('label483', 'label482');" onmouseover="ContentPreview('label483');" onmouseout="ContentUnpreview('label483');" title="click to collapse or expand..."> more... </a>
 <div id="label483" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip</span> - IP address to be reserved for the MAC address. <span class="li-normal">type: str</span>  <a id='label484' href="javascript:ContentClick('label485', 'label484');" onmouseover="ContentPreview('label485');" onmouseout="ContentUnpreview('label485');" title="click to collapse or expand..."> more... </a>
 <div id="label485" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mac</span> - MAC address of the client that will get the reserved IP address. <span class="li-normal">type: str</span>  <a id='label486' href="javascript:ContentClick('label487', 'label486');" onmouseover="ContentPreview('label487');" onmouseout="ContentUnpreview('label487');" title="click to collapse or expand..."> more... </a>
 <div id="label487" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mac</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">remote-id</span> - Option 82 remote-ID of the client that will get the reserved IP address. <span class="li-normal">type: str</span>  <a id='label488' href="javascript:ContentClick('label489', 'label488');" onmouseover="ContentPreview('label489');" onmouseout="ContentUnpreview('label489');" title="click to collapse or expand..."> more... </a>
 <div id="label489" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>remote-id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">remote-id-type</span> - DHCP option type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span>  <a id='label490' href="javascript:ContentClick('label491', 'label490');" onmouseover="ContentPreview('label491');" onmouseout="ContentUnpreview('label491');" title="click to collapse or expand..."> more... </a>
 <div id="label491" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>remote-id-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">type</span> - DHCP reserved-address type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mac, option82]</span>  <a id='label492' href="javascript:ContentClick('label493', 'label492');" onmouseover="ContentPreview('label493');" onmouseout="ContentUnpreview('label493');" title="click to collapse or expand..."> more... </a>
 <div id="label493" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">server-type</span> - DHCP server can be a normal DHCP server or an IPsec DHCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span>  <a id='label494' href="javascript:ContentClick('label495', 'label494');" onmouseover="ContentPreview('label495');" onmouseout="ContentUnpreview('label495');" title="click to collapse or expand..."> more... </a>
 <div id="label495" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>server-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Enable/disable this DHCP configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label496' href="javascript:ContentClick('label497', 'label496');" onmouseover="ContentPreview('label497');" onmouseout="ContentUnpreview('label497');" title="click to collapse or expand..."> more... </a>
 <div id="label497" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">tftp-server</span> - One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces. <span class="li-normal">type: str</span> <a id='label498' href="javascript:ContentClick('label499', 'label498');" onmouseover="ContentPreview('label499');" onmouseout="ContentUnpreview('label499');" title="click to collapse or expand..."> more... </a>
 <div id="label499" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tftp-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">timezone</span> - Select the time zone to be assigned to DHCP clients. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]</span>  <a id='label500' href="javascript:ContentClick('label501', 'label500');" onmouseover="ContentPreview('label501');" onmouseout="ContentUnpreview('label501');" title="click to collapse or expand..."> more... </a>
 <div id="label501" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>timezone</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">timezone-option</span> - Options for the DHCP server to set the clients time zone. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, default, specify]</span>  <a id='label502' href="javascript:ContentClick('label503', 'label502');" onmouseover="ContentPreview('label503');" onmouseout="ContentUnpreview('label503');" title="click to collapse or expand..."> more... </a>
 <div id="label503" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>timezone-option</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vci-match</span> - Enable/disable vendor class identifier (VCI) matching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label504' href="javascript:ContentClick('label505', 'label504');" onmouseover="ContentPreview('label505');" onmouseout="ContentUnpreview('label505');" title="click to collapse or expand..."> more... </a>
 <div id="label505" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vci-match</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vci-string</span> - One or more VCI strings in quotes separated by spaces. <span class="li-normal">type: str</span> <a id='label506' href="javascript:ContentClick('label507', 'label506');" onmouseover="ContentPreview('label507');" onmouseout="ContentUnpreview('label507');" title="click to collapse or expand..."> more... </a>
 <div id="label507" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vci-string</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac-service</span> - Options for assigning WiFi Access Controllers to DHCP clients <span class="li-normal">type: str</span>  <span class="li-normal">choices: [specify, local]</span>  <a id='label508' href="javascript:ContentClick('label509', 'label508');" onmouseover="ContentPreview('label509');" onmouseout="ContentUnpreview('label509');" title="click to collapse or expand..."> more... </a>
 <div id="label509" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac1</span> - WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span>  <a id='label510' href="javascript:ContentClick('label511', 'label510');" onmouseover="ContentPreview('label511');" onmouseout="ContentUnpreview('label511');" title="click to collapse or expand..."> more... </a>
 <div id="label511" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac2</span> - WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span>  <a id='label512' href="javascript:ContentClick('label513', 'label512');" onmouseover="ContentPreview('label513');" onmouseout="ContentUnpreview('label513');" title="click to collapse or expand..."> more... </a>
 <div id="label513" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ac3</span> - WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417). <span class="li-normal">type: str</span>  <a id='label514' href="javascript:ContentClick('label515', 'label514');" onmouseover="ContentPreview('label515');" onmouseout="ContentUnpreview('label515');" title="click to collapse or expand..."> more... </a>
 <div id="label515" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ac3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wins-server1</span> - WINS server 1. <span class="li-normal">type: str</span>  <a id='label516' href="javascript:ContentClick('label517', 'label516');" onmouseover="ContentPreview('label517');" onmouseout="ContentUnpreview('label517');" title="click to collapse or expand..."> more... </a>
 <div id="label517" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wins-server1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wins-server2</span> - WINS server 2. <span class="li-normal">type: str</span>  <a id='label518' href="javascript:ContentClick('label519', 'label518');" onmouseover="ContentPreview('label519');" onmouseout="ContentUnpreview('label519');" title="click to collapse or expand..."> more... </a>
 <div id="label519" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wins-server2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">interface</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">ac-name</span> - PPPoE server name. <span class="li-normal">type: str</span>  <a id='label520' href="javascript:ContentClick('label521', 'label520');" onmouseover="ContentPreview('label521');" onmouseout="ContentUnpreview('label521');" title="click to collapse or expand..."> more... </a>
 <div id="label521" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ac-name</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">aggregate</span> - Aggregate. <span class="li-normal">type: str</span>  <a id='label522' href="javascript:ContentClick('label523', 'label522');" onmouseover="ContentPreview('label523');" onmouseout="ContentUnpreview('label523');" title="click to collapse or expand..."> more... </a>
 <div id="label523" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>aggregate</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">algorithm</span> - Frame distribution algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [L2, L3, L4, LB]</span>  <a id='label524' href="javascript:ContentClick('label525', 'label524');" onmouseover="ContentPreview('label525');" onmouseout="ContentUnpreview('label525');" title="click to collapse or expand..."> more... </a>
 <div id="label525" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>algorithm</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">alias</span> - Alias will be displayed with the interface name to make it easier to distinguish. <span class="li-normal">type: str</span>  <a id='label526' href="javascript:ContentClick('label527', 'label526');" onmouseover="ContentPreview('label527');" onmouseout="ContentUnpreview('label527');" title="click to collapse or expand..."> more... </a>
 <div id="label527" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>alias</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">allowaccess</span> - Permitted types of management access to this interface. <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test]</span>  <a id='label528' href="javascript:ContentClick('label529', 'label528');" onmouseover="ContentPreview('label529');" onmouseout="ContentUnpreview('label529');" title="click to collapse or expand..."> more... </a>
 <div id="label529" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>allowaccess</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ap-discover</span> - Enable/disable automatic registration of unknown FortiAP devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label530' href="javascript:ContentClick('label531', 'label530');" onmouseover="ContentPreview('label531');" onmouseout="ContentUnpreview('label531');" title="click to collapse or expand..."> more... </a>
 <div id="label531" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ap-discover</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">arpforward</span> - Enable/disable ARP forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label532' href="javascript:ContentClick('label533', 'label532');" onmouseover="ContentPreview('label533');" onmouseout="ContentUnpreview('label533');" title="click to collapse or expand..."> more... </a>
 <div id="label533" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>arpforward</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">atm-protocol</span> - ATM protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, ipoa]</span>  <a id='label534' href="javascript:ContentClick('label535', 'label534');" onmouseover="ContentPreview('label535');" onmouseout="ContentUnpreview('label535');" title="click to collapse or expand..."> more... </a>
 <div id="label535" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>atm-protocol</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auth-type</span> - PPP authentication type to use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span>  <a id='label536' href="javascript:ContentClick('label537', 'label536');" onmouseover="ContentPreview('label537');" onmouseout="ContentUnpreview('label537');" title="click to collapse or expand..."> more... </a>
 <div id="label537" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auth-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auto-auth-extension-device</span> - Enable/disable automatic authorization of dedicated Fortinet extension device on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label538' href="javascript:ContentClick('label539', 'label538');" onmouseover="ContentPreview('label539');" onmouseout="ContentUnpreview('label539');" title="click to collapse or expand..."> more... </a>
 <div id="label539" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auto-auth-extension-device</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">bandwidth-measure-time</span> - Bandwidth measure time <span class="li-normal">type: int</span>  <a id='label540' href="javascript:ContentClick('label541', 'label540');" onmouseover="ContentPreview('label541');" onmouseout="ContentUnpreview('label541');" title="click to collapse or expand..."> more... </a>
 <div id="label541" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>bandwidth-measure-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">bfd</span> - Bidirectional Forwarding Detection (BFD) settings. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, enable, disable]</span>  <a id='label542' href="javascript:ContentClick('label543', 'label542');" onmouseover="ContentPreview('label543');" onmouseout="ContentUnpreview('label543');" title="click to collapse or expand..."> more... </a>
 <div id="label543" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>bfd</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">bfd-desired-min-tx</span> - BFD desired minimal transmit interval. <span class="li-normal">type: int</span>  <a id='label544' href="javascript:ContentClick('label545', 'label544');" onmouseover="ContentPreview('label545');" onmouseout="ContentUnpreview('label545');" title="click to collapse or expand..."> more... </a>
 <div id="label545" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>bfd-desired-min-tx</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">bfd-detect-mult</span> - BFD detection multiplier. <span class="li-normal">type: int</span>  <a id='label546' href="javascript:ContentClick('label547', 'label546');" onmouseover="ContentPreview('label547');" onmouseout="ContentUnpreview('label547');" title="click to collapse or expand..."> more... </a>
 <div id="label547" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>bfd-detect-mult</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">bfd-required-min-rx</span> - BFD required minimal receive interval. <span class="li-normal">type: int</span>  <a id='label548' href="javascript:ContentClick('label549', 'label548');" onmouseover="ContentPreview('label549');" onmouseout="ContentUnpreview('label549');" title="click to collapse or expand..."> more... </a>
 <div id="label549" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>bfd-required-min-rx</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">broadcast-forticlient-discovery</span> - Broadcast-Forticlient-Discovery. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label550' href="javascript:ContentClick('label551', 'label550');" onmouseover="ContentPreview('label551');" onmouseout="ContentUnpreview('label551');" title="click to collapse or expand..."> more... </a>
 <div id="label551" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>broadcast-forticlient-discovery</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">broadcast-forward</span> - Enable/disable broadcast forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label552' href="javascript:ContentClick('label553', 'label552');" onmouseover="ContentPreview('label553');" onmouseout="ContentUnpreview('label553');" title="click to collapse or expand..."> more... </a>
 <div id="label553" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>broadcast-forward</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">captive-portal</span> - Enable/disable captive portal. <span class="li-normal">type: int</span>  <a id='label554' href="javascript:ContentClick('label555', 'label554');" onmouseover="ContentPreview('label555');" onmouseout="ContentUnpreview('label555');" title="click to collapse or expand..."> more... </a>
 <div id="label555" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>captive-portal</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">cli-conn-status</span> - Cli-Conn-Status. <span class="li-normal">type: int</span>  <a id='label556' href="javascript:ContentClick('label557', 'label556');" onmouseover="ContentPreview('label557');" onmouseout="ContentUnpreview('label557');" title="click to collapse or expand..."> more... </a>
 <div id="label557" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>cli-conn-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span>  <a id='label558' href="javascript:ContentClick('label559', 'label558');" onmouseover="ContentPreview('label559');" onmouseout="ContentUnpreview('label559');" title="click to collapse or expand..."> more... </a>
 <div id="label559" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>color</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns</span> - Ddns. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label560' href="javascript:ContentClick('label561', 'label560');" onmouseover="ContentPreview('label561');" onmouseout="ContentUnpreview('label561');" title="click to collapse or expand..."> more... </a>
 <div id="label561" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-auth</span> - Ddns-Auth. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tsig]</span>  <a id='label562' href="javascript:ContentClick('label563', 'label562');" onmouseover="ContentPreview('label563');" onmouseout="ContentUnpreview('label563');" title="click to collapse or expand..."> more... </a>
 <div id="label563" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-auth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-domain</span> - Ddns-Domain. <span class="li-normal">type: str</span>  <a id='label564' href="javascript:ContentClick('label565', 'label564');" onmouseover="ContentPreview('label565');" onmouseout="ContentUnpreview('label565');" title="click to collapse or expand..."> more... </a>
 <div id="label565" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-domain</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-key</span> - Ddns-Key. <span class="li-normal">type: str</span>  <a id='label566' href="javascript:ContentClick('label567', 'label566');" onmouseover="ContentPreview('label567');" onmouseout="ContentUnpreview('label567');" title="click to collapse or expand..."> more... </a>
 <div id="label567" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-key</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-keyname</span> - Ddns-Keyname. <span class="li-normal">type: str</span>  <a id='label568' href="javascript:ContentClick('label569', 'label568');" onmouseover="ContentPreview('label569');" onmouseout="ContentUnpreview('label569');" title="click to collapse or expand..."> more... </a>
 <div id="label569" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-keyname</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-password</span> - Ddns-Password. <span class="li-normal">type: str</span> <a id='label570' href="javascript:ContentClick('label571', 'label570');" onmouseover="ContentPreview('label571');" onmouseout="ContentUnpreview('label571');" title="click to collapse or expand..."> more... </a>
 <div id="label571" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-password</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-server</span> - Ddns-Server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhs.org, dyndns.org, dyns.net, tzo.com, ods.org, vavic.com, now.net.cn, dipdns.net, easydns.com, genericDDNS]</span>  <a id='label572' href="javascript:ContentClick('label573', 'label572');" onmouseover="ContentPreview('label573');" onmouseout="ContentUnpreview('label573');" title="click to collapse or expand..."> more... </a>
 <div id="label573" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-server-ip</span> - Ddns-Server-Ip. <span class="li-normal">type: str</span>  <a id='label574' href="javascript:ContentClick('label575', 'label574');" onmouseover="ContentPreview('label575');" onmouseout="ContentUnpreview('label575');" title="click to collapse or expand..."> more... </a>
 <div id="label575" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-server-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-sn</span> - Ddns-Sn. <span class="li-normal">type: str</span>  <a id='label576' href="javascript:ContentClick('label577', 'label576');" onmouseover="ContentPreview('label577');" onmouseout="ContentUnpreview('label577');" title="click to collapse or expand..."> more... </a>
 <div id="label577" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-sn</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-ttl</span> - Ddns-Ttl. <span class="li-normal">type: int</span>  <a id='label578' href="javascript:ContentClick('label579', 'label578');" onmouseover="ContentPreview('label579');" onmouseout="ContentUnpreview('label579');" title="click to collapse or expand..."> more... </a>
 <div id="label579" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-ttl</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-username</span> - Ddns-Username. <span class="li-normal">type: str</span>  <a id='label580' href="javascript:ContentClick('label581', 'label580');" onmouseover="ContentPreview('label581');" onmouseout="ContentUnpreview('label581');" title="click to collapse or expand..."> more... </a>
 <div id="label581" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-username</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ddns-zone</span> - Ddns-Zone. <span class="li-normal">type: str</span>  <a id='label582' href="javascript:ContentClick('label583', 'label582');" onmouseover="ContentPreview('label583');" onmouseout="ContentUnpreview('label583');" title="click to collapse or expand..."> more... </a>
 <div id="label583" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ddns-zone</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dedicated-to</span> - Configure interface for single purpose. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, management]</span>  <a id='label584' href="javascript:ContentClick('label585', 'label584');" onmouseover="ContentPreview('label585');" onmouseout="ContentUnpreview('label585');" title="click to collapse or expand..."> more... </a>
 <div id="label585" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dedicated-to</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">defaultgw</span> - Enable to get the gateway IP from the DHCP or PPPoE server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label586' href="javascript:ContentClick('label587', 'label586');" onmouseover="ContentPreview('label587');" onmouseout="ContentUnpreview('label587');" title="click to collapse or expand..."> more... </a>
 <div id="label587" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>defaultgw</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span>  <a id='label588' href="javascript:ContentClick('label589', 'label588');" onmouseover="ContentPreview('label589');" onmouseout="ContentUnpreview('label589');" title="click to collapse or expand..."> more... </a>
 <div id="label589" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>description</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">detected-peer-mtu</span> - Detected-Peer-Mtu. <span class="li-normal">type: int</span>  <a id='label590' href="javascript:ContentClick('label591', 'label590');" onmouseover="ContentPreview('label591');" onmouseout="ContentUnpreview('label591');" title="click to collapse or expand..."> more... </a>
 <div id="label591" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>detected-peer-mtu</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">detectprotocol</span> - Protocols used to detect the server. <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span>  <a id='label592' href="javascript:ContentClick('label593', 'label592');" onmouseover="ContentPreview('label593');" onmouseout="ContentUnpreview('label593');" title="click to collapse or expand..."> more... </a>
 <div id="label593" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>detectprotocol</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">detectserver</span> - Gateways ping server for this IP. <span class="li-normal">type: str</span>  <a id='label594' href="javascript:ContentClick('label595', 'label594');" onmouseover="ContentPreview('label595');" onmouseout="ContentUnpreview('label595');" title="click to collapse or expand..."> more... </a>
 <div id="label595" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>detectserver</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">device-access-list</span> - Device-Access-List. <span class="li-normal">type: str</span>  <a id='label596' href="javascript:ContentClick('label597', 'label596');" onmouseover="ContentPreview('label597');" onmouseout="ContentUnpreview('label597');" title="click to collapse or expand..."> more... </a>
 <div id="label597" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>device-access-list</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">device-identification</span> - Enable/disable passively gathering of device identity information about the devices on the network connected to this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label598' href="javascript:ContentClick('label599', 'label598');" onmouseover="ContentPreview('label599');" onmouseout="ContentUnpreview('label599');" title="click to collapse or expand..."> more... </a>
 <div id="label599" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>device-identification</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">device-identification-active-scan</span> - Device-Identification-Active-Scan. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label600' href="javascript:ContentClick('label601', 'label600');" onmouseover="ContentPreview('label601');" onmouseout="ContentUnpreview('label601');" title="click to collapse or expand..."> more... </a>
 <div id="label601" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>device-identification-active-scan</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">device-netscan</span> - Device-Netscan. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label602' href="javascript:ContentClick('label603', 'label602');" onmouseover="ContentPreview('label603');" onmouseout="ContentUnpreview('label603');" title="click to collapse or expand..."> more... </a>
 <div id="label603" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>device-netscan</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">device-user-identification</span> - Enable/disable passive gathering of user identity information about users on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label604' href="javascript:ContentClick('label605', 'label604');" onmouseover="ContentPreview('label605');" onmouseout="ContentUnpreview('label605');" title="click to collapse or expand..."> more... </a>
 <div id="label605" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>device-user-identification</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">devindex</span> - Devindex. <span class="li-normal">type: int</span>  <a id='label606' href="javascript:ContentClick('label607', 'label606');" onmouseover="ContentPreview('label607');" onmouseout="ContentUnpreview('label607');" title="click to collapse or expand..."> more... </a>
 <div id="label607" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>devindex</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-client-identifier</span> - DHCP client identifier. <span class="li-normal">type: str</span>  <a id='label608' href="javascript:ContentClick('label609', 'label608');" onmouseover="ContentPreview('label609');" onmouseout="ContentUnpreview('label609');" title="click to collapse or expand..."> more... </a>
 <div id="label609" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-client-identifier</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-agent-option</span> - Enable/disable DHCP relay agent option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label610' href="javascript:ContentClick('label611', 'label610');" onmouseover="ContentPreview('label611');" onmouseout="ContentUnpreview('label611');" title="click to collapse or expand..."> more... </a>
 <div id="label611" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-agent-option</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-interface</span> - Specify outgoing interface to reach server. <span class="li-normal">type: str</span>  <a id='label612' href="javascript:ContentClick('label613', 'label612');" onmouseover="ContentPreview('label613');" onmouseout="ContentUnpreview('label613');" title="click to collapse or expand..."> more... </a>
 <div id="label613" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-interface-select-method</span> - Specify how to select outgoing interface to reach server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, sdwan, specify]</span>  <a id='label614' href="javascript:ContentClick('label615', 'label614');" onmouseover="ContentPreview('label615');" onmouseout="ContentUnpreview('label615');" title="click to collapse or expand..."> more... </a>
 <div id="label615" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-interface-select-method</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-ip</span> - DHCP relay IP address. <span class="li-normal">type: str</span> <a id='label616' href="javascript:ContentClick('label617', 'label616');" onmouseover="ContentPreview('label617');" onmouseout="ContentUnpreview('label617');" title="click to collapse or expand..."> more... </a>
 <div id="label617" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-service</span> - Enable/disable allowing this interface to act as a DHCP relay. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label618' href="javascript:ContentClick('label619', 'label618');" onmouseover="ContentPreview('label619');" onmouseout="ContentUnpreview('label619');" title="click to collapse or expand..."> more... </a>
 <div id="label619" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-type</span> - DHCP relay type (regular or IPsec). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span>  <a id='label620' href="javascript:ContentClick('label621', 'label620');" onmouseover="ContentPreview('label621');" onmouseout="ContentUnpreview('label621');" title="click to collapse or expand..."> more... </a>
 <div id="label621" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-renew-time</span> - DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server. <span class="li-normal">type: int</span>  <a id='label622' href="javascript:ContentClick('label623', 'label622');" onmouseover="ContentPreview('label623');" onmouseout="ContentUnpreview('label623');" title="click to collapse or expand..."> more... </a>
 <div id="label623" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-renew-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">disc-retry-timeout</span> - Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout. <span class="li-normal">type: int</span>  <a id='label624' href="javascript:ContentClick('label625', 'label624');" onmouseover="ContentPreview('label625');" onmouseout="ContentUnpreview('label625');" title="click to collapse or expand..."> more... </a>
 <div id="label625" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>disc-retry-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">disconnect-threshold</span> - Time in milliseconds to wait before sending a notification that this interface is down or disconnected. <span class="li-normal">type: int</span>  <a id='label626' href="javascript:ContentClick('label627', 'label626');" onmouseover="ContentPreview('label627');" onmouseout="ContentUnpreview('label627');" title="click to collapse or expand..."> more... </a>
 <div id="label627" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>disconnect-threshold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">distance</span> - Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route. <span class="li-normal">type: int</span>  <a id='label628' href="javascript:ContentClick('label629', 'label628');" onmouseover="ContentPreview('label629');" onmouseout="ContentUnpreview('label629');" title="click to collapse or expand..."> more... </a>
 <div id="label629" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>distance</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-query</span> - Dns-Query. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, recursive, non-recursive]</span>  <a id='label630' href="javascript:ContentClick('label631', 'label630');" onmouseover="ContentPreview('label631');" onmouseout="ContentUnpreview('label631');" title="click to collapse or expand..."> more... </a>
 <div id="label631" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-query</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server-override</span> - Enable/disable use DNS acquired by DHCP or PPPoE. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label632' href="javascript:ContentClick('label633', 'label632');" onmouseover="ContentPreview('label633');" onmouseout="ContentUnpreview('label633');" title="click to collapse or expand..."> more... </a>
 <div id="label633" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">drop-fragment</span> - Enable/disable drop fragment packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label634' href="javascript:ContentClick('label635', 'label634');" onmouseover="ContentPreview('label635');" onmouseout="ContentUnpreview('label635');" title="click to collapse or expand..."> more... </a>
 <div id="label635" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>drop-fragment</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">drop-overlapped-fragment</span> - Enable/disable drop overlapped fragment packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label636' href="javascript:ContentClick('label637', 'label636');" onmouseover="ContentPreview('label637');" onmouseout="ContentUnpreview('label637');" title="click to collapse or expand..."> more... </a>
 <div id="label637" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>drop-overlapped-fragment</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">egress-cos</span> - Override outgoing CoS in user VLAN tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span>  <a id='label638' href="javascript:ContentClick('label639', 'label638');" onmouseover="ContentPreview('label639');" onmouseout="ContentUnpreview('label639');" title="click to collapse or expand..."> more... </a>
 <div id="label639" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>egress-cos</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">egress-shaping-profile</span> - Outgoing traffic shaping profile. <span class="li-normal">type: str</span>  <a id='label640' href="javascript:ContentClick('label641', 'label640');" onmouseover="ContentPreview('label641');" onmouseout="ContentUnpreview('label641');" title="click to collapse or expand..."> more... </a>
 <div id="label641" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>egress-shaping-profile</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">eip</span> - Eip. <span class="li-normal">type: str</span>  <a id='label642' href="javascript:ContentClick('label643', 'label642');" onmouseover="ContentPreview('label643');" onmouseout="ContentUnpreview('label643');" title="click to collapse or expand..."> more... </a>
 <div id="label643" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>eip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">endpoint-compliance</span> - Endpoint-Compliance. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label644' href="javascript:ContentClick('label645', 'label644');" onmouseover="ContentPreview('label645');" onmouseout="ContentUnpreview('label645');" title="click to collapse or expand..."> more... </a>
 <div id="label645" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>endpoint-compliance</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">estimated-downstream-bandwidth</span> - Estimated maximum downstream bandwidth (kbps). <span class="li-normal">type: int</span>  <a id='label646' href="javascript:ContentClick('label647', 'label646');" onmouseover="ContentPreview('label647');" onmouseout="ContentUnpreview('label647');" title="click to collapse or expand..."> more... </a>
 <div id="label647" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>estimated-downstream-bandwidth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">estimated-upstream-bandwidth</span> - Estimated maximum upstream bandwidth (kbps). <span class="li-normal">type: int</span>  <a id='label648' href="javascript:ContentClick('label649', 'label648');" onmouseover="ContentPreview('label649');" onmouseout="ContentUnpreview('label649');" title="click to collapse or expand..."> more... </a>
 <div id="label649" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>estimated-upstream-bandwidth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">explicit-ftp-proxy</span> - Enable/disable the explicit FTP proxy on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label650' href="javascript:ContentClick('label651', 'label650');" onmouseover="ContentPreview('label651');" onmouseout="ContentUnpreview('label651');" title="click to collapse or expand..."> more... </a>
 <div id="label651" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>explicit-ftp-proxy</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">explicit-web-proxy</span> - Enable/disable the explicit web proxy on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label652' href="javascript:ContentClick('label653', 'label652');" onmouseover="ContentPreview('label653');" onmouseout="ContentUnpreview('label653');" title="click to collapse or expand..."> more... </a>
 <div id="label653" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>explicit-web-proxy</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">external</span> - Enable/disable identifying the interface as an external interface (which usually means its connected to the Internet). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label654' href="javascript:ContentClick('label655', 'label654');" onmouseover="ContentPreview('label655');" onmouseout="ContentUnpreview('label655');" title="click to collapse or expand..."> more... </a>
 <div id="label655" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>external</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fail-action-on-extender</span> - Action on extender when interface fail . <span class="li-normal">type: str</span>  <span class="li-normal">choices: [soft-restart, hard-restart, reboot]</span>  <a id='label656' href="javascript:ContentClick('label657', 'label656');" onmouseover="ContentPreview('label657');" onmouseout="ContentUnpreview('label657');" title="click to collapse or expand..."> more... </a>
 <div id="label657" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fail-action-on-extender</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fail-alert-interfaces</span> - Names of the FortiGate interfaces to which the link failure alert is sent. <span class="li-normal">type: str</span>  <a id='label658' href="javascript:ContentClick('label659', 'label658');" onmouseover="ContentPreview('label659');" onmouseout="ContentUnpreview('label659');" title="click to collapse or expand..."> more... </a>
 <div id="label659" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fail-alert-interfaces</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fail-alert-method</span> - Select link-failed-signal or link-down method to alert about a failed link. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [link-failed-signal, link-down]</span>  <a id='label660' href="javascript:ContentClick('label661', 'label660');" onmouseover="ContentPreview('label661');" onmouseout="ContentUnpreview('label661');" title="click to collapse or expand..."> more... </a>
 <div id="label661" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fail-alert-method</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fail-detect</span> - Enable/disable fail detection features for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label662' href="javascript:ContentClick('label663', 'label662');" onmouseover="ContentPreview('label663');" onmouseout="ContentUnpreview('label663');" title="click to collapse or expand..."> more... </a>
 <div id="label663" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fail-detect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fail-detect-option</span> - Options for detecting that this interface has failed. <span class="li-normal">type: array</span> <span class="li-normal">choices: [detectserver, link-down]</span>  <a id='label664' href="javascript:ContentClick('label665', 'label664');" onmouseover="ContentPreview('label665');" onmouseout="ContentUnpreview('label665');" title="click to collapse or expand..."> more... </a>
 <div id="label665" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fail-detect-option</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fdp</span> - Fdp. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label666' href="javascript:ContentClick('label667', 'label666');" onmouseover="ContentPreview('label667');" onmouseout="ContentUnpreview('label667');" title="click to collapse or expand..."> more... </a>
 <div id="label667" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fdp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fortiheartbeat</span> - Fortiheartbeat. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label668' href="javascript:ContentClick('label669', 'label668');" onmouseover="ContentPreview('label669');" onmouseout="ContentUnpreview('label669');" title="click to collapse or expand..."> more... </a>
 <div id="label669" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fortiheartbeat</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fortilink</span> - Enable FortiLink to dedicate this interface to manage other Fortinet devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label670' href="javascript:ContentClick('label671', 'label670');" onmouseover="ContentPreview('label671');" onmouseout="ContentUnpreview('label671');" title="click to collapse or expand..."> more... </a>
 <div id="label671" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fortilink</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fortilink-backup-link</span> - Fortilink-Backup-Link. <span class="li-normal">type: int</span>  <a id='label672' href="javascript:ContentClick('label673', 'label672');" onmouseover="ContentPreview('label673');" onmouseout="ContentUnpreview('label673');" title="click to collapse or expand..."> more... </a>
 <div id="label673" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fortilink-backup-link</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fortilink-neighbor-detect</span> - Protocol for FortiGate neighbor discovery. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [lldp, fortilink]</span>  <a id='label674' href="javascript:ContentClick('label675', 'label674');" onmouseover="ContentPreview('label675');" onmouseout="ContentUnpreview('label675');" title="click to collapse or expand..."> more... </a>
 <div id="label675" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fortilink-neighbor-detect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fortilink-split-interface</span> - Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label676' href="javascript:ContentClick('label677', 'label676');" onmouseover="ContentPreview('label677');" onmouseout="ContentUnpreview('label677');" title="click to collapse or expand..."> more... </a>
 <div id="label677" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fortilink-split-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fortilink-stacking</span> - Enable/disable FortiLink switch-stacking on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label678' href="javascript:ContentClick('label679', 'label678');" onmouseover="ContentPreview('label679');" onmouseout="ContentUnpreview('label679');" title="click to collapse or expand..."> more... </a>
 <div id="label679" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fortilink-stacking</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">forward-domain</span> - Transparent mode forward domain. <span class="li-normal">type: int</span>  <a id='label680' href="javascript:ContentClick('label681', 'label680');" onmouseover="ContentPreview('label681');" onmouseout="ContentUnpreview('label681');" title="click to collapse or expand..."> more... </a>
 <div id="label681" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>forward-domain</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">forward-error-correction</span> - Enable/disable forward error correction (FEC Clause 91). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, rs-fec, base-r-fec, fec-cl91, fec-cl74, rs-544, none, cl91-rs-fec, cl74-fc-fec]</span>  <a id='label682' href="javascript:ContentClick('label683', 'label682');" onmouseover="ContentPreview('label683');" onmouseout="ContentUnpreview('label683');" title="click to collapse or expand..."> more... </a>
 <div id="label683" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>forward-error-correction</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fp-anomaly</span> - Fp-Anomaly. <span class="li-normal">type: array</span> <span class="li-normal">choices: [drop_tcp_fin_noack, pass_winnuke, pass_tcpland, pass_udpland, pass_icmpland, pass_ipland, pass_iprr, pass_ipssrr, pass_iplsrr, pass_ipstream, pass_ipsecurity, pass_iptimestamp, pass_ipunknown_option, pass_ipunknown_prot, pass_icmp_frag, pass_tcp_no_flag, pass_tcp_fin_noack, drop_winnuke, drop_tcpland, drop_udpland, drop_icmpland, drop_ipland, drop_iprr, drop_ipssrr, drop_iplsrr, drop_ipstream, drop_ipsecurity, drop_iptimestamp, drop_ipunknown_option, drop_ipunknown_prot, drop_icmp_frag, drop_tcp_no_flag]</span>  <a id='label684' href="javascript:ContentClick('label685', 'label684');" onmouseover="ContentPreview('label685');" onmouseout="ContentUnpreview('label685');" title="click to collapse or expand..."> more... </a>
 <div id="label685" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fp-anomaly</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fp-disable</span> - Fp-Disable. <span class="li-normal">type: array</span> <span class="li-normal">choices: [all, ipsec, none]</span>  <a id='label686' href="javascript:ContentClick('label687', 'label686');" onmouseover="ContentPreview('label687');" onmouseout="ContentUnpreview('label687');" title="click to collapse or expand..."> more... </a>
 <div id="label687" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>fp-disable</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">gateway-address</span> - Gateway address <span class="li-normal">type: str</span>  <a id='label688' href="javascript:ContentClick('label689', 'label688');" onmouseover="ContentPreview('label689');" onmouseout="ContentUnpreview('label689');" title="click to collapse or expand..."> more... </a>
 <div id="label689" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>gateway-address</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">gi-gk</span> - Enable/disable Gi Gatekeeper. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label690' href="javascript:ContentClick('label691', 'label690');" onmouseover="ContentPreview('label691');" onmouseout="ContentUnpreview('label691');" title="click to collapse or expand..."> more... </a>
 <div id="label691" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>gi-gk</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">gwaddr</span> - Gateway address <span class="li-normal">type: str</span>  <a id='label692' href="javascript:ContentClick('label693', 'label692');" onmouseover="ContentPreview('label693');" onmouseout="ContentUnpreview('label693');" title="click to collapse or expand..."> more... </a>
 <div id="label693" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>gwaddr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">gwdetect</span> - Enable/disable detect gateway alive for first. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label694' href="javascript:ContentClick('label695', 'label694');" onmouseover="ContentPreview('label695');" onmouseout="ContentUnpreview('label695');" title="click to collapse or expand..."> more... </a>
 <div id="label695" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>gwdetect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ha-priority</span> - HA election priority for the PING server. <span class="li-normal">type: int</span>  <a id='label696' href="javascript:ContentClick('label697', 'label696');" onmouseover="ContentPreview('label697');" onmouseout="ContentUnpreview('label697');" title="click to collapse or expand..."> more... </a>
 <div id="label697" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ha-priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">icmp-accept-redirect</span> - Enable/disable ICMP accept redirect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label698' href="javascript:ContentClick('label699', 'label698');" onmouseover="ContentPreview('label699');" onmouseout="ContentUnpreview('label699');" title="click to collapse or expand..."> more... </a>
 <div id="label699" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>icmp-accept-redirect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">icmp-redirect</span> - Icmp-Redirect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label700' href="javascript:ContentClick('label701', 'label700');" onmouseover="ContentPreview('label701');" onmouseout="ContentUnpreview('label701');" title="click to collapse or expand..."> more... </a>
 <div id="label701" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>icmp-redirect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">icmp-send-redirect</span> - Enable/disable sending of ICMP redirects. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label702' href="javascript:ContentClick('label703', 'label702');" onmouseover="ContentPreview('label703');" onmouseout="ContentUnpreview('label703');" title="click to collapse or expand..."> more... </a>
 <div id="label703" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>icmp-send-redirect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ident-accept</span> - Enable/disable authentication for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label704' href="javascript:ContentClick('label705', 'label704');" onmouseover="ContentPreview('label705');" onmouseout="ContentUnpreview('label705');" title="click to collapse or expand..."> more... </a>
 <div id="label705" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ident-accept</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">idle-timeout</span> - PPPoE auto disconnect after idle timeout seconds, 0 means no timeout. <span class="li-normal">type: int</span>  <a id='label706' href="javascript:ContentClick('label707', 'label706');" onmouseover="ContentPreview('label707');" onmouseout="ContentUnpreview('label707');" title="click to collapse or expand..."> more... </a>
 <div id="label707" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>idle-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">if-mdix</span> - If-Mdix. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, normal, crossover]</span>  <a id='label708' href="javascript:ContentClick('label709', 'label708');" onmouseover="ContentPreview('label709');" onmouseout="ContentUnpreview('label709');" title="click to collapse or expand..."> more... </a>
 <div id="label709" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>if-mdix</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">if-media</span> - If-Media. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, copper, fiber]</span>  <a id='label710' href="javascript:ContentClick('label711', 'label710');" onmouseover="ContentPreview('label711');" onmouseout="ContentUnpreview('label711');" title="click to collapse or expand..."> more... </a>
 <div id="label711" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>if-media</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">in-force-vlan-cos</span> - In-Force-Vlan-Cos. <span class="li-normal">type: int</span>  <a id='label712' href="javascript:ContentClick('label713', 'label712');" onmouseover="ContentPreview('label713');" onmouseout="ContentUnpreview('label713');" title="click to collapse or expand..."> more... </a>
 <div id="label713" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>in-force-vlan-cos</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">inbandwidth</span> - Bandwidth limit for incoming traffic (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span>  <a id='label714' href="javascript:ContentClick('label715', 'label714');" onmouseover="ContentPreview('label715');" onmouseout="ContentUnpreview('label715');" title="click to collapse or expand..."> more... </a>
 <div id="label715" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>inbandwidth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ingress-cos</span> - Override incoming CoS in user VLAN tag on VLAN interface or assign a priority VLAN tag on physical interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, cos0, cos1, cos2, cos3, cos4, cos5, cos6, cos7]</span>  <a id='label716' href="javascript:ContentClick('label717', 'label716');" onmouseover="ContentPreview('label717');" onmouseout="ContentUnpreview('label717');" title="click to collapse or expand..."> more... </a>
 <div id="label717" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ingress-cos</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ingress-shaping-profile</span> - Incoming traffic shaping profile. <span class="li-normal">type: str</span>  <a id='label718' href="javascript:ContentClick('label719', 'label718');" onmouseover="ContentPreview('label719');" onmouseout="ContentUnpreview('label719');" title="click to collapse or expand..."> more... </a>
 <div id="label719" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ingress-shaping-profile</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span>  <a id='label720' href="javascript:ContentClick('label721', 'label720');" onmouseover="ContentPreview('label721');" onmouseout="ContentUnpreview('label721');" title="click to collapse or expand..."> more... </a>
 <div id="label721" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ingress-spillover-threshold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">internal</span> - Implicitly created. <span class="li-normal">type: int</span>  <a id='label722' href="javascript:ContentClick('label723', 'label722');" onmouseover="ContentPreview('label723');" onmouseout="ContentUnpreview('label723');" title="click to collapse or expand..."> more... </a>
 <div id="label723" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>internal</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip</span> - Interface IPv4 address and subnet mask, syntax: X. <span class="li-normal">type: str</span>  <a id='label724' href="javascript:ContentClick('label725', 'label724');" onmouseover="ContentPreview('label725');" onmouseout="ContentUnpreview('label725');" title="click to collapse or expand..."> more... </a>
 <div id="label725" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip-managed-by-fortiipam</span> - Enable/disable automatic IP address assignment of this interface by FortiIPAM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label726' href="javascript:ContentClick('label727', 'label726');" onmouseover="ContentPreview('label727');" onmouseout="ContentUnpreview('label727');" title="click to collapse or expand..."> more... </a>
 <div id="label727" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip-managed-by-fortiipam</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipmac</span> - Enable/disable IP/MAC binding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label728' href="javascript:ContentClick('label729', 'label728');" onmouseover="ContentPreview('label729');" onmouseout="ContentUnpreview('label729');" title="click to collapse or expand..."> more... </a>
 <div id="label729" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipmac</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ips-sniffer-mode</span> - Enable/disable the use of this interface as a one-armed sniffer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label730' href="javascript:ContentClick('label731', 'label730');" onmouseover="ContentPreview('label731');" onmouseout="ContentUnpreview('label731');" title="click to collapse or expand..."> more... </a>
 <div id="label731" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ips-sniffer-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipunnumbered</span> - Unnumbered IP used for PPPoE interfaces for which no unique local address is provided. <span class="li-normal">type: str</span>  <a id='label732' href="javascript:ContentClick('label733', 'label732');" onmouseover="ContentPreview('label733');" onmouseout="ContentUnpreview('label733');" title="click to collapse or expand..."> more... </a>
 <div id="label733" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipunnumbered</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv6</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">autoconf</span> - Enable/disable address auto config. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label734' href="javascript:ContentClick('label735', 'label734');" onmouseover="ContentPreview('label735');" onmouseout="ContentUnpreview('label735');" title="click to collapse or expand..."> more... </a>
 <div id="label735" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>autoconf</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-client-options</span> - Dhcp6-Client-Options. <span class="li-normal">type: array</span> <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span>  <a id='label736' href="javascript:ContentClick('label737', 'label736');" onmouseover="ContentPreview('label737');" onmouseout="ContentUnpreview('label737');" title="click to collapse or expand..."> more... </a>
 <div id="label737" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-client-options</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-information-request</span> - Enable/disable DHCPv6 information request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label738' href="javascript:ContentClick('label739', 'label738');" onmouseover="ContentPreview('label739');" onmouseout="ContentUnpreview('label739');" title="click to collapse or expand..."> more... </a>
 <div id="label739" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-information-request</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-delegation</span> - Enable/disable DHCPv6 prefix delegation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label740' href="javascript:ContentClick('label741', 'label740');" onmouseover="ContentPreview('label741');" onmouseout="ContentUnpreview('label741');" title="click to collapse or expand..."> more... </a>
 <div id="label741" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-delegation</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-hint</span> - DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server. <span class="li-normal">type: str</span>  <a id='label742' href="javascript:ContentClick('label743', 'label742');" onmouseover="ContentPreview('label743');" onmouseout="ContentUnpreview('label743');" title="click to collapse or expand..."> more... </a>
 <div id="label743" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-hint</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-hint-plt</span> - DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time. <span class="li-normal">type: int</span>  <a id='label744' href="javascript:ContentClick('label745', 'label744');" onmouseover="ContentPreview('label745');" onmouseout="ContentUnpreview('label745');" title="click to collapse or expand..."> more... </a>
 <div id="label745" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-hint-plt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-prefix-hint-vlt</span> - DHCPv6 prefix hint valid life time (sec). <span class="li-normal">type: int</span>  <a id='label746' href="javascript:ContentClick('label747', 'label746');" onmouseover="ContentPreview('label747');" onmouseout="ContentUnpreview('label747');" title="click to collapse or expand..."> more... </a>
 <div id="label747" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-prefix-hint-vlt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-relay-ip</span> - DHCPv6 relay IP address. <span class="li-normal">type: str</span>  <a id='label748' href="javascript:ContentClick('label749', 'label748');" onmouseover="ContentPreview('label749');" onmouseout="ContentUnpreview('label749');" title="click to collapse or expand..."> more... </a>
 <div id="label749" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-relay-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-relay-service</span> - Enable/disable DHCPv6 relay. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label750' href="javascript:ContentClick('label751', 'label750');" onmouseover="ContentPreview('label751');" onmouseout="ContentUnpreview('label751');" title="click to collapse or expand..."> more... </a>
 <div id="label751" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-relay-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp6-relay-type</span> - DHCPv6 relay type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span>  <a id='label752' href="javascript:ContentClick('label753', 'label752');" onmouseover="ContentPreview('label753');" onmouseout="ContentUnpreview('label753');" title="click to collapse or expand..."> more... </a>
 <div id="label753" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp6-relay-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">icmp6-send-redirect</span> - Enable/disable sending of ICMPv6 redirects. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label754' href="javascript:ContentClick('label755', 'label754');" onmouseover="ContentPreview('label755');" onmouseout="ContentUnpreview('label755');" title="click to collapse or expand..."> more... </a>
 <div id="label755" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>icmp6-send-redirect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface-identifier</span> - IPv6 interface identifier. <span class="li-normal">type: str</span>  <a id='label756' href="javascript:ContentClick('label757', 'label756');" onmouseover="ContentPreview('label757');" onmouseout="ContentUnpreview('label757');" title="click to collapse or expand..."> more... </a>
 <div id="label757" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>interface-identifier</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-address</span> - Primary IPv6 address prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx <span class="li-normal">type: str</span>  <a id='label758' href="javascript:ContentClick('label759', 'label758');" onmouseover="ContentPreview('label759');" onmouseout="ContentUnpreview('label759');" title="click to collapse or expand..."> more... </a>
 <div id="label759" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-address</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-allowaccess</span> - Allow management access to the interface. <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap, fabric]</span>  <a id='label760' href="javascript:ContentClick('label761', 'label760');" onmouseover="ContentPreview('label761');" onmouseout="ContentUnpreview('label761');" title="click to collapse or expand..."> more... </a>
 <div id="label761" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-allowaccess</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-default-life</span> - Default life (sec). <span class="li-normal">type: int</span>  <a id='label762' href="javascript:ContentClick('label763', 'label762');" onmouseover="ContentPreview('label763');" onmouseout="ContentUnpreview('label763');" title="click to collapse or expand..."> more... </a>
 <div id="label763" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-default-life</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-delegated-prefix-list</span> - Ip6-Delegated-Prefix-List. <span class="li-normal">type: array</span>
 <a id='label764' href="javascript:ContentClick('label765', 'label764');" onmouseover="ContentPreview('label765');" onmouseout="ContentUnpreview('label765');" title="click to collapse or expand..."> more... </a>
 <div id="label765" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-delegated-prefix-list</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - Enable/disable the autonomous flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label766' href="javascript:ContentClick('label767', 'label766');" onmouseover="ContentPreview('label767');" onmouseout="ContentUnpreview('label767');" title="click to collapse or expand..."> more... </a>
 <div id="label767" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>autonomous-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">onlink-flag</span> - Enable/disable the onlink flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label768' href="javascript:ContentClick('label769', 'label768');" onmouseover="ContentPreview('label769');" onmouseout="ContentUnpreview('label769');" title="click to collapse or expand..."> more... </a>
 <div id="label769" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>onlink-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">prefix-id</span> - Prefix ID. <span class="li-normal">type: int</span>  <a id='label770' href="javascript:ContentClick('label771', 'label770');" onmouseover="ContentPreview('label771');" onmouseout="ContentUnpreview('label771');" title="click to collapse or expand..."> more... </a>
 <div id="label771" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>prefix-id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> - Recursive DNS server option. <span class="li-normal">type: str</span> <a id='label772' href="javascript:ContentClick('label773', 'label772');" onmouseover="ContentPreview('label773');" onmouseout="ContentUnpreview('label773');" title="click to collapse or expand..."> more... </a>
 <div id="label773" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>rdnss</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rdnss-service</span> - Recursive DNS service option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [delegated, default, specify]</span>  <a id='label774' href="javascript:ContentClick('label775', 'label774');" onmouseover="ContentPreview('label775');" onmouseout="ContentUnpreview('label775');" title="click to collapse or expand..."> more... </a>
 <div id="label775" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>rdnss-service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">subnet</span> - Add subnet ID to routing prefix. <span class="li-normal">type: str</span>  <a id='label776' href="javascript:ContentClick('label777', 'label776');" onmouseover="ContentPreview('label777');" onmouseout="ContentUnpreview('label777');" title="click to collapse or expand..."> more... </a>
 <div id="label777" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>subnet</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">upstream-interface</span> - Name of the interface that provides delegated information. <span class="li-normal">type: str</span>  <a id='label778' href="javascript:ContentClick('label779', 'label778');" onmouseover="ContentPreview('label779');" onmouseout="ContentUnpreview('label779');" title="click to collapse or expand..."> more... </a>
 <div id="label779" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>upstream-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">delegated-prefix-iaid</span> - IAID of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>  <a id='label780' href="javascript:ContentClick('label781', 'label780');" onmouseover="ContentPreview('label781');" onmouseout="ContentUnpreview('label781');" title="click to collapse or expand..."> more... </a>
 <div id="label781" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>delegated-prefix-iaid</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ip6-dns-server-override</span> - Enable/disable using the DNS server acquired by DHCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label782' href="javascript:ContentClick('label783', 'label782');" onmouseover="ContentPreview('label783');" onmouseout="ContentUnpreview('label783');" title="click to collapse or expand..."> more... </a>
 <div id="label783" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-dns-server-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-extra-addr</span> - Ip6-Extra-Addr. <span class="li-normal">type: array</span>
 <a id='label784' href="javascript:ContentClick('label785', 'label784');" onmouseover="ContentPreview('label785');" onmouseout="ContentUnpreview('label785');" title="click to collapse or expand..."> more... </a>
 <div id="label785" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-extra-addr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">prefix</span> - IPv6 address prefix. <span class="li-normal">type: str</span>  <a id='label786' href="javascript:ContentClick('label787', 'label786');" onmouseover="ContentPreview('label787');" onmouseout="ContentUnpreview('label787');" title="click to collapse or expand..."> more... </a>
 <div id="label787" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>prefix</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ip6-hop-limit</span> - Hop limit (0 means unspecified). <span class="li-normal">type: int</span>  <a id='label788' href="javascript:ContentClick('label789', 'label788');" onmouseover="ContentPreview('label789');" onmouseout="ContentUnpreview('label789');" title="click to collapse or expand..."> more... </a>
 <div id="label789" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-hop-limit</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-link-mtu</span> - IPv6 link MTU. <span class="li-normal">type: int</span>  <a id='label790' href="javascript:ContentClick('label791', 'label790');" onmouseover="ContentPreview('label791');" onmouseout="ContentUnpreview('label791');" title="click to collapse or expand..."> more... </a>
 <div id="label791" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-link-mtu</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-manage-flag</span> - Enable/disable the managed flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label792' href="javascript:ContentClick('label793', 'label792');" onmouseover="ContentPreview('label793');" onmouseout="ContentUnpreview('label793');" title="click to collapse or expand..."> more... </a>
 <div id="label793" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-manage-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-max-interval</span> - IPv6 maximum interval (4 to 1800 sec). <span class="li-normal">type: int</span>  <a id='label794' href="javascript:ContentClick('label795', 'label794');" onmouseover="ContentPreview('label795');" onmouseout="ContentUnpreview('label795');" title="click to collapse or expand..."> more... </a>
 <div id="label795" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-max-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-min-interval</span> - IPv6 minimum interval (3 to 1350 sec). <span class="li-normal">type: int</span>  <a id='label796' href="javascript:ContentClick('label797', 'label796');" onmouseover="ContentPreview('label797');" onmouseout="ContentUnpreview('label797');" title="click to collapse or expand..."> more... </a>
 <div id="label797" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-min-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-mode</span> - Addressing mode (static, DHCP, delegated). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span>  <a id='label798' href="javascript:ContentClick('label799', 'label798');" onmouseover="ContentPreview('label799');" onmouseout="ContentUnpreview('label799');" title="click to collapse or expand..."> more... </a>
 <div id="label799" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-other-flag</span> - Enable/disable the other IPv6 flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label800' href="javascript:ContentClick('label801', 'label800');" onmouseover="ContentPreview('label801');" onmouseout="ContentUnpreview('label801');" title="click to collapse or expand..."> more... </a>
 <div id="label801" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-other-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-prefix-list</span> - Ip6-Prefix-List. <span class="li-normal">type: array</span>
 <a id='label802' href="javascript:ContentClick('label803', 'label802');" onmouseover="ContentPreview('label803');" onmouseout="ContentUnpreview('label803');" title="click to collapse or expand..."> more... </a>
 <div id="label803" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-prefix-list</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">autonomous-flag</span> - Enable/disable the autonomous flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label804' href="javascript:ContentClick('label805', 'label804');" onmouseover="ContentPreview('label805');" onmouseout="ContentUnpreview('label805');" title="click to collapse or expand..."> more... </a>
 <div id="label805" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>autonomous-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dnssl</span> - DNS search list option. <span class="li-normal">type: str</span> <a id='label806' href="javascript:ContentClick('label807', 'label806');" onmouseover="ContentPreview('label807');" onmouseout="ContentUnpreview('label807');" title="click to collapse or expand..."> more... </a>
 <div id="label807" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dnssl</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">onlink-flag</span> - Enable/disable the onlink flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label808' href="javascript:ContentClick('label809', 'label808');" onmouseover="ContentPreview('label809');" onmouseout="ContentUnpreview('label809');" title="click to collapse or expand..."> more... </a>
 <div id="label809" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>onlink-flag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">preferred-life-time</span> - Preferred life time (sec). <span class="li-normal">type: int</span>  <a id='label810' href="javascript:ContentClick('label811', 'label810');" onmouseover="ContentPreview('label811');" onmouseout="ContentUnpreview('label811');" title="click to collapse or expand..."> more... </a>
 <div id="label811" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>preferred-life-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">prefix</span> - IPv6 prefix. <span class="li-normal">type: str</span>  <a id='label812' href="javascript:ContentClick('label813', 'label812');" onmouseover="ContentPreview('label813');" onmouseout="ContentUnpreview('label813');" title="click to collapse or expand..."> more... </a>
 <div id="label813" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>prefix</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rdnss</span> - Recursive DNS server option. <span class="li-normal">type: str</span> <a id='label814' href="javascript:ContentClick('label815', 'label814');" onmouseover="ContentPreview('label815');" onmouseout="ContentUnpreview('label815');" title="click to collapse or expand..."> more... </a>
 <div id="label815" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>rdnss</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">valid-life-time</span> - Valid life time (sec). <span class="li-normal">type: int</span>  <a id='label816' href="javascript:ContentClick('label817', 'label816');" onmouseover="ContentPreview('label817');" onmouseout="ContentUnpreview('label817');" title="click to collapse or expand..."> more... </a>
 <div id="label817" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>valid-life-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">ip6-reachable-time</span> - IPv6 reachable time (milliseconds; 0 means unspecified). <span class="li-normal">type: int</span>  <a id='label818' href="javascript:ContentClick('label819', 'label818');" onmouseover="ContentPreview('label819');" onmouseout="ContentUnpreview('label819');" title="click to collapse or expand..."> more... </a>
 <div id="label819" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-reachable-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-retrans-time</span> - IPv6 retransmit time (milliseconds; 0 means unspecified). <span class="li-normal">type: int</span>  <a id='label820' href="javascript:ContentClick('label821', 'label820');" onmouseover="ContentPreview('label821');" onmouseout="ContentUnpreview('label821');" title="click to collapse or expand..."> more... </a>
 <div id="label821" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-retrans-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-send-adv</span> - Enable/disable sending advertisements about the interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label822' href="javascript:ContentClick('label823', 'label822');" onmouseover="ContentPreview('label823');" onmouseout="ContentUnpreview('label823');" title="click to collapse or expand..."> more... </a>
 <div id="label823" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-send-adv</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-subnet</span> - Subnet to routing prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx <span class="li-normal">type: str</span>  <a id='label824' href="javascript:ContentClick('label825', 'label824');" onmouseover="ContentPreview('label825');" onmouseout="ContentUnpreview('label825');" title="click to collapse or expand..."> more... </a>
 <div id="label825" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-subnet</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-upstream-interface</span> - Interface name providing delegated information. <span class="li-normal">type: str</span>  <a id='label826' href="javascript:ContentClick('label827', 'label826');" onmouseover="ContentPreview('label827');" onmouseout="ContentUnpreview('label827');" title="click to collapse or expand..."> more... </a>
 <div id="label827" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-upstream-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-cert</span> - Neighbor discovery certificate. <span class="li-normal">type: str</span>  <a id='label828' href="javascript:ContentClick('label829', 'label828');" onmouseover="ContentPreview('label829');" onmouseout="ContentUnpreview('label829');" title="click to collapse or expand..."> more... </a>
 <div id="label829" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-cert</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-cga-modifier</span> - Neighbor discovery CGA modifier. <span class="li-normal">type: str</span>  <a id='label830' href="javascript:ContentClick('label831', 'label830');" onmouseover="ContentPreview('label831');" onmouseout="ContentUnpreview('label831');" title="click to collapse or expand..."> more... </a>
 <div id="label831" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-cga-modifier</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-mode</span> - Neighbor discovery mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [basic, SEND-compatible]</span>  <a id='label832' href="javascript:ContentClick('label833', 'label832');" onmouseover="ContentPreview('label833');" onmouseout="ContentUnpreview('label833');" title="click to collapse or expand..."> more... </a>
 <div id="label833" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-security-level</span> - Neighbor discovery security level (0 - 7; 0 = least secure, default = 0). <span class="li-normal">type: int</span>  <a id='label834' href="javascript:ContentClick('label835', 'label834');" onmouseover="ContentPreview('label835');" onmouseout="ContentUnpreview('label835');" title="click to collapse or expand..."> more... </a>
 <div id="label835" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-security-level</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-timestamp-delta</span> - Neighbor discovery timestamp delta value (1 - 3600 sec; default = 300). <span class="li-normal">type: int</span>  <a id='label836' href="javascript:ContentClick('label837', 'label836');" onmouseover="ContentPreview('label837');" onmouseout="ContentUnpreview('label837');" title="click to collapse or expand..."> more... </a>
 <div id="label837" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-timestamp-delta</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nd-timestamp-fuzz</span> - Neighbor discovery timestamp fuzz factor (1 - 60 sec; default = 1). <span class="li-normal">type: int</span>  <a id='label838' href="javascript:ContentClick('label839', 'label838');" onmouseover="ContentPreview('label839');" onmouseout="ContentUnpreview('label839');" title="click to collapse or expand..."> more... </a>
 <div id="label839" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nd-timestamp-fuzz</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">unique-autoconf-addr</span> - Enable/disable unique auto config address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label840' href="javascript:ContentClick('label841', 'label840');" onmouseover="ContentPreview('label841');" onmouseout="ContentUnpreview('label841');" title="click to collapse or expand..."> more... </a>
 <div id="label841" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>unique-autoconf-addr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrip6_link_local</span> - Link-local IPv6 address of virtual router. <span class="li-normal">type: str</span>  <a id='label842' href="javascript:ContentClick('label843', 'label842');" onmouseover="ContentPreview('label843');" onmouseout="ContentUnpreview('label843');" title="click to collapse or expand..."> more... </a>
 <div id="label843" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrip6_link_local</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrrp-virtual-mac6</span> - Enable/disable virtual MAC for VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label844' href="javascript:ContentClick('label845', 'label844');" onmouseover="ContentPreview('label845');" onmouseout="ContentUnpreview('label845');" title="click to collapse or expand..."> more... </a>
 <div id="label845" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrrp-virtual-mac6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrrp6</span> - Vrrp6. <span class="li-normal">type: array</span>
 <a id='label846' href="javascript:ContentClick('label847', 'label846');" onmouseover="ContentPreview('label847');" onmouseout="ContentUnpreview('label847');" title="click to collapse or expand..."> more... </a>
 <div id="label847" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrrp6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - Enable/disable accept mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label848' href="javascript:ContentClick('label849', 'label848');" onmouseover="ContentPreview('label849');" onmouseout="ContentUnpreview('label849');" title="click to collapse or expand..."> more... </a>
 <div id="label849" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>accept-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">adv-interval</span> - Advertisement interval (1 - 255 seconds). <span class="li-normal">type: int</span>  <a id='label850' href="javascript:ContentClick('label851', 'label850');" onmouseover="ContentPreview('label851');" onmouseout="ContentUnpreview('label851');" title="click to collapse or expand..."> more... </a>
 <div id="label851" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>adv-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">preempt</span> - Enable/disable preempt mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label852' href="javascript:ContentClick('label853', 'label852');" onmouseover="ContentPreview('label853');" onmouseout="ContentUnpreview('label853');" title="click to collapse or expand..."> more... </a>
 <div id="label853" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>preempt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">priority</span> - Priority of the virtual router (1 - 255). <span class="li-normal">type: int</span>  <a id='label854' href="javascript:ContentClick('label855', 'label854');" onmouseover="ContentPreview('label855');" onmouseout="ContentUnpreview('label855');" title="click to collapse or expand..."> more... </a>
 <div id="label855" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">start-time</span> - Startup time (1 - 255 seconds). <span class="li-normal">type: int</span>  <a id='label856' href="javascript:ContentClick('label857', 'label856');" onmouseover="ContentPreview('label857');" onmouseout="ContentUnpreview('label857');" title="click to collapse or expand..."> more... </a>
 <div id="label857" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>start-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Enable/disable VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label858' href="javascript:ContentClick('label859', 'label858');" onmouseover="ContentPreview('label859');" onmouseout="ContentUnpreview('label859');" title="click to collapse or expand..."> more... </a>
 <div id="label859" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">vrdst6</span> - Monitor the route to this destination. <span class="li-normal">type: str</span>  <a id='label860' href="javascript:ContentClick('label861', 'label860');" onmouseover="ContentPreview('label861');" onmouseout="ContentUnpreview('label861');" title="click to collapse or expand..."> more... </a>
 <div id="label861" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrdst6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrgrp</span> - VRRP group ID (1 - 65535). <span class="li-normal">type: int</span>  <a id='label862' href="javascript:ContentClick('label863', 'label862');" onmouseover="ContentPreview('label863');" onmouseout="ContentUnpreview('label863');" title="click to collapse or expand..."> more... </a>
 <div id="label863" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrgrp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrid</span> - Virtual router identifier (1 - 255). <span class="li-normal">type: int</span>  <a id='label864' href="javascript:ContentClick('label865', 'label864');" onmouseover="ContentPreview('label865');" onmouseout="ContentUnpreview('label865');" title="click to collapse or expand..."> more... </a>
 <div id="label865" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrip6</span> - IPv6 address of the virtual router. <span class="li-normal">type: str</span>  <a id='label866' href="javascript:ContentClick('label867', 'label866');" onmouseover="ContentPreview('label867');" onmouseout="ContentUnpreview('label867');" title="click to collapse or expand..."> more... </a>
 <div id="label867" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrip6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">cli-conn6-status</span> - Cli-Conn6-Status. <span class="li-normal">type: int</span>  <a id='label868' href="javascript:ContentClick('label869', 'label868');" onmouseover="ContentPreview('label869');" onmouseout="ContentUnpreview('label869');" title="click to collapse or expand..."> more... </a>
 <div id="label869" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>cli-conn6-status</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-prefix-mode</span> - Assigning a prefix from DHCP or RA. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhcp6, ra]</span>  <a id='label870' href="javascript:ContentClick('label871', 'label870');" onmouseover="ContentPreview('label871');" onmouseout="ContentUnpreview('label871');" title="click to collapse or expand..."> more... </a>
 <div id="label871" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-prefix-mode</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ra-send-mtu</span> - Enable/disable sending link MTU in RA packet. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label872' href="javascript:ContentClick('label873', 'label872');" onmouseover="ContentPreview('label873');" onmouseout="ContentUnpreview('label873');" title="click to collapse or expand..."> more... </a>
 <div id="label873" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ra-send-mtu</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip6-delegated-prefix-iaid</span> - IAID of obtained delegated-prefix from the upstream interface. <span class="li-normal">type: int</span>  <a id='label874' href="javascript:ContentClick('label875', 'label874');" onmouseover="ContentPreview('label875');" onmouseout="ContentUnpreview('label875');" title="click to collapse or expand..."> more... </a>
 <div id="label875" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip6-delegated-prefix-iaid</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">l2forward</span> - Enable/disable l2 forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label876' href="javascript:ContentClick('label877', 'label876');" onmouseover="ContentPreview('label877');" onmouseout="ContentUnpreview('label877');" title="click to collapse or expand..."> more... </a>
 <div id="label877" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>l2forward</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">l2tp-client</span> - Enable/disable this interface as a Layer 2 Tunnelling Protocol (L2TP) client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label878' href="javascript:ContentClick('label879', 'label878');" onmouseover="ContentPreview('label879');" onmouseout="ContentUnpreview('label879');" title="click to collapse or expand..."> more... </a>
 <div id="label879" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>l2tp-client</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lacp-ha-slave</span> - LACP HA slave. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label880' href="javascript:ContentClick('label881', 'label880');" onmouseover="ContentPreview('label881');" onmouseout="ContentUnpreview('label881');" title="click to collapse or expand..."> more... </a>
 <div id="label881" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lacp-ha-slave</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lacp-mode</span> - LACP mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, passive, active]</span>  <a id='label882' href="javascript:ContentClick('label883', 'label882');" onmouseover="ContentPreview('label883');" onmouseout="ContentUnpreview('label883');" title="click to collapse or expand..."> more... </a>
 <div id="label883" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lacp-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lacp-speed</span> - How often the interface sends LACP messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slow, fast]</span>  <a id='label884' href="javascript:ContentClick('label885', 'label884');" onmouseover="ContentPreview('label885');" onmouseout="ContentUnpreview('label885');" title="click to collapse or expand..."> more... </a>
 <div id="label885" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lacp-speed</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lcp-echo-interval</span> - Time in seconds between PPPoE Link Control Protocol (LCP) echo requests. <span class="li-normal">type: int</span>  <a id='label886' href="javascript:ContentClick('label887', 'label886');" onmouseover="ContentPreview('label887');" onmouseout="ContentUnpreview('label887');" title="click to collapse or expand..."> more... </a>
 <div id="label887" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lcp-echo-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lcp-max-echo-fails</span> - Maximum missed LCP echo messages before disconnect. <span class="li-normal">type: int</span>  <a id='label888' href="javascript:ContentClick('label889', 'label888');" onmouseover="ContentPreview('label889');" onmouseout="ContentUnpreview('label889');" title="click to collapse or expand..."> more... </a>
 <div id="label889" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lcp-max-echo-fails</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">link-up-delay</span> - Number of milliseconds to wait before considering a link is up. <span class="li-normal">type: int</span>  <a id='label890' href="javascript:ContentClick('label891', 'label890');" onmouseover="ContentPreview('label891');" onmouseout="ContentUnpreview('label891');" title="click to collapse or expand..."> more... </a>
 <div id="label891" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>link-up-delay</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">listen-forticlient-connection</span> - Listen-Forticlient-Connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label892' href="javascript:ContentClick('label893', 'label892');" onmouseover="ContentPreview('label893');" onmouseout="ContentUnpreview('label893');" title="click to collapse or expand..."> more... </a>
 <div id="label893" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>listen-forticlient-connection</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lldp-network-policy</span> - LLDP-MED network policy profile. <span class="li-normal">type: str</span>  <a id='label894' href="javascript:ContentClick('label895', 'label894');" onmouseover="ContentPreview('label895');" onmouseout="ContentUnpreview('label895');" title="click to collapse or expand..."> more... </a>
 <div id="label895" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lldp-network-policy</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lldp-reception</span> - Enable/disable Link Layer Discovery Protocol (LLDP) reception. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vdom]</span>  <a id='label896' href="javascript:ContentClick('label897', 'label896');" onmouseover="ContentPreview('label897');" onmouseout="ContentUnpreview('label897');" title="click to collapse or expand..."> more... </a>
 <div id="label897" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lldp-reception</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lldp-transmission</span> - Enable/disable Link Layer Discovery Protocol (LLDP) transmission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable, vdom]</span>  <a id='label898' href="javascript:ContentClick('label899', 'label898');" onmouseover="ContentPreview('label899');" onmouseout="ContentUnpreview('label899');" title="click to collapse or expand..."> more... </a>
 <div id="label899" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lldp-transmission</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">log</span> - Log. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label900' href="javascript:ContentClick('label901', 'label900');" onmouseover="ContentPreview('label901');" onmouseout="ContentUnpreview('label901');" title="click to collapse or expand..."> more... </a>
 <div id="label901" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>log</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">macaddr</span> - Change the interfaces MAC address. <span class="li-normal">type: str</span>  <a id='label902' href="javascript:ContentClick('label903', 'label902');" onmouseover="ContentPreview('label903');" onmouseout="ContentUnpreview('label903');" title="click to collapse or expand..."> more... </a>
 <div id="label903" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>macaddr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">managed-subnetwork-size</span> - Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate units DHCP server settings. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 32, 64, 128]</span>  <a id='label904' href="javascript:ContentClick('label905', 'label904');" onmouseover="ContentPreview('label905');" onmouseout="ContentUnpreview('label905');" title="click to collapse or expand..."> more... </a>
 <div id="label905" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>managed-subnetwork-size</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">management-ip</span> - High Availability in-band management IP address of this interface. <span class="li-normal">type: str</span>  <a id='label906' href="javascript:ContentClick('label907', 'label906');" onmouseover="ContentPreview('label907');" onmouseout="ContentUnpreview('label907');" title="click to collapse or expand..."> more... </a>
 <div id="label907" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>management-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">max-egress-burst-rate</span> - Max-Egress-Burst-Rate. <span class="li-normal">type: int</span>  <a id='label908' href="javascript:ContentClick('label909', 'label908');" onmouseover="ContentPreview('label909');" onmouseout="ContentUnpreview('label909');" title="click to collapse or expand..."> more... </a>
 <div id="label909" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>max-egress-burst-rate</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">max-egress-rate</span> - Max-Egress-Rate. <span class="li-normal">type: int</span>  <a id='label910' href="javascript:ContentClick('label911', 'label910');" onmouseover="ContentPreview('label911');" onmouseout="ContentUnpreview('label911');" title="click to collapse or expand..."> more... </a>
 <div id="label911" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>max-egress-rate</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">measured-downstream-bandwidth</span> - Measured downstream bandwidth (kbps). <span class="li-normal">type: int</span>  <a id='label912' href="javascript:ContentClick('label913', 'label912');" onmouseover="ContentPreview('label913');" onmouseout="ContentUnpreview('label913');" title="click to collapse or expand..."> more... </a>
 <div id="label913" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>measured-downstream-bandwidth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">measured-upstream-bandwidth</span> - Measured upstream bandwidth (kbps). <span class="li-normal">type: int</span>  <a id='label914' href="javascript:ContentClick('label915', 'label914');" onmouseover="ContentPreview('label915');" onmouseout="ContentUnpreview('label915');" title="click to collapse or expand..."> more... </a>
 <div id="label915" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>measured-upstream-bandwidth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mediatype</span> - Select SFP media interface type <span class="li-normal">type: str</span>  <span class="li-normal">choices: [serdes-sfp, sgmii-sfp, cfp2-sr10, cfp2-lr4, serdes-copper-sfp, sr, cr, lr, qsfp28-sr4, qsfp28-lr4, qsfp28-cr4, sr4, cr4, lr4, none, gmii, sgmii]</span>  <a id='label916' href="javascript:ContentClick('label917', 'label916');" onmouseover="ContentPreview('label917');" onmouseout="ContentUnpreview('label917');" title="click to collapse or expand..."> more... </a>
 <div id="label917" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mediatype</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">member</span> - Physical interfaces that belong to the aggregate or redundant interface. <span class="li-normal">type: str</span>  <a id='label918' href="javascript:ContentClick('label919', 'label918');" onmouseover="ContentPreview('label919');" onmouseout="ContentUnpreview('label919');" title="click to collapse or expand..."> more... </a>
 <div id="label919" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>member</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">min-links</span> - Minimum number of aggregated ports that must be up. <span class="li-normal">type: int</span>  <a id='label920' href="javascript:ContentClick('label921', 'label920');" onmouseover="ContentPreview('label921');" onmouseout="ContentUnpreview('label921');" title="click to collapse or expand..."> more... </a>
 <div id="label921" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>min-links</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">min-links-down</span> - Action to take when less than the configured minimum number of links are active. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [operational, administrative]</span>  <a id='label922' href="javascript:ContentClick('label923', 'label922');" onmouseover="ContentPreview('label923');" onmouseout="ContentUnpreview('label923');" title="click to collapse or expand..."> more... </a>
 <div id="label923" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>min-links-down</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mode</span> - Addressing mode (static, DHCP, PPPoE). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, pppoa, ipoa, eoa]</span>  <a id='label924' href="javascript:ContentClick('label925', 'label924');" onmouseover="ContentPreview('label925');" onmouseout="ContentUnpreview('label925');" title="click to collapse or expand..."> more... </a>
 <div id="label925" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">monitor-bandwidth</span> - Enable monitoring bandwidth on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label926' href="javascript:ContentClick('label927', 'label926');" onmouseover="ContentPreview('label927');" onmouseout="ContentUnpreview('label927');" title="click to collapse or expand..."> more... </a>
 <div id="label927" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>monitor-bandwidth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mtu</span> - MTU value for this interface. <span class="li-normal">type: int</span>  <a id='label928' href="javascript:ContentClick('label929', 'label928');" onmouseover="ContentPreview('label929');" onmouseout="ContentUnpreview('label929');" title="click to collapse or expand..."> more... </a>
 <div id="label929" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mtu</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mtu-override</span> - Enable to set a custom MTU for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label930' href="javascript:ContentClick('label931', 'label930');" onmouseover="ContentPreview('label931');" onmouseout="ContentUnpreview('label931');" title="click to collapse or expand..."> more... </a>
 <div id="label931" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mtu-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mux-type</span> - Multiplexer type <span class="li-normal">type: str</span>  <span class="li-normal">choices: [llc-encaps, vc-encaps]</span>  <a id='label932' href="javascript:ContentClick('label933', 'label932');" onmouseover="ContentPreview('label933');" onmouseout="ContentUnpreview('label933');" title="click to collapse or expand..."> more... </a>
 <div id="label933" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>mux-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span>  <a id='label934' href="javascript:ContentClick('label935', 'label934');" onmouseover="ContentPreview('label935');" onmouseout="ContentUnpreview('label935');" title="click to collapse or expand..."> more... </a>
 <div id="label935" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>name</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ndiscforward</span> - Enable/disable NDISC forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label936' href="javascript:ContentClick('label937', 'label936');" onmouseover="ContentPreview('label937');" onmouseout="ContentUnpreview('label937');" title="click to collapse or expand..."> more... </a>
 <div id="label937" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ndiscforward</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">netbios-forward</span> - Enable/disable NETBIOS forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label938' href="javascript:ContentClick('label939', 'label938');" onmouseover="ContentPreview('label939');" onmouseout="ContentUnpreview('label939');" title="click to collapse or expand..."> more... </a>
 <div id="label939" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>netbios-forward</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">netflow-sampler</span> - Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tx, rx, both]</span>  <a id='label940' href="javascript:ContentClick('label941', 'label940');" onmouseover="ContentPreview('label941');" onmouseout="ContentUnpreview('label941');" title="click to collapse or expand..."> more... </a>
 <div id="label941" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>netflow-sampler</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">np-qos-profile</span> - Np-Qos-Profile. <span class="li-normal">type: int</span>  <a id='label942' href="javascript:ContentClick('label943', 'label942');" onmouseover="ContentPreview('label943');" onmouseout="ContentUnpreview('label943');" title="click to collapse or expand..."> more... </a>
 <div id="label943" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>np-qos-profile</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">npu-fastpath</span> - Npu-Fastpath. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label944' href="javascript:ContentClick('label945', 'label944');" onmouseover="ContentPreview('label945');" onmouseout="ContentUnpreview('label945');" title="click to collapse or expand..."> more... </a>
 <div id="label945" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>npu-fastpath</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">nst</span> - Nst. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label946' href="javascript:ContentClick('label947', 'label946');" onmouseover="ContentPreview('label947');" onmouseout="ContentUnpreview('label947');" title="click to collapse or expand..."> more... </a>
 <div id="label947" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>nst</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">out-force-vlan-cos</span> - Out-Force-Vlan-Cos. <span class="li-normal">type: int</span>  <a id='label948' href="javascript:ContentClick('label949', 'label948');" onmouseover="ContentPreview('label949');" onmouseout="ContentUnpreview('label949');" title="click to collapse or expand..."> more... </a>
 <div id="label949" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>out-force-vlan-cos</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">outbandwidth</span> - Bandwidth limit for outgoing traffic (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span>  <a id='label950' href="javascript:ContentClick('label951', 'label950');" onmouseover="ContentPreview('label951');" onmouseout="ContentUnpreview('label951');" title="click to collapse or expand..."> more... </a>
 <div id="label951" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>outbandwidth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">padt-retry-timeout</span> - PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time. <span class="li-normal">type: int</span>  <a id='label952' href="javascript:ContentClick('label953', 'label952');" onmouseover="ContentPreview('label953');" onmouseout="ContentUnpreview('label953');" title="click to collapse or expand..."> more... </a>
 <div id="label953" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>padt-retry-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">password</span> - PPPoE accounts password. <span class="li-normal">type: str</span> <a id='label954' href="javascript:ContentClick('label955', 'label954');" onmouseover="ContentPreview('label955');" onmouseout="ContentUnpreview('label955');" title="click to collapse or expand..."> more... </a>
 <div id="label955" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>password</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">peer-interface</span> - Peer-Interface. <span class="li-normal">type: str</span>  <a id='label956' href="javascript:ContentClick('label957', 'label956');" onmouseover="ContentPreview('label957');" onmouseout="ContentUnpreview('label957');" title="click to collapse or expand..."> more... </a>
 <div id="label957" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>peer-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">phy-mode</span> - DSL physical mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, adsl, vdsl, adsl-auto, vdsl2, adsl2+, adsl2, g.dmt, t1.413, g.lite]</span>  <a id='label958' href="javascript:ContentClick('label959', 'label958');" onmouseover="ContentPreview('label959');" onmouseout="ContentUnpreview('label959');" title="click to collapse or expand..."> more... </a>
 <div id="label959" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>phy-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ping-serv-status</span> - Ping-Serv-Status. <span class="li-normal">type: int</span>  <a id='label960' href="javascript:ContentClick('label961', 'label960');" onmouseover="ContentPreview('label961');" onmouseout="ContentUnpreview('label961');" title="click to collapse or expand..."> more... </a>
 <div id="label961" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ping-serv-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe</span> - Enable/disable PoE status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label962' href="javascript:ContentClick('label963', 'label962');" onmouseover="ContentPreview('label963');" onmouseout="ContentUnpreview('label963');" title="click to collapse or expand..."> more... </a>
 <div id="label963" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>poe</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">polling-interval</span> - sFlow polling interval (1 - 255 sec). <span class="li-normal">type: int</span>  <a id='label964' href="javascript:ContentClick('label965', 'label964');" onmouseover="ContentPreview('label965');" onmouseout="ContentUnpreview('label965');" title="click to collapse or expand..."> more... </a>
 <div id="label965" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>polling-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pppoe-unnumbered-negotiate</span> - Enable/disable PPPoE unnumbered negotiation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label966' href="javascript:ContentClick('label967', 'label966');" onmouseover="ContentPreview('label967');" onmouseout="ContentUnpreview('label967');" title="click to collapse or expand..."> more... </a>
 <div id="label967" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pppoe-unnumbered-negotiate</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pptp-auth-type</span> - PPTP authentication type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, pap, chap, mschapv1, mschapv2]</span>  <a id='label968' href="javascript:ContentClick('label969', 'label968');" onmouseover="ContentPreview('label969');" onmouseout="ContentUnpreview('label969');" title="click to collapse or expand..."> more... </a>
 <div id="label969" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pptp-auth-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pptp-client</span> - Enable/disable PPTP client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label970' href="javascript:ContentClick('label971', 'label970');" onmouseover="ContentPreview('label971');" onmouseout="ContentUnpreview('label971');" title="click to collapse or expand..."> more... </a>
 <div id="label971" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pptp-client</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pptp-password</span> - PPTP password. <span class="li-normal">type: str</span> <a id='label972' href="javascript:ContentClick('label973', 'label972');" onmouseover="ContentPreview('label973');" onmouseout="ContentUnpreview('label973');" title="click to collapse or expand..."> more... </a>
 <div id="label973" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pptp-password</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pptp-server-ip</span> - PPTP server IP address. <span class="li-normal">type: str</span>  <a id='label974' href="javascript:ContentClick('label975', 'label974');" onmouseover="ContentPreview('label975');" onmouseout="ContentUnpreview('label975');" title="click to collapse or expand..."> more... </a>
 <div id="label975" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pptp-server-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pptp-timeout</span> - Idle timer in minutes (0 for disabled). <span class="li-normal">type: int</span>  <a id='label976' href="javascript:ContentClick('label977', 'label976');" onmouseover="ContentPreview('label977');" onmouseout="ContentUnpreview('label977');" title="click to collapse or expand..."> more... </a>
 <div id="label977" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pptp-timeout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pptp-user</span> - PPTP user name. <span class="li-normal">type: str</span>  <a id='label978' href="javascript:ContentClick('label979', 'label978');" onmouseover="ContentPreview('label979');" onmouseout="ContentUnpreview('label979');" title="click to collapse or expand..."> more... </a>
 <div id="label979" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pptp-user</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">preserve-session-route</span> - Enable/disable preservation of session route when dirty. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label980' href="javascript:ContentClick('label981', 'label980');" onmouseover="ContentPreview('label981');" onmouseout="ContentUnpreview('label981');" title="click to collapse or expand..."> more... </a>
 <div id="label981" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>preserve-session-route</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">priority</span> - Priority of learned routes. <span class="li-normal">type: int</span>  <a id='label982' href="javascript:ContentClick('label983', 'label982');" onmouseover="ContentPreview('label983');" onmouseout="ContentUnpreview('label983');" title="click to collapse or expand..."> more... </a>
 <div id="label983" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">priority-override</span> - Enable/disable fail back to higher priority port once recovered. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label984' href="javascript:ContentClick('label985', 'label984');" onmouseover="ContentPreview('label985');" onmouseout="ContentUnpreview('label985');" title="click to collapse or expand..."> more... </a>
 <div id="label985" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>priority-override</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">proxy-captive-portal</span> - Enable/disable proxy captive portal on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label986' href="javascript:ContentClick('label987', 'label986');" onmouseover="ContentPreview('label987');" onmouseout="ContentUnpreview('label987');" title="click to collapse or expand..."> more... </a>
 <div id="label987" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>proxy-captive-portal</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">redundant-interface</span> - Redundant-Interface. <span class="li-normal">type: str</span>  <a id='label988' href="javascript:ContentClick('label989', 'label988');" onmouseover="ContentPreview('label989');" onmouseout="ContentUnpreview('label989');" title="click to collapse or expand..."> more... </a>
 <div id="label989" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>redundant-interface</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">remote-ip</span> - Remote IP address of tunnel. <span class="li-normal">type: str</span>  <a id='label990' href="javascript:ContentClick('label991', 'label990');" onmouseover="ContentPreview('label991');" onmouseout="ContentUnpreview('label991');" title="click to collapse or expand..."> more... </a>
 <div id="label991" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>remote-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">replacemsg-override-group</span> - Replacement message override group. <span class="li-normal">type: str</span>  <a id='label992' href="javascript:ContentClick('label993', 'label992');" onmouseover="ContentPreview('label993');" onmouseout="ContentUnpreview('label993');" title="click to collapse or expand..."> more... </a>
 <div id="label993" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>replacemsg-override-group</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">retransmission</span> - Enable/disable DSL retransmission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label994' href="javascript:ContentClick('label995', 'label994');" onmouseover="ContentPreview('label995');" onmouseout="ContentUnpreview('label995');" title="click to collapse or expand..."> more... </a>
 <div id="label995" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>retransmission</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ring-rx</span> - RX ring size. <span class="li-normal">type: int</span>  <a id='label996' href="javascript:ContentClick('label997', 'label996');" onmouseover="ContentPreview('label997');" onmouseout="ContentUnpreview('label997');" title="click to collapse or expand..."> more... </a>
 <div id="label997" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ring-rx</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ring-tx</span> - TX ring size. <span class="li-normal">type: int</span>  <a id='label998' href="javascript:ContentClick('label999', 'label998');" onmouseover="ContentPreview('label999');" onmouseout="ContentUnpreview('label999');" title="click to collapse or expand..."> more... </a>
 <div id="label999" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ring-tx</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">role</span> - Interface role. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [lan, wan, dmz, undefined]</span>  <a id='label1000' href="javascript:ContentClick('label1001', 'label1000');" onmouseover="ContentPreview('label1001');" onmouseout="ContentUnpreview('label1001');" title="click to collapse or expand..."> more... </a>
 <div id="label1001" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>role</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sample-direction</span> - Data that NetFlow collects (rx, tx, or both). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rx, tx, both]</span>  <a id='label1002' href="javascript:ContentClick('label1003', 'label1002');" onmouseover="ContentPreview('label1003');" onmouseout="ContentUnpreview('label1003');" title="click to collapse or expand..."> more... </a>
 <div id="label1003" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sample-direction</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sample-rate</span> - sFlow sample rate (10 - 99999). <span class="li-normal">type: int</span>  <a id='label1004' href="javascript:ContentClick('label1005', 'label1004');" onmouseover="ContentPreview('label1005');" onmouseout="ContentUnpreview('label1005');" title="click to collapse or expand..."> more... </a>
 <div id="label1005" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sample-rate</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">scan-botnet-connections</span> - Scan-Botnet-Connections. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span>  <a id='label1006' href="javascript:ContentClick('label1007', 'label1006');" onmouseover="ContentPreview('label1007');" onmouseout="ContentUnpreview('label1007');" title="click to collapse or expand..."> more... </a>
 <div id="label1007" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>scan-botnet-connections</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secondary-IP</span> - Enable/disable adding a secondary IP to this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1008' href="javascript:ContentClick('label1009', 'label1008');" onmouseover="ContentPreview('label1009');" onmouseout="ContentUnpreview('label1009');" title="click to collapse or expand..."> more... </a>
 <div id="label1009" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>secondary-IP</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">secondaryip</span> - Secondaryip. <span class="li-normal">type: array</span>
 <a id='label1010' href="javascript:ContentClick('label1011', 'label1010');" onmouseover="ContentPreview('label1011');" onmouseout="ContentUnpreview('label1011');" title="click to collapse or expand..."> more... </a>
 <div id="label1011" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>secondaryip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> - Management access settings for the secondary IP address. <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap, dnp, ftm, fabric, speed-test]</span>  <a id='label1012' href="javascript:ContentClick('label1013', 'label1012');" onmouseover="ContentPreview('label1013');" onmouseout="ContentUnpreview('label1013');" title="click to collapse or expand..."> more... </a>
 <div id="label1013" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>allowaccess</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">detectprotocol</span> - Protocols used to detect the server. <span class="li-normal">type: array</span> <span class="li-normal">choices: [ping, tcp-echo, udp-echo]</span>  <a id='label1014' href="javascript:ContentClick('label1015', 'label1014');" onmouseover="ContentPreview('label1015');" onmouseout="ContentUnpreview('label1015');" title="click to collapse or expand..."> more... </a>
 <div id="label1015" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>detectprotocol</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">detectserver</span> - Gateways ping server for this IP. <span class="li-normal">type: str</span>  <a id='label1016' href="javascript:ContentClick('label1017', 'label1016');" onmouseover="ContentPreview('label1017');" onmouseout="ContentUnpreview('label1017');" title="click to collapse or expand..."> more... </a>
 <div id="label1017" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>detectserver</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">gwdetect</span> - Enable/disable detect gateway alive for first. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1018' href="javascript:ContentClick('label1019', 'label1018');" onmouseover="ContentPreview('label1019');" onmouseout="ContentUnpreview('label1019');" title="click to collapse or expand..."> more... </a>
 <div id="label1019" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>gwdetect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ha-priority</span> - HA election priority for the PING server. <span class="li-normal">type: int</span>  <a id='label1020' href="javascript:ContentClick('label1021', 'label1020');" onmouseover="ContentPreview('label1021');" onmouseout="ContentUnpreview('label1021');" title="click to collapse or expand..."> more... </a>
 <div id="label1021" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ha-priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label1022' href="javascript:ContentClick('label1023', 'label1022');" onmouseover="ContentPreview('label1023');" onmouseout="ContentUnpreview('label1023');" title="click to collapse or expand..."> more... </a>
 <div id="label1023" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">ip</span> - Secondary IP address of the interface. <span class="li-normal">type: str</span>  <a id='label1024' href="javascript:ContentClick('label1025', 'label1024');" onmouseover="ContentPreview('label1025');" onmouseout="ContentUnpreview('label1025');" title="click to collapse or expand..."> more... </a>
 <div id="label1025" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ping-serv-status</span> - Ping-Serv-Status. <span class="li-normal">type: int</span>  <a id='label1026' href="javascript:ContentClick('label1027', 'label1026');" onmouseover="ContentPreview('label1027');" onmouseout="ContentUnpreview('label1027');" title="click to collapse or expand..."> more... </a>
 <div id="label1027" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ping-serv-status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">seq</span> - Seq. <span class="li-normal">type: int</span>  <a id='label1028' href="javascript:ContentClick('label1029', 'label1028');" onmouseover="ContentPreview('label1029');" onmouseout="ContentUnpreview('label1029');" title="click to collapse or expand..."> more... </a>
 <div id="label1029" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>seq</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">security-8021x-dynamic-vlan-id</span> - VLAN ID for virtual switch. <span class="li-normal">type: int</span>  <a id='label1030' href="javascript:ContentClick('label1031', 'label1030');" onmouseover="ContentPreview('label1031');" onmouseout="ContentUnpreview('label1031');" title="click to collapse or expand..."> more... </a>
 <div id="label1031" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-8021x-dynamic-vlan-id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-8021x-master</span> - 802. <span class="li-normal">type: str</span>  <a id='label1032' href="javascript:ContentClick('label1033', 'label1032');" onmouseover="ContentPreview('label1033');" onmouseout="ContentUnpreview('label1033');" title="click to collapse or expand..."> more... </a>
 <div id="label1033" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-8021x-master</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-8021x-mode</span> - 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, dynamic-vlan, fallback, slave]</span>  <a id='label1034' href="javascript:ContentClick('label1035', 'label1034');" onmouseover="ContentPreview('label1035');" onmouseout="ContentUnpreview('label1035');" title="click to collapse or expand..."> more... </a>
 <div id="label1035" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-8021x-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-exempt-list</span> - Name of security-exempt-list. <span class="li-normal">type: str</span>  <a id='label1036' href="javascript:ContentClick('label1037', 'label1036');" onmouseover="ContentPreview('label1037');" onmouseout="ContentUnpreview('label1037');" title="click to collapse or expand..."> more... </a>
 <div id="label1037" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-exempt-list</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-external-logout</span> - URL of external authentication logout server. <span class="li-normal">type: str</span>  <a id='label1038' href="javascript:ContentClick('label1039', 'label1038');" onmouseover="ContentPreview('label1039');" onmouseout="ContentUnpreview('label1039');" title="click to collapse or expand..."> more... </a>
 <div id="label1039" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-external-logout</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-external-web</span> - URL of external authentication web server. <span class="li-normal">type: str</span>  <a id='label1040' href="javascript:ContentClick('label1041', 'label1040');" onmouseover="ContentPreview('label1041');" onmouseout="ContentUnpreview('label1041');" title="click to collapse or expand..."> more... </a>
 <div id="label1041" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-external-web</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-groups</span> - User groups that can authenticate with the captive portal. <span class="li-normal">type: str</span>  <a id='label1042' href="javascript:ContentClick('label1043', 'label1042');" onmouseover="ContentPreview('label1043');" onmouseout="ContentUnpreview('label1043');" title="click to collapse or expand..."> more... </a>
 <div id="label1043" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-groups</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-mac-auth-bypass</span> - Enable/disable MAC authentication bypass. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, mac-auth-only]</span>  <a id='label1044' href="javascript:ContentClick('label1045', 'label1044');" onmouseover="ContentPreview('label1045');" onmouseout="ContentUnpreview('label1045');" title="click to collapse or expand..."> more... </a>
 <div id="label1045" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-mac-auth-bypass</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-mode</span> - Turn on captive portal authentication for this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, captive-portal, 802.1X]</span>  <a id='label1046' href="javascript:ContentClick('label1047', 'label1046');" onmouseover="ContentPreview('label1047');" onmouseout="ContentUnpreview('label1047');" title="click to collapse or expand..."> more... </a>
 <div id="label1047" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">security-redirect-url</span> - URL redirection after disclaimer/authentication. <span class="li-normal">type: str</span>  <a id='label1048' href="javascript:ContentClick('label1049', 'label1048');" onmouseover="ContentPreview('label1049');" onmouseout="ContentUnpreview('label1049');" title="click to collapse or expand..."> more... </a>
 <div id="label1049" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>security-redirect-url</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">service-name</span> - PPPoE service name. <span class="li-normal">type: str</span>  <a id='label1050' href="javascript:ContentClick('label1051', 'label1050');" onmouseover="ContentPreview('label1051');" onmouseout="ContentUnpreview('label1051');" title="click to collapse or expand..."> more... </a>
 <div id="label1051" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>service-name</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sflow-sampler</span> - Enable/disable sFlow on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1052' href="javascript:ContentClick('label1053', 'label1052');" onmouseover="ContentPreview('label1053');" onmouseout="ContentUnpreview('label1053');" title="click to collapse or expand..."> more... </a>
 <div id="label1053" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sflow-sampler</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">speed</span> - Interface speed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, 10full, 10half, 100full, 100half, 1000full, 1000half, 10000full, 1000auto, 10000auto, 40000full, 100Gfull, 25000full, 40000auto, 25000auto, 100Gauto, 400Gfull, 400Gauto]</span>  <a id='label1054' href="javascript:ContentClick('label1055', 'label1054');" onmouseover="ContentPreview('label1055');" onmouseout="ContentUnpreview('label1055');" title="click to collapse or expand..."> more... </a>
 <div id="label1055" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>speed</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">spillover-threshold</span> - Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited. <span class="li-normal">type: int</span>  <a id='label1056' href="javascript:ContentClick('label1057', 'label1056');" onmouseover="ContentPreview('label1057');" onmouseout="ContentUnpreview('label1057');" title="click to collapse or expand..."> more... </a>
 <div id="label1057" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>spillover-threshold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">src-check</span> - Enable/disable source IP check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1058' href="javascript:ContentClick('label1059', 'label1058');" onmouseover="ContentPreview('label1059');" onmouseout="ContentUnpreview('label1059');" title="click to collapse or expand..."> more... </a>
 <div id="label1059" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>src-check</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Bring the interface up or shut the interface down. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [down, up]</span>  <a id='label1060' href="javascript:ContentClick('label1061', 'label1060');" onmouseover="ContentPreview('label1061');" onmouseout="ContentUnpreview('label1061');" title="click to collapse or expand..."> more... </a>
 <div id="label1061" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">stp</span> - Enable/disable STP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1062' href="javascript:ContentClick('label1063', 'label1062');" onmouseover="ContentPreview('label1063');" onmouseout="ContentUnpreview('label1063');" title="click to collapse or expand..."> more... </a>
 <div id="label1063" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>stp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stp-ha-slave</span> - Control STP behaviour on HA slave. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, priority-adjust]</span>  <a id='label1064' href="javascript:ContentClick('label1065', 'label1064');" onmouseover="ContentPreview('label1065');" onmouseout="ContentUnpreview('label1065');" title="click to collapse or expand..."> more... </a>
 <div id="label1065" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>stp-ha-slave</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stpforward</span> - Enable/disable STP forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1066' href="javascript:ContentClick('label1067', 'label1066');" onmouseover="ContentPreview('label1067');" onmouseout="ContentUnpreview('label1067');" title="click to collapse or expand..."> more... </a>
 <div id="label1067" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>stpforward</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stpforward-mode</span> - Configure STP forwarding mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]</span>  <a id='label1068' href="javascript:ContentClick('label1069', 'label1068');" onmouseover="ContentPreview('label1069');" onmouseout="ContentUnpreview('label1069');" title="click to collapse or expand..."> more... </a>
 <div id="label1069" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>stpforward-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">strip-priority-vlan-tag</span> - Strip-Priority-Vlan-Tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1070' href="javascript:ContentClick('label1071', 'label1070');" onmouseover="ContentPreview('label1071');" onmouseout="ContentUnpreview('label1071');" title="click to collapse or expand..."> more... </a>
 <div id="label1071" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>strip-priority-vlan-tag</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">subst</span> - Enable to always send packets from this interface to a destination MAC address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1072' href="javascript:ContentClick('label1073', 'label1072');" onmouseover="ContentPreview('label1073');" onmouseout="ContentUnpreview('label1073');" title="click to collapse or expand..."> more... </a>
 <div id="label1073" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>subst</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">substitute-dst-mac</span> - Destination MAC address that all packets are sent to from this interface. <span class="li-normal">type: str</span>  <a id='label1074' href="javascript:ContentClick('label1075', 'label1074');" onmouseover="ContentPreview('label1075');" onmouseout="ContentUnpreview('label1075');" title="click to collapse or expand..."> more... </a>
 <div id="label1075" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>substitute-dst-mac</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">swc-first-create</span> - Initial create for switch-controller VLANs. <span class="li-normal">type: int</span>  <a id='label1076' href="javascript:ContentClick('label1077', 'label1076');" onmouseover="ContentPreview('label1077');" onmouseout="ContentUnpreview('label1077');" title="click to collapse or expand..."> more... </a>
 <div id="label1077" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>swc-first-create</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">swc-vlan</span> - Swc-Vlan. <span class="li-normal">type: int</span>  <a id='label1078' href="javascript:ContentClick('label1079', 'label1078');" onmouseover="ContentPreview('label1079');" onmouseout="ContentUnpreview('label1079');" title="click to collapse or expand..."> more... </a>
 <div id="label1079" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>swc-vlan</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch</span> - Switch. <span class="li-normal">type: str</span>  <a id='label1080' href="javascript:ContentClick('label1081', 'label1080');" onmouseover="ContentPreview('label1081');" onmouseout="ContentUnpreview('label1081');" title="click to collapse or expand..."> more... </a>
 <div id="label1081" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-access-vlan</span> - Block FortiSwitch port-to-port traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1082' href="javascript:ContentClick('label1083', 'label1082');" onmouseover="ContentPreview('label1083');" onmouseout="ContentUnpreview('label1083');" title="click to collapse or expand..."> more... </a>
 <div id="label1083" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-access-vlan</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-arp-inspection</span> - Enable/disable FortiSwitch ARP inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1084' href="javascript:ContentClick('label1085', 'label1084');" onmouseover="ContentPreview('label1085');" onmouseout="ContentUnpreview('label1085');" title="click to collapse or expand..."> more... </a>
 <div id="label1085" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-arp-inspection</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-auth</span> - Switch-Controller-Auth. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [radius, usergroup]</span>  <a id='label1086' href="javascript:ContentClick('label1087', 'label1086');" onmouseover="ContentPreview('label1087');" onmouseout="ContentUnpreview('label1087');" title="click to collapse or expand..."> more... </a>
 <div id="label1087" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-auth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-dhcp-snooping</span> - Switch controller DHCP snooping. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1088' href="javascript:ContentClick('label1089', 'label1088');" onmouseover="ContentPreview('label1089');" onmouseout="ContentUnpreview('label1089');" title="click to collapse or expand..."> more... </a>
 <div id="label1089" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-dhcp-snooping</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-dhcp-snooping-option82</span> - Switch controller DHCP snooping option82. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1090' href="javascript:ContentClick('label1091', 'label1090');" onmouseover="ContentPreview('label1091');" onmouseout="ContentUnpreview('label1091');" title="click to collapse or expand..."> more... </a>
 <div id="label1091" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-dhcp-snooping-option82</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-dhcp-snooping-verify-mac</span> - Switch controller DHCP snooping verify MAC. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1092' href="javascript:ContentClick('label1093', 'label1092');" onmouseover="ContentPreview('label1093');" onmouseout="ContentUnpreview('label1093');" title="click to collapse or expand..."> more... </a>
 <div id="label1093" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-dhcp-snooping-verify-mac</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-feature</span> - Interfaces purpose when assigning traffic (read only). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, default-vlan, quarantine, sniffer, voice, camera, rspan, video, nac, nac-segment]</span>  <a id='label1094' href="javascript:ContentClick('label1095', 'label1094');" onmouseover="ContentPreview('label1095');" onmouseout="ContentUnpreview('label1095');" title="click to collapse or expand..."> more... </a>
 <div id="label1095" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-feature</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-igmp-snooping</span> - Switch controller IGMP snooping. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1096' href="javascript:ContentClick('label1097', 'label1096');" onmouseover="ContentPreview('label1097');" onmouseout="ContentUnpreview('label1097');" title="click to collapse or expand..."> more... </a>
 <div id="label1097" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-igmp-snooping</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-igmp-snooping-fast-leave</span> - Switch controller IGMP snooping fast-leave. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1098' href="javascript:ContentClick('label1099', 'label1098');" onmouseover="ContentPreview('label1099');" onmouseout="ContentUnpreview('label1099');" title="click to collapse or expand..."> more... </a>
 <div id="label1099" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-igmp-snooping-fast-leave</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-igmp-snooping-proxy</span> - Switch controller IGMP snooping proxy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1100' href="javascript:ContentClick('label1101', 'label1100');" onmouseover="ContentPreview('label1101');" onmouseout="ContentUnpreview('label1101');" title="click to collapse or expand..."> more... </a>
 <div id="label1101" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-igmp-snooping-proxy</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-iot-scanning</span> - Enable/disable managed FortiSwitch IoT scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1102' href="javascript:ContentClick('label1103', 'label1102');" onmouseover="ContentPreview('label1103');" onmouseout="ContentUnpreview('label1103');" title="click to collapse or expand..."> more... </a>
 <div id="label1103" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-iot-scanning</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-learning-limit</span> - Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default). <span class="li-normal">type: int</span>  <a id='label1104' href="javascript:ContentClick('label1105', 'label1104');" onmouseover="ContentPreview('label1105');" onmouseout="ContentUnpreview('label1105');" title="click to collapse or expand..."> more... </a>
 <div id="label1105" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-learning-limit</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-mgmt-vlan</span> - VLAN to use for FortiLink management purposes. <span class="li-normal">type: int</span>  <a id='label1106' href="javascript:ContentClick('label1107', 'label1106');" onmouseover="ContentPreview('label1107');" onmouseout="ContentUnpreview('label1107');" title="click to collapse or expand..."> more... </a>
 <div id="label1107" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-mgmt-vlan</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-nac</span> - Integrated NAC settings for managed FortiSwitch. <span class="li-normal">type: str</span>  <a id='label1108' href="javascript:ContentClick('label1109', 'label1108');" onmouseover="ContentPreview('label1109');" onmouseout="ContentUnpreview('label1109');" title="click to collapse or expand..."> more... </a>
 <div id="label1109" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-nac</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-radius-server</span> - Switch-Controller-Radius-Server. <span class="li-normal">type: str</span>  <a id='label1110' href="javascript:ContentClick('label1111', 'label1110');" onmouseover="ContentPreview('label1111');" onmouseout="ContentUnpreview('label1111');" title="click to collapse or expand..."> more... </a>
 <div id="label1111" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-radius-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-rspan-mode</span> - Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1112' href="javascript:ContentClick('label1113', 'label1112');" onmouseover="ContentPreview('label1113');" onmouseout="ContentUnpreview('label1113');" title="click to collapse or expand..."> more... </a>
 <div id="label1113" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-rspan-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-source-ip</span> - Source IP address used in FortiLink over L3 connections. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [outbound, fixed]</span>  <a id='label1114' href="javascript:ContentClick('label1115', 'label1114');" onmouseover="ContentPreview('label1115');" onmouseout="ContentUnpreview('label1115');" title="click to collapse or expand..."> more... </a>
 <div id="label1115" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-source-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-traffic-policy</span> - Switch controller traffic policy for the VLAN. <span class="li-normal">type: str</span>  <a id='label1116' href="javascript:ContentClick('label1117', 'label1116');" onmouseover="ContentPreview('label1117');" onmouseout="ContentUnpreview('label1117');" title="click to collapse or expand..."> more... </a>
 <div id="label1117" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-traffic-policy</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tc-mode</span> - DSL transfer mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ptm, atm]</span>  <a id='label1118' href="javascript:ContentClick('label1119', 'label1118');" onmouseover="ContentPreview('label1119');" onmouseout="ContentUnpreview('label1119');" title="click to collapse or expand..."> more... </a>
 <div id="label1119" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tc-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tcp-mss</span> - TCP maximum segment size. <span class="li-normal">type: int</span>  <a id='label1120' href="javascript:ContentClick('label1121', 'label1120');" onmouseover="ContentPreview('label1121');" onmouseout="ContentUnpreview('label1121');" title="click to collapse or expand..."> more... </a>
 <div id="label1121" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tcp-mss</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trunk</span> - Enable/disable VLAN trunk. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1122' href="javascript:ContentClick('label1123', 'label1122');" onmouseover="ContentPreview('label1123');" onmouseout="ContentUnpreview('label1123');" title="click to collapse or expand..."> more... </a>
 <div id="label1123" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>trunk</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trust-ip-1</span> - Trusted host for dedicated management traffic (0. <span class="li-normal">type: str</span>  <a id='label1124' href="javascript:ContentClick('label1125', 'label1124');" onmouseover="ContentPreview('label1125');" onmouseout="ContentUnpreview('label1125');" title="click to collapse or expand..."> more... </a>
 <div id="label1125" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>trust-ip-1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trust-ip-2</span> - Trusted host for dedicated management traffic (0. <span class="li-normal">type: str</span>  <a id='label1126' href="javascript:ContentClick('label1127', 'label1126');" onmouseover="ContentPreview('label1127');" onmouseout="ContentUnpreview('label1127');" title="click to collapse or expand..."> more... </a>
 <div id="label1127" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>trust-ip-2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trust-ip-3</span> - Trusted host for dedicated management traffic (0. <span class="li-normal">type: str</span>  <a id='label1128' href="javascript:ContentClick('label1129', 'label1128');" onmouseover="ContentPreview('label1129');" onmouseout="ContentUnpreview('label1129');" title="click to collapse or expand..."> more... </a>
 <div id="label1129" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>trust-ip-3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trust-ip6-1</span> - Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). <span class="li-normal">type: str</span>  <a id='label1130' href="javascript:ContentClick('label1131', 'label1130');" onmouseover="ContentPreview('label1131');" onmouseout="ContentUnpreview('label1131');" title="click to collapse or expand..."> more... </a>
 <div id="label1131" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>trust-ip6-1</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trust-ip6-2</span> - Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). <span class="li-normal">type: str</span>  <a id='label1132' href="javascript:ContentClick('label1133', 'label1132');" onmouseover="ContentPreview('label1133');" onmouseout="ContentUnpreview('label1133');" title="click to collapse or expand..."> more... </a>
 <div id="label1133" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>trust-ip6-2</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trust-ip6-3</span> - Trusted IPv6 host for dedicated management traffic (::/0 for all hosts). <span class="li-normal">type: str</span>  <a id='label1134' href="javascript:ContentClick('label1135', 'label1134');" onmouseover="ContentPreview('label1135');" onmouseout="ContentUnpreview('label1135');" title="click to collapse or expand..."> more... </a>
 <div id="label1135" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>trust-ip6-3</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">type</span> - Interface type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [physical, vlan, aggregate, redundant, tunnel, wireless, vdom-link, loopback, switch, hard-switch, hdlc, vap-switch, wl-mesh, fortilink, switch-vlan, fctrl-trunk, tdm, fext-wan, vxlan, emac-vlan, geneve, ssl, lan-extension]</span>  <a id='label1136' href="javascript:ContentClick('label1137', 'label1136');" onmouseover="ContentPreview('label1137');" onmouseout="ContentUnpreview('label1137');" title="click to collapse or expand..."> more... </a>
 <div id="label1137" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">username</span> - Username of the PPPoE account, provided by your ISP. <span class="li-normal">type: str</span>  <a id='label1138' href="javascript:ContentClick('label1139', 'label1138');" onmouseover="ContentPreview('label1139');" onmouseout="ContentUnpreview('label1139');" title="click to collapse or expand..."> more... </a>
 <div id="label1139" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>username</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vci</span> - Virtual Channel ID <span class="li-normal">type: int</span>  <a id='label1140' href="javascript:ContentClick('label1141', 'label1140');" onmouseover="ContentPreview('label1141');" onmouseout="ContentUnpreview('label1141');" title="click to collapse or expand..."> more... </a>
 <div id="label1141" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vci</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vectoring</span> - Enable/disable DSL vectoring. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1142' href="javascript:ContentClick('label1143', 'label1142');" onmouseover="ContentPreview('label1143');" onmouseout="ContentUnpreview('label1143');" title="click to collapse or expand..."> more... </a>
 <div id="label1143" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vectoring</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vindex</span> - Vindex. <span class="li-normal">type: int</span>  <a id='label1144' href="javascript:ContentClick('label1145', 'label1144');" onmouseover="ContentPreview('label1145');" onmouseout="ContentUnpreview('label1145');" title="click to collapse or expand..."> more... </a>
 <div id="label1145" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vindex</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlan-protocol</span> - Ethernet protocol of VLAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [8021q, 8021ad]</span>  <a id='label1146' href="javascript:ContentClick('label1147', 'label1146');" onmouseover="ContentPreview('label1147');" onmouseout="ContentUnpreview('label1147');" title="click to collapse or expand..."> more... </a>
 <div id="label1147" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vlan-protocol</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlanforward</span> - Enable/disable traffic forwarding between VLANs on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1148' href="javascript:ContentClick('label1149', 'label1148');" onmouseover="ContentPreview('label1149');" onmouseout="ContentUnpreview('label1149');" title="click to collapse or expand..."> more... </a>
 <div id="label1149" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vlanforward</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlanid</span> - VLAN ID (1 - 4094). <span class="li-normal">type: int</span>  <a id='label1150' href="javascript:ContentClick('label1151', 'label1150');" onmouseover="ContentPreview('label1151');" onmouseout="ContentUnpreview('label1151');" title="click to collapse or expand..."> more... </a>
 <div id="label1151" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vlanid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vpi</span> - Virtual Path ID <span class="li-normal">type: int</span>  <a id='label1152' href="javascript:ContentClick('label1153', 'label1152');" onmouseover="ContentPreview('label1153');" onmouseout="ContentUnpreview('label1153');" title="click to collapse or expand..."> more... </a>
 <div id="label1153" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vpi</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrf</span> - Virtual Routing Forwarding ID. <span class="li-normal">type: int</span>  <a id='label1154' href="javascript:ContentClick('label1155', 'label1154');" onmouseover="ContentPreview('label1155');" onmouseout="ContentUnpreview('label1155');" title="click to collapse or expand..."> more... </a>
 <div id="label1155" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrf</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrrp</span> - Vrrp. <span class="li-normal">type: array</span>
 <a id='label1156' href="javascript:ContentClick('label1157', 'label1156');" onmouseover="ContentPreview('label1157');" onmouseout="ContentUnpreview('label1157');" title="click to collapse or expand..."> more... </a>
 <div id="label1157" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrrp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">accept-mode</span> - Enable/disable accept mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1158' href="javascript:ContentClick('label1159', 'label1158');" onmouseover="ContentPreview('label1159');" onmouseout="ContentUnpreview('label1159');" title="click to collapse or expand..."> more... </a>
 <div id="label1159" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>accept-mode</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">adv-interval</span> - Advertisement interval (1 - 255 seconds). <span class="li-normal">type: int</span>  <a id='label1160' href="javascript:ContentClick('label1161', 'label1160');" onmouseover="ContentPreview('label1161');" onmouseout="ContentUnpreview('label1161');" title="click to collapse or expand..."> more... </a>
 <div id="label1161" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>adv-interval</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ignore-default-route</span> - Enable/disable ignoring of default route when checking destination. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1162' href="javascript:ContentClick('label1163', 'label1162');" onmouseover="ContentPreview('label1163');" onmouseout="ContentUnpreview('label1163');" title="click to collapse or expand..."> more... </a>
 <div id="label1163" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ignore-default-route</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">preempt</span> - Enable/disable preempt mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1164' href="javascript:ContentClick('label1165', 'label1164');" onmouseover="ContentPreview('label1165');" onmouseout="ContentUnpreview('label1165');" title="click to collapse or expand..."> more... </a>
 <div id="label1165" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>preempt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">priority</span> - Priority of the virtual router (1 - 255). <span class="li-normal">type: int</span>  <a id='label1166' href="javascript:ContentClick('label1167', 'label1166');" onmouseover="ContentPreview('label1167');" onmouseout="ContentUnpreview('label1167');" title="click to collapse or expand..."> more... </a>
 <div id="label1167" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">start-time</span> - Startup time (1 - 255 seconds). <span class="li-normal">type: int</span>  <a id='label1168' href="javascript:ContentClick('label1169', 'label1168');" onmouseover="ContentPreview('label1169');" onmouseout="ContentUnpreview('label1169');" title="click to collapse or expand..."> more... </a>
 <div id="label1169" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>start-time</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Enable/disable this VRRP configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1170' href="javascript:ContentClick('label1171', 'label1170');" onmouseover="ContentPreview('label1171');" onmouseout="ContentUnpreview('label1171');" title="click to collapse or expand..."> more... </a>
 <div id="label1171" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <li><span class="li-head">version</span> - VRRP version. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [2, 3]</span>  <a id='label1172' href="javascript:ContentClick('label1173', 'label1172');" onmouseover="ContentPreview('label1173');" onmouseout="ContentUnpreview('label1173');" title="click to collapse or expand..."> more... </a>
 <div id="label1173" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>version</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrdst</span> - Monitor the route to this destination. <span class="li-normal">type: str</span> <a id='label1174' href="javascript:ContentClick('label1175', 'label1174');" onmouseover="ContentPreview('label1175');" onmouseout="ContentUnpreview('label1175');" title="click to collapse or expand..."> more... </a>
 <div id="label1175" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrdst</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrdst-priority</span> - Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254). <span class="li-normal">type: int</span>  <a id='label1176' href="javascript:ContentClick('label1177', 'label1176');" onmouseover="ContentPreview('label1177');" onmouseout="ContentUnpreview('label1177');" title="click to collapse or expand..."> more... </a>
 <div id="label1177" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrdst-priority</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrgrp</span> - VRRP group ID (1 - 65535). <span class="li-normal">type: int</span>  <a id='label1178' href="javascript:ContentClick('label1179', 'label1178');" onmouseover="ContentPreview('label1179');" onmouseout="ContentUnpreview('label1179');" title="click to collapse or expand..."> more... </a>
 <div id="label1179" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrgrp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrid</span> - Virtual router identifier (1 - 255). <span class="li-normal">type: int</span>  <a id='label1180' href="javascript:ContentClick('label1181', 'label1180');" onmouseover="ContentPreview('label1181');" onmouseout="ContentUnpreview('label1181');" title="click to collapse or expand..."> more... </a>
 <div id="label1181" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vrip</span> - IP address of the virtual router. <span class="li-normal">type: str</span>  <a id='label1182' href="javascript:ContentClick('label1183', 'label1182');" onmouseover="ContentPreview('label1183');" onmouseout="ContentUnpreview('label1183');" title="click to collapse or expand..."> more... </a>
 <div id="label1183" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 <li><span class="li-head">vrrp-virtual-mac</span> - Enable/disable use of virtual MAC for VRRP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1184' href="javascript:ContentClick('label1185', 'label1184');" onmouseover="ContentPreview('label1185');" onmouseout="ContentUnpreview('label1185');" title="click to collapse or expand..."> more... </a>
 <div id="label1185" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vrrp-virtual-mac</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wccp</span> - Enable/disable WCCP on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1186' href="javascript:ContentClick('label1187', 'label1186');" onmouseover="ContentPreview('label1187');" onmouseout="ContentUnpreview('label1187');" title="click to collapse or expand..."> more... </a>
 <div id="label1187" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wccp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">weight</span> - Default weight for static routes (if route has no weight configured). <span class="li-normal">type: int</span>  <a id='label1188' href="javascript:ContentClick('label1189', 'label1188');" onmouseover="ContentPreview('label1189');" onmouseout="ContentUnpreview('label1189');" title="click to collapse or expand..."> more... </a>
 <div id="label1189" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>weight</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-5g-threshold</span> - Minimal signal strength to be considered as a good 5G AP. <span class="li-normal">type: str</span>  <a id='label1190' href="javascript:ContentClick('label1191', 'label1190');" onmouseover="ContentPreview('label1191');" onmouseout="ContentUnpreview('label1191');" title="click to collapse or expand..."> more... </a>
 <div id="label1191" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-5g-threshold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-acl</span> - Access control for MAC addresses in the MAC list. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span>  <a id='label1192' href="javascript:ContentClick('label1193', 'label1192');" onmouseover="ContentPreview('label1193');" onmouseout="ContentUnpreview('label1193');" title="click to collapse or expand..."> more... </a>
 <div id="label1193" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-acl</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ap-band</span> - How to select the AP to connect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, 5g-preferred, 5g-only]</span>  <a id='label1194' href="javascript:ContentClick('label1195', 'label1194');" onmouseover="ContentPreview('label1195');" onmouseout="ContentUnpreview('label1195');" title="click to collapse or expand..."> more... </a>
 <div id="label1195" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ap-band</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-auth</span> - WiFi authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [PSK, RADIUS, radius, usergroup]</span>  <a id='label1196' href="javascript:ContentClick('label1197', 'label1196');" onmouseover="ContentPreview('label1197');" onmouseout="ContentUnpreview('label1197');" title="click to collapse or expand..."> more... </a>
 <div id="label1197" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-auth</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-auto-connect</span> - Enable/disable WiFi network auto connect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1198' href="javascript:ContentClick('label1199', 'label1198');" onmouseover="ContentPreview('label1199');" onmouseout="ContentUnpreview('label1199');" title="click to collapse or expand..."> more... </a>
 <div id="label1199" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-auto-connect</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-auto-save</span> - Enable/disable WiFi network automatic save. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1200' href="javascript:ContentClick('label1201', 'label1200');" onmouseover="ContentPreview('label1201');" onmouseout="ContentUnpreview('label1201');" title="click to collapse or expand..."> more... </a>
 <div id="label1201" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-auto-save</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-broadcast-ssid</span> - Enable/disable SSID broadcast in the beacon. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1202' href="javascript:ContentClick('label1203', 'label1202');" onmouseover="ContentPreview('label1203');" onmouseout="ContentUnpreview('label1203');" title="click to collapse or expand..."> more... </a>
 <div id="label1203" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-broadcast-ssid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-encrypt</span> - Data encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TKIP, AES]</span>  <a id='label1204' href="javascript:ContentClick('label1205', 'label1204');" onmouseover="ContentPreview('label1205');" onmouseout="ContentUnpreview('label1205');" title="click to collapse or expand..."> more... </a>
 <div id="label1205" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-encrypt</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-fragment-threshold</span> - WiFi fragment threshold (800 - 2346). <span class="li-normal">type: int</span>  <a id='label1206' href="javascript:ContentClick('label1207', 'label1206');" onmouseover="ContentPreview('label1207');" onmouseout="ContentUnpreview('label1207');" title="click to collapse or expand..."> more... </a>
 <div id="label1207" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-fragment-threshold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-key</span> - WiFi WEP Key. <span class="li-normal">type: str</span> <a id='label1208' href="javascript:ContentClick('label1209', 'label1208');" onmouseover="ContentPreview('label1209');" onmouseout="ContentUnpreview('label1209');" title="click to collapse or expand..."> more... </a>
 <div id="label1209" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-key</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-keyindex</span> - WEP key index (1 - 4). <span class="li-normal">type: int</span>  <a id='label1210' href="javascript:ContentClick('label1211', 'label1210');" onmouseover="ContentPreview('label1211');" onmouseout="ContentUnpreview('label1211');" title="click to collapse or expand..."> more... </a>
 <div id="label1211" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-keyindex</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-mac-filter</span> - Enable/disable MAC filter status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1212' href="javascript:ContentClick('label1213', 'label1212');" onmouseover="ContentPreview('label1213');" onmouseout="ContentUnpreview('label1213');" title="click to collapse or expand..."> more... </a>
 <div id="label1213" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-mac-filter</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-passphrase</span> - WiFi pre-shared key for WPA. <span class="li-normal">type: str</span> <a id='label1214' href="javascript:ContentClick('label1215', 'label1214');" onmouseover="ContentPreview('label1215');" onmouseout="ContentUnpreview('label1215');" title="click to collapse or expand..."> more... </a>
 <div id="label1215" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-passphrase</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-radius-server</span> - WiFi RADIUS server for WPA. <span class="li-normal">type: str</span>  <a id='label1216' href="javascript:ContentClick('label1217', 'label1216');" onmouseover="ContentPreview('label1217');" onmouseout="ContentUnpreview('label1217');" title="click to collapse or expand..."> more... </a>
 <div id="label1217" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-radius-server</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-rts-threshold</span> - WiFi RTS threshold (256 - 2346). <span class="li-normal">type: int</span>  <a id='label1218' href="javascript:ContentClick('label1219', 'label1218');" onmouseover="ContentPreview('label1219');" onmouseout="ContentUnpreview('label1219');" title="click to collapse or expand..."> more... </a>
 <div id="label1219" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-rts-threshold</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-security</span> - Wireless access security of SSID. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise]</span>  <a id='label1220' href="javascript:ContentClick('label1221', 'label1220');" onmouseover="ContentPreview('label1221');" onmouseout="ContentUnpreview('label1221');" title="click to collapse or expand..."> more... </a>
 <div id="label1221" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-security</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-ssid</span> - IEEE 802. <span class="li-normal">type: str</span>  <a id='label1222' href="javascript:ContentClick('label1223', 'label1222');" onmouseover="ContentPreview('label1223');" onmouseout="ContentUnpreview('label1223');" title="click to collapse or expand..."> more... </a>
 <div id="label1223" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-ssid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wifi-usergroup</span> - WiFi user group for WPA. <span class="li-normal">type: str</span>  <a id='label1224' href="javascript:ContentClick('label1225', 'label1224');" onmouseover="ContentPreview('label1225');" onmouseout="ContentUnpreview('label1225');" title="click to collapse or expand..."> more... </a>
 <div id="label1225" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wifi-usergroup</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">wins-ip</span> - WINS server IP. <span class="li-normal">type: str</span>  <a id='label1226' href="javascript:ContentClick('label1227', 'label1226');" onmouseover="ContentPreview('label1227');" onmouseout="ContentUnpreview('label1227');" title="click to collapse or expand..."> more... </a>
 <div id="label1227" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>wins-ip</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-request-all-server</span> - Enable/disable sending of DHCP requests to all servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1228' href="javascript:ContentClick('label1229', 'label1228');" onmouseover="ContentPreview('label1229');" onmouseout="ContentUnpreview('label1229');" title="click to collapse or expand..."> more... </a>
 <div id="label1229" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-request-all-server</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stp-ha-secondary</span> - Control STP behaviour on HA secondary. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, priority-adjust]</span>  <a id='label1230' href="javascript:ContentClick('label1231', 'label1230');" onmouseover="ContentPreview('label1231');" onmouseout="ContentUnpreview('label1231');" title="click to collapse or expand..."> more... </a>
 <div id="label1231" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>stp-ha-secondary</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">switch-controller-dynamic</span> - Integrated FortiLink settings for managed FortiSwitch. <span class="li-normal">type: str</span>  <a id='label1232' href="javascript:ContentClick('label1233', 'label1232');" onmouseover="ContentPreview('label1233');" onmouseout="ContentUnpreview('label1233');" title="click to collapse or expand..."> more... </a>
 <div id="label1233" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>switch-controller-dynamic</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auth-cert</span> - HTTPS server certificate. <span class="li-normal">type: str</span>  <a id='label1234' href="javascript:ContentClick('label1235', 'label1234');" onmouseover="ContentPreview('label1235');" onmouseout="ContentUnpreview('label1235');" title="click to collapse or expand..."> more... </a>
 <div id="label1235" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auth-cert</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">auth-portal-addr</span> - Address of captive portal. <span class="li-normal">type: str</span>  <a id='label1236' href="javascript:ContentClick('label1237', 'label1236');" onmouseover="ContentPreview('label1237');" onmouseout="ContentUnpreview('label1237');" title="click to collapse or expand..."> more... </a>
 <div id="label1237" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>auth-portal-addr</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-classless-route-addition</span> - Enable/disable addition of classless static routes retrieved from DHCP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1238' href="javascript:ContentClick('label1239', 'label1238');" onmouseover="ContentPreview('label1239');" onmouseout="ContentUnpreview('label1239');" title="click to collapse or expand..."> more... </a>
 <div id="label1239" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-classless-route-addition</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-relay-link-selection</span> - DHCP relay link selection. <span class="li-normal">type: str</span>  <a id='label1240' href="javascript:ContentClick('label1241', 'label1240');" onmouseover="ContentPreview('label1241');" onmouseout="ContentUnpreview('label1241');" title="click to collapse or expand..."> more... </a>
 <div id="label1241" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dhcp-relay-link-selection</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dns-server-protocol</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [cleartext, dot, doh]</span>  <a id='label1242' href="javascript:ContentClick('label1243', 'label1242');" onmouseover="ContentPreview('label1243');" onmouseout="ContentUnpreview('label1243');" title="click to collapse or expand..."> more... </a>
 <div id="label1243" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dns-server-protocol</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">eap-ca-cert</span> - EAP CA certificate name. <span class="li-normal">type: str</span>  <a id='label1244' href="javascript:ContentClick('label1245', 'label1244');" onmouseover="ContentPreview('label1245');" onmouseout="ContentUnpreview('label1245');" title="click to collapse or expand..."> more... </a>
 <div id="label1245" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>eap-ca-cert</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">eap-identity</span> - EAP identity. <span class="li-normal">type: str</span>  <a id='label1246' href="javascript:ContentClick('label1247', 'label1246');" onmouseover="ContentPreview('label1247');" onmouseout="ContentUnpreview('label1247');" title="click to collapse or expand..."> more... </a>
 <div id="label1247" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>eap-identity</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">eap-method</span> - EAP method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tls, peap]</span>  <a id='label1248' href="javascript:ContentClick('label1249', 'label1248');" onmouseover="ContentPreview('label1249');" onmouseout="ContentUnpreview('label1249');" title="click to collapse or expand..."> more... </a>
 <div id="label1249" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>eap-method</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">eap-password</span> - No description for the parameter <span class="li-normal">type: str</span> <a id='label1250' href="javascript:ContentClick('label1251', 'label1250');" onmouseover="ContentPreview('label1251');" onmouseout="ContentUnpreview('label1251');" title="click to collapse or expand..."> more... </a>
 <div id="label1251" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>eap-password</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">eap-supplicant</span> - Enable/disable EAP-Supplicant. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1252' href="javascript:ContentClick('label1253', 'label1252');" onmouseover="ContentPreview('label1253');" onmouseout="ContentUnpreview('label1253');" title="click to collapse or expand..."> more... </a>
 <div id="label1253" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>eap-supplicant</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">eap-user-cert</span> - EAP user certificate name. <span class="li-normal">type: str</span>  <a id='label1254' href="javascript:ContentClick('label1255', 'label1254');" onmouseover="ContentPreview('label1255');" onmouseout="ContentUnpreview('label1255');" title="click to collapse or expand..."> more... </a>
 <div id="label1255" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>eap-user-cert</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ike-saml-server</span> - Configure IKE authentication SAML server. <span class="li-normal">type: str</span>  <a id='label1256' href="javascript:ContentClick('label1257', 'label1256');" onmouseover="ContentPreview('label1257');" onmouseout="ContentUnpreview('label1257');" title="click to collapse or expand..."> more... </a>
 <div id="label1257" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ike-saml-server</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lacp-ha-secondary</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1258' href="javascript:ContentClick('label1259', 'label1258');" onmouseover="ContentPreview('label1259');" onmouseout="ContentUnpreview('label1259');" title="click to collapse or expand..."> more... </a>
 <div id="label1259" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>lacp-ha-secondary</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-atm-qos</span> - SFP-DSL ADSL Fallback PVC ATM QoS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [cbr, rt-vbr, nrt-vbr]</span>  <a id='label1260' href="javascript:ContentClick('label1261', 'label1260');" onmouseover="ContentPreview('label1261');" onmouseout="ContentUnpreview('label1261');" title="click to collapse or expand..."> more... </a>
 <div id="label1261" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-atm-qos</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-chan</span> - SFP-DSL ADSL Fallback PVC Channel. <span class="li-normal">type: int</span>  <a id='label1262' href="javascript:ContentClick('label1263', 'label1262');" onmouseover="ContentPreview('label1263');" onmouseout="ContentUnpreview('label1263');" title="click to collapse or expand..."> more... </a>
 <div id="label1263" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-chan</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-crc</span> - SFP-DSL ADSL Fallback PVC CRC Option:  bit0: sar LLC preserve, bit1: ream LLC preserve, bit2: ream VC-MUX has crc. <span class="li-normal">type: int</span>  <a id='label1264' href="javascript:ContentClick('label1265', 'label1264');" onmouseover="ContentPreview('label1265');" onmouseout="ContentUnpreview('label1265');" title="click to collapse or expand..."> more... </a>
 <div id="label1265" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-crc</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-pcr</span> - SFP-DSL ADSL Fallback PVC Packet Cell Rate in cells (0 - 5500). <span class="li-normal">type: int</span>  <a id='label1266' href="javascript:ContentClick('label1267', 'label1266');" onmouseover="ContentPreview('label1267');" onmouseout="ContentUnpreview('label1267');" title="click to collapse or expand..."> more... </a>
 <div id="label1267" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-pcr</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-scr</span> - SFP-DSL ADSL Fallback PVC Sustainable Cell Rate in cells (0 - 5500). <span class="li-normal">type: int</span>  <a id='label1268' href="javascript:ContentClick('label1269', 'label1268');" onmouseover="ContentPreview('label1269');" onmouseout="ContentUnpreview('label1269');" title="click to collapse or expand..."> more... </a>
 <div id="label1269" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-scr</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-vlan-id</span> - SFP-DSL ADSL Fallback PVC VLAN ID. <span class="li-normal">type: int</span>  <a id='label1270' href="javascript:ContentClick('label1271', 'label1270');" onmouseover="ContentPreview('label1271');" onmouseout="ContentUnpreview('label1271');" title="click to collapse or expand..."> more... </a>
 <div id="label1271" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-vlan-id</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-vlan-rx-id</span> - SFP-DSL ADSL Fallback PVC VLANID RX. <span class="li-normal">type: int</span>  <a id='label1272' href="javascript:ContentClick('label1273', 'label1272');" onmouseover="ContentPreview('label1273');" onmouseout="ContentUnpreview('label1273');" title="click to collapse or expand..."> more... </a>
 <div id="label1273" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-vlan-rx-id</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-vlan-rx-op</span> - SFP-DSL ADSL Fallback PVC VLAN RX op. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass-through, replace, remove]</span>  <a id='label1274' href="javascript:ContentClick('label1275', 'label1274');" onmouseover="ContentPreview('label1275');" onmouseout="ContentUnpreview('label1275');" title="click to collapse or expand..."> more... </a>
 <div id="label1275" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-vlan-rx-op</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-vlan-tx-id</span> - SFP-DSL ADSL Fallback PVC VLAN ID TX. <span class="li-normal">type: int</span>  <a id='label1276' href="javascript:ContentClick('label1277', 'label1276');" onmouseover="ContentPreview('label1277');" onmouseout="ContentUnpreview('label1277');" title="click to collapse or expand..."> more... </a>
 <div id="label1277" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-vlan-tx-id</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pvc-vlan-tx-op</span> - SFP-DSL ADSL Fallback PVC VLAN TX op. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass-through, replace, remove]</span>  <a id='label1278' href="javascript:ContentClick('label1279', 'label1278');" onmouseover="ContentPreview('label1279');" onmouseout="ContentUnpreview('label1279');" title="click to collapse or expand..."> more... </a>
 <div id="label1279" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pvc-vlan-tx-op</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">reachable-time</span> - IPv4 reachable time in milliseconds (30000 - 3600000, default = 30000). <span class="li-normal">type: int</span>  <a id='label1280' href="javascript:ContentClick('label1281', 'label1280');" onmouseover="ContentPreview('label1281');" onmouseout="ContentUnpreview('label1281');" title="click to collapse or expand..."> more... </a>
 <div id="label1281" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>reachable-time</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">select-profile-30a-35b</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [30A, 35B]</span>  <a id='label1282' href="javascript:ContentClick('label1283', 'label1282');" onmouseover="ContentPreview('label1283');" onmouseout="ContentUnpreview('label1283');" title="click to collapse or expand..."> more... </a>
 <div id="label1283" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>select-profile-30a-35b</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sfp-dsl</span> - Enable/disable SFP DSL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1284' href="javascript:ContentClick('label1285', 'label1284');" onmouseover="ContentPreview('label1285');" onmouseout="ContentUnpreview('label1285');" title="click to collapse or expand..."> more... </a>
 <div id="label1285" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sfp-dsl</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sfp-dsl-adsl-fallback</span> - Enable/disable SFP DSL ADSL fallback. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1286' href="javascript:ContentClick('label1287', 'label1286');" onmouseover="ContentPreview('label1287');" onmouseout="ContentUnpreview('label1287');" title="click to collapse or expand..."> more... </a>
 <div id="label1287" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sfp-dsl-adsl-fallback</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sfp-dsl-autodetect</span> - Enable/disable SFP DSL MAC address autodetect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label1288' href="javascript:ContentClick('label1289', 'label1288');" onmouseover="ContentPreview('label1289');" onmouseout="ContentUnpreview('label1289');" title="click to collapse or expand..."> more... </a>
 <div id="label1289" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sfp-dsl-autodetect</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sfp-dsl-mac</span> - SFP DSL MAC address. <span class="li-normal">type: str</span>  <a id='label1290' href="javascript:ContentClick('label1291', 'label1290');" onmouseover="ContentPreview('label1291');" onmouseout="ContentUnpreview('label1291');" title="click to collapse or expand..."> more... </a>
 <div id="label1291" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sfp-dsl-mac</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sw-algorithm</span> - Frame distribution algorithm for switch. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [l2, l3, eh]</span>  <a id='label1292' href="javascript:ContentClick('label1293', 'label1292');" onmouseover="ContentPreview('label1293');" onmouseout="ContentUnpreview('label1293');" title="click to collapse or expand..."> more... </a>
 <div id="label1293" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>sw-algorithm</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">system-id</span> - Define a system ID for the aggregate interface. <span class="li-normal">type: str</span>  <a id='label1294' href="javascript:ContentClick('label1295', 'label1294');" onmouseover="ContentPreview('label1295');" onmouseout="ContentUnpreview('label1295');" title="click to collapse or expand..."> more... </a>
 <div id="label1295" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>system-id</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">system-id-type</span> - Method in which system ID is generated. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, user]</span>  <a id='label1296' href="javascript:ContentClick('label1297', 'label1296');" onmouseover="ContentPreview('label1297');" onmouseout="ContentUnpreview('label1297');" title="click to collapse or expand..."> more... </a>
 <div id="label1297" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>system-id-type</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlan-id</span> - No description for the parameter <span class="li-normal">type: int</span>  <a id='label1298' href="javascript:ContentClick('label1299', 'label1298');" onmouseover="ContentPreview('label1299');" onmouseout="ContentUnpreview('label1299');" title="click to collapse or expand..."> more... </a>
 <div id="label1299" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vlan-id</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlan-op-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tag, untag, passthrough]</span>  <a id='label1300' href="javascript:ContentClick('label1301', 'label1300');" onmouseover="ContentPreview('label1301');" onmouseout="ContentUnpreview('label1301');" title="click to collapse or expand..."> more... </a>
 <div id="label1301" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>vlan-op-mode</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
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
    - name: no description
      fmgr_fsp_vlan:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         fsp_vlan:
            _dhcp-status: <value in [disable, enable]>
            auth: <value in [radius, usergroup]>
            color: <value of integer>
            comments: <value of string>
            dynamic_mapping:
              -
                  _dhcp-status: <value in [disable, enable]>
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  dhcp-server:
                     auto-configuration: <value in [disable, enable]>
                     auto-managed-status: <value in [disable, enable]>
                     conflicted-ip-timeout: <value of integer>
                     ddns-auth: <value in [disable, tsig]>
                     ddns-key: <value of string>
                     ddns-keyname: <value of string>
                     ddns-server-ip: <value of string>
                     ddns-ttl: <value of integer>
                     ddns-update: <value in [disable, enable]>
                     ddns-update-override: <value in [disable, enable]>
                     ddns-zone: <value of string>
                     default-gateway: <value of string>
                     dhcp-settings-from-fortiipam: <value in [disable, enable]>
                     dns-server1: <value of string>
                     dns-server2: <value of string>
                     dns-server3: <value of string>
                     dns-server4: <value of string>
                     dns-service: <value in [default, specify, local]>
                     domain: <value of string>
                     enable: <value in [disable, enable]>
                     exclude-range:
                       -
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     filename: <value of string>
                     forticlient-on-net-status: <value in [disable, enable]>
                     id: <value of integer>
                     ip-mode: <value in [range, usrgrp]>
                     ip-range:
                       -
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     ipsec-lease-hold: <value of integer>
                     lease-time: <value of integer>
                     mac-acl-default-action: <value in [assign, block]>
                     netmask: <value of string>
                     next-server: <value of string>
                     ntp-server1: <value of string>
                     ntp-server2: <value of string>
                     ntp-server3: <value of string>
                     ntp-service: <value in [default, specify, local]>
                     option1: <value of string>
                     option2: <value of string>
                     option3: <value of string>
                     option4: <value of string>
                     option5: <value of string>
                     option6: <value of string>
                     options:
                       -
                           code: <value of integer>
                           id: <value of integer>
                           ip: <value of string>
                           type: <value in [hex, string, ip, ...]>
                           value: <value of string>
                     reserved-address:
                       -
                           action: <value in [assign, block, reserved]>
                           circuit-id: <value of string>
                           circuit-id-type: <value in [hex, string]>
                           description: <value of string>
                           id: <value of integer>
                           ip: <value of string>
                           mac: <value of string>
                           remote-id: <value of string>
                           remote-id-type: <value in [hex, string]>
                           type: <value in [mac, option82]>
                     server-type: <value in [regular, ipsec]>
                     status: <value in [disable, enable]>
                     tftp-server: <value of string>
                     timezone: <value in [00, 01, 02, ...]>
                     timezone-option: <value in [disable, default, specify]>
                     vci-match: <value in [disable, enable]>
                     vci-string: <value of string>
                     wifi-ac-service: <value in [specify, local]>
                     wifi-ac1: <value of string>
                     wifi-ac2: <value of string>
                     wifi-ac3: <value of string>
                     wins-server1: <value of string>
                     wins-server2: <value of string>
                  interface:
                     dhcp-relay-agent-option: <value in [disable, enable]>
                     dhcp-relay-ip: <value of string>
                     dhcp-relay-service: <value in [disable, enable]>
                     dhcp-relay-type: <value in [regular, ipsec]>
                     ip: <value of string>
                     ipv6:
                        autoconf: <value in [disable, enable]>
                        dhcp6-client-options:
                          - rapid
                          - iapd
                          - iana
                          - dns
                          - dnsname
                        dhcp6-information-request: <value in [disable, enable]>
                        dhcp6-prefix-delegation: <value in [disable, enable]>
                        dhcp6-prefix-hint: <value of string>
                        dhcp6-prefix-hint-plt: <value of integer>
                        dhcp6-prefix-hint-vlt: <value of integer>
                        dhcp6-relay-ip: <value of string>
                        dhcp6-relay-service: <value in [disable, enable]>
                        dhcp6-relay-type: <value in [regular]>
                        icmp6-send-redirect: <value in [disable, enable]>
                        interface-identifier: <value of string>
                        ip6-address: <value of string>
                        ip6-allowaccess:
                          - https
                          - ping
                          - ssh
                          - snmp
                          - http
                          - telnet
                          - fgfm
                          - capwap
                          - fabric
                        ip6-default-life: <value of integer>
                        ip6-delegated-prefix-list:
                          -
                              autonomous-flag: <value in [disable, enable]>
                              onlink-flag: <value in [disable, enable]>
                              prefix-id: <value of integer>
                              rdnss: <value of string>
                              rdnss-service: <value in [delegated, default, specify]>
                              subnet: <value of string>
                              upstream-interface: <value of string>
                              delegated-prefix-iaid: <value of integer>
                        ip6-dns-server-override: <value in [disable, enable]>
                        ip6-extra-addr:
                          -
                              prefix: <value of string>
                        ip6-hop-limit: <value of integer>
                        ip6-link-mtu: <value of integer>
                        ip6-manage-flag: <value in [disable, enable]>
                        ip6-max-interval: <value of integer>
                        ip6-min-interval: <value of integer>
                        ip6-mode: <value in [static, dhcp, pppoe, ...]>
                        ip6-other-flag: <value in [disable, enable]>
                        ip6-prefix-list:
                          -
                              autonomous-flag: <value in [disable, enable]>
                              dnssl: <value of string>
                              onlink-flag: <value in [disable, enable]>
                              preferred-life-time: <value of integer>
                              prefix: <value of string>
                              rdnss: <value of string>
                              valid-life-time: <value of integer>
                        ip6-reachable-time: <value of integer>
                        ip6-retrans-time: <value of integer>
                        ip6-send-adv: <value in [disable, enable]>
                        ip6-subnet: <value of string>
                        ip6-upstream-interface: <value of string>
                        nd-cert: <value of string>
                        nd-cga-modifier: <value of string>
                        nd-mode: <value in [basic, SEND-compatible]>
                        nd-security-level: <value of integer>
                        nd-timestamp-delta: <value of integer>
                        nd-timestamp-fuzz: <value of integer>
                        unique-autoconf-addr: <value in [disable, enable]>
                        vrip6_link_local: <value of string>
                        vrrp-virtual-mac6: <value in [disable, enable]>
                        vrrp6:
                          -
                              accept-mode: <value in [disable, enable]>
                              adv-interval: <value of integer>
                              preempt: <value in [disable, enable]>
                              priority: <value of integer>
                              start-time: <value of integer>
                              status: <value in [disable, enable]>
                              vrdst6: <value of string>
                              vrgrp: <value of integer>
                              vrid: <value of integer>
                              vrip6: <value of string>
                        cli-conn6-status: <value of integer>
                        ip6-prefix-mode: <value in [dhcp6, ra]>
                        ra-send-mtu: <value in [disable, enable]>
                        ip6-delegated-prefix-iaid: <value of integer>
                     secondary-IP: <value in [disable, enable]>
                     secondaryip:
                       -
                           allowaccess:
                             - https
                             - ping
                             - ssh
                             - snmp
                             - http
                             - telnet
                             - fgfm
                             - auto-ipsec
                             - radius-acct
                             - probe-response
                             - capwap
                             - dnp
                             - ftm
                             - fabric
                             - speed-test
                           detectprotocol:
                             - ping
                             - tcp-echo
                             - udp-echo
                           detectserver: <value of string>
                           gwdetect: <value in [disable, enable]>
                           ha-priority: <value of integer>
                           id: <value of integer>
                           ip: <value of string>
                           ping-serv-status: <value of integer>
                           seq: <value of integer>
                     vlanid: <value of integer>
                     dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
            name: <value of string>
            portal-message-override-group: <value of string>
            radius-server: <value of string>
            security: <value in [open, captive-portal, 8021x]>
            selected-usergroups: <value of string>
            usergroup: <value of string>
            vdom: <value of string>
            vlanid: <value of integer>
            dhcp-server:
               auto-configuration: <value in [disable, enable]>
               auto-managed-status: <value in [disable, enable]>
               conflicted-ip-timeout: <value of integer>
               ddns-auth: <value in [disable, tsig]>
               ddns-key: <value of string>
               ddns-keyname: <value of string>
               ddns-server-ip: <value of string>
               ddns-ttl: <value of integer>
               ddns-update: <value in [disable, enable]>
               ddns-update-override: <value in [disable, enable]>
               ddns-zone: <value of string>
               default-gateway: <value of string>
               dhcp-settings-from-fortiipam: <value in [disable, enable]>
               dns-server1: <value of string>
               dns-server2: <value of string>
               dns-server3: <value of string>
               dns-server4: <value of string>
               dns-service: <value in [default, specify, local]>
               domain: <value of string>
               enable: <value in [disable, enable]>
               exclude-range:
                 -
                     end-ip: <value of string>
                     id: <value of integer>
                     start-ip: <value of string>
               filename: <value of string>
               forticlient-on-net-status: <value in [disable, enable]>
               id: <value of integer>
               ip-mode: <value in [range, usrgrp]>
               ip-range:
                 -
                     end-ip: <value of string>
                     id: <value of integer>
                     start-ip: <value of string>
               ipsec-lease-hold: <value of integer>
               lease-time: <value of integer>
               mac-acl-default-action: <value in [assign, block]>
               netmask: <value of string>
               next-server: <value of string>
               ntp-server1: <value of string>
               ntp-server2: <value of string>
               ntp-server3: <value of string>
               ntp-service: <value in [default, specify, local]>
               option1: <value of string>
               option2: <value of string>
               option3: <value of string>
               option4: <value of string>
               option5: <value of string>
               option6: <value of string>
               options:
                 -
                     code: <value of integer>
                     id: <value of integer>
                     ip: <value of string>
                     type: <value in [hex, string, ip, ...]>
                     value: <value of string>
               reserved-address:
                 -
                     action: <value in [assign, block, reserved]>
                     circuit-id: <value of string>
                     circuit-id-type: <value in [hex, string]>
                     description: <value of string>
                     id: <value of integer>
                     ip: <value of string>
                     mac: <value of string>
                     remote-id: <value of string>
                     remote-id-type: <value in [hex, string]>
                     type: <value in [mac, option82]>
               server-type: <value in [regular, ipsec]>
               status: <value in [disable, enable]>
               tftp-server: <value of string>
               timezone: <value in [00, 01, 02, ...]>
               timezone-option: <value in [disable, default, specify]>
               vci-match: <value in [disable, enable]>
               vci-string: <value of string>
               wifi-ac-service: <value in [specify, local]>
               wifi-ac1: <value of string>
               wifi-ac2: <value of string>
               wifi-ac3: <value of string>
               wins-server1: <value of string>
               wins-server2: <value of string>
            interface:
               ac-name: <value of string>
               aggregate: <value of string>
               algorithm: <value in [L2, L3, L4, ...]>
               alias: <value of string>
               allowaccess:
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - auto-ipsec
                 - radius-acct
                 - probe-response
                 - capwap
                 - dnp
                 - ftm
                 - fabric
                 - speed-test
               ap-discover: <value in [disable, enable]>
               arpforward: <value in [disable, enable]>
               atm-protocol: <value in [none, ipoa]>
               auth-type: <value in [auto, pap, chap, ...]>
               auto-auth-extension-device: <value in [disable, enable]>
               bandwidth-measure-time: <value of integer>
               bfd: <value in [global, enable, disable]>
               bfd-desired-min-tx: <value of integer>
               bfd-detect-mult: <value of integer>
               bfd-required-min-rx: <value of integer>
               broadcast-forticlient-discovery: <value in [disable, enable]>
               broadcast-forward: <value in [disable, enable]>
               captive-portal: <value of integer>
               cli-conn-status: <value of integer>
               color: <value of integer>
               ddns: <value in [disable, enable]>
               ddns-auth: <value in [disable, tsig]>
               ddns-domain: <value of string>
               ddns-key: <value of string>
               ddns-keyname: <value of string>
               ddns-password: <value of string>
               ddns-server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
               ddns-server-ip: <value of string>
               ddns-sn: <value of string>
               ddns-ttl: <value of integer>
               ddns-username: <value of string>
               ddns-zone: <value of string>
               dedicated-to: <value in [none, management]>
               defaultgw: <value in [disable, enable]>
               description: <value of string>
               detected-peer-mtu: <value of integer>
               detectprotocol:
                 - ping
                 - tcp-echo
                 - udp-echo
               detectserver: <value of string>
               device-access-list: <value of string>
               device-identification: <value in [disable, enable]>
               device-identification-active-scan: <value in [disable, enable]>
               device-netscan: <value in [disable, enable]>
               device-user-identification: <value in [disable, enable]>
               devindex: <value of integer>
               dhcp-client-identifier: <value of string>
               dhcp-relay-agent-option: <value in [disable, enable]>
               dhcp-relay-interface: <value of string>
               dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
               dhcp-relay-ip: <value of string>
               dhcp-relay-service: <value in [disable, enable]>
               dhcp-relay-type: <value in [regular, ipsec]>
               dhcp-renew-time: <value of integer>
               disc-retry-timeout: <value of integer>
               disconnect-threshold: <value of integer>
               distance: <value of integer>
               dns-query: <value in [disable, recursive, non-recursive]>
               dns-server-override: <value in [disable, enable]>
               drop-fragment: <value in [disable, enable]>
               drop-overlapped-fragment: <value in [disable, enable]>
               egress-cos: <value in [disable, cos0, cos1, ...]>
               egress-shaping-profile: <value of string>
               eip: <value of string>
               endpoint-compliance: <value in [disable, enable]>
               estimated-downstream-bandwidth: <value of integer>
               estimated-upstream-bandwidth: <value of integer>
               explicit-ftp-proxy: <value in [disable, enable]>
               explicit-web-proxy: <value in [disable, enable]>
               external: <value in [disable, enable]>
               fail-action-on-extender: <value in [soft-restart, hard-restart, reboot]>
               fail-alert-interfaces: <value of string>
               fail-alert-method: <value in [link-failed-signal, link-down]>
               fail-detect: <value in [disable, enable]>
               fail-detect-option:
                 - detectserver
                 - link-down
               fdp: <value in [disable, enable]>
               fortiheartbeat: <value in [disable, enable]>
               fortilink: <value in [disable, enable]>
               fortilink-backup-link: <value of integer>
               fortilink-neighbor-detect: <value in [lldp, fortilink]>
               fortilink-split-interface: <value in [disable, enable]>
               fortilink-stacking: <value in [disable, enable]>
               forward-domain: <value of integer>
               forward-error-correction: <value in [disable, enable, rs-fec, ...]>
               fp-anomaly:
                 - drop_tcp_fin_noack
                 - pass_winnuke
                 - pass_tcpland
                 - pass_udpland
                 - pass_icmpland
                 - pass_ipland
                 - pass_iprr
                 - pass_ipssrr
                 - pass_iplsrr
                 - pass_ipstream
                 - pass_ipsecurity
                 - pass_iptimestamp
                 - pass_ipunknown_option
                 - pass_ipunknown_prot
                 - pass_icmp_frag
                 - pass_tcp_no_flag
                 - pass_tcp_fin_noack
                 - drop_winnuke
                 - drop_tcpland
                 - drop_udpland
                 - drop_icmpland
                 - drop_ipland
                 - drop_iprr
                 - drop_ipssrr
                 - drop_iplsrr
                 - drop_ipstream
                 - drop_ipsecurity
                 - drop_iptimestamp
                 - drop_ipunknown_option
                 - drop_ipunknown_prot
                 - drop_icmp_frag
                 - drop_tcp_no_flag
               fp-disable:
                 - all
                 - ipsec
                 - none
               gateway-address: <value of string>
               gi-gk: <value in [disable, enable]>
               gwaddr: <value of string>
               gwdetect: <value in [disable, enable]>
               ha-priority: <value of integer>
               icmp-accept-redirect: <value in [disable, enable]>
               icmp-redirect: <value in [disable, enable]>
               icmp-send-redirect: <value in [disable, enable]>
               ident-accept: <value in [disable, enable]>
               idle-timeout: <value of integer>
               if-mdix: <value in [auto, normal, crossover]>
               if-media: <value in [auto, copper, fiber]>
               in-force-vlan-cos: <value of integer>
               inbandwidth: <value of integer>
               ingress-cos: <value in [disable, cos0, cos1, ...]>
               ingress-shaping-profile: <value of string>
               ingress-spillover-threshold: <value of integer>
               internal: <value of integer>
               ip: <value of string>
               ip-managed-by-fortiipam: <value in [disable, enable]>
               ipmac: <value in [disable, enable]>
               ips-sniffer-mode: <value in [disable, enable]>
               ipunnumbered: <value of string>
               ipv6:
                  autoconf: <value in [disable, enable]>
                  dhcp6-client-options:
                    - rapid
                    - iapd
                    - iana
                    - dns
                    - dnsname
                  dhcp6-information-request: <value in [disable, enable]>
                  dhcp6-prefix-delegation: <value in [disable, enable]>
                  dhcp6-prefix-hint: <value of string>
                  dhcp6-prefix-hint-plt: <value of integer>
                  dhcp6-prefix-hint-vlt: <value of integer>
                  dhcp6-relay-ip: <value of string>
                  dhcp6-relay-service: <value in [disable, enable]>
                  dhcp6-relay-type: <value in [regular]>
                  icmp6-send-redirect: <value in [disable, enable]>
                  interface-identifier: <value of string>
                  ip6-address: <value of string>
                  ip6-allowaccess:
                    - https
                    - ping
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - capwap
                    - fabric
                  ip6-default-life: <value of integer>
                  ip6-delegated-prefix-list:
                    -
                        autonomous-flag: <value in [disable, enable]>
                        onlink-flag: <value in [disable, enable]>
                        prefix-id: <value of integer>
                        rdnss: <value of string>
                        rdnss-service: <value in [delegated, default, specify]>
                        subnet: <value of string>
                        upstream-interface: <value of string>
                        delegated-prefix-iaid: <value of integer>
                  ip6-dns-server-override: <value in [disable, enable]>
                  ip6-extra-addr:
                    -
                        prefix: <value of string>
                  ip6-hop-limit: <value of integer>
                  ip6-link-mtu: <value of integer>
                  ip6-manage-flag: <value in [disable, enable]>
                  ip6-max-interval: <value of integer>
                  ip6-min-interval: <value of integer>
                  ip6-mode: <value in [static, dhcp, pppoe, ...]>
                  ip6-other-flag: <value in [disable, enable]>
                  ip6-prefix-list:
                    -
                        autonomous-flag: <value in [disable, enable]>
                        dnssl: <value of string>
                        onlink-flag: <value in [disable, enable]>
                        preferred-life-time: <value of integer>
                        prefix: <value of string>
                        rdnss: <value of string>
                        valid-life-time: <value of integer>
                  ip6-reachable-time: <value of integer>
                  ip6-retrans-time: <value of integer>
                  ip6-send-adv: <value in [disable, enable]>
                  ip6-subnet: <value of string>
                  ip6-upstream-interface: <value of string>
                  nd-cert: <value of string>
                  nd-cga-modifier: <value of string>
                  nd-mode: <value in [basic, SEND-compatible]>
                  nd-security-level: <value of integer>
                  nd-timestamp-delta: <value of integer>
                  nd-timestamp-fuzz: <value of integer>
                  unique-autoconf-addr: <value in [disable, enable]>
                  vrip6_link_local: <value of string>
                  vrrp-virtual-mac6: <value in [disable, enable]>
                  vrrp6:
                    -
                        accept-mode: <value in [disable, enable]>
                        adv-interval: <value of integer>
                        preempt: <value in [disable, enable]>
                        priority: <value of integer>
                        start-time: <value of integer>
                        status: <value in [disable, enable]>
                        vrdst6: <value of string>
                        vrgrp: <value of integer>
                        vrid: <value of integer>
                        vrip6: <value of string>
                  cli-conn6-status: <value of integer>
                  ip6-prefix-mode: <value in [dhcp6, ra]>
                  ra-send-mtu: <value in [disable, enable]>
                  ip6-delegated-prefix-iaid: <value of integer>
               l2forward: <value in [disable, enable]>
               l2tp-client: <value in [disable, enable]>
               lacp-ha-slave: <value in [disable, enable]>
               lacp-mode: <value in [static, passive, active]>
               lacp-speed: <value in [slow, fast]>
               lcp-echo-interval: <value of integer>
               lcp-max-echo-fails: <value of integer>
               link-up-delay: <value of integer>
               listen-forticlient-connection: <value in [disable, enable]>
               lldp-network-policy: <value of string>
               lldp-reception: <value in [disable, enable, vdom]>
               lldp-transmission: <value in [enable, disable, vdom]>
               log: <value in [disable, enable]>
               macaddr: <value of string>
               managed-subnetwork-size: <value in [256, 512, 1024, ...]>
               management-ip: <value of string>
               max-egress-burst-rate: <value of integer>
               max-egress-rate: <value of integer>
               measured-downstream-bandwidth: <value of integer>
               measured-upstream-bandwidth: <value of integer>
               mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
               member: <value of string>
               min-links: <value of integer>
               min-links-down: <value in [operational, administrative]>
               mode: <value in [static, dhcp, pppoe, ...]>
               monitor-bandwidth: <value in [disable, enable]>
               mtu: <value of integer>
               mtu-override: <value in [disable, enable]>
               mux-type: <value in [llc-encaps, vc-encaps]>
               name: <value of string>
               ndiscforward: <value in [disable, enable]>
               netbios-forward: <value in [disable, enable]>
               netflow-sampler: <value in [disable, tx, rx, ...]>
               np-qos-profile: <value of integer>
               npu-fastpath: <value in [disable, enable]>
               nst: <value in [disable, enable]>
               out-force-vlan-cos: <value of integer>
               outbandwidth: <value of integer>
               padt-retry-timeout: <value of integer>
               password: <value of string>
               peer-interface: <value of string>
               phy-mode: <value in [auto, adsl, vdsl, ...]>
               ping-serv-status: <value of integer>
               poe: <value in [disable, enable]>
               polling-interval: <value of integer>
               pppoe-unnumbered-negotiate: <value in [disable, enable]>
               pptp-auth-type: <value in [auto, pap, chap, ...]>
               pptp-client: <value in [disable, enable]>
               pptp-password: <value of string>
               pptp-server-ip: <value of string>
               pptp-timeout: <value of integer>
               pptp-user: <value of string>
               preserve-session-route: <value in [disable, enable]>
               priority: <value of integer>
               priority-override: <value in [disable, enable]>
               proxy-captive-portal: <value in [disable, enable]>
               redundant-interface: <value of string>
               remote-ip: <value of string>
               replacemsg-override-group: <value of string>
               retransmission: <value in [disable, enable]>
               ring-rx: <value of integer>
               ring-tx: <value of integer>
               role: <value in [lan, wan, dmz, ...]>
               sample-direction: <value in [rx, tx, both]>
               sample-rate: <value of integer>
               scan-botnet-connections: <value in [disable, block, monitor]>
               secondary-IP: <value in [disable, enable]>
               secondaryip:
                 -
                     allowaccess:
                       - https
                       - ping
                       - ssh
                       - snmp
                       - http
                       - telnet
                       - fgfm
                       - auto-ipsec
                       - radius-acct
                       - probe-response
                       - capwap
                       - dnp
                       - ftm
                       - fabric
                       - speed-test
                     detectprotocol:
                       - ping
                       - tcp-echo
                       - udp-echo
                     detectserver: <value of string>
                     gwdetect: <value in [disable, enable]>
                     ha-priority: <value of integer>
                     id: <value of integer>
                     ip: <value of string>
                     ping-serv-status: <value of integer>
                     seq: <value of integer>
               security-8021x-dynamic-vlan-id: <value of integer>
               security-8021x-master: <value of string>
               security-8021x-mode: <value in [default, dynamic-vlan, fallback, ...]>
               security-exempt-list: <value of string>
               security-external-logout: <value of string>
               security-external-web: <value of string>
               security-groups: <value of string>
               security-mac-auth-bypass: <value in [disable, enable, mac-auth-only]>
               security-mode: <value in [none, captive-portal, 802.1X]>
               security-redirect-url: <value of string>
               service-name: <value of string>
               sflow-sampler: <value in [disable, enable]>
               speed: <value in [auto, 10full, 10half, ...]>
               spillover-threshold: <value of integer>
               src-check: <value in [disable, enable]>
               status: <value in [down, up]>
               stp: <value in [disable, enable]>
               stp-ha-slave: <value in [disable, enable, priority-adjust]>
               stpforward: <value in [disable, enable]>
               stpforward-mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
               strip-priority-vlan-tag: <value in [disable, enable]>
               subst: <value in [disable, enable]>
               substitute-dst-mac: <value of string>
               swc-first-create: <value of integer>
               swc-vlan: <value of integer>
               switch: <value of string>
               switch-controller-access-vlan: <value in [disable, enable]>
               switch-controller-arp-inspection: <value in [disable, enable]>
               switch-controller-auth: <value in [radius, usergroup]>
               switch-controller-dhcp-snooping: <value in [disable, enable]>
               switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
               switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
               switch-controller-feature: <value in [none, default-vlan, quarantine, ...]>
               switch-controller-igmp-snooping: <value in [disable, enable]>
               switch-controller-igmp-snooping-fast-leave: <value in [disable, enable]>
               switch-controller-igmp-snooping-proxy: <value in [disable, enable]>
               switch-controller-iot-scanning: <value in [disable, enable]>
               switch-controller-learning-limit: <value of integer>
               switch-controller-mgmt-vlan: <value of integer>
               switch-controller-nac: <value of string>
               switch-controller-radius-server: <value of string>
               switch-controller-rspan-mode: <value in [disable, enable]>
               switch-controller-source-ip: <value in [outbound, fixed]>
               switch-controller-traffic-policy: <value of string>
               tc-mode: <value in [ptm, atm]>
               tcp-mss: <value of integer>
               trunk: <value in [disable, enable]>
               trust-ip-1: <value of string>
               trust-ip-2: <value of string>
               trust-ip-3: <value of string>
               trust-ip6-1: <value of string>
               trust-ip6-2: <value of string>
               trust-ip6-3: <value of string>
               type: <value in [physical, vlan, aggregate, ...]>
               username: <value of string>
               vci: <value of integer>
               vectoring: <value in [disable, enable]>
               vindex: <value of integer>
               vlan-protocol: <value in [8021q, 8021ad]>
               vlanforward: <value in [disable, enable]>
               vlanid: <value of integer>
               vpi: <value of integer>
               vrf: <value of integer>
               vrrp:
                 -
                     accept-mode: <value in [disable, enable]>
                     adv-interval: <value of integer>
                     ignore-default-route: <value in [disable, enable]>
                     preempt: <value in [disable, enable]>
                     priority: <value of integer>
                     start-time: <value of integer>
                     status: <value in [disable, enable]>
                     version: <value in [2, 3]>
                     vrdst: <value of string>
                     vrdst-priority: <value of integer>
                     vrgrp: <value of integer>
                     vrid: <value of integer>
                     vrip: <value of string>
               vrrp-virtual-mac: <value in [disable, enable]>
               wccp: <value in [disable, enable]>
               weight: <value of integer>
               wifi-5g-threshold: <value of string>
               wifi-acl: <value in [deny, allow]>
               wifi-ap-band: <value in [any, 5g-preferred, 5g-only]>
               wifi-auth: <value in [PSK, RADIUS, radius, ...]>
               wifi-auto-connect: <value in [disable, enable]>
               wifi-auto-save: <value in [disable, enable]>
               wifi-broadcast-ssid: <value in [disable, enable]>
               wifi-encrypt: <value in [TKIP, AES]>
               wifi-fragment-threshold: <value of integer>
               wifi-key: <value of string>
               wifi-keyindex: <value of integer>
               wifi-mac-filter: <value in [disable, enable]>
               wifi-passphrase: <value of string>
               wifi-radius-server: <value of string>
               wifi-rts-threshold: <value of integer>
               wifi-security: <value in [None, WEP64, wep64, ...]>
               wifi-ssid: <value of string>
               wifi-usergroup: <value of string>
               wins-ip: <value of string>
               dhcp-relay-request-all-server: <value in [disable, enable]>
               stp-ha-secondary: <value in [disable, enable, priority-adjust]>
               switch-controller-dynamic: <value of string>
               auth-cert: <value of string>
               auth-portal-addr: <value of string>
               dhcp-classless-route-addition: <value in [disable, enable]>
               dhcp-relay-link-selection: <value of string>
               dns-server-protocol:
                 - cleartext
                 - dot
                 - doh
               eap-ca-cert: <value of string>
               eap-identity: <value of string>
               eap-method: <value in [tls, peap]>
               eap-password: <value of string>
               eap-supplicant: <value in [disable, enable]>
               eap-user-cert: <value of string>
               ike-saml-server: <value of string>
               lacp-ha-secondary: <value in [disable, enable]>
               pvc-atm-qos: <value in [cbr, rt-vbr, nrt-vbr]>
               pvc-chan: <value of integer>
               pvc-crc: <value of integer>
               pvc-pcr: <value of integer>
               pvc-scr: <value of integer>
               pvc-vlan-id: <value of integer>
               pvc-vlan-rx-id: <value of integer>
               pvc-vlan-rx-op: <value in [pass-through, replace, remove]>
               pvc-vlan-tx-id: <value of integer>
               pvc-vlan-tx-op: <value in [pass-through, replace, remove]>
               reachable-time: <value of integer>
               select-profile-30a-35b: <value in [30A, 35B]>
               sfp-dsl: <value in [disable, enable]>
               sfp-dsl-adsl-fallback: <value in [disable, enable]>
               sfp-dsl-autodetect: <value in [disable, enable]>
               sfp-dsl-mac: <value of string>
               sw-algorithm: <value in [l2, l3, eh]>
               system-id: <value of string>
               system-id-type: <value in [auto, user]>
               vlan-id: <value of integer>
               vlan-op-mode: <value in [tag, untag, passthrough]>



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



