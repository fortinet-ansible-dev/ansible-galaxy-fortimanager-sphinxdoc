:source: fmgr_user_saml.py

:orphan:

.. _fmgr_user_saml:

fmgr_user_saml -- SAML server entry configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>user_saml</td>
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
 <li><span class="li-head">user_saml</span> - SAML server entry configuration. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">cert</span> - Certificate to sign SAML messages. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entity-id</span> - SP entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-name</span> - Group name in assertion statement. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-cert</span> - IDP Certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-entity-id</span> - IDP entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-logout-url</span> - IDP single logout url. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-sign-on-url</span> - IDP single sign-on URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - SAML server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">single-logout-url</span> - SP single logout URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">single-sign-on-url</span> - SP single sign-on URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user-name</span> - User name in assertion statement. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">adfs-claim</span> - Enable/disable ADFS Claim for user/group attribute in assertion statement (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">digest-method</span> - Digest Method Algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sha1, sha256]</span> </li>
 <li><span class="li-head">group-claim-type</span> - Group claim in assertion statement. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [email, given-name, name, upn, common-name, email-adfs-1x, group, upn-adfs-1x, role, sur-name, ppid, name-identifier, authentication-method, deny-only-group-sid, deny-only-primary-sid, deny-only-primary-group-sid, group-sid, primary-group-sid, primary-sid, windows-account-name]</span> </li>
 <li><span class="li-head">limit-relaystate</span> - Enable/disable limiting of relay-state parameter when it exceeds SAML 2. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-claim-type</span> - User name claim in assertion statement. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [email, given-name, name, upn, common-name, email-adfs-1x, group, upn-adfs-1x, role, sur-name, ppid, name-identifier, authentication-method, deny-only-group-sid, deny-only-primary-sid, deny-only-primary-group-sid, group-sid, primary-group-sid, primary-sid, windows-account-name]</span> </li>
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
    - name: SAML server entry configuration.
      fmgr_user_saml:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_saml:
            cert: <value of string>
            entity-id: <value of string>
            group-name: <value of string>
            idp-cert: <value of string>
            idp-entity-id: <value of string>
            idp-single-logout-url: <value of string>
            idp-single-sign-on-url: <value of string>
            name: <value of string>
            single-logout-url: <value of string>
            single-sign-on-url: <value of string>
            user-name: <value of string>
            adfs-claim: <value in [disable, enable]>
            digest-method: <value in [sha1, sha256]>
            group-claim-type: <value in [email, given-name, name, ...]>
            limit-relaystate: <value in [disable, enable]>
            user-claim-type: <value in [email, given-name, name, ...]>



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



