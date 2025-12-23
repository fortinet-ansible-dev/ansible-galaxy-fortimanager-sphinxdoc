:source: fmgr_wtpprofile_radio4.py

:orphan:

.. _fmgr_wtpprofile_radio4:

fmgr_wtpprofile_radio4 -- Configuration options for radio 4.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
- Tested with FortiManager v7.x.


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.15.0


FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>



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
 <li><span class="li-head">wtp_profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wtpprofile_radio4</span> - Configuration options for radio 4. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">airtime_fairness</span> <b>(Alias name: airtime-fairness)</b>  Enable/disable airtime fairness (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">amsdu</span> Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_handoff</span> <b>(Alias name: ap-handoff)</b>  Enable/disable ap handoff of clients to other aps (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.1 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_addr</span> <b>(Alias name: ap-sniffer-addr)</b>  Mac address to monitor. <span class="li-normal">type: str</span>
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_bufsize</span> <b>(Alias name: ap-sniffer-bufsize)</b>  Sniffer buffer size (1 - 32 mb, default = 16). <span class="li-normal">type: int</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_chan</span> <b>(Alias name: ap-sniffer-chan)</b>  Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span>
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_ctl</span> <b>(Alias name: ap-sniffer-ctl)</b>  Enable/disable sniffer on wifi control frame (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_data</span> <b>(Alias name: ap-sniffer-data)</b>  Enable/disable sniffer on wifi data frame (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_mgmt_beacon</span> <b>(Alias name: ap-sniffer-mgmt-beacon)</b>  Enable/disable sniffer on wifi management beacon frames (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_mgmt_other</span> <b>(Alias name: ap-sniffer-mgmt-other)</b>  Enable/disable sniffer on wifi management other frames  (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_mgmt_probe</span> <b>(Alias name: ap-sniffer-mgmt-probe)</b>  Enable/disable sniffer on wifi management probe frames (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_power_high</span> <b>(Alias name: auto-power-high)</b>  The upper bound of automatic transmit power adjustment in dbm (the actual range of transmit power depends on the ap platform type). <span class="li-normal">type: int</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_power_level</span> <b>(Alias name: auto-power-level)</b>  Enable/disable automatic power-level adjustment to prevent co-channel interference (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_power_low</span> <b>(Alias name: auto-power-low)</b>  The lower bound of automatic transmit power adjustment in dbm (the actual range of transmit power depends on the ap platform type). <span class="li-normal">type: int</span>
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">band</span> Wifi band that radio 3 operates on. <span class="li-normal">type: str</span> <span class="li-normal">choices: [802.11b, 802.11a, 802.11g, 802.11n, 802.11ac, 802.11n-5G, 802.11ax-5G, 802.11ax, 802.11g-only, 802.11n-only, 802.11n,g-only, 802.11ac-only, 802.11ac,n-only, 802.11n-5G-only, 802.11ax-5G-only, 802.11ax,ac-only, 802.11ax,ac,n-only, 802.11ax-only, 802.11ax,n-only, 802.11ax,n,g-only, 802.11ac-2G, 802.11ax-6G, 802.11n-2G, 802.11ac-5G, 802.11ax-2G, 802.11be-2G, 802.11be-5G, 802.11be-6G]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">band_5g_type</span> <b>(Alias name: band-5g-type)</b>  Wifi 5g band type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [5g-full, 5g-high, 5g-low]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bandwidth_admission_control</span> <b>(Alias name: bandwidth-admission-control)</b>  Enable/disable wifi multimedia (wmm) bandwidth admission control to optimize wifi bandwidth use. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bandwidth_capacity</span> <b>(Alias name: bandwidth-capacity)</b>  Maximum bandwidth capacity allowed (1 - 600000 kbps, default = 2000). <span class="li-normal">type: int</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">beacon_interval</span> <b>(Alias name: beacon-interval)</b>  Beacon interval. <span class="li-normal">type: int</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">call_admission_control</span> <b>(Alias name: call-admission-control)</b>  Enable/disable wifi multimedia (wmm) call admission control to optimize wifi bandwidth use for voip calls. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">call_capacity</span> <b>(Alias name: call-capacity)</b>  Maximum number of voice over wlan (vowlan) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">channel</span> Selected list of wireless radio channels. <span class="li-normal">type: list</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">channel_bonding</span> <b>(Alias name: channel-bonding)</b>  Channel bandwidth: 160,80, 40, or 20mhz. <span class="li-normal">type: str</span> <span class="li-normal">choices: [80MHz, 40MHz, 20MHz, 160MHz, 320MHz, 240MHz]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">channel_utilization</span> <b>(Alias name: channel-utilization)</b>  Enable/disable measuring channel utilization. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">coexistence</span> Enable/disable allowing both ht20 and ht40 on the same radio (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">darrp</span> Enable/disable distributed automatic radio resource provisioning (darrp) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">dtim</span> Delivery traffic indication map (dtim) period (1 - 255, default = 1). <span class="li-normal">type: int</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">frag_threshold</span> <b>(Alias name: frag-threshold)</b>  Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">frequency_handoff</span> <b>(Alias name: frequency-handoff)</b>  Enable/disable frequency handoff of clients to other channels (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.1 -> v7.6.2</code></p>
 </div>
 </li>
 <li><span class="li-head">max_clients</span> <b>(Alias name: max-clients)</b>  Maximum number of stations (stas) or wifi clients supported by the radio. <span class="li-normal">type: int</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_distance</span> <b>(Alias name: max-distance)</b>  Maximum expected distance between the ap and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span>
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mode</span> Mode of radio 3. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ap, monitor, sniffer, disabled, sam]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">power_level</span> <b>(Alias name: power-level)</b>  Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100). <span class="li-normal">type: int</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">powersave_optimize</span> <b>(Alias name: powersave-optimize)</b>  Enable client power-saving features such as tim, ac vo, and obss etc. <span class="li-normal">type: list</span> <span class="li-normal">choices: [tim, ac-vo, no-obss-scan, no-11b-rate, client-rate-follow]</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">protection_mode</span> <b>(Alias name: protection-mode)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [rtscts, ctsonly, disable]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">radio_id</span> <b>(Alias name: radio-id)</b>  Radio id. <span class="li-normal">type: int</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rts_threshold</span> <b>(Alias name: rts-threshold)</b>  Maximum packet size for rts transmissions, specifying the maximum size of a data packet before rts/cts (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">short_guard_interval</span> <b>(Alias name: short-guard-interval)</b>  Use either the short guard interval (short gi) of 400 ns or the long guard interval (long gi) of 800 ns. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">spectrum_analysis</span> <b>(Alias name: spectrum-analysis)</b>  Enable/disable spectrum analysis to find interference that would negatively impact wireless performance. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, scan-only]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">transmit_optimize</span> <b>(Alias name: transmit-optimize)</b>  Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. <span class="li-normal">type: list</span> <span class="li-normal">choices: [disable, power-save, aggr-limit, retry-limit, send-bar]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap_all</span> <b>(Alias name: vap-all)</b>  Enable/disable the automatic inheritance of all virtual access points (vaps) (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable, tunnel, bridge, manual]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vaps</span> Manually selected list of virtual access points (vaps). <span class="li-normal">type: list or str</span>
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">wids_profile</span> <b>(Alias name: wids-profile)</b>  Wireless intrusion detection system (wids) profile name to assign to the radio. <span class="li-normal">type: str</span>
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">zero_wait_dfs</span> <b>(Alias name: zero-wait-dfs)</b>  Enable/disable zero wait dfs on radio (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap1</span> Virtual access point (vap) for wlan id 1 <span class="li-normal">type: str</span>
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap2</span> Virtual access point (vap) for wlan id 2 <span class="li-normal">type: str</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap3</span> Virtual access point (vap) for wlan id 3 <span class="li-normal">type: str</span>
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap4</span> Virtual access point (vap) for wlan id 4 <span class="li-normal">type: str</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap5</span> Virtual access point (vap) for wlan id 5 <span class="li-normal">type: str</span>
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap6</span> Virtual access point (vap) for wlan id 6 <span class="li-normal">type: str</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap7</span> Virtual access point (vap) for wlan id 7 <span class="li-normal">type: str</span>
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vap8</span> Virtual access point (vap) for wlan id 8 <span class="li-normal">type: str</span>
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bss_color</span> <b>(Alias name: bss-color)</b>  Bss color value for this 11ax radio (0 - 63, 0 means disable. <span class="li-normal">type: int</span>
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_power_target</span> <b>(Alias name: auto-power-target)</b>  The target of automatic transmit power adjustment in dbm. <span class="li-normal">type: str</span>
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">drma</span> Enable/disable dynamic radio mode assignment (drma) (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">drma_sensitivity</span> <b>(Alias name: drma-sensitivity)</b>  Network coverage factor (ncf) percentage required to consider a radio as redundant (default = low). <span class="li-normal">type: str</span> <span class="li-normal">choices: [low, medium, high]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">iperf_protocol</span> <b>(Alias name: iperf-protocol)</b>  Iperf test protocol (default = udp). <span class="li-normal">type: str</span> <span class="li-normal">choices: [udp, tcp]</span> 
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">iperf_server_port</span> <b>(Alias name: iperf-server-port)</b>  Iperf service port number. <span class="li-normal">type: int</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">power_mode</span> <b>(Alias name: power-mode)</b>  Set radio effective isotropic radiated power (eirp) in dbm or by a percentage of the maximum eirp (default = percentage). <span class="li-normal">type: str</span> <span class="li-normal">choices: [dBm, percentage]</span> 
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">power_value</span> <b>(Alias name: power-value)</b>  Radio eirp power in dbm (1 - 33, default = 27). <span class="li-normal">type: int</span>
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_bssid</span> <b>(Alias name: sam-bssid)</b>  Bssid for wifi network. <span class="li-normal">type: str</span>
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_captive_portal</span> <b>(Alias name: sam-captive-portal)</b>  Enable/disable captive portal authentication (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_password</span> <b>(Alias name: sam-password)</b>  Passphrase for wifi network connection. <span class="li-normal">type: list</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_report_intv</span> <b>(Alias name: sam-report-intv)</b>  Sam report interval (sec), 0 for a one-time report. <span class="li-normal">type: int</span>
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_security_type</span> <b>(Alias name: sam-security-type)</b>  Select wifi network security type (default = wpa-personal). <span class="li-normal">type: str</span> <span class="li-normal">choices: [open, wpa-personal, wpa-enterprise, owe, wpa3-sae]</span> 
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_server</span> <b>(Alias name: sam-server)</b>  Sam test server ip address or domain name. <span class="li-normal">type: str</span>
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_ssid</span> <b>(Alias name: sam-ssid)</b>  Ssid for wifi network. <span class="li-normal">type: str</span>
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_test</span> <b>(Alias name: sam-test)</b>  Select sam test type (default = ping). <span class="li-normal">type: str</span> <span class="li-normal">choices: [ping, iperf]</span> 
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_username</span> <b>(Alias name: sam-username)</b>  Username for wifi network connection. <span class="li-normal">type: str</span>
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">arrp_profile</span> <b>(Alias name: arrp-profile)</b>  Distributed automatic radio resource provisioning (darrp) profile name to assign to the radio. <span class="li-normal">type: str</span>
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">bss_color_mode</span> <b>(Alias name: bss-color-mode)</b>  Bss color mode for this 11ax radio (default = auto). <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, static]</span> 
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_cwp_failure_string</span> <b>(Alias name: sam-cwp-failure-string)</b>  Failure identification on the page after an incorrect login. <span class="li-normal">type: str</span>
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_cwp_match_string</span> <b>(Alias name: sam-cwp-match-string)</b>  Identification string from the captive portal login form. <span class="li-normal">type: str</span>
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_cwp_password</span> <b>(Alias name: sam-cwp-password)</b>  Password for captive portal authentication. <span class="li-normal">type: list</span>
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_cwp_success_string</span> <b>(Alias name: sam-cwp-success-string)</b>  Success identification on the page after a successful login. <span class="li-normal">type: str</span>
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_cwp_test_url</span> <b>(Alias name: sam-cwp-test-url)</b>  Website the client is trying to access. <span class="li-normal">type: str</span>
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_cwp_username</span> <b>(Alias name: sam-cwp-username)</b>  Username for captive portal authentication. <span class="li-normal">type: str</span>
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_server_fqdn</span> <b>(Alias name: sam-server-fqdn)</b>  Sam test server domain name. <span class="li-normal">type: str</span>
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_server_ip</span> <b>(Alias name: sam-server-ip)</b>  Sam test server ip address. <span class="li-normal">type: str</span>
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_server_type</span> <b>(Alias name: sam-server-type)</b>  Select sam server type (default = ip). <span class="li-normal">type: str</span> <span class="li-normal">choices: [ip, fqdn]</span> 
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">d80211d</span> <b>(Alias name: 80211d)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">optional_antenna</span> <b>(Alias name: optional-antenna)</b>  Optional antenna used on fap (default = none). <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, FANT-04ABGN-8065-P-N, FANT-04ABGN-0606-O-R, FANT-04ABGN-0606-P-R, FANT-10ACAX-1213-D-N, FANT-08ABGN-1213-D-R, custom, FANT-04BEAX-0606-P-R]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mimo_mode</span> <b>(Alias name: mimo-mode)</b>  Configure radio mimo mode (default = default). <span class="li-normal">type: str</span> <span class="li-normal">choices: [default, 1x1, 2x2, 3x3, 4x4, 8x8]</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">optional_antenna_gain</span> <b>(Alias name: optional-antenna-gain)</b>  Optional antenna gain in dbi (0 to 20, default = 0). <span class="li-normal">type: str</span>
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_ca_certificate</span> <b>(Alias name: sam-ca-certificate)</b>  Ca certificate for wpa2/wpa3-enterprise. <span class="li-normal">type: str</span>
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_client_certificate</span> <b>(Alias name: sam-client-certificate)</b>  Client certificate for wpa2/wpa3-enterprise. <span class="li-normal">type: str</span>
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_eap_method</span> <b>(Alias name: sam-eap-method)</b>  Select wpa2/wpa3-enterprise eap method (default = peap). <span class="li-normal">type: str</span> <span class="li-normal">choices: [tls, peap, both]</span> 
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_private_key</span> <b>(Alias name: sam-private-key)</b>  Private key for wpa2/wpa3-enterprise. <span class="li-normal">type: str</span>
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sam_private_key_password</span> <b>(Alias name: sam-private-key-password)</b>  Password for private key file for wpa2/wpa3-enterprise. <span class="li-normal">type: list</span>
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">channel_bonding_ext</span> <b>(Alias name: channel-bonding-ext)</b>  Channel bandwidth extension: 320 mhz-1 and 320 mhz-2 (default = 320 mhz-2). <span class="li-normal">type: str</span> <span class="li-normal">choices: [320MHz-1, 320MHz-2]</span> 
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">d80211mc</span> <b>(Alias name: 80211mc)</b>  Enable/disable 802. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ap_sniffer_chan_width</span> <b>(Alias name: ap-sniffer-chan-width)</b>  Channel bandwidth for sniffer. <span class="li-normal">type: str</span> <span class="li-normal">choices: [320MHz, 240MHz, 160MHz, 80MHz, 40MHz, 20MHz]</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.4 -> latest</code></p>
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
      - name: Configuration options for radio 4.
        fortinet.fortimanager.fmgr_wtpprofile_radio4:
          # bypass_validation: false
          # workspace_locking_adom: <global or your adom name>
          # workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          wtp_profile: <your own value>
          wtpprofile_radio4:
            # airtime_fairness: <value in [disable, enable]>
            # amsdu: <value in [disable, enable]>
            # ap_handoff: <value in [disable, enable]>
            # ap_sniffer_addr: <string>
            # ap_sniffer_bufsize: <integer>
            # ap_sniffer_chan: <integer>
            # ap_sniffer_ctl: <value in [disable, enable]>
            # ap_sniffer_data: <value in [disable, enable]>
            # ap_sniffer_mgmt_beacon: <value in [disable, enable]>
            # ap_sniffer_mgmt_other: <value in [disable, enable]>
            # ap_sniffer_mgmt_probe: <value in [disable, enable]>
            # auto_power_high: <integer>
            # auto_power_level: <value in [disable, enable]>
            # auto_power_low: <integer>
            # band: <value in [802.11b, 802.11a, 802.11g, ...]>
            # band_5g_type: <value in [5g-full, 5g-high, 5g-low]>
            # bandwidth_admission_control: <value in [disable, enable]>
            # bandwidth_capacity: <integer>
            # beacon_interval: <integer>
            # call_admission_control: <value in [disable, enable]>
            # call_capacity: <integer>
            # channel: <list or string>
            # channel_bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
            # channel_utilization: <value in [disable, enable]>
            # coexistence: <value in [disable, enable]>
            # darrp: <value in [disable, enable]>
            # dtim: <integer>
            # frag_threshold: <integer>
            # frequency_handoff: <value in [disable, enable]>
            # max_clients: <integer>
            # max_distance: <integer>
            # mode: <value in [ap, monitor, sniffer, ...]>
            # power_level: <integer>
            # powersave_optimize:
            #   - "tim"
            #   - "ac-vo"
            #   - "no-obss-scan"
            #   - "no-11b-rate"
            #   - "client-rate-follow"
            # protection_mode: <value in [rtscts, ctsonly, disable]>
            # radio_id: <integer>
            # rts_threshold: <integer>
            # short_guard_interval: <value in [disable, enable]>
            # spectrum_analysis: <value in [disable, enable, scan-only]>
            # transmit_optimize:
            #   - "disable"
            #   - "power-save"
            #   - "aggr-limit"
            #   - "retry-limit"
            #   - "send-bar"
            # vap_all: <value in [disable, enable, tunnel, ...]>
            # vaps: <list or string>
            # wids_profile: <string>
            # zero_wait_dfs: <value in [disable, enable]>
            # vap1: <string>
            # vap2: <string>
            # vap3: <string>
            # vap4: <string>
            # vap5: <string>
            # vap6: <string>
            # vap7: <string>
            # vap8: <string>
            # bss_color: <integer>
            # auto_power_target: <string>
            # drma: <value in [disable, enable]>
            # drma_sensitivity: <value in [low, medium, high]>
            # iperf_protocol: <value in [udp, tcp]>
            # iperf_server_port: <integer>
            # power_mode: <value in [dBm, percentage]>
            # power_value: <integer>
            # sam_bssid: <string>
            # sam_captive_portal: <value in [disable, enable]>
            # sam_password: <list or string>
            # sam_report_intv: <integer>
            # sam_security_type: <value in [open, wpa-personal, wpa-enterprise, ...]>
            # sam_server: <string>
            # sam_ssid: <string>
            # sam_test: <value in [ping, iperf]>
            # sam_username: <string>
            # arrp_profile: <string>
            # bss_color_mode: <value in [auto, static]>
            # sam_cwp_failure_string: <string>
            # sam_cwp_match_string: <string>
            # sam_cwp_password: <list or string>
            # sam_cwp_success_string: <string>
            # sam_cwp_test_url: <string>
            # sam_cwp_username: <string>
            # sam_server_fqdn: <string>
            # sam_server_ip: <string>
            # sam_server_type: <value in [ip, fqdn]>
            # d80211d: <value in [disable, enable]>
            # optional_antenna: <value in [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, ...]>
            # mimo_mode: <value in [default, 1x1, 2x2, ...]>
            # optional_antenna_gain: <string>
            # sam_ca_certificate: <string>
            # sam_client_certificate: <string>
            # sam_eap_method: <value in [tls, peap, both]>
            # sam_private_key: <string>
            # sam_private_key_password: <list or string>
            # channel_bonding_ext: <value in [320MHz-1, 320MHz-2]>
            # d80211mc: <value in [disable, enable]>
            # ap_sniffer_chan_width: <value in [320MHz, 240MHz, 160MHz, ...]>


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
