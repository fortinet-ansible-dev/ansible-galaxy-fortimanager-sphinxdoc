:source: fmgr_extensioncontroller_extenderprofile_cellular_smsnotification_receiver.py

:orphan:

.. _fmgr_extensioncontroller_extenderprofile_cellular_smsnotification_receiver:

fmgr_extensioncontroller_extenderprofile_cellular_smsnotification_receiver -- SMS notification receiver list.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.2.0

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
 <li><span class="li-head">extender-profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">extensioncontroller_extenderprofile_cellular_smsnotification_receiver</span> - SMS notification receiver list. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">alert</span> - No description for the parameter <span class="li-normal">type: list</span> <span class="li-normal">choices: [system-reboot, data-exhausted, session-disconnect, low-signal-strength, mode-switch, os-image-fallback, fgt-backup-mode-switch]</span> 
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
 <li><span class="li-head">name</span> - FortiExtender SMS notification receiver name. <span class="li-normal">type: str</span>
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
 <li><span class="li-head">phone-number</span> - Receiver phone number. <span class="li-normal">type: str</span>
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
 <li><span class="li-head">status</span> - SMS notification receiver status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
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
      - name: SMS notification receiver list.
        fmgr_extensioncontroller_extenderprofile_cellular_smsnotification_receiver:
          bypass_validation: False
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          rc_succeeded: [0, -2, -3, ...]
          rc_failed: [-2, -3, ...]
          adom: <your own value>
          extender-profile: <your own value>
          state: <value in [present, absent]>
          extensioncontroller_extenderprofile_cellular_smsnotification_receiver:
            alert:
              - system-reboot
              - data-exhausted
              - session-disconnect
              - low-signal-strength
              - mode-switch
              - os-image-fallback
              - fgt-backup-mode-switch
            name: <string>
            phone-number: <string>
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



