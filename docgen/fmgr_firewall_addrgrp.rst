:source: fmgr_firewall_addrgrp.py

:orphan:

.. _fmgr_firewall_addrgrp:

fmgr_firewall_addrgrp -- Configure IPv4 address groups.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/addrgrp`
- `/pm/config/global/obj/firewall/addrgrp`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure IPv4 address groups.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allow-routing</span> - Enable/disable use of this group in the static route configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">allow-routing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">exclude</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">exclude-member</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">member</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">member</span> - Address objects contained within the group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Address group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tagging</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Tag category. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Tagging entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - Enable/disable address visibility in the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 address groups.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow-routing, color, member, name, uuid, visibility]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRGRP
      fmgr_firewall_addrgrp:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     allow-routing: <value in [disable, enable]>
                     color: <value of integer>
                     comment: <value of string>
                     dynamic_mapping:
                       -
                           _scope:
                             -
                                 name: <value of string>
                                 vdom: <value of string>
                           allow-routing: <value in [disable, enable]>
                           color: <value of integer>
                           comment: <value of string>
                           exclude: <value in [disable, enable]>
                           exclude-member: <value of string>
                           member: <value of string>
                           tags: <value of string>
                           uuid: <value of string>
                           visibility: <value in [disable, enable]>
                     member: <value of string>
                     name: <value of string>
                     tagging:
                       -
                           category: <value of string>
                           name: <value of string>
                           tags:
                             - <value of string>
                     uuid: <value of string>
                     visibility: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRGRP
      fmgr_firewall_addrgrp:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [allow-routing, color, member, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/addrgrp</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> allow-routing </span> - Enable/disable use of this group in the static route configuration. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - Color of icon on the GUI. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> allow-routing </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exclude </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exclude-member </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> member </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> member </span> - Address objects contained within the group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Address group name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tagging </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> category </span> - Tag category. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Tagging entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - Enable/disable address visibility in the GUI. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/addrgrp</span>  </li>
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



