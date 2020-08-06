:source: fmgr_user_ldap.py

:orphan:

.. _fmgr_user_ldap:

fmgr_user_ldap -- Configure LDAP server entries.
++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">user_ldap</span> - Configure LDAP server entries. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">account-key-filter</span> - Account key filter, using the UPN as the search filter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">account-key-processing</span> - Account key processing operation, either keep or strip domain string of UPN in the token. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [same, strip]</span> </li>
 <li><span class="li-head">ca-cert</span> - CA certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cnid</span> - Common name identifier for the LDAP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dn</span> - Distinguished name used to look up entries on the LDAP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">account-key-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">account-key-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">account-key-processing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [same, strip]</span> </li>
 <li><span class="li-head">ca-cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cnid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-member-check</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [user-attr, group-object, posix-group-object]</span> </li>
 <li><span class="li-head">group-object-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-object-search-base</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-search-base</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">member-attr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obtain-user-info</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">password-expiry-warning</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">password-renewal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">retrieve-protection-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">search-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [nested, recursive]</span> </li>
 <li><span class="li-head">secondary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secure</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, starttls, ldaps]</span> </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-identity-check</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">source-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1, TLSv1-1, TLSv1-2, SSLv3]</span> </li>
 <li><span class="li-head">tertiary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [simple, anonymous, regular]</span> </li>
 <li><span class="li-head">user-info-exchange-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">group-filter</span> - Filter used for group matching. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-member-check</span> - Group member checking methods. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [user-attr, group-object, posix-group-object]</span> </li>
 <li><span class="li-head">group-object-filter</span> - Filter used for group searching. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-search-base</span> - Search base used for group searching. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">member-attr</span> - Name of attribute from which to get group membership. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - LDAP server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">password-expiry-warning</span> - Enable/disable password expiry warnings. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">password-renewal</span> - Enable/disable online password renewal. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port</span> - Port to be used for communication with the LDAP server (default = 389). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">secondary-server</span> - Secondary LDAP server CN domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secure</span> - Port to be used for authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, starttls, ldaps]</span> </li>
 <li><span class="li-head">server</span> - LDAP server CN domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-identity-check</span> - Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">source-ip</span> - Source IP for communications to LDAP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1, TLSv1-1, TLSv1-2, SSLv3]</span> </li>
 <li><span class="li-head">tertiary-server</span> - Tertiary LDAP server CN domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Authentication type for LDAP searches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [simple, anonymous, regular]</span> </li>
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
    - name: Configure LDAP server entries.
      fmgr_user_ldap:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_ldap:
            account-key-filter: <value of string>
            account-key-processing: <value in [same, strip]>
            ca-cert: <value of string>
            cnid: <value of string>
            dn: <value of string>
            dynamic_mapping:
              -
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  account-key-filter: <value of string>
                  account-key-name: <value of string>
                  account-key-processing: <value in [same, strip]>
                  ca-cert: <value of string>
                  cnid: <value of string>
                  dn: <value of string>
                  filter: <value of string>
                  group: <value of string>
                  group-filter: <value of string>
                  group-member-check: <value in [user-attr, group-object, posix-group-object]>
                  group-object-filter: <value of string>
                  group-object-search-base: <value of string>
                  group-search-base: <value of string>
                  member-attr: <value of string>
                  obtain-user-info: <value in [disable, enable]>
                  password: <value of string>
                  password-expiry-warning: <value in [disable, enable]>
                  password-renewal: <value in [disable, enable]>
                  port: <value of integer>
                  retrieve-protection-profile: <value of string>
                  search-type:
                    - nested
                    - recursive
                  secondary-server: <value of string>
                  secure: <value in [disable, starttls, ldaps]>
                  server: <value of string>
                  server-identity-check: <value in [disable, enable]>
                  source-ip: <value of string>
                  ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
                  tertiary-server: <value of string>
                  type: <value in [simple, anonymous, regular]>
                  user-info-exchange-server: <value of string>
                  username: <value of string>
            group-filter: <value of string>
            group-member-check: <value in [user-attr, group-object, posix-group-object]>
            group-object-filter: <value of string>
            group-search-base: <value of string>
            member-attr: <value of string>
            name: <value of string>
            password: <value of string>
            password-expiry-warning: <value in [disable, enable]>
            password-renewal: <value in [disable, enable]>
            port: <value of integer>
            secondary-server: <value of string>
            secure: <value in [disable, starttls, ldaps]>
            server: <value of string>
            server-identity-check: <value in [disable, enable]>
            source-ip: <value of string>
            ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
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


