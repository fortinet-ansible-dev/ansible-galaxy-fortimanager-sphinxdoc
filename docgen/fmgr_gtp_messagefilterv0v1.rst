:source: fmgr_gtp_messagefilterv0v1.py

:orphan:

.. _fmgr_gtp_messagefilterv0v1:

fmgr_gtp_messagefilterv0v1 -- Message filter for GTPv0/v1 messages.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">gtp_messagefilterv0v1</span> - Message filter for GTPv0/v1 messages. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">create-mbms</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">create-pdp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">data-record</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-aa-pdp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-mbms</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-pdp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">echo</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">end-marker</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">error-indication</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">failure-report</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">fwd-relocation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">fwd-srns-context</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">gtp-pdu</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">identification</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-de-registration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-notification</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-registration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-start</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-stop</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-update</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">ms-info-change-notif</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">node-alive</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">note-ms-present</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">pdu-notification</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">ran-info</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">redirection</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">relocation-cancel</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">send-route</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">sgsn-context</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">support-extension</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message-white-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">update-mbms</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">update-pdp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">v0-create-aa-pdp--v1-init-pdp-ctx</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">version-not-support</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
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
    - name: Message filter for GTPv0/v1 messages.
      fmgr_gtp_messagefilterv0v1:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         gtp_messagefilterv0v1:
            create-mbms: <value in [allow, deny]>
            create-pdp: <value in [allow, deny]>
            data-record: <value in [allow, deny]>
            delete-aa-pdp: <value in [allow, deny]>
            delete-mbms: <value in [allow, deny]>
            delete-pdp: <value in [allow, deny]>
            echo: <value in [allow, deny]>
            end-marker: <value in [allow, deny]>
            error-indication: <value in [allow, deny]>
            failure-report: <value in [allow, deny]>
            fwd-relocation: <value in [allow, deny]>
            fwd-srns-context: <value in [allow, deny]>
            gtp-pdu: <value in [allow, deny]>
            identification: <value in [allow, deny]>
            mbms-de-registration: <value in [allow, deny]>
            mbms-notification: <value in [allow, deny]>
            mbms-registration: <value in [allow, deny]>
            mbms-session-start: <value in [allow, deny]>
            mbms-session-stop: <value in [allow, deny]>
            mbms-session-update: <value in [allow, deny]>
            ms-info-change-notif: <value in [allow, deny]>
            name: <value of string>
            node-alive: <value in [allow, deny]>
            note-ms-present: <value in [allow, deny]>
            pdu-notification: <value in [allow, deny]>
            ran-info: <value in [allow, deny]>
            redirection: <value in [allow, deny]>
            relocation-cancel: <value in [allow, deny]>
            send-route: <value in [allow, deny]>
            sgsn-context: <value in [allow, deny]>
            support-extension: <value in [allow, deny]>
            unknown-message: <value in [allow, deny]>
            unknown-message-white-list:
              - <value of integer>
            update-mbms: <value in [allow, deny]>
            update-pdp: <value in [allow, deny]>
            v0-create-aa-pdp--v1-init-pdp-ctx: <value in [deny, allow]>
            version-not-support: <value in [allow, deny]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
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



