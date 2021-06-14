:source: fmgr_fmupdate_webspam_fgdsetting.py

:orphan:

.. _fmgr_fmupdate_webspam_fgdsetting:

fmgr_fmupdate_webspam_fgdsetting -- Configure the FortiGuard run parameters.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>fmupdate_webspam_fgdsetting</td>
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
 <li><span class="li-head">fmupdate_webspam_fgdsetting</span> - Configure the FortiGuard run parameters. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">as-cache</span> - Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">as-log</span> - Antispam log setting (default = nospam). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, nospam, all]</span>  <span class="li-normal">default: nospam</span> </li>
 <li><span class="li-head">as-preload</span> - Enable/disable preloading antispam database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">av-cache</span> - Antivirus service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">av-log</span> - Antivirus log setting (default = novirus). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, novirus, all]</span>  <span class="li-normal">default: novirus</span> </li>
 <li><span class="li-head">av-preload</span> - Enable/disable preloading antivirus database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">av2-cache</span> - Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 800). <span class="li-normal">type: int</span>  <span class="li-normal">default: 800</span> </li>
 <li><span class="li-head">av2-log</span> - Outbreak prevention log setting (default = noav2). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, noav2, all]</span>  <span class="li-normal">default: noav2</span> </li>
 <li><span class="li-head">av2-preload</span> - Enable/disable preloading outbreak prevention database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">eventlog-query</span> - Enable/disable record query to event-log besides fgd-log (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">fgd-pull-interval</span> - Fgd pull interval setting, in minutes (1 - 1440, default = 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">fq-cache</span> - File query service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">fq-log</span> - File query log setting (default = nofilequery). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, nofilequery, all]</span>  <span class="li-normal">default: nofilequery</span> </li>
 <li><span class="li-head">fq-preload</span> - Enable/disable preloading file query database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">linkd-log</span> - Linkd log setting (default = debug). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: debug</span> </li>
 <li><span class="li-head">max-client-worker</span> - max worker for tcp client connection (0~16: 0 means use cpu number up to 4). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">max-log-quota</span> - Maximum log quota setting, in megabytes (100 - 20480, default = 6144). <span class="li-normal">type: int</span>  <span class="li-normal">default: 6144</span> </li>
 <li><span class="li-head">max-unrated-site</span> - Maximum number of unrated site in memory, in kilobytes(10 - 5120, default = 500). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">restrict-as1-dbver</span> - Restrict system update to indicated antispam(1) database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-as2-dbver</span> - Restrict system update to indicated antispam(2) database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-as4-dbver</span> - Restrict system update to indicated antispam(4) database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-av-dbver</span> - Restrict system update to indicated antivirus database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-av2-dbver</span> - Restrict system update to indicated outbreak prevention database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-fq-dbver</span> - Restrict system update to indicated file query database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-wf-dbver</span> - Restrict system update to indicated web filter database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-override</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">servlist</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Override server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip6</span> - IPv6 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::</span> </li>
 <li><span class="li-head">port</span> - Port number to use when contacting FortiGuard (1 - 65535, default = 443). <span class="li-normal">type: int</span>  <span class="li-normal">default: 443</span> </li>
 <li><span class="li-head">service-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [fgd, fgc, fsa]</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Override status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 </ul>
 <li><span class="li-head">stat-log-interval</span> - Statistic log interval setting, in minutes (1 - 1440, default = 60). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">stat-sync-interval</span> - Synchronization interval for statistic of unrated site in minutes (1 - 60, default = 60). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">update-interval</span> - FortiGuard database update wait time if not enough delta files, in hours (2 - 24, default = 6). <span class="li-normal">type: int</span>  <span class="li-normal">default: 6</span> </li>
 <li><span class="li-head">update-log</span> - Enable/disable update log setting (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">wf-cache</span> - Web filter service maximum memory usage, in megabytes (maximum = Physical memory-1024, 0 = no limit, default = 600). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">wf-dn-cache-expire-time</span> - Web filter DN cache expire time, in minutes (1 - 1440, 0 = never, default = 30). <span class="li-normal">type: int</span>  <span class="li-normal">default: 30</span> </li>
 <li><span class="li-head">wf-dn-cache-max-number</span> - Maximum number of Web filter DN cache (0 = disable, default = 10000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 10000</span> </li>
 <li><span class="li-head">wf-log</span> - Web filter log setting (default = nour1) <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, nourl, all]</span>  <span class="li-normal">default: nourl</span> </li>
 <li><span class="li-head">wf-preload</span> - Enable/disable preloading the web filter database into memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
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
    - name: Configure the FortiGuard run parameters.
      fmgr_fmupdate_webspam_fgdsetting:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         fmupdate_webspam_fgdsetting:
            as-cache: <value of integer>
            as-log: <value in [disable, nospam, all]>
            as-preload: <value in [disable, enable]>
            av-cache: <value of integer>
            av-log: <value in [disable, novirus, all]>
            av-preload: <value in [disable, enable]>
            av2-cache: <value of integer>
            av2-log: <value in [disable, noav2, all]>
            av2-preload: <value in [disable, enable]>
            eventlog-query: <value in [disable, enable]>
            fgd-pull-interval: <value of integer>
            fq-cache: <value of integer>
            fq-log: <value in [disable, nofilequery, all]>
            fq-preload: <value in [disable, enable]>
            linkd-log: <value in [emergency, alert, critical, ...]>
            max-client-worker: <value of integer>
            max-log-quota: <value of integer>
            max-unrated-site: <value of integer>
            restrict-as1-dbver: <value of string>
            restrict-as2-dbver: <value of string>
            restrict-as4-dbver: <value of string>
            restrict-av-dbver: <value of string>
            restrict-av2-dbver: <value of string>
            restrict-fq-dbver: <value of string>
            restrict-wf-dbver: <value of string>
            server-override:
               servlist:
                 -
                     id: <value of integer>
                     ip: <value of string>
                     ip6: <value of string>
                     port: <value of integer>
                     service-type:
                       - fgd
                       - fgc
                       - fsa
               status: <value in [disable, enable]>
            stat-log-interval: <value of integer>
            stat-sync-interval: <value of integer>
            update-interval: <value of integer>
            update-log: <value in [disable, enable]>
            wf-cache: <value of integer>
            wf-dn-cache-expire-time: <value of integer>
            wf-dn-cache-max-number: <value of integer>
            wf-log: <value in [disable, nourl, all]>
            wf-preload: <value in [disable, enable]>



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



