:source: fmgr_system_sdnconnector.py

:orphan:

.. _fmgr_system_sdnconnector:

fmgr_system_sdnconnector -- Configure connection to SDN Connector.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">system_sdnconnector</span> - Configure connection to SDN Connector. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_local_cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">access-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">azure-region</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, china, germany, usgov, local]</span> </li>
 <li><span class="li-head">client-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">client-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">compartment-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">gcp-project</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">key-passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">login-endpoint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nic</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">public-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">nsx-cert-fingerprint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-fingerprint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-region</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [phoenix, ashburn, frankfurt, london, toronto]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">private-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">region</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resource-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resource-url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rest-interface</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mgmt, sync]</span> </li>
 <li><span class="li-head">rest-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">rest-sport</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rest-ssl</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">route</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">route-table</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">route</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">next-hop</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">secret-key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">service-account</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">subscription-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tenant-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack, kubernetes, vmware, acs, alicloud]</span> </li>
 <li><span class="li-head">update-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">use-metadata-iam</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vmx-image-url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vmx-service-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpc-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: Configure connection to SDN Connector.
      fmgr_system_sdnconnector:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         system_sdnconnector:
            _local_cert: <value of string>
            access-key: <value of string>
            azure-region: <value in [global, china, germany, ...]>
            client-id: <value of string>
            client-secret:
              - <value of string>
            compartment-id: <value of string>
            external-ip:
              -
                  name: <value of string>
            gcp-project: <value of string>
            key-passwd:
              - <value of string>
            login-endpoint: <value of string>
            name: <value of string>
            nic:
              -
                  ip:
                    -
                        name: <value of string>
                        public-ip: <value of string>
                  name: <value of string>
            nsx-cert-fingerprint: <value of string>
            oci-cert: <value of string>
            oci-fingerprint: <value of string>
            oci-region: <value in [phoenix, ashburn, frankfurt, ...]>
            password:
              - <value of string>
            private-key: <value of string>
            region: <value of string>
            resource-group: <value of string>
            resource-url: <value of string>
            rest-interface: <value in [mgmt, sync]>
            rest-password:
              - <value of string>
            rest-sport: <value of integer>
            rest-ssl: <value in [disable, enable]>
            route:
              -
                  name: <value of string>
            route-table:
              -
                  name: <value of string>
                  route:
                    -
                        name: <value of string>
                        next-hop: <value of string>
            secret-key:
              - <value of string>
            server: <value of string>
            server-port: <value of integer>
            service-account: <value of string>
            status: <value in [disable, enable]>
            subscription-id: <value of string>
            tenant-id: <value of string>
            type: <value in [aci, aws, nsx, ...]>
            update-interval: <value of integer>
            use-metadata-iam: <value in [disable, enable]>
            user-id: <value of string>
            username: <value of string>
            vmx-image-url: <value of string>
            vmx-service-name: <value of string>
            vpc-id: <value of string>



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



