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

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/global`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">parameters for method: [get]</span> - Global range attributes.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Global range attributes.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 <li><span class="li-head">disable-module</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortiview-noc]</span> </li>
 </ul>
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
 <li><span class="li-head">ssl-protocol</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tlsv1.2, tlsv1.1, tlsv1.0, sslv3]</span> </li>
 </ul>
 <li><span class="li-head">ssl-static-key-ciphers</span> - Enable/disable SSL static key ciphers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">task-list-size</span> - Maximum number of completed tasks to keep. <span class="li-normal">type: int</span>  <span class="li-normal">default: 2000</span> </li>
 <li><span class="li-head">tftp</span> - Enable/disable TFTP in `exec restore image` command (disabled by default in FIPS mode) <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">timezone</span> - Time zone. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]</span>  <span class="li-normal">default: 04</span> </li>
 <li><span class="li-head">tunnel-mtu</span> - Maximum transportation unit(68 - 9000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 1500</span> </li>
 <li><span class="li-head">usg</span> - Enable/disable Fortiguard server restriction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">vdom-mirror</span> - VDOM mirror. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">webservice-proto</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tlsv1.2, tlsv1.1, tlsv1.0, sslv3, sslv2]</span> </li>
 </ul>
 <li><span class="li-head">workflow-max-sessions</span> - Maximum number of workflow sessions per ADOM (minimum 100). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">workspace-mode</span> - Set workspace mode (ADOM Locking). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, normal, workflow]</span>  <span class="li-normal">default: disabled</span> </li>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

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

    - name: REQUESTING /CLI/SYSTEM/GLOBAL
      fmgr_system_global:
         method: <value in [set, update]>
         params:
            -
               data:
                  admin-lockout-duration: <value of integer default: 60>
                  admin-lockout-threshold: <value of integer default: 3>
                  adom-mode: <value in [normal, advanced] default: 'normal'>
                  adom-rev-auto-delete: <value in [disable, by-revisions, by-days] default: 'by-revisions'>
                  adom-rev-max-backup-revisions: <value of integer default: 5>
                  adom-rev-max-days: <value of integer default: 30>
                  adom-rev-max-revisions: <value of integer default: 120>
                  adom-select: <value in [disable, enable] default: 'enable'>
                  adom-status: <value in [disable, enable] default: 'disable'>
                  clt-cert-req: <value in [disable, enable, optional] default: 'disable'>
                  console-output: <value in [standard, more] default: 'standard'>
                  country-flag: <value in [disable, enable] default: 'enable'>
                  create-revision: <value in [disable, enable] default: 'disable'>
                  daylightsavetime: <value in [disable, enable] default: 'enable'>
                  default-disk-quota: <value of integer default: 1000>
                  detect-unregistered-log-device: <value in [disable, enable] default: 'enable'>
                  device-view-mode: <value in [regular, tree] default: 'regular'>
                  dh-params: <value in [1024, 1536, 2048, ...] default: '2048'>
                  disable-module:
                    - <value in [fortiview-noc]>
                  enc-algorithm: <value in [low, medium, high] default: 'high'>
                  faz-status: <value in [disable, enable] default: 'disable'>
                  fgfm-local-cert: <value of string>
                  fgfm-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...] default: 'tlsv1.2'>
                  ha-member-auto-grouping: <value in [disable, enable] default: 'enable'>
                  hitcount_concurrent: <value of integer default: 100>
                  hitcount_interval: <value of integer default: 300>
                  hostname: <value of string default: 'FMG-VM64'>
                  import-ignore-addr-cmt: <value in [disable, enable] default: 'disable'>
                  language: <value in [english, simch, japanese, ...] default: 'english'>
                  latitude: <value of string>
                  ldap-cache-timeout: <value of integer default: 86400>
                  ldapconntimeout: <value of integer default: 60000>
                  lock-preempt: <value in [disable, enable] default: 'disable'>
                  log-checksum: <value in [none, md5, md5-auth] default: 'none'>
                  log-forward-cache-size: <value of integer default: 0>
                  longitude: <value of string>
                  max-log-forward: <value of integer default: 5>
                  max-running-reports: <value of integer default: 1>
                  oftp-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...] default: 'tlsv1.2'>
                  partial-install: <value in [disable, enable] default: 'disable'>
                  partial-install-force: <value in [disable, enable] default: 'disable'>
                  partial-install-rev: <value in [disable, enable] default: 'disable'>
                  perform-improve-by-ha: <value in [disable, enable] default: 'disable'>
                  policy-hit-count: <value in [disable, enable] default: 'disable'>
                  policy-object-in-dual-pane: <value in [disable, enable] default: 'disable'>
                  pre-login-banner: <value in [disable, enable] default: 'disable'>
                  pre-login-banner-message: <value of string>
                  remoteauthtimeout: <value of integer default: 10>
                  search-all-adoms: <value in [disable, enable] default: 'disable'>
                  ssl-low-encryption: <value in [disable, enable] default: 'disable'>
                  ssl-protocol:
                    - <value in [tlsv1.2, tlsv1.1, tlsv1.0, ...]>
                  ssl-static-key-ciphers: <value in [disable, enable] default: 'enable'>
                  task-list-size: <value of integer default: 2000>
                  tftp: <value in [disable, enable] default: 'disable'>
                  timezone: <value in [00, 01, 02, ...] default: '04'>
                  tunnel-mtu: <value of integer default: 1500>
                  usg: <value in [disable, enable] default: 'disable'>
                  vdom-mirror: <value in [disable, enable] default: 'disable'>
                  webservice-proto:
                    - <value in [tlsv1.2, tlsv1.1, tlsv1.0, ...]>
                  workflow-max-sessions: <value of integer default: 500>
                  workspace-mode: <value in [disabled, normal, workflow] default: 'disabled'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> admin-lockout-duration </span> - Lockout duration(sec) for administration. <span class="li-normal">type: int</span>  <span class="li-normal">example: 60</span>  </li>
 <li> <span class="li-return"> admin-lockout-threshold </span> - Lockout threshold for administration. <span class="li-normal">type: int</span>  <span class="li-normal">example: 3</span>  </li>
 <li> <span class="li-return"> adom-mode </span> - ADOM mode. <span class="li-normal">type: str</span>  <span class="li-normal">example: normal</span>  </li>
 <li> <span class="li-return"> adom-rev-auto-delete </span> - Auto delete features for old ADOM revisions. <span class="li-normal">type: str</span>  <span class="li-normal">example: by-revisions</span>  </li>
 <li> <span class="li-return"> adom-rev-max-backup-revisions </span> - Maximum number of ADOM revisions to backup. <span class="li-normal">type: int</span>  <span class="li-normal">example: 5</span>  </li>
 <li> <span class="li-return"> adom-rev-max-days </span> - Number of days to keep old ADOM revisions. <span class="li-normal">type: int</span>  <span class="li-normal">example: 30</span>  </li>
 <li> <span class="li-return"> adom-rev-max-revisions </span> - Maximum number of ADOM revisions to keep. <span class="li-normal">type: int</span>  <span class="li-normal">example: 120</span>  </li>
 <li> <span class="li-return"> adom-select </span> - Enable/disable select ADOM after login. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> adom-status </span> - ADOM status. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> clt-cert-req </span> - Require client certificate for GUI login. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> console-output </span> - Console output mode. <span class="li-normal">type: str</span>  <span class="li-normal">example: standard</span>  </li>
 <li> <span class="li-return"> country-flag </span> - Country flag Status. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> create-revision </span> - Enable/disable create revision by default. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> daylightsavetime </span> - Enable/disable daylight saving time. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> default-disk-quota </span> - Default disk quota for registered device (MB). <span class="li-normal">type: int</span>  <span class="li-normal">example: 1000</span>  </li>
 <li> <span class="li-return"> detect-unregistered-log-device </span> - Detect unregistered logging device from log message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> device-view-mode </span> - Set devices/groups view mode. <span class="li-normal">type: str</span>  <span class="li-normal">example: regular</span>  </li>
 <li> <span class="li-return"> dh-params </span> - Minimum size of Diffie-Hellman prime for SSH/HTTPS (bits). <span class="li-normal">type: str</span>  <span class="li-normal">example: 2048</span>  </li>
 <li> <span class="li-return"> disable-module </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> enc-algorithm </span> - SSL communication encryption algorithms. <span class="li-normal">type: str</span>  <span class="li-normal">example: high</span>  </li>
 <li> <span class="li-return"> faz-status </span> - FAZ status. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> fgfm-local-cert </span> - set the fgfm local certificate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fgfm-ssl-protocol </span> - set the lowest SSL protocols for fgfmsd. <span class="li-normal">type: str</span>  <span class="li-normal">example: tlsv1.2</span>  </li>
 <li> <span class="li-return"> ha-member-auto-grouping </span> - Enable/disable automatically group HA members feature <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> hitcount_concurrent </span> - The number of FortiGates that FortiManager polls at one time (10 - 500, default = 100). <span class="li-normal">type: int</span>  <span class="li-normal">example: 100</span>  </li>
 <li> <span class="li-return"> hitcount_interval </span> - The interval for getting hit count from managed FortiGate devices, in seconds (60 - 86400, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">example: 300</span>  </li>
 <li> <span class="li-return"> hostname </span> - System hostname. <span class="li-normal">type: str</span>  <span class="li-normal">example: FMG-VM64</span>  </li>
 <li> <span class="li-return"> import-ignore-addr-cmt </span> - Enable/Disable import ignore of address comments. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> language </span> - System global language. <span class="li-normal">type: str</span>  <span class="li-normal">example: english</span>  </li>
 <li> <span class="li-return"> latitude </span> - fmg location latitude <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ldap-cache-timeout </span> - LDAP browser cache timeout (seconds). <span class="li-normal">type: int</span>  <span class="li-normal">example: 86400</span>  </li>
 <li> <span class="li-return"> ldapconntimeout </span> - LDAP connection timeout (msec). <span class="li-normal">type: int</span>  <span class="li-normal">example: 60000</span>  </li>
 <li> <span class="li-return"> lock-preempt </span> - Enable/disable ADOM lock override. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> log-checksum </span> - Record log file hash value, timestamp, and authentication code at transmission or rolling. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> log-forward-cache-size </span> - Log forwarding disk cache size (GB). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> longitude </span> - fmg location longitude <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-log-forward </span> - Maximum number of log-forward and aggregation settings. <span class="li-normal">type: int</span>  <span class="li-normal">example: 5</span>  </li>
 <li> <span class="li-return"> max-running-reports </span> - Maximum number of reports generating at one time. <span class="li-normal">type: int</span>  <span class="li-normal">example: 1</span>  </li>
 <li> <span class="li-return"> oftp-ssl-protocol </span> - set the lowest SSL protocols for oftpd. <span class="li-normal">type: str</span>  <span class="li-normal">example: tlsv1.2</span>  </li>
 <li> <span class="li-return"> partial-install </span> - Enable/Disable partial install (install some objects). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> partial-install-force </span> - Enable/Disable partial install when devdb is modified. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> partial-install-rev </span> - Enable/Disable auto creating adom revision for partial install. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> perform-improve-by-ha </span> - Enable/Disable performance improvement by distributing tasks to HA slaves. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> policy-hit-count </span> - show policy hit count. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> policy-object-in-dual-pane </span> - show policies and objects in dual pane. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> pre-login-banner </span> - Enable/disable pre-login banner. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> pre-login-banner-message </span> - Pre-login banner message. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> remoteauthtimeout </span> - Remote authentication (RADIUS/LDAP) timeout (sec). <span class="li-normal">type: int</span>  <span class="li-normal">example: 10</span>  </li>
 <li> <span class="li-return"> search-all-adoms </span> - Enable/Disable Search all ADOMs for where-used query. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> ssl-low-encryption </span> - SSL low-grade encryption. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> ssl-protocol </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ssl-static-key-ciphers </span> - Enable/disable SSL static key ciphers. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> task-list-size </span> - Maximum number of completed tasks to keep. <span class="li-normal">type: int</span>  <span class="li-normal">example: 2000</span>  </li>
 <li> <span class="li-return"> tftp </span> - Enable/disable TFTP in `exec restore image` command (disabled by default in FIPS mode) <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> timezone </span> - Time zone. <span class="li-normal">type: str</span>  <span class="li-normal">example: 04</span>  </li>
 <li> <span class="li-return"> tunnel-mtu </span> - Maximum transportation unit(68 - 9000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 1500</span>  </li>
 <li> <span class="li-return"> usg </span> - Enable/disable Fortiguard server restriction. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> vdom-mirror </span> - VDOM mirror. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> webservice-proto </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> workflow-max-sessions </span> - Maximum number of workflow sessions per ADOM (minimum 100). <span class="li-normal">type: int</span>  <span class="li-normal">example: 500</span>  </li>
 <li> <span class="li-return"> workspace-mode </span> - Set workspace mode (ADOM Locking). <span class="li-normal">type: str</span>  <span class="li-normal">example: disabled</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/global</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/global</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



