:source: fmgr_firewall_vip64.py

:orphan:

.. _fmgr_firewall_vip64:

fmgr_firewall_vip64 -- Configure IPv6 to IPv4 virtual IPs.
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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_vip64</span> - Configure IPv6 to IPv4 virtual IPs. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">arp-reply</span> - Enable ARP reply. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">arp-reply</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldb-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive]</span> </li>
 <li><span class="li-head">mappedip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">monitor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">portforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp]</span> </li>
 <li><span class="li-head">server-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, tcp, udp, ip]</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, server-load-balance]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">extip</span> - Start-external-IP [-end-external-IP]. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - External service port. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Custom defined id. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldb-method</span> - Load balance method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive]</span> </li>
 <li><span class="li-head">mappedip</span> - Start-mapped-IP [-end-mapped-IP]. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedport</span> - Mapped service port. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">monitor</span> - Health monitors. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - VIP64 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">portforward</span> - Enable port forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">protocol</span> - Mapped port protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp]</span> </li>
 <li><span class="li-head">realservers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">client-ip</span> - Restrict server to a client IP in this range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">healthcheck</span> - Per server health check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vip]</span> </li>
 <li><span class="li-head">holddown-interval</span> - Hold down interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - Real server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - Mapped server IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - Maximum number of connections allowed to server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Health monitors. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Mapped server port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Server administrative status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, standby, disable]</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - Server type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, tcp, udp, ip]</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">type</span> - VIP type: static NAT. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, server-load-balance]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
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
    - name: Configure IPv6 to IPv4 virtual IPs.
      fmgr_firewall_vip64:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_vip64:
            arp-reply: <value in [disable, enable]>
            color: <value of integer>
            comment: <value of string>
            dynamic_mapping:
              -
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  arp-reply: <value in [disable, enable]>
                  color: <value of integer>
                  comment: <value of string>
                  extip: <value of string>
                  extport: <value of string>
                  id: <value of integer>
                  ldb-method: <value in [static, round-robin, weighted, ...]>
                  mappedip: <value of string>
                  mappedport: <value of string>
                  monitor: <value of string>
                  portforward: <value in [disable, enable]>
                  protocol: <value in [tcp, udp]>
                  server-type: <value in [http, tcp, udp, ...]>
                  src-filter: <value of string>
                  type: <value in [static-nat, server-load-balance]>
                  uuid: <value of string>
            extip: <value of string>
            extport: <value of string>
            id: <value of integer>
            ldb-method: <value in [static, round-robin, weighted, ...]>
            mappedip: <value of string>
            mappedport: <value of string>
            monitor: <value of string>
            name: <value of string>
            portforward: <value in [disable, enable]>
            protocol: <value in [tcp, udp]>
            realservers:
              -
                  client-ip: <value of string>
                  healthcheck: <value in [disable, enable, vip]>
                  holddown-interval: <value of integer>
                  id: <value of integer>
                  ip: <value of string>
                  max-connections: <value of integer>
                  monitor: <value of string>
                  port: <value of integer>
                  status: <value in [active, standby, disable]>
                  weight: <value of integer>
            server-type: <value in [http, tcp, udp, ...]>
            src-filter: <value of string>
            type: <value in [static-nat, server-load-balance]>
            uuid: <value of string>



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



