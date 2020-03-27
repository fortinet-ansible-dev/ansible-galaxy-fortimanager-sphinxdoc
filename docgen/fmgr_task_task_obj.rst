:source: fmgr_task_task_obj.py

:orphan:

.. _fmgr_task_task_obj:

fmgr_task_task_obj -- Read-only table containing the 10000 most recent tasks of the system.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get]** the following FortiManager json-rpc urls.
- `/task/task/{task}`
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
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">task</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Read-only table containing the 10000 most recent tasks of the system. This table can be used for tracking non-blocking tasks initiated by the Device Manager Command and Security Console modules.</li>
 <ul class="ul-self">
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

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



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> adom </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> end_tm </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> flags </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> history </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> detail </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> percent </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> line </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> detail </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> err </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> oid </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> percent </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> state </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: pending</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> num_done </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> num_err </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> num_lines </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> num_warn </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> percent </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> pid </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> src </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: device manager</span>  </li>
 <li> <span class="li-return"> start_tm </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> state </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: pending</span>  </li>
 <li> <span class="li-return"> title </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tot_percent </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> user </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /task/task/{task}</span>  </li>
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



