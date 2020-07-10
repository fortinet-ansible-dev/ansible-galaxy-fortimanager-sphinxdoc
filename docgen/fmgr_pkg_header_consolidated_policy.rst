:source: fmgr_pkg_header_consolidated_policy.py

:orphan:

.. _fmgr_pkg_header_consolidated_policy:

fmgr_pkg_header_consolidated_policy
+++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_header_consolidated_policy</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept, ipsec]</span> </li>
 <li><span class="li-head">app-category</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">app-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">application-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auto-asic-offload</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cifs-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffserv-forward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffserv-reverse</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffservcode-forward</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffservcode-rev</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dnsfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr4</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">emailfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fixedport</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-policy-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icap-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">inbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">inspection-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">ippool</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poolname4</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">poolname6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule-timeout</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">session-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr4</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-filter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-policy-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tcp-mss-receiver</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-mss-sender</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">traffic-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-category</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">users</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-inspection-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">utm-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">voip-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpntunnel</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">waf-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: no description
      fmgr_pkg_header_consolidated_policy:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         pkg: <your own value>
         state: <value in [present, absent]>
         pkg_header_consolidated_policy:
            action: <value in [deny, accept, ipsec]>
            app-category: <value of integer>
            app-group: <value of string>
            application: <value of integer>
            application-list: <value of string>
            auto-asic-offload: <value in [disable, enable]>
            av-profile: <value of string>
            cifs-profile: <value of string>
            comments: <value of string>
            diffserv-forward: <value in [disable, enable]>
            diffserv-reverse: <value in [disable, enable]>
            diffservcode-forward: <value of string>
            diffservcode-rev: <value of string>
            dlp-sensor: <value of string>
            dnsfilter-profile: <value of string>
            dstaddr4: <value of string>
            dstaddr6: <value of string>
            dstintf: <value of string>
            emailfilter-profile: <value of string>
            fixedport: <value in [disable, enable]>
            groups: <value of string>
            http-policy-redirect: <value in [disable, enable]>
            icap-profile: <value of string>
            inbound: <value in [disable, enable]>
            inspection-mode: <value in [proxy, flow]>
            ippool: <value in [disable, enable]>
            ips-sensor: <value of string>
            logtraffic: <value in [disable, all, utm]>
            logtraffic-start: <value in [disable, enable]>
            mms-profile: <value of string>
            name: <value of string>
            nat: <value in [disable, enable]>
            outbound: <value in [disable, enable]>
            per-ip-shaper: <value of string>
            policyid: <value of integer>
            poolname4: <value of string>
            poolname6: <value of string>
            profile-group: <value of string>
            profile-protocol-options: <value of string>
            profile-type: <value in [single, group]>
            schedule: <value of string>
            schedule-timeout: <value in [disable, enable]>
            service: <value of string>
            session-ttl: <value of integer>
            spamfilter-profile: <value of string>
            srcaddr4: <value of string>
            srcaddr6: <value of string>
            srcintf: <value of string>
            ssh-filter-profile: <value of string>
            ssh-policy-redirect: <value in [disable, enable]>
            ssl-ssh-profile: <value of string>
            status: <value in [disable, enable]>
            tcp-mss-receiver: <value of integer>
            tcp-mss-sender: <value of integer>
            traffic-shaper: <value of string>
            traffic-shaper-reverse: <value of string>
            url-category: <value of integer>
            users: <value of string>
            utm-inspection-mode: <value in [proxy, flow]>
            utm-status: <value in [disable, enable]>
            uuid: <value of string>
            voip-profile: <value of string>
            vpntunnel: <value of string>
            waf-profile: <value of string>
            webfilter-profile: <value of string>



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



