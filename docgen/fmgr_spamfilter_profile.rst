:source: fmgr_spamfilter_profile.py

:orphan:

.. _fmgr_spamfilter_profile:

fmgr_spamfilter_profile -- Configure AntiSpam profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/spamfilter/profile`
- `/pm/config/global/obj/spamfilter/profile`
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
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure AntiSpam profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external</span> - Enable/disable external Email inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">flow-based</span> - Enable/disable flow-based spam filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bannedword, spamemailbwl, spamfsip, spamfssubmit, spamfschksum, spamfsurl, spamhelodns, spamipbwl, spamraddrdns, spamrbl, spamhdrcheck, spamfsphish, spambwl]</span> </li>
 </ul>
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
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure AntiSpam profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [comment, external, flow-based, name, options, replacemsg-group, spam-bwl-table, spam-bword-table, spam-bword-threshold, spam-filtering, spam-iptrust-table, spam-log, spam-log-fortiguard-response, spam-mheader-table, spam-rbl-table]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">get used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, datasrc, get reserved, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/PROFILE
      fmgr_spamfilter_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     comment: <value of string>
                     external: <value in [disable, enable]>
                     flow-based: <value in [disable, enable]>
                     name: <value of string>
                     options:
                       - <value in [bannedword, spamemailbwl, spamfsip, ...]>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/PROFILE
      fmgr_spamfilter_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [comment, external, flow-based, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/spamfilter/profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> external </span> - Enable/disable external Email inspection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> flow-based </span> - Enable/disable flow-based spam filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> options </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-bwl-table </span> - Anti-spam black/white list table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-bword-table </span> - Anti-spam banned word table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-bword-threshold </span> - Spam banned word threshold. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> spam-filtering </span> - Enable/disable spam filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-iptrust-table </span> - Anti-spam IP trust table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-log </span> - Enable/disable spam logging for email filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-log-fortiguard-response </span> - Enable/disable logging FortiGuard spam response. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-mheader-table </span> - Anti-spam MIME header table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spam-rbl-table </span> - Anti-spam DNSBL table ID. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/spamfilter/profile</span>  </li>
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



