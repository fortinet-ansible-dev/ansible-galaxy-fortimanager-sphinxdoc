:source: fmgr_firewall_ippool_obj.py

:orphan:

.. _fmgr_firewall_ippool_obj:

fmgr_firewall_ippool_obj -- Configure IPv4 IP pools.
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/ippool/{ippool}`
- `/pm/config/global/obj/firewall/ippool/{ippool}`
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
 <li><span class="li-head">ippool</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure IPv4 IP pools.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">arp-intf</span> - Select an interface from available options that will reply to ARP requests. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">arp-reply</span> - Enable/disable replying to ARP requests when an IP Pool is added to a policy (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">associated-interface</span> - Associated interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">block-size</span> - Number of addresses in a block (64 to 4096, default = 128). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comments</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">arp-intf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">arp-reply</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">associated-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">block-size</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">endip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">num-blocks-per-user</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pba-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">permit-any-host</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">source-endip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-startip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">startip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [overload, one-to-one, fixed-port-range, port-block-allocation]</span> </li>
 </ul>
 <li><span class="li-head">endip</span> - Final IPv4 address (inclusive) in the range for the address pool (format xxx. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - IP pool name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">num-blocks-per-user</span> - Number of addresses blocks that can be used by a user (1 to 128, default = 8). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pba-timeout</span> - Port block allocation timeout (seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">permit-any-host</span> - Enable/disable full cone NAT. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">source-endip</span> - Final IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-startip</span> - First IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">startip</span> - First IPv4 address (inclusive) in the range for the address pool (format xxx. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - IP pool type (overload, one-to-one, fixed port range, or port block allocation). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [overload, one-to-one, fixed-port-range, port-block-allocation]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure IPv4 IP pools.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 IP pools.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/IPPOOL/{IPPOOL}
      fmgr_firewall_ippool_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ippool: <value of string>
         params:
            -
               data:
                  arp-intf: <value of string>
                  arp-reply: <value in [disable, enable]>
                  associated-interface: <value of string>
                  block-size: <value of integer>
                  comments: <value of string>
                  dynamic_mapping:
                    -
                        _scope:
                          -
                              name: <value of string>
                              vdom: <value of string>
                        arp-intf: <value of string>
                        arp-reply: <value in [disable, enable]>
                        associated-interface: <value of string>
                        block-size: <value of integer>
                        comments: <value of string>
                        endip: <value of string>
                        num-blocks-per-user: <value of integer>
                        pba-timeout: <value of integer>
                        permit-any-host: <value in [disable, enable]>
                        source-endip: <value of string>
                        source-startip: <value of string>
                        startip: <value of string>
                        type: <value in [overload, one-to-one, fixed-port-range, ...]>
                  endip: <value of string>
                  name: <value of string>
                  num-blocks-per-user: <value of integer>
                  pba-timeout: <value of integer>
                  permit-any-host: <value in [disable, enable]>
                  source-endip: <value of string>
                  source-startip: <value of string>
                  startip: <value of string>
                  type: <value in [overload, one-to-one, fixed-port-range, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/IPPOOL/{IPPOOL}
      fmgr_firewall_ippool_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ippool: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ippool/{ippool}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> arp-intf </span> - Select an interface from available options that will reply to ARP requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> arp-reply </span> - Enable/disable replying to ARP requests when an IP Pool is added to a policy (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> associated-interface </span> - Associated interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-size </span> - Number of addresses in a block (64 to 4096, default = 128). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comments </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> arp-intf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> arp-reply </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> associated-interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-size </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comments </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> num-blocks-per-user </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> pba-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> permit-any-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-endip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-startip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> startip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> endip </span> - Final IPv4 address (inclusive) in the range for the address pool (format xxx. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - IP pool name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> num-blocks-per-user </span> - Number of addresses blocks that can be used by a user (1 to 128, default = 8). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> pba-timeout </span> - Port block allocation timeout (seconds). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> permit-any-host </span> - Enable/disable full cone NAT. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-endip </span> - Final IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-startip </span> - First IPv4 address (inclusive) in the range of the source addresses to be translated (format xxx. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> startip </span> - First IPv4 address (inclusive) in the range for the address pool (format xxx. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - IP pool type (overload, one-to-one, fixed port range, or port block allocation). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ippool/{ippool}</span>  </li>
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



