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
 <li><span class="li-head">user</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">system_admin_user_dashboard</span> - Custom dashboard widgets. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">column</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">diskio-content-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [util, iops, blks]</span> </li>
 <li><span class="li-head">diskio-period</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span> </li>
 <li><span class="li-head">log-rate-period</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [2min , 1hour, 6hours]</span> </li>
 <li><span class="li-head">log-rate-topn</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 3, 4, 5]</span> </li>
 <li><span class="li-head">log-rate-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, device]</span> </li>
 <li><span class="li-head">moduleid</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">num-entries</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">refresh-interval</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">res-cpu-display</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [average , each]</span> </li>
 <li><span class="li-head">res-period</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [10min , hour, day]</span> </li>
 <li><span class="li-head">res-view-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [real-time , history]</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [close, open]</span> </li>
 <li><span class="li-head">tabid</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">time-period</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span> </li>
 <li><span class="li-head">widget-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [top-lograte, sysres, sysinfo, licinfo, jsconsole, sysop, alert, statistics, rpteng, raid, logrecv, devsummary, logdb-perf, logdb-lag, disk-io, log-rcvd-fwd]</span> </li>
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
    - name: Custom dashboard widgets.
      fmgr_system_admin_user_dashboard:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         user: <your own value>
         state: <value in [present, absent]>
         system_admin_user_dashboard:
            column: <value of integer>
            diskio-content-type: <value in [util, iops, blks]>
            diskio-period: <value in [1hour, 8hour, 24hour]>
            log-rate-period: <value in [2min , 1hour, 6hours]>
            log-rate-topn: <value in [1, 2, 3, ...]>
            log-rate-type: <value in [log, device]>
            moduleid: <value of integer>
            name: <value of string>
            num-entries: <value of integer>
            refresh-interval: <value of integer>
            res-cpu-display: <value in [average , each]>
            res-period: <value in [10min , hour, day]>
            res-view-type: <value in [real-time , history]>
            status: <value in [close, open]>
            tabid: <value of integer>
            time-period: <value in [1hour, 8hour, 24hour]>
            widget-type: <value in [top-lograte, sysres, sysinfo, ...]>



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



