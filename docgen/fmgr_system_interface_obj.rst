:source: fmgr_system_interface_obj.py

:orphan:

.. _fmgr_system_interface_obj:

fmgr_system_interface_obj -- Interface configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/interface/{interface}`
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
 <li><span class="li-head">interface</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - Interface configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Interface configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">alias</span> - Alias. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, https, ssh, snmp, http, webservice, https-logging]</span> </li>
 </ul>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - IP address of interface. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0 0.0.0.0</span> </li>
 <li><span class="li-head">ipv6</span> <li><span class="li-head">ip6-address</span> - IPv6 address/prefix of interface. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::/0</span> </li>
 <li><span class="li-head">ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, https, ssh, snmp, http, webservice, https-logging]</span> </li>
 </ul>
 <li><span class="li-head">ip6-autoconf</span> - Enable/disable address auto config (SLAAC). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">mtu</span> - Maximum transportation unit(68 - 9000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 1500</span> </li>
 <li><span class="li-head">name</span> - Interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">serviceaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fgtupdates, fclupdates, webfilter-antispam]</span> </li>
 </ul>
 <li><span class="li-head">speed</span> - Speed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, 10full, 10half, 100full, 100half, 1000full, 10000full]</span>  <span class="li-normal">default: auto</span> </li>
 <li><span class="li-head">status</span> - Interface status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [down, up]</span>  <span class="li-normal">default: up</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/INTERFACE/{INTERFACE}
      fmgr_system_interface_obj:
         method: <value in [set, update]>
         url_params:
            interface: <value of string>
         params:
            -
               data:
                  alias: <value of string>
                  allowaccess:
                    - <value in [ping, https, ssh, ...]>
                  description: <value of string>
                  ip: <value of string default: '0.0.0.0 0.0.0.0'>
                  ipv6:
                     ip6-address: <value of string default: '::/0'>
                     ip6-allowaccess:
                       - <value in [ping, https, ssh, ...]>
                     ip6-autoconf: <value in [disable, enable] default: 'enable'>
                  mtu: <value of integer default: 1500>
                  name: <value of string>
                  serviceaccess:
                    - <value in [fgtupdates, fclupdates, webfilter-antispam]>
                  speed: <value in [auto, 10full, 10half, ...] default: 'auto'>
                  status: <value in [down, up] default: 'up'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/interface/{interface}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> alias </span> - Alias. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> allowaccess </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> description </span> - Description. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - IP address of interface. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ipv6 </span> <li> <span class="li-return"> ip6-address </span> - IPv6 address/prefix of interface. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::/0</span>  </li>
 <li> <span class="li-return"> ip6-allowaccess </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ip6-autoconf </span> - Enable/disable address auto config (SLAAC). <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> mtu </span> - Maximum transportation unit(68 - 9000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 1500</span>  </li>
 <li> <span class="li-return"> name </span> - Interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> serviceaccess </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> speed </span> - Speed. <span class="li-normal">type: str</span>  <span class="li-normal">example: auto</span>  </li>
 <li> <span class="li-return"> status </span> - Interface status. <span class="li-normal">type: str</span>  <span class="li-normal">example: up</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/interface/{interface}</span>  </li>
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



