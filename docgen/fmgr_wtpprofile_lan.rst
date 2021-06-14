:source: fmgr_wtpprofile_lan.py

:orphan:

.. _fmgr_wtpprofile_lan:

fmgr_wtpprofile_lan -- WTP LAN port mapping.
++++++++++++++++++++++++++++++++++++++++++++

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
 <td>wtpprofile_lan</td>
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
 <li><span class="li-head">wtp-profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">wtpprofile_lan</span> - WTP LAN port mapping. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">port-mode</span> - LAN port mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port-ssid</span> - Bridge LAN port to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port1-mode</span> - LAN port 1 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port1-ssid</span> - Bridge LAN port 1 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port2-mode</span> - LAN port 2 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port2-ssid</span> - Bridge LAN port 2 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port3-mode</span> - LAN port 3 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port3-ssid</span> - Bridge LAN port 3 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port4-mode</span> - LAN port 4 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port4-ssid</span> - Bridge LAN port 4 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port5-mode</span> - LAN port 5 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port5-ssid</span> - Bridge LAN port 5 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port6-mode</span> - LAN port 6 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port6-ssid</span> - Bridge LAN port 6 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port7-mode</span> - LAN port 7 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port7-ssid</span> - Bridge LAN port 7 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port8-mode</span> - LAN port 8 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port8-ssid</span> - Bridge LAN port 8 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-esl-mode</span> - ESL port mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port-esl-ssid</span> - Bridge ESL port to SSID. <span class="li-normal">type: str</span> </li>
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
    - name: WTP LAN port mapping.
      fmgr_wtpprofile_lan:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         wtp-profile: <your own value>
         wtpprofile_lan:
            port-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port-ssid: <value of string>
            port1-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port1-ssid: <value of string>
            port2-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port2-ssid: <value of string>
            port3-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port3-ssid: <value of string>
            port4-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port4-ssid: <value of string>
            port5-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port5-ssid: <value of string>
            port6-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port6-ssid: <value of string>
            port7-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port7-ssid: <value of string>
            port8-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port8-ssid: <value of string>
            port-esl-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port-esl-ssid: <value of string>



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



