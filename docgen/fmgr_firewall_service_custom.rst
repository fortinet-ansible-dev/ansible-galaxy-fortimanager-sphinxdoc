:source: fmgr_firewall_service_custom.py

:orphan:

.. _fmgr_firewall_service_custom:

fmgr_firewall_service_custom -- Configure custom services.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device.
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0.


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.9.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method of the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_service_custom</span> - Configure custom services. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">app-category</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">app-service-type</span> - Application service type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, app-id, app-category]</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: int</span></li>
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






Notes
-----
.. note::

   - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.

   - To create or update an object, use state: present directive.

   - To delete an object, use state: absent directive

   - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

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
    - name: Configure custom services.
      fmgr_firewall_service_custom:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_service_custom:
            app-category: <value of integer>
            app-service-type: <value in [disable, app-id, app-category]>
            application: <value of integer>
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



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
 <li> <span class="li-return">response_data</span> - The data body of the api response <span class="li-normal">returned: optional</span> <span class="li-normal">type: list or dict</span></li>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



