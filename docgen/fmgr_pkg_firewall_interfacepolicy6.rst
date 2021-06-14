:source: fmgr_pkg_firewall_interfacepolicy6.py

:orphan:

.. _fmgr_pkg_firewall_interfacepolicy6:

fmgr_pkg_firewall_interfacepolicy6 -- Configure IPv6 interface policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>pkg_firewall_interfacepolicy6</td>
 <td>yes</td>
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
 <li><span class="li-head">pkg_firewall_interfacepolicy6</span> - Configure IPv6 interface policies. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">address-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">application-list</span> - Application list name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application-list-status</span> - Enable/disable application control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-profile</span> - Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile-status</span> - Enable/disable antivirus. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comments</span> - Comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - DLP sensor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor-status</span> - Enable/disable DLP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dsri</span> - Enable/disable DSRI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr6</span> - IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface</span> - Monitored interface name from available interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips-sensor</span> - IPS sensor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips-sensor-status</span> - Enable/disable IPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">label</span> - Label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - Logging type to be used in this policy (Options: all | utm | disable, Default: utm). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - Enable/disable scanning for connections to Botnet servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">service6</span> - Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Antispam profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spamfilter-profile-status</span> - Enable/disable antispam. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr6</span> - IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile-status</span> - Enable/disable web filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">emailfilter-profile</span> - Email filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">emailfilter-profile-status</span> - Enable/disable email filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure IPv6 interface policies.
      fmgr_pkg_firewall_interfacepolicy6:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         pkg: <your own value>
         state: <value in [present, absent]>
         pkg_firewall_interfacepolicy6:
            address-type: <value in [ipv4, ipv6]>
            application-list: <value of string>
            application-list-status: <value in [disable, enable]>
            av-profile: <value of string>
            av-profile-status: <value in [disable, enable]>
            comments: <value of string>
            dlp-sensor: <value of string>
            dlp-sensor-status: <value in [disable, enable]>
            dsri: <value in [disable, enable]>
            dstaddr6: <value of string>
            interface: <value of string>
            ips-sensor: <value of string>
            ips-sensor-status: <value in [disable, enable]>
            label: <value of string>
            logtraffic: <value in [disable, all, utm]>
            policyid: <value of integer>
            scan-botnet-connections: <value in [disable, block, monitor]>
            service6: <value of string>
            spamfilter-profile: <value of string>
            spamfilter-profile-status: <value in [disable, enable]>
            srcaddr6: <value of string>
            status: <value in [disable, enable]>
            webfilter-profile: <value of string>
            webfilter-profile-status: <value in [disable, enable]>
            emailfilter-profile: <value of string>
            emailfilter-profile-status: <value in [disable, enable]>



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



