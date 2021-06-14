:source: fmgr_dnsfilter_profile.py

:orphan:

.. _fmgr_dnsfilter_profile:

fmgr_dnsfilter_profile -- Configure DNS domain filter profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>dnsfilter_profile</td>
 <td>yes</td>
 <td>yes</td>
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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">dnsfilter_profile</span> - Configure DNS domain filter profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">block-action</span> - Action to take for blocked domains. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, redirect]</span> </li>
 <li><span class="li-head">block-botnet</span> - Enable/disable blocking botnet C&C DNS lookups. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-ip-blocklist</span> - One or more external IP block lists. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">log-all-domain</span> - Enable/disable logging of all domains visited (detailed DNS logging). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">redirect-portal</span> - IP address of the SDNS redirect portal. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">safe-search</span> - Enable/disable Google, Bing, and YouTube safe search. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sdns-domain-log</span> - Enable/disable domain filtering and botnet domain logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sdns-ftgd-err-log</span> - Enable/disable FortiGuard SDNS rating error logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">youtube-restrict</span> - Set safe search for YouTube restriction level. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [strict, moderate]</span> </li>
 <li><span class="li-head">dns-translation</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dst</span> - IPv4 address or subnet on the external network to substitute for the resolved address in DNS query replies. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">netmask</span> - If src and dst are subnets rather than single IP addresses, enter the netmask for both src and dst. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">src</span> - IPv4 address or subnet on the internal network to compare with the resolved address in DNS query replies. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this DNS translation entry. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">addr-type</span> - DNS translation type (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">dst6</span> - IPv6 address or subnet on the external network to substitute for the resolved address in DNS query replies. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">prefix</span> - If src6 and dst6 are subnets rather than single IP addresses, enter the prefix for both src6 and dst6 (1 - 128, default = 128). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">src6</span> - IPv6 address or subnet on the internal network to compare with the resolved address in DNS query replies. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">redirect-portal6</span> - IPv6 address of the SDNS redirect portal. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">domain-filter</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">domain-filter-table</span> - DNS domain filter table ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">ftgd-dns</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">filters</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take for DNS requests matching the category. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [monitor, block]</span> </li>
 <li><span class="li-head">category</span> - Category number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable DNS filter logging for this DNS profile. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [error-allow, ftgd-disable]</span> </li>
 </ul>
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
    - name: Configure DNS domain filter profiles.
      fmgr_dnsfilter_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         dnsfilter_profile:
            block-action: <value in [block, redirect]>
            block-botnet: <value in [disable, enable]>
            comment: <value of string>
            external-ip-blocklist: <value of string>
            log-all-domain: <value in [disable, enable]>
            name: <value of string>
            redirect-portal: <value of string>
            safe-search: <value in [disable, enable]>
            sdns-domain-log: <value in [disable, enable]>
            sdns-ftgd-err-log: <value in [disable, enable]>
            youtube-restrict: <value in [strict, moderate]>
            dns-translation:
              -
                  dst: <value of string>
                  id: <value of integer>
                  netmask: <value of string>
                  src: <value of string>
                  status: <value in [disable, enable]>
                  addr-type: <value in [ipv4, ipv6]>
                  dst6: <value of string>
                  prefix: <value of integer>
                  src6: <value of string>
            redirect-portal6: <value of string>
            domain-filter:
               domain-filter-table: <value of integer>
            ftgd-dns:
               filters:
                 -
                     action: <value in [monitor, block]>
                     category: <value of string>
                     id: <value of integer>
                     log: <value in [disable, enable]>
               options:
                 - error-allow
                 - ftgd-disable



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



