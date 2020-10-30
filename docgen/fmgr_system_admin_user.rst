:source: fmgr_system_admin_user.py

:orphan:

.. _fmgr_system_admin_user:

fmgr_system_admin_user -- Admin user.
+++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">system_admin_user</span> - Admin user. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom-name</span> - Admin domain names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">adom-exclude</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom-name</span> - Admin domain names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">app-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">app-filter-name</span> - App filter name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">avatar</span> - Image file for avatar (maximum 4K base64 encoded). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ca</span> - PKI user certificate CA (CA name in local). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">change-password</span> - Enable/disable restricted user to change self password. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dashboard</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">column</span> - Widgets column ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">diskio-content-type</span> - Disk I/O Monitor widgets chart type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [util, iops, blks]</span> </li>
 <li><span class="li-head">diskio-period</span> - Disk I/O Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span> </li>
 <li><span class="li-head">log-rate-period</span> - Log receive monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [2min , 1hour, 6hours]</span> </li>
 <li><span class="li-head">log-rate-topn</span> - Log receive monitor widgets number of top items to display. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 3, 4, 5]</span> </li>
 <li><span class="li-head">log-rate-type</span> - Log receive monitor widgets statistics breakdown options. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, device]</span> </li>
 <li><span class="li-head">moduleid</span> - Widget ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">name</span> - Widget name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">num-entries</span> - Number of entries. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">refresh-interval</span> - Widgets refresh interval. <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">res-cpu-display</span> - Widgets CPU display type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [average , each]</span> </li>
 <li><span class="li-head">res-period</span> - Widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [10min , hour, day]</span> </li>
 <li><span class="li-head">res-view-type</span> - Widgets data view type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [real-time , history]</span> </li>
 <li><span class="li-head">status</span> - Widgets opened/closed state. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [close, open]</span> </li>
 <li><span class="li-head">tabid</span> - ID of tab where widget is displayed. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">time-period</span> - Log Database Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span> </li>
 <li><span class="li-head">widget-type</span> - Widget type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [top-lograte, sysres, sysinfo, licinfo, jsconsole, sysop, alert, statistics, rpteng, raid, logrecv, devsummary, logdb-perf, logdb-lag, disk-io, log-rcvd-fwd]</span> </li>
 </ul>
 <li><span class="li-head">dashboard-tabs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Tab name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tabid</span> - Tab ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 </ul>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dev-group</span> - device group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">email-address</span> - Email address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ext-auth-accprofile-override</span> - Allow to use the access profile provided by the remote authentication server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ext-auth-adom-override</span> - Allow to use the ADOM provided by the remote authentication server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ext-auth-group-match</span> - Only administrators belonging to this group can login. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">first-name</span> - First name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">force-password-change</span> - Enable/disable force password change on next login. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">group</span> - Group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hidden</span> - Hidden administrator. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ips-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ips-filter-name</span> - IPS filter name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipv6_trusthost1</span> - Admin user trusted host IPv6, default ::/0 for all. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost10</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost2</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost3</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost4</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost5</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost6</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost7</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost8</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6_trusthost9</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">last-name</span> - Last name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ldap-server</span> - LDAP server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">meta-data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">fieldlength</span> - Field length. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">fieldname</span> - Field name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fieldvalue</span> - Field value. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">importance</span> - Importance. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [optional, required]</span> </li>
 <li><span class="li-head">status</span> - Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 </ul>
 <li><span class="li-head">mobile-number</span> - Mobile number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pager-number</span> - Pager number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">password-expire</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">phone-number</span> - Phone number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policy-package</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">policy-package-name</span> - Policy package names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">profileid</span> - Profile ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radius_server</span> - RADIUS server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-access</span> - Enable/disable restricted access to development VDOM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">restrict-dev-vdom</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dev-vdom</span> - Device or device VDOM. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">rpc-permit</span> - set none/read/read-write rpc-permission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [read-write, none, read]</span> </li>
 <li><span class="li-head">ssh-public-key1</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">ssh-public-key2</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">ssh-public-key3</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">subject</span> - PKI user certificate name constraints. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tacacs-plus-server</span> - TACACS+ server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost1</span> - Admin user trusted host IP, default 0. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost10</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost2</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost3</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost4</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost5</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost6</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost7</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost8</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost9</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">two-factor-auth</span> - Enable 2-factor authentication (certificate + password). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user_type</span> - User type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [local, radius, ldap, tacacs-plus, pki-auth, group]</span> </li>
 <li><span class="li-head">userid</span> - User name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">web-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">web-filter-name</span> - Web filter name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">wildcard</span> - Enable/disable wildcard remote authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Admin user.
      fmgr_system_admin_user:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         state: <value in [present, absent]>
         system_admin_user:
            adom:
              -
                  adom-name: <value of string>
            adom-exclude:
              -
                  adom-name: <value of string>
            app-filter:
              -
                  app-filter-name: <value of string>
            avatar: <value of string>
            ca: <value of string>
            change-password: <value in [disable, enable]>
            dashboard:
              -
                  column: <value of integer>
                  diskio-content-type: <value in [util, iops, blks]>
                  diskio-period: <value in [1hour, 8hour, 24hour]>
                  log-rate-period: <value in [2min , 1hour, 6hours]>
                  log-rate-topn: <value in [1, 2, 3, ...]>
                  log-rate-type: <value in [log, device]>
                  moduleid: <value of integer>
                  name: <value of string>
                  num-entries: <value of integer>
                  refresh-interval: <value of integer>
                  res-cpu-display: <value in [average , each]>
                  res-period: <value in [10min , hour, day]>
                  res-view-type: <value in [real-time , history]>
                  status: <value in [close, open]>
                  tabid: <value of integer>
                  time-period: <value in [1hour, 8hour, 24hour]>
                  widget-type: <value in [top-lograte, sysres, sysinfo, ...]>
            dashboard-tabs:
              -
                  name: <value of string>
                  tabid: <value of integer>
            description: <value of string>
            dev-group: <value of string>
            email-address: <value of string>
            ext-auth-accprofile-override: <value in [disable, enable]>
            ext-auth-adom-override: <value in [disable, enable]>
            ext-auth-group-match: <value of string>
            first-name: <value of string>
            force-password-change: <value in [disable, enable]>
            group: <value of string>
            hidden: <value of integer>
            ips-filter:
              -
                  ips-filter-name: <value of string>
            ipv6_trusthost1: <value of string>
            ipv6_trusthost10: <value of string>
            ipv6_trusthost2: <value of string>
            ipv6_trusthost3: <value of string>
            ipv6_trusthost4: <value of string>
            ipv6_trusthost5: <value of string>
            ipv6_trusthost6: <value of string>
            ipv6_trusthost7: <value of string>
            ipv6_trusthost8: <value of string>
            ipv6_trusthost9: <value of string>
            last-name: <value of string>
            ldap-server: <value of string>
            meta-data:
              -
                  fieldlength: <value of integer>
                  fieldname: <value of string>
                  fieldvalue: <value of string>
                  importance: <value in [optional, required]>
                  status: <value in [disabled, enabled]>
            mobile-number: <value of string>
            pager-number: <value of string>
            password: <value of string>
            password-expire: <value of string>
            phone-number: <value of string>
            policy-package:
              -
                  policy-package-name: <value of string>
            profileid: <value of string>
            radius_server: <value of string>
            restrict-access: <value in [disable, enable]>
            restrict-dev-vdom:
              -
                  dev-vdom: <value of string>
            rpc-permit: <value in [read-write, none, read]>
            ssh-public-key1: <value of string>
            ssh-public-key2: <value of string>
            ssh-public-key3: <value of string>
            subject: <value of string>
            tacacs-plus-server: <value of string>
            trusthost1: <value of string>
            trusthost10: <value of string>
            trusthost2: <value of string>
            trusthost3: <value of string>
            trusthost4: <value of string>
            trusthost5: <value of string>
            trusthost6: <value of string>
            trusthost7: <value of string>
            trusthost8: <value of string>
            trusthost9: <value of string>
            two-factor-auth: <value in [disable, enable]>
            user_type: <value in [local, radius, ldap, ...]>
            userid: <value of string>
            web-filter:
              -
                  web-filter-name: <value of string>
            wildcard: <value in [disable, enable]>



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



