:source: fmgr_devprof_system_emailserver.py

:orphan:

.. _fmgr_devprof_system_emailserver:

fmgr_devprof_system_emailserver -- Configure the email server used by the FortiGate various things.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">devprof_system_emailserver</span> - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authen... <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">authenticate</span> - Enable/disable authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">port</span> - SMTP server port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">reply-to</span> - Reply-To email address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security</span> - Connection security used by the email server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, starttls, smtps]</span> </li>
 <li><span class="li-head">server</span> - SMTP server IP address or hostname. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - SMTP server IPv4 source IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip6</span> - SMTP server IPv6 source IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1, TLSv1-1, TLSv1-2, SSLv3]</span> </li>
 <li><span class="li-head">type</span> - Use FortiGuard Message service or custom email server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [custom]</span> </li>
 <li><span class="li-head">username</span> - SMTP server user name for authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">validate-server</span> - Enable/disable validation of server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authen...
      fmgr_devprof_system_emailserver:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         devprof: <your own value>
         devprof_system_emailserver:
            authenticate: <value in [disable, enable]>
            password: <value of string>
            port: <value of integer>
            reply-to: <value of string>
            security: <value in [none, starttls, smtps]>
            server: <value of string>
            source-ip: <value of string>
            source-ip6: <value of string>
            ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
            type: <value in [custom]>
            username: <value of string>
            validate-server: <value in [disable, enable]>



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



