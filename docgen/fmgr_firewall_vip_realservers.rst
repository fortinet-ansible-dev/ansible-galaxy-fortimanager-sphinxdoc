:source: fmgr_firewall_vip_realservers.py

:orphan:

.. _fmgr_firewall_vip_realservers:

fmgr_firewall_vip_realservers -- Select the real servers that this server load balancing VIP will distribute traffic to.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vip</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_vip_realservers</span> - Select the real servers that this server load balancing VIP will distribute traffic to. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">client-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">healthcheck</span> - Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vip]</span> </li>
 <li><span class="li-head">holddown-interval</span> - Time in seconds that the health check monitor continues to monitor and unresponsive server that should be active. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-host</span> - HTTP server domain name in HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - IP address of the real server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - Max number of active connections that can be directed to the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Port for communicating with the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, standby, disable]</span> </li>
 <li><span class="li-head">weight</span> - Weight of the real server. <span class="li-normal">type: int</span> </li>
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
    - name: Select the real servers that this server load balancing VIP will distribute traffic to.
      fmgr_firewall_vip_realservers:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vip: <your own value>
         state: <value in [present, absent]>
         firewall_vip_realservers:
            client-ip: <value of string>
            healthcheck: <value in [disable, enable, vip]>
            holddown-interval: <value of integer>
            http-host: <value of string>
            ip: <value of string>
            max-connections: <value of integer>
            monitor: <value of string>
            port: <value of integer>
            seq: <value of integer>
            status: <value in [active, standby, disable]>
            weight: <value of integer>



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



