:source: fmgr_fmupdate_fdssetting.py

:orphan:

.. _fmgr_fmupdate_fdssetting:

fmgr_fmupdate_fdssetting -- Configure FortiGuard settings.
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
 <td>fmupdate_fdssetting</td>
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
 <li><span class="li-head">fmupdate_fdssetting</span> - Configure FortiGuard settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">User-Agent</span> - Configure the user agent string. <span class="li-normal">type: str</span>  <span class="li-normal">default: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)</span> </li>
 <li><span class="li-head">fds-clt-ssl-protocol</span> - The SSL protocols version for connecting fds server (default = tlsv1. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span>  <span class="li-normal">default: tlsv1.2</span> </li>
 <li><span class="li-head">fds-ssl-protocol</span> - The SSL protocols version for receiving fgt connection (default = tlsv1. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2, tlsv1.3]</span>  <span class="li-normal">default: tlsv1.2</span> </li>
 <li><span class="li-head">fmtr-log</span> - fmtr log level <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> </li>
 <li><span class="li-head">linkd-log</span> - The linkd log level (default = info). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> </li>
 <li><span class="li-head">max-av-ips-version</span> - The maximum number of downloadable, full version AV/IPS packages (1 - 1000, default = 20). <span class="li-normal">type: int</span>  <span class="li-normal">default: 20</span> </li>
 <li><span class="li-head">max-work</span> - The maximum number of worker processing download requests (1 - 32, default = 1). <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">push-override</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">ip</span> - External or virtual IP address of the NAT device that will forward push messages to the FortiManager unit. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">port</span> - Receiving port number on the NAT device (1 - 65535, default = 9443). <span class="li-normal">type: int</span>  <span class="li-normal">default: 9443</span> </li>
 <li><span class="li-head">status</span> - Enable/disable push updates for clients (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 </ul>
 <li><span class="li-head">push-override-to-client</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">announce-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - ID of the announce IP address (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - Announce IPv4 address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">port</span> - Announce IP port (1 - 65535, default = 8890). <span class="li-normal">type: int</span>  <span class="li-normal">default: 8890</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Enable/disable push updates (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 </ul>
 <li><span class="li-head">send_report</span> - send report/fssi to fds server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">send_setup</span> - forward setup to fds server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">server-override</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">servlist</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Override server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip6</span> - IPv6 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::</span> </li>
 <li><span class="li-head">port</span> - Port number to use when contacting FortiGuard (1 - 65535, default = 443). <span class="li-normal">type: int</span>  <span class="li-normal">default: 443</span> </li>
 <li><span class="li-head">service-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [fds, fct]</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Override status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 </ul>
 <li><span class="li-head">system-support-fct</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 6.4, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 6.4, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 6.4]</span> </li>
 <li><span class="li-head">system-support-fgt</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [5.4, 5.6, 6.0, 6.2, 5.4, 5.6, 6.0, 6.2, 6.4, 5.4, 5.6, 6.0, 6.2, 6.4, 7.0, 5.4, 5.6, 6.0, 6.2, 5.4, 5.6, 6.0, 6.2, 6.4, 5.4, 5.6, 6.0, 6.2, 6.4, 7.0, 5.4, 5.6, 6.0, 6.2, 5.4, 5.6, 6.0, 6.2, 6.4, 5.4, 5.6, 6.0, 6.2, 6.4, 7.0]</span> </li>
 <li><span class="li-head">system-support-fml</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [4.x, 5.x, 6.x]</span> </li>
 <li><span class="li-head">system-support-fsa</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [1.x, 2.x, 3.x, 1.x, 2.x, 3.x, 4.x, 1.x, 2.x, 3.x, 1.x, 2.x, 3.x, 1.x, 2.x, 3.x, 4.x, 1.x, 2.x, 3.x, 1.x, 2.x, 3.x, 1.x, 2.x, 3.x, 4.x]</span> </li>
 <li><span class="li-head">system-support-fsw</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 6.4, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 6.4, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 4.x, 5.0, 5.2, 5.4, 5.6, 6.0, 6.2, 6.4]</span> </li>
 <li><span class="li-head">umsvc-log</span> - The um_service log level (default = info). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> </li>
 <li><span class="li-head">unreg-dev-option</span> - set the option for unregister devices <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ignore, svc-only, add-service]</span>  <span class="li-normal">default: add-service</span> </li>
 <li><span class="li-head">update-schedule</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">day</span> - Configure the day the update will occur, if the freqnecy is weekly (Sunday - Saturday, default = Monday). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]</span>  <span class="li-normal">default: Monday</span> </li>
 <li><span class="li-head">frequency</span> - Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [every, daily, weekly]</span>  <span class="li-normal">default: every</span> </li>
 <li><span class="li-head">status</span> - Enable/disable scheduled updates. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">time</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">wanip-query-mode</span> - public ip query mode <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, ipify]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">fortiguard-anycast</span> - Enable/disable use of FortiGuards anycast network <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">fortiguard-anycast-source</span> - Configure which of Fortinets servers to provide FortiGuard services in FortiGuards anycast network. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortinet, aws]</span>  <span class="li-normal">default: fortinet</span> </li>
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
    - name: Configure FortiGuard settings.
      fmgr_fmupdate_fdssetting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         fmupdate_fdssetting:
            User-Agent: <value of string>
            fds-clt-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
            fds-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
            fmtr-log: <value in [emergency, alert, critical, ...]>
            linkd-log: <value in [emergency, alert, critical, ...]>
            max-av-ips-version: <value of integer>
            max-work: <value of integer>
            push-override:
               ip: <value of string>
               port: <value of integer>
               status: <value in [disable, enable]>
            push-override-to-client:
               announce-ip:
                 -
                     id: <value of integer>
                     ip: <value of string>
                     port: <value of integer>
               status: <value in [disable, enable]>
            send_report: <value in [disable, enable]>
            send_setup: <value in [disable, enable]>
            server-override:
               servlist:
                 -
                     id: <value of integer>
                     ip: <value of string>
                     ip6: <value of string>
                     port: <value of integer>
                     service-type:
                       - fds
                       - fct
               status: <value in [disable, enable]>
            system-support-fct:
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
            system-support-fgt:
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 7.0
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 7.0
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 7.0
            system-support-fml:
              - 4.x
              - 5.x
              - 6.x
            system-support-fsa:
              - 1.x
              - 2.x
              - 3.x
              - 1.x
              - 2.x
              - 3.x
              - 4.x
              - 1.x
              - 2.x
              - 3.x
              - 1.x
              - 2.x
              - 3.x
              - 1.x
              - 2.x
              - 3.x
              - 4.x
              - 1.x
              - 2.x
              - 3.x
              - 1.x
              - 2.x
              - 3.x
              - 1.x
              - 2.x
              - 3.x
              - 4.x
            system-support-fsw:
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 4.x
              - 5.0
              - 5.2
              - 5.4
              - 5.6
              - 6.0
              - 6.2
              - 6.4
            umsvc-log: <value in [emergency, alert, critical, ...]>
            unreg-dev-option: <value in [ignore, svc-only, add-service]>
            update-schedule:
               day: <value in [Sunday, Monday, Tuesday, ...]>
               frequency: <value in [every, daily, weekly]>
               status: <value in [disable, enable]>
               time: <value of string>
            wanip-query-mode: <value in [disable, ipify]>
            fortiguard-anycast: <value in [disable, enable]>
            fortiguard-anycast-source: <value in [fortinet, aws]>



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



