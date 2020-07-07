:source: fmgr_switchcontroller_managedswitch.py

:orphan:

.. _fmgr_switchcontroller_managedswitch:

fmgr_switchcontroller_managedswitch -- Configure FortiSwitch devices that are managed by this FortiGate.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">switchcontroller_managedswitch</span> - Configure FortiSwitch devices that are managed by this FortiGate. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_platform</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allowed-vlans</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">allowed-vlans-all</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">arp-inspection-trust</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [untrusted, trusted]</span> </li>
 <li><span class="li-head">bundle</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-snoop-option82-trust</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-snooping</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [trusted, untrusted]</span> </li>
 <li><span class="li-head">discard-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, all-untagged, all-tagged]</span> </li>
 <li><span class="li-head">edge-port</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmp-snooping</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-reports</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-traffic</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-speed</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slow, fast]</span> </li>
 <li><span class="li-head">learning-limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lldp-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">lldp-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, rx-only, tx-only, tx-rx]</span> </li>
 <li><span class="li-head">loop-guard</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">loop-guard-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-bundle</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mclag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">member-withdrawal-behavior</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [forward, block]</span> </li>
 <li><span class="li-head">members</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">min-bundle</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, lacp-passive, lacp-active]</span> </li>
 <li><span class="li-head">poe-pre-standard-detection</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">poe-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-owner</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-security-policy</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-selection-criteria</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [src-mac, dst-mac, src-dst-mac, src-ip, dst-ip, src-dst-ip]</span> </li>
 <li><span class="li-head">qos-policy</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sample-direction</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rx, tx, both]</span> </li>
 <li><span class="li-head">sflow-counter-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sample-rate</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sampler</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">stp-root-guard</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-state</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [physical, trunk]</span> </li>
 <li><span class="li-head">untagged-vlans</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">switch-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: Configure FortiSwitch devices that are managed by this FortiGate.
      fmgr_switchcontroller_managedswitch:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         switchcontroller_managedswitch:
            _platform: <value of string>
            description: <value of string>
            name: <value of string>
            ports:
              -
                  allowed-vlans: <value of string>
                  allowed-vlans-all: <value in [disable, enable]>
                  arp-inspection-trust: <value in [untrusted, trusted]>
                  bundle: <value in [disable, enable]>
                  description: <value of string>
                  dhcp-snoop-option82-trust: <value in [disable, enable]>
                  dhcp-snooping: <value in [trusted, untrusted]>
                  discard-mode: <value in [none, all-untagged, all-tagged]>
                  edge-port: <value in [disable, enable]>
                  igmp-snooping: <value in [disable, enable]>
                  igmps-flood-reports: <value in [disable, enable]>
                  igmps-flood-traffic: <value in [disable, enable]>
                  lacp-speed: <value in [slow, fast]>
                  learning-limit: <value of integer>
                  lldp-profile: <value of string>
                  lldp-status: <value in [disable, rx-only, tx-only, ...]>
                  loop-guard: <value in [disabled, enabled]>
                  loop-guard-timeout: <value of integer>
                  max-bundle: <value of integer>
                  mclag: <value in [disable, enable]>
                  member-withdrawal-behavior: <value in [forward, block]>
                  members:
                    - <value of string>
                  min-bundle: <value of integer>
                  mode: <value in [static, lacp-passive, lacp-active]>
                  poe-pre-standard-detection: <value in [disable, enable]>
                  poe-status: <value in [disable, enable]>
                  port-name: <value of string>
                  port-owner: <value of string>
                  port-security-policy: <value of string>
                  port-selection-criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
                  qos-policy: <value of string>
                  sample-direction: <value in [rx, tx, both]>
                  sflow-counter-interval: <value of integer>
                  sflow-sample-rate: <value of integer>
                  sflow-sampler: <value in [disabled, enabled]>
                  stp-bpdu-guard: <value in [disabled, enabled]>
                  stp-bpdu-guard-timeout: <value of integer>
                  stp-root-guard: <value in [disabled, enabled]>
                  stp-state: <value in [disabled, enabled]>
                  type: <value in [physical, trunk]>
                  untagged-vlans: <value of string>
                  vlan: <value of string>
            switch-id: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
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



