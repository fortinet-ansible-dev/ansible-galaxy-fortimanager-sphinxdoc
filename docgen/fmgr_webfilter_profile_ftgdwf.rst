:source: fmgr_webfilter_profile_ftgdwf.py

:orphan:

.. _fmgr_webfilter_profile_ftgdwf:

fmgr_webfilter_profile_ftgdwf -- FortiGuard Web Filter settings.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">profile</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">webfilter_profile_ftgdwf</span> - FortiGuard Web Filter settings. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">exempt-quota</span> - Do not stop quota for these categories. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filters</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take for matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, monitor, warning, authenticate]</span> </li>
 <li><span class="li-head">auth-usr-grp</span> - Groups with permission to authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">category</span> - Categories and groups the filter examines. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">override-replacemsg</span> - Override replacement message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">warn-duration</span> - Duration of warnings. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">warning-duration-type</span> - Re-display warning after closing browser or after a timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session, timeout]</span> </li>
 <li><span class="li-head">warning-prompt</span> - Warning prompts in each category or each domain. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [per-domain, per-category]</span> </li>
 </ul>
 <li><span class="li-head">max-quota-timeout</span> - Maximum FortiGuard quota used by single page view in seconds (excludes streams). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [error-allow, http-err-detail, rate-image-urls, strict-blocking, rate-server-ip, redir-block, connect-request-bypass, log-all-url, ftgd-disable]</span> </li>
 <li><span class="li-head">ovrd</span> - Allow web filter profile overrides. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quota</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - FortiGuard categories to apply quota to (category action must be set to monitor). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">duration</span> - Duration of quota. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">override-replacemsg</span> - Override replacement message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Quota type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [time, traffic]</span> </li>
 <li><span class="li-head">unit</span> - Traffic quota unit of measurement. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [B, KB, MB, GB]</span> </li>
 <li><span class="li-head">value</span> - Traffic quota value. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">rate-crl-urls</span> - Enable/disable rating CRL by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-css-urls</span> - Enable/disable rating CSS by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-image-urls</span> - Enable/disable rating images by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-javascript-urls</span> - Enable/disable rating JavaScript by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: FortiGuard Web Filter settings.
      fmgr_webfilter_profile_ftgdwf:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         profile: <your own value>
         webfilter_profile_ftgdwf:
            exempt-quota: <value of string>
            filters:
              -
                  action: <value in [block, monitor, warning, ...]>
                  auth-usr-grp: <value of string>
                  category: <value of string>
                  id: <value of integer>
                  log: <value in [disable, enable]>
                  override-replacemsg: <value of string>
                  warn-duration: <value of string>
                  warning-duration-type: <value in [session, timeout]>
                  warning-prompt: <value in [per-domain, per-category]>
            max-quota-timeout: <value of integer>
            options:
              - error-allow
              - http-err-detail
              - rate-image-urls
              - strict-blocking
              - rate-server-ip
              - redir-block
              - connect-request-bypass
              - log-all-url
              - ftgd-disable
            ovrd: <value of string>
            quota:
              -
                  category: <value of string>
                  duration: <value of string>
                  id: <value of integer>
                  override-replacemsg: <value of string>
                  type: <value in [time, traffic]>
                  unit: <value in [B, KB, MB, ...]>
                  value: <value of integer>
            rate-crl-urls: <value in [disable, enable]>
            rate-css-urls: <value in [disable, enable]>
            rate-image-urls: <value in [disable, enable]>
            rate-javascript-urls: <value in [disable, enable]>



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



