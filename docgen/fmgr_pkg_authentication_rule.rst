:source: fmgr_pkg_authentication_rule.py

:orphan:

.. _fmgr_pkg_authentication_rule:

fmgr_pkg_authentication_rule -- Configure Authentication Rules.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>pkg_authentication_rule</td>
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
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_authentication_rule</span> - Configure Authentication Rules. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">active-auth-method</span> - Select an active authentication method. <span class="li-normal">type: str</span>  <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>active-auth-method</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">comments</span> - Comment. <span class="li-normal">type: str</span>  <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>comments</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ip-based</span> - Enable/disable IP-based authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>ip-based</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">name</span> - Authentication rule name. <span class="li-normal">type: str</span>  <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>name</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">protocol</span> - Select the protocol to use for authentication (default = http). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, ftp, socks, ssh]</span>  <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>protocol</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">srcaddr</span> - Select an IPv4 source address from available options. <span class="li-normal">type: str</span>  <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>srcaddr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">srcaddr6</span> - Select an IPv6 source address. <span class="li-normal">type: str</span>  <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>srcaddr6</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">sso-auth-method</span> - Select a single-sign on (SSO) authentication method. <span class="li-normal">type: str</span>  <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>sso-auth-method</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Enable/disable this authentication rule. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">transaction-based</span> - Enable/disable transaction based authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>transaction-based</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">web-auth-cookie</span> - Enable/disable Web authentication cookies (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>web-auth-cookie</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">web-portal</span> - Enable/disable web portal for proxy transparent policy (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>web-portal</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dstaddr</span> - Select an IPv4 destination address from available options. <span class="li-normal">type: str</span>  <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dstaddr</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dstaddr6</span> - Select an IPv6 destination address from available options. <span class="li-normal">type: str</span>  <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dstaddr6</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">srcintf</span> - Incoming (ingress) interface. <span class="li-normal">type: str</span>  <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>srcintf</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
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
    - name: Configure Authentication Rules.
      fmgr_pkg_authentication_rule:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         pkg: <your own value>
         state: <value in [present, absent]>
         pkg_authentication_rule:
            active-auth-method: <value of string>
            comments: <value of string>
            ip-based: <value in [disable, enable]>
            name: <value of string>
            protocol: <value in [http, ftp, socks, ...]>
            srcaddr: <value of string>
            srcaddr6: <value of string>
            sso-auth-method: <value of string>
            status: <value in [disable, enable]>
            transaction-based: <value in [disable, enable]>
            web-auth-cookie: <value in [disable, enable]>
            web-portal: <value in [disable, enable]>
            dstaddr: <value of string>
            dstaddr6: <value of string>
            srcintf: <value of string>



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



