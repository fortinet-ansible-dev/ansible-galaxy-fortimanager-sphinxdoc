:source: fmgr_pkg_firewall_shapingpolicy.py

:orphan:

.. _fmgr_pkg_firewall_shapingpolicy:

fmgr_pkg_firewall_shapingpolicy -- Configure shaping policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>pkg_firewall_shapingpolicy</td>
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
 <li><span class="li-head">pkg_firewall_shapingpolicy</span> - Configure shaping policies. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">app-category</span> - IDs of one or more application categories that this shaper applies application control traffic shaping to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">dstaddr</span> - IPv4 destination address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr6</span> - IPv6 destination address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - One or more outgoing (egress) interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - Apply this traffic shaping policy to user groups that have authenticated with the FortiGate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Shaping policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-version</span> - Apply this traffic shaping policy to IPv4 or IPv6 traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [4, 6]</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - Per-IP traffic shaper to apply with this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule</span> - Schedule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - Service and service group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - IPv4 source address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr6</span> - IPv6 source address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this traffic shaping policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">traffic-shaper</span> - Traffic shaper to apply to traffic forwarded by the firewall policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - Traffic shaper to apply to response traffic received by the firewall policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-category</span> - IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - Apply this traffic shaping policy to individual users that have authenticated with the FortiGate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">app-group</span> - One or more application group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">class-id</span> - Traffic class ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffserv-forward</span> - Enable to change packets DiffServ values to the specified diffservcode-forward value. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffserv-reverse</span> - Enable to change packets reverse (reply) DiffServ values to the specified diffservcode-rev value. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffservcode-forward</span> - Change packets DiffServ to this value. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffservcode-rev</span> - Change packets reverse (reply) DiffServ to this value. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom-group</span> - Custom Internet Service group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-group</span> - Internet Service group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src</span> - Enable/disable use of Internet Services in source for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-src-custom</span> - Custom Internet Service source name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-custom-group</span> - Custom Internet Service source group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-group</span> - Internet Service source group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-id</span> - Internet Service source ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Shaping policy name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - One or more incoming (ingress) interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos</span> - ToS (Type of Service) value used for comparison. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - Non-zero bit positions are used for comparison while zero bit positions are ignored. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-negate</span> - Enable negated TOS match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-name</span> - Internet Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-name</span> - Internet Service source name. <span class="li-normal">type: str</span> </li>
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
    - name: Configure shaping policies.
      fmgr_pkg_firewall_shapingpolicy:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         pkg: <your own value>
         state: <value in [present, absent]>
         pkg_firewall_shapingpolicy:
            app-category: <value of string>
            application: <value of integer>
            dstaddr: <value of string>
            dstaddr6: <value of string>
            dstintf: <value of string>
            groups: <value of string>
            id: <value of integer>
            ip-version: <value in [4, 6]>
            per-ip-shaper: <value of string>
            schedule: <value of string>
            service: <value of string>
            srcaddr: <value of string>
            srcaddr6: <value of string>
            status: <value in [disable, enable]>
            traffic-shaper: <value of string>
            traffic-shaper-reverse: <value of string>
            url-category: <value of string>
            users: <value of string>
            app-group: <value of string>
            class-id: <value of integer>
            comment: <value of string>
            diffserv-forward: <value in [disable, enable]>
            diffserv-reverse: <value in [disable, enable]>
            diffservcode-forward: <value of string>
            diffservcode-rev: <value of string>
            internet-service: <value in [disable, enable]>
            internet-service-custom: <value of string>
            internet-service-custom-group: <value of string>
            internet-service-group: <value of string>
            internet-service-id: <value of string>
            internet-service-src: <value in [disable, enable]>
            internet-service-src-custom: <value of string>
            internet-service-src-custom-group: <value of string>
            internet-service-src-group: <value of string>
            internet-service-src-id: <value of string>
            name: <value of string>
            srcintf: <value of string>
            tos: <value of string>
            tos-mask: <value of string>
            tos-negate: <value in [disable, enable]>
            internet-service-name: <value of string>
            internet-service-src-name: <value of string>



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



