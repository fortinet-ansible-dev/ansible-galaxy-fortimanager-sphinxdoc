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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">gtp_messagefilterv0v1</span> - Message filter for GTPv0/v1 messages. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">create-mbms</span> - GTPv1 create MBMS context (req 100, resp 101). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">create-pdp</span> - Create PDP context (req 16, resp 17). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">data-record</span> - Data record transfer (req 240, resp 241). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-aa-pdp</span> - GTPv0 delete AA PDP context (req 24, resp 25). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-mbms</span> - GTPv1 delete MBMS context (req 104, resp 105). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-pdp</span> - Delete PDP context (req 20, resp 21). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">echo</span> - Echo (req 1, resp 2). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">end-marker</span> - GTPv1 End marker (254). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">error-indication</span> - Error indication (26). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">failure-report</span> - Failure report (req 34, resp 35). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">fwd-relocation</span> - GTPv1 forward relocation (req 53, resp 54, complete 55, complete ack 59). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">fwd-srns-context</span> - GTPv1 forward SRNS (context 58, context ack 60). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">gtp-pdu</span> - PDU (255). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">identification</span> - Identification (req 48, resp 49). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-de-registration</span> - GTPv1 MBMS de-registration (req 114, resp 115). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-notification</span> - GTPv1 MBMS notification (req 96, resp 97, reject req 98. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-registration</span> - GTPv1 MBMS registration (req 112, resp 113). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-start</span> - GTPv1 MBMS session start (req 116, resp 117). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-stop</span> - GTPv1 MBMS session stop (req 118, resp 119). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-update</span> - GTPv1 MBMS session update (req 120, resp 121). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">ms-info-change-notif</span> - GTPv1 MS info change notification (req 128, resp 129). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">name</span> - Message filter name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">node-alive</span> - Node alive (req 4, resp 5). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">note-ms-present</span> - Note MS GPRS present (req 36, resp 37). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">pdu-notification</span> - PDU notification (req 27, resp 28, reject req 29, reject resp 30). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">ran-info</span> - GTPv1 RAN information relay (70). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">redirection</span> - Redirection (req 6, resp 7). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">relocation-cancel</span> - GTPv1 relocation cancel (req 56, resp 57). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">send-route</span> - Send routing information for GPRS (req 32, resp 33). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">sgsn-context</span> - SGSN context (req 50, resp 51, ack 52). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">support-extension</span> - GTPv1 supported extension headers notify (31). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message</span> - Allow or Deny unknown messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message-white-list</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">update-mbms</span> - GTPv1 update MBMS context (req 102, resp 103). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">update-pdp</span> - Update PDP context (req 18, resp 19). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">v0-create-aa-pdp--v1-init-pdp-ctx</span> - GTPv0 create AA PDP context (req 22, resp 23); Or GTPv1 initiate PDP context (req 22, resp 23). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
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
    - name: Message filter for GTPv0/v1 messages.
      fmgr_gtp_messagefilterv0v1:
         bypass_validation: False
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
            unknown-message-white-list: <value of integer>
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



