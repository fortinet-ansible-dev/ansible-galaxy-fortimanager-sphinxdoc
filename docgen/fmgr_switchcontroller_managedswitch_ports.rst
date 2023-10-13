:source: fmgr_switchcontroller_managedswitch_ports.py

:orphan:

.. _fmgr_switchcontroller_managedswitch_ports:

fmgr_switchcontroller_managedswitch_ports -- Managed-switch port list.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

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

- ansible>=2.9.0



FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <br>
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 <p>



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
 <li><span class="li-head">managed-switch</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">switchcontroller_managedswitch_ports</span> - Managed-switch port list. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">allowed-vlans</span> - Configure switch port tagged vlans <span class="li-normal">type: list or str</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">allowed-vlans-all</span> - Enable/disable all defined vlans on this port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">arp-inspection-trust</span> - Trusted or untrusted dynamic ARP inspection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [untrusted, trusted]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">bundle</span> - Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">description</span> - Description for port. <span class="li-normal">type: str</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-snoop-option82-trust</span> - Enable/disable allowance of DHCP with option-82 on untrusted interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-snooping</span> - Trusted or untrusted DHCP-snooping interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [trusted, untrusted]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">discard-mode</span> - Configure discard mode for port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, all-untagged, all-tagged]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">edge-port</span> - Enable/disable this interface as an edge port, bridging connections between workstations and/or computers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">igmp-snooping</span> - Set IGMP snooping mode for the physical port interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">igmps-flood-reports</span> - Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">igmps-flood-traffic</span> - Enable/disable flooding of IGMP snooping traffic to this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lacp-speed</span> - end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast). <span class="li-normal">type: str</span> <span class="li-normal">choices: [slow, fast]</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">learning-limit</span> - Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default). <span class="li-normal">type: int</span>
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lldp-profile</span> - LLDP port TLV profile. <span class="li-normal">type: str</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">lldp-status</span> - LLDP transmit and receive status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, rx-only, tx-only, tx-rx]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">loop-guard</span> - Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, enabled]</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">loop-guard-timeout</span> - Loop-guard timeout (0 - 120 min, default = 45). <span class="li-normal">type: int</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">max-bundle</span> - Maximum size of LAG bundle (1 - 24, default = 24) <span class="li-normal">type: int</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mclag</span> - Enable/disable multi-chassis link aggregation (MCLAG). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">member-withdrawal-behavior</span> - Port behavior after it withdraws because of loss of control packets. <span class="li-normal">type: str</span> <span class="li-normal">choices: [forward, block]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">members</span> - No description for the parameter <span class="li-normal">type: list</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">min-bundle</span> - Minimum size of LAG bundle (1 - 24, default = 1) <span class="li-normal">type: int</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mode</span> - LACP mode: ignore and do not send control messages, or negotiate 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, lacp-passive, lacp-active]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-pre-standard-detection</span> - Enable/disable PoE pre-standard detection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-status</span> - Enable/disable PoE status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">port-name</span> - Switch port name. <span class="li-normal">type: str</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">port-owner</span> - Switch port name. <span class="li-normal">type: str</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">port-security-policy</span> - Switch controller authentication policy to apply to this managed switch from available options. <span class="li-normal">type: str</span>
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">port-selection-criteria</span> - Algorithm for aggregate port selection. <span class="li-normal">type: str</span> <span class="li-normal">choices: [src-mac, dst-mac, src-dst-mac, src-ip, dst-ip, src-dst-ip]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">qos-policy</span> - Switch controller QoS policy from available options. <span class="li-normal">type: str</span>
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sample-direction</span> - sFlow sample direction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [rx, tx, both]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sflow-counter-interval</span> - sFlow sampler counter polling interval (1 - 255 sec). <span class="li-normal">type: int</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sflow-sample-rate</span> - sFlow sampler sample rate (0 - 99999 p/sec). <span class="li-normal">type: int</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sflow-sampler</span> - Enable/disable sFlow protocol on this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, enabled]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stp-bpdu-guard</span> - Enable/disable STP BPDU guard on this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, enabled]</span> 
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stp-bpdu-guard-timeout</span> - BPDU Guard disabling protection (0 - 120 min). <span class="li-normal">type: int</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stp-root-guard</span> - Enable/disable STP root guard on this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, enabled]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">stp-state</span> - Enable/disable Spanning Tree Protocol (STP) on this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, enabled]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">type</span> - Interface type: physical or trunk port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [physical, trunk]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">untagged-vlans</span> - Configure switch port untagged vlans <span class="li-normal">type: list or str</span>
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlan</span> - Assign switch ports to a VLAN. <span class="li-normal">type: str</span>
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">export-to-pool-flag</span> - Switch controller export port to pool-list. <span class="li-normal">type: int</span>
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mac-addr</span> - Port/Trunk MAC. <span class="li-normal">type: str</span>
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">packet-sample-rate</span> - Packet sampling rate (0 - 99999 p/sec). <span class="li-normal">type: int</span>
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">packet-sampler</span> - Enable/disable packet sampling on this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, enabled]</span> 
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sticky-mac</span> - Enable or disable sticky-mac on the interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">storm-control-policy</span> - Switch controller storm control policy from available options. <span class="li-normal">type: str</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dot1x-enable</span> - No description for the parameter <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">max-miss-heartbeats</span> - Maximum tolerant missed heartbeats. <span class="li-normal">type: int</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>None</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">access-mode</span> - Access mode of the port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [normal, nac, dynamic, static]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip-source-guard</span> - Enable/disable IP source guard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mclag-icl-port</span> - No description for the parameter <span class="li-normal">type: int</span>
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">p2p-port</span> - No description for the parameter <span class="li-normal">type: int</span>
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">aggregator-mode</span> - LACP member select mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [bandwidth, count]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">rpvst-port</span> - Enable/disable inter-operability with rapid PVST on this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, enabled]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">flow-control</span> - Flow control direction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, tx, rx, both]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">media-type</span> - No description for the parameter <span class="li-normal">type: str</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pause-meter</span> - Configure ingress pause metering rate, in kbps (default = 0, disabled). <span class="li-normal">type: int</span>
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">pause-meter-resume</span> - Resume threshold for resuming traffic on ingress port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [25%, 50%, 75%]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">trunk-member</span> - Trunk member. <span class="li-normal">type: int</span>
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fec-capable</span> - FEC capable. <span class="li-normal">type: int</span>
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fec-state</span> - State of forward error correction. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disabled, cl74, cl91]</span> 
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">matched-dpp-intf-tags</span> - Matched interface tags in the dynamic port policy. <span class="li-normal">type: str</span>
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">matched-dpp-policy</span> - Matched child policy in the dynamic port policy. <span class="li-normal">type: str</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">port-policy</span> - Switch controller dynamic port policy from available options. <span class="li-normal">type: str</span>
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Switch port admin status: up or down. <span class="li-normal">type: str</span> <span class="li-normal">choices: [down, up]</span> 
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>True</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dsl-profile</span> - DSL policy configuration. <span class="li-normal">type: str</span>
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">flap-duration</span> - Period over which flap events are calculated (seconds). <span class="li-normal">type: int</span>
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">flap-rate</span> - Number of stage change events needed within flap-duration. <span class="li-normal">type: int</span>
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">flap-timeout</span> - Flap guard disabling protection (min). <span class="li-normal">type: int</span>
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">flapguard</span> - Enable/disable flap guard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">interface-tags</span> - No description for the parameter <span class="li-normal">type: list or str</span>
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-max-power</span> - No description for the parameter <span class="li-normal">type: str</span>
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-standard</span> - No description for the parameter <span class="li-normal">type: str</span>
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
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
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">igmp-snooping-flood-reports</span> - Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">mcast-snooping-flood-traffic</span> - Enable/disable flooding of IGMP snooping traffic to this interface. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">link-status</span> - No description for the parameter <span class="li-normal">type: str</span> <span class="li-normal">choices: [down, up]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-mode-bt-cabable</span> - PoE mode IEEE 802. <span class="li-normal">type: int</span>
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-port-mode</span> - Configure PoE port mode. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ieee802-3af, ieee802-3at, ieee802-3bt]</span> 
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-port-power</span> - Configure PoE port power. <span class="li-normal">type: str</span> <span class="li-normal">choices: [normal, perpetual, perpetual-fast]</span> 
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">poe-port-priority</span> - Configure PoE port priority. <span class="li-normal">type: str</span> <span class="li-normal">choices: [critical-priority, high-priority, low-priority, medium-priority]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">acl-group</span> - No description for the parameter <span class="li-normal">type: list</span>
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dhcp-snoop-option82-override</span> - No description for the parameter <span class="li-normal">type: list</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">circuit-id</span> - Circuit ID string. <span class="li-normal">type: str</span>
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">remote-id</span> - Remote ID string. <span class="li-normal">type: str</span>
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">vlan-name</span> - DHCP snooping option 82 VLAN. <span class="li-normal">type: str</span>
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">fortiswitch-acls</span> - No description for the parameter <span class="li-normal">type: list</span>
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">isl-peer-device-sn</span> - No description for the parameter <span class="li-normal">type: str</span>
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">authenticated-port</span> - No description for the parameter <span class="li-normal">type: int</span>
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">encrypted-port</span> - No description for the parameter <span class="li-normal">type: int</span>
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ptp-status</span> - Enable/disable PTP policy on this FortiSwitch port. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">restricted-auth-port</span> - No description for the parameter <span class="li-normal">type: int</span>
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <table>
 <tr>
 <td><code class="docutils literal notranslate">6.2.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.2 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.4 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.2.6 </code></td>
 <td><code class="docutils literal notranslate">6.2.7 </code></td>
 <td><code class="docutils literal notranslate">6.2.8 </code></td>
 <td><code class="docutils literal notranslate">6.2.9 </code></td>
 <td><code class="docutils literal notranslate">6.2.10 </code></td>
 <td><code class="docutils literal notranslate">6.2.11 </code></td>
 <td><code class="docutils literal notranslate">6.2.12 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>None</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.3 </code></td>
 <td><code class="docutils literal notranslate">6.4.4 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.6 </code></td>
 <td><code class="docutils literal notranslate">6.4.7 </code></td>
 <td><code class="docutils literal notranslate">6.4.8 </code></td>
 <td><code class="docutils literal notranslate">6.4.9 </code></td>
 <td><code class="docutils literal notranslate">6.4.10 </code></td>
 <td><code class="docutils literal notranslate">6.4.11 </code></td>
 <td><code class="docutils literal notranslate">6.4.12 </code></td>
 <td><code class="docutils literal notranslate">6.4.13 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.1 </code></td>
 <td><code class="docutils literal notranslate">7.0.2 </code></td>
 <td><code class="docutils literal notranslate">7.0.3 </code></td>
 <td><code class="docutils literal notranslate">7.0.4 </code></td>
 <td><code class="docutils literal notranslate">7.0.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.6 </code></td>
 <td><code class="docutils literal notranslate">7.0.7 </code></td>
 <td><code class="docutils literal notranslate">7.0.8 </code></td>
 <td><code class="docutils literal notranslate">7.0.9 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.1 </code></td>
 <td><code class="docutils literal notranslate">7.2.2 </code></td>
 <td><code class="docutils literal notranslate">7.2.3 </code></td>
 <td><code class="docutils literal notranslate">7.2.4 </code></td>
 </tr>
 <tr>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 <tr>
 <td><code class="docutils literal notranslate">7.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.4.1 </code></td>
 </tr>
 <tr>
 <td>False</td>
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
      - name: Managed-switch port list.
        fmgr_switchcontroller_managedswitch_ports:
          bypass_validation: False
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          rc_succeeded: [0, -2, -3, ...]
          rc_failed: [-2, -3, ...]
          adom: <your own value>
          managed-switch: <your own value>
          state: <value in [present, absent]>
          switchcontroller_managedswitch_ports:
            allowed-vlans: <list or string>
            allowed-vlans-all: <value in [disable, enable]>
            arp-inspection-trust: <value in [untrusted, trusted]>
            bundle: <value in [disable, enable]>
            description: <string>
            dhcp-snoop-option82-trust: <value in [disable, enable]>
            dhcp-snooping: <value in [trusted, untrusted]>
            discard-mode: <value in [none, all-untagged, all-tagged]>
            edge-port: <value in [disable, enable]>
            igmp-snooping: <value in [disable, enable]>
            igmps-flood-reports: <value in [disable, enable]>
            igmps-flood-traffic: <value in [disable, enable]>
            lacp-speed: <value in [slow, fast]>
            learning-limit: <integer>
            lldp-profile: <string>
            lldp-status: <value in [disable, rx-only, tx-only, ...]>
            loop-guard: <value in [disabled, enabled]>
            loop-guard-timeout: <integer>
            max-bundle: <integer>
            mclag: <value in [disable, enable]>
            member-withdrawal-behavior: <value in [forward, block]>
            members: <list or string>
            min-bundle: <integer>
            mode: <value in [static, lacp-passive, lacp-active]>
            poe-pre-standard-detection: <value in [disable, enable]>
            poe-status: <value in [disable, enable]>
            port-name: <string>
            port-owner: <string>
            port-security-policy: <string>
            port-selection-criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
            qos-policy: <string>
            sample-direction: <value in [rx, tx, both]>
            sflow-counter-interval: <integer>
            sflow-sample-rate: <integer>
            sflow-sampler: <value in [disabled, enabled]>
            stp-bpdu-guard: <value in [disabled, enabled]>
            stp-bpdu-guard-timeout: <integer>
            stp-root-guard: <value in [disabled, enabled]>
            stp-state: <value in [disabled, enabled]>
            type: <value in [physical, trunk]>
            untagged-vlans: <list or string>
            vlan: <string>
            export-to-pool-flag: <integer>
            mac-addr: <string>
            packet-sample-rate: <integer>
            packet-sampler: <value in [disabled, enabled]>
            sticky-mac: <value in [disable, enable]>
            storm-control-policy: <string>
            dot1x-enable: <value in [disable, enable]>
            max-miss-heartbeats: <integer>
            access-mode: <value in [normal, nac, dynamic, ...]>
            ip-source-guard: <value in [disable, enable]>
            mclag-icl-port: <integer>
            p2p-port: <integer>
            aggregator-mode: <value in [bandwidth, count]>
            rpvst-port: <value in [disabled, enabled]>
            flow-control: <value in [disable, tx, rx, ...]>
            media-type: <string>
            pause-meter: <integer>
            pause-meter-resume: <value in [25%, 50%, 75%]>
            trunk-member: <integer>
            fec-capable: <integer>
            fec-state: <value in [disabled, cl74, cl91]>
            matched-dpp-intf-tags: <string>
            matched-dpp-policy: <string>
            port-policy: <string>
            status: <value in [down, up]>
            dsl-profile: <string>
            flap-duration: <integer>
            flap-rate: <integer>
            flap-timeout: <integer>
            flapguard: <value in [disable, enable]>
            interface-tags: <list or string>
            poe-max-power: <string>
            poe-standard: <string>
            igmp-snooping-flood-reports: <value in [disable, enable]>
            mcast-snooping-flood-traffic: <value in [disable, enable]>
            link-status: <value in [down, up]>
            poe-mode-bt-cabable: <integer>
            poe-port-mode: <value in [ieee802-3af, ieee802-3at, ieee802-3bt]>
            poe-port-power: <value in [normal, perpetual, perpetual-fast]>
            poe-port-priority: <value in [critical-priority, high-priority, low-priority, ...]>
            acl-group: <list or string>
            dhcp-snoop-option82-override:
              -
                circuit-id: <string>
                remote-id: <string>
                vlan-name: <string>
            fortiswitch-acls: <list or integer>
            isl-peer-device-sn: <string>
            authenticated-port: <integer>
            encrypted-port: <integer>
            ptp-status: <value in [disable, enable]>
            restricted-auth-port: <integer>
  


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
 <li> <span class="li-return">rc</span> - The status the request. <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">0</li>
 <li> <span class="li-return">version_check_warning</span> - Warning if the parameters used in the playbook are not supported by the current FortiManager version. <span class="li-normal">returned: if at least on parameter mpt supported by the current FortiManager version</span> <span class="li-normal">type: list</span> <span class="li-normal">0</li>
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


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



