:source: fmgr_firewall_mmsprofile_notification.py

:orphan:

.. _fmgr_firewall_mmsprofile_notification:

fmgr_firewall_mmsprofile_notification -- Notification configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 </tr>
 <tr>
 <td>firewall_mmsprofile_notification</td>
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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">mms-profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_mmsprofile_notification</span> - Notification configuration. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">alert-int</span> - Alert notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">alert-int-mode</span> - Alert notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">alert-src-msisdn</span> - Specify from address for alert messages. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">alert-status</span> - Alert notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bword-int</span> - Banned word notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bword-int-mode</span> - Banned word notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">bword-status</span> - Banned word notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">carrier-endpoint-bwl-int</span> - Carrier end point black/white list notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">carrier-endpoint-bwl-int-mode</span> - Carrier end point black/white list notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">carrier-endpoint-bwl-status</span> - Carrier end point black/white list notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">days-allowed</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> </li>
 <li><span class="li-head">detect-server</span> - Enable/disable automatic server address determination. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dupe-int</span> - Duplicate notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dupe-int-mode</span> - Duplicate notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">dupe-status</span> - Duplicate notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">file-block-int</span> - File block notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">file-block-int-mode</span> - File block notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">file-block-status</span> - File block notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">flood-int</span> - Flood notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">flood-int-mode</span> - Flood notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">flood-status</span> - Flood notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">from-in-header</span> - Enable/disable insertion of from address in HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-checksum-int</span> - MMS checksum notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mms-checksum-int-mode</span> - MMS checksum notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">mms-checksum-status</span> - MMS checksum notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mmsc-hostname</span> - Host name or IP address of the MMSC. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mmsc-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">mmsc-port</span> - Port used on the MMSC for sending MMS messages (1 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mmsc-url</span> - URL used on the MMSC for sending MMS messages. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mmsc-username</span> - User name required for authentication with the MMSC. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-protocol</span> - Protocol to use for sending notification messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mm1, mm3, mm4, mm7]</span> </li>
 <li><span class="li-head">msg-type</span> - MM7 message type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [submit-req, deliver-req]</span> </li>
 <li><span class="li-head">protocol</span> - Protocol. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rate-limit</span> - Rate limit for sending notification messages (0 - 250). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tod-window-duration</span> - Time of day window duration. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tod-window-end</span> - Obsolete. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tod-window-start</span> - Time of day window start. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user-domain</span> - Domain name to which the user addresses belong. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vas-id</span> - VAS identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vasp-id</span> - VASP identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">virus-int</span> - Virus notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">virus-int-mode</span> - Virus notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">virus-status</span> - Virus notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Notification configuration.
      fmgr_firewall_mmsprofile_notification:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         mms-profile: <your own value>
         firewall_mmsprofile_notification:
            alert-int: <value of integer>
            alert-int-mode: <value in [hours, minutes]>
            alert-src-msisdn: <value of string>
            alert-status: <value in [disable, enable]>
            bword-int: <value of integer>
            bword-int-mode: <value in [hours, minutes]>
            bword-status: <value in [disable, enable]>
            carrier-endpoint-bwl-int: <value of integer>
            carrier-endpoint-bwl-int-mode: <value in [hours, minutes]>
            carrier-endpoint-bwl-status: <value in [disable, enable]>
            days-allowed:
              - sunday
              - monday
              - tuesday
              - wednesday
              - thursday
              - friday
              - saturday
            detect-server: <value in [disable, enable]>
            dupe-int: <value of integer>
            dupe-int-mode: <value in [hours, minutes]>
            dupe-status: <value in [disable, enable]>
            file-block-int: <value of integer>
            file-block-int-mode: <value in [hours, minutes]>
            file-block-status: <value in [disable, enable]>
            flood-int: <value of integer>
            flood-int-mode: <value in [hours, minutes]>
            flood-status: <value in [disable, enable]>
            from-in-header: <value in [disable, enable]>
            mms-checksum-int: <value of integer>
            mms-checksum-int-mode: <value in [hours, minutes]>
            mms-checksum-status: <value in [disable, enable]>
            mmsc-hostname: <value of string>
            mmsc-password: <value of string>
            mmsc-port: <value of integer>
            mmsc-url: <value of string>
            mmsc-username: <value of string>
            msg-protocol: <value in [mm1, mm3, mm4, ...]>
            msg-type: <value in [submit-req, deliver-req]>
            protocol: <value of string>
            rate-limit: <value of integer>
            tod-window-duration: <value of string>
            tod-window-end: <value of string>
            tod-window-start: <value of string>
            user-domain: <value of string>
            vas-id: <value of string>
            vasp-id: <value of string>
            virus-int: <value of integer>
            virus-int-mode: <value in [hours, minutes]>
            virus-status: <value in [disable, enable]>



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



