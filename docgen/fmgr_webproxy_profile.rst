:source: fmgr_webproxy_profile.py

:orphan:

.. _fmgr_webproxy_profile:

fmgr_webproxy_profile -- Configure web proxy profiles.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/web-proxy/profile`
- `/pm/config/global/obj/web-proxy/profile`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure web proxy profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">header-client-ip</span> - Action to take on the HTTP client-IP header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, add, remove]</span> </li>
 <li><span class="li-head">header-front-end-https</span> - Action to take on the HTTP front-end-HTTPS header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, add, remove]</span> </li>
 <li><span class="li-head">header-via-request</span> - Action to take on the HTTP via header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, add, remove]</span> </li>
 <li><span class="li-head">header-via-response</span> - Action to take on the HTTP via header in forwarded responses: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, add, remove]</span> </li>
 <li><span class="li-head">header-x-authenticated-groups</span> - Action to take on the HTTP x-authenticated-groups header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, add, remove]</span> </li>
 <li><span class="li-head">header-x-authenticated-user</span> - Action to take on the HTTP x-authenticated-user header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, add, remove]</span> </li>
 <li><span class="li-head">header-x-forwarded-for</span> - Action to take on the HTTP x-forwarded-for header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, add, remove]</span> </li>
 <li><span class="li-head">headers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action when HTTP the header forwarded. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [add-to-request, add-to-response, remove-from-request, remove-from-response]</span> </li>
 <li><span class="li-head">content</span> - HTTP headers content. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - HTTP forwarded header id. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - HTTP forwarded header name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log-header-change</span> - Enable/disable logging HTTP header changes. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">strip-encoding</span> - Enable/disable stripping unsupported encoding from the request header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure web proxy profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [header-client-ip, header-front-end-https, header-via-request, header-via-response, header-x-authenticated-groups, header-x-authenticated-user, header-x-forwarded-for, log-header-change, name, strip-encoding]</span> </li>
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/WEB-PROXY/PROFILE
      fmgr_webproxy_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     header-client-ip: <value in [pass, add, remove]>
                     header-front-end-https: <value in [pass, add, remove]>
                     header-via-request: <value in [pass, add, remove]>
                     header-via-response: <value in [pass, add, remove]>
                     header-x-authenticated-groups: <value in [pass, add, remove]>
                     header-x-authenticated-user: <value in [pass, add, remove]>
                     header-x-forwarded-for: <value in [pass, add, remove]>
                     headers:
                       -
                           action: <value in [add-to-request, add-to-response, remove-from-request, ...]>
                           content: <value of string>
                           id: <value of integer>
                           name: <value of string>
                     log-header-change: <value in [disable, enable]>
                     name: <value of string>
                     strip-encoding: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEB-PROXY/PROFILE
      fmgr_webproxy_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [header-client-ip, header-front-end-https, header-via-request, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/web-proxy/profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> header-client-ip </span> - Action to take on the HTTP client-IP header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-front-end-https </span> - Action to take on the HTTP front-end-HTTPS header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-via-request </span> - Action to take on the HTTP via header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-via-response </span> - Action to take on the HTTP via header in forwarded responses: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-x-authenticated-groups </span> - Action to take on the HTTP x-authenticated-groups header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-x-authenticated-user </span> - Action to take on the HTTP x-authenticated-user header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-x-forwarded-for </span> - Action to take on the HTTP x-forwarded-for header in forwarded requests: forwards (pass), adds, or removes the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> headers </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action when HTTP the header forwarded. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> content </span> - HTTP headers content. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - HTTP forwarded header id. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - HTTP forwarded header name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log-header-change </span> - Enable/disable logging HTTP header changes. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> strip-encoding </span> - Enable/disable stripping unsupported encoding from the request header. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/web-proxy/profile</span>  </li>
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



