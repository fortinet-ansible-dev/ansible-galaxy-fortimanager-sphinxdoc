:source: fmgr_devprof_system_global.py

:orphan:

.. _fmgr_devprof_system_global:

fmgr_devprof_system_global -- Configure global attributes.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof_system_global</span> - Configure global attributes. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">admin-https-redirect</span> - Enable/disable redirection of HTTP administration access to HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">admin-port</span> - Administrative access port for HTTP. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admin-scp</span> - Enable/disable using SCP to download the system configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">admin-sport</span> - Administrative access port for HTTPS. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admin-ssh-port</span> - Administrative access port for SSH. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admin-ssh-v1</span> - Enable/disable SSH v1 compatibility. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">admin-telnet-port</span> - Administrative access port for TELNET. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admintimeout</span> - Number of minutes before an idle administrator session times out (5 - 480 minutes (8 hours), default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gui-ipv6</span> - Enable/disable IPv6 settings on the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gui-lines-per-page</span> - Number of lines to display per page for web administration. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gui-theme</span> - Color scheme for the administration GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [blue, green, melongene, red, mariner]</span> </li>
 <li><span class="li-head">language</span> - GUI display language. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [english, simch, japanese, korean, spanish, trach, french, portuguese]</span> </li>
 <li><span class="li-head">switch-controller</span> - Enable/disable switch controller feature. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure global attributes.
      fmgr_devprof_system_global:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         devprof_system_global:
            admin-https-redirect: <value in [disable, enable]>
            admin-port: <value of integer>
            admin-scp: <value in [disable, enable]>
            admin-sport: <value of integer>
            admin-ssh-port: <value of integer>
            admin-ssh-v1: <value in [disable, enable]>
            admin-telnet-port: <value of integer>
            admintimeout: <value of integer>
            gui-ipv6: <value in [disable, enable]>
            gui-lines-per-page: <value of integer>
            gui-theme: <value in [blue, green, melongene, ...]>
            language: <value in [english, simch, japanese, ...]>
            switch-controller: <value in [disable, enable]>



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



