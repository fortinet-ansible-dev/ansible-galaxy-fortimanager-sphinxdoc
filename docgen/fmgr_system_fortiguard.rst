:source: fmgr_system_fortiguard.py

:orphan:

.. _fmgr_system_fortiguard:

fmgr_system_fortiguard -- Configure FortiGuard services.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0.0

.. warning::
   Starting in version 3.0.0, all input arguments will be named using the underscore naming convention (snake_case).
  
   - Argument name before 3.0.0: ``var-name``, ``var name``, ``var.name``
   - New argument name starting in 3.0.0: ``var_name``
  
   FortiManager Ansible v2.4+ supports both previous argument name and new underscore name.
   You will receive deprecation warnings if you keep using the previous argument name.
   You can ignore the warning by setting deprecation_warnings=False in ansible.cfg.

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device.
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v7.x.


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.15.0


FortiManager Version Compatibility
----------------------------------
.. raw:: html

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>



Parameters
----------
.. raw:: html

 <ul>
 <li><span class="li-head">access_token</span> -The token to access FortiManager without using username and password. <span class="li-normal">type: str</span> <span class="li-required">required: false</span></li> <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters. <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task. <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">forticloud_access_token</span> - Access token of forticloud managed API users, this option is available with FortiManager later than 6.4.0. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">proposed_method</span> - The overridden method for the underlying Json RPC request. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: set, update, add</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden. <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden. <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock. <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">system_fortiguard</span> - Configure FortiGuard services. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">antispam_cache</span> <b>(Alias name: antispam-cache)</b>  Enable/disable fortiguard antispam request caching. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antispam_cache_mpercent</span> <b>(Alias name: antispam-cache-mpercent)</b>  Maximum percent of fortigate memory the antispam cache is allowed to use (1 - 15%). <span class="li-normal">type: int</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antispam_cache_ttl</span> <b>(Alias name: antispam-cache-ttl)</b>  Time-to-live for antispam cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span>
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antispam_expiration</span> <b>(Alias name: antispam-expiration)</b>  Antispam expiration. <span class="li-normal">type: int</span>
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antispam_force_off</span> <b>(Alias name: antispam-force-off)</b>  Enable/disable turning off the fortiguard antispam service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antispam_license</span> <b>(Alias name: antispam-license)</b>  Antispam license. <span class="li-normal">type: int</span>
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antispam_timeout</span> <b>(Alias name: antispam-timeout)</b>  Antispam query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span>
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_join_forticloud</span> <b>(Alias name: auto-join-forticloud)</b>  Automatically connect to and login to forticloud. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_server_ip</span> <b>(Alias name: ddns-server-ip)</b>  Ip address of the fortiddns server. <span class="li-normal">type: str</span>
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_server_port</span> <b>(Alias name: ddns-server-port)</b>  Port used to communicate with fortiddns servers. <span class="li-normal">type: int</span>
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">load_balance_servers</span> <b>(Alias name: load-balance-servers)</b>  Number of servers to alternate between as first fortiguard option. <span class="li-normal">type: int</span>
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_cache</span> <b>(Alias name: outbreak-prevention-cache)</b>  Enable/disable fortiguard virus outbreak prevention cache. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_cache_mpercent</span> <b>(Alias name: outbreak-prevention-cache-mpercent)</b>  Maximum percent of memory fortiguard virus outbreak prevention cache can use (1 - 15%, default = 2). <span class="li-normal">type: int</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_cache_ttl</span> <b>(Alias name: outbreak-prevention-cache-ttl)</b>  Time-to-live for fortiguard virus outbreak prevention cache entries (300 - 86400 sec, default = 300). <span class="li-normal">type: int</span>
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_expiration</span> <b>(Alias name: outbreak-prevention-expiration)</b>  Outbreak prevention expiration. <span class="li-normal">type: int</span>
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_force_off</span> <b>(Alias name: outbreak-prevention-force-off)</b>  Turn off fortiguard virus outbreak prevention service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_license</span> <b>(Alias name: outbreak-prevention-license)</b>  Outbreak prevention license. <span class="li-normal">type: int</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_timeout</span> <b>(Alias name: outbreak-prevention-timeout)</b>  Fortiguard virus outbreak prevention time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Port used to communicate with the fortiguard servers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [53, 80, 8888, 443]</span> 
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sdns_server_ip</span> <b>(Alias name: sdns-server-ip)</b>  Ip address of the fortidns server. <span class="li-normal">type: list</span>
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sdns_server_port</span> <b>(Alias name: sdns-server-port)</b>  Port used to communicate with fortidns servers. <span class="li-normal">type: int</span>
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">service_account_id</span> <b>(Alias name: service-account-id)</b>  Service account id. <span class="li-normal">type: str</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">source_ip</span> <b>(Alias name: source-ip)</b>  Source ipv4 address used to communicate with fortiguard. <span class="li-normal">type: str</span>
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">source_ip6</span> <b>(Alias name: source-ip6)</b>  Source ipv6 address used to communicate with fortiguard. <span class="li-normal">type: str</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_server_location</span> <b>(Alias name: update-server-location)</b>  Signature update server location. <span class="li-normal">type: str</span> <span class="li-normal">choices: [any, usa, automatic, eu]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_cache</span> <b>(Alias name: webfilter-cache)</b>  Enable/disable fortiguard web filter caching. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_cache_ttl</span> <b>(Alias name: webfilter-cache-ttl)</b>  Time-to-live for web filter cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_expiration</span> <b>(Alias name: webfilter-expiration)</b>  Webfilter expiration. <span class="li-normal">type: int</span>
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_force_off</span> <b>(Alias name: webfilter-force-off)</b>  Enable/disable turning off the fortiguard web filtering service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_license</span> <b>(Alias name: webfilter-license)</b>  Webfilter license. <span class="li-normal">type: int</span>
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">webfilter_timeout</span> <b>(Alias name: webfilter-timeout)</b>  Web filter query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span>
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">protocol</span> Protocol used to communicate with the fortiguard servers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [udp, http, https]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_password</span> <b>(Alias name: proxy-password)</b>  Proxy user password. <span class="li-normal">type: list</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_server_ip</span> <b>(Alias name: proxy-server-ip)</b>  Ip address of the proxy server. <span class="li-normal">type: str</span>
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_server_port</span> <b>(Alias name: proxy-server-port)</b>  Port used to communicate with the proxy server. <span class="li-normal">type: int</span>
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">proxy_username</span> <b>(Alias name: proxy-username)</b>  Proxy user name. <span class="li-normal">type: str</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sandbox_region</span> <b>(Alias name: sandbox-region)</b>  Cloud sandbox region. <span class="li-normal">type: str</span>
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">avquery_cache_ttl</span> <b>(Alias name: avquery-cache-ttl)</b>  Time-to-live for antivirus cache entries (300 - 86400 sec, default = 1800). <span class="li-normal">type: int</span>
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.4.15</code></p>
 </div>
 </li>
 <li><span class="li-head">avquery_timeout</span> <b>(Alias name: avquery-timeout)</b>  Antivirus query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span>
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.4.15</code></p>
 </div>
 </li>
 <li><span class="li-head">avquery_cache</span> <b>(Alias name: avquery-cache)</b>  Enable/disable the fortiguard antivirus cache. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.4.15</code></p>
 </div>
 </li>
 <li><span class="li-head">avquery_cache_mpercent</span> <b>(Alias name: avquery-cache-mpercent)</b>  Maximum percent of memory the antivirus cache can use (1 - 15%, default = 2). <span class="li-normal">type: int</span>
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.4.15</code></p>
 </div>
 </li>
 <li><span class="li-head">avquery_license</span> <b>(Alias name: avquery-license)</b>  Interval of time between license checks for the fortiguard antivirus contract. <span class="li-normal">type: int</span>
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.4.15</code></p>
 </div>
 </li>
 <li><span class="li-head">avquery_force_off</span> <b>(Alias name: avquery-force-off)</b>  Turn off the fortiguard antivirus service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.0 -> v6.4.15</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiguard_anycast</span> <b>(Alias name: fortiguard-anycast)</b>  Enable/disable use of fortiguards anycast network. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">fortiguard_anycast_source</span> <b>(Alias name: fortiguard-anycast-source)</b>  Configure which of fortinets servers to provide fortiguard services in fortiguards anycast network. <span class="li-normal">type: str</span> <span class="li-normal">choices: [fortinet, aws, debug]</span> 
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">interface</span> Specify outgoing interface to reach server. <span class="li-normal">type: str</span>
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">interface_select_method</span> <b>(Alias name: interface-select-method)</b>  Specify how to select outgoing interface to reach server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [auto, sdwan, specify]</span> 
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.2.5 -> v6.2.13</code>, <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sdns_options</span> <b>(Alias name: sdns-options)</b>  Customization options for the fortiguard dns service. <span class="li-normal">type: list</span> <span class="li-normal">choices: [include-question-section]</span> 
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">anycast_sdns_server_ip</span> <b>(Alias name: anycast-sdns-server-ip)</b>  Ip address of the fortiguard anycast dns rating server. <span class="li-normal">type: str</span>
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">anycast_sdns_server_port</span> <b>(Alias name: anycast-sdns-server-port)</b>  Port to connect to on the fortiguard anycast dns rating server. <span class="li-normal">type: int</span>
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v6.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">persistent_connection</span> <b>(Alias name: persistent-connection)</b>  Enable/disable use of persistent connection to receive update notification from fortiguard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_build_proxy</span> <b>(Alias name: update-build-proxy)</b>  Enable/disable proxy dictionary rebuild. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_extdb</span> <b>(Alias name: update-extdb)</b>  Enable/disable external resource update. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_ffdb</span> <b>(Alias name: update-ffdb)</b>  Enable/disable internet service database update. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_uwdb</span> <b>(Alias name: update-uwdb)</b>  Enable/disable allowlist update. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">videofilter_expiration</span> <b>(Alias name: videofilter-expiration)</b>  Videofilter expiration. <span class="li-normal">type: int</span>
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">videofilter_license</span> <b>(Alias name: videofilter-license)</b>  Videofilter license. <span class="li-normal">type: int</span>
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ddns_server_ip6</span> <b>(Alias name: ddns-server-ip6)</b>  Ipv6 address of the fortiddns server. <span class="li-normal">type: str</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vdom</span> Fortiguard service virtual domain name. <span class="li-normal">type: str</span>
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_firmware_upgrade</span> <b>(Alias name: auto-firmware-upgrade)</b>  Enable/disable automatic patch-level firmware upgrade from fortiguard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_firmware_upgrade_day</span> <b>(Alias name: auto-firmware-upgrade-day)</b>  Allowed day(s) of the week to start automatic patch-level firmware upgrade from fortiguard. <span class="li-normal">type: list</span> <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> 
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_firmware_upgrade_end_hour</span> <b>(Alias name: auto-firmware-upgrade-end-hour)</b>  End time in the designated time window for automatic patch-level firmware upgrade from fortiguard in 24 hour time (0 ~ 23, default = 4). <span class="li-normal">type: int</span>
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_firmware_upgrade_start_hour</span> <b>(Alias name: auto-firmware-upgrade-start-hour)</b>  Start time in the designated time window for automatic patch-level firmware upgrade from fortiguard in 24 hour time (0 ~ 23, default = 2). <span class="li-normal">type: int</span>
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">sandbox_inline_scan</span> <b>(Alias name: sandbox-inline-scan)</b>  Enable/disable forticloud sandbox inline-scan. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auto_firmware_upgrade_delay</span> <b>(Alias name: auto-firmware-upgrade-delay)</b>  Delay of day(s) before installing an automatic patch-level firmware upgrade from fortiguard (default = 3). <span class="li-normal">type: int</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.4 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">gui_prompt_auto_upgrade</span> <b>(Alias name: gui-prompt-auto-upgrade)</b>  Enable/disable prompting of automatic patch-level firmware upgrade recommendation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.4 -> v7.2.9</code>, <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">FDS_license_expiring_days</span> <b>(Alias name: FDS-license-expiring-days)</b>  Threshold for number of days before fortiguard license expiration to generate license expiring event log (1 - 100 days, default = 15). <span class="li-normal">type: int</span>
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">antispam_cache_mpermille</span> <b>(Alias name: antispam-cache-mpermille)</b>  Maximum permille of fortigate memory the antispam cache is allowed to use (1 - 150). <span class="li-normal">type: int</span>
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">outbreak_prevention_cache_mpermille</span> <b>(Alias name: outbreak-prevention-cache-mpermille)</b>  Maximum permille of memory fortiguard virus outbreak prevention cache can use (1 - 150 permille, default = 1). <span class="li-normal">type: int</span>
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">update_dldb</span> <b>(Alias name: update-dldb)</b>  Enable/disable dlp signature update. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">vrf_select</span> <b>(Alias name: vrf-select)</b>  Vrf id used for connection to server. <span class="li-normal">type: int</span>
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">subscribe_update_notification</span> <b>(Alias name: subscribe-update-notification)</b>  Enable/disable subscription to receive update notification from fortiguard. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.6.3 -> latest</code></p>
 </div>
 </li>
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

  - name: Example playbook (generated based on argument schema)
    hosts: fortimanagers
    connection: httpapi
    gather_facts: false
    vars:
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_httpapi_port: 443
    tasks:
      - name: Configure FortiGuard services.
        fortinet.fortimanager.fmgr_system_fortiguard:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          system_fortiguard:
            # antispam_cache: <value in [disable, enable]>
            # antispam_cache_mpercent: <integer>
            # antispam_cache_ttl: <integer>
            # antispam_expiration: <integer>
            # antispam_force_off: <value in [disable, enable]>
            # antispam_license: <integer>
            # antispam_timeout: <integer>
            # auto_join_forticloud: <value in [disable, enable]>
            # ddns_server_ip: <string>
            # ddns_server_port: <integer>
            # load_balance_servers: <integer>
            # outbreak_prevention_cache: <value in [disable, enable]>
            # outbreak_prevention_cache_mpercent: <integer>
            # outbreak_prevention_cache_ttl: <integer>
            # outbreak_prevention_expiration: <integer>
            # outbreak_prevention_force_off: <value in [disable, enable]>
            # outbreak_prevention_license: <integer>
            # outbreak_prevention_timeout: <integer>
            # port: <value in [53, 80, 8888, ...]>
            # sdns_server_ip: <list or string>
            # sdns_server_port: <integer>
            # service_account_id: <string>
            # source_ip: <string>
            # source_ip6: <string>
            # update_server_location: <value in [any, usa, automatic, ...]>
            # webfilter_cache: <value in [disable, enable]>
            # webfilter_cache_ttl: <integer>
            # webfilter_expiration: <integer>
            # webfilter_force_off: <value in [disable, enable]>
            # webfilter_license: <integer>
            # webfilter_timeout: <integer>
            # protocol: <value in [udp, http, https]>
            # proxy_password: <list or string>
            # proxy_server_ip: <string>
            # proxy_server_port: <integer>
            # proxy_username: <string>
            # sandbox_region: <string>
            # avquery_cache_ttl: <integer>
            # avquery_timeout: <integer>
            # avquery_cache: <value in [disable, enable]>
            # avquery_cache_mpercent: <integer>
            # avquery_license: <integer>
            # avquery_force_off: <value in [disable, enable]>
            # fortiguard_anycast: <value in [disable, enable]>
            # fortiguard_anycast_source: <value in [fortinet, aws, debug]>
            # interface: <string>
            # interface_select_method: <value in [auto, sdwan, specify]>
            # sdns_options:
            #   - "include-question-section"
            # anycast_sdns_server_ip: <string>
            # anycast_sdns_server_port: <integer>
            # persistent_connection: <value in [disable, enable]>
            # update_build_proxy: <value in [disable, enable]>
            # update_extdb: <value in [disable, enable]>
            # update_ffdb: <value in [disable, enable]>
            # update_uwdb: <value in [disable, enable]>
            # videofilter_expiration: <integer>
            # videofilter_license: <integer>
            # ddns_server_ip6: <string>
            # vdom: <string>
            # auto_firmware_upgrade: <value in [disable, enable]>
            # auto_firmware_upgrade_day:
            #   - "sunday"
            #   - "monday"
            #   - "tuesday"
            #   - "wednesday"
            #   - "thursday"
            #   - "friday"
            #   - "saturday"
            # auto_firmware_upgrade_end_hour: <integer>
            # auto_firmware_upgrade_start_hour: <integer>
            # sandbox_inline_scan: <value in [disable, enable]>
            # auto_firmware_upgrade_delay: <integer>
            # gui_prompt_auto_upgrade: <value in [disable, enable]>
            # FDS_license_expiring_days: <integer>
            # antispam_cache_mpermille: <integer>
            # outbreak_prevention_cache_mpermille: <integer>
            # update_dldb: <value in [disable, enable]>
            # vrf_select: <integer>
            # subscribe_update_notification: <value in [disable, enable]>


Return Values
-------------

Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:

.. raw:: html

 <ul>
 <li> <span class="li-return">meta</span> - The result of the request.<span class="li-normal">returned: always</span> <span class="li-normal">type: dict</span></li>
 <ul class="ul-self"> <li> <span class="li-return">request_url</span> - The full url requested. <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request. <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_data</span> - The data body of the api response. <span class="li-normal">returned: optional</span> <span class="li-normal">type: list or dict</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response. <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</span></li>
 <li> <span class="li-return">system_information</span> - The information of the target system. <span class="li-normal">returned: always</span> <span class="li-normal">type: dict</span></li>
 </ul>
 <li> <span class="li-return">rc</span> - The status the request. <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">version_check_warning</span> - Warning if the parameters used in the playbook are not supported by the current FortiManager version. <span class="li-normal">returned: if at least one parameter not supported by the current FortiManager version</span> <span class="li-normal">type: list</span> </li>
 </ul>


Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)
