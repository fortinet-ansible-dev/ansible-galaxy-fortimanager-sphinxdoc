:source: fmgr_vpnsslweb_portal_bookmarkgroup.py

:orphan:

.. _fmgr_vpnsslweb_portal_bookmarkgroup:

fmgr_vpnsslweb_portal_bookmarkgroup -- Portal bookmark group.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">portal</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vpnsslweb_portal_bookmarkgroup</span> - Portal bookmark group. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">bookmarks</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">additional-params</span> - Additional parameters. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">apptype</span> - Application type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [web, telnet, ssh, ftp, smb, vnc, rdp, citrix, rdpnative, portforward, sftp]</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">folder</span> - Network shared file folder parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">form-data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">value</span> - Value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">host</span> - Host name/IP parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">listening-port</span> - Listening port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">load-balancing-info</span> - The load balancing information or cookie which should be provided to the connection broker. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logon-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">logon-user</span> - Logon user. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Bookmark name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Remote port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preconnection-blob</span> - An arbitrary string which identifies the RDP source. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">preconnection-id</span> - The numeric ID of the RDP source (0-2147483648). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">remote-port</span> - Remote port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security</span> - Security mode for RDP connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rdp, nla, tls, any]</span> </li>
 <li><span class="li-head">server-layout</span> - Server side keyboard layout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [en-us-qwerty, de-de-qwertz, fr-fr-azerty, it-it-qwerty, sv-se-qwerty, failsafe, en-gb-qwerty, es-es-qwerty, fr-ch-qwertz, ja-jp-qwerty, pt-br-qwerty, tr-tr-qwerty]</span> </li>
 <li><span class="li-head">show-status-window</span> - Enable/disable showing of status window. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso</span> - Single Sign-On. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, static, auto]</span> </li>
 <li><span class="li-head">sso-credential</span> - Single sign-on credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslvpn-login, alternative]</span> </li>
 <li><span class="li-head">sso-credential-sent-once</span> - Single sign-on credentials are only sent once to remote server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sso-username</span> - SSO user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url</span> - URL parameter. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Bookmark group name. <span class="li-normal">type: str</span> </li>
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
    - name: Portal bookmark group.
      fmgr_vpnsslweb_portal_bookmarkgroup:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         portal: <your own value>
         state: <value in [present, absent]>
         vpnsslweb_portal_bookmarkgroup:
            bookmarks:
              -
                  additional-params: <value of string>
                  apptype: <value in [web, telnet, ssh, ...]>
                  description: <value of string>
                  folder: <value of string>
                  form-data:
                    -
                        name: <value of string>
                        value: <value of string>
                  host: <value of string>
                  listening-port: <value of integer>
                  load-balancing-info: <value of string>
                  logon-password: <value of string>
                  logon-user: <value of string>
                  name: <value of string>
                  port: <value of integer>
                  preconnection-blob: <value of string>
                  preconnection-id: <value of integer>
                  remote-port: <value of integer>
                  security: <value in [rdp, nla, tls, ...]>
                  server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
                  show-status-window: <value in [disable, enable]>
                  sso: <value in [disable, static, auto]>
                  sso-credential: <value in [sslvpn-login, alternative]>
                  sso-credential-sent-once: <value in [disable, enable]>
                  sso-password: <value of string>
                  sso-username: <value of string>
                  url: <value of string>
            name: <value of string>



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



