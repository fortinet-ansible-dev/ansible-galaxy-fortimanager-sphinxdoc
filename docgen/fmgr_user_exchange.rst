:source: fmgr_user_exchange.py

:orphan:

.. _fmgr_user_exchange:

fmgr_user_exchange -- Configure MS Exchange server entries.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>user_exchange</td>
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
 <li><span class="li-head">user_exchange</span> - Configure MS Exchange server entries. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">addr-type</span> - Indicate whether the server IP-address is IPv4 or IPv6. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">auth-level</span> - Authentication security level used for the RPC protocol layer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, normal, high, connect, call, packet, integrity, privacy]</span> </li>
 <li><span class="li-head">auth-type</span> - Authentication security type used for the RPC protocol layer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [spnego, ntlm, kerberos]</span> </li>
 <li><span class="li-head">connect-protocol</span> - Connection protocol used to connect to MS Exchange service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rpc-over-tcp, rpc-over-http, rpc-over-https]</span> </li>
 <li><span class="li-head">domain-name</span> - MS Exchange server fully qualified domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-auth-type</span> - Authentication security type used for the HTTP transport. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ntlm, basic]</span> </li>
 <li><span class="li-head">ip</span> - Server IPv4 address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6</span> - Server IPv6 address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">kdc-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">name</span> - MS Exchange server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server-name</span> - MS Exchange server hostname. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - Minimum SSL/TLS protocol version for HTTPS transport (default is to follow system global setting). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1-1, TLSv1-2, SSLv3, TLSv1]</span> </li>
 <li><span class="li-head">username</span> - User name used to sign in to the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auto-discover-kdc</span> - Enable/disable automatic discovery of KDC IP addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure MS Exchange server entries.
      fmgr_user_exchange:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_exchange:
            addr-type: <value in [ipv4, ipv6]>
            auth-level: <value in [low, medium, normal, ...]>
            auth-type: <value in [spnego, ntlm, kerberos]>
            connect-protocol: <value in [rpc-over-tcp, rpc-over-http, rpc-over-https]>
            domain-name: <value of string>
            http-auth-type: <value in [ntlm, basic]>
            ip: <value of string>
            ip6: <value of string>
            kdc-ip: <value of string>
            name: <value of string>
            password: <value of string>
            server-name: <value of string>
            ssl-min-proto-version: <value in [default, TLSv1-1, TLSv1-2, ...]>
            username: <value of string>
            auto-discover-kdc: <value in [disable, enable]>



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



