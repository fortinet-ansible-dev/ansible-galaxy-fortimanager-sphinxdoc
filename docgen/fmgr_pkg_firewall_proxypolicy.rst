:source: fmgr_pkg_firewall_proxypolicy.py

:orphan:

.. _fmgr_pkg_firewall_proxypolicy:

fmgr_pkg_firewall_proxypolicy -- Configure proxy policies.
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
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_firewall_proxypolicy</span> - Configure proxy policies. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Accept or deny traffic matching the policy parameters. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [accept, deny, redirect]</span> </li>
 <li><span class="li-head">application-list</span> - Name of an existing Application list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comments</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">disclaimer</span> - Web proxy disclaimer setting: by domain, policy, or user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, domain, policy, user]</span> </li>
 <li><span class="li-head">dlp-sensor</span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr-negate</span> - When enabled, destination addresses match against any address EXCEPT the specified destination addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr6</span> - IPv6 destination address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - Destination interface names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">global-label</span> - Global web-based manager visible label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - Names of group objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-tunnel-auth</span> - Enable/disable HTTP tunnel authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icap-profile</span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-negate</span> - When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">label</span> - VDOM-specific GUI visible label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - Enable/disable logging traffic through the policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - Enable/disable policy log traffic start. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - Name of an existing MMS profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poolname</span> - Name of IP pool object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - Name of profile group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">proxy</span> - Type of explicit proxy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [explicit-web, transparent-web, ftp, wanopt, ssh, ssh-tunnel]</span> </li>
 <li><span class="li-head">redirect-url</span> - Redirect URL for further explicit web proxy processing. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - Authentication replacement message override group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - Enable/disable scanning of connections to Botnet servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">schedule</span> - Name of schedule object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - Name of service objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - When enabled, services match against any service EXCEPT the specified destination services. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address objects (must be set when using Web proxy). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr-negate</span> - When enabled, source addresses match against any address EXCEPT the specified source addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr6</span> - IPv6 source address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - Source interface names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of the policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tags</span> - Names of object-tags applied to address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">transparent</span> - Enable to use the IP address of the client to connect to the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">users</span> - Names of user objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - Enable the use of UTM profiles/sensors/lists. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">waf-profile</span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webcache</span> - Enable/disable web caching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webcache-https</span> - Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webproxy-forward-server</span> - Name of web proxy forward server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webproxy-profile</span> - Name of web proxy profile. <span class="li-normal">type: str</span> </li>
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
    - name: Configure proxy policies.
      fmgr_pkg_firewall_proxypolicy:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         pkg: <your own value>
         state: <value in [present, absent]>
         pkg_firewall_proxypolicy:
            action: <value in [accept, deny, redirect]>
            application-list: <value of string>
            av-profile: <value of string>
            comments: <value of string>
            disclaimer: <value in [disable, domain, policy, ...]>
            dlp-sensor: <value of string>
            dstaddr: <value of string>
            dstaddr-negate: <value in [disable, enable]>
            dstaddr6: <value of string>
            dstintf: <value of string>
            global-label: <value of string>
            groups: <value of string>
            http-tunnel-auth: <value in [disable, enable]>
            icap-profile: <value of string>
            internet-service: <value in [disable, enable]>
            internet-service-custom: <value of string>
            internet-service-id: <value of string>
            internet-service-negate: <value in [disable, enable]>
            ips-sensor: <value of string>
            label: <value of string>
            logtraffic: <value in [disable, all, utm]>
            logtraffic-start: <value in [disable, enable]>
            mms-profile: <value of string>
            policyid: <value of integer>
            poolname: <value of string>
            profile-group: <value of string>
            profile-protocol-options: <value of string>
            profile-type: <value in [single, group]>
            proxy: <value in [explicit-web, transparent-web, ftp, ...]>
            redirect-url: <value of string>
            replacemsg-override-group: <value of string>
            scan-botnet-connections: <value in [disable, block, monitor]>
            schedule: <value of string>
            service: <value of string>
            service-negate: <value in [disable, enable]>
            spamfilter-profile: <value of string>
            srcaddr: <value of string>
            srcaddr-negate: <value in [disable, enable]>
            srcaddr6: <value of string>
            srcintf: <value of string>
            ssl-ssh-profile: <value of string>
            status: <value in [disable, enable]>
            tags: <value of string>
            transparent: <value in [disable, enable]>
            users: <value of string>
            utm-status: <value in [disable, enable]>
            uuid: <value of string>
            waf-profile: <value of string>
            webcache: <value in [disable, enable]>
            webcache-https: <value in [disable, enable]>
            webfilter-profile: <value of string>
            webproxy-forward-server: <value of string>
            webproxy-profile: <value of string>



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



