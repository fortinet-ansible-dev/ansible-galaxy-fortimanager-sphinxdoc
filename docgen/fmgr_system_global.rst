:source: fmgr_system_global.py

:orphan:

.. _fmgr_system_global:

fmgr_system_global -- Global range attributes.
++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">proposed_method</span> - The overridden method of the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">system_global</span> - Global range attributes. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">admin-lockout-duration</span> - Lockout duration(sec) for administration. <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">admin-lockout-threshold</span> - Lockout threshold for administration. <span class="li-normal">type: int</span>  <span class="li-normal">default: 3</span> </li>
 <li><span class="li-head">adom-mode</span> - ADOM mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [normal, advanced]</span>  <span class="li-normal">default: normal</span> </li>
 <li><span class="li-head">adom-rev-auto-delete</span> - Auto delete features for old ADOM revisions. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, by-revisions, by-days]</span>  <span class="li-normal">default: by-revisions</span> </li>
 <li><span class="li-head">adom-rev-max-backup-revisions</span> - Maximum number of ADOM revisions to backup. <span class="li-normal">type: int</span>  <span class="li-normal">default: 5</span> </li>
 <li><span class="li-head">adom-rev-max-days</span> - Number of days to keep old ADOM revisions. <span class="li-normal">type: int</span>  <span class="li-normal">default: 30</span> </li>
 <li><span class="li-head">adom-rev-max-revisions</span> - Maximum number of ADOM revisions to keep. <span class="li-normal">type: int</span>  <span class="li-normal">default: 120</span> </li>
 <li><span class="li-head">adom-select</span> - Enable/disable select ADOM after login. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">adom-status</span> - ADOM status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">clt-cert-req</span> - Require client certificate for GUI login. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, optional]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">console-output</span> - Console output mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [standard, more]</span>  <span class="li-normal">default: standard</span> </li>
 <li><span class="li-head">country-flag</span> - Country flag Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">create-revision</span> - Enable/disable create revision by default. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">daylightsavetime</span> - Enable/disable daylight saving time. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">default-disk-quota</span> - Default disk quota for registered device (MB). <span class="li-normal">type: int</span>  <span class="li-normal">default: 1000</span> </li>
 <li><span class="li-head">detect-unregistered-log-device</span> - Detect unregistered logging device from log message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">device-view-mode</span> - Set devices/groups view mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, tree]</span>  <span class="li-normal">default: regular</span> </li>
 <li><span class="li-head">dh-params</span> - Minimum size of Diffie-Hellman prime for SSH/HTTPS (bits). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1024, 1536, 2048, 3072, 4096, 6144, 8192]</span>  <span class="li-normal">default: 2048</span> </li>
 <li><span class="li-head">disable-module</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [fortiview-noc]</span> </li>
 <li><span class="li-head">enc-algorithm</span> - SSL communication encryption algorithms. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span>  <span class="li-normal">default: high</span> </li>
 <li><span class="li-head">faz-status</span> - FAZ status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">fgfm-local-cert</span> - set the fgfm local certificate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fgfm-ssl-protocol</span> - set the lowest SSL protocols for fgfmsd. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2]</span>  <span class="li-normal">default: tlsv1.2</span> </li>
 <li><span class="li-head">ha-member-auto-grouping</span> - Enable/disable automatically group HA members feature <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">hitcount_concurrent</span> - The number of FortiGates that FortiManager polls at one time (10 - 500, default = 100). <span class="li-normal">type: int</span>  <span class="li-normal">default: 100</span> </li>
 <li><span class="li-head">hitcount_interval</span> - The interval for getting hit count from managed FortiGate devices, in seconds (60 - 86400, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">hostname</span> - System hostname. <span class="li-normal">type: str</span>  <span class="li-normal">default: FMG-VM64</span> </li>
 <li><span class="li-head">import-ignore-addr-cmt</span> - Enable/Disable import ignore of address comments. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">language</span> - System global language. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [english, simch, japanese, korean, spanish, trach]</span>  <span class="li-normal">default: english</span> </li>
 <li><span class="li-head">latitude</span> - fmg location latitude <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ldap-cache-timeout</span> - LDAP browser cache timeout (seconds). <span class="li-normal">type: int</span>  <span class="li-normal">default: 86400</span> </li>
 <li><span class="li-head">ldapconntimeout</span> - LDAP connection timeout (msec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60000</span> </li>
 <li><span class="li-head">lock-preempt</span> - Enable/disable ADOM lock override. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">log-checksum</span> - Record log file hash value, timestamp, and authentication code at transmission or rolling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, md5, md5-auth]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">log-forward-cache-size</span> - Log forwarding disk cache size (GB). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">longitude</span> - fmg location longitude <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-log-forward</span> - Maximum number of log-forward and aggregation settings. <span class="li-normal">type: int</span>  <span class="li-normal">default: 5</span> </li>
 <li><span class="li-head">max-running-reports</span> - Maximum number of reports generating at one time. <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">oftp-ssl-protocol</span> - set the lowest SSL protocols for oftpd. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2]</span>  <span class="li-normal">default: tlsv1.2</span> </li>
 <li><span class="li-head">partial-install</span> - Enable/Disable partial install (install some objects). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">partial-install-force</span> - Enable/Disable partial install when devdb is modified. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">partial-install-rev</span> - Enable/Disable auto creating adom revision for partial install. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">perform-improve-by-ha</span> - Enable/Disable performance improvement by distributing tasks to HA slaves. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">policy-hit-count</span> - show policy hit count. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">policy-object-in-dual-pane</span> - show policies and objects in dual pane. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">pre-login-banner</span> - Enable/disable pre-login banner. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">pre-login-banner-message</span> - Pre-login banner message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remoteauthtimeout</span> - Remote authentication (RADIUS/LDAP) timeout (sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">search-all-adoms</span> - Enable/Disable Search all ADOMs for where-used query. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">ssl-low-encryption</span> - SSL low-grade encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">ssl-protocol</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tlsv1.2, tlsv1.1, tlsv1.0, sslv3]</span> </li>
 <li><span class="li-head">ssl-static-key-ciphers</span> - Enable/disable SSL static key ciphers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">task-list-size</span> - Maximum number of completed tasks to keep. <span class="li-normal">type: int</span>  <span class="li-normal">default: 2000</span> </li>
 <li><span class="li-head">tftp</span> - Enable/disable TFTP in `exec restore image` command (disabled by default in FIPS mode) <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">timezone</span> - Time zone. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]</span>  <span class="li-normal">default: 04</span> </li>
 <li><span class="li-head">tunnel-mtu</span> - Maximum transportation unit(68 - 9000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 1500</span> </li>
 <li><span class="li-head">usg</span> - Enable/disable Fortiguard server restriction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">vdom-mirror</span> - VDOM mirror. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">webservice-proto</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [tlsv1.2, tlsv1.1, tlsv1.0, sslv3, sslv2]</span> </li>
 <li><span class="li-head">workflow-max-sessions</span> - Maximum number of workflow sessions per ADOM (minimum 100). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">workspace-mode</span> - Set workspace mode (ADOM Locking). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, normal, workflow]</span>  <span class="li-normal">default: disabled</span> </li>
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
    - name: Global range attributes.
      fmgr_system_global:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_global:
            admin-lockout-duration: <value of integer>
            admin-lockout-threshold: <value of integer>
            adom-mode: <value in [normal, advanced]>
            adom-rev-auto-delete: <value in [disable, by-revisions, by-days]>
            adom-rev-max-backup-revisions: <value of integer>
            adom-rev-max-days: <value of integer>
            adom-rev-max-revisions: <value of integer>
            adom-select: <value in [disable, enable]>
            adom-status: <value in [disable, enable]>
            clt-cert-req: <value in [disable, enable, optional]>
            console-output: <value in [standard, more]>
            country-flag: <value in [disable, enable]>
            create-revision: <value in [disable, enable]>
            daylightsavetime: <value in [disable, enable]>
            default-disk-quota: <value of integer>
            detect-unregistered-log-device: <value in [disable, enable]>
            device-view-mode: <value in [regular, tree]>
            dh-params: <value in [1024, 1536, 2048, ...]>
            disable-module:
              - fortiview-noc
            enc-algorithm: <value in [low, medium, high]>
            faz-status: <value in [disable, enable]>
            fgfm-local-cert: <value of string>
            fgfm-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
            ha-member-auto-grouping: <value in [disable, enable]>
            hitcount_concurrent: <value of integer>
            hitcount_interval: <value of integer>
            hostname: <value of string>
            import-ignore-addr-cmt: <value in [disable, enable]>
            language: <value in [english, simch, japanese, ...]>
            latitude: <value of string>
            ldap-cache-timeout: <value of integer>
            ldapconntimeout: <value of integer>
            lock-preempt: <value in [disable, enable]>
            log-checksum: <value in [none, md5, md5-auth]>
            log-forward-cache-size: <value of integer>
            longitude: <value of string>
            max-log-forward: <value of integer>
            max-running-reports: <value of integer>
            oftp-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
            partial-install: <value in [disable, enable]>
            partial-install-force: <value in [disable, enable]>
            partial-install-rev: <value in [disable, enable]>
            perform-improve-by-ha: <value in [disable, enable]>
            policy-hit-count: <value in [disable, enable]>
            policy-object-in-dual-pane: <value in [disable, enable]>
            pre-login-banner: <value in [disable, enable]>
            pre-login-banner-message: <value of string>
            remoteauthtimeout: <value of integer>
            search-all-adoms: <value in [disable, enable]>
            ssl-low-encryption: <value in [disable, enable]>
            ssl-protocol:
              - tlsv1.2
              - tlsv1.1
              - tlsv1.0
              - sslv3
            ssl-static-key-ciphers: <value in [disable, enable]>
            task-list-size: <value of integer>
            tftp: <value in [disable, enable]>
            timezone: <value in [00, 01, 02, ...]>
            tunnel-mtu: <value of integer>
            usg: <value in [disable, enable]>
            vdom-mirror: <value in [disable, enable]>
            webservice-proto:
              - tlsv1.2
              - tlsv1.1
              - tlsv1.0
              - sslv3
              - sslv2
            workflow-max-sessions: <value of integer>
            workspace-mode: <value in [disabled, normal, workflow]>



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



