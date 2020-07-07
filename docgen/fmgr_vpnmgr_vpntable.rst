:source: fmgr_vpnmgr_vpntable.py

:orphan:

.. _fmgr_vpnmgr_vpntable:

fmgr_vpnmgr_vpntable
++++++++++++++++++++

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
 <li><span class="li-head">vpnmgr_vpntable</span> - no description <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">authmethod</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [psk, rsa-signature, signature]</span> </li>
 <li><span class="li-head">auto-zone-policy</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">certificate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dpd</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, on-idle, on-demand]</span> </li>
 <li><span class="li-head">dpd-retrycount</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dpd-retryinterval</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">fcc-enforcement</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hub2spoke-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ike-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2]</span> </li>
 <li><span class="li-head">ike1dhgroup</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31, 32]</span> </li>
 </ul>
 <li><span class="li-head">ike1dpd</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ike1keylifesec</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike1localid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ike1mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [main, aggressive]</span> </li>
 <li><span class="li-head">ike1natkeepalive</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike1nattraversal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, forced]</span> </li>
 <li><span class="li-head">ike1proposal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [des-md5, des-sha1, 3des-md5, 3des-sha1, aes128-md5, aes128-sha1, aes192-md5, aes192-sha1, aes256-md5, aes256-sha1, des-sha256, 3des-sha256, aes128-sha256, aes192-sha256, aes256-sha256, des-sha384, des-sha512, 3des-sha384, 3des-sha512, aes128-sha384, aes128-sha512, aes192-sha384, aes192-sha512, aes256-sha384, aes256-sha512, aria128-md5, aria128-sha1, aria128-sha256, aria128-sha384, aria128-sha512, aria192-md5, aria192-sha1, aria192-sha256, aria192-sha384, aria192-sha512, aria256-md5, aria256-sha1, aria256-sha256, aria256-sha384, aria256-sha512, seed-md5, seed-sha1, seed-sha256, seed-sha384, seed-sha512, aes128gcm-prfsha1, aes128gcm-prfsha256, aes128gcm-prfsha384, aes128gcm-prfsha512, aes256gcm-prfsha1, aes256gcm-prfsha256, aes256gcm-prfsha384, aes256gcm-prfsha512, chacha20poly1305-prfsha1, chacha20poly1305-prfsha256, chacha20poly1305-prfsha384, chacha20poly1305-prfsha512]</span> </li>
 <li><span class="li-head">ike2autonego</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ike2dhgroup</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31, 32]</span> </li>
 </ul>
 <li><span class="li-head">ike2keepalive</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ike2keylifekbs</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike2keylifesec</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike2keylifetype</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [seconds, kbs, both]</span> </li>
 <li><span class="li-head">ike2proposal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [null-md5, null-sha1, des-null, 3des-null, des-md5, des-sha1, 3des-md5, 3des-sha1, aes128-md5, aes128-sha1, aes192-md5, aes192-sha1, aes256-md5, aes256-sha1, aes128-null, aes192-null, aes256-null, null-sha256, des-sha256, 3des-sha256, aes128-sha256, aes192-sha256, aes256-sha256, des-sha384, des-sha512, 3des-sha384, 3des-sha512, aes128-sha384, aes128-sha512, aes192-sha384, aes192-sha512, aes256-sha384, aes256-sha512, null-sha384, null-sha512, aria128-null, aria128-md5, aria128-sha1, aria128-sha256, aria128-sha384, aria128-sha512, aria192-null, aria192-md5, aria192-sha1, aria192-sha256, aria192-sha384, aria192-sha512, aria256-null, aria256-md5, aria256-sha1, aria256-sha256, aria256-sha384, aria256-sha512, seed-null, seed-md5, seed-sha1, seed-sha256, seed-sha384, seed-sha512, aes128gcm, aes256gcm, chacha20poly1305]</span> </li>
 <li><span class="li-head">inter-vdom</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">intf-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [off, on]</span> </li>
 <li><span class="li-head">localid-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, fqdn, user-fqdn, keyid, address, asn1dn]</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">negotiate-timeout</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 30</span> </li>
 <li><span class="li-head">npu-offload</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pfs</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">psk-auto-generate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">psksecret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">replay</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsa-certificate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spoke2hub-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">topology</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [meshed, star, dialup]</span> </li>
 <li><span class="li-head">vpn-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
      fmgr_vpnmgr_vpntable:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         vpnmgr_vpntable:
            authmethod: <value in [psk, rsa-signature, signature]>
            auto-zone-policy: <value in [disable, enable]>
            certificate: <value of string>
            description: <value of string>
            dpd: <value in [disable, enable, on-idle, ...]>
            dpd-retrycount: <value of integer>
            dpd-retryinterval:
              - <value of integer>
            fcc-enforcement: <value in [disable, enable]>
            hub2spoke-zone: <value of string>
            ike-version: <value in [1, 2]>
            ike1dhgroup:
              - <value in [1, 2, 5, ...]>
            ike1dpd: <value in [disable, enable]>
            ike1keylifesec: <value of integer>
            ike1localid: <value of string>
            ike1mode: <value in [main, aggressive]>
            ike1natkeepalive: <value of integer>
            ike1nattraversal: <value in [disable, enable, forced]>
            ike1proposal: <value in [des-md5, des-sha1, 3des-md5, ...]>
            ike2autonego: <value in [disable, enable]>
            ike2dhgroup:
              - <value in [1, 2, 5, ...]>
            ike2keepalive: <value in [disable, enable]>
            ike2keylifekbs: <value of integer>
            ike2keylifesec: <value of integer>
            ike2keylifetype: <value in [seconds, kbs, both]>
            ike2proposal: <value in [null-md5, null-sha1, des-null, ...]>
            inter-vdom: <value in [disable, enable]>
            intf-mode: <value in [off, on]>
            localid-type: <value in [auto, fqdn, user-fqdn, ...]>
            name: <value of string>
            negotiate-timeout: <value of integer>
            npu-offload: <value in [disable, enable]>
            pfs: <value in [disable, enable]>
            psk-auto-generate: <value in [disable, enable]>
            psksecret:
              - <value of string>
            replay: <value in [disable, enable]>
            rsa-certificate: <value of string>
            spoke2hub-zone: <value of string>
            topology: <value in [meshed, star, dialup]>
            vpn-zone: <value of string>



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



