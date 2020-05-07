:source: fmgr_system_ha.py

:orphan:

.. _fmgr_system_ha:

fmgr_system_ha -- HA configuration.
+++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/ha`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">loose_validation</span> - Do parameter validation in a loose way <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal">default: false</span>  </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">parameters for method: [get]</span> - HA configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - HA configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">clusterid</span> - Cluster ID range (1 - 64). <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">file-quota</span> - File quota in MB (2048 - 20480). <span class="li-normal">type: int</span>  <span class="li-normal">default: 4096</span> </li>
 <li><span class="li-head">hb-interval</span> - Heartbeat interval (1 - 255). <span class="li-normal">type: int</span>  <span class="li-normal">default: 5</span> </li>
 <li><span class="li-head">hb-lost-threshold</span> - Heartbeat lost threshold (1 - 255). <span class="li-normal">type: int</span>  <span class="li-normal">default: 3</span> </li>
 <li><span class="li-head">mode</span> - Mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [standalone, master, slave]</span>  <span class="li-normal">default: standalone</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC Njg3MTI2ODY4ODEyMzY2NtF8Bgn7rP641A/Sf8QzaQhOnUfyVTFTNoFxfoZ5gzjrvXiDpQmIecJchwHMf6cMUMYR/EPxGUXBEohaVdi4YNK74+fWHu9m1Hd8UTU4tZ9UtBelMIOQUT1HMDGLFwqwKg/NXibio9aMJDW6WYPLMYpBnPng</span> </li>
 </ul>
 <li><span class="li-head">peer</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Id. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - IP address of peer. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip6</span> - IP address (V6) of peer. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::</span> </li>
 <li><span class="li-head">serial-number</span> - Serial number of peer. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Peer admin status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 </ul>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

   - To run in workspace mode, the paremeter workspace_locking_adom must be included in the task

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

    - name: REQUESTING /CLI/SYSTEM/HA
      fmgr_system_ha:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         params:
            -
               data:
                  clusterid: <value of integer default: 1>
                  file-quota: <value of integer default: 4096>
                  hb-interval: <value of integer default: 5>
                  hb-lost-threshold: <value of integer default: 3>
                  mode: <value in [standalone, master, slave] default: 'standalone'>
                  password:
                    - <value of string default: 'ENC Njg3MTI2ODY4ODEyMzY2NtF8Bgn7rP641A/Sf8QzaQhOnUfyVTFTNoFxfoZ5gzjrvXiDpQmI...'>
                  peer:
                    -
                        id: <value of integer default: 0>
                        ip: <value of string default: '0.0.0.0'>
                        ip6: <value of string default: '::'>
                        serial-number: <value of string>
                        status: <value in [disable, enable] default: 'enable'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> clusterid </span> - Cluster ID range (1 - 64). <span class="li-normal">type: int</span>  <span class="li-normal">example: 1</span>  </li>
 <li> <span class="li-return"> file-quota </span> - File quota in MB (2048 - 20480). <span class="li-normal">type: int</span>  <span class="li-normal">example: 4096</span>  </li>
 <li> <span class="li-return"> hb-interval </span> - Heartbeat interval (1 - 255). <span class="li-normal">type: int</span>  <span class="li-normal">example: 5</span>  </li>
 <li> <span class="li-return"> hb-lost-threshold </span> - Heartbeat lost threshold (1 - 255). <span class="li-normal">type: int</span>  <span class="li-normal">example: 3</span>  </li>
 <li> <span class="li-return"> mode </span> - Mode. <span class="li-normal">type: str</span>  <span class="li-normal">example: standalone</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC Njg3MTI2ODY4ODEyMzY2NtF8Bgn7rP641A/Sf8QzaQhOnUfyVTFTNoFxfoZ5gzjrvXiDpQmIecJchwHMf6cMUMYR/EPxGUXBEohaVdi4YNK74+fWHu9m1Hd8UTU4tZ9UtBelMIOQUT1HMDGLFwqwKg/NXibio9aMJDW6WYPLMYpBnPng</span>  </li>
 </ul>
 <li> <span class="li-return"> peer </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Id. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ip </span> - IP address of peer. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ip6 </span> - IP address (V6) of peer. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::</span>  </li>
 <li> <span class="li-return"> serial-number </span> - Serial number of peer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Peer admin status. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 </ul>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/ha</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/ha</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



