:source: fmgr_system_sql.py

:orphan:

.. _fmgr_system_sql:

fmgr_system_sql -- SQL settings.
++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">system_sql</span> - SQL settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">background-rebuild</span> - Disable/Enable rebuild SQL database in the background. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">custom-index</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">case-sensitive</span> - Disable/Enable case sensitive index. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">device-type</span> - Device type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [FortiGate, FortiManager, FortiClient, FortiMail, FortiWeb, FortiCache, FortiSandbox, FortiDDoS, FortiAuthenticator, FortiProxy]</span>  <span class="li-normal">default: FortiGate</span> </li>
 <li><span class="li-head">id</span> - Add or Edit log index fields. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">index-field</span> - Log field name to be indexed. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">log-type</span> - Log type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, app-ctrl, attack, content, dlp, emailfilter, event, generic, history, traffic, virus, voip, webfilter, netscan, fct-event, fct-traffic, fct-netscan, waf, gtp, dns, ssh, ssl]</span>  <span class="li-normal">default: traffic</span> </li>
 </ul>
 <li><span class="li-head">database-name</span> - Database name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">database-type</span> - Database type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mysql, postgres]</span>  <span class="li-normal">default: postgres</span> </li>
 <li><span class="li-head">device-count-high</span> - Must set to enable if the count of registered devices is greater than 8000. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">event-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for event logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">fct-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for FortiClient logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 240</span> </li>
 <li><span class="li-head">logtype</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, app-ctrl, attack, content, dlp, emailfilter, event, generic, history, traffic, virus, voip, webfilter, netscan, fct-event, fct-traffic, fct-netscan, waf, gtp, dns, ssh, ssl]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">prompt-sql-upgrade</span> - Prompt to convert log database into SQL database at start time on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">rebuild-event</span> - Disable/Enable rebuild event during SQL database rebuilding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">rebuild-event-start-time</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server</span> - Database IP or hostname. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-time</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">status</span> - SQL database status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, local]</span>  <span class="li-normal">default: local</span> </li>
 <li><span class="li-head">text-search-index</span> - Disable/Enable text search index. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">traffic-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for traffic logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ts-index-field</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Category of text search index fields. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">value</span> - Fields of text search index. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">username</span> - User name for login remote database. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for UTM logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
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
    - name: SQL settings.
      fmgr_system_sql:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         system_sql:
            background-rebuild: <value in [disable, enable]>
            custom-index:
              -
                  case-sensitive: <value in [disable, enable]>
                  device-type: <value in [FortiGate, FortiManager, FortiClient, ...]>
                  id: <value of integer>
                  index-field: <value of string>
                  log-type: <value in [none, app-ctrl, attack, ...]>
            database-name: <value of string>
            database-type: <value in [mysql, postgres]>
            device-count-high: <value in [disable, enable]>
            event-table-partition-time: <value of integer>
            fct-table-partition-time: <value of integer>
            logtype:
              - none
              - app-ctrl
              - attack
              - content
              - dlp
              - emailfilter
              - event
              - generic
              - history
              - traffic
              - virus
              - voip
              - webfilter
              - netscan
              - fct-event
              - fct-traffic
              - fct-netscan
              - waf
              - gtp
              - dns
              - ssh
              - ssl
            password: <value of string>
            prompt-sql-upgrade: <value in [disable, enable]>
            rebuild-event: <value in [disable, enable]>
            rebuild-event-start-time: <value of string>
            server: <value of string>
            start-time: <value of string>
            status: <value in [disable, local]>
            text-search-index: <value in [disable, enable]>
            traffic-table-partition-time: <value of integer>
            ts-index-field:
              -
                  category: <value of string>
                  value: <value of string>
            username: <value of string>
            utm-table-partition-time: <value of integer>



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



