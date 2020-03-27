:source: fmgr_dvmdb_device.py

:orphan:

.. _fmgr_dvmdb_device:

fmgr_dvmdb_device -- Device table, most attributes are read-only and can only be changed internally.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/dvmdb/adom/{adom}/device`
- `/dvmdb/device`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Device table, most attributes are read-only and can only be changed internally. Refer to Device Manager Command module for API to add, delete, and manage devices.</li>
 <ul class="ul-self">
 <li><span class="li-head">expand member</span> - Fetch all or selected attributes of object members. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [adm_pass, adm_usr, app_ver, av_ver, beta, branch_pt, build, checksum, conf_status, conn_mode, conn_status, db_status, desc, dev_status, fap_cnt, faz.full_act, faz.perm, faz.quota, faz.used, fex_cnt, flags, foslic_cpu, foslic_dr_site, foslic_inst_time, foslic_last_sync, foslic_ram, foslic_type, foslic_utm, fsw_cnt, ha_group_id, ha_group_name, ha_mode, hdisk_size, hostname, hw_rev_major, hw_rev_minor, ip, ips_ext, ips_ver, last_checked, last_resync, latitude, lic_flags, lic_region, location_from, logdisk_size, longitude, maxvdom, mgmt_id, mgmt_if, mgmt_mode, mgt_vdom, mr, name, os_type, os_ver, patch, platform_str, psk, sn, version, vm_cpu, vm_cpu_limit, vm_lic_expire, vm_mem, vm_mem_limit, vm_status]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Device table, most attributes are read-only and can only be changed internally. Refer to Device Manager Command module for API to add, delete, and manage devices.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adm_pass</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
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
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [has_hdd, vdom_enabled, discover, reload, interim_build, offline_mode, is_model, fips_mode, linked_to_model, ip-conflict, faz-autosync]</span> </li>
 </ul>
 <li><span class="li-head">foslic_cpu</span> - VM Meter vCPU count. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_dr_site</span> - VM Meter DR Site status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">foslic_inst_time</span> - VM Meter first deployment time (in UNIX timestamp). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_last_sync</span> - VM Meter last synchronized time (in UNIX timestamp). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_ram</span> - VM Meter device RAM size (in MB). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">foslic_type</span> - VM Meter license type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [temporary, trial, regular, trial_expired]</span>  <span class="li-normal">default: temporary</span> </li>
 <li><span class="li-head">foslic_utm</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fw, av, ips, app, url, utm, fwb]</span> </li>
 </ul>
 <li><span class="li-head">fsw_cnt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ha_group_id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ha_group_name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ha_mode</span> - enabled - Value reserved for non-FOS HA devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [standalone, AP, AA, ELBC, DUAL, enabled, unknown]</span>  <span class="li-normal">default: standalone</span> </li>
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
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mgmt_id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mgmt_if</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mgmt_mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unreg, fmg, faz, fmgfaz]</span>  <span class="li-normal">default: unreg</span> </li>
 <li><span class="li-head">mgt_vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: -1</span> </li>
 <li><span class="li-head">name</span> - Unique name for the device. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, fos, fsw, foc, fml, faz, fwb, fch, fct, log, fmg, fsa, fdd, fac, fpx]</span>  <span class="li-normal">default: unknown</span> </li>
 <li><span class="li-head">os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]</span>  <span class="li-normal">default: unknown</span> </li>
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
 </ul>
 <li><span class="li-head">version</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_cpu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_cpu_limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_lic_expire</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_mem</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_mem_limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vm_status</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

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

    - name: REQUESTING /DVMDB/DEVICE
      fmgr_dvmdb_device:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               expand member: <value of string>
               fields:
                 -
                    - <value in [adm_pass, adm_usr, app_ver, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               meta fields:
                 - <value of string>
               option: <value in [count, object member, syntax]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>

    - name: REQUESTING /DVMDB/DEVICE
      fmgr_dvmdb_device:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     adm_pass:
                       - <value of string>
                     adm_usr: <value of string>
                     app_ver: <value of string>
                     av_ver: <value of string>
                     beta: <value of integer>
                     branch_pt: <value of integer>
                     build: <value of integer>
                     checksum: <value of string>
                     conf_status: <value in [unknown, insync, outofsync] default: 'unknown'>
                     conn_mode: <value in [active, passive] default: 'passive'>
                     conn_status: <value in [UNKNOWN, up, down] default: 'UNKNOWN'>
                     db_status: <value in [unknown, nomod, mod] default: 'unknown'>
                     desc: <value of string>
                     dev_status: <value in [none, unknown, checkedin, ...] default: 'unknown'>
                     fap_cnt: <value of integer>
                     faz.full_act: <value of integer>
                     faz.perm: <value of integer>
                     faz.quota: <value of integer>
                     faz.used: <value of integer>
                     fex_cnt: <value of integer>
                     flags:
                       - <value in [has_hdd, vdom_enabled, discover, ...]>
                     foslic_cpu: <value of integer>
                     foslic_dr_site: <value in [disable, enable] default: 'disable'>
                     foslic_inst_time: <value of integer>
                     foslic_last_sync: <value of integer>
                     foslic_ram: <value of integer>
                     foslic_type: <value in [temporary, trial, regular, ...] default: 'temporary'>
                     foslic_utm:
                       - <value in [fw, av, ips, ...]>
                     fsw_cnt: <value of integer>
                     ha_group_id: <value of integer>
                     ha_group_name: <value of string>
                     ha_mode: <value in [standalone, AP, AA, ...] default: 'standalone'>
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
                     maxvdom: <value of integer default: 10>
                     meta fields: <value of string>
                     mgmt_id: <value of integer>
                     mgmt_if: <value of string>
                     mgmt_mode: <value in [unreg, fmg, faz, ...] default: 'unreg'>
                     mgt_vdom: <value of string>
                     mr: <value of integer default: -1>
                     name: <value of string>
                     os_type: <value in [unknown, fos, fsw, ...] default: 'unknown'>
                     os_ver: <value in [unknown, 0.0, 1.0, ...] default: 'unknown'>
                     patch: <value of integer>
                     platform_str: <value of string>
                     psk: <value of string>
                     sn: <value of string>
                     vdom:
                       -
                           comments: <value of string>
                           name: <value of string>
                           opmode: <value in [nat, transparent] default: 'nat'>
                           rtm_prof_id: <value of integer>
                           status: <value of string>
                     version: <value of integer>
                     vm_cpu: <value of integer>
                     vm_cpu_limit: <value of integer>
                     vm_lic_expire: <value of integer>
                     vm_mem: <value of integer>
                     vm_mem_limit: <value of integer>
                     vm_status: <value of integer>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> adm_pass </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> adm_usr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> app_ver </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av_ver </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> beta </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> branch_pt </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> build </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> checksum </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> conf_status </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> conn_mode </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: passive</span>  </li>
 <li> <span class="li-return"> conn_status </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: UNKNOWN</span>  </li>
 <li> <span class="li-return"> db_status </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> desc </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dev_status </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> fap_cnt </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> faz.full_act </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> faz.perm </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> faz.quota </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> faz.used </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fex_cnt </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> flags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> foslic_cpu </span> - VM Meter vCPU count. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> foslic_dr_site </span> - VM Meter DR Site status. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> foslic_inst_time </span> - VM Meter first deployment time (in UNIX timestamp). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> foslic_last_sync </span> - VM Meter last synchronized time (in UNIX timestamp). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> foslic_ram </span> - VM Meter device RAM size (in MB). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> foslic_type </span> - VM Meter license type. <span class="li-normal">type: str</span>  <span class="li-normal">example: temporary</span>  </li>
 <li> <span class="li-return"> foslic_utm </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> fsw_cnt </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ha_group_id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ha_group_name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ha_mode </span> - enabled - Value reserved for non-FOS HA devices. <span class="li-normal">type: str</span>  <span class="li-normal">example: standalone</span>  </li>
 <li> <span class="li-return"> hdisk_size </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> hostname </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hw_rev_major </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> hw_rev_minor </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips_ext </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ips_ver </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> last_checked </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> last_resync </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> latitude </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> lic_flags </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> lic_region </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> location_from </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logdisk_size </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> longitude </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> maxvdom </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 10</span>  </li>
 <li> <span class="li-return"> meta fields </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mgmt_id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mgmt_if </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mgmt_mode </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: unreg</span>  </li>
 <li> <span class="li-return"> mgt_vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mr </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: -1</span>  </li>
 <li> <span class="li-return"> name </span> - Unique name for the device. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> os_type </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> os_ver </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: unknown</span>  </li>
 <li> <span class="li-return"> patch </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> platform_str </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> psk </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sn </span> - Unique value for each device. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> comments </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> opmode </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: nat</span>  </li>
 <li> <span class="li-return"> rtm_prof_id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> version </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vm_cpu </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vm_cpu_limit </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vm_lic_expire </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vm_mem </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vm_mem_limit </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vm_status </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/device</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/device</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



