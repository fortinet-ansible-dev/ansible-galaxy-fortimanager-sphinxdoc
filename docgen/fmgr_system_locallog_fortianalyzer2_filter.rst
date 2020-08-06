:source: fmgr_system_locallog_fortianalyzer2_filter.py

:orphan:

.. _fmgr_system_locallog_fortianalyzer2_filter:

fmgr_system_locallog_fortianalyzer2_filter -- Filter for FortiAnalyzer2 logging.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">system_locallog_fortianalyzer2_filter</span> - Filter for FortiAnalyzer2 logging. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">devcfg</span> - Log device configuration message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">devops</span> - Managered devices operations messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diskquota</span> - Log Fortianalyzer disk quota messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dm</span> - Log deployment manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dvm</span> - Log device manager messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ediscovery</span> - Log Fortianalyzer ediscovery messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">epmgr</span> - Log endpoint manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">event</span> - Log event messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eventmgmt</span> - Log Fortianalyzer event handler messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">faz</span> - Log Fortianalyzer messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fazha</span> - Log Fortianalyzer HA messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fazsys</span> - Log Fortianalyzer system messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fgd</span> - Log FortiGuard service message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fgfm</span> - Log FGFM protocol message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fips</span> - Whether to log fips messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fmgws</span> - Log web service messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fmlmgr</span> - Log FortiMail manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fmwmgr</span> - Log firmware manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortiview</span> - Log Fortianalyzer FortiView messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">glbcfg</span> - Log global database message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ha</span> - Log HA message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hcache</span> - Log Fortianalyzer hcache messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">iolog</span> - Log debug IO log message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">logd</span> - Log the status of log daemon. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">logdb</span> - Log Fortianalyzer log DB messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">logdev</span> - Log Fortianalyzer log device messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">logfile</span> - Log Fortianalyzer log file messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable]</span> </li>
 <li><span class="li-head">logging</span> - Log Fortianalyzer logging messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lrmgr</span> - Log log and report manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">objcfg</span> - Log object configuration change message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">report</span> - Log Fortianalyzer report messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rev</span> - Log revision history message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rtmon</span> - Log real-time monitor message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scfw</span> - Log firewall objects message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scply</span> - Log policy console message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scrmgr</span> - Log script manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scvpn</span> - Log VPN console message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">system</span> - Log system manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webport</span> - Log web portal message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Filter for FortiAnalyzer2 logging.
      fmgr_system_locallog_fortianalyzer2_filter:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_locallog_fortianalyzer2_filter:
            devcfg: <value in [disable, enable]>
            devops: <value in [disable, enable]>
            diskquota: <value in [disable, enable]>
            dm: <value in [disable, enable]>
            dvm: <value in [disable, enable]>
            ediscovery: <value in [disable, enable]>
            epmgr: <value in [disable, enable]>
            event: <value in [disable, enable]>
            eventmgmt: <value in [disable, enable]>
            faz: <value in [disable, enable]>
            fazha: <value in [disable, enable]>
            fazsys: <value in [disable, enable]>
            fgd: <value in [disable, enable]>
            fgfm: <value in [disable, enable]>
            fips: <value in [disable, enable]>
            fmgws: <value in [disable, enable]>
            fmlmgr: <value in [disable, enable]>
            fmwmgr: <value in [disable, enable]>
            fortiview: <value in [disable, enable]>
            glbcfg: <value in [disable, enable]>
            ha: <value in [disable, enable]>
            hcache: <value in [disable, enable]>
            iolog: <value in [disable, enable]>
            logd: <value in [disable, enable]>
            logdb: <value in [disable, enable]>
            logdev: <value in [disable, enable]>
            logfile: <value in [enable, disable]>
            logging: <value in [disable, enable]>
            lrmgr: <value in [disable, enable]>
            objcfg: <value in [disable, enable]>
            report: <value in [disable, enable]>
            rev: <value in [disable, enable]>
            rtmon: <value in [disable, enable]>
            scfw: <value in [disable, enable]>
            scply: <value in [disable, enable]>
            scrmgr: <value in [disable, enable]>
            scvpn: <value in [disable, enable]>
            system: <value in [disable, enable]>
            webport: <value in [disable, enable]>



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



