:source: fmgr_system_fortiguard.py

:orphan:

.. _fmgr_system_fortiguard:

fmgr_system_fortiguard -- Configure FortiGuard services.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">system_fortiguard</span> - Configure FortiGuard services. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">antispam-cache</span> - Enable/disable FortiGuard antispam request caching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">antispam-cache-mpercent</span> - Maximum percent of FortiGate memory the antispam cache is allowed to use (1 - 15%). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-cache-ttl</span> - Time-to-live for antispam cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-expiration</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-force-off</span> - Enable/disable turning off the FortiGuard antispam service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">antispam-license</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-timeout</span> - Antispam query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-join-forticloud</span> - Automatically connect to and login to FortiCloud. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-server-ip</span> - IP address of the FortiDDNS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-server-port</span> - Port used to communicate with FortiDDNS servers. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">load-balance-servers</span> - Number of servers to alternate between as first FortiGuard option. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-cache</span> - Enable/disable FortiGuard Virus Outbreak Prevention cache. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbreak-prevention-cache-mpercent</span> - Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%, default = 2). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-cache-ttl</span> - Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-expiration</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-force-off</span> - Turn off FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbreak-prevention-license</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-timeout</span> - FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port</span> - Port used to communicate with the FortiGuard servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [53, 80, 8888]</span> </li>
 <li><span class="li-head">sdns-server-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sdns-server-port</span> - Port used to communicate with FortiDNS servers. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">service-account-id</span> - Service account ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IPv4 address used to communicate with FortiGuard. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip6</span> - Source IPv6 address used to communicate with FortiGuard. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">update-server-location</span> - Signature update server location. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, usa]</span> </li>
 <li><span class="li-head">webfilter-cache</span> - Enable/disable FortiGuard web filter caching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-cache-ttl</span> - Time-to-live for web filter cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">webfilter-expiration</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">webfilter-force-off</span> - Enable/disable turning off the FortiGuard web filtering service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-license</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">webfilter-timeout</span> - Web filter query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span> </li>
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
    - name: Configure FortiGuard services.
      fmgr_system_fortiguard:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         system_fortiguard:
            antispam-cache: <value in [disable, enable]>
            antispam-cache-mpercent: <value of integer>
            antispam-cache-ttl: <value of integer>
            antispam-expiration: <value of integer>
            antispam-force-off: <value in [disable, enable]>
            antispam-license: <value of integer>
            antispam-timeout: <value of integer>
            auto-join-forticloud: <value in [disable, enable]>
            ddns-server-ip: <value of string>
            ddns-server-port: <value of integer>
            load-balance-servers: <value of integer>
            outbreak-prevention-cache: <value in [disable, enable]>
            outbreak-prevention-cache-mpercent: <value of integer>
            outbreak-prevention-cache-ttl: <value of integer>
            outbreak-prevention-expiration: <value of integer>
            outbreak-prevention-force-off: <value in [disable, enable]>
            outbreak-prevention-license: <value of integer>
            outbreak-prevention-timeout: <value of integer>
            port: <value in [53, 80, 8888]>
            sdns-server-ip: <value of string>
            sdns-server-port: <value of integer>
            service-account-id: <value of string>
            source-ip: <value of string>
            source-ip6: <value of string>
            update-server-location: <value in [any, usa]>
            webfilter-cache: <value in [disable, enable]>
            webfilter-cache-ttl: <value of integer>
            webfilter-expiration: <value of integer>
            webfilter-force-off: <value in [disable, enable]>
            webfilter-license: <value of integer>
            webfilter-timeout: <value of integer>



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



