:source: fmgr_emailfilter_profile.py

:orphan:

.. _fmgr_emailfilter_profile:

fmgr_emailfilter_profile -- Configure Email Filter profiles.
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



FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <br>
 <table>
 <tr>
 <td></td>
 <td><code class="docutils literal notranslate">6.2.1 </code></td>
 <td><code class="docutils literal notranslate">6.4.0 </code></td>
 <td><code class="docutils literal notranslate">7.0.0 </code></td>
 </tr>
 <tr>
 <td>emailfilter_profile</td>
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
 <li><span class="li-head">emailfilter_profile</span> - Configure Email Filter profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external</span> - Enable/disable external Email inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, bannedword, spambwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambal]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spam-bwl-table</span> - Anti-spam black/white list table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spam-bword-table</span> - Anti-spam banned word table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spam-bword-threshold</span> - Spam banned word threshold. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">spam-filtering</span> - Enable/disable spam filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spam-iptrust-table</span> - Anti-spam IP trust table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spam-log</span> - Enable/disable spam logging for email filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spam-log-fortiguard-response</span> - Enable/disable logging FortiGuard spam response. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spam-mheader-table</span> - Anti-spam MIME header table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spam-rbl-table</span> - Anti-spam DNSBL table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">feature-set</span> - Flow/proxy feature set. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">gmail</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">log-all</span> - Enable/disable logging of all email traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">imap</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action for spam email. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, tag]</span> </li>
 <li><span class="li-head">log-all</span> - Enable/disable logging of all email traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tag-msg</span> - Subject text or header added to spam email. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tag-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [subject, header, spaminfo]</span> </li>
 </ul>
 <li><span class="li-head">mapi</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action for spam email. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard]</span> </li>
 <li><span class="li-head">log-all</span> - Enable/disable logging of all email traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">msn-hotmail</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">log-all</span> - Enable/disable logging of all email traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">other-webmails</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">log-all</span> - Enable/disable logging of all email traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">pop3</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action for spam email. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, tag]</span> </li>
 <li><span class="li-head">log-all</span> - Enable/disable logging of all email traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tag-msg</span> - Subject text or header added to spam email. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tag-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [subject, header, spaminfo]</span> </li>
 </ul>
 <li><span class="li-head">smtp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - Action for spam email. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, tag, discard]</span> </li>
 <li><span class="li-head">hdrip</span> - Enable/disable SMTP email header IP checks for spamfsip, spamrbl and spambal filters. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-override</span> - Enable/disable local filter to override SMTP remote check result. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-all</span> - Enable/disable logging of all email traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tag-msg</span> - Subject text or header added to spam email. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tag-type</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [subject, header, spaminfo]</span> </li>
 </ul>
 <li><span class="li-head">spam-bal-table</span> - Anti-spam block/allow list table ID. <span class="li-normal">type: str</span> </li>
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
    - name: Configure Email Filter profiles.
      fmgr_emailfilter_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         emailfilter_profile:
            comment: <value of string>
            external: <value in [disable, enable]>
            name: <value of string>
            options:
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - bannedword
              - spambwl
              - spamfsip
              - spamfssubmit
              - spamfschksum
              - spamfsurl
              - spamhelodns
              - spamraddrdns
              - spamrbl
              - spamhdrcheck
              - spamfsphish
              - spambal
            replacemsg-group: <value of string>
            spam-bwl-table: <value of string>
            spam-bword-table: <value of string>
            spam-bword-threshold: <value of integer>
            spam-filtering: <value in [disable, enable]>
            spam-iptrust-table: <value of string>
            spam-log: <value in [disable, enable]>
            spam-log-fortiguard-response: <value in [disable, enable]>
            spam-mheader-table: <value of string>
            spam-rbl-table: <value of string>
            feature-set: <value in [proxy, flow]>
            gmail:
               log-all: <value in [disable, enable]>
            imap:
               action: <value in [pass, tag]>
               log-all: <value in [disable, enable]>
               tag-msg: <value of string>
               tag-type:
                 - subject
                 - header
                 - spaminfo
            mapi:
               action: <value in [pass, discard]>
               log-all: <value in [disable, enable]>
            msn-hotmail:
               log-all: <value in [disable, enable]>
            other-webmails:
               log-all: <value in [disable, enable]>
            pop3:
               action: <value in [pass, tag]>
               log-all: <value in [disable, enable]>
               tag-msg: <value of string>
               tag-type:
                 - subject
                 - header
                 - spaminfo
            smtp:
               action: <value in [pass, tag, discard]>
               hdrip: <value in [disable, enable]>
               local-override: <value in [disable, enable]>
               log-all: <value in [disable, enable]>
               tag-msg: <value of string>
               tag-type:
                 - subject
                 - header
                 - spaminfo
            spam-bal-table: <value of string>



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



