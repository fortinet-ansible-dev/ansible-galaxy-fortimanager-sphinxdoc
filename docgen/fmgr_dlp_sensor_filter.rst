:source: fmgr_dlp_sensor_filter.py

:orphan:

.. _fmgr_dlp_sensor_filter:

fmgr_dlp_sensor_filter -- Set up DLP filters for this sensor.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dlp_sensor_filter</td>
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
 <li><span class="li-head">sensor</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">dlp_sensor_filter</span> - Set up DLP filters for this sensor. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take with content that this DLP sensor matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log-only, block, exempt, ban, ban-sender, quarantine-ip, quarantine-port, none, allow]</span>  <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>action</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">archive</span> - Enable/disable DLP archiving. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, summary-only]</span>  <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>archive</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">company-identifier</span> - Enter a company identifier watermark to match. <span class="li-normal">type: str</span>  <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>company-identifier</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">expiry</span> - Quarantine duration in days, hours, minutes format (dddhhmm). <span class="li-normal">type: str</span>  <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>expiry</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">file-size</span> - Match files this size or larger (0 - 4294967295 kbytes). <span class="li-normal">type: int</span>  <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>file-size</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">file-type</span> - Select the number of a DLP file pattern table to match. <span class="li-normal">type: str</span>  <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>file-type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">filter-by</span> - Select the type of content to match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [credit-card, ssn, regexp, file-type, file-size, fingerprint, watermark, encrypted]</span>  <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>filter-by</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">fp-sensitivity</span> - Select a DLP file pattern sensitivity to match. <span class="li-normal">type: str</span>  <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>fp-sensitivity</td>
 <td>True</td>
 <td>False</td>
 <td>False</td>
 <td>False</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span>  <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>id</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">match-percentage</span> - Percentage of fingerprints in the fingerprint databases designated with the selected fp-sensitivity to match. <span class="li-normal">type: int</span>  <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>match-percentage</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">name</span> - Filter name. <span class="li-normal">type: str</span>  <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>name</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">proto</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh, imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post, cifs, ssh]</span>  <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>proto</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">regexp</span> - Enter a regular expression to match (max. <span class="li-normal">type: str</span>  <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>regexp</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">severity</span> - Select the severity or threat level that matches this filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [info, low, medium, high, critical]</span>  <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>severity</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">type</span> - Select whether to check the content of messages (an email message) or files (downloaded files or email attachments). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [file, message]</span>  <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>type</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sensitivity</span> - Select a DLP file pattern sensitivity to match. <span class="li-normal">type: str</span>  <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sensitivity</td>
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
    - name: Set up DLP filters for this sensor.
      fmgr_dlp_sensor_filter:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         sensor: <your own value>
         state: <value in [present, absent]>
         dlp_sensor_filter:
            action: <value in [log-only, block, exempt, ...]>
            archive: <value in [disable, enable, summary-only]>
            company-identifier: <value of string>
            expiry: <value of string>
            file-size: <value of integer>
            file-type: <value of string>
            filter-by: <value in [credit-card, ssn, regexp, ...]>
            fp-sensitivity: <value of string>
            id: <value of integer>
            match-percentage: <value of integer>
            name: <value of string>
            proto:
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
              - imap
              - smtp
              - pop3
              - ftp
              - nntp
              - mm1
              - mm3
              - mm4
              - mm7
              - mapi
              - aim
              - icq
              - msn
              - yahoo
              - http-get
              - http-post
              - cifs
              - ssh
            regexp: <value of string>
            severity: <value in [info, low, medium, ...]>
            type: <value in [file, message]>
            sensitivity: <value of string>



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



