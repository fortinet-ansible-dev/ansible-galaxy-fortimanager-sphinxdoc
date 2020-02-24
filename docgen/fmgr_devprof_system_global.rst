:source: fmgr_devprof_system_global.py

:orphan:

.. _fmgr_devprof_system_global:

fmgr_devprof_system_global -- Configure global attributes.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/system/global`
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
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">devprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure global attributes.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure global attributes.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">admin-https-redirect</span> - Enable/disable redirection of HTTP administration access to HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">admin-port</span> - Administrative access port for HTTP. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admin-scp</span> - Enable/disable using SCP to download the system configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">admin-sport</span> - Administrative access port for HTTPS. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admin-ssh-port</span> - Administrative access port for SSH. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admin-ssh-v1</span> - Enable/disable SSH v1 compatibility. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">admin-telnet-port</span> - Administrative access port for TELNET. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">admintimeout</span> - Number of minutes before an idle administrator session times out (5 - 480 minutes (8 hours), default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gui-ipv6</span> - Enable/disable IPv6 settings on the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gui-lines-per-page</span> - Number of lines to display per page for web administration. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gui-theme</span> - Color scheme for the administration GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [blue, green, melongene, red, mariner]</span> </li>
 <li><span class="li-head">language</span> - GUI display language. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [english, simch, japanese, korean, spanish, trach, french, portuguese]</span> </li>
 <li><span class="li-head">switch-controller</span> - Enable/disable switch controller feature. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/GLOBAL
      fmgr_devprof_system_global:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/GLOBAL
      fmgr_devprof_system_global:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               data:
                  admin-https-redirect: <value in [disable, enable]>
                  admin-port: <value of integer>
                  admin-scp: <value in [disable, enable]>
                  admin-sport: <value of integer>
                  admin-ssh-port: <value of integer>
                  admin-ssh-v1: <value in [disable, enable]>
                  admin-telnet-port: <value of integer>
                  admintimeout: <value of integer>
                  gui-ipv6: <value in [disable, enable]>
                  gui-lines-per-page: <value of integer>
                  gui-theme: <value in [blue, green, melongene, ...]>
                  language: <value in [english, simch, japanese, ...]>
                  switch-controller: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> admin-https-redirect </span> - Enable/disable redirection of HTTP administration access to HTTPS. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> admin-port </span> - Administrative access port for HTTP. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> admin-scp </span> - Enable/disable using SCP to download the system configuration. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> admin-sport </span> - Administrative access port for HTTPS. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> admin-ssh-port </span> - Administrative access port for SSH. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> admin-ssh-v1 </span> - Enable/disable SSH v1 compatibility. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> admin-telnet-port </span> - Administrative access port for TELNET. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> admintimeout </span> - Number of minutes before an idle administrator session times out (5 - 480 minutes (8 hours), default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> gui-ipv6 </span> - Enable/disable IPv6 settings on the GUI. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gui-lines-per-page </span> - Number of lines to display per page for web administration. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> gui-theme </span> - Color scheme for the administration GUI. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> language </span> - GUI display language. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> switch-controller </span> - Enable/disable switch controller feature. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/global</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/global</span>  </li>
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



