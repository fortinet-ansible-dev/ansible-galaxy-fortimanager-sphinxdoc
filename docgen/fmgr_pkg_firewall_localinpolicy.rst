:source: fmgr_pkg_firewall_localinpolicy.py

:orphan:

.. _fmgr_pkg_firewall_localinpolicy:

fmgr_pkg_firewall_localinpolicy -- Configure user defined IPv4 local-in policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device.
- Examples include all parameters and values need to be adjusted to data sources before usage.



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
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>pkg_firewall_localinpolicy</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
 <td>yes</td>
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
 <li><span class="li-head">forticloud_access_token</span> - Access token of forticloud managed API users, this option is available with FortiManager later than 6.4.0 <span class="li-normal">type: str</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_firewall_localinpolicy</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action performed on traffic matching the policy (default = deny). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept]</span>  <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>action</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dstaddr</span> - Destination address object from available options. <span class="li-normal">type: str</span>  <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dstaddr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ha-mgmt-intf-only</span> - Enable/disable dedicating the HA management interface only for local-in policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ha-mgmt-intf-only</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">intf</span> - Incoming interface name from available options. <span class="li-normal">type: str</span>  <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>intf</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">policyid</span> - User defined local in policy ID. <span class="li-normal">type: int</span>  <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>policyid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">schedule</span> - Schedule object from available options. <span class="li-normal">type: str</span>  <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>schedule</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">service</span> - Service object from available options. <span class="li-normal">type: str</span>  <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>service</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">srcaddr</span> - Source address object from available options. <span class="li-normal">type: str</span>  <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>srcaddr</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">status</span> - Enable/disable this local-in policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.0.0 </code></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>status</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">comments</span> - Comment. <span class="li-normal">type: str</span>  <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.2.3 </code></td>
 <td><code class="docutils literal notranslate">6.2.5 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>comments</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">6.4.2 </code></td>
 <td><code class="docutils literal notranslate">6.4.5 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>uuid</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">dstaddr-negate</span> - When enabled dstaddr specifies what the destination address must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>dstaddr-negate</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">service-negate</span> - When enabled service specifies what the service must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>service-negate</td>
 <td>True</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">srcaddr-negate</span> - When enabled srcaddr specifies what the source address must NOT be. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>srcaddr-negate</td>
 <td>True</td>
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

 - hosts: fortimanager00
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Configure user defined IPv4 local-in policies.
      fmgr_pkg_firewall_localinpolicy:
         bypass_validation: False
         adom: ansible
         pkg: ansible # package name
         state: present
         pkg_firewall_localinpolicy:
            action: deny #<value in [deny, accept]>
            dstaddr: all
            intf: any
            policyid: 1
            schedule: always
            service: ALL
            srcaddr: all
            status: disable
 - name: gathering fortimanager facts
   hosts: fortimanager00
   gather_facts: no
   connection: httpapi
   collections:
     - fortinet.fortimanager
   vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
   tasks:
    - name: retrieve all the user defined IPv4 local-in policies
      fmgr_fact:
        facts:
            selector: 'pkg_firewall_localinpolicy'
            params:
                adom: 'ansible'
                pkg: 'ansible' # package name
                local-in-policy: 'your_value'


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



