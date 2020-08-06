:source: fmgr_pkg_footer_policy6_identitybasedpolicy6.py

:orphan:

.. _fmgr_pkg_footer_policy6_identitybasedpolicy6:

fmgr_pkg_footer_policy6_identitybasedpolicy6
++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">policy6</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_footer_policy6_identitybasedpolicy6</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept]</span> </li>
 <li><span class="li-head">application-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deep-inspection-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">devices</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">endpoint-compliance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">icap-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ips-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, all, utm]</span> </li>
 <li><span class="li-head">mms-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">send-deny-packet</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-portal</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-realm</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">voip-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: no description
      fmgr_pkg_footer_policy6_identitybasedpolicy6:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         pkg: <your own value>
         policy6: <your own value>
         state: <value in [present, absent]>
         pkg_footer_policy6_identitybasedpolicy6:
            action: <value in [deny, accept]>
            application-list: <value of string>
            av-profile: <value of string>
            deep-inspection-options: <value of string>
            devices: <value of string>
            dlp-sensor: <value of string>
            endpoint-compliance: <value in [disable, enable]>
            groups: <value of string>
            icap-profile: <value of string>
            id: <value of integer>
            ips-sensor: <value of string>
            logtraffic: <value in [disable, enable, all, ...]>
            mms-profile: <value of string>
            per-ip-shaper: <value of string>
            profile-group: <value of string>
            profile-protocol-options: <value of string>
            profile-type: <value in [single, group]>
            replacemsg-group: <value of string>
            schedule: <value of string>
            send-deny-packet: <value in [disable, enable]>
            service: <value of string>
            service-negate: <value in [disable, enable]>
            spamfilter-profile: <value of string>
            sslvpn-portal: <value of string>
            sslvpn-realm: <value of string>
            traffic-shaper: <value of string>
            traffic-shaper-reverse: <value of string>
            utm-status: <value in [disable, enable]>
            voip-profile: <value of string>
            webfilter-profile: <value of string>



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



