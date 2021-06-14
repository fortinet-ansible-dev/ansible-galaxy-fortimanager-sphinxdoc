:source: fmgr_wanprof_system_virtualwanlink_healthcheck.py

:orphan:

.. _fmgr_wanprof_system_virtualwanlink_healthcheck:

fmgr_wanprof_system_virtualwanlink_healthcheck -- SD-WAN status checking or health checking.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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



FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <br>
 <table>
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 </tr>
 <tr>
 <td>wanprof_system_virtualwanlink_healthcheck</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 </tr>
 </table>
 <p>



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
 <li><span class="li-head">wanprof_system_virtualwanlink_healthcheck</span> - SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can co... <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_dynamic-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">failtime</span> - Number of failures before server is considered lost (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-agent</span> - String in the http-agent field in the HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-get</span> - URL used to communicate with the server if the protocol if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-match</span> - Response string expected from the server if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interval</span> - Status check interval, or the time between attempting to connect to the server (1 - 3600 sec, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Status check or health check name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-size</span> - Packet size of a twamp test session, <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">port</span> - Port number used to communicate with the server over the selected protocol. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">protocol</span> - Protocol used to determine if the FortiGate can communicate with the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http, twamp, ping6, dns]</span> </li>
 <li><span class="li-head">recoverytime</span> - Number of successful responses received before server is considered recovered (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-mode</span> - Twamp controller security mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, authentication]</span> </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">jitter-threshold</span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-threshold</span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [latency, jitter, packet-loss]</span> </li>
 <li><span class="li-head">packetloss-threshold</span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">threshold-alert-jitter</span> - Alert threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-latency</span> - Alert threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-packetloss</span> - Alert threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-jitter</span> - Warning threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-latency</span> - Warning threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-packetloss</span> - Warning threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-cascade-interface</span> - Enable/disable update cascade interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">update-static-route</span> - Enable/disable updating the static route. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">probe-packets</span> - Enable/disable transmission of probe packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sla-fail-log-period</span> - Time interval in seconds that SLA fail log messages will be generated (0 - 3600, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sla-pass-log-period</span> - Time interval in seconds that SLA pass log messages will be generated (0 - 3600, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">diffservcode</span> - Differentiated services code point (DSCP) in the IP header of the probe packet. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-request-domain</span> - Fully qualified domain name to resolve for the DNS probe. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ha-priority</span> - HA election priority (1 - 50). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">probe-count</span> - Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">probe-timeout</span> - Time to wait before a probe packet is considered lost (500 - 5000 msec, default = 500). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">system-dns</span> - Enable/disable system DNS as the probe server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can co...
      fmgr_wanprof_system_virtualwanlink_healthcheck:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         wanprof: <your own value>
         state: <value in [present, absent]>
         wanprof_system_virtualwanlink_healthcheck:
            _dynamic-server: <value of string>
            addr-mode: <value in [ipv4, ipv6]>
            failtime: <value of integer>
            http-agent: <value of string>
            http-get: <value of string>
            http-match: <value of string>
            interval: <value of integer>
            members: <value of string>
            name: <value of string>
            packet-size: <value of integer>
            password: <value of string>
            port: <value of integer>
            protocol: <value in [ping, tcp-echo, udp-echo, ...]>
            recoverytime: <value of integer>
            security-mode: <value in [none, authentication]>
            server: <value of string>
            sla:
              -
                  id: <value of integer>
                  jitter-threshold: <value of integer>
                  latency-threshold: <value of integer>
                  link-cost-factor:
                    - latency
                    - jitter
                    - packet-loss
                  packetloss-threshold: <value of integer>
            threshold-alert-jitter: <value of integer>
            threshold-alert-latency: <value of integer>
            threshold-alert-packetloss: <value of integer>
            threshold-warning-jitter: <value of integer>
            threshold-warning-latency: <value of integer>
            threshold-warning-packetloss: <value of integer>
            update-cascade-interface: <value in [disable, enable]>
            update-static-route: <value in [disable, enable]>
            internet-service-id: <value of string>
            probe-packets: <value in [disable, enable]>
            sla-fail-log-period: <value of integer>
            sla-pass-log-period: <value of integer>
            diffservcode: <value of string>
            dns-request-domain: <value of string>
            ha-priority: <value of integer>
            probe-count: <value of integer>
            probe-timeout: <value of integer>
            system-dns: <value in [disable, enable]>



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



