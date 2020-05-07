:source: fmgr_devprof_system_ntp.py

:orphan:

.. _fmgr_devprof_system_ntp:

fmgr_devprof_system_ntp -- Configure system NTP information.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/system/ntp`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure system NTP information.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure system NTP information.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ntpserver</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">authentication</span> - Enable/disable MD5 authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - NTP server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">key-id</span> - Key ID for authentication. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ntpv3</span> - Enable to use NTPv3 instead of NTPv4. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">server</span> - IP address or hostname of the NTP Server. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ntpsync</span> - Enable/disable setting the FortiGate system time by synchronizing with an NTP Server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">source-ip6</span> - Source IPv6 address for communication to the NTP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">syncinterval</span> - NTP synchronization interval (1 - 1440 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">type</span> - Use the FortiGuard NTP server or any other available NTP Server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortiguard, custom]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/NTP
      fmgr_devprof_system_ntp:
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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/NTP
      fmgr_devprof_system_ntp:
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
                  ntpserver:
                    -
                        authentication: <value in [disable, enable]>
                        id: <value of integer>
                        key:
                          - <value of string>
                        key-id: <value of integer>
                        ntpv3: <value in [disable, enable]>
                        server: <value of string>
                  ntpsync: <value in [disable, enable]>
                  source-ip6: <value of string>
                  syncinterval: <value of integer>
                  type: <value in [fortiguard, custom]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> ntpserver </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> authentication </span> - Enable/disable MD5 authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - NTP server ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> key-id </span> - Key ID for authentication. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ntpv3 </span> - Enable to use NTPv3 instead of NTPv4. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server </span> - IP address or hostname of the NTP Server. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ntpsync </span> - Enable/disable setting the FortiGate system time by synchronizing with an NTP Server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip6 </span> - Source IPv6 address for communication to the NTP server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> syncinterval </span> - NTP synchronization interval (1 - 1440 min). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> type </span> - Use the FortiGuard NTP server or any other available NTP Server. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/ntp</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/ntp</span>  </li>
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



