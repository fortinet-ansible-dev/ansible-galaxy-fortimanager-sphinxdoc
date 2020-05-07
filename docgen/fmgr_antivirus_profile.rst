:source: fmgr_antivirus_profile.py

:orphan:

.. _fmgr_antivirus_profile:

fmgr_antivirus_profile -- Configure AntiVirus profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/antivirus/profile`
- `/pm/config/global/obj/antivirus/profile`
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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure AntiVirus profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">analytics-bl-filetype</span> - Only submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">analytics-db</span> - Enable/disable using the FortiSandbox signature database to supplement the AV signature databases. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">analytics-max-upload</span> - Maximum size of files that can be uploaded to FortiSandbox (1 - 395 MBytes, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">analytics-wl-filetype</span> - Do not submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-block-log</span> - Enable/disable logging for AntiVirus file blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-virus-log</span> - Enable/disable AntiVirus logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging for antivirus. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ftgd-analytics</span> - Settings to control which files are uploaded to FortiSandbox. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, suspicious, everything]</span> </li>
 <li><span class="li-head">inspection-mode</span> - Inspection mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow-based]</span> </li>
 <li><span class="li-head">mobile-malware-db</span> - Enable/disable using the mobile malware signature database. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group customized for this profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">scan-mode</span> - Choose between full scan mode and quick scan mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [quick, full]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure AntiVirus profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [analytics-bl-filetype, analytics-db, analytics-max-upload, analytics-wl-filetype, av-block-log, av-virus-log, comment, extended-log, ftgd-analytics, inspection-mode, mobile-malware-db, name, replacemsg-group, scan-mode]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">get used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, datasrc, get reserved, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/ANTIVIRUS/PROFILE
      fmgr_antivirus_profile:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     analytics-bl-filetype: <value of string>
                     analytics-db: <value in [disable, enable]>
                     analytics-max-upload: <value of integer>
                     analytics-wl-filetype: <value of string>
                     av-block-log: <value in [disable, enable]>
                     av-virus-log: <value in [disable, enable]>
                     comment: <value of string>
                     extended-log: <value in [disable, enable]>
                     ftgd-analytics: <value in [disable, suspicious, everything]>
                     inspection-mode: <value in [proxy, flow-based]>
                     mobile-malware-db: <value in [disable, enable]>
                     name: <value of string>
                     replacemsg-group: <value of string>
                     scan-mode: <value in [quick, full]>

    - name: REQUESTING /PM/CONFIG/OBJ/ANTIVIRUS/PROFILE
      fmgr_antivirus_profile:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [analytics-bl-filetype, analytics-db, analytics-max-upload, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/antivirus/profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> analytics-bl-filetype </span> - Only submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> analytics-db </span> - Enable/disable using the FortiSandbox signature database to supplement the AV signature databases. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> analytics-max-upload </span> - Maximum size of files that can be uploaded to FortiSandbox (1 - 395 MBytes, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> analytics-wl-filetype </span> - Do not submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-block-log </span> - Enable/disable logging for AntiVirus file blocking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-virus-log </span> - Enable/disable AntiVirus logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extended-log </span> - Enable/disable extended logging for antivirus. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ftgd-analytics </span> - Settings to control which files are uploaded to FortiSandbox. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inspection-mode </span> - Inspection mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mobile-malware-db </span> - Enable/disable using the mobile malware signature database. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group customized for this profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> scan-mode </span> - Choose between full scan mode and quick scan mode. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/antivirus/profile</span>  </li>
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



