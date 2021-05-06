:source: fmgr_user_group.py

:orphan:

.. _fmgr_user_group:

fmgr_user_group -- Configure user groups.
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



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method of the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">user_group</span> - Configure user groups. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">auth-concurrent-override</span> - Enable/disable overriding the global number of concurrent authentication sessions for this user group. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-concurrent-value</span> - Maximum number of concurrent authenticated connections per user (0 - 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">authtimeout</span> - Authentication timeout in minutes for this user group. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">company</span> - Set the action for the company guest user field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [optional, mandatory, disabled]</span> </li>
 <li><span class="li-head">email</span> - Enable/disable the guest user email address field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">expire</span> - Time in seconds before guest user accounts expire. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">expire-type</span> - Determine when the expiration countdown begins. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [immediately, first-successful-login]</span> </li>
 <li><span class="li-head">group-type</span> - Set the group to be for firewall authentication, FSSO, RSSO, or guest users. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [firewall, directory-service, fsso-service, guest, rsso]</span> </li>
 <li><span class="li-head">guest</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">company</span> - Set the action for the company guest user field. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">email</span> - Email. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">expiration</span> - Expire time. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mobile-phone</span> - Mobile phone. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Guest name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sponsor</span> - Set the action for the sponsor guest user field. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user-id</span> - Guest ID. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">http-digest-realm</span> - Realm attribute for MD5-digest authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Group ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">match</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_gui_meta</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-name</span> - Name of matching group on remote authentication server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server-name</span> - Name of remote auth server. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">max-accounts</span> - Maximum number of guest accounts that can be created for this group (0 means unlimited). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">member</span> - Names of users, peers, LDAP severs, or RADIUS servers to add to the user group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mobile-phone</span> - Enable/disable the guest user mobile phone number field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">multiple-guest-add</span> - Enable/disable addition of multiple guests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - Guest user password type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto-generate, specify, disable]</span> </li>
 <li><span class="li-head">sms-custom-server</span> - SMS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-server</span> - Send SMS through FortiGuard or other external server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortiguard, custom]</span> </li>
 <li><span class="li-head">sponsor</span> - Set the action for the sponsor guest user field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [optional, mandatory, disabled]</span> </li>
 <li><span class="li-head">sso-attribute-value</span> - Name of the RADIUS user group that this local user group represents. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user-id</span> - Guest user ID type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [email, auto-generate, specify]</span> </li>
 <li><span class="li-head">user-name</span> - Enable/disable the guest user name entry. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure user groups.
      fmgr_user_group:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_group:
            auth-concurrent-override: <value in [disable, enable]>
            auth-concurrent-value: <value of integer>
            authtimeout: <value of integer>
            company: <value in [optional, mandatory, disabled]>
            email: <value in [disable, enable]>
            expire: <value of integer>
            expire-type: <value in [immediately, first-successful-login]>
            group-type: <value in [firewall, directory-service, fsso-service, ...]>
            guest:
              -
                  comment: <value of string>
                  company: <value of string>
                  email: <value of string>
                  expiration: <value of string>
                  mobile-phone: <value of string>
                  name: <value of string>
                  password: <value of string>
                  sponsor: <value of string>
                  user-id: <value of string>
            http-digest-realm: <value of string>
            id: <value of integer>
            match:
              -
                  _gui_meta: <value of string>
                  group-name: <value of string>
                  id: <value of integer>
                  server-name: <value of string>
            max-accounts: <value of integer>
            member: <value of string>
            mobile-phone: <value in [disable, enable]>
            multiple-guest-add: <value in [disable, enable]>
            name: <value of string>
            password: <value in [auto-generate, specify, disable]>
            sms-custom-server: <value of string>
            sms-server: <value in [fortiguard, custom]>
            sponsor: <value in [optional, mandatory, disabled]>
            sso-attribute-value: <value of string>
            user-id: <value in [email, auto-generate, specify]>
            user-name: <value in [disable, enable]>



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



