:source: fmgr_system_npu_fpanomaly.py

:orphan:

.. _fmgr_system_npu_fpanomaly:

fmgr_system_npu_fpanomaly -- NP6Lite anomaly protection (packet drop or send trap to host).
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>system_npu_fpanomaly</td>
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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">system_npu_fpanomaly</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">esp-minlen-err</span> - Invalid IPv4 ESP short packet anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>esp-minlen-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">icmp-csum-err</span> - Invalid IPv4 ICMP packet checksum anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>icmp-csum-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">icmp-minlen-err</span> - Invalid IPv4 ICMP short packet anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>icmp-minlen-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv4-csum-err</span> - Invalid IPv4 packet checksum anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv4-csum-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv4-ihl-err</span> - Invalid IPv4 header length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv4-ihl-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv4-len-err</span> - Invalid IPv4 packet length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv4-len-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv4-opt-err</span> - Invalid IPv4 option parsing anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv4-opt-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv4-ttlzero-err</span> - Invalid IPv4 TTL field zero anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv4-ttlzero-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv4-ver-err</span> - Invalid IPv4 header version anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv4-ver-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv6-exthdr-len-err</span> - Invalid IPv6 packet chain extension header total length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv6-exthdr-len-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv6-exthdr-order-err</span> - Invalid IPv6 packet extension header ordering anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv6-exthdr-order-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv6-ihl-err</span> - Invalid IPv6 packet length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv6-ihl-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv6-plen-zero</span> - Invalid IPv6 packet payload length zero anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv6-plen-zero</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">ipv6-ver-err</span> - Invalid IPv6 packet version anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>ipv6-ver-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tcp-csum-err</span> - Invalid IPv4 TCP packet checksum anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tcp-csum-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tcp-hlen-err</span> - Invalid IPv4 TCP header length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tcp-hlen-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">tcp-plen-err</span> - Invalid IPv4 TCP packet length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>tcp-plen-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">udp-csum-err</span> - Invalid IPv4 UDP packet checksum anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>udp-csum-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">udp-hlen-err</span> - Invalid IPv4 UDP packet header length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>udp-hlen-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">udp-len-err</span> - Invalid IPv4 UDP packet length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>udp-len-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">udp-plen-err</span> - Invalid IPv4 UDP packet minimum length anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>udp-plen-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">udplite-cover-err</span> - Invalid IPv4 UDP-Lite packet coverage anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>udplite-cover-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">udplite-csum-err</span> - Invalid IPv4 UDP-Lite packet checksum anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>udplite-csum-err</td>
 <td>True</td>
 </tr>
 </table>
 </div>
 </li>
 <li><span class="li-head">unknproto-minlen-err</span> - Invalid IPv4 L4 unknown protocol short packet anomalies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [drop, trap-to-host]</span>  <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <table border="1">
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">7.2.0 </code></td>
 </tr>
 <tr>
 <td>unknproto-minlen-err</td>
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
    - name: no description
      fmgr_system_npu_fpanomaly:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         system_npu_fpanomaly:
            esp-minlen-err: <value in [drop, trap-to-host]>
            icmp-csum-err: <value in [drop, trap-to-host]>
            icmp-minlen-err: <value in [drop, trap-to-host]>
            ipv4-csum-err: <value in [drop, trap-to-host]>
            ipv4-ihl-err: <value in [drop, trap-to-host]>
            ipv4-len-err: <value in [drop, trap-to-host]>
            ipv4-opt-err: <value in [drop, trap-to-host]>
            ipv4-ttlzero-err: <value in [drop, trap-to-host]>
            ipv4-ver-err: <value in [drop, trap-to-host]>
            ipv6-exthdr-len-err: <value in [drop, trap-to-host]>
            ipv6-exthdr-order-err: <value in [drop, trap-to-host]>
            ipv6-ihl-err: <value in [drop, trap-to-host]>
            ipv6-plen-zero: <value in [drop, trap-to-host]>
            ipv6-ver-err: <value in [drop, trap-to-host]>
            tcp-csum-err: <value in [drop, trap-to-host]>
            tcp-hlen-err: <value in [drop, trap-to-host]>
            tcp-plen-err: <value in [drop, trap-to-host]>
            udp-csum-err: <value in [drop, trap-to-host]>
            udp-hlen-err: <value in [drop, trap-to-host]>
            udp-len-err: <value in [drop, trap-to-host]>
            udp-plen-err: <value in [drop, trap-to-host]>
            udplite-cover-err: <value in [drop, trap-to-host]>
            udplite-csum-err: <value in [drop, trap-to-host]>
            unknproto-minlen-err: <value in [drop, trap-to-host]>



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



