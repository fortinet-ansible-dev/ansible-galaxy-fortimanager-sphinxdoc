:source: fmgr_firewall_profileprotocoloptions_ftp.py

:orphan:

.. _fmgr_firewall_profileprotocoloptions_ftp:

fmgr_firewall_profileprotocoloptions_ftp -- Configure FTP protocol options.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>firewall_profileprotocoloptions_ftp</td>
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
 <li><span class="li-head">profile-protocol-options</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_profileprotocoloptions_ftp</span> - Configure FTP protocol options. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">comfort-amount</span> - Amount of data to send in a transmission for client comforting (1 - 10240 bytes, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comfort-interval</span> - Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [clientcomfort, no-content-summary, oversize, splice, bypass-rest-command, bypass-mode-command]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-offloaded</span> - SSL decryption and encryption performed by an external device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes]</span> </li>
 <li><span class="li-head">stream-based-uncompressed-limit</span> - Maximum stream-based uncompressed data size that will be scanned (MB, 0 = unlimited (default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-maximum</span> - Maximum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-minimum</span> - Minimum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-size</span> - Set TCP static window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-type</span> - TCP window type to use for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [system, static, dynamic]</span> </li>
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
    - name: Configure FTP protocol options.
      fmgr_firewall_profileprotocoloptions_ftp:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         profile-protocol-options: <your own value>
         firewall_profileprotocoloptions_ftp:
            comfort-amount: <value of integer>
            comfort-interval: <value of integer>
            inspect-all: <value in [disable, enable]>
            options:
              - clientcomfort
              - no-content-summary
              - oversize
              - splice
              - bypass-rest-command
              - bypass-mode-command
            oversize-limit: <value of integer>
            ports: <value of integer>
            scan-bzip2: <value in [disable, enable]>
            status: <value in [disable, enable]>
            uncompressed-nest-limit: <value of integer>
            uncompressed-oversize-limit: <value of integer>
            ssl-offloaded: <value in [no, yes]>
            stream-based-uncompressed-limit: <value of integer>
            tcp-window-maximum: <value of integer>
            tcp-window-minimum: <value of integer>
            tcp-window-size: <value of integer>
            tcp-window-type: <value in [system, static, dynamic]>



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



