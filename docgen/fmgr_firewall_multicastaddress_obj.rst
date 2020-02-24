:source: fmgr_firewall_multicastaddress_obj.py

:orphan:

.. _fmgr_firewall_multicastaddress_obj:

fmgr_firewall_multicastaddress_obj -- Configure multicast addresses.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/multicast-address/{multicast-address}`
- `/pm/config/global/obj/firewall/multicast-address/{multicast-address}`
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
 <li><span class="li-head">multicast-address</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure multicast addresses.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">associated-interface</span> - Interface associated with the address object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">color</span> - Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-ip</span> - Final IPv4 address (inclusive) in the range for the address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Multicast address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-ip</span> - First IPv4 address (inclusive) in the range for the address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet</span> - Broadcast address and subnet. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tagging</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Tag category. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Tagging entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">type</span> - Type of address object: multicast IP address range or broadcast IP/mask to be treated as a multicast address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [multicastrange, broadcastmask]</span> </li>
 <li><span class="li-head">visibility</span> - Enable/disable visibility of the multicast address on the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure multicast addresses.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure multicast addresses.</li>
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MULTICAST-ADDRESS/{MULTICAST-ADDRESS}
      fmgr_firewall_multicastaddress_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            multicast-address: <value of string>
         params:
            -
               data:
                  associated-interface: <value of string>
                  color: <value of integer>
                  comment: <value of string>
                  end-ip: <value of string>
                  name: <value of string>
                  start-ip: <value of string>
                  subnet: <value of string>
                  tagging:
                    -
                        category: <value of string>
                        name: <value of string>
                        tags:
                          - <value of string>
                  type: <value in [multicastrange, broadcastmask]>
                  visibility: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MULTICAST-ADDRESS/{MULTICAST-ADDRESS}
      fmgr_firewall_multicastaddress_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            multicast-address: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/multicast-address/{multicast-address}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> associated-interface </span> - Interface associated with the address object. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-ip </span> - Final IPv4 address (inclusive) in the range for the address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Multicast address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-ip </span> - First IPv4 address (inclusive) in the range for the address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet </span> - Broadcast address and subnet. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tagging </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> category </span> - Tag category. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Tagging entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> type </span> - Type of address object: multicast IP address range or broadcast IP/mask to be treated as a multicast address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - Enable/disable visibility of the multicast address on the GUI. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/multicast-address/{multicast-address}</span>  </li>
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



