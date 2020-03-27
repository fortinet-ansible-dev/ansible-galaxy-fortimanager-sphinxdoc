:source: fmgr_firewall_ippool6_obj.py

:orphan:

.. _fmgr_firewall_ippool6_obj:

fmgr_firewall_ippool6_obj -- Configure IPv6 IP pools.
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/ippool6/{ippool6}`
- `/pm/config/global/obj/firewall/ippool6/{ippool6}`
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
 <li><span class="li-head">ippool6</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure IPv6 IP pools.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comments</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">endip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">startip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">endip</span> - Final IPv6 address (inclusive) in the range for the address pool (format xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx, Default: ::). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - IPv6 IP pool name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">startip</span> - First IPv6 address (inclusive) in the range for the address pool (format xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx, Default: ::). <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure IPv6 IP pools.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv6 IP pools.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/IPPOOL6/{IPPOOL6}
      fmgr_firewall_ippool6_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ippool6: <value of string>
         params:
            -
               data:
                  comments: <value of string>
                  dynamic_mapping:
                    -
                        _scope:
                          -
                              name: <value of string>
                              vdom: <value of string>
                        comments: <value of string>
                        endip: <value of string>
                        startip: <value of string>
                  endip: <value of string>
                  name: <value of string>
                  startip: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/IPPOOL6/{IPPOOL6}
      fmgr_firewall_ippool6_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ippool6: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ippool6/{ippool6}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comments </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> comments </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> startip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> endip </span> - Final IPv6 address (inclusive) in the range for the address pool (format xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx, Default: ::). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - IPv6 IP pool name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> startip </span> - First IPv6 address (inclusive) in the range for the address pool (format xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx, Default: ::). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ippool6/{ippool6}</span>  </li>
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



