:source: fmgr_fmupdate_fwmsetting.py

:orphan:

.. _fmgr_fmupdate_fwmsetting:

fmgr_fmupdate_fwmsetting -- Configure firmware management settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>



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
 <li><span class="li-head">fmupdate_fwmsetting</span> - Configure firmware management settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">fds_image_timeout</span> <b>(Alias name: fds-image-timeout)</b>  Timer for fgt download image from fortiguard (300-3600s default=1800) <span class="li-normal">type: int</span> <span class="li-normal">default: 1800</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_fds_retry</span> <b>(Alias name: max-fds-retry)</b>  The retries when fgt download from fds fail (5-20, default=10) <span class="li-normal">type: int</span> <span class="li-normal">default: 5</span> 
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v6.2.3</code></p>
 </div>
 </li>
 <li><span class="li-head">multiple_steps_interval</span> <b>(Alias name: multiple-steps-interval)</b>  Waiting time between multiple steps upgrade (30-180s, default=60) <span class="li-normal">type: int</span> <span class="li-normal">default: 60</span> 
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">skip_disk_check</span> <b>(Alias name: skip-disk-check)</b>  Skip disk check when upgrade image. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> v6.2.3</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_scan_fgt_disk</span> <b>(Alias name: auto-scan-fgt-disk)</b>  Auto scan fgt disk if needed. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">check_fgt_disk</span> <b>(Alias name: check-fgt-disk)</b>  Check fgt disk before upgrade image. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fds_failover_fmg</span> <b>(Alias name: fds-failover-fmg)</b>  Using fmg local image file is download from fds fails. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">immx_source</span> <b>(Alias name: immx-source)</b>  Configure which of immx file to be used for choosing upgrade pach. <span class="li-normal">type: str</span> <span class="li-normal">choices: [fmg, fgt, cloud]</span>  <span class="li-normal">default: fmg</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log</span> Configure log setting for fwm daemon <span class="li-normal">type: str</span> <span class="li-normal">choices: [fwm, fwm_dm, fwm_dm_json]</span>  <span class="li-normal">default: fwm_dm</span> 
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.8 -> v6.4.15</code>, <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">upgrade_timeout</span> <b>(Alias name: upgrade-timeout)</b>  Upgrade timeout. <span class="li-normal">type: dict</span>
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">check_status_timeout</span> <b>(Alias name: check-status-timeout)</b>  Timeout for checking status after tunnnel is up. <span class="li-normal">type: int</span> <span class="li-normal">default: 600</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ctrl_check_status_timeout</span> <b>(Alias name: ctrl-check-status-timeout)</b>  Timeout for checking fap/fsw/fext status after request upgrade. <span class="li-normal">type: int</span> <span class="li-normal">default: 1200</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ctrl_put_image_by_fds_timeout</span> <b>(Alias name: ctrl-put-image-by-fds-timeout)</b>  Timeout for waiting device get fap/fsw/fext image from fortiguard. <span class="li-normal">type: int</span> <span class="li-normal">default: 900</span> 
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ha_sync_timeout</span> <b>(Alias name: ha-sync-timeout)</b>  Timeout for waiting ha sync. <span class="li-normal">type: int</span> <span class="li-normal">default: 1800</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">license_check_timeout</span> <b>(Alias name: license-check-timeout)</b>  Timeout for waiting fortigate check license. <span class="li-normal">type: int</span> <span class="li-normal">default: 600</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">prepare_image_timeout</span> <b>(Alias name: prepare-image-timeout)</b>  Timeout for preparing image. <span class="li-normal">type: int</span> <span class="li-normal">default: 600</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">put_image_by_fds_timeout</span> <b>(Alias name: put-image-by-fds-timeout)</b>  Timeout for waiting device get image from fortiguard. <span class="li-normal">type: int</span> <span class="li-normal">default: 1800</span> 
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">put_image_timeout</span> <b>(Alias name: put-image-timeout)</b>  Timeout for waiting send image over tunnel. <span class="li-normal">type: int</span> <span class="li-normal">default: 1800</span> 
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">reboot_of_fsck_timeout</span> <b>(Alias name: reboot-of-fsck-timeout)</b>  Timeout for waiting fortigate reboot. <span class="li-normal">type: int</span> <span class="li-normal">default: 1800</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">reboot_of_upgrade_timeout</span> <b>(Alias name: reboot-of-upgrade-timeout)</b>  Timeout for waiting fortigate reboot after image upgrade. <span class="li-normal">type: int</span> <span class="li-normal">default: 1200</span> 
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">retrieve_timeout</span> <b>(Alias name: retrieve-timeout)</b>  Timeout for waiting retrieve. <span class="li-normal">type: int</span> <span class="li-normal">default: 1800</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">rpc_timeout</span> <b>(Alias name: rpc-timeout)</b>  Timeout for waiting fortigate rpc response. <span class="li-normal">type: int</span> <span class="li-normal">default: 180</span> 
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">total_timeout</span> <b>(Alias name: total-timeout)</b>  Timeout for the whole fortigate upgrade(1-86400s, default=3600) <span class="li-normal">type: int</span> <span class="li-normal">default: 3600</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.5 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">health_check_timeout</span> <b>(Alias name: health-check-timeout)</b>  Timeout for waiting retrieve. <span class="li-normal">type: int</span> <span class="li-normal">default: 600</span> 
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">retry_interval</span> <b>(Alias name: retry-interval)</b>  Waiting time for resending request to device(1-360s, default=60) <span class="li-normal">type: int</span> <span class="li-normal">default: 60</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.10 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">retry_max</span> <b>(Alias name: retry-max)</b>  Max retry times(0-100, default=10) <span class="li-normal">type: int</span> <span class="li-normal">default: 10</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.10 -> v7.0.13</code>, <code class="docutils literal notranslate">v7.2.5 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">health_check</span> <b>(Alias name: health-check)</b>  Do health check after upgrade <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_device_history</span> <b>(Alias name: max-device-history)</b>  Max number of device upgrade report(1-10000, default=100) <span class="li-normal">type: int</span> <span class="li-normal">default: 100</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_profile_history</span> <b>(Alias name: max-profile-history)</b>  Max number of profile upgrade report(1-10000, default=100) <span class="li-normal">type: int</span> <span class="li-normal">default: 100</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">retrieve</span> Do retrieve after upgrade <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">revision_diff</span> <b>(Alias name: revision-diff)</b>  Calculate diff script after upgrade <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">send_image_retry</span> <b>(Alias name: send-image-retry)</b>  Retry send image when failed(0-2, default=0(no retry)) <span class="li-normal">type: int</span> <span class="li-normal">default: 0</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.6 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.4 -> v7.4.5</code>, <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
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
    vars:
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_httpapi_port: 443
    tasks:
      - name: Configure firmware management settings.
        fortinet.fortimanager.fmgr_fmupdate_fwmsetting:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          fmupdate_fwmsetting:
            fds_image_timeout: <integer>
            max_fds_retry: <integer>
            multiple_steps_interval: <integer>
            skip_disk_check: <value in [disable, enable]>
            auto_scan_fgt_disk: <value in [disable, enable]>
            check_fgt_disk: <value in [disable, enable]>
            fds_failover_fmg: <value in [disable, enable]>
            immx_source: <value in [fmg, fgt, cloud]>
            log: <value in [fwm, fwm_dm, fwm_dm_json]>
            upgrade_timeout:
              check_status_timeout: <integer>
              ctrl_check_status_timeout: <integer>
              ctrl_put_image_by_fds_timeout: <integer>
              ha_sync_timeout: <integer>
              license_check_timeout: <integer>
              prepare_image_timeout: <integer>
              put_image_by_fds_timeout: <integer>
              put_image_timeout: <integer>
              reboot_of_fsck_timeout: <integer>
              reboot_of_upgrade_timeout: <integer>
              retrieve_timeout: <integer>
              rpc_timeout: <integer>
              total_timeout: <integer>
              health_check_timeout: <integer>
            retry_interval: <integer>
            retry_max: <integer>
            health_check: <value in [disable, enable]>
            max_device_history: <integer>
            max_profile_history: <integer>
            retrieve: <value in [disable, enable]>
            revision_diff: <value in [disable, enable]>
            send_image_retry: <integer>


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
