:source: fmgr_icap_profile.py

:orphan:

.. _fmgr_icap_profile:

fmgr_icap_profile -- Configure ICAP profiles.
+++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">icap_profile</span> - Configure ICAP profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">methods</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [delete, get, head, options, post, put, trace, other]</span> </li>
 <li><span class="li-head">name</span> - ICAP profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">request</span> - Enable/disable whether an HTTP request is passed to an ICAP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">request-failure</span> - Action to take if the ICAP server cannot be contacted when processing an HTTP request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [error, bypass]</span> </li>
 <li><span class="li-head">request-path</span> - Path component of the ICAP URI that identifies the HTTP request processing service. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">request-server</span> - ICAP server to use for an HTTP request. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">response</span> - Enable/disable whether an HTTP response is passed to an ICAP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">response-failure</span> - Action to take if the ICAP server cannot be contacted when processing an HTTP response. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [error, bypass]</span> </li>
 <li><span class="li-head">response-path</span> - Path component of the ICAP URI that identifies the HTTP response processing service. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">response-server</span> - ICAP server to use for an HTTP response. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">streaming-content-bypass</span> - Enable/disable bypassing of ICAP server for streaming content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure ICAP profiles.
      fmgr_icap_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         icap_profile:
            methods:
              - delete
              - get
              - head
              - options
              - post
              - put
              - trace
              - other
            name: <value of string>
            replacemsg-group: <value of string>
            request: <value in [disable, enable]>
            request-failure: <value in [error, bypass]>
            request-path: <value of string>
            request-server: <value of string>
            response: <value in [disable, enable]>
            response-failure: <value in [error, bypass]>
            response-path: <value of string>
            response-server: <value of string>
            streaming-content-bypass: <value in [disable, enable]>



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



