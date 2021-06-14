:source: fmgr_user_local.py

:orphan:

.. _fmgr_user_local:

fmgr_user_local -- Configure local users.
+++++++++++++++++++++++++++++++++++++++++

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
 <td>user_local</td>
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
 <li><span class="li-head">user_local</span> - Configure local users. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">auth-concurrent-override</span> - Enable/disable overriding the policy-auth-concurrent under config system global. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-concurrent-value</span> - Maximum number of concurrent logins permitted from the same user. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">authtimeout</span> - Time in minutes before the authentication timeout for a user is reached. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">email-to</span> - Two-factor recipients email address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortitoken</span> - Two-factor recipients FortiToken serial number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - User ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldap-server</span> - Name of LDAP server with which the user must authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - User name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">passwd-policy</span> - Password policy to apply to this user, as defined in config user password-policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ppk-identity</span> - IKEv2 Postquantum Preshared Key Identity. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ppk-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">radius-server</span> - Name of RADIUS server with which the user must authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-custom-server</span> - Two-factor recipients SMS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-phone</span> - Two-factor recipients mobile phone number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-server</span> - Send SMS through FortiGuard or other external server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortiguard, custom]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable allowing the local user to authenticate with the FortiGate unit. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tacacs+-server</span> - Name of TACACS+ server with which the user must authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">two-factor</span> - Enable/disable two-factor authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, fortitoken, email, sms, fortitoken-cloud]</span> </li>
 <li><span class="li-head">type</span> - Authentication method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [password, radius, tacacs+, ldap]</span> </li>
 <li><span class="li-head">workstation</span> - Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">two-factor-authentication</span> - Authentication method by FortiToken Cloud. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortitoken, email, sms]</span> </li>
 <li><span class="li-head">two-factor-notification</span> - Notification method for user activation by FortiToken Cloud. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [email, sms]</span> </li>
 <li><span class="li-head">username-case-insensitivity</span> - Enable/disable case sensitivity when performing username matching (uppercase and lowercase letters are treated either as distinct or equivalent). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">username-case-sensitivity</span> - Enable/disable case sensitivity when performing username matching (uppercase and lowercase letters are treated either as distinct or equivalent). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure local users.
      fmgr_user_local:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_local:
            auth-concurrent-override: <value in [disable, enable]>
            auth-concurrent-value: <value of integer>
            authtimeout: <value of integer>
            email-to: <value of string>
            fortitoken: <value of string>
            id: <value of integer>
            ldap-server: <value of string>
            name: <value of string>
            passwd: <value of string>
            passwd-policy: <value of string>
            ppk-identity: <value of string>
            ppk-secret: <value of string>
            radius-server: <value of string>
            sms-custom-server: <value of string>
            sms-phone: <value of string>
            sms-server: <value in [fortiguard, custom]>
            status: <value in [disable, enable]>
            tacacs+-server: <value of string>
            two-factor: <value in [disable, fortitoken, email, ...]>
            type: <value in [password, radius, tacacs+, ...]>
            workstation: <value of string>
            two-factor-authentication: <value in [fortitoken, email, sms]>
            two-factor-notification: <value in [email, sms]>
            username-case-insensitivity: <value in [disable, enable]>
            username-case-sensitivity: <value in [disable, enable]>



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



