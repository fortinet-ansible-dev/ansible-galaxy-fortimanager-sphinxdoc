:source: fmgr_firewall_address.py

:orphan:

.. _fmgr_firewall_address:

fmgr_firewall_address -- Configure IPv4 addresses.
++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/address`
- `/pm/config/global/obj/firewall/address`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure IPv4 addresses.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allow-routing</span> - Enable/disable use of this address in the static route configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">associated-interface</span> - Network interface associated with address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cache-ttl</span> - Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">country</span> - IP addresses associated to a specific country. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">allow-routing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">associated-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cache-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">country</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">epg-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">organization</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policy-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sdn</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack]</span> </li>
 <li><span class="li-head">sdn-addr-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [private, public, all]</span> </li>
 <li><span class="li-head">sdn-tag</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tenant</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipmask, iprange, fqdn, wildcard, geography, url, wildcard-fqdn, nsx, aws, dynamic, interface-subnet, mac]</span> </li>
 <li><span class="li-head">url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wildcard</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wildcard-fqdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">end-ip</span> - Final IP address (inclusive) in the range for the address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">epg-name</span> - Endpoint group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - Match criteria filter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - Fully Qualified Domain Name address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> - IP. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj-id</span> - Object ID for NSX. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">organization</span> - Organization domain name (Syntax: organization/domain). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policy-group</span> - Policy group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sdn</span> - SDN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack]</span> </li>
 <li><span class="li-head">sdn-tag</span> - SDN Tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-ip</span> - First IP address (inclusive) in the range for the address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet</span> - IP address and subnet mask of address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet-name</span> - Subnet name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tagging</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Tag category. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Tagging entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">tenant</span> - Tenant. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipmask, iprange, fqdn, wildcard, geography, url, wildcard-fqdn, nsx, aws, dynamic, interface-subnet, mac]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - Enable/disable address visibility in the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wildcard</span> - IP address and wildcard netmask. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wildcard-fqdn</span> - Fully Qualified Domain Name with wildcard characters. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 addresses.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow-routing, associated-interface, cache-ttl, color, country, end-ip, epg-name, filter, fqdn, name, obj-id, organization, policy-group, sdn, sdn-tag, start-ip, subnet, subnet-name, tenant, type, uuid, visibility, wildcard, wildcard-fqdn]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS
      fmgr_firewall_address:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     allow-routing: <value in [disable, enable]>
                     associated-interface: <value of string>
                     cache-ttl: <value of integer>
                     color: <value of integer>
                     comment: <value of string>
                     country: <value of string>
                     dynamic_mapping:
                       -
                           _scope:
                             -
                                 name: <value of string>
                                 vdom: <value of string>
                           allow-routing: <value in [disable, enable]>
                           associated-interface: <value of string>
                           cache-ttl: <value of integer>
                           color: <value of integer>
                           comment: <value of string>
                           country: <value of string>
                           end-ip: <value of string>
                           end-mac: <value of string>
                           epg-name: <value of string>
                           filter: <value of string>
                           fqdn: <value of string>
                           interface: <value of string>
                           obj-id: <value of string>
                           organization: <value of string>
                           policy-group: <value of string>
                           sdn: <value in [aci, aws, nsx, ...]>
                           sdn-addr-type: <value in [private, public, all]>
                           sdn-tag: <value of string>
                           start-ip: <value of string>
                           start-mac: <value of string>
                           subnet: <value of string>
                           subnet-name: <value of string>
                           tags: <value of string>
                           tenant: <value of string>
                           type: <value in [ipmask, iprange, fqdn, ...]>
                           url: <value of string>
                           uuid: <value of string>
                           visibility: <value in [disable, enable]>
                           wildcard: <value of string>
                           wildcard-fqdn: <value of string>
                     end-ip: <value of string>
                     epg-name: <value of string>
                     filter: <value of string>
                     fqdn: <value of string>
                     list:
                       -
                           ip: <value of string>
                     name: <value of string>
                     obj-id: <value of string>
                     organization: <value of string>
                     policy-group: <value of string>
                     sdn: <value in [aci, aws, nsx, ...]>
                     sdn-tag: <value of string>
                     start-ip: <value of string>
                     subnet: <value of string>
                     subnet-name: <value of string>
                     tagging:
                       -
                           category: <value of string>
                           name: <value of string>
                           tags:
                             - <value of string>
                     tenant: <value of string>
                     type: <value in [ipmask, iprange, fqdn, ...]>
                     uuid: <value of string>
                     visibility: <value in [disable, enable]>
                     wildcard: <value of string>
                     wildcard-fqdn: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS
      fmgr_firewall_address:
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
                    - <value in [allow-routing, associated-interface, cache-ttl, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/address</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> allow-routing </span> - Enable/disable use of this address in the static route configuration. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> associated-interface </span> - Network interface associated with address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cache-ttl </span> - Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> color </span> - Color of icon on the GUI. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> country </span> - IP addresses associated to a specific country. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> allow-routing </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> associated-interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cache-ttl </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> color </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> country </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-mac </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> epg-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fqdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> obj-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> organization </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policy-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn-addr-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn-tag </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-mac </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tenant </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wildcard </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wildcard-fqdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> end-ip </span> - Final IP address (inclusive) in the range for the address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> epg-name </span> - Endpoint group name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter </span> - Match criteria filter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fqdn </span> - Fully Qualified Domain Name address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ip </span> - IP. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> obj-id </span> - Object ID for NSX. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> organization </span> - Organization domain name (Syntax: organization/domain). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policy-group </span> - Policy group name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn </span> - SDN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn-tag </span> - SDN Tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-ip </span> - First IP address (inclusive) in the range for the address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet </span> - IP address and subnet mask of address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet-name </span> - Subnet name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tagging </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> category </span> - Tag category. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Tagging entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> tenant </span> - Tenant. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Type of address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - Enable/disable address visibility in the GUI. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wildcard </span> - IP address and wildcard netmask. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wildcard-fqdn </span> - Fully Qualified Domain Name with wildcard characters. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/address</span>  </li>
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



