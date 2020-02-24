:source: fmgr_dvm_cmd_add_device.py

:orphan:

.. _fmgr_dvm_cmd_add_device:

fmgr_dvm_cmd_add_device -- Add a device to the Device Manager database.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[exec]** the following FortiManager json-rpc urls.
- `/dvm/cmd/add/device`
- `/dvm/cmd/add/device`
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
 <li><span class="li-head">parameters for method: [exec]</span> - Add a device to the Device Manager database.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - Name or ID of the ADOM where the command is to be executed on. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device</span> <li><span class="li-head">adm_pass</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">adm_usr</span> - <i>add real and promote device</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">desc</span> - <i>available for all operations</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device action</span> - Specify add device operations, or leave blank to add real device: <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">faz.quota</span> - <i>available for all operations</i>. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - <i>add real device only</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">meta fields</span> - <i>add real and model device</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mgmt_mode</span> - <i>add real and model device</i>. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unreg, fmg, faz, fmgfaz]</span> </li>
 <li><span class="li-head">mr</span> - <i>add model device only</i>. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - <i>required for all operations</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_type</span> - <i>add model device only</i>. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, fos, fsw, foc, fml, faz, fwb, fch, fct, log, fmg, fsa, fdd, fac]</span> </li>
 <li><span class="li-head">os_ver</span> - <i>add model device only</i>. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0]</span> </li>
 <li><span class="li-head">patch</span> - <i>add model device only</i>. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">platform_str</span> - <i>add model device only</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sn</span> - <i>add model device only</i>. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, create_task, nonblocking, log_dev]</span> </li>
 </ul>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /DVM/CMD/ADD/DEVICE
      fmgr_dvm_cmd_add_device:
         method: <value in [exec]>
         params:
            -
               data:
                  adom: <value of string>
                  device:
                     adm_pass:
                       - <value of string>
                     adm_usr: <value of string>
                     desc: <value of string>
                     device action: <value of string>
                     faz.quota: <value of integer>
                     ip: <value of string>
                     meta fields: <value of string>
                     mgmt_mode: <value in [unreg, fmg, faz, ...]>
                     mr: <value of integer>
                     name: <value of string>
                     os_type: <value in [unknown, fos, fsw, ...]>
                     os_ver: <value in [unknown, 0.0, 1.0, ...]>
                     patch: <value of integer>
                     platform_str: <value of string>
                     sn: <value of string>
                  flags:
                    - <value in [none, create_task, nonblocking, ...]>
                  groups:
                    -
                        name: <value of string>
                        vdom: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [exec]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> device </span> <li> <span class="li-return"> adm_pass </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li> <span class="li-return"> ha_slave </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> idx </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> prio </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> role </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: slave</span>  </li>
 <li> <span class="li-return"> sn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
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
 <li> <span class="li-return"> pid </span> - When "nonblocking" flag is set, return the process ID for the command. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> taskid </span> - When "create_task" flag is set, return the ID of the task associated with the command. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvm/cmd/add/device</span>  </li>
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



