:source: fmgr_firewall_address.py

:orphan:

.. _fmgr_firewall_address:

fmgr_firewall_address -- Configure IPv4 addresses.
++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_address</span> - Configure IPv4 addresses. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">allow-routing</span> - Enable/disable use of this address in the static route configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">associated-interface</span> - Network interface associated with address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cache-ttl</span> - Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">country</span> - IP addresses associated to a specific country. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">allow-routing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">associated-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cache-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">country</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">epg-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">organization</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policy-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sdn</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack]</span> </li>
 <li><span class="li-head">sdn-addr-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [private, public, all]</span> </li>
 <li><span class="li-head">sdn-tag</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tenant</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipmask, iprange, fqdn, wildcard, geography, wildcard-fqdn, dynamic]</span> </li>
 <li><span class="li-head">url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wildcard</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wildcard-fqdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">end-ip</span> - Final IP address (inclusive) in the range for the address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">epg-name</span> - Endpoint group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - Match criteria filter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - Fully Qualified Domain Name address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> - IP. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj-id</span> - Object ID for NSX. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">organization</span> - Organization domain name (Syntax: organization/domain). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policy-group</span> - Policy group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sdn</span> - SDN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack]</span> </li>
 <li><span class="li-head">sdn-tag</span> - SDN Tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-ip</span> - First IP address (inclusive) in the range for the address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet</span> - IP address and subnet mask of address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet-name</span> - Subnet name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tagging</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Tag category. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Tagging entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 </ul>
 <li><span class="li-head">tenant</span> - Tenant. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipmask, iprange, fqdn, wildcard, geography, wildcard-fqdn, dynamic]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - Enable/disable address visibility in the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wildcard</span> - IP address and wildcard netmask. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wildcard-fqdn</span> - Fully Qualified Domain Name with wildcard characters. <span class="li-normal">type: str</span> </li>
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
    - name: Configure IPv4 addresses.
      fmgr_firewall_address:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_address:
            allow-routing: <value in [disable, enable]>
            associated-interface: <value of string>
            cache-ttl: <value of integer>
            color: <value of integer>
            comment: <value of string>
            country: <value of string>
            dynamic_mapping:
              -
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  allow-routing: <value in [disable, enable]>
                  associated-interface: <value of string>
                  cache-ttl: <value of integer>
                  color: <value of integer>
                  comment: <value of string>
                  country: <value of string>
                  end-ip: <value of string>
                  end-mac: <value of string>
                  epg-name: <value of string>
                  filter: <value of string>
                  fqdn: <value of string>
                  interface: <value of string>
                  obj-id: <value of string>
                  organization: <value of string>
                  policy-group: <value of string>
                  sdn: <value in [aci, aws, nsx, ...]>
                  sdn-addr-type: <value in [private, public, all]>
                  sdn-tag: <value of string>
                  start-ip: <value of string>
                  start-mac: <value of string>
                  subnet: <value of string>
                  subnet-name: <value of string>
                  tags: <value of string>
                  tenant: <value of string>
                  type: <value in [ipmask, iprange, fqdn, ...]>
                  url: <value of string>
                  uuid: <value of string>
                  visibility: <value in [disable, enable]>
                  wildcard: <value of string>
                  wildcard-fqdn: <value of string>
            end-ip: <value of string>
            epg-name: <value of string>
            filter: <value of string>
            fqdn: <value of string>
            list:
              -
                  ip: <value of string>
            name: <value of string>
            obj-id: <value of string>
            organization: <value of string>
            policy-group: <value of string>
            sdn: <value in [aci, aws, nsx, ...]>
            sdn-tag: <value of string>
            start-ip: <value of string>
            subnet: <value of string>
            subnet-name: <value of string>
            tagging:
              -
                  category: <value of string>
                  name: <value of string>
                  tags: <value of string>
            tenant: <value of string>
            type: <value in [ipmask, iprange, fqdn, ...]>
            uuid: <value of string>
            visibility: <value in [disable, enable]>
            wildcard: <value of string>
            wildcard-fqdn: <value of string>



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



