:source: fmgr_gtp_messagefilterv2.py

:orphan:

.. _fmgr_gtp_messagefilterv2:

fmgr_gtp_messagefilterv2 -- Message filter for GTPv2 messages.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">gtp_messagefilterv2</span> - Message filter for GTPv2 messages. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">bearer-resource-cmd-fail</span> - Bearer resource (command 68, failure indication 69). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">change-notification</span> - Change notification (req 38, resp 39). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">create-bearer</span> - Create bearer (req 95, resp 96). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">create-session</span> - Create session (req 32, resp 33). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-bearer-cmd-fail</span> - Delete bearer (command 66, failure indication 67). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-bearer-req-resp</span> - Delete bearer (req 99, resp 100). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-pdn-connection-set</span> - Delete PDN connection set (req 101, resp 102). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-session</span> - Delete session (req 36, resp 37). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">echo</span> - Echo (req 1, resp 2). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">modify-bearer-cmd-fail</span> - Modify bearer (command 64 , failure indication 65). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">modify-bearer-req-resp</span> - Modify bearer (req 34, resp 35). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">name</span> - Message filter name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resume</span> - Resume (notify 164 , ack 165). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">suspend</span> - Suspend (notify 162, ack 163). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">trace-session</span> - Trace session (activation 71, deactivation 72). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message</span> - Allow or Deny unknown messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message-white-list</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">update-bearer</span> - Update bearer (req 97, resp 98). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">update-pdn-connection-set</span> - Update PDN connection set (req 200, resp 201). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">version-not-support</span> - Version not supported (3). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
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
    - name: Message filter for GTPv2 messages.
      fmgr_gtp_messagefilterv2:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         gtp_messagefilterv2:
            bearer-resource-cmd-fail: <value in [allow, deny]>
            change-notification: <value in [allow, deny]>
            create-bearer: <value in [allow, deny]>
            create-session: <value in [allow, deny]>
            delete-bearer-cmd-fail: <value in [allow, deny]>
            delete-bearer-req-resp: <value in [allow, deny]>
            delete-pdn-connection-set: <value in [allow, deny]>
            delete-session: <value in [allow, deny]>
            echo: <value in [allow, deny]>
            modify-bearer-cmd-fail: <value in [allow, deny]>
            modify-bearer-req-resp: <value in [allow, deny]>
            name: <value of string>
            resume: <value in [allow, deny]>
            suspend: <value in [allow, deny]>
            trace-session: <value in [allow, deny]>
            unknown-message: <value in [allow, deny]>
            unknown-message-white-list: <value of integer>
            update-bearer: <value in [allow, deny]>
            update-pdn-connection-set: <value in [allow, deny]>
            version-not-support: <value in [allow, deny]>



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



