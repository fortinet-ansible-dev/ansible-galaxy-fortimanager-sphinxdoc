:source: fmgr_pkg_header_policy6.py

:orphan:

.. _fmgr_pkg_header_policy6:

fmgr_pkg_header_policy6
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
 <li><span class="li-head">pkg</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">pkg_header_policy6</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept, ipsec, ssl-vpn]</span> </li>
 <li><span class="li-head">anti-replay</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">app-category</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">app-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">application-charts</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [top10-app, top10-p2p-user, top10-media-user]</span> </li>
 <li><span class="li-head">application-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auto-asic-offload</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">casi-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cifs-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">custom-log-fields</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deep-inspection-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-detection-portal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">devices</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffserv-forward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffserv-reverse</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffservcode-forward</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffservcode-rev</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dnsfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dscp-match</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-value</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dsri</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dynamic-profile-access</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [imap, smtp, pop3, http, ftp, im, nntp, imaps, smtps, pop3s, https, ftps]</span> </li>
 <li><span class="li-head">dynamic-profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">email-collection-portal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">emailfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">firewall-session-dirty</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [check-all, check-new]</span> </li>
 <li><span class="li-head">fixedport</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fsae</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">global-label</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-policy-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icap-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">identity-based</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">identity-based-policy6</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept]</span> </li>
 <li><span class="li-head">application-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deep-inspection-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">devices</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">endpoint-compliance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">icap-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ips-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, all, utm]</span> </li>
 <li><span class="li-head">mms-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">send-deny-packet</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-portal</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-realm</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">voip-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">identity-from</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auth, device]</span> </li>
 <li><span class="li-head">inbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">inspection-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">ippool</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">label</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">natinbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">natoutbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">np-accelation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">np-acceleration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poolname</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rsso</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">send-deny-packet</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">session-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-filter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-policy-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-mirror</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-mirror-intf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, local, radius, ldap, tacacs+]</span> </li>
 <li><span class="li-head">sslvpn-ccert</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sslvpn-cipher</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, high, medium]</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tcp-mss-receiver</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-mss-sender</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-session-without-syn</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [all, data-only, disable]</span> </li>
 <li><span class="li-head">timeout-send-rst</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tos</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">traffic-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-category</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-inspection-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">utm-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan-cos-fwd</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vlan-cos-rev</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vlan-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">voip-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpntunnel</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
      fmgr_pkg_header_policy6:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         pkg: <your own value>
         state: <value in [present, absent]>
         pkg_header_policy6:
            action: <value in [deny, accept, ipsec, ...]>
            anti-replay: <value in [disable, enable]>
            app-category: <value of string>
            app-group: <value of string>
            application: <value of integer>
            application-charts:
              - top10-app
              - top10-p2p-user
              - top10-media-user
            application-list: <value of string>
            auto-asic-offload: <value in [disable, enable]>
            av-profile: <value of string>
            casi-profile: <value of string>
            cifs-profile: <value of string>
            comments: <value of string>
            custom-log-fields: <value of string>
            deep-inspection-options: <value of string>
            device-detection-portal: <value in [disable, enable]>
            devices: <value of string>
            diffserv-forward: <value in [disable, enable]>
            diffserv-reverse: <value in [disable, enable]>
            diffservcode-forward: <value of string>
            diffservcode-rev: <value of string>
            dlp-sensor: <value of string>
            dnsfilter-profile: <value of string>
            dscp-match: <value in [disable, enable]>
            dscp-negate: <value in [disable, enable]>
            dscp-value: <value of string>
            dsri: <value in [disable, enable]>
            dstaddr: <value of string>
            dstaddr-negate: <value in [disable, enable]>
            dstintf: <value of string>
            dynamic-profile: <value in [disable, enable]>
            dynamic-profile-access:
              - imap
              - smtp
              - pop3
              - http
              - ftp
              - im
              - nntp
              - imaps
              - smtps
              - pop3s
              - https
              - ftps
            dynamic-profile-group: <value of string>
            email-collection-portal: <value in [disable, enable]>
            emailfilter-profile: <value of string>
            firewall-session-dirty: <value in [check-all, check-new]>
            fixedport: <value in [disable, enable]>
            fsae: <value in [disable, enable]>
            global-label: <value of string>
            groups: <value of string>
            http-policy-redirect: <value in [disable, enable]>
            icap-profile: <value of string>
            identity-based: <value in [disable, enable]>
            identity-based-policy6:
              -
                  action: <value in [deny, accept]>
                  application-list: <value of string>
                  av-profile: <value of string>
                  deep-inspection-options: <value of string>
                  devices: <value of string>
                  dlp-sensor: <value of string>
                  endpoint-compliance: <value in [disable, enable]>
                  groups: <value of string>
                  icap-profile: <value of string>
                  id: <value of integer>
                  ips-sensor: <value of string>
                  logtraffic: <value in [disable, enable, all, ...]>
                  mms-profile: <value of string>
                  per-ip-shaper: <value of string>
                  profile-group: <value of string>
                  profile-protocol-options: <value of string>
                  profile-type: <value in [single, group]>
                  replacemsg-group: <value of string>
                  schedule: <value of string>
                  send-deny-packet: <value in [disable, enable]>
                  service: <value of string>
                  service-negate: <value in [disable, enable]>
                  spamfilter-profile: <value of string>
                  sslvpn-portal: <value of string>
                  sslvpn-realm: <value of string>
                  traffic-shaper: <value of string>
                  traffic-shaper-reverse: <value of string>
                  utm-status: <value in [disable, enable]>
                  voip-profile: <value of string>
                  webfilter-profile: <value of string>
            identity-from: <value in [auth, device]>
            inbound: <value in [disable, enable]>
            inspection-mode: <value in [proxy, flow]>
            ippool: <value in [disable, enable]>
            ips-sensor: <value of string>
            label: <value of string>
            logtraffic: <value in [disable, enable, all, ...]>
            logtraffic-start: <value in [disable, enable]>
            mms-profile: <value of string>
            name: <value of string>
            nat: <value in [disable, enable]>
            natinbound: <value in [disable, enable]>
            natoutbound: <value in [disable, enable]>
            np-accelation: <value in [disable, enable]>
            np-acceleration: <value in [disable, enable]>
            outbound: <value in [disable, enable]>
            per-ip-shaper: <value of string>
            policyid: <value of integer>
            poolname: <value of string>
            profile-group: <value of string>
            profile-protocol-options: <value of string>
            profile-type: <value in [single, group]>
            replacemsg-group: <value of string>
            replacemsg-override-group: <value of string>
            rsso: <value in [disable, enable]>
            schedule: <value of string>
            send-deny-packet: <value in [disable, enable]>
            service: <value of string>
            service-negate: <value in [disable, enable]>
            session-ttl: <value of integer>
            spamfilter-profile: <value of string>
            srcaddr: <value of string>
            srcaddr-negate: <value in [disable, enable]>
            srcintf: <value of string>
            ssh-filter-profile: <value of string>
            ssh-policy-redirect: <value in [disable, enable]>
            ssl-mirror: <value in [disable, enable]>
            ssl-mirror-intf: <value of string>
            ssl-ssh-profile: <value of string>
            sslvpn-auth: <value in [any, local, radius, ...]>
            sslvpn-ccert: <value in [disable, enable]>
            sslvpn-cipher: <value in [any, high, medium]>
            status: <value in [disable, enable]>
            tags: <value of string>
            tcp-mss-receiver: <value of integer>
            tcp-mss-sender: <value of integer>
            tcp-session-without-syn: <value in [all, data-only, disable]>
            timeout-send-rst: <value in [disable, enable]>
            tos: <value of string>
            tos-mask: <value of string>
            tos-negate: <value in [disable, enable]>
            traffic-shaper: <value of string>
            traffic-shaper-reverse: <value of string>
            url-category: <value of string>
            users: <value of string>
            utm-inspection-mode: <value in [proxy, flow]>
            utm-status: <value in [disable, enable]>
            uuid: <value of string>
            vlan-cos-fwd: <value of integer>
            vlan-cos-rev: <value of integer>
            vlan-filter: <value of string>
            voip-profile: <value of string>
            vpntunnel: <value of string>
            webfilter-profile: <value of string>



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



