:source: fmgr_system_admin_profile.py

:orphan:

.. _fmgr_system_admin_profile:

fmgr_system_admin_profile -- Admin profile.
+++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">system_admin_profile</span> - Admin profile. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom-lock</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">adom-policy-packages</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">adom-switch</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">app-filter</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">assignment</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">change-password</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">config-retrieve</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">config-revert</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">consistency-check</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">datamask</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">datamask-custom-fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">field-category</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, fortiview, alert, ueba, all]</span> </li>
 </ul>
 <li><span class="li-head">field-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">field-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">field-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [string, ip, mac, email, unknown]</span> </li>
 </ul>
 <li><span class="li-head">datamask-custom-priority</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">datamask-fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [user, srcip, srcname, srcmac, dstip, dstname, email, message, domain]</span> </li>
 </ul>
 <li><span class="li-head">datamask-key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">deploy-management</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-ap</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-config</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-forticlient</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-fortiswitch</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-manager</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-op</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-policy-package-lock</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-revision-deletion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">device-wan-link-load-balance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">event-management</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">fgd-center-advanced</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">fgd-center-fmw-mgmt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">fgd-center-licensing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">fgd_center</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">global-policy-packages</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">import-policy-packages</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">intf-mapping</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">ips-filter</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-viewer</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">policy-objects</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">profileid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">read-passwd</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">realtime-monitor</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">report-viewer</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">scope</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, adom]</span> </li>
 <li><span class="li-head">set-install-targets</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">system-setting</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">term-access</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [system, restricted]</span> </li>
 <li><span class="li-head">vpn-manager</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span> </li>
 <li><span class="li-head">web-filter</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Admin profile.
      fmgr_system_admin_profile:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         state: <value in [present, absent]>
         system_admin_profile:
            adom-lock: <value in [none, read, read-write]>
            adom-policy-packages: <value in [none, read, read-write]>
            adom-switch: <value in [none, read, read-write]>
            app-filter: <value in [disable, enable]>
            assignment: <value in [none, read, read-write]>
            change-password: <value in [disable, enable]>
            config-retrieve: <value in [none, read, read-write]>
            config-revert: <value in [none, read, read-write]>
            consistency-check: <value in [none, read, read-write]>
            datamask: <value in [disable, enable]>
            datamask-custom-fields:
              -
                  field-category:
                    - <value in [log, fortiview, alert, ...]>
                  field-name: <value of string>
                  field-status: <value in [disable, enable]>
                  field-type: <value in [string, ip, mac, ...]>
            datamask-custom-priority: <value in [disable, enable]>
            datamask-fields:
              - <value in [user, srcip, srcname, ...]>
            datamask-key:
              - <value of string>
            deploy-management: <value in [none, read, read-write]>
            description: <value of string>
            device-ap: <value in [none, read, read-write]>
            device-config: <value in [none, read, read-write]>
            device-forticlient: <value in [none, read, read-write]>
            device-fortiswitch: <value in [none, read, read-write]>
            device-manager: <value in [none, read, read-write]>
            device-op: <value in [none, read, read-write]>
            device-policy-package-lock: <value in [none, read, read-write]>
            device-profile: <value in [none, read, read-write]>
            device-revision-deletion: <value in [none, read, read-write]>
            device-wan-link-load-balance: <value in [none, read, read-write]>
            event-management: <value in [none, read, read-write]>
            fgd-center-advanced: <value in [none, read, read-write]>
            fgd-center-fmw-mgmt: <value in [none, read, read-write]>
            fgd-center-licensing: <value in [none, read, read-write]>
            fgd_center: <value in [none, read, read-write]>
            global-policy-packages: <value in [none, read, read-write]>
            import-policy-packages: <value in [none, read, read-write]>
            intf-mapping: <value in [none, read, read-write]>
            ips-filter: <value in [disable, enable]>
            log-viewer: <value in [none, read, read-write]>
            policy-objects: <value in [none, read, read-write]>
            profileid: <value of string>
            read-passwd: <value in [none, read, read-write]>
            realtime-monitor: <value in [none, read, read-write]>
            report-viewer: <value in [none, read, read-write]>
            scope: <value in [global, adom]>
            set-install-targets: <value in [none, read, read-write]>
            system-setting: <value in [none, read, read-write]>
            term-access: <value in [none, read, read-write]>
            type: <value in [system, restricted]>
            vpn-manager: <value in [none, read, read-write]>
            web-filter: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
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



