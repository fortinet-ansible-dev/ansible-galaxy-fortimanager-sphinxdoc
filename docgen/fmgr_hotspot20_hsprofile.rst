:source: fmgr_hotspot20_hsprofile.py

:orphan:

.. _fmgr_hotspot20_hsprofile:

fmgr_hotspot20_hsprofile -- Configure hotspot profile.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>hotspot20_hsprofile</td>
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
 <li><span class="li-head">hotspot20_hsprofile</span> - Configure hotspot profile. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">3gpp-plmn</span> - 3GPP PLMN name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">access-network-asra</span> - Enable/disable additional step required for access (ASRA). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">access-network-esr</span> - Enable/disable emergency services reachable (ESR). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">access-network-internet</span> - Enable/disable connectivity to the Internet. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">access-network-type</span> - Access network type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [private-network, private-network-with-guest-access, chargeable-public-network, free-public-network, personal-device-network, emergency-services-only-network, test-or-experimental, wildcard]</span> </li>
 <li><span class="li-head">access-network-uesa</span> - Enable/disable unauthenticated emergency service accessible (UESA). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">anqp-domain-id</span> - ANQP Domain ID (0-65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bss-transition</span> - Enable/disable basic service set (BSS) transition Support. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">conn-cap</span> - Connection capability name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deauth-request-timeout</span> - Deauthentication request timeout (in seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dgaf</span> - Enable/disable downstream group-addressed forwarding (DGAF). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">domain-name</span> - Domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gas-comeback-delay</span> - GAS comeback delay (0 or 100 - 4000 milliseconds, default = 500). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gas-fragmentation-limit</span> - GAS fragmentation limit (512 - 4096, default = 1024). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">hessid</span> - Homogeneous extended service set identifier (HESSID). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-addr-type</span> - IP address type name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">l2tif</span> - Enable/disable Layer 2 traffic inspection and filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nai-realm</span> - NAI realm list name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Hotspot profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">network-auth</span> - Network authentication name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oper-friendly-name</span> - Operator friendly name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">osu-provider</span> - Manually selected list of OSU provider(s). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">osu-ssid</span> - Online sign up (OSU) SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pame-bi</span> - Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">proxy-arp</span> - Enable/disable Proxy ARP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">qos-map</span> - QoS MAP set ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">roaming-consortium</span> - Roaming consortium list name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">venue-group</span> - Venue group. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unspecified, assembly, business, educational, factory, institutional, mercantile, residential, storage, utility, vehicular, outdoor]</span> </li>
 <li><span class="li-head">venue-name</span> - Venue name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">venue-type</span> - Venue type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unspecified, arena, stadium, passenger-terminal, amphitheater, amusement-park, place-of-worship, convention-center, library, museum, restaurant, theater, bar, coffee-shop, zoo-or-aquarium, emergency-center, doctor-office, bank, fire-station, police-station, post-office, professional-office, research-facility, attorney-office, primary-school, secondary-school, university-or-college, factory, hospital, long-term-care-facility, rehab-center, group-home, prison-or-jail, retail-store, grocery-market, auto-service-station, shopping-mall, gas-station, private, hotel-or-motel, dormitory, boarding-house, automobile, airplane, bus, ferry, ship-or-boat, train, motor-bike, muni-mesh-network, city-park, rest-area, traffic-control, bus-stop, kiosk]</span> </li>
 <li><span class="li-head">wan-metrics</span> - WAN metric name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wnm-sleep-mode</span> - Enable/disable wireless network management (WNM) sleep mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure hotspot profile.
      fmgr_hotspot20_hsprofile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         hotspot20_hsprofile:
            3gpp-plmn: <value of string>
            access-network-asra: <value in [disable, enable]>
            access-network-esr: <value in [disable, enable]>
            access-network-internet: <value in [disable, enable]>
            access-network-type: <value in [private-network, private-network-with-guest-access, chargeable-public-network, ...]>
            access-network-uesa: <value in [disable, enable]>
            anqp-domain-id: <value of integer>
            bss-transition: <value in [disable, enable]>
            conn-cap: <value of string>
            deauth-request-timeout: <value of integer>
            dgaf: <value in [disable, enable]>
            domain-name: <value of string>
            gas-comeback-delay: <value of integer>
            gas-fragmentation-limit: <value of integer>
            hessid: <value of string>
            ip-addr-type: <value of string>
            l2tif: <value in [disable, enable]>
            nai-realm: <value of string>
            name: <value of string>
            network-auth: <value of string>
            oper-friendly-name: <value of string>
            osu-provider: <value of string>
            osu-ssid: <value of string>
            pame-bi: <value in [disable, enable]>
            proxy-arp: <value in [disable, enable]>
            qos-map: <value of string>
            roaming-consortium: <value of string>
            venue-group: <value in [unspecified, assembly, business, ...]>
            venue-name: <value of string>
            venue-type: <value in [unspecified, arena, stadium, ...]>
            wan-metrics: <value of string>
            wnm-sleep-mode: <value in [disable, enable]>



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



