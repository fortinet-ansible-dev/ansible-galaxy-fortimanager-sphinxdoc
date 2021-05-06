:source: fmgr_dvmdb_adom.py

:orphan:

.. _fmgr_dvmdb_adom:

fmgr_dvmdb_adom -- ADOM table, most attributes are read-only and can only be changed internally.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">dvmdb_adom</span> - ADOM table, most attributes are read-only and can only be changed internally. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">desc</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [migration, db_export, no_vpn_console, backup, other_devices, central_sdwan, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg]</span> </li>
 <li><span class="li-head">log_db_retention_hours</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 1440</span> </li>
 <li><span class="li-head">log_disk_quota</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log_disk_quota_alert_thres</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 90</span> </li>
 <li><span class="li-head">log_disk_quota_split_ratio</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 70</span> </li>
 <li><span class="li-head">log_file_retention_hours</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 8760</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: dict</span> </li>
 <li><span class="li-head">mig_mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 2</span> </li>
 <li><span class="li-head">mig_os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]</span>  <span class="li-normal">default: 6.0</span> </li>
 <li><span class="li-head">mode</span> - ems - (Value no longer used as of 4. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ems, gms, provider]</span>  <span class="li-normal">default: gms</span> </li>
 <li><span class="li-head">mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 2</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]</span>  <span class="li-normal">default: 6.0</span> </li>
 <li><span class="li-head">restricted_prds</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx]</span> </li>
 <li><span class="li-head">state</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: ADOM table, most attributes are read-only and can only be changed internally.
      fmgr_dvmdb_adom:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         state: <value in [present, absent]>
         dvmdb_adom:
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
            state: <value of integer>
            uuid: <value of string>



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



