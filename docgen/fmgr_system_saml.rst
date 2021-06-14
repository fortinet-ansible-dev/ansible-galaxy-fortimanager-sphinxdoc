:source: fmgr_system_saml.py

:orphan:

.. _fmgr_system_saml:

fmgr_system_saml -- Global settings for SAML authentication.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>system_saml</td>
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
 <li><span class="li-head">system_saml</span> - Global settings for SAML authentication. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">acs-url</span> - SP ACS(login) URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cert</span> - Certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entity-id</span> - SP entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-cert</span> - IDP Certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-entity-id</span> - IDP entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-logout-url</span> - IDP single logout url. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-sign-on-url</span> - IDP single sign-on URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">login-auto-redirect</span> - Enable/Disable auto redirect to IDP login page. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">role</span> - SAML role. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [IDP, SP, FAB-SP]</span>  <span class="li-normal">default: SP</span> </li>
 <li><span class="li-head">server-address</span> - server address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-providers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">idp-entity-id</span> - IDP Entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-logout-url</span> - IDP single logout url. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-sign-on-url</span> - IDP single sign-on URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">prefix</span> - Prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-cert</span> - SP certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-entity-id</span> - SP Entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-single-logout-url</span> - SP single logout URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-single-sign-on-url</span> - SP single sign-on URL. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sls-url</span> - SP SLS(logout) URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SAML authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">default-profile</span> - Default Profile Name. <span class="li-normal">type: str</span>  <span class="li-normal">default: Restricted_User</span> </li>
 <li><span class="li-head">fabric-idp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dev-id</span> - IDP Device ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-cert</span> - IDP Certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-entity-id</span> - IDP entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-logout-url</span> - IDP single logout url. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-sign-on-url</span> - IDP single sign-on URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-status</span> - Enable/disable SAML authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 </ul>
 <li><span class="li-head">forticloud-sso</span> - Enable/disable FortiCloud SSO (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
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
    - name: Global settings for SAML authentication.
      fmgr_system_saml:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_saml:
            acs-url: <value of string>
            cert: <value of string>
            entity-id: <value of string>
            idp-cert: <value of string>
            idp-entity-id: <value of string>
            idp-single-logout-url: <value of string>
            idp-single-sign-on-url: <value of string>
            login-auto-redirect: <value in [disable, enable]>
            role: <value in [IDP, SP, FAB-SP]>
            server-address: <value of string>
            service-providers:
              -
                  idp-entity-id: <value of string>
                  idp-single-logout-url: <value of string>
                  idp-single-sign-on-url: <value of string>
                  name: <value of string>
                  prefix: <value of string>
                  sp-cert: <value of string>
                  sp-entity-id: <value of string>
                  sp-single-logout-url: <value of string>
                  sp-single-sign-on-url: <value of string>
            sls-url: <value of string>
            status: <value in [disable, enable]>
            default-profile: <value of string>
            fabric-idp:
              -
                  dev-id: <value of string>
                  idp-cert: <value of string>
                  idp-entity-id: <value of string>
                  idp-single-logout-url: <value of string>
                  idp-single-sign-on-url: <value of string>
                  idp-status: <value in [disable, enable]>
            forticloud-sso: <value in [disable, enable]>



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



