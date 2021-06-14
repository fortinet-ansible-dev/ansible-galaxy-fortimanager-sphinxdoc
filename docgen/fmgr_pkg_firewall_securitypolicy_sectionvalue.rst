:source: fmgr_pkg_firewall_securitypolicy_sectionvalue.py

:orphan:

.. _fmgr_pkg_firewall_securitypolicy_sectionvalue:

fmgr_pkg_firewall_securitypolicy_sectionvalue -- Configure NGFW IPv4/IPv6 application policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>pkg_firewall_securitypolicy_sectionvalue</td>
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
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">security-policy</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_firewall_securitypolicy_sectionvalue</span> - Configure NGFW IPv4/IPv6 application policies. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Policy action (accept/deny). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept]</span> </li>
 <li><span class="li-head">app-category</span> - Application category ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">app-group</span> - Application group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">application-list</span> - Name of an existing Application list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cifs-profile</span> - Name of an existing CIFS profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comments</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dnsfilter-profile</span> - Name of an existing DNS filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr4</span> - Destination IPv4 address name and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr6</span> - Destination IPv6 address name and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - Outgoing (egress) interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">emailfilter-profile</span> - Name of an existing email filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">enforce-default-app-port</span> - Enable/disable default application port enforcement for allowed applications. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - Names of user groups that can authenticate with this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">icap-profile</span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom-group</span> - Custom Internet Service group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-group</span> - Internet Service group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-negate</span> - When enabled internet-service specifies what the service must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-src</span> - Enable/disable use of Internet Services in source for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-src-custom</span> - Custom Internet Service source name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-custom-group</span> - Custom Internet Service source group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-group</span> - Internet Service source group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-id</span> - Internet Service source ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-negate</span> - When enabled internet-service-src specifies what the service must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - Enable or disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - Record logs when a session starts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - Name of an existing MMS profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Policy name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">profile-group</span> - Name of profile group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">schedule</span> - Schedule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - Service and service group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - When enabled service specifies what the service must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr4</span> - Source IPv4 address name and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr6</span> - Source IPv6 address name and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - Incoming (ingress) interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-filter-profile</span> - Name of an existing SSH filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable or disable this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">url-category</span> - URL category ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - Names of individual users that can authenticate with this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - Enable security profiles. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">voip-profile</span> - Name of an existing VoIP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination IPv4 address name and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fsso-groups</span> - Names of FSSO groups. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">global-label</span> - Label for the policy that appears when the GUI is in Global View mode. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-name</span> - Internet Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-name</span> - Internet Service source name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">send-deny-packet</span> - Enable to send a reply when a session is denied or blocked by a firewall policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr</span> - Source IPv4 address name and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr-negate</span> - When enabled dstaddr/dstaddr6 specifies what the destination address must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">file-filter-profile</span> - Name of an existing file-filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">learning-mode</span> - Enable to allow everything, but log all of the meaningful data for security information gathering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr-negate</span> - When enabled srcaddr/srcaddr6 specifies what the source address must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">videofilter-profile</span> - Name of an existing VideoFilter profile. <span class="li-normal">type: str</span> </li>
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
    - name: Configure NGFW IPv4/IPv6 application policies.
      fmgr_pkg_firewall_securitypolicy_sectionvalue:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         pkg: <your own value>
         security-policy: <your own value>
         state: <value in [present, absent]>
         pkg_firewall_securitypolicy_sectionvalue:
            action: <value in [deny, accept]>
            app-category: <value of string>
            app-group: <value of string>
            application: <value of integer>
            application-list: <value of string>
            av-profile: <value of string>
            cifs-profile: <value of string>
            comments: <value of string>
            dlp-sensor: <value of string>
            dnsfilter-profile: <value of string>
            dstaddr4: <value of string>
            dstaddr6: <value of string>
            dstintf: <value of string>
            emailfilter-profile: <value of string>
            enforce-default-app-port: <value in [disable, enable]>
            groups: <value of string>
            icap-profile: <value of string>
            internet-service: <value in [disable, enable]>
            internet-service-custom: <value of string>
            internet-service-custom-group: <value of string>
            internet-service-group: <value of string>
            internet-service-id: <value of string>
            internet-service-negate: <value in [disable, enable]>
            internet-service-src: <value in [disable, enable]>
            internet-service-src-custom: <value of string>
            internet-service-src-custom-group: <value of string>
            internet-service-src-group: <value of string>
            internet-service-src-id: <value of string>
            internet-service-src-negate: <value in [disable, enable]>
            ips-sensor: <value of string>
            logtraffic: <value in [disable, all, utm]>
            logtraffic-start: <value in [disable, enable]>
            mms-profile: <value of string>
            name: <value of string>
            policyid: <value of integer>
            profile-group: <value of string>
            profile-protocol-options: <value of string>
            profile-type: <value in [single, group]>
            schedule: <value of string>
            service: <value of string>
            service-negate: <value in [disable, enable]>
            srcaddr4: <value of string>
            srcaddr6: <value of string>
            srcintf: <value of string>
            ssh-filter-profile: <value of string>
            ssl-ssh-profile: <value of string>
            status: <value in [disable, enable]>
            url-category: <value of string>
            users: <value of string>
            utm-status: <value in [disable, enable]>
            uuid: <value of string>
            voip-profile: <value of string>
            webfilter-profile: <value of string>
            dstaddr: <value of string>
            fsso-groups: <value of string>
            global-label: <value of string>
            internet-service-name: <value of string>
            internet-service-src-name: <value of string>
            send-deny-packet: <value in [disable, enable]>
            srcaddr: <value of string>
            dstaddr-negate: <value in [disable, enable]>
            file-filter-profile: <value of string>
            learning-mode: <value in [disable, enable]>
            srcaddr-negate: <value in [disable, enable]>
            videofilter-profile: <value of string>



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



