:source: fmgr_waf_profile_constraint.py

:orphan:

.. _fmgr_waf_profile_constraint:

fmgr_waf_profile_constraint -- WAF HTTP protocol restrictions.
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
 <td>waf_profile_constraint</td>
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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">waf_profile_constraint</span> - WAF HTTP protocol restrictions. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">content-length</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Length of HTTP content in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">exception</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">address</span> - Host address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">content-length</span> - HTTP content length in request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header-length</span> - HTTP header length in request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hostname</span> - Enable/disable hostname check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - Exception ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">line-length</span> - HTTP line length in request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">malformed</span> - Enable/disable malformed HTTP request check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-cookie</span> - Maximum number of cookies in HTTP request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-header-line</span> - Maximum number of HTTP header line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-range-segment</span> - Maximum number of range segments in HTTP range line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-url-param</span> - Maximum number of parameters in URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">method</span> - Enable/disable HTTP method check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">param-length</span> - Maximum length of parameter in URL, HTTP POST request or HTTP body. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pattern</span> - URL pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">regex</span> - Enable/disable regular expression based pattern match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">url-param-length</span> - Maximum length of parameter in URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">version</span> - Enable/disable HTTP version check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">header-length</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Length of HTTP header in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">hostname</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">line-length</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Length of HTTP line in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">malformed</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">max-cookie</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-cookie</span> - Maximum number of cookies in HTTP request (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">max-header-line</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-header-line</span> - Maximum number HTTP header lines (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">max-range-segment</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-range-segment</span> - Maximum number of range segments in HTTP range line (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">max-url-param</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-url-param</span> - Maximum number of parameters in URL (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">method</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">param-length</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">url-param-length</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Maximum length of URL parameter in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">version</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
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
    - name: WAF HTTP protocol restrictions.
      fmgr_waf_profile_constraint:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         profile: <your own value>
         waf_profile_constraint:
            content-length:
               action: <value in [allow, block]>
               length: <value of integer>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            exception:
              -
                  address: <value of string>
                  content-length: <value in [disable, enable]>
                  header-length: <value in [disable, enable]>
                  hostname: <value in [disable, enable]>
                  id: <value of integer>
                  line-length: <value in [disable, enable]>
                  malformed: <value in [disable, enable]>
                  max-cookie: <value in [disable, enable]>
                  max-header-line: <value in [disable, enable]>
                  max-range-segment: <value in [disable, enable]>
                  max-url-param: <value in [disable, enable]>
                  method: <value in [disable, enable]>
                  param-length: <value in [disable, enable]>
                  pattern: <value of string>
                  regex: <value in [disable, enable]>
                  url-param-length: <value in [disable, enable]>
                  version: <value in [disable, enable]>
            header-length:
               action: <value in [allow, block]>
               length: <value of integer>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            hostname:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            line-length:
               action: <value in [allow, block]>
               length: <value of integer>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            malformed:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            max-cookie:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               max-cookie: <value of integer>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            max-header-line:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               max-header-line: <value of integer>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            max-range-segment:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               max-range-segment: <value of integer>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            max-url-param:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               max-url-param: <value of integer>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            method:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            param-length:
               action: <value in [allow, block]>
               length: <value of integer>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            url-param-length:
               action: <value in [allow, block]>
               length: <value of integer>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>
            version:
               action: <value in [allow, block]>
               log: <value in [disable, enable]>
               severity: <value in [low, medium, high]>
               status: <value in [disable, enable]>



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



