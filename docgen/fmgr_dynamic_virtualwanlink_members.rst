:source: fmgr_dynamic_virtualwanlink_members.py

:orphan:

.. _fmgr_dynamic_virtualwanlink_members:

fmgr_dynamic_virtualwanlink_members
+++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">dynamic_virtualwanlink_members</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cost</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-failtime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-http-get</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-match</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http]</span> </li>
 <li><span class="li-head">detect-recoverytime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cost</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-failtime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-http-get</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-match</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http]</span> </li>
 <li><span class="li-head">detect-recoverytime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">volume-ratio</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">volume-ratio</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
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
      fmgr_dynamic_virtualwanlink_members:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         dynamic_virtualwanlink_members:
            comment: <value of string>
            cost: <value of integer>
            detect-failtime: <value of integer>
            detect-http-get: <value of string>
            detect-http-match: <value of string>
            detect-http-port: <value of integer>
            detect-interval: <value of integer>
            detect-protocol: <value in [ping, tcp-echo, udp-echo, ...]>
            detect-recoverytime: <value of integer>
            detect-server: <value of string>
            detect-timeout: <value of integer>
            dynamic_mapping:
              -
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  comment: <value of string>
                  cost: <value of integer>
                  detect-failtime: <value of integer>
                  detect-http-get: <value of string>
                  detect-http-match: <value of string>
                  detect-http-port: <value of integer>
                  detect-interval: <value of integer>
                  detect-protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                  detect-recoverytime: <value of integer>
                  detect-server: <value of string>
                  detect-timeout: <value of integer>
                  gateway: <value of string>
                  gateway6: <value of string>
                  ingress-spillover-threshold: <value of integer>
                  interface: <value of string>
                  priority: <value of integer>
                  source: <value of string>
                  source6: <value of string>
                  spillover-threshold: <value of integer>
                  status: <value in [disable, enable]>
                  volume-ratio: <value of integer>
                  weight: <value of integer>
            gateway: <value of string>
            gateway6: <value of string>
            ingress-spillover-threshold: <value of integer>
            interface: <value of string>
            name: <value of string>
            priority: <value of integer>
            source: <value of string>
            source6: <value of string>
            spillover-threshold: <value of integer>
            status: <value in [disable, enable]>
            volume-ratio: <value of integer>
            weight: <value of integer>



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



