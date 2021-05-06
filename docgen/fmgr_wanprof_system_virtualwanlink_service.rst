:source: fmgr_wanprof_system_virtualwanlink_service.py

:orphan:

.. _fmgr_wanprof_system_virtualwanlink_service:

fmgr_wanprof_system_virtualwanlink_service -- Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wanprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wanprof_system_virtualwanlink_service</span> - Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">bandwidth-weight</span> - Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">default</span> - Enable/disable use of SD-WAN as default service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward</span> - Enable/disable forward traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward-tag</span> - Forward traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dscp-reverse</span> - Enable/disable reverse traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-reverse-tag</span> - Reverse traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst</span> - Destination address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst-negate</span> - Enable/disable negation of destination address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dst6</span> - Destination address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-port</span> - End destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gateway</span> - Enable/disable SD-WAN service gateway. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - User groups. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">health-check</span> - Health check. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hold-down-time</span> - Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - Priority rule ID (1 - 4000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet service for application-based load balancing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-ctrl</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">internet-service-ctrl-group</span> - Control-based Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet service name list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom-group</span> - Custom Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-group</span> - Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet service ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">jitter-weight</span> - Coefficient of jitter in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-weight</span> - Coefficient of latency in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - Link cost factor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [latency, jitter, packet-loss, inbandwidth, outbandwidth, bibandwidth, custom-profile-1]</span> </li>
 <li><span class="li-head">link-cost-threshold</span> - Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">member</span> - Member sequence number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mode</span> - Control how the priority rule sets the priority of interfaces in the SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, manual, priority, sla, load-balance]</span> </li>
 <li><span class="li-head">name</span> - Priority rule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-loss-weight</span> - Coefficient of packet-loss in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority-members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">protocol</span> - Protocol number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">quality-link</span> - Quality grade. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">route-tag</span> - IPv4 route map route-tag. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">health-check</span> - Virtual WAN Link health-check. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">src</span> - Source address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">src-negate</span> - Enable/disable negation of source address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">src6</span> - Source address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-port</span> - Start destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SD-WAN service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tos</span> - Type of service bit pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - Type of service evaluated bits. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - User name. <span class="li-normal">type: str</span> </li>
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
    - name: Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.
      fmgr_wanprof_system_virtualwanlink_service:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         wanprof: <your own value>
         state: <value in [present, absent]>
         wanprof_system_virtualwanlink_service:
            addr-mode: <value in [ipv4, ipv6]>
            bandwidth-weight: <value of integer>
            default: <value in [disable, enable]>
            dscp-forward: <value in [disable, enable]>
            dscp-forward-tag: <value of string>
            dscp-reverse: <value in [disable, enable]>
            dscp-reverse-tag: <value of string>
            dst: <value of string>
            dst-negate: <value in [disable, enable]>
            dst6: <value of string>
            end-port: <value of integer>
            gateway: <value in [disable, enable]>
            groups: <value of string>
            health-check: <value of string>
            hold-down-time: <value of integer>
            id: <value of integer>
            internet-service: <value in [disable, enable]>
            internet-service-ctrl: <value of integer>
            internet-service-ctrl-group: <value of string>
            internet-service-custom: <value of string>
            internet-service-custom-group: <value of string>
            internet-service-group: <value of string>
            internet-service-id: <value of string>
            jitter-weight: <value of integer>
            latency-weight: <value of integer>
            link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
            link-cost-threshold: <value of integer>
            member: <value of string>
            mode: <value in [auto, manual, priority, ...]>
            name: <value of string>
            packet-loss-weight: <value of integer>
            priority-members: <value of string>
            protocol: <value of integer>
            quality-link: <value of integer>
            route-tag: <value of integer>
            sla:
              -
                  health-check: <value of string>
                  id: <value of integer>
            src: <value of string>
            src-negate: <value in [disable, enable]>
            src6: <value of string>
            start-port: <value of integer>
            status: <value in [disable, enable]>
            tos: <value of string>
            tos-mask: <value of string>
            users: <value of string>



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



