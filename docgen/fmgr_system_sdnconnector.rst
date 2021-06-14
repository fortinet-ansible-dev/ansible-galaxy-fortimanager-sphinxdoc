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
 <td>system_sdnconnector</td>
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
 <li><span class="li-head">system_sdnconnector</span> - Configure connection to SDN Connector. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">_local_cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">access-key</span> - AWS access key ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">azure-region</span> - Azure server region. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, china, germany, usgov, local]</span> </li>
 <li><span class="li-head">client-id</span> - Azure client ID (application ID). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">client-secret</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">compartment-id</span> - Compartment ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - External IP name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">gcp-project</span> - GCP project name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">key-passwd</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">login-endpoint</span> - Azure Stack login enpoint. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - SDN connector name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nic</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - IP configuration name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">public-ip</span> - Public IP name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resource-group</span> - Resource group of Azure public IP. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Network interface name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">nsx-cert-fingerprint</span> - NSX certificate fingerprint. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-cert</span> - OCI certificate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-fingerprint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-region</span> - OCI server region. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [phoenix, ashburn, frankfurt, london, toronto]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">private-key</span> - Private key of GCP service account. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">region</span> - AWS region name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resource-group</span> - Azure resource group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resource-url</span> - Azure Stack resource URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rest-interface</span> - Interface name for REST service to listen on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mgmt, sync]</span> </li>
 <li><span class="li-head">rest-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">rest-sport</span> - REST service access port (1 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rest-ssl</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">route</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Route name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">route-table</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Route table name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">route</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Route name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">next-hop</span> - Next hop address. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">resource-group</span> - Resource group of Azure route table. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subscription-id</span> - Subscription ID of Azure route table. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">secret-key</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">server</span> - Server address of the remote SDN connector. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-port</span> - Port number of the remote SDN connector. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">service-account</span> - GCP service account email. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable connection to the remote SDN connector. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">subscription-id</span> - Azure subscription ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tenant-id</span> - Tenant ID (directory ID). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of SDN connector. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack, kubernetes, vmware, acs, alicloud, sepm, aci-direct, ibm, nutanix]</span> </li>
 <li><span class="li-head">update-interval</span> - Dynamic object update interval (0 - 3600 sec, 0 means disabled, default = 60). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">use-metadata-iam</span> - Enable/disable using IAM role from metadata to call API. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-id</span> - User ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username</span> - Username of the remote SDN connector as login credentials. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vmx-image-url</span> - URL of web-hosted VMX image. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vmx-service-name</span> - VMX Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpc-id</span> - AWS VPC ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">domain</span> - Openstack domain. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ha-status</span> - Enable/disable use for FortiGate HA service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">last-update</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">oci-region-type</span> - OCI region type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [commercial, government]</span> </li>
 <li><span class="li-head">secret-token</span> - Secret token of Kubernetes service account. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">updating</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">group-name</span> - Group name of computers. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">api-key</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">compute-generation</span> - Compute generation for IBM cloud infrastructure. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ibm-region</span> - IBM cloud region name. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-south, us-east, germany, great-britain, japan, australia]</span> </li>
 <li><span class="li-head">server-list</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">vcenter-password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">vcenter-server</span> - vCenter server address for NSX quarantine. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vcenter-username</span> - vCenter server username for NSX quarantine. <span class="li-normal">type: str</span> </li>
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
         bypass_validation: False
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
            client-secret: <value of string>
            compartment-id: <value of string>
            external-ip:
              -
                  name: <value of string>
            gcp-project: <value of string>
            key-passwd: <value of string>
            login-endpoint: <value of string>
            name: <value of string>
            nic:
              -
                  ip:
                    -
                        name: <value of string>
                        public-ip: <value of string>
                        resource-group: <value of string>
                  name: <value of string>
            nsx-cert-fingerprint: <value of string>
            oci-cert: <value of string>
            oci-fingerprint: <value of string>
            oci-region: <value in [phoenix, ashburn, frankfurt, ...]>
            password: <value of string>
            private-key: <value of string>
            region: <value of string>
            resource-group: <value of string>
            resource-url: <value of string>
            rest-interface: <value in [mgmt, sync]>
            rest-password: <value of string>
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
                  resource-group: <value of string>
                  subscription-id: <value of string>
            secret-key: <value of string>
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
            domain: <value of string>
            ha-status: <value in [disable, enable]>
            last-update: <value of integer>
            oci-region-type: <value in [commercial, government]>
            secret-token: <value of string>
            updating: <value of integer>
            group-name: <value of string>
            api-key: <value of string>
            compute-generation: <value of integer>
            ibm-region: <value in [us-south, us-east, germany, ...]>
            server-list: <value of string>
            vcenter-password: <value of string>
            vcenter-server: <value of string>
            vcenter-username: <value of string>



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



