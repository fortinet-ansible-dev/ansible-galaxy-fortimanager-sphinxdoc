:source: fmgr_firewall_gtp_messageratelimit.py

:orphan:

.. _fmgr_firewall_gtp_messageratelimit:

fmgr_firewall_gtp_messageratelimit -- Message rate limiting.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">gtp</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_gtp_messageratelimit</span> - Message rate limiting. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">create-aa-pdp-request</span> - Rate limit for create AA PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-aa-pdp-response</span> - Rate limit for create AA PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-mbms-request</span> - Rate limit for create MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-mbms-response</span> - Rate limit for create MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-pdp-request</span> - Rate limit for create PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-pdp-response</span> - Rate limit for create PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-aa-pdp-request</span> - Rate limit for delete AA PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-aa-pdp-response</span> - Rate limit for delete AA PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-mbms-request</span> - Rate limit for delete MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-mbms-response</span> - Rate limit for delete MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-request</span> - Rate limit for delete PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-response</span> - Rate limit for delete PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-reponse</span> - Rate limit for echo response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-request</span> - Rate limit for echo requests (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">error-indication</span> - Rate limit for error indication (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">failure-report-request</span> - Rate limit for failure report request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">failure-report-response</span> - Rate limit for failure report response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-reloc-complete-ack</span> - Rate limit for forward relocation complete acknowledge (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-complete</span> - Rate limit for forward relocation complete (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-request</span> - Rate limit for forward relocation request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-response</span> - Rate limit for forward relocation response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-srns-context</span> - Rate limit for forward SRNS context (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-srns-context-ack</span> - Rate limit for forward SRNS context acknowledge (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">g-pdu</span> - Rate limit for G-PDU (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">identification-request</span> - Rate limit for identification request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">identification-response</span> - Rate limit for identification response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-de-reg-request</span> - Rate limit for MBMS de-registration request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-de-reg-response</span> - Rate limit for MBMS de-registration response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-rej-request</span> - Rate limit for MBMS notification reject request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-rej-response</span> - Rate limit for MBMS notification reject response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-request</span> - Rate limit for MBMS notification request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-response</span> - Rate limit for MBMS notification response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-reg-request</span> - Rate limit for MBMS registration request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-reg-response</span> - Rate limit for MBMS registration response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-start-request</span> - Rate limit for MBMS session start request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-start-response</span> - Rate limit for MBMS session start response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-stop-request</span> - Rate limit for MBMS session stop request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-stop-response</span> - Rate limit for MBMS session stop response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">note-ms-request</span> - Rate limit for note MS GPRS present request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">note-ms-response</span> - Rate limit for note MS GPRS present response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-rej-request</span> - Rate limit for PDU notify reject request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-rej-response</span> - Rate limit for PDU notify reject response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-request</span> - Rate limit for PDU notify request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-response</span> - Rate limit for PDU notify response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ran-info</span> - Rate limit for RAN information relay (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">relocation-cancel-request</span> - Rate limit for relocation cancel request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">relocation-cancel-response</span> - Rate limit for relocation cancel response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">send-route-request</span> - Rate limit for send routing information for GPRS request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">send-route-response</span> - Rate limit for send routing information for GPRS response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-ack</span> - Rate limit for SGSN context acknowledgement (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-request</span> - Rate limit for SGSN context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-response</span> - Rate limit for SGSN context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">support-ext-hdr-notify</span> - Rate limit for support extension headers notification (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-mbms-request</span> - Rate limit for update MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-mbms-response</span> - Rate limit for update MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-pdp-request</span> - Rate limit for update PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-pdp-response</span> - Rate limit for update PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">version-not-support</span> - Rate limit for version not supported (packets per second). <span class="li-normal">type: int</span> </li>
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
    - name: Message rate limiting.
      fmgr_firewall_gtp_messageratelimit:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         gtp: <your own value>
         firewall_gtp_messageratelimit:
            create-aa-pdp-request: <value of integer>
            create-aa-pdp-response: <value of integer>
            create-mbms-request: <value of integer>
            create-mbms-response: <value of integer>
            create-pdp-request: <value of integer>
            create-pdp-response: <value of integer>
            delete-aa-pdp-request: <value of integer>
            delete-aa-pdp-response: <value of integer>
            delete-mbms-request: <value of integer>
            delete-mbms-response: <value of integer>
            delete-pdp-request: <value of integer>
            delete-pdp-response: <value of integer>
            echo-reponse: <value of integer>
            echo-request: <value of integer>
            error-indication: <value of integer>
            failure-report-request: <value of integer>
            failure-report-response: <value of integer>
            fwd-reloc-complete-ack: <value of integer>
            fwd-relocation-complete: <value of integer>
            fwd-relocation-request: <value of integer>
            fwd-relocation-response: <value of integer>
            fwd-srns-context: <value of integer>
            fwd-srns-context-ack: <value of integer>
            g-pdu: <value of integer>
            identification-request: <value of integer>
            identification-response: <value of integer>
            mbms-de-reg-request: <value of integer>
            mbms-de-reg-response: <value of integer>
            mbms-notify-rej-request: <value of integer>
            mbms-notify-rej-response: <value of integer>
            mbms-notify-request: <value of integer>
            mbms-notify-response: <value of integer>
            mbms-reg-request: <value of integer>
            mbms-reg-response: <value of integer>
            mbms-ses-start-request: <value of integer>
            mbms-ses-start-response: <value of integer>
            mbms-ses-stop-request: <value of integer>
            mbms-ses-stop-response: <value of integer>
            note-ms-request: <value of integer>
            note-ms-response: <value of integer>
            pdu-notify-rej-request: <value of integer>
            pdu-notify-rej-response: <value of integer>
            pdu-notify-request: <value of integer>
            pdu-notify-response: <value of integer>
            ran-info: <value of integer>
            relocation-cancel-request: <value of integer>
            relocation-cancel-response: <value of integer>
            send-route-request: <value of integer>
            send-route-response: <value of integer>
            sgsn-context-ack: <value of integer>
            sgsn-context-request: <value of integer>
            sgsn-context-response: <value of integer>
            support-ext-hdr-notify: <value of integer>
            update-mbms-request: <value of integer>
            update-mbms-response: <value of integer>
            update-pdp-request: <value of integer>
            update-pdp-response: <value of integer>
            version-not-support: <value of integer>



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



