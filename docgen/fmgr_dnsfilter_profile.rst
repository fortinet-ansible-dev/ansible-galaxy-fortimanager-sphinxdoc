:source: fmgr_dnsfilter_profile.py

:orphan:

.. _fmgr_dnsfilter_profile:

fmgr_dnsfilter_profile -- Configure DNS domain filter profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/dnsfilter/profile`
- `/pm/config/global/obj/dnsfilter/profile`
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
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure DNS domain filter profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure DNS domain filter profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block-action, block-botnet, comment, external-ip-blocklist, log-all-domain, name, redirect-portal, safe-search, sdns-domain-log, sdns-ftgd-err-log, youtube-restrict]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/DNSFILTER/PROFILE
      fmgr_dnsfilter_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
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

    - name: REQUESTING /PM/CONFIG/OBJ/DNSFILTER/PROFILE
      fmgr_dnsfilter_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [block-action, block-botnet, comment, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dnsfilter/profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dnsfilter/profile</span>  </li>
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



