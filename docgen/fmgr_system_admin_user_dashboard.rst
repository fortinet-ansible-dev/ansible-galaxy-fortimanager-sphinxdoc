:source: fmgr_system_admin_user_dashboard.py

:orphan:

.. _fmgr_system_admin_user_dashboard:

fmgr_system_admin_user_dashboard -- Custom dashboard widgets.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>system_admin_user_dashboard</td>
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
 <li><span class="li-head">user</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">system_admin_user_dashboard</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">column</span> - Widgets column ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span>  <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
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
 <td>column</td>
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
 <li><span class="li-head">diskio-content-type</span> - Disk I/O Monitor widgets chart type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [util, iops, blks]</span>  <span class="li-normal">default: util</span>  <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
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
 <td>diskio-content-type</td>
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
 <li><span class="li-head">diskio-period</span> - Disk I/O Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span>  <span class="li-normal">default: 1hour</span>  <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
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
 <td>diskio-period</td>
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
 <li><span class="li-head">log-rate-period</span> - Log receive monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [2min, 1hour, 6hours]</span>  </li>
 <li><span class="li-head">log-rate-topn</span> - Log receive monitor widgets number of top items to display. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 3, 4, 5]</span>  <span class="li-normal">default: 5</span>  <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
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
 <td>log-rate-topn</td>
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
 <li><span class="li-head">log-rate-type</span> - Log receive monitor widgets statistics breakdown options. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, device]</span>  <span class="li-normal">default: device</span>  <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
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
 <td>log-rate-type</td>
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
 <li><span class="li-head">moduleid</span> - Widget ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span>  <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
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
 <td>moduleid</td>
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
 <li><span class="li-head">name</span> - Widget name. <span class="li-normal">type: str</span>  <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
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
 <li><span class="li-head">num-entries</span> - Number of entries. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span>  <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
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
 <td>num-entries</td>
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
 <li><span class="li-head">refresh-interval</span> - Widgets refresh interval. <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span>  <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
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
 <td>refresh-interval</td>
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
 <li><span class="li-head">res-cpu-display</span> - Widgets CPU display type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [average, each]</span>  <span class="li-normal">default: average</span>  </li>
 <li><span class="li-head">res-period</span> - Widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [10min, hour, day]</span>  </li>
 <li><span class="li-head">res-view-type</span> - Widgets data view type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [real-time, history]</span>  </li>
 <li><span class="li-head">status</span> - Widgets opened/closed state. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [close, open]</span>  <span class="li-normal">default: open</span>  <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
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
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tabid</span> - ID of tab where widget is displayed. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span>  <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tabid</td>
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
 <li><span class="li-head">time-period</span> - Log Database Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span>  <span class="li-normal">default: 1hour</span>  <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>time-period</td>
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
 <li><span class="li-head">widget-type</span> - Widget type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [top-lograte, sysres, sysinfo, licinfo, jsconsole, sysop, alert, statistics, rpteng, raid, logrecv, devsummary, logdb-perf, logdb-lag, disk-io, log-rcvd-fwd]</span>  <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>widget-type</td>
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

 - hosts: fortimanager00
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Custom dashboard widgets.
      fmgr_system_admin_user_dashboard:
         bypass_validation: False
         user: ansible-test
         state: present
         system_admin_user_dashboard:
            column: 1
            diskio-content-type: util #<value in [util, iops, blks]>
            diskio-period: 1hour #<value in [1hour, 8hour, 24hour]>
            log-rate-period: 1hour #<value in [2min , 1hour, 6hours]>
            log-rate-topn: 5 #<value in [1, 2, 3, ...]>
            log-rate-type: device #<value in [log, device]>
            moduleid: 10
            name: ansible-test-dashboard
            num-entries: 10
            refresh-interval: 0
            res-cpu-display: 'each' #<value in [average , each]>
            res-period: 10min #<value in [10min , hour, day]>
            res-view-type: history #<value in [real-time , history]>
            status: open #<value in [close, open]>
            tabid: 1
            time-period: 1hour #<value in [1hour, 8hour, 24hour]>
            widget-type: sysres #<value in [top-lograte, sysres, sysinfo, ...]>
 - name: gathering fortimanager facts
   hosts: fortimanager00
   gather_facts: no
   connection: httpapi
   collections:
     - fortinet.fortimanager
   vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
   tasks:
    - name: retrieve all the dashboard widgets
      fmgr_fact:
        facts:
            selector: 'system_admin_user_dashboard'
            params:
                user: 'ansible-test'
                dashboard: 'your_value'


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



