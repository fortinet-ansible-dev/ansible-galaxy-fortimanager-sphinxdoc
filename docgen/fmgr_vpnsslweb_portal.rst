:source: fmgr_vpnsslweb_portal.py

:orphan:

.. _fmgr_vpnsslweb_portal:

fmgr_vpnsslweb_portal -- Portal.
++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">vpnsslweb_portal</span> - Portal. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">allow-user-access</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [web, ftp, telnet, smb, vnc, rdp, ssh, ping, citrix, portforward, sftp]</span> </li>
 <li><span class="li-head">auto-connect</span> - Enable/disable automatic connect by client when system is up. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bookmark-group</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">bookmarks</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">additional-params</span> - Additional parameters. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">apptype</span> - Application type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [web, telnet, ssh, ftp, smb, vnc, rdp, citrix, rdpnative, portforward, sftp]</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">folder</span> - Network shared file folder parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">form-data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">value</span> - Value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">host</span> - Host name/IP parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">listening-port</span> - Listening port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">load-balancing-info</span> - The load balancing information or cookie which should be provided to the connection broker. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logon-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">logon-user</span> - Logon user. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Bookmark name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Remote port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preconnection-blob</span> - An arbitrary string which identifies the RDP source. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">preconnection-id</span> - The numeric ID of the RDP source (0-2147483648). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">remote-port</span> - Remote port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security</span> - Security mode for RDP connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rdp, nla, tls, any]</span> </li>
 <li><span class="li-head">server-layout</span> - Server side keyboard layout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [en-us-qwerty, de-de-qwertz, fr-fr-azerty, it-it-qwerty, sv-se-qwerty, failsafe, en-gb-qwerty, es-es-qwerty, fr-ch-qwertz, ja-jp-qwerty, pt-br-qwerty, tr-tr-qwerty]</span> </li>
 <li><span class="li-head">show-status-window</span> - Enable/disable showing of status window. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso</span> - Single Sign-On. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, static, auto]</span> </li>
 <li><span class="li-head">sso-credential</span> - Single sign-on credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslvpn-login, alternative]</span> </li>
 <li><span class="li-head">sso-credential-sent-once</span> - Single sign-on credentials are only sent once to remote server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">sso-username</span> - SSO user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url</span> - URL parameter. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Bookmark group name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">custom-lang</span> - Change the web portal display language. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">customize-forticlient-download-url</span> - Enable support of customized download URL for FortiClient. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-bookmark</span> - Enable to display the web portal bookmark widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-connection-tools</span> - Enable to display the web portal connection tools widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-history</span> - Enable to display the web portal user login history widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-status</span> - Enable to display the web portal status widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dns-server1</span> - IPv4 DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server2</span> - IPv4 DNS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-suffix</span> - DNS suffix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">exclusive-routing</span> - Enable/disable all traffic go through tunnel only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">forticlient-download</span> - Enable/disable download option for FortiClient. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">forticlient-download-method</span> - FortiClient download method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [direct, ssl-vpn]</span> </li>
 <li><span class="li-head">heading</span> - Web portal heading message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hide-sso-credential</span> - Enable to prevent SSO credential being sent to client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">host-check</span> - Type of host checking performed on endpoints. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, av, fw, av-fw, custom]</span> </li>
 <li><span class="li-head">host-check-interval</span> - Periodic host check interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">host-check-policy</span> - One or more policies to require the endpoint to have specific security software. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-mode</span> - Method by which users of this SSL-VPN tunnel obtain IP addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, user-group]</span> </li>
 <li><span class="li-head">ip-pools</span> - IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-dns-server1</span> - IPv6 DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-dns-server2</span> - IPv6 DNS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-exclusive-routing</span> - Enable/disable all IPv6 traffic go through tunnel only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-pools</span> - IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-service-restriction</span> - Enable/disable IPv6 tunnel service restriction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-split-tunneling</span> - Enable/disable IPv6 split tunneling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-split-tunneling-routing-address</span> - IPv6 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-tunnel-mode</span> - Enable/disable IPv6 SSL-VPN tunnel mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-wins-server1</span> - IPv6 WINS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-wins-server2</span> - IPv6 WINS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">keep-alive</span> - Enable/disable automatic reconnect for FortiClient connections. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">limit-user-logins</span> - Enable to limit each user to one SSL-VPN session at a time. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-addr-action</span> - Client MAC address action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">mac-addr-check</span> - Enable/disable MAC address host checking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-addr-check-rule</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">mac-addr-list</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">mac-addr-mask</span> - Client MAC address mask. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Client MAC address check rule name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">macos-forticlient-download-url</span> - Download URL for Mac FortiClient. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Portal name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os-check</span> - Enable to let the FortiGate decide action based on client OS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">redir-url</span> - Client login redirect URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">save-password</span> - Enable/disable FortiClient saving the users password. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service-restriction</span> - Enable/disable tunnel service restriction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">skip-check-for-unsupported-browser</span> - Enable to skip host check if browser does not support it. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">skip-check-for-unsupported-os</span> - Enable to skip host check if client OS does not support it. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">smb-ntlmv1-auth</span> - Enable support of NTLMv1 for Samba authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">smbv1</span> - Enable/disable support of SMBv1 for Samba. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">split-dns</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dns-server1</span> - DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server2</span> - DNS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">domains</span> - Split DNS domains used for SSL-VPN clients separated by comma(,). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ipv6-dns-server1</span> - IPv6 DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-dns-server2</span> - IPv6 DNS server 2. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">split-tunneling</span> - Enable/disable IPv4 split tunneling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">split-tunneling-routing-address</span> - IPv4 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">theme</span> - Web portal color scheme. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [gray, blue, orange, crimson, steelblue, darkgrey, green, melongene, red, mariner]</span> </li>
 <li><span class="li-head">tunnel-mode</span> - Enable/disable IPv4 SSL-VPN tunnel mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-bookmark</span> - Enable to allow web portal users to create their own bookmarks. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-group-bookmark</span> - Enable to allow web portal users to create bookmarks for all users in the same user group. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-mode</span> - Enable/disable SSL VPN web mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">windows-forticlient-download-url</span> - Download URL for Windows FortiClient. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server1</span> - IPv4 WINS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server2</span> - IPv4 WINS server 1. <span class="li-normal">type: str</span> </li>
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
    - name: Portal.
      fmgr_vpnsslweb_portal:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         vpnsslweb_portal:
            allow-user-access:
              - web
              - ftp
              - telnet
              - smb
              - vnc
              - rdp
              - ssh
              - ping
              - citrix
              - portforward
              - sftp
            auto-connect: <value in [disable, enable]>
            bookmark-group:
              -
                  bookmarks:
                    -
                        additional-params: <value of string>
                        apptype: <value in [web, telnet, ssh, ...]>
                        description: <value of string>
                        folder: <value of string>
                        form-data:
                          -
                              name: <value of string>
                              value: <value of string>
                        host: <value of string>
                        listening-port: <value of integer>
                        load-balancing-info: <value of string>
                        logon-password: <value of string>
                        logon-user: <value of string>
                        name: <value of string>
                        port: <value of integer>
                        preconnection-blob: <value of string>
                        preconnection-id: <value of integer>
                        remote-port: <value of integer>
                        security: <value in [rdp, nla, tls, ...]>
                        server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
                        show-status-window: <value in [disable, enable]>
                        sso: <value in [disable, static, auto]>
                        sso-credential: <value in [sslvpn-login, alternative]>
                        sso-credential-sent-once: <value in [disable, enable]>
                        sso-password: <value of string>
                        sso-username: <value of string>
                        url: <value of string>
                  name: <value of string>
            custom-lang: <value of string>
            customize-forticlient-download-url: <value in [disable, enable]>
            display-bookmark: <value in [disable, enable]>
            display-connection-tools: <value in [disable, enable]>
            display-history: <value in [disable, enable]>
            display-status: <value in [disable, enable]>
            dns-server1: <value of string>
            dns-server2: <value of string>
            dns-suffix: <value of string>
            exclusive-routing: <value in [disable, enable]>
            forticlient-download: <value in [disable, enable]>
            forticlient-download-method: <value in [direct, ssl-vpn]>
            heading: <value of string>
            hide-sso-credential: <value in [disable, enable]>
            host-check: <value in [none, av, fw, ...]>
            host-check-interval: <value of integer>
            host-check-policy: <value of string>
            ip-mode: <value in [range, user-group]>
            ip-pools: <value of string>
            ipv6-dns-server1: <value of string>
            ipv6-dns-server2: <value of string>
            ipv6-exclusive-routing: <value in [disable, enable]>
            ipv6-pools: <value of string>
            ipv6-service-restriction: <value in [disable, enable]>
            ipv6-split-tunneling: <value in [disable, enable]>
            ipv6-split-tunneling-routing-address: <value of string>
            ipv6-tunnel-mode: <value in [disable, enable]>
            ipv6-wins-server1: <value of string>
            ipv6-wins-server2: <value of string>
            keep-alive: <value in [disable, enable]>
            limit-user-logins: <value in [disable, enable]>
            mac-addr-action: <value in [deny, allow]>
            mac-addr-check: <value in [disable, enable]>
            mac-addr-check-rule:
              -
                  mac-addr-list: <value of string>
                  mac-addr-mask: <value of integer>
                  name: <value of string>
            macos-forticlient-download-url: <value of string>
            name: <value of string>
            os-check: <value in [disable, enable]>
            redir-url: <value of string>
            save-password: <value in [disable, enable]>
            service-restriction: <value in [disable, enable]>
            skip-check-for-unsupported-browser: <value in [disable, enable]>
            skip-check-for-unsupported-os: <value in [disable, enable]>
            smb-ntlmv1-auth: <value in [disable, enable]>
            smbv1: <value in [disable, enable]>
            split-dns:
              -
                  dns-server1: <value of string>
                  dns-server2: <value of string>
                  domains: <value of string>
                  id: <value of integer>
                  ipv6-dns-server1: <value of string>
                  ipv6-dns-server2: <value of string>
            split-tunneling: <value in [disable, enable]>
            split-tunneling-routing-address: <value of string>
            theme: <value in [gray, blue, orange, ...]>
            tunnel-mode: <value in [disable, enable]>
            user-bookmark: <value in [disable, enable]>
            user-group-bookmark: <value in [disable, enable]>
            web-mode: <value in [disable, enable]>
            windows-forticlient-download-url: <value of string>
            wins-server1: <value of string>
            wins-server2: <value of string>



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



