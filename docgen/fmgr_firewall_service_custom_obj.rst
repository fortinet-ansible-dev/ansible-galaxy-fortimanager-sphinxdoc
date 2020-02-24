:source: fmgr_firewall_service_custom_obj.py

:orphan:

.. _fmgr_firewall_service_custom_obj:

fmgr_firewall_service_custom_obj -- Configure custom services.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/service/custom/{custom}`
- `/pm/config/global/obj/firewall/service/custom/{custom}`
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
 <li><span class="li-head">custom</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure custom services.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">app-category</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">app-service-type</span> - Application service type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, app-id, app-category]</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">category</span> - Service category. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">check-reset-range</span> - Configure the type of ICMP error message verification. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, default, strict]</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - Fully qualified domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">helper</span> - Helper name. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, auto, ftp, tftp, ras, h323, tns, mms, sip, pptp, rtsp, dns-udp, dns-tcp, pmap, rsh, dcerpc, mgcp, gtp-c, gtp-u, gtp-b]</span> </li>
 <li><span class="li-head">icmpcode</span> - ICMP code. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">icmptype</span> - ICMP type. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">iprange</span> - Start and end of the IP range associated with service. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Custom service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">protocol</span> - Protocol type based on IANA numbers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ICMP, IP, TCP/UDP/SCTP, ICMP6, HTTP, FTP, CONNECT, SOCKS, ALL, SOCKS-TCP, SOCKS-UDP]</span> </li>
 <li><span class="li-head">protocol-number</span> - IP protocol number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">proxy</span> - Enable/disable web proxy service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sctp-portrange</span> - Multiple SCTP port ranges. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">session-ttl</span> - Session TTL (300 - 604800, 0 = default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-halfclose-timer</span> - Wait time to close a TCP session waiting for an unanswered FIN packet (1 - 86400 sec, 0 = default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-halfopen-timer</span> - Wait time to close a TCP session waiting for an unanswered open session packet (1 - 86400 sec, 0 = default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-portrange</span> - Multiple TCP port ranges. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tcp-timewait-timer</span> - Set the length of the TCP TIME-WAIT state in seconds (1 - 300 sec, 0 = default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">udp-idle-timer</span> - UDP half close timeout (0 - 86400 sec, 0 = default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">udp-portrange</span> - Multiple UDP port ranges. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - Enable/disable the visibility of the service on the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure custom services.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure custom services.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Configure custom services.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [before, after]</span> </li>
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SERVICE/CUSTOM/{CUSTOM}
      fmgr_firewall_service_custom_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            custom: <value of string>
         params:
            -
               data:
                  app-category:
                    - <value of integer>
                  app-service-type: <value in [disable, app-id, app-category]>
                  application:
                    - <value of integer>
                  category: <value of string>
                  check-reset-range: <value in [disable, default, strict]>
                  color: <value of integer>
                  comment: <value of string>
                  fqdn: <value of string>
                  helper: <value in [disable, auto, ftp, ...]>
                  icmpcode: <value of integer>
                  icmptype: <value of integer>
                  iprange: <value of string>
                  name: <value of string>
                  protocol: <value in [ICMP, IP, TCP/UDP/SCTP, ...]>
                  protocol-number: <value of integer>
                  proxy: <value in [disable, enable]>
                  sctp-portrange: <value of string>
                  session-ttl: <value of integer>
                  tcp-halfclose-timer: <value of integer>
                  tcp-halfopen-timer: <value of integer>
                  tcp-portrange: <value of string>
                  tcp-timewait-timer: <value of integer>
                  udp-idle-timer: <value of integer>
                  udp-portrange: <value of string>
                  visibility: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SERVICE/CUSTOM/{CUSTOM}
      fmgr_firewall_service_custom_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            custom: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SERVICE/CUSTOM/{CUSTOM}
      fmgr_firewall_service_custom_obj:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            custom: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, move, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/service/custom/{custom}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> app-category </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> app-service-type </span> - Application service type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> category </span> - Service category. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> check-reset-range </span> - Configure the type of ICMP error message verification. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - Color of icon on the GUI. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fqdn </span> - Fully qualified domain name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> helper </span> - Helper name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icmpcode </span> - ICMP code. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> icmptype </span> - ICMP type. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> iprange </span> - Start and end of the IP range associated with service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Custom service name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol type based on IANA numbers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol-number </span> - IP protocol number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> proxy </span> - Enable/disable web proxy service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sctp-portrange </span> - Multiple SCTP port ranges. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> session-ttl </span> - Session TTL (300 - 604800, 0 = default). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-halfclose-timer </span> - Wait time to close a TCP session waiting for an unanswered FIN packet (1 - 86400 sec, 0 = default). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-halfopen-timer </span> - Wait time to close a TCP session waiting for an unanswered open session packet (1 - 86400 sec, 0 = default). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-portrange </span> - Multiple TCP port ranges. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tcp-timewait-timer </span> - Set the length of the TCP TIME-WAIT state in seconds (1 - 300 sec, 0 = default). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> udp-idle-timer </span> - UDP half close timeout (0 - 86400 sec, 0 = default). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> udp-portrange </span> - Multiple UDP port ranges. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - Enable/disable the visibility of the service on the GUI. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/service/custom/{custom}</span>  </li>
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



