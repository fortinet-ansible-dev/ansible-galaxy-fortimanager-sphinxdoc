:source: fmgr_switchcontroller_managedswitch_ports.py

:orphan:

.. _fmgr_switchcontroller_managedswitch_ports:

fmgr_switchcontroller_managedswitch_ports -- Managed-switch port list.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">managed-switch</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">switchcontroller_managedswitch_ports</span> - Managed-switch port list. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">allowed-vlans</span> - Configure switch port tagged vlans <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">allowed-vlans-all</span> - Enable/disable all defined vlans on this port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">arp-inspection-trust</span> - Trusted or untrusted dynamic ARP inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [untrusted, trusted]</span> </li>
 <li><span class="li-head">bundle</span> - Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">description</span> - Description for port. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-snoop-option82-trust</span> - Enable/disable allowance of DHCP with option-82 on untrusted interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-snooping</span> - Trusted or untrusted DHCP-snooping interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [trusted, untrusted]</span> </li>
 <li><span class="li-head">discard-mode</span> - Configure discard mode for port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, all-untagged, all-tagged]</span> </li>
 <li><span class="li-head">edge-port</span> - Enable/disable this interface as an edge port, bridging connections between workstations and/or computers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmp-snooping</span> - Set IGMP snooping mode for the physical port interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-reports</span> - Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-traffic</span> - Enable/disable flooding of IGMP snooping traffic to this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-speed</span> - end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slow, fast]</span> </li>
 <li><span class="li-head">learning-limit</span> - Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lldp-profile</span> - LLDP port TLV profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">lldp-status</span> - LLDP transmit and receive status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, rx-only, tx-only, tx-rx]</span> </li>
 <li><span class="li-head">loop-guard</span> - Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">loop-guard-timeout</span> - Loop-guard timeout (0 - 120 min, default = 45). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-bundle</span> - Maximum size of LAG bundle (1 - 24, default = 24) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mclag</span> - Enable/disable multi-chassis link aggregation (MCLAG). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">member-withdrawal-behavior</span> - Port behavior after it withdraws because of loss of control packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [forward, block]</span> </li>
 <li><span class="li-head">members</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">min-bundle</span> - Minimum size of LAG bundle (1 - 24, default = 1) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - LACP mode: ignore and do not send control messages, or negotiate 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, lacp-passive, lacp-active]</span> </li>
 <li><span class="li-head">poe-pre-standard-detection</span> - Enable/disable PoE pre-standard detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">poe-status</span> - Enable/disable PoE status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port-name</span> - Switch port name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-owner</span> - Switch port name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-security-policy</span> - Switch controller authentication policy to apply to this managed switch from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-selection-criteria</span> - Algorithm for aggregate port selection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [src-mac, dst-mac, src-dst-mac, src-ip, dst-ip, src-dst-ip]</span> </li>
 <li><span class="li-head">qos-policy</span> - Switch controller QoS policy from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sample-direction</span> - sFlow sample direction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rx, tx, both]</span> </li>
 <li><span class="li-head">sflow-counter-interval</span> - sFlow sampler counter polling interval (1 - 255 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sample-rate</span> - sFlow sampler sample rate (0 - 99999 p/sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sampler</span> - Enable/disable sFlow protocol on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard</span> - Enable/disable STP BPDU guard on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard-timeout</span> - BPDU Guard disabling protection (0 - 120 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">stp-root-guard</span> - Enable/disable STP root guard on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-state</span> - Enable/disable Spanning Tree Protocol (STP) on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">type</span> - Interface type: physical or trunk port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [physical, trunk]</span> </li>
 <li><span class="li-head">untagged-vlans</span> - Configure switch port untagged vlans <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan</span> - Assign switch ports to a VLAN. <span class="li-normal">type: str</span> </li>
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
    - name: Managed-switch port list.
      fmgr_switchcontroller_managedswitch_ports:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         managed-switch: <your own value>
         state: <value in [present, absent]>
         switchcontroller_managedswitch_ports:
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
            members: <value of string>
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



