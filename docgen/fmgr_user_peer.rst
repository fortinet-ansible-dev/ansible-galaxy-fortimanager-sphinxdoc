:source: fmgr_user_peer.py

:orphan:

.. _fmgr_user_peer:

fmgr_user_peer -- Configure peer users.
+++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">user_peer</span> - Configure peer users. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">ca</span> - Name of the CA certificate as returned by the execute vpn certificate ca list command. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cn</span> - Peer certificate common name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cn-type</span> - Peer certificate common name type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [string, email, FQDN, ipv4, ipv6]</span> </li>
 <li><span class="li-head">ldap-mode</span> - Mode for LDAP peer authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [password, principal-name]</span> </li>
 <li><span class="li-head">ldap-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">ldap-server</span> - Name of an LDAP server defined under the user ldap command. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ldap-username</span> - Username for LDAP server bind. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mandatory-ca-verify</span> - Determine what happens to the peer if the CA certificate is not installed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Peer name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ocsp-override-server</span> - Online Certificate Status Protocol (OCSP) server for certificate retrieval. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">subject</span> - Peer certificate name constraints. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">two-factor</span> - Enable/disable two-factor authentication, applying certificate and password-based authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure peer users.
      fmgr_user_peer:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_peer:
            ca: <value of string>
            cn: <value of string>
            cn-type: <value in [string, email, FQDN, ...]>
            ldap-mode: <value in [password, principal-name]>
            ldap-password: <value of string>
            ldap-server: <value of string>
            ldap-username: <value of string>
            mandatory-ca-verify: <value in [disable, enable]>
            name: <value of string>
            ocsp-override-server: <value of string>
            passwd: <value of string>
            subject: <value of string>
            two-factor: <value in [disable, enable]>



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



