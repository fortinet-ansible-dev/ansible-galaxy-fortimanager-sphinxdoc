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

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/system/email-server`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">devprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure the email server used by the FortiGate various things. For example, for sending email messages to users to support user authentication features.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">authenticate</span> - Enable/disable authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
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
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

Examples
--------

.. code-block:: yaml+jinja

 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/EMAIL-SERVER
      fmgr_devprof_system_emailserver:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/EMAIL-SERVER
      fmgr_devprof_system_emailserver:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               data:
                  authenticate: <value in [disable, enable]>
                  password:
                    - <value of string>
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
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> authenticate </span> - Enable/disable authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - SMTP server port. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> reply-to </span> - Reply-To email address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> security </span> - Connection security used by the email server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server </span> - SMTP server IP address or hostname. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - SMTP server IPv4 source IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip6 </span> - SMTP server IPv6 source IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-proto-version </span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Use FortiGuard Message service or custom email server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> username </span> - SMTP server user name for authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> validate-server </span> - Enable/disable validation of server certificate. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/email-server</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/email-server</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



