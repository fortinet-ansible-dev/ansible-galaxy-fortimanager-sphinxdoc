:source: fmgr_firewall_address6_obj.py

:orphan:

.. _fmgr_firewall_address6_obj:

fmgr_firewall_address6_obj -- Configure IPv6 firewall addresses.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/address6/{address6}`
- `/pm/config/global/obj/firewall/address6/{address6}`
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
 <li><span class="li-head">address6</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure IPv6 firewall addresses.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">cache-ttl</span> - Minimal TTL of individual IPv6 addresses in FQDN cache. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - Integer value to determine the color of the icon in the GUI (range 1 to 32, default = 0, which sets the value to 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">cache-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">host</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">host-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, specific]</span> </li>
 <li><span class="li-head">ip6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sdn</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [nsx]</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">template</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipprefix, iprange, nsx, dynamic, fqdn, template]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">end-ip</span> - Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - Fully qualified domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">host</span> - Host Address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">host-type</span> - Host type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, specific]</span> </li>
 <li><span class="li-head">ip6</span> - IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> - IP. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj-id</span> - Object ID for NSX. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sdn</span> - SDN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [nsx]</span> </li>
 <li><span class="li-head">start-ip</span> - First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet-segment</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Subnet segment type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, specific]</span> </li>
 <li><span class="li-head">value</span> - Subnet segment value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">tagging</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Tag category. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Tagging entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">template</span> - IPv6 address template. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of IPv6 address object (default = ipprefix). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipprefix, iprange, nsx, dynamic, fqdn, template]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - Enable/disable the visibility of the object in the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure IPv6 firewall addresses.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv6 firewall addresses.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS6/{ADDRESS6}
      fmgr_firewall_address6_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            address6: <value of string>
         params:
            -
               data:
                  cache-ttl: <value of integer>
                  color: <value of integer>
                  comment: <value of string>
                  dynamic_mapping:
                    -
                        _scope:
                          -
                              name: <value of string>
                              vdom: <value of string>
                        cache-ttl: <value of integer>
                        color: <value of integer>
                        comment: <value of string>
                        end-ip: <value of string>
                        fqdn: <value of string>
                        host: <value of string>
                        host-type: <value in [any, specific]>
                        ip6: <value of string>
                        obj-id: <value of string>
                        sdn: <value in [nsx]>
                        start-ip: <value of string>
                        tags: <value of string>
                        template: <value of string>
                        type: <value in [ipprefix, iprange, nsx, ...]>
                        uuid: <value of string>
                        visibility: <value in [disable, enable]>
                  end-ip: <value of string>
                  fqdn: <value of string>
                  host: <value of string>
                  host-type: <value in [any, specific]>
                  ip6: <value of string>
                  list:
                    -
                        ip: <value of string>
                  name: <value of string>
                  obj-id: <value of string>
                  sdn: <value in [nsx]>
                  start-ip: <value of string>
                  subnet-segment:
                    -
                        name: <value of string>
                        type: <value in [any, specific]>
                        value: <value of string>
                  tagging:
                    -
                        category: <value of string>
                        name: <value of string>
                        tags:
                          - <value of string>
                  template: <value of string>
                  type: <value in [ipprefix, iprange, nsx, ...]>
                  uuid: <value of string>
                  visibility: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS6/{ADDRESS6}
      fmgr_firewall_address6_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            address6: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/address6/{address6}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> cache-ttl </span> - Minimal TTL of individual IPv6 addresses in FQDN cache. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> color </span> - Integer value to determine the color of the icon in the GUI (range 1 to 32, default = 0, which sets the value to 1). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> cache-ttl </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> color </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fqdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> obj-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> template </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> end-ip </span> - Final IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fqdn </span> - Fully qualified domain name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host </span> - Host Address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-type </span> - Host type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6 </span> - IPv6 address prefix (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ip </span> - IP. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> obj-id </span> - Object ID for NSX. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn </span> - SDN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-ip </span> - First IP address (inclusive) in the range for the address (format: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet-segment </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Subnet segment type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> value </span> - Subnet segment value. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> tagging </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> category </span> - Tag category. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Tagging entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> template </span> - IPv6 address template. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Type of IPv6 address object (default = ipprefix). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - Enable/disable the visibility of the object in the GUI. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/address6/{address6}</span>  </li>
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



