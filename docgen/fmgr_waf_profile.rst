:source: fmgr_waf_profile.py

:orphan:

.. _fmgr_waf_profile:

fmgr_waf_profile -- Web application firewall configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/waf/profile`
- `/pm/config/global/obj/waf/profile`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Web application firewall configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external</span> - Disable/Enable external HTTP Inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - WAF Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-access</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">access-pattern</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - URL access pattern ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">negate</span> - Enable/disable match negation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pattern</span> - URL pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">regex</span> - Enable/disable regular expression based pattern match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, permit, block]</span> </li>
 <li><span class="li-head">address</span> - Host address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - URL access ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Web application firewall configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [comment, extended-log, external, name]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE
      fmgr_waf_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     comment: <value of string>
                     extended-log: <value in [disable, enable]>
                     external: <value in [disable, enable]>
                     name: <value of string>
                     url-access:
                       -
                           access-pattern:
                             -
                                 id: <value of integer>
                                 negate: <value in [disable, enable]>
                                 pattern: <value of string>
                                 regex: <value in [disable, enable]>
                                 srcaddr: <value of string>
                           action: <value in [bypass, permit, block]>
                           address: <value of string>
                           id: <value of integer>
                           log: <value in [disable, enable]>
                           severity: <value in [low, medium, high]>

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE
      fmgr_waf_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [comment, extended-log, external, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extended-log </span> - Enable/disable extended logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> external </span> - Disable/Enable external HTTP Inspection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - WAF Profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url-access </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> access-pattern </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - URL access pattern ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> negate </span> - Enable/disable match negation. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern </span> - URL pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> regex </span> - Enable/disable regular expression based pattern match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - Source address. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> address </span> - Host address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - URL access ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile</span>  </li>
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



