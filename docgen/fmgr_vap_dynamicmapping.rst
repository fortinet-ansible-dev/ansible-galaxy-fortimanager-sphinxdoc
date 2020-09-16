:source: fmgr_vap_dynamicmapping.py

:orphan:

.. _fmgr_vap_dynamicmapping:

fmgr_vap_dynamicmapping
+++++++++++++++++++++++

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
 <li><span class="li-head">vap</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">vap_dynamicmapping</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_centmgmt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_dhcp_svr_id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap]</span> </li>
 <li><span class="li-head">_intf_device-identification</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_device-netscan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_dhcp-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">_intf_dhcp-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_dhcp-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span>  <span class="li-normal">default: regular</span> </li>
 <li><span class="li-head">_intf_dhcp6-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_dhcp6-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_dhcp6-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span>  <span class="li-normal">default: regular</span> </li>
 <li><span class="li-head">_intf_ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_ip6-address</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, any, fgfm, capwap]</span> </li>
 <li><span class="li-head">_intf_listen-forticlient-connection</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">acct-interim-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">address-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">alias</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">atf-weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [PSK, psk, RADIUS, radius, usergroup]</span> </li>
 <li><span class="li-head">broadcast-ssid</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">broadcast-suppression</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [dhcp, arp, dhcp2, arp2, netbios-ns, netbios-ds, arp3, dhcp-up, dhcp-down, arp-known, arp-unknown, arp-reply, ipv6, dhcp-starvation, arp-poison, all-other-mc, all-other-bc, arp-proxy, dhcp-ucast]</span> </li>
 <li><span class="li-head">captive-portal-ac-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">captive-portal-macauth-radius-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">captive-portal-macauth-radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">captive-portal-radius-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">captive-portal-radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">captive-portal-session-timeout-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">client-count</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp-lease-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp-option82-circuit-id-insertion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, style-1, style-2]</span> </li>
 <li><span class="li-head">dhcp-option82-insertion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-option82-remote-id-insertion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, style-1]</span> </li>
 <li><span class="li-head">dynamic-vlan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eap-reauth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eap-reauth-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-key-retries</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">encrypt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TKIP, AES, TKIP-AES]</span> </li>
 <li><span class="li-head">external-fast-roaming</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-logout</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-web</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fast-bss-transition</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fast-roaming</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ft-mobility-domain</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ft-over-ds</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ft-r0-key-lifetime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gtk-rekey</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gtk-rekey-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">hotspot20-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">intra-vap-privacy</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">key</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">keyindex</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldpc</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tx, rx, rxtx]</span> </li>
 <li><span class="li-head">local-authentication</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-bridging</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-lan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">local-standalone</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-standalone-nat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-switching</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-auth-bypass</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-filter</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-filter-policy-other</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">max-clients</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-clients-ap</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">me-disable-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mesh-backhaul</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mpsk</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mpsk-concurrent-clients</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">multicast-enhance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">multicast-rate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [0, 6000, 12000, 24000]</span> </li>
 <li><span class="li-head">okc</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">owe-groups</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [19, 20, 21]</span> </li>
 <li><span class="li-head">owe-transition</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">owe-transition-ssid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passphrase</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">pmf</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, optional]</span> </li>
 <li><span class="li-head">pmf-assoc-comeback-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pmf-sa-query-retry-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">portal-message-override-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">portal-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auth, auth+disclaimer, disclaimer, email-collect, cmcc, cmcc-macauth, auth-mac]</span> </li>
 <li><span class="li-head">probe-resp-suppression</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">probe-resp-threshold</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ptk-rekey</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ptk-rekey-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">qos-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quarantine</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radio-2g-threshold</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radio-5g-threshold</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radio-sensitivity</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-mac-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-mac-auth-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radius-mac-auth-usergroups</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rates-11a</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> </li>
 <li><span class="li-head">rates-11ac-ss12</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/1, mcs9/1, mcs0/2, mcs1/2, mcs2/2, mcs3/2, mcs4/2, mcs5/2, mcs6/2, mcs7/2, mcs8/2, mcs9/2, mcs10/1, mcs11/1, mcs10/2, mcs11/2]</span> </li>
 <li><span class="li-head">rates-11ac-ss34</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [mcs0/3, mcs1/3, mcs2/3, mcs3/3, mcs4/3, mcs5/3, mcs6/3, mcs7/3, mcs8/3, mcs9/3, mcs0/4, mcs1/4, mcs2/4, mcs3/4, mcs4/4, mcs5/4, mcs6/4, mcs7/4, mcs8/4, mcs9/4, mcs10/3, mcs11/3, mcs10/4, mcs11/4]</span> </li>
 <li><span class="li-head">rates-11bg</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> </li>
 <li><span class="li-head">rates-11n-ss12</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/2, mcs9/2, mcs10/2, mcs11/2, mcs12/2, mcs13/2, mcs14/2, mcs15/2]</span> </li>
 <li><span class="li-head">rates-11n-ss34</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [mcs16/3, mcs17/3, mcs18/3, mcs19/3, mcs20/3, mcs21/3, mcs22/3, mcs23/3, mcs24/4, mcs25/4, mcs26/4, mcs27/4, mcs28/4, mcs29/4, mcs30/4, mcs31/4]</span> </li>
 <li><span class="li-head">sae-groups</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31]</span> </li>
 <li><span class="li-head">sae-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, captive-portal, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise, wpa-personal+captive-portal, wpa-only-personal+captive-portal, wpa2-only-personal+captive-portal, osen, wpa3-enterprise, sae, sae-transition, owe, wpa3-sae, wpa3-sae-transition]</span> </li>
 <li><span class="li-head">security-exempt-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-obsolete-option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">security-redirect-url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">selected-usergroups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">split-tunneling</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tkip-counter-measure</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">usergroup</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan-auto</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vlan-pooling</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [wtp-group, round-robin, hash, disable]</span> </li>
 <li><span class="li-head">vlanid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">voice-enterprise</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: no description
      fmgr_vap_dynamicmapping:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vap: <your own value>
         state: <value in [present, absent]>
         vap_dynamicmapping:
            _centmgmt: <value in [disable, enable]>
            _dhcp_svr_id: <value of string>
            _intf_allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
            _intf_device-identification: <value in [disable, enable]>
            _intf_device-netscan: <value in [disable, enable]>
            _intf_dhcp-relay-ip: <value of string>
            _intf_dhcp-relay-service: <value in [disable, enable]>
            _intf_dhcp-relay-type: <value in [regular, ipsec]>
            _intf_dhcp6-relay-ip: <value of string>
            _intf_dhcp6-relay-service: <value in [disable, enable]>
            _intf_dhcp6-relay-type: <value in [regular]>
            _intf_ip: <value of string>
            _intf_ip6-address: <value of string>
            _intf_ip6-allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - any
              - fgfm
              - capwap
            _intf_listen-forticlient-connection: <value in [disable, enable]>
            _scope:
              -
                  name: <value of string>
                  vdom: <value of string>
            acct-interim-interval: <value of integer>
            address-group: <value of string>
            alias: <value of string>
            atf-weight: <value of integer>
            auth: <value in [PSK, psk, RADIUS, ...]>
            broadcast-ssid: <value in [disable, enable]>
            broadcast-suppression:
              - dhcp
              - arp
              - dhcp2
              - arp2
              - netbios-ns
              - netbios-ds
              - arp3
              - dhcp-up
              - dhcp-down
              - arp-known
              - arp-unknown
              - arp-reply
              - ipv6
              - dhcp-starvation
              - arp-poison
              - all-other-mc
              - all-other-bc
              - arp-proxy
              - dhcp-ucast
            captive-portal-ac-name: <value of string>
            captive-portal-macauth-radius-secret: <value of string>
            captive-portal-macauth-radius-server: <value of string>
            captive-portal-radius-secret: <value of string>
            captive-portal-radius-server: <value of string>
            captive-portal-session-timeout-interval: <value of integer>
            client-count: <value of integer>
            dhcp-lease-time: <value of integer>
            dhcp-option82-circuit-id-insertion: <value in [disable, style-1, style-2]>
            dhcp-option82-insertion: <value in [disable, enable]>
            dhcp-option82-remote-id-insertion: <value in [disable, style-1]>
            dynamic-vlan: <value in [disable, enable]>
            eap-reauth: <value in [disable, enable]>
            eap-reauth-intv: <value of integer>
            eapol-key-retries: <value in [disable, enable]>
            encrypt: <value in [TKIP, AES, TKIP-AES]>
            external-fast-roaming: <value in [disable, enable]>
            external-logout: <value of string>
            external-web: <value of string>
            fast-bss-transition: <value in [disable, enable]>
            fast-roaming: <value in [disable, enable]>
            ft-mobility-domain: <value of integer>
            ft-over-ds: <value in [disable, enable]>
            ft-r0-key-lifetime: <value of integer>
            gtk-rekey: <value in [disable, enable]>
            gtk-rekey-intv: <value of integer>
            hotspot20-profile: <value of string>
            intra-vap-privacy: <value in [disable, enable]>
            ip: <value of string>
            key: <value of string>
            keyindex: <value of integer>
            ldpc: <value in [disable, tx, rx, ...]>
            local-authentication: <value in [disable, enable]>
            local-bridging: <value in [disable, enable]>
            local-lan: <value in [deny, allow]>
            local-standalone: <value in [disable, enable]>
            local-standalone-nat: <value in [disable, enable]>
            local-switching: <value in [disable, enable]>
            mac-auth-bypass: <value in [disable, enable]>
            mac-filter: <value in [disable, enable]>
            mac-filter-policy-other: <value in [deny, allow]>
            max-clients: <value of integer>
            max-clients-ap: <value of integer>
            me-disable-thresh: <value of integer>
            mesh-backhaul: <value in [disable, enable]>
            mpsk: <value in [disable, enable]>
            mpsk-concurrent-clients: <value of integer>
            multicast-enhance: <value in [disable, enable]>
            multicast-rate: <value in [0, 6000, 12000, ...]>
            okc: <value in [disable, enable]>
            owe-groups:
              - 19
              - 20
              - 21
            owe-transition: <value in [disable, enable]>
            owe-transition-ssid: <value of string>
            passphrase: <value of string>
            pmf: <value in [disable, enable, optional]>
            pmf-assoc-comeback-timeout: <value of integer>
            pmf-sa-query-retry-timeout: <value of integer>
            portal-message-override-group: <value of string>
            portal-type: <value in [auth, auth+disclaimer, disclaimer, ...]>
            probe-resp-suppression: <value in [disable, enable]>
            probe-resp-threshold: <value of string>
            ptk-rekey: <value in [disable, enable]>
            ptk-rekey-intv: <value of integer>
            qos-profile: <value of string>
            quarantine: <value in [disable, enable]>
            radio-2g-threshold: <value of string>
            radio-5g-threshold: <value of string>
            radio-sensitivity: <value in [disable, enable]>
            radius-mac-auth: <value in [disable, enable]>
            radius-mac-auth-server: <value of string>
            radius-mac-auth-usergroups: <value of string>
            radius-server: <value of string>
            rates-11a:
              - 1
              - 1-basic
              - 2
              - 2-basic
              - 5.5
              - 5.5-basic
              - 6
              - 6-basic
              - 9
              - 9-basic
              - 12
              - 12-basic
              - 18
              - 18-basic
              - 24
              - 24-basic
              - 36
              - 36-basic
              - 48
              - 48-basic
              - 54
              - 54-basic
              - 11
              - 11-basic
            rates-11ac-ss12:
              - mcs0/1
              - mcs1/1
              - mcs2/1
              - mcs3/1
              - mcs4/1
              - mcs5/1
              - mcs6/1
              - mcs7/1
              - mcs8/1
              - mcs9/1
              - mcs0/2
              - mcs1/2
              - mcs2/2
              - mcs3/2
              - mcs4/2
              - mcs5/2
              - mcs6/2
              - mcs7/2
              - mcs8/2
              - mcs9/2
              - mcs10/1
              - mcs11/1
              - mcs10/2
              - mcs11/2
            rates-11ac-ss34:
              - mcs0/3
              - mcs1/3
              - mcs2/3
              - mcs3/3
              - mcs4/3
              - mcs5/3
              - mcs6/3
              - mcs7/3
              - mcs8/3
              - mcs9/3
              - mcs0/4
              - mcs1/4
              - mcs2/4
              - mcs3/4
              - mcs4/4
              - mcs5/4
              - mcs6/4
              - mcs7/4
              - mcs8/4
              - mcs9/4
              - mcs10/3
              - mcs11/3
              - mcs10/4
              - mcs11/4
            rates-11bg:
              - 1
              - 1-basic
              - 2
              - 2-basic
              - 5.5
              - 5.5-basic
              - 6
              - 6-basic
              - 9
              - 9-basic
              - 12
              - 12-basic
              - 18
              - 18-basic
              - 24
              - 24-basic
              - 36
              - 36-basic
              - 48
              - 48-basic
              - 54
              - 54-basic
              - 11
              - 11-basic
            rates-11n-ss12:
              - mcs0/1
              - mcs1/1
              - mcs2/1
              - mcs3/1
              - mcs4/1
              - mcs5/1
              - mcs6/1
              - mcs7/1
              - mcs8/2
              - mcs9/2
              - mcs10/2
              - mcs11/2
              - mcs12/2
              - mcs13/2
              - mcs14/2
              - mcs15/2
            rates-11n-ss34:
              - mcs16/3
              - mcs17/3
              - mcs18/3
              - mcs19/3
              - mcs20/3
              - mcs21/3
              - mcs22/3
              - mcs23/3
              - mcs24/4
              - mcs25/4
              - mcs26/4
              - mcs27/4
              - mcs28/4
              - mcs29/4
              - mcs30/4
              - mcs31/4
            sae-groups:
              - 1
              - 2
              - 5
              - 14
              - 15
              - 16
              - 17
              - 18
              - 19
              - 20
              - 21
              - 27
              - 28
              - 29
              - 30
              - 31
            sae-password: <value of string>
            schedule: <value of string>
            security: <value in [None, WEP64, wep64, ...]>
            security-exempt-list: <value of string>
            security-obsolete-option: <value in [disable, enable]>
            security-redirect-url: <value of string>
            selected-usergroups: <value of string>
            split-tunneling: <value in [disable, enable]>
            ssid: <value of string>
            tkip-counter-measure: <value in [disable, enable]>
            usergroup: <value of string>
            utm-profile: <value of string>
            vdom: <value of string>
            vlan-auto: <value in [disable, enable]>
            vlan-pooling: <value in [wtp-group, round-robin, hash, ...]>
            vlanid: <value of integer>
            voice-enterprise: <value in [disable, enable]>



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



