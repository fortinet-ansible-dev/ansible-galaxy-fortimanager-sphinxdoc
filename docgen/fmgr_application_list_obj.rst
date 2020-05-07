:source: fmgr_application_list_obj.py

:orphan:

.. _fmgr_application_list_obj:

fmgr_application_list_obj -- Configure application control lists.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/application/list/{list}`
- `/pm/config/global/obj/application/list/{list}`
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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">list</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure application control lists.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">app-replacemsg</span> - Enable/disable replacement messages for blocked applications. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - comments <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deep-app-inspection</span> - Enable/disable deep application inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">entries</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Pass or block traffic, or reset connection for traffic from this application. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block, reset]</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">behavior</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">category</span> - Category ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging for this application list. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-packet</span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">parameters</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Parameter ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">value</span> - Parameter value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">per-ip-shaper</span> - Per-IP traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">popularity</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 3, 4, 5]</span> </li>
 </ul>
 <li><span class="li-head">protocols</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">quarantine</span> - Quarantine method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, attacker]</span> </li>
 <li><span class="li-head">quarantine-expiry</span> - Duration of quarantine. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quarantine-log</span> - Enable/disable quarantine logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-count</span> - Count of the rate. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-duration</span> - Duration (sec) of the rate. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-mode</span> - Rate limit mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [periodical, continuous]</span> </li>
 <li><span class="li-head">rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip, dhcp-client-mac, dns-domain]</span> </li>
 <li><span class="li-head">risk</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">session-ttl</span> - Session TTL (0 = default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">shaper</span> - Traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">shaper-reverse</span> - Reverse traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sub-category</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">technology</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">vendor</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - List name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow-dns, allow-icmp, allow-http, allow-ssl, allow-quic]</span> </li>
 </ul>
 <li><span class="li-head">other-application-action</span> - Action for other applications. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block]</span> </li>
 <li><span class="li-head">other-application-log</span> - Enable/disable logging for other applications. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">p2p-black-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [skype, edonkey, bittorrent]</span> </li>
 </ul>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">unknown-application-action</span> - Pass or block traffic from unknown applications. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block]</span> </li>
 <li><span class="li-head">unknown-application-log</span> - Enable/disable logging for unknown applications. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure application control lists.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure application control lists.</li>
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

   - To run in workspace mode, the paremeter workspace_locking_adom must be included in the task

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

    - name: REQUESTING /PM/CONFIG/OBJ/APPLICATION/LIST/{LIST}
      fmgr_application_list_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            list: <value of string>
         params:
            -
               data:
                  app-replacemsg: <value in [disable, enable]>
                  comment: <value of string>
                  deep-app-inspection: <value in [disable, enable]>
                  entries:
                    -
                        action: <value in [pass, block, reset]>
                        application:
                          - <value of integer>
                        behavior:
                          - <value of string>
                        category: <value of string>
                        id: <value of integer>
                        log: <value in [disable, enable]>
                        log-packet: <value in [disable, enable]>
                        parameters:
                          -
                              id: <value of integer>
                              value: <value of string>
                        per-ip-shaper: <value of string>
                        popularity:
                          - <value in [1, 2, 3, ...]>
                        protocols:
                          - <value of string>
                        quarantine: <value in [none, attacker]>
                        quarantine-expiry: <value of string>
                        quarantine-log: <value in [disable, enable]>
                        rate-count: <value of integer>
                        rate-duration: <value of integer>
                        rate-mode: <value in [periodical, continuous]>
                        rate-track: <value in [none, src-ip, dest-ip, ...]>
                        risk:
                          - <value of integer>
                        session-ttl: <value of integer>
                        shaper: <value of string>
                        shaper-reverse: <value of string>
                        sub-category:
                          - <value of integer>
                        technology:
                          - <value of string>
                        vendor:
                          - <value of string>
                  extended-log: <value in [disable, enable]>
                  name: <value of string>
                  options:
                    - <value in [allow-dns, allow-icmp, allow-http, ...]>
                  other-application-action: <value in [pass, block]>
                  other-application-log: <value in [disable, enable]>
                  p2p-black-list:
                    - <value in [skype, edonkey, bittorrent]>
                  replacemsg-group: <value of string>
                  unknown-application-action: <value in [pass, block]>
                  unknown-application-log: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/APPLICATION/LIST/{LIST}
      fmgr_application_list_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            list: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/application/list/{list}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> app-replacemsg </span> - Enable/disable replacement messages for blocked applications. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - comments <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deep-app-inspection </span> - Enable/disable deep application inspection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> entries </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Pass or block traffic, or reset connection for traffic from this application. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> behavior </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> category </span> - Category ID list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Entry ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging for this application list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-packet </span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> parameters </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Parameter ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> value </span> - Parameter value. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> per-ip-shaper </span> - Per-IP traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> popularity </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> protocols </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> quarantine </span> - Quarantine method. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-expiry </span> - Duration of quarantine. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-log </span> - Enable/disable quarantine logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-count </span> - Count of the rate. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rate-duration </span> - Duration (sec) of the rate. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rate-mode </span> - Rate limit mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-track </span> - Track the packet protocol field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> risk </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> session-ttl </span> - Session TTL (0 = default). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> shaper </span> - Traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> shaper-reverse </span> - Reverse traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sub-category </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> technology </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> vendor </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> extended-log </span> - Enable/disable extended logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - List name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> options </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> other-application-action </span> - Action for other applications. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> other-application-log </span> - Enable/disable logging for other applications. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> p2p-black-list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unknown-application-action </span> - Pass or block traffic from unknown applications. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unknown-application-log </span> - Enable/disable logging for unknown applications. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/application/list/{list}</span>  </li>
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



