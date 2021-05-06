:source: fmgr_system_admin_ldap.py

:orphan:

.. _fmgr_system_admin_ldap:

fmgr_system_admin_ldap -- LDAP server entry configuration.
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
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">system_admin_ldap</span> - LDAP server entry configuration. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom-name</span> - Admin domain names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">adom-attr</span> - Attribute used to retrieve adom <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">attributes</span> - Attributes used for group searching. <span class="li-normal">type: str</span>  <span class="li-normal">default: member,uniquemember,memberuid</span> </li>
 <li><span class="li-head">ca-cert</span> - CA certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cnid</span> - Common Name Identifier (default = CN). <span class="li-normal">type: str</span>  <span class="li-normal">default: cn</span> </li>
 <li><span class="li-head">connect-timeout</span> - LDAP connection timeout (msec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">dn</span> - Distinguished Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - Filter used for group searching. <span class="li-normal">type: str</span>  <span class="li-normal">default: (objectclass=*)</span> </li>
 <li><span class="li-head">group</span> - Full base DN used for group searching. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">memberof-attr</span> - Attribute used to retrieve memeberof. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - LDAP server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">port</span> - Port number of LDAP server (default = 389). <span class="li-normal">type: int</span>  <span class="li-normal">default: 389</span> </li>
 <li><span class="li-head">profile-attr</span> - Attribute used to retrieve admin profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secondary-server</span> - {<name_str|ip_str>} secondary LDAP server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secure</span> - SSL connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, starttls, ldaps]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">server</span> - {<name_str|ip_str>} LDAP server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tertiary-server</span> - {<name_str|ip_str>} tertiary LDAP server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of LDAP binding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [simple, anonymous, regular]</span>  <span class="li-normal">default: simple</span> </li>
 <li><span class="li-head">username</span> - Username (full DN) for initial binding. <span class="li-normal">type: str</span> </li>
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
    - name: LDAP server entry configuration.
      fmgr_system_admin_ldap:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         state: <value in [present, absent]>
         system_admin_ldap:
            adom:
              -
                  adom-name: <value of string>
            adom-attr: <value of string>
            attributes: <value of string>
            ca-cert: <value of string>
            cnid: <value of string>
            connect-timeout: <value of integer>
            dn: <value of string>
            filter: <value of string>
            group: <value of string>
            memberof-attr: <value of string>
            name: <value of string>
            password: <value of string>
            port: <value of integer>
            profile-attr: <value of string>
            secondary-server: <value of string>
            secure: <value in [disable, starttls, ldaps]>
            server: <value of string>
            tertiary-server: <value of string>
            type: <value in [simple, anonymous, regular]>
            username: <value of string>



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



