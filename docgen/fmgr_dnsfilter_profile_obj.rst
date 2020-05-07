:source: fmgr_dnsfilter_profile_obj.py

:orphan:

.. _fmgr_dnsfilter_profile_obj:

fmgr_dnsfilter_profile_obj -- Configure DNS domain filter profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/dnsfilter/profile/{profile}`
- `/pm/config/global/obj/dnsfilter/profile/{profile}`
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
 <li><span class="li-head">profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure DNS domain filter profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">block-action</span> - Action to take for blocked domains. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, redirect]</span> </li>
 <li><span class="li-head">block-botnet</span> - Enable/disable blocking botnet C&C DNS lookups. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-ip-blocklist</span> - One or more external IP block lists. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">log-all-domain</span> - Enable/disable logging of all domains visited (detailed DNS logging). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">redirect-portal</span> - IP address of the SDNS redirect portal. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">safe-search</span> - Enable/disable Google, Bing, and YouTube safe search. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sdns-domain-log</span> - Enable/disable domain filtering and botnet domain logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sdns-ftgd-err-log</span> - Enable/disable FortiGuard SDNS rating error logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">youtube-restrict</span> - Set safe search for YouTube restriction level. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [strict, moderate]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure DNS domain filter profiles.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure DNS domain filter profiles.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/DNSFILTER/PROFILE/{PROFILE}
      fmgr_dnsfilter_profile_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  block-action: <value in [block, redirect]>
                  block-botnet: <value in [disable, enable]>
                  comment: <value of string>
                  external-ip-blocklist: <value of string>
                  log-all-domain: <value in [disable, enable]>
                  name: <value of string>
                  redirect-portal: <value of string>
                  safe-search: <value in [disable, enable]>
                  sdns-domain-log: <value in [disable, enable]>
                  sdns-ftgd-err-log: <value in [disable, enable]>
                  youtube-restrict: <value in [strict, moderate]>

    - name: REQUESTING /PM/CONFIG/OBJ/DNSFILTER/PROFILE/{PROFILE}
      fmgr_dnsfilter_profile_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dnsfilter/profile/{profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> block-action </span> - Action to take for blocked domains. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-botnet </span> - Enable/disable blocking botnet C&C DNS lookups. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> external-ip-blocklist </span> - One or more external IP block lists. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-all-domain </span> - Enable/disable logging of all domains visited (detailed DNS logging). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> redirect-portal </span> - IP address of the SDNS redirect portal. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> safe-search </span> - Enable/disable Google, Bing, and YouTube safe search. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdns-domain-log </span> - Enable/disable domain filtering and botnet domain logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdns-ftgd-err-log </span> - Enable/disable FortiGuard SDNS rating error logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> youtube-restrict </span> - Set safe search for YouTube restriction level. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dnsfilter/profile/{profile}</span>  </li>
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



