:source: fmgr_webfilter_profile_obj.py

:orphan:

.. _fmgr_webfilter_profile_obj:

fmgr_webfilter_profile_obj -- Configure Web filter profiles.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/webfilter/profile/{profile}`
- `/pm/config/global/obj/webfilter/profile/{profile}`
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
 <li><span class="li-head">profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure Web filter profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging for web filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">https-replacemsg</span> - Enable replacement messages for HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">inspection-mode</span> - Web filtering inspection mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow-based, dns]</span> </li>
 <li><span class="li-head">log-all-url</span> - Enable/disable logging all URLs visited. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check]</span> </li>
 </ul>
 <li><span class="li-head">ovrd-perm</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bannedword-override, urlfilter-override, fortiguard-wf-override, contenttype-check-override]</span> </li>
 </ul>
 <li><span class="li-head">post-action</span> - Action taken for HTTP POST traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [normal, comfort, block]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">web-content-log</span> - Enable/disable logging logging blocked web content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-extended-all-action-log</span> - Enable/disable extended any filter action logging for web filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-activex-log</span> - Enable/disable logging ActiveX. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-applet-log</span> - Enable/disable logging Java applets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-command-block-log</span> - Enable/disable logging blocked commands. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-cookie-log</span> - Enable/disable logging cookie filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-cookie-removal-log</span> - Enable/disable logging blocked cookies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-js-log</span> - Enable/disable logging Java scripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-jscript-log</span> - Enable/disable logging JScripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-referer-log</span> - Enable/disable logging referrers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-unknown-log</span> - Enable/disable logging unknown scripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-vbs-log</span> - Enable/disable logging VBS scripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-ftgd-err-log</span> - Enable/disable logging rating errors. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-ftgd-quota-usage</span> - Enable/disable logging daily quota usage. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-invalid-domain-log</span> - Enable/disable logging invalid domain names. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-url-log</span> - Enable/disable logging URL filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wisp</span> - Enable/disable web proxy WISP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wisp-algorithm</span> - WISP server selection algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto-learning, primary-secondary, round-robin]</span> </li>
 <li><span class="li-head">wisp-servers</span> - WISP servers. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">youtube-channel-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">channel-id</span> - YouTube channel ID to be filtered. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">youtube-channel-status</span> - YouTube channel filter status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, blacklist, whitelist]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure Web filter profiles.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure Web filter profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}
      fmgr_webfilter_profile_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  comment: <value of string>
                  extended-log: <value in [disable, enable]>
                  https-replacemsg: <value in [disable, enable]>
                  inspection-mode: <value in [proxy, flow-based, dns]>
                  log-all-url: <value in [disable, enable]>
                  name: <value of string>
                  options:
                    - <value in [block-invalid-url, jscript, js, ...]>
                  ovrd-perm:
                    - <value in [bannedword-override, urlfilter-override, fortiguard-wf-override, ...]>
                  post-action: <value in [normal, comfort, block]>
                  replacemsg-group: <value of string>
                  web-content-log: <value in [disable, enable]>
                  web-extended-all-action-log: <value in [disable, enable]>
                  web-filter-activex-log: <value in [disable, enable]>
                  web-filter-applet-log: <value in [disable, enable]>
                  web-filter-command-block-log: <value in [disable, enable]>
                  web-filter-cookie-log: <value in [disable, enable]>
                  web-filter-cookie-removal-log: <value in [disable, enable]>
                  web-filter-js-log: <value in [disable, enable]>
                  web-filter-jscript-log: <value in [disable, enable]>
                  web-filter-referer-log: <value in [disable, enable]>
                  web-filter-unknown-log: <value in [disable, enable]>
                  web-filter-vbs-log: <value in [disable, enable]>
                  web-ftgd-err-log: <value in [disable, enable]>
                  web-ftgd-quota-usage: <value in [disable, enable]>
                  web-invalid-domain-log: <value in [disable, enable]>
                  web-url-log: <value in [disable, enable]>
                  wisp: <value in [disable, enable]>
                  wisp-algorithm: <value in [auto-learning, primary-secondary, round-robin]>
                  wisp-servers: <value of string>
                  youtube-channel-filter:
                    -
                        channel-id: <value of string>
                        comment: <value of string>
                        id: <value of integer>
                  youtube-channel-status: <value in [disable, blacklist, whitelist]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}
      fmgr_webfilter_profile_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Optional comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extended-log </span> - Enable/disable extended logging for web filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> https-replacemsg </span> - Enable replacement messages for HTTPS. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inspection-mode </span> - Web filtering inspection mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-all-url </span> - Enable/disable logging all URLs visited. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> options </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ovrd-perm </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> post-action </span> - Action taken for HTTP POST traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-content-log </span> - Enable/disable logging logging blocked web content. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-extended-all-action-log </span> - Enable/disable extended any filter action logging for web filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-activex-log </span> - Enable/disable logging ActiveX. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-applet-log </span> - Enable/disable logging Java applets. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-command-block-log </span> - Enable/disable logging blocked commands. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-cookie-log </span> - Enable/disable logging cookie filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-cookie-removal-log </span> - Enable/disable logging blocked cookies. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-js-log </span> - Enable/disable logging Java scripts. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-jscript-log </span> - Enable/disable logging JScripts. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-referer-log </span> - Enable/disable logging referrers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-unknown-log </span> - Enable/disable logging unknown scripts. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter-vbs-log </span> - Enable/disable logging VBS scripts. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-ftgd-err-log </span> - Enable/disable logging rating errors. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-ftgd-quota-usage </span> - Enable/disable logging daily quota usage. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-invalid-domain-log </span> - Enable/disable logging invalid domain names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-url-log </span> - Enable/disable logging URL filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wisp </span> - Enable/disable web proxy WISP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wisp-algorithm </span> - WISP server selection algorithm. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wisp-servers </span> - WISP servers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> youtube-channel-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> channel-id </span> - YouTube channel ID to be filtered. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> youtube-channel-status </span> - YouTube channel filter status. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}</span>  </li>
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



