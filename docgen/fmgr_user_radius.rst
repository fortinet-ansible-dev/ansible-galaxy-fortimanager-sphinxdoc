:source: fmgr_user_radius.py

:orphan:

.. _fmgr_user_radius:

fmgr_user_radius -- Configure RADIUS server entries.
++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">user_radius</span> - Configure RADIUS server entries. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">accounting-server</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - ID (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port</span> - RADIUS accounting port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server</span> - {&lt;name_str|ip_str&gt;} Server CN domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IP address for communications to the RADIUS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">acct-all-servers</span> - Enable/disable sending of accounting messages to all configured servers (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">acct-interim-interval</span> - Time in seconds between each accounting interim update message. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">all-usergroup</span> - Enable/disable automatically including this RADIUS server in all user groups. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-type</span> - Authentication methods/protocols permitted for this RADIUS server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pap, chap, ms_chap, ms_chap_v2, auto]</span> </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">acct-all-servers</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">acct-interim-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">all-usergroup</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pap, chap, ms_chap, ms_chap_v2, auto]</span> </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">dp-carrier-endpoint-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">dp-carrier-endpoint-block-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">dp-context-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-flush-ip-session</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-hold-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-http-header</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dp-http-header-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ip-header-address, default-profile]</span> </li>
 <li><span class="li-head">dp-http-header-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-http-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-log-dyn_flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span> </li>
 <li><span class="li-head">dp-log-period</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-mem-percent</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-profile-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">dp-profile-attribute-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dp-radius-response</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-radius-server-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">dp-validate-request-secret</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dynamic-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">endpoint-translation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-convert-hex</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-header</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-range-max</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-range-min</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-string</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-source</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-header, cookie]</span> </li>
 <li><span class="li-head">ep-ip-header</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ep-ip-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-missing-header-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session-ip, policy-profile]</span> </li>
 <li><span class="li-head">ep-profile-query-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session-ip, extract-ip, extract-carrier-endpoint]</span> </li>
 <li><span class="li-head">h3c-compatibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nas-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password-encoding</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ISO-8859-1, auto]</span> </li>
 <li><span class="li-head">password-renewal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-coa</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-context-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-endpoint-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">rsso-endpoint-block-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">rsso-ep-one-ip-only</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-flush-ip-session</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-log-flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span> </li>
 <li><span class="li-head">rsso-log-period</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-radius-response</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-radius-server-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">rsso-validate-request-secret</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">secondary-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">secondary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sso-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">sso-attribute-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sso-attribute-value-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tertiary-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">tertiary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">use-group-for-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">use-management-vdom</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">username-case-sensitive</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">h3c-compatibility</span> - Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - RADIUS server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nas-ip</span> - IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password-encoding</span> - Password encoding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ISO-8859-1, auto]</span> </li>
 <li><span class="li-head">password-renewal</span> - Enable/disable password renewal. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-coa</span> - Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-port</span> - RADIUS service port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso</span> - Enable/disable RADIUS based single sign on feature. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-context-timeout</span> - Time in seconds before the logged out user is removed from the "user context list" of logged on users. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-endpoint-attribute</span> - RADIUS attributes used to extract the user end point identifer from the RADIUS Start record. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">rsso-endpoint-block-attribute</span> - RADIUS attributes used to block a user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">rsso-ep-one-ip-only</span> - Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-flush-ip-session</span> - Enable/disable flushing user IP sessions on RADIUS accounting Stop messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-log-flags</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span> </li>
 <li><span class="li-head">rsso-log-period</span> - Time interval in seconds that group event log messages will be generated for dynamic profile events. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-radius-response</span> - Enable/disable sending RADIUS response packets after receiving Start and Stop records. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-radius-server-port</span> - UDP port to listen on for RADIUS Start and Stop records. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">rsso-validate-request-secret</span> - Enable/disable validating the RADIUS request shared secret in the Start or End record. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">secondary-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">secondary-server</span> - {&lt;name_str|ip_str&gt;} secondary RADIUS CN domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server</span> - Primary RADIUS server CN domain name or IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IP address for communications to the RADIUS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sso-attribute</span> - RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">sso-attribute-key</span> - Key prefix for SSO group value in the SSO attribute. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sso-attribute-value-override</span> - Enable/disable override old attribute value with new value for the same endpoint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tertiary-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">tertiary-server</span> - {&lt;name_str|ip_str&gt;} tertiary RADIUS CN domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">timeout</span> - Time in seconds between re-sending authentication requests. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">use-management-vdom</span> - Enable/disable using management VDOM to send requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">username-case-sensitive</span> - Enable/disable case sensitive user names. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure RADIUS server entries.
      fmgr_user_radius:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         user_radius:
            accounting-server:
              -
                  id: <value of integer>
                  port: <value of integer>
                  secret: <value of string>
                  server: <value of string>
                  source-ip: <value of string>
                  status: <value in [disable, enable]>
            acct-all-servers: <value in [disable, enable]>
            acct-interim-interval: <value of integer>
            all-usergroup: <value in [disable, enable]>
            auth-type: <value in [pap, chap, ms_chap, ...]>
            class: <value of string>
            dynamic_mapping:
              -
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  acct-all-servers: <value in [disable, enable]>
                  acct-interim-interval: <value of integer>
                  all-usergroup: <value in [disable, enable]>
                  auth-type: <value in [pap, chap, ms_chap, ...]>
                  class: <value of string>
                  dp-carrier-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  dp-carrier-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  dp-context-timeout: <value of integer>
                  dp-flush-ip-session: <value in [disable, enable]>
                  dp-hold-time: <value of integer>
                  dp-http-header: <value of string>
                  dp-http-header-fallback: <value in [ip-header-address, default-profile]>
                  dp-http-header-status: <value in [disable, enable]>
                  dp-http-header-suppress: <value in [disable, enable]>
                  dp-log-dyn_flags:
                    - none
                    - protocol-error
                    - profile-missing
                    - context-missing
                    - accounting-stop-missed
                    - accounting-event
                    - radiusd-other
                    - endpoint-block
                  dp-log-period: <value of integer>
                  dp-mem-percent: <value of integer>
                  dp-profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  dp-profile-attribute-key: <value of string>
                  dp-radius-response: <value in [disable, enable]>
                  dp-radius-server-port: <value of integer>
                  dp-secret: <value of string>
                  dp-validate-request-secret: <value in [disable, enable]>
                  dynamic-profile: <value in [disable, enable]>
                  endpoint-translation: <value in [disable, enable]>
                  ep-carrier-endpoint-convert-hex: <value in [disable, enable]>
                  ep-carrier-endpoint-header: <value of string>
                  ep-carrier-endpoint-header-suppress: <value in [disable, enable]>
                  ep-carrier-endpoint-prefix: <value in [disable, enable]>
                  ep-carrier-endpoint-prefix-range-max: <value of integer>
                  ep-carrier-endpoint-prefix-range-min: <value of integer>
                  ep-carrier-endpoint-prefix-string: <value of string>
                  ep-carrier-endpoint-source: <value in [http-header, cookie]>
                  ep-ip-header: <value of string>
                  ep-ip-header-suppress: <value in [disable, enable]>
                  ep-missing-header-fallback: <value in [session-ip, policy-profile]>
                  ep-profile-query-type: <value in [session-ip, extract-ip, extract-carrier-endpoint]>
                  h3c-compatibility: <value in [disable, enable]>
                  nas-ip: <value of string>
                  password-encoding: <value in [ISO-8859-1, auto]>
                  password-renewal: <value in [disable, enable]>
                  radius-coa: <value in [disable, enable]>
                  radius-port: <value of integer>
                  rsso: <value in [disable, enable]>
                  rsso-context-timeout: <value of integer>
                  rsso-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  rsso-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  rsso-ep-one-ip-only: <value in [disable, enable]>
                  rsso-flush-ip-session: <value in [disable, enable]>
                  rsso-log-flags:
                    - none
                    - protocol-error
                    - profile-missing
                    - context-missing
                    - accounting-stop-missed
                    - accounting-event
                    - radiusd-other
                    - endpoint-block
                  rsso-log-period: <value of integer>
                  rsso-radius-response: <value in [disable, enable]>
                  rsso-radius-server-port: <value of integer>
                  rsso-secret: <value of string>
                  rsso-validate-request-secret: <value in [disable, enable]>
                  secondary-secret: <value of string>
                  secondary-server: <value of string>
                  secret: <value of string>
                  server: <value of string>
                  source-ip: <value of string>
                  sso-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  sso-attribute-key: <value of string>
                  sso-attribute-value-override: <value in [disable, enable]>
                  tertiary-secret: <value of string>
                  tertiary-server: <value of string>
                  timeout: <value of integer>
                  use-group-for-profile: <value in [disable, enable]>
                  use-management-vdom: <value in [disable, enable]>
                  username-case-sensitive: <value in [disable, enable]>
            h3c-compatibility: <value in [disable, enable]>
            name: <value of string>
            nas-ip: <value of string>
            password-encoding: <value in [ISO-8859-1, auto]>
            password-renewal: <value in [disable, enable]>
            radius-coa: <value in [disable, enable]>
            radius-port: <value of integer>
            rsso: <value in [disable, enable]>
            rsso-context-timeout: <value of integer>
            rsso-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
            rsso-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
            rsso-ep-one-ip-only: <value in [disable, enable]>
            rsso-flush-ip-session: <value in [disable, enable]>
            rsso-log-flags:
              - none
              - protocol-error
              - profile-missing
              - context-missing
              - accounting-stop-missed
              - accounting-event
              - radiusd-other
              - endpoint-block
            rsso-log-period: <value of integer>
            rsso-radius-response: <value in [disable, enable]>
            rsso-radius-server-port: <value of integer>
            rsso-secret: <value of string>
            rsso-validate-request-secret: <value in [disable, enable]>
            secondary-secret: <value of string>
            secondary-server: <value of string>
            secret: <value of string>
            server: <value of string>
            source-ip: <value of string>
            sso-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
            sso-attribute-key: <value of string>
            sso-attribute-value-override: <value in [disable, enable]>
            tertiary-secret: <value of string>
            tertiary-server: <value of string>
            timeout: <value of integer>
            use-management-vdom: <value in [disable, enable]>
            username-case-sensitive: <value in [disable, enable]>



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



