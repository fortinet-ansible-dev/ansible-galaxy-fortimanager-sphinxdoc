:source: fmgr_firewall_profilegroup_obj.py

:orphan:

.. _fmgr_firewall_profilegroup_obj:

fmgr_firewall_profilegroup_obj -- Configure profile groups.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/profile-group/{profile-group}`
- `/pm/config/global/obj/firewall/profile-group/{profile-group}`
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
 <li><span class="li-head">profile-group</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure profile groups.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">application-list</span> - Name of an existing Application list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dnsfilter-profile</span> - Name of an existing DNS filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">icap-profile</span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips-sensor</span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mms-profile</span> - Name of an existing MMS profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Profile group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-filter-profile</span> - Name of an existing SSH filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">voip-profile</span> - Name of an existing VoIP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">waf-profile</span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure profile groups.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure profile groups.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-GROUP/{PROFILE-GROUP}
      fmgr_firewall_profilegroup_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-group: <value of string>
         params:
            -
               data:
                  application-list: <value of string>
                  av-profile: <value of string>
                  dlp-sensor: <value of string>
                  dnsfilter-profile: <value of string>
                  icap-profile: <value of string>
                  ips-sensor: <value of string>
                  mms-profile: <value of string>
                  name: <value of string>
                  profile-protocol-options: <value of string>
                  spamfilter-profile: <value of string>
                  ssh-filter-profile: <value of string>
                  ssl-ssh-profile: <value of string>
                  voip-profile: <value of string>
                  waf-profile: <value of string>
                  webfilter-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-GROUP/{PROFILE-GROUP}
      fmgr_firewall_profilegroup_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-group: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/profile-group/{profile-group}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> application-list </span> - Name of an existing Application list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dnsfilter-profile </span> - Name of an existing DNS filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icap-profile </span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-profile </span> - Name of an existing MMS profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Profile group name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-protocol-options </span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spamfilter-profile </span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssh-filter-profile </span> - Name of an existing SSH filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-ssh-profile </span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> voip-profile </span> - Name of an existing VoIP profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> waf-profile </span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile </span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/profile-group/{profile-group}</span>  </li>
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



