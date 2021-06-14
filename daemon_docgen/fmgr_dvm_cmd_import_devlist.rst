:source: fmgr_dvm_cmd_import_devlist.py

:orphan:

.. _fmgr_dvm_cmd_import_devlist:

fmgr_dvm_cmd_import_devlist -- Import a list of ADOMs and devices.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>dvm_cmd_import_devlist</td>
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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">dvm_cmd_import_devlist</span> - Import a list of ADOMs and devices. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - Name or ID of the ADOM where the command is to be executed on. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, create_task, nonblocking, log_dev]</span> </li>
 <li><span class="li-head">import-adom-members</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - Target ADOM to associate device VDOM with. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dev</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">import-adoms</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">desc</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [migration, db_export, no_vpn_console, backup, other_devices, central_sdwan, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg, migration, db_export, no_vpn_console, backup, other_devices, central_sdwan, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg, per_device_fsw, migration, db_export, no_vpn_console, backup, other_devices, central_sdwan, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg, per_device_fsw, migration, db_export, no_vpn_console, backup, other_devices, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg, per_device_fsw, migration, db_export, no_vpn_console, backup, other_devices, central_sdwan, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg, per_device_fsw, migration, db_export, no_vpn_console, backup, other_devices, central_sdwan, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg, per_device_fsw, migration, db_export, no_vpn_console, backup, other_devices, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg, per_device_fsw]</span> </li>
 <li><span class="li-head">log_db_retention_hours</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 1440</span> </li>
 <li><span class="li-head">log_disk_quota</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log_disk_quota_alert_thres</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 90</span> </li>
 <li><span class="li-head">log_disk_quota_split_ratio</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 70</span> </li>
 <li><span class="li-head">log_file_retention_hours</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 8760</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: dict</span> </li>
 <li><span class="li-head">mig_mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 2</span> </li>
 <li><span class="li-head">mig_os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]</span>  <span class="li-normal">default: 6.0</span> </li>
 <li><span class="li-head">mode</span> - ems - (Value no longer used as of 4. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ems, gms, provider]</span>  <span class="li-normal">default: gms</span> </li>
 <li><span class="li-head">mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 2</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]</span>  <span class="li-normal">default: 6.0</span> </li>
 <li><span class="li-head">restricted_prds</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx, fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx, fna, fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx, fna, fdc, fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx, fna, ffw, fsr, fad, fdc, fap, fxt, fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx, fna, fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx, fna, fdc, fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx, fna, ffw, fsr, fad, fdc, fap, fxt]</span> </li>
 <li><span class="li-head">state</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">create_time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">workspace_mode</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">import-devices</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adm_pass</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">adm_usr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">app_ver</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av_ver</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">beta</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">branch_pt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">build</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">checksum</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">conf_status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, insync, outofsync]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">conn_mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, passive]</span>  <span class="li-normal">default: passive</span> </li>
 <li><span class="li-head">conn_status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [UNKNOWN, up, down]</span>  <span class="li-normal">default: UNKNOWN</span> </li>
 <li><span class="li-head">db_status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, nomod, mod]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">desc</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dev_status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, unknown, checkedin, inprogress, installed, aborted, sched, retry, canceled, pending, retrieved, changed_conf, sync_fail, timeout, rev_revert, auto_updated]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">fap_cnt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">faz.full_act</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">faz.perm</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">faz.quota</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">faz.used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fex_cnt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [has_hdd, vdom_enabled, discover, reload, interim_build, offline_mode, is_model, fips_mode, linked_to_model, ip-conflict, faz-autosync]</span> </li>
 <li><span class="li-head">foslic_cpu</span> - VM Meter vCPU count. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_dr_site</span> - VM Meter DR Site status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">foslic_inst_time</span> - VM Meter first deployment time (in UNIX timestamp). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_last_sync</span> - VM Meter last synchronized time (in UNIX timestamp). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_ram</span> - VM Meter device RAM size (in MB). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_type</span> - VM Meter license type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [temporary, trial, regular, trial_expired]</span>  <span class="li-normal">default: temporary</span> </li>
 <li><span class="li-head">foslic_utm</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [fw, av, ips, app, url, utm, fwb]</span> </li>
 <li><span class="li-head">fsw_cnt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ha_group_id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ha_group_name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ha_mode</span> - enabled - Value reserved for non-FOS HA devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [standalone, AP, AA, ELBC, DUAL, enabled, unknown, fmg-enabled, autoscale]</span>  <span class="li-normal">default: standalone</span> </li>
 <li><span class="li-head">ha_slave</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">idx</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">prio</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">role</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slave, master]</span>  <span class="li-normal">default: slave</span> </li>
 <li><span class="li-head">sn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">hdisk_size</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">hostname</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hw_rev_major</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">hw_rev_minor</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips_ext</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ips_ver</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">last_checked</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">last_resync</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latitude</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">lic_flags</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lic_region</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">location_from</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logdisk_size</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">longitude</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">maxvdom</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: dict</span> </li>
 <li><span class="li-head">mgmt_id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mgmt_if</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mgmt_mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unreg, fmg, faz, fmgfaz]</span>  <span class="li-normal">default: unreg</span> </li>
 <li><span class="li-head">mgt_vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: -1</span> </li>
 <li><span class="li-head">name</span> - Unique name for the device. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, fos, fsw, foc, fml, faz, fwb, fch, fct, log, fmg, fsa, fdd, fac, fpx, fna, fdc, ffw, fsr, fad, fap, fxt]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">patch</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">platform_str</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">psk</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sn</span> - Unique value for each device. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">opmode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [nat, transparent]</span>  <span class="li-normal">default: nat</span> </li>
 <li><span class="li-head">rtm_prof_id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: dict</span> </li>
 <li><span class="li-head">vpn_id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">version</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_cpu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_cpu_limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_lic_expire</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_mem</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_mem_limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">module_sn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">prefer_img_ver</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hyperscale</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nsxt_service_name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">prio</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">private_key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">private_key_status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">role</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [master, ha-slave, autoscale-slave]</span>  <span class="li-normal">default: master</span> </li>
 </ul>
 <li><span class="li-head">import-group-members</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - ADOM where the device group is located. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dev</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">grp</span> - Target device group to associate device VDOM with. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: Import a list of ADOMs and devices.
      fmgr_dvm_cmd_import_devlist:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         dvm_cmd_import_devlist:
            adom: <value of string>
            flags:
              - none
              - create_task
              - nonblocking
              - log_dev
            import-adom-members:
              -
                  adom: <value of string>
                  dev: <value of string>
                  vdom: <value of string>
            import-adoms:
              -
                  desc: <value of string>
                  flags:
                    - migration
                    - db_export
                    - no_vpn_console
                    - backup
                    - other_devices
                    - central_sdwan
                    - is_autosync
                    - per_device_wtp
                    - policy_check_on_install
                    - install_on_policy_check_fail
                    - auto_push_cfg
                    - migration
                    - db_export
                    - no_vpn_console
                    - backup
                    - other_devices
                    - central_sdwan
                    - is_autosync
                    - per_device_wtp
                    - policy_check_on_install
                    - install_on_policy_check_fail
                    - auto_push_cfg
                    - per_device_fsw
                    - migration
                    - db_export
                    - no_vpn_console
                    - backup
                    - other_devices
                    - central_sdwan
                    - is_autosync
                    - per_device_wtp
                    - policy_check_on_install
                    - install_on_policy_check_fail
                    - auto_push_cfg
                    - per_device_fsw
                    - migration
                    - db_export
                    - no_vpn_console
                    - backup
                    - other_devices
                    - is_autosync
                    - per_device_wtp
                    - policy_check_on_install
                    - install_on_policy_check_fail
                    - auto_push_cfg
                    - per_device_fsw
                    - migration
                    - db_export
                    - no_vpn_console
                    - backup
                    - other_devices
                    - central_sdwan
                    - is_autosync
                    - per_device_wtp
                    - policy_check_on_install
                    - install_on_policy_check_fail
                    - auto_push_cfg
                    - per_device_fsw
                    - migration
                    - db_export
                    - no_vpn_console
                    - backup
                    - other_devices
                    - central_sdwan
                    - is_autosync
                    - per_device_wtp
                    - policy_check_on_install
                    - install_on_policy_check_fail
                    - auto_push_cfg
                    - per_device_fsw
                    - migration
                    - db_export
                    - no_vpn_console
                    - backup
                    - other_devices
                    - is_autosync
                    - per_device_wtp
                    - policy_check_on_install
                    - install_on_policy_check_fail
                    - auto_push_cfg
                    - per_device_fsw
                  log_db_retention_hours: <value of integer>
                  log_disk_quota: <value of integer>
                  log_disk_quota_alert_thres: <value of integer>
                  log_disk_quota_split_ratio: <value of integer>
                  log_file_retention_hours: <value of integer>
                  meta fields: <value of dict>
                  mig_mr: <value of integer>
                  mig_os_ver: <value in [unknown, 0.0, 1.0, ...]>
                  mode: <value in [ems, gms, provider]>
                  mr: <value of integer>
                  name: <value of string>
                  os_ver: <value in [unknown, 0.0, 1.0, ...]>
                  restricted_prds:
                    - fos
                    - foc
                    - fml
                    - fch
                    - fwb
                    - log
                    - fct
                    - faz
                    - fsa
                    - fsw
                    - fmg
                    - fdd
                    - fac
                    - fpx
                    - fos
                    - foc
                    - fml
                    - fch
                    - fwb
                    - log
                    - fct
                    - faz
                    - fsa
                    - fsw
                    - fmg
                    - fdd
                    - fac
                    - fpx
                    - fna
                    - fos
                    - foc
                    - fml
                    - fch
                    - fwb
                    - log
                    - fct
                    - faz
                    - fsa
                    - fsw
                    - fmg
                    - fdd
                    - fac
                    - fpx
                    - fna
                    - fdc
                    - fos
                    - foc
                    - fml
                    - fch
                    - fwb
                    - log
                    - fct
                    - faz
                    - fsa
                    - fsw
                    - fmg
                    - fdd
                    - fac
                    - fpx
                    - fna
                    - ffw
                    - fsr
                    - fad
                    - fdc
                    - fap
                    - fxt
                    - fos
                    - foc
                    - fml
                    - fch
                    - fwb
                    - log
                    - fct
                    - faz
                    - fsa
                    - fsw
                    - fmg
                    - fdd
                    - fac
                    - fpx
                    - fna
                    - fos
                    - foc
                    - fml
                    - fch
                    - fwb
                    - log
                    - fct
                    - faz
                    - fsa
                    - fsw
                    - fmg
                    - fdd
                    - fac
                    - fpx
                    - fna
                    - fdc
                    - fos
                    - foc
                    - fml
                    - fch
                    - fwb
                    - log
                    - fct
                    - faz
                    - fsa
                    - fsw
                    - fmg
                    - fdd
                    - fac
                    - fpx
                    - fna
                    - ffw
                    - fsr
                    - fad
                    - fdc
                    - fap
                    - fxt
                  state: <value of integer>
                  uuid: <value of string>
                  create_time: <value of integer>
                  workspace_mode: <value of integer>
            import-devices:
              -
                  adm_pass: <value of string>
                  adm_usr: <value of string>
                  app_ver: <value of string>
                  av_ver: <value of string>
                  beta: <value of integer>
                  branch_pt: <value of integer>
                  build: <value of integer>
                  checksum: <value of string>
                  conf_status: <value in [unknown, insync, outofsync]>
                  conn_mode: <value in [active, passive]>
                  conn_status: <value in [UNKNOWN, up, down]>
                  db_status: <value in [unknown, nomod, mod]>
                  desc: <value of string>
                  dev_status: <value in [none, unknown, checkedin, ...]>
                  fap_cnt: <value of integer>
                  faz.full_act: <value of integer>
                  faz.perm: <value of integer>
                  faz.quota: <value of integer>
                  faz.used: <value of integer>
                  fex_cnt: <value of integer>
                  flags:
                    - has_hdd
                    - vdom_enabled
                    - discover
                    - reload
                    - interim_build
                    - offline_mode
                    - is_model
                    - fips_mode
                    - linked_to_model
                    - ip-conflict
                    - faz-autosync
                  foslic_cpu: <value of integer>
                  foslic_dr_site: <value in [disable, enable]>
                  foslic_inst_time: <value of integer>
                  foslic_last_sync: <value of integer>
                  foslic_ram: <value of integer>
                  foslic_type: <value in [temporary, trial, regular, ...]>
                  foslic_utm:
                    - fw
                    - av
                    - ips
                    - app
                    - url
                    - utm
                    - fwb
                  fsw_cnt: <value of integer>
                  ha_group_id: <value of integer>
                  ha_group_name: <value of string>
                  ha_mode: <value in [standalone, AP, AA, ...]>
                  ha_slave:
                    -
                        idx: <value of integer>
                        name: <value of string>
                        prio: <value of integer>
                        role: <value in [slave, master]>
                        sn: <value of string>
                        status: <value of integer>
                  hdisk_size: <value of integer>
                  hostname: <value of string>
                  hw_rev_major: <value of integer>
                  hw_rev_minor: <value of integer>
                  ip: <value of string>
                  ips_ext: <value of integer>
                  ips_ver: <value of string>
                  last_checked: <value of integer>
                  last_resync: <value of integer>
                  latitude: <value of string>
                  lic_flags: <value of integer>
                  lic_region: <value of string>
                  location_from: <value of string>
                  logdisk_size: <value of integer>
                  longitude: <value of string>
                  maxvdom: <value of integer>
                  meta fields: <value of dict>
                  mgmt_id: <value of integer>
                  mgmt_if: <value of string>
                  mgmt_mode: <value in [unreg, fmg, faz, ...]>
                  mgt_vdom: <value of string>
                  mr: <value of integer>
                  name: <value of string>
                  os_type: <value in [unknown, fos, fsw, ...]>
                  os_ver: <value in [unknown, 0.0, 1.0, ...]>
                  patch: <value of integer>
                  platform_str: <value of string>
                  psk: <value of string>
                  sn: <value of string>
                  vdom:
                    -
                        comments: <value of string>
                        name: <value of string>
                        opmode: <value in [nat, transparent]>
                        rtm_prof_id: <value of integer>
                        status: <value of string>
                        meta fields: <value of dict>
                        vpn_id: <value of integer>
                  version: <value of integer>
                  vm_cpu: <value of integer>
                  vm_cpu_limit: <value of integer>
                  vm_lic_expire: <value of integer>
                  vm_mem: <value of integer>
                  vm_mem_limit: <value of integer>
                  vm_status: <value of integer>
                  module_sn: <value of string>
                  prefer_img_ver: <value of string>
                  hyperscale: <value of integer>
                  nsxt_service_name: <value of string>
                  prio: <value of integer>
                  private_key: <value of string>
                  private_key_status: <value of integer>
                  role: <value in [master, ha-slave, autoscale-slave]>
            import-group-members:
              -
                  adom: <value of string>
                  dev: <value of string>
                  grp: <value of string>
                  vdom: <value of string>



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



