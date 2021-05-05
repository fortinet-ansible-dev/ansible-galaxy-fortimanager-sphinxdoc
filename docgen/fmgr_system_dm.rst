:source: fmgr_system_dm.py

:orphan:

.. _fmgr_system_dm:

fmgr_system_dm -- Configure dm.
+++++++++++++++++++++++++++++++

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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">system_dm</span> - Configure dm. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">concurrent-install-image-limit</span> - Maximum number of concurrent install image (1 - 1000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">concurrent-install-limit</span> - Maximum number of concurrent installs (5 - 2000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 480</span> </li>
 <li><span class="li-head">concurrent-install-script-limit</span> - Maximum number of concurrent install scripts (5 - 2000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 480</span> </li>
 <li><span class="li-head">discover-timeout</span> - Check connection timeout when discover device (3 - 15). <span class="li-normal">type: int</span>  <span class="li-normal">default: 6</span> </li>
 <li><span class="li-head">dpm-logsize</span> - Maximum dpm log size per device (1 - 10000K). <span class="li-normal">type: int</span>  <span class="li-normal">default: 10000</span> </li>
 <li><span class="li-head">fgfm-sock-timeout</span> - Maximum FGFM socket idle time (90 - 1800 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 360</span> </li>
 <li><span class="li-head">fgfm_keepalive_itvl</span> - FGFM protocol keep alive interval (30 - 600 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 120</span> </li>
 <li><span class="li-head">force-remote-diff</span> - Always use remote diff when installing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">fortiap-refresh-cnt</span> - Max auto refresh FortiAP number each time (1 - 10000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">fortiap-refresh-itvl</span> - Auto refresh FortiAP status interval (0 - 1440) minutes, set to 0 will disable auto refresh. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">fortiext-refresh-cnt</span> - Max device number for FortiExtender auto refresh (1 - 10000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 50</span> </li>
 <li><span class="li-head">install-image-timeout</span> - Maximum waiting time for image transfer and device upgrade (600 - 7200 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 3600</span> </li>
 <li><span class="li-head">install-tunnel-retry-itvl</span> - Time to re-establish tunnel during install (10 - 60 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">max-revs</span> - Maximum number of revisions saved (1 - 250). <span class="li-normal">type: int</span>  <span class="li-normal">default: 100</span> </li>
 <li><span class="li-head">nr-retry</span> - Number of retries. <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">retry</span> - Enable/disable configuration install retry. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">retry-intvl</span> - Retry interval. <span class="li-normal">type: int</span>  <span class="li-normal">default: 15</span> </li>
 <li><span class="li-head">rollback-allow-reboot</span> - Enable/disable FortiGate reboot to rollback when installing script/config. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">script-logsize</span> - Maximum script log size per device (1 - 10000K). <span class="li-normal">type: int</span>  <span class="li-normal">default: 100</span> </li>
 <li><span class="li-head">skip-scep-check</span> - Enable/disable installing scep related objects even if scep url is configured. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">skip-tunnel-fcp-req</span> - Enable/disable skip the fcp request sent from fgfm tunnel <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">verify-install</span> - Verify install against remote configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, optimal, enable]</span>  <span class="li-normal">default: enable</span> </li>
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
    - name: Configure dm.
      fmgr_system_dm:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_dm:
            concurrent-install-image-limit: <value of integer>
            concurrent-install-limit: <value of integer>
            concurrent-install-script-limit: <value of integer>
            discover-timeout: <value of integer>
            dpm-logsize: <value of integer>
            fgfm-sock-timeout: <value of integer>
            fgfm_keepalive_itvl: <value of integer>
            force-remote-diff: <value in [disable, enable]>
            fortiap-refresh-cnt: <value of integer>
            fortiap-refresh-itvl: <value of integer>
            fortiext-refresh-cnt: <value of integer>
            install-image-timeout: <value of integer>
            install-tunnel-retry-itvl: <value of integer>
            max-revs: <value of integer>
            nr-retry: <value of integer>
            retry: <value in [disable, enable]>
            retry-intvl: <value of integer>
            rollback-allow-reboot: <value in [disable, enable]>
            script-logsize: <value of integer>
            skip-scep-check: <value in [disable, enable]>
            skip-tunnel-fcp-req: <value in [disable, enable]>
            verify-install: <value in [disable, optimal, enable]>



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



