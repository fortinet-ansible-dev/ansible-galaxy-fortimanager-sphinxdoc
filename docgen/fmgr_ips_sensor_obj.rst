:source: fmgr_ips_sensor_obj.py

:orphan:

.. _fmgr_ips_sensor_obj:

fmgr_ips_sensor_obj -- Configure IPS sensor.
++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/ips/sensor/{sensor}`
- `/pm/config/global/obj/ips/sensor/{sensor}`
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
 <li><span class="li-head">loose_validation</span> - Do parameter validation in a loose way <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal">default: false</span>  </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">sensor</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure IPS sensor.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">block-malicious-url</span> - Enable/disable malicious URL blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entries</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action taken with traffic in which signatures are detected. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block, reset, default]</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">exempt-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dst-ip</span> - Destination IP address and netmask. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Exempt IP ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">src-ip</span> - Source IP address and netmask. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">id</span> - Rule ID in IPS database (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">location</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log</span> - Enable/disable logging of signatures included in filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-attack-context</span> - Enable/disable logging of attack context: URL buffer, header buffer, body buffer, packet buffer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-packet</span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">os</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">protocol</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">quarantine</span> - Quarantine method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, attacker, both, interface]</span> </li>
 <li><span class="li-head">quarantine-expiry</span> - Duration of quarantine. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quarantine-log</span> - Enable/disable quarantine logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-count</span> - Count of the rate. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-duration</span> - Duration (sec) of the rate. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rate-mode</span> - Rate limit mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [periodical, continuous]</span> </li>
 <li><span class="li-head">rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip, dhcp-client-mac, dns-domain]</span> </li>
 <li><span class="li-head">rule</span> - Identifies the predefined or custom IPS signatures to add to the sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">severity</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Status of the signatures included in filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, default]</span> </li>
 </ul>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action of selected rules. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block, default, reset]</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">location</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log</span> - Enable/disable logging of selected rules. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, default]</span> </li>
 <li><span class="li-head">log-packet</span> - Enable/disable packet logging of selected rules. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, default]</span> </li>
 <li><span class="li-head">name</span> - Filter name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">protocol</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">quarantine</span> - Quarantine IP or interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, attacker, both, interface]</span> </li>
 <li><span class="li-head">quarantine-expiry</span> - Duration of quarantine in minute. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">quarantine-log</span> - Enable/disable logging of selected quarantine. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Selected rules status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, default]</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Sensor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">override</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action of override rule. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block, reset]</span> </li>
 <li><span class="li-head">exempt-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dst-ip</span> - Destination IP address and netmask. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Exempt IP ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">src-ip</span> - Source IP address and netmask. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-packet</span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">quarantine</span> - Quarantine IP or interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, attacker, both, interface]</span> </li>
 <li><span class="li-head">quarantine-expiry</span> - Duration of quarantine in minute. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">quarantine-log</span> - Enable/disable logging of selected quarantine. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rule-id</span> - Override rule ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable status of override rule. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure IPS sensor.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPS sensor.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}
      fmgr_ips_sensor_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            -
               data:
                  block-malicious-url: <value in [disable, enable]>
                  comment: <value of string>
                  entries:
                    -
                        action: <value in [pass, block, reset, ...]>
                        application:
                          - <value of string>
                        exempt-ip:
                          -
                              dst-ip: <value of string>
                              id: <value of integer>
                              src-ip: <value of string>
                        id: <value of integer>
                        location:
                          - <value of string>
                        log: <value in [disable, enable]>
                        log-attack-context: <value in [disable, enable]>
                        log-packet: <value in [disable, enable]>
                        os:
                          - <value of string>
                        protocol:
                          - <value of string>
                        quarantine: <value in [none, attacker, both, ...]>
                        quarantine-expiry: <value of string>
                        quarantine-log: <value in [disable, enable]>
                        rate-count: <value of integer>
                        rate-duration: <value of integer>
                        rate-mode: <value in [periodical, continuous]>
                        rate-track: <value in [none, src-ip, dest-ip, ...]>
                        rule: <value of string>
                        severity:
                          - <value of string>
                        status: <value in [disable, enable, default]>
                  extended-log: <value in [disable, enable]>
                  filter:
                    -
                        action: <value in [pass, block, default, ...]>
                        application:
                          - <value of string>
                        location:
                          - <value of string>
                        log: <value in [disable, enable, default]>
                        log-packet: <value in [disable, enable, default]>
                        name: <value of string>
                        os:
                          - <value of string>
                        protocol:
                          - <value of string>
                        quarantine: <value in [none, attacker, both, ...]>
                        quarantine-expiry: <value of integer>
                        quarantine-log: <value in [disable, enable]>
                        severity:
                          - <value of string>
                        status: <value in [disable, enable, default]>
                  name: <value of string>
                  override:
                    -
                        action: <value in [pass, block, reset]>
                        exempt-ip:
                          -
                              dst-ip: <value of string>
                              id: <value of integer>
                              src-ip: <value of string>
                        log: <value in [disable, enable]>
                        log-packet: <value in [disable, enable]>
                        quarantine: <value in [none, attacker, both, ...]>
                        quarantine-expiry: <value of integer>
                        quarantine-log: <value in [disable, enable]>
                        rule-id: <value of integer>
                        status: <value in [disable, enable]>
                  replacemsg-group: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}
      fmgr_ips_sensor_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/ips/sensor/{sensor}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> block-malicious-url </span> - Enable/disable malicious URL blocking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> entries </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action taken with traffic in which signatures are detected. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> exempt-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dst-ip </span> - Destination IP address and netmask. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Exempt IP ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> src-ip </span> - Source IP address and netmask. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - Rule ID in IPS database (0 - 4294967295). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> location </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log </span> - Enable/disable logging of signatures included in filter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-attack-context </span> - Enable/disable logging of attack context: URL buffer, header buffer, body buffer, packet buffer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-packet </span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> os </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> protocol </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> quarantine </span> - Quarantine method. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-expiry </span> - Duration of quarantine. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-log </span> - Enable/disable quarantine logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-count </span> - Count of the rate. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rate-duration </span> - Duration (sec) of the rate. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rate-mode </span> - Rate limit mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-track </span> - Track the packet protocol field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rule </span> - Identifies the predefined or custom IPS signatures to add to the sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - Status of the signatures included in filter. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> extended-log </span> - Enable/disable extended logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action of selected rules. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> location </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log </span> - Enable/disable logging of selected rules. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-packet </span> - Enable/disable packet logging of selected rules. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Filter name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> os </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> protocol </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> quarantine </span> - Quarantine IP or interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-expiry </span> - Duration of quarantine in minute. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> quarantine-log </span> - Enable/disable logging of selected quarantine. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - Selected rules status. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Sensor name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> override </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action of override rule. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exempt-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dst-ip </span> - Destination IP address and netmask. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Exempt IP ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> src-ip </span> - Source IP address and netmask. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-packet </span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine </span> - Quarantine IP or interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-expiry </span> - Duration of quarantine in minute. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> quarantine-log </span> - Enable/disable logging of selected quarantine. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rule-id </span> - Override rule ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable status of override rule. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/ips/sensor/{sensor}</span>  </li>
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



