:source: fmgr_webfilter_profile_antiphish.py

:orphan:

.. _fmgr_webfilter_profile_antiphish:

fmgr_webfilter_profile_antiphish -- AntiPhishing profile.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>webfilter_profile_antiphish</td>
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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">webfilter_profile_antiphish</span> - AntiPhishing profile. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">check-basic-auth</span> - Enable/disable checking of HTTP Basic Auth field for known credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">check-uri</span> - Enable/disable checking of GET URI parameters for known credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">custom-patterns</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Category that the pattern matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [username, password]</span> </li>
 <li><span class="li-head">pattern</span> - Target pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Pattern will be treated either as a regex pattern or literal string. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regex, literal]</span> </li>
 </ul>
 <li><span class="li-head">default-action</span> - Action to be taken when there is no matching rule. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, block, exempt]</span> </li>
 <li><span class="li-head">domain-controller</span> - Domain for which to verify received credentials against. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">inspection-entries</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to be taken upon an AntiPhishing match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, block, exempt]</span> </li>
 <li><span class="li-head">fortiguard-category</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">name</span> - Inspection target name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">max-body-len</span> - Maximum size of a POST body to check for credentials. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Toggle AntiPhishing functionality. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">authentication</span> - Authentication methods. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [domain-controller, ldap]</span> </li>
 <li><span class="li-head">check-username-only</span> - Enable/disable username only matching of credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ldap</span> - LDAP server for which to verify received credentials against. <span class="li-normal">type: str</span> </li>
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
    - name: AntiPhishing profile.
      fmgr_webfilter_profile_antiphish:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         profile: <your own value>
         webfilter_profile_antiphish:
            check-basic-auth: <value in [disable, enable]>
            check-uri: <value in [disable, enable]>
            custom-patterns:
              -
                  category: <value in [username, password]>
                  pattern: <value of string>
                  type: <value in [regex, literal]>
            default-action: <value in [log, block, exempt]>
            domain-controller: <value of string>
            inspection-entries:
              -
                  action: <value in [log, block, exempt]>
                  fortiguard-category: <value of string>
                  name: <value of string>
            max-body-len: <value of integer>
            status: <value in [disable, enable]>
            authentication: <value in [domain-controller, ldap]>
            check-username-only: <value in [disable, enable]>
            ldap: <value of string>



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



