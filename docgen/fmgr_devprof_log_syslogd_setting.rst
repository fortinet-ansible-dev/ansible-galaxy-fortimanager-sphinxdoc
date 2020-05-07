:source: fmgr_devprof_log_syslogd_setting.py

:orphan:

.. _fmgr_devprof_log_syslogd_setting:

fmgr_devprof_log_syslogd_setting -- Global settings for remote syslog server.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/log/syslogd/setting`
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
 <li><span class="li-head">loose_validation</span> - Do parameter validation in a loose way <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal">default: false</span>  </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">devprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Global settings for remote syslog server.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Global settings for remote syslog server.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">certificate</span> - Certificate used to communicate with Syslog server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">enc-algorithm</span> - Enable/disable reliable syslogging with TLS encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, disable, high-medium]</span> </li>
 <li><span class="li-head">facility</span> - Remote syslog facility. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [kernel, user, mail, daemon, auth, syslog, lpr, news, uucp, cron, authpriv, ftp, ntp, audit, alert, clock, local0, local1, local2, local3, local4, local5, local6, local7]</span> </li>
 <li><span class="li-head">mode</span> - Remote syslog logging over UDP/Reliable TCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [udp, legacy-reliable, reliable]</span> </li>
 <li><span class="li-head">port</span> - Server listen port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server</span> - Address of remote syslog server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1-1, TLSv1-2, SSLv3, TLSv1]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable remote syslog logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

   - To run in workspace mode, the paremeter workspace_locking_adom must be included in the task

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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/LOG/SYSLOGD/SETTING
      fmgr_devprof_log_syslogd_setting:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/LOG/SYSLOGD/SETTING
      fmgr_devprof_log_syslogd_setting:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               data:
                  certificate: <value of string>
                  enc-algorithm: <value in [high, low, disable, ...]>
                  facility: <value in [kernel, user, mail, ...]>
                  mode: <value in [udp, legacy-reliable, reliable]>
                  port: <value of integer>
                  server: <value of string>
                  ssl-min-proto-version: <value in [default, TLSv1-1, TLSv1-2, ...]>
                  status: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> certificate </span> - Certificate used to communicate with Syslog server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> enc-algorithm </span> - Enable/disable reliable syslogging with TLS encryption. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> facility </span> - Remote syslog facility. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mode </span> - Remote syslog logging over UDP/Reliable TCP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Server listen port. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> server </span> - Address of remote syslog server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-proto-version </span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable remote syslog logging. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/log/syslogd/setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/log/syslogd/setting</span>  </li>
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



