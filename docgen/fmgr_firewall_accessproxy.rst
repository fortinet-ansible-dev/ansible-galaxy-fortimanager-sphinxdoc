:source: fmgr_firewall_accessproxy.py

:orphan:

.. _fmgr_firewall_accessproxy:

fmgr_firewall_accessproxy -- Configure Access Proxy.
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.1.0

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

 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>



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
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode. <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock. <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">firewall_accessproxy</span> - Configure Access Proxy. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">api_gateway</span> <b>(Alias name: api-gateway)</b>  Api gateway. <span class="li-normal">type: list</span>
 <a id='label0' href="javascript:ContentClick('label1', 'label0');" onmouseover="ContentPreview('label1');" onmouseout="ContentUnpreview('label1');" title="click to collapse or expand..."> more... </a>
 <div id="label1" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">http_cookie_age</span> <b>(Alias name: http-cookie-age)</b>  Time in minutes that client web browsers should keep a cookie. <span class="li-normal">type: int</span>
 <a id='label2' href="javascript:ContentClick('label3', 'label2');" onmouseover="ContentPreview('label3');" onmouseout="ContentUnpreview('label3');" title="click to collapse or expand..."> more... </a>
 <div id="label3" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_domain</span> <b>(Alias name: http-cookie-domain)</b>  Domain that http cookie persistence should apply to. <span class="li-normal">type: str</span>
 <a id='label4' href="javascript:ContentClick('label5', 'label4');" onmouseover="ContentPreview('label5');" onmouseout="ContentUnpreview('label5');" title="click to collapse or expand..."> more... </a>
 <div id="label5" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_domain_from_host</span> <b>(Alias name: http-cookie-domain-from-host)</b>  Enable/disable use of http cookie domain from host field in http. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label6' href="javascript:ContentClick('label7', 'label6');" onmouseover="ContentPreview('label7');" onmouseout="ContentUnpreview('label7');" title="click to collapse or expand..."> more... </a>
 <div id="label7" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_generation</span> <b>(Alias name: http-cookie-generation)</b>  Generation of http cookie to be accepted. <span class="li-normal">type: int</span>
 <a id='label8' href="javascript:ContentClick('label9', 'label8');" onmouseover="ContentPreview('label9');" onmouseout="ContentUnpreview('label9');" title="click to collapse or expand..."> more... </a>
 <div id="label9" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_path</span> <b>(Alias name: http-cookie-path)</b>  Limit http cookie persistence to the specified path. <span class="li-normal">type: str</span>
 <a id='label10' href="javascript:ContentClick('label11', 'label10');" onmouseover="ContentPreview('label11');" onmouseout="ContentUnpreview('label11');" title="click to collapse or expand..."> more... </a>
 <div id="label11" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_share</span> <b>(Alias name: http-cookie-share)</b>  Control sharing of cookies across api gateway. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, same-ip]</span> 
 <a id='label12' href="javascript:ContentClick('label13', 'label12');" onmouseover="ContentPreview('label13');" onmouseout="ContentUnpreview('label13');" title="click to collapse or expand..."> more... </a>
 <div id="label13" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">https_cookie_secure</span> <b>(Alias name: https-cookie-secure)</b>  Enable/disable verification that inserted https cookies are secure. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label14' href="javascript:ContentClick('label15', 'label14');" onmouseover="ContentPreview('label15');" onmouseout="ContentUnpreview('label15');" title="click to collapse or expand..."> more... </a>
 <div id="label15" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Api gateway id. <span class="li-normal">type: int</span>
 <a id='label16' href="javascript:ContentClick('label17', 'label16');" onmouseover="ContentPreview('label17');" onmouseout="ContentUnpreview('label17');" title="click to collapse or expand..."> more... </a>
 <div id="label17" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldb_method</span> <b>(Alias name: ldb-method)</b>  Method used to distribute sessions to real servers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive, http-host]</span> 
 <a id='label18' href="javascript:ContentClick('label19', 'label18');" onmouseover="ContentPreview('label19');" onmouseout="ContentUnpreview('label19');" title="click to collapse or expand..."> more... </a>
 <div id="label19" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">persistence</span> Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, http-cookie]</span> 
 <a id='label20' href="javascript:ContentClick('label21', 'label20');" onmouseover="ContentPreview('label21');" onmouseout="ContentUnpreview('label21');" title="click to collapse or expand..."> more... </a>
 <div id="label21" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">realservers</span> Realservers. <span class="li-normal">type: list</span>
 <a id='label22' href="javascript:ContentClick('label23', 'label22');" onmouseover="ContentPreview('label23');" onmouseout="ContentUnpreview('label23');" title="click to collapse or expand..."> more... </a>
 <div id="label23" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">address</span> Address or address group of the real server. <span class="li-normal">type: str</span>
 <a id='label24' href="javascript:ContentClick('label25', 'label24');" onmouseover="ContentPreview('label25');" onmouseout="ContentUnpreview('label25');" title="click to collapse or expand..."> more... </a>
 <div id="label25" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">health_check</span> <b>(Alias name: health-check)</b>  Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label26' href="javascript:ContentClick('label27', 'label26');" onmouseover="ContentPreview('label27');" onmouseout="ContentUnpreview('label27');" title="click to collapse or expand..."> more... </a>
 <div id="label27" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">health_check_proto</span> <b>(Alias name: health-check-proto)</b>  Protocol of the health check monitor to use when polling to determine servers connectivity status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ping, http, tcp-connect]</span> 
 <a id='label28' href="javascript:ContentClick('label29', 'label28');" onmouseover="ContentPreview('label29');" onmouseout="ContentUnpreview('label29');" title="click to collapse or expand..."> more... </a>
 <div id="label29" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_host</span> <b>(Alias name: http-host)</b>  Http server domain name in http header. <span class="li-normal">type: str</span>
 <a id='label30' href="javascript:ContentClick('label31', 'label30');" onmouseover="ContentPreview('label31');" onmouseout="ContentUnpreview('label31');" title="click to collapse or expand..."> more... </a>
 <div id="label31" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Real server id. <span class="li-normal">type: int</span>
 <a id='label32' href="javascript:ContentClick('label33', 'label32');" onmouseover="ContentPreview('label33');" onmouseout="ContentUnpreview('label33');" title="click to collapse or expand..."> more... </a>
 <div id="label33" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ip address of the real server. <span class="li-normal">type: str</span>
 <a id='label34' href="javascript:ContentClick('label35', 'label34');" onmouseover="ContentPreview('label35');" onmouseout="ContentUnpreview('label35');" title="click to collapse or expand..."> more... </a>
 <div id="label35" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mappedport</span> Port for communicating with the real server. <span class="li-normal">type: list or str</span>
 <a id='label36' href="javascript:ContentClick('label37', 'label36');" onmouseover="ContentPreview('label37');" onmouseout="ContentUnpreview('label37');" title="click to collapse or expand..."> more... </a>
 <div id="label37" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Port for communicating with the real server. <span class="li-normal">type: int</span>
 <a id='label38' href="javascript:ContentClick('label39', 'label38');" onmouseover="ContentPreview('label39');" onmouseout="ContentUnpreview('label39');" title="click to collapse or expand..."> more... </a>
 <div id="label39" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span> <span class="li-normal">choices: [active, standby, disable]</span> 
 <a id='label40' href="javascript:ContentClick('label41', 'label40');" onmouseover="ContentPreview('label41');" onmouseout="ContentUnpreview('label41');" title="click to collapse or expand..."> more... </a>
 <div id="label41" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">weight</span> Weight of the real server. <span class="li-normal">type: int</span>
 <a id='label42' href="javascript:ContentClick('label43', 'label42');" onmouseover="ContentPreview('label43');" onmouseout="ContentUnpreview('label43');" title="click to collapse or expand..."> more... </a>
 <div id="label43" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">addr_type</span> <b>(Alias name: addr-type)</b>  Type of address. <span class="li-normal">type: str</span> <span class="li-normal">choices: [fqdn, ip]</span> 
 <a id='label44' href="javascript:ContentClick('label45', 'label44');" onmouseover="ContentPreview('label45');" onmouseout="ContentUnpreview('label45');" title="click to collapse or expand..."> more... </a>
 <div id="label45" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">domain</span> Wildcard domain name of the real server. <span class="li-normal">type: str</span>
 <a id='label46' href="javascript:ContentClick('label47', 'label46');" onmouseover="ContentPreview('label47');" onmouseout="ContentUnpreview('label47');" title="click to collapse or expand..."> more... </a>
 <div id="label47" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">holddown_interval</span> <b>(Alias name: holddown-interval)</b>  Enable/disable holddown timer. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label48' href="javascript:ContentClick('label49', 'label48');" onmouseover="ContentPreview('label49');" onmouseout="ContentUnpreview('label49');" title="click to collapse or expand..."> more... </a>
 <div id="label49" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_client_cert</span> <b>(Alias name: ssh-client-cert)</b>  Set access-proxy ssh client certificate profile. <span class="li-normal">type: str</span>
 <a id='label50' href="javascript:ContentClick('label51', 'label50');" onmouseover="ContentPreview('label51');" onmouseout="ContentUnpreview('label51');" title="click to collapse or expand..."> more... </a>
 <div id="label51" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_host_key</span> <b>(Alias name: ssh-host-key)</b>  One or more server host key. <span class="li-normal">type: list or str</span>
 <a id='label52' href="javascript:ContentClick('label53', 'label52');" onmouseover="ContentPreview('label53');" onmouseout="ContentUnpreview('label53');" title="click to collapse or expand..."> more... </a>
 <div id="label53" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_host_key_validation</span> <b>(Alias name: ssh-host-key-validation)</b>  Enable/disable ssh real server host key validation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label54' href="javascript:ContentClick('label55', 'label54');" onmouseover="ContentPreview('label55');" onmouseout="ContentUnpreview('label55');" title="click to collapse or expand..."> more... </a>
 <div id="label55" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">type</span> Tcp forwarding server type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tcp-forwarding, ssh]</span> 
 <a id='label56' href="javascript:ContentClick('label57', 'label56');" onmouseover="ContentPreview('label57');" onmouseout="ContentUnpreview('label57');" title="click to collapse or expand..."> more... </a>
 <div id="label57" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">translate_host</span> <b>(Alias name: translate-host)</b>  Enable/disable translation of hostname/ip from virtual server to real server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label58' href="javascript:ContentClick('label59', 'label58');" onmouseover="ContentPreview('label59');" onmouseout="ContentUnpreview('label59');" title="click to collapse or expand..."> more... </a>
 <div id="label59" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_auth</span> <b>(Alias name: external-auth)</b>  Enable/disable use of external browser as user-agent for saml user authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label60' href="javascript:ContentClick('label61', 'label60');" onmouseover="ContentPreview('label61');" onmouseout="ContentUnpreview('label61');" title="click to collapse or expand..."> more... </a>
 <div id="label61" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tunnel_encryption</span> <b>(Alias name: tunnel-encryption)</b>  Tunnel encryption. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label62' href="javascript:ContentClick('label63', 'label62');" onmouseover="ContentPreview('label63');" onmouseout="ContentUnpreview('label63');" title="click to collapse or expand..."> more... </a>
 <div id="label63" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">saml_server</span> <b>(Alias name: saml-server)</b>  Saml service provider configuration for vip authentication. <span class="li-normal">type: str</span>
 <a id='label64' href="javascript:ContentClick('label65', 'label64');" onmouseover="ContentPreview('label65');" onmouseout="ContentUnpreview('label65');" title="click to collapse or expand..."> more... </a>
 <div id="label65" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">service</span> Service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [http, https, tcp-forwarding, samlsp, web-portal, saas]</span> 
 <a id='label66' href="javascript:ContentClick('label67', 'label66');" onmouseover="ContentPreview('label67');" onmouseout="ContentUnpreview('label67');" title="click to collapse or expand..."> more... </a>
 <div id="label67" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_algorithm</span> <b>(Alias name: ssl-algorithm)</b>  Permitted encryption algorithms for the server side of ssl full mode sessions according to encryption strength. <span class="li-normal">type: str</span> <span class="li-normal">choices: [high, medium, low, custom]</span> 
 <a id='label68' href="javascript:ContentClick('label69', 'label68');" onmouseover="ContentPreview('label69');" onmouseout="ContentUnpreview('label69');" title="click to collapse or expand..."> more... </a>
 <div id="label69" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_cipher_suites</span> <b>(Alias name: ssl-cipher-suites)</b>  Ssl cipher suites. <span class="li-normal">type: list</span>
 <a id='label70' href="javascript:ContentClick('label71', 'label70');" onmouseover="ContentPreview('label71');" onmouseout="ContentUnpreview('label71');" title="click to collapse or expand..."> more... </a>
 <div id="label71" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">cipher</span> Cipher suite name. <span class="li-normal">type: str</span> <span class="li-normal">choices: [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, TLS-RSA-WITH-3DES-EDE-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA, TLS-RSA-WITH-AES-256-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA256, TLS-RSA-WITH-AES-256-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-RSA-WITH-SEED-CBC-SHA, TLS-RSA-WITH-ARIA-128-CBC-SHA256, TLS-RSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-RSA-WITH-DES-CBC-SHA, TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA, TLS-DHE-RSA-WITH-AES-256-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA256, TLS-DHE-RSA-WITH-AES-256-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-RSA-WITH-SEED-CBC-SHA, TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-RC4-128-SHA, TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA, TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-AES-128-GCM-SHA256, TLS-DHE-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-AES-128-CBC-SHA, TLS-DHE-DSS-WITH-AES-256-CBC-SHA, TLS-DHE-DSS-WITH-AES-128-CBC-SHA256, TLS-DHE-DSS-WITH-AES-128-GCM-SHA256, TLS-DHE-DSS-WITH-AES-256-CBC-SHA256, TLS-DHE-DSS-WITH-AES-256-GCM-SHA384, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384, TLS-RSA-WITH-AES-128-GCM-SHA256, TLS-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-DSS-WITH-SEED-CBC-SHA, TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA, TLS-DHE-DSS-WITH-DES-CBC-SHA, TLS-AES-128-GCM-SHA256, TLS-AES-256-GCM-SHA384, TLS-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA]</span> 
 <a id='label72' href="javascript:ContentClick('label73', 'label72');" onmouseover="ContentPreview('label73');" onmouseout="ContentUnpreview('label73');" title="click to collapse or expand..."> more... </a>
 <div id="label73" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Ssl/tls cipher suites priority. <span class="li-normal">type: int</span>
 <a id='label74' href="javascript:ContentClick('label75', 'label74');" onmouseover="ContentPreview('label75');" onmouseout="ContentUnpreview('label75');" title="click to collapse or expand..."> more... </a>
 <div id="label75" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">versions</span> Ssl/tls versions that the cipher suite can be used with. <span class="li-normal">type: list</span> <span class="li-normal">choices: [tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label76' href="javascript:ContentClick('label77', 'label76');" onmouseover="ContentPreview('label77');" onmouseout="ContentUnpreview('label77');" title="click to collapse or expand..."> more... </a>
 <div id="label77" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ssl_dh_bits</span> <b>(Alias name: ssl-dh-bits)</b>  Number of bits to use in the diffie-hellman exchange for rsa encryption of ssl sessions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [768, 1024, 1536, 2048, 3072, 4096]</span> 
 <a id='label78' href="javascript:ContentClick('label79', 'label78');" onmouseover="ContentPreview('label79');" onmouseout="ContentUnpreview('label79');" title="click to collapse or expand..."> more... </a>
 <div id="label79" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_max_version</span> <b>(Alias name: ssl-max-version)</b>  Highest ssl/tls version acceptable from a server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label80' href="javascript:ContentClick('label81', 'label80');" onmouseover="ContentPreview('label81');" onmouseout="ContentUnpreview('label81');" title="click to collapse or expand..."> more... </a>
 <div id="label81" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_min_version</span> <b>(Alias name: ssl-min-version)</b>  Lowest ssl/tls version acceptable from a server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label82' href="javascript:ContentClick('label83', 'label82');" onmouseover="ContentPreview('label83');" onmouseout="ContentUnpreview('label83');" title="click to collapse or expand..."> more... </a>
 <div id="label83" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">url_map</span> <b>(Alias name: url-map)</b>  Url pattern to match. <span class="li-normal">type: str</span>
 <a id='label84' href="javascript:ContentClick('label85', 'label84');" onmouseover="ContentPreview('label85');" onmouseout="ContentUnpreview('label85');" title="click to collapse or expand..."> more... </a>
 <div id="label85" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">url_map_type</span> <b>(Alias name: url-map-type)</b>  Type of url-map. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sub-string, wildcard, regex]</span> 
 <a id='label86' href="javascript:ContentClick('label87', 'label86');" onmouseover="ContentPreview('label87');" onmouseout="ContentUnpreview('label87');" title="click to collapse or expand..."> more... </a>
 <div id="label87" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">virtual_host</span> <b>(Alias name: virtual-host)</b>  Virtual host. <span class="li-normal">type: str</span>
 <a id='label88' href="javascript:ContentClick('label89', 'label88');" onmouseover="ContentPreview('label89');" onmouseout="ContentUnpreview('label89');" title="click to collapse or expand..."> more... </a>
 <div id="label89" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">saml_redirect</span> <b>(Alias name: saml-redirect)</b>  Enable/disable saml redirection after successful authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label90' href="javascript:ContentClick('label91', 'label90');" onmouseover="ContentPreview('label91');" onmouseout="ContentUnpreview('label91');" title="click to collapse or expand..."> more... </a>
 <div id="label91" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_vpn_web_portal</span> <b>(Alias name: ssl-vpn-web-portal)</b>  Ssl-vpn web portal. <span class="li-normal">type: str</span>
 <a id='label92' href="javascript:ContentClick('label93', 'label92');" onmouseover="ContentPreview('label93');" onmouseout="ContentUnpreview('label93');" title="click to collapse or expand..."> more... </a>
 <div id="label93" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application</span> Saas application controlled by this access proxy. <span class="li-normal">type: list</span>
 <a id='label94' href="javascript:ContentClick('label95', 'label94');" onmouseover="ContentPreview('label95');" onmouseout="ContentUnpreview('label95');" title="click to collapse or expand..."> more... </a>
 <div id="label95" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_renegotiation</span> <b>(Alias name: ssl-renegotiation)</b>  Enable/disable secure renegotiation to comply with rfc 5746. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label96' href="javascript:ContentClick('label97', 'label96');" onmouseover="ContentPreview('label97');" onmouseout="ContentUnpreview('label97');" title="click to collapse or expand..."> more... </a>
 <div id="label97" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">h2_support</span> <b>(Alias name: h2-support)</b>  Http2 support, default=enable. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label98' href="javascript:ContentClick('label99', 'label98');" onmouseover="ContentPreview('label99');" onmouseout="ContentUnpreview('label99');" title="click to collapse or expand..."> more... </a>
 <div id="label99" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">h3_support</span> <b>(Alias name: h3-support)</b>  Http3/quic support, default=disable. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label100' href="javascript:ContentClick('label101', 'label100');" onmouseover="ContentPreview('label101');" onmouseout="ContentUnpreview('label101');" title="click to collapse or expand..."> more... </a>
 <div id="label101" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic</span> Quic. <span class="li-normal">type: dict</span>
 <a id='label102' href="javascript:ContentClick('label103', 'label102');" onmouseover="ContentPreview('label103');" onmouseout="ContentUnpreview('label103');" title="click to collapse or expand..."> more... </a>
 <div id="label103" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">ack_delay_exponent</span> <b>(Alias name: ack-delay-exponent)</b>  Ack delay exponent (1 - 20, default = 3). <span class="li-normal">type: int</span>
 <a id='label104' href="javascript:ContentClick('label105', 'label104');" onmouseover="ContentPreview('label105');" onmouseout="ContentUnpreview('label105');" title="click to collapse or expand..."> more... </a>
 <div id="label105" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">active_connection_id_limit</span> <b>(Alias name: active-connection-id-limit)</b>  Active connection id limit (1 - 8, default = 2). <span class="li-normal">type: int</span>
 <a id='label106' href="javascript:ContentClick('label107', 'label106');" onmouseover="ContentPreview('label107');" onmouseout="ContentUnpreview('label107');" title="click to collapse or expand..."> more... </a>
 <div id="label107" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">active_migration</span> <b>(Alias name: active-migration)</b>  Enable/disable active migration (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label108' href="javascript:ContentClick('label109', 'label108');" onmouseover="ContentPreview('label109');" onmouseout="ContentUnpreview('label109');" title="click to collapse or expand..."> more... </a>
 <div id="label109" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">grease_quic_bit</span> <b>(Alias name: grease-quic-bit)</b>  Enable/disable grease quic bit (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label110' href="javascript:ContentClick('label111', 'label110');" onmouseover="ContentPreview('label111');" onmouseout="ContentUnpreview('label111');" title="click to collapse or expand..."> more... </a>
 <div id="label111" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_ack_delay</span> <b>(Alias name: max-ack-delay)</b>  Maximum ack delay in milliseconds (1 - 16383, default = 25). <span class="li-normal">type: int</span>
 <a id='label112' href="javascript:ContentClick('label113', 'label112');" onmouseover="ContentPreview('label113');" onmouseout="ContentUnpreview('label113');" title="click to collapse or expand..."> more... </a>
 <div id="label113" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_datagram_frame_size</span> <b>(Alias name: max-datagram-frame-size)</b>  Maximum datagram frame size in bytes (1 - 1500, default = 1500). <span class="li-normal">type: int</span>
 <a id='label114' href="javascript:ContentClick('label115', 'label114');" onmouseover="ContentPreview('label115');" onmouseout="ContentUnpreview('label115');" title="click to collapse or expand..."> more... </a>
 <div id="label115" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_idle_timeout</span> <b>(Alias name: max-idle-timeout)</b>  Maximum idle timeout milliseconds (1 - 60000, default = 30000). <span class="li-normal">type: int</span>
 <a id='label116' href="javascript:ContentClick('label117', 'label116');" onmouseover="ContentPreview('label117');" onmouseout="ContentUnpreview('label117');" title="click to collapse or expand..."> more... </a>
 <div id="label117" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_udp_payload_size</span> <b>(Alias name: max-udp-payload-size)</b>  Maximum udp payload size in bytes (1200 - 1500, default = 1500). <span class="li-normal">type: int</span>
 <a id='label118' href="javascript:ContentClick('label119', 'label118');" onmouseover="ContentPreview('label119');" onmouseout="ContentUnpreview('label119');" title="click to collapse or expand..."> more... </a>
 <div id="label119" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 </ul>
 </li>
 <li><span class="li-head">client_cert</span> <b>(Alias name: client-cert)</b>  Enable/disable to request client certificate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label120' href="javascript:ContentClick('label121', 'label120');" onmouseover="ContentPreview('label121');" onmouseout="ContentUnpreview('label121');" title="click to collapse or expand..."> more... </a>
 <div id="label121" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">empty_cert_action</span> <b>(Alias name: empty-cert-action)</b>  Action of an empty client certificate. <span class="li-normal">type: str</span> <span class="li-normal">choices: [block, accept, accept-unmanageable]</span> 
 <a id='label122' href="javascript:ContentClick('label123', 'label122');" onmouseover="ContentPreview('label123');" onmouseout="ContentUnpreview('label123');" title="click to collapse or expand..."> more... </a>
 <div id="label123" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldb_method</span> <b>(Alias name: ldb-method)</b>  Method used to distribute sessions to ssl real servers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive]</span> 
 <a id='label124' href="javascript:ContentClick('label125', 'label124');" onmouseover="ContentPreview('label125');" onmouseout="ContentUnpreview('label125');" title="click to collapse or expand..."> more... </a>
 <div id="label125" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Access proxy name. <span class="li-normal">type: str</span>
 <a id='label126' href="javascript:ContentClick('label127', 'label126');" onmouseover="ContentPreview('label127');" onmouseout="ContentUnpreview('label127');" title="click to collapse or expand..."> more... </a>
 <div id="label127" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">realservers</span> Realservers. <span class="li-normal">type: list</span>
 <a id='label128' href="javascript:ContentClick('label129', 'label128');" onmouseover="ContentPreview('label129');" onmouseout="ContentUnpreview('label129');" title="click to collapse or expand..."> more... </a>
 <div id="label129" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">id</span> Real server id. <span class="li-normal">type: int</span>
 <a id='label130' href="javascript:ContentClick('label131', 'label130');" onmouseover="ContentPreview('label131');" onmouseout="ContentUnpreview('label131');" title="click to collapse or expand..."> more... </a>
 <div id="label131" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ip address of the real server. <span class="li-normal">type: str</span>
 <a id='label132' href="javascript:ContentClick('label133', 'label132');" onmouseover="ContentPreview('label133');" onmouseout="ContentUnpreview('label133');" title="click to collapse or expand..."> more... </a>
 <div id="label133" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Port for communicating with the real server. <span class="li-normal">type: int</span>
 <a id='label134' href="javascript:ContentClick('label135', 'label134');" onmouseover="ContentPreview('label135');" onmouseout="ContentUnpreview('label135');" title="click to collapse or expand..."> more... </a>
 <div id="label135" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span> <span class="li-normal">choices: [active, standby, disable]</span> 
 <a id='label136' href="javascript:ContentClick('label137', 'label136');" onmouseover="ContentPreview('label137');" onmouseout="ContentUnpreview('label137');" title="click to collapse or expand..."> more... </a>
 <div id="label137" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">weight</span> Weight of the real server. <span class="li-normal">type: int</span>
 <a id='label138' href="javascript:ContentClick('label139', 'label138');" onmouseover="ContentPreview('label139');" onmouseout="ContentUnpreview('label139');" title="click to collapse or expand..."> more... </a>
 <div id="label139" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">server_pubkey_auth</span> <b>(Alias name: server-pubkey-auth)</b>  Enable/disable ssh real server public key authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label140' href="javascript:ContentClick('label141', 'label140');" onmouseover="ContentPreview('label141');" onmouseout="ContentUnpreview('label141');" title="click to collapse or expand..."> more... </a>
 <div id="label141" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">server_pubkey_auth_settings</span> <b>(Alias name: server-pubkey-auth-settings)</b>  Server pubkey auth settings. <span class="li-normal">type: dict</span>
 <a id='label142' href="javascript:ContentClick('label143', 'label142');" onmouseover="ContentPreview('label143');" onmouseout="ContentUnpreview('label143');" title="click to collapse or expand..."> more... </a>
 <div id="label143" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">auth_ca</span> <b>(Alias name: auth-ca)</b>  Name of the ssh server public key authentication ca. <span class="li-normal">type: str</span>
 <a id='label144' href="javascript:ContentClick('label145', 'label144');" onmouseover="ContentPreview('label145');" onmouseout="ContentUnpreview('label145');" title="click to collapse or expand..."> more... </a>
 <div id="label145" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">cert_extension</span> <b>(Alias name: cert-extension)</b>  Cert extension. <span class="li-normal">type: list</span>
 <a id='label146' href="javascript:ContentClick('label147', 'label146');" onmouseover="ContentPreview('label147');" onmouseout="ContentUnpreview('label147');" title="click to collapse or expand..."> more... </a>
 <div id="label147" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">critical</span> Critical option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [no, yes]</span> 
 <a id='label148' href="javascript:ContentClick('label149', 'label148');" onmouseover="ContentPreview('label149');" onmouseout="ContentUnpreview('label149');" title="click to collapse or expand..."> more... </a>
 <div id="label149" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">data</span> Name of certificate extension. <span class="li-normal">type: str</span>
 <a id='label150' href="javascript:ContentClick('label151', 'label150');" onmouseover="ContentPreview('label151');" onmouseout="ContentUnpreview('label151');" title="click to collapse or expand..."> more... </a>
 <div id="label151" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">name</span> Name of certificate extension. <span class="li-normal">type: str</span>
 <a id='label152' href="javascript:ContentClick('label153', 'label152');" onmouseover="ContentPreview('label153');" onmouseout="ContentUnpreview('label153');" title="click to collapse or expand..."> more... </a>
 <div id="label153" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">type</span> Type of certificate extension. <span class="li-normal">type: str</span> <span class="li-normal">choices: [fixed, user]</span> 
 <a id='label154' href="javascript:ContentClick('label155', 'label154');" onmouseover="ContentPreview('label155');" onmouseout="ContentUnpreview('label155');" title="click to collapse or expand..."> more... </a>
 <div id="label155" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">permit_agent_forwarding</span> <b>(Alias name: permit-agent-forwarding)</b>  Enable/disable appending permit-agent-forwarding certificate extension. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label156' href="javascript:ContentClick('label157', 'label156');" onmouseover="ContentPreview('label157');" onmouseout="ContentUnpreview('label157');" title="click to collapse or expand..."> more... </a>
 <div id="label157" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">permit_port_forwarding</span> <b>(Alias name: permit-port-forwarding)</b>  Enable/disable appending permit-port-forwarding certificate extension. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label158' href="javascript:ContentClick('label159', 'label158');" onmouseover="ContentPreview('label159');" onmouseout="ContentUnpreview('label159');" title="click to collapse or expand..."> more... </a>
 <div id="label159" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">permit_pty</span> <b>(Alias name: permit-pty)</b>  Enable/disable appending permit-pty certificate extension. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label160' href="javascript:ContentClick('label161', 'label160');" onmouseover="ContentPreview('label161');" onmouseout="ContentUnpreview('label161');" title="click to collapse or expand..."> more... </a>
 <div id="label161" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">permit_user_rc</span> <b>(Alias name: permit-user-rc)</b>  Enable/disable appending permit-user-rc certificate extension. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label162' href="javascript:ContentClick('label163', 'label162');" onmouseover="ContentPreview('label163');" onmouseout="ContentUnpreview('label163');" title="click to collapse or expand..."> more... </a>
 <div id="label163" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">permit_x11_forwarding</span> <b>(Alias name: permit-x11-forwarding)</b>  Enable/disable appending permit-x11-forwarding certificate extension. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label164' href="javascript:ContentClick('label165', 'label164');" onmouseover="ContentPreview('label165');" onmouseout="ContentUnpreview('label165');" title="click to collapse or expand..."> more... </a>
 <div id="label165" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">source_address</span> <b>(Alias name: source-address)</b>  Enable/disable appending source-address certificate critical option. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label166' href="javascript:ContentClick('label167', 'label166');" onmouseover="ContentPreview('label167');" onmouseout="ContentUnpreview('label167');" title="click to collapse or expand..."> more... </a>
 <div id="label167" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">vip</span> Virtual ip name. <span class="li-normal">type: str</span>
 <a id='label168' href="javascript:ContentClick('label169', 'label168');" onmouseover="ContentPreview('label169');" onmouseout="ContentUnpreview('label169');" title="click to collapse or expand..."> more... </a>
 <div id="label169" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">api_gateway6</span> <b>(Alias name: api-gateway6)</b>  Api gateway6. <span class="li-normal">type: list</span>
 <a id='label170' href="javascript:ContentClick('label171', 'label170');" onmouseover="ContentPreview('label171');" onmouseout="ContentUnpreview('label171');" title="click to collapse or expand..."> more... </a>
 <div id="label171" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">http_cookie_age</span> <b>(Alias name: http-cookie-age)</b>  Time in minutes that client web browsers should keep a cookie. <span class="li-normal">type: int</span>
 <a id='label172' href="javascript:ContentClick('label173', 'label172');" onmouseover="ContentPreview('label173');" onmouseout="ContentUnpreview('label173');" title="click to collapse or expand..."> more... </a>
 <div id="label173" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_domain</span> <b>(Alias name: http-cookie-domain)</b>  Domain that http cookie persistence should apply to. <span class="li-normal">type: str</span>
 <a id='label174' href="javascript:ContentClick('label175', 'label174');" onmouseover="ContentPreview('label175');" onmouseout="ContentUnpreview('label175');" title="click to collapse or expand..."> more... </a>
 <div id="label175" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_domain_from_host</span> <b>(Alias name: http-cookie-domain-from-host)</b>  Enable/disable use of http cookie domain from host field in http. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label176' href="javascript:ContentClick('label177', 'label176');" onmouseover="ContentPreview('label177');" onmouseout="ContentUnpreview('label177');" title="click to collapse or expand..."> more... </a>
 <div id="label177" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_generation</span> <b>(Alias name: http-cookie-generation)</b>  Generation of http cookie to be accepted. <span class="li-normal">type: int</span>
 <a id='label178' href="javascript:ContentClick('label179', 'label178');" onmouseover="ContentPreview('label179');" onmouseout="ContentUnpreview('label179');" title="click to collapse or expand..."> more... </a>
 <div id="label179" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_path</span> <b>(Alias name: http-cookie-path)</b>  Limit http cookie persistence to the specified path. <span class="li-normal">type: str</span>
 <a id='label180' href="javascript:ContentClick('label181', 'label180');" onmouseover="ContentPreview('label181');" onmouseout="ContentUnpreview('label181');" title="click to collapse or expand..."> more... </a>
 <div id="label181" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_cookie_share</span> <b>(Alias name: http-cookie-share)</b>  Control sharing of cookies across api gateway. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, same-ip]</span> 
 <a id='label182' href="javascript:ContentClick('label183', 'label182');" onmouseover="ContentPreview('label183');" onmouseout="ContentUnpreview('label183');" title="click to collapse or expand..."> more... </a>
 <div id="label183" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">https_cookie_secure</span> <b>(Alias name: https-cookie-secure)</b>  Enable/disable verification that inserted https cookies are secure. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label184' href="javascript:ContentClick('label185', 'label184');" onmouseover="ContentPreview('label185');" onmouseout="ContentUnpreview('label185');" title="click to collapse or expand..."> more... </a>
 <div id="label185" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Api gateway id. <span class="li-normal">type: int</span>
 <a id='label186' href="javascript:ContentClick('label187', 'label186');" onmouseover="ContentPreview('label187');" onmouseout="ContentUnpreview('label187');" title="click to collapse or expand..."> more... </a>
 <div id="label187" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ldb_method</span> <b>(Alias name: ldb-method)</b>  Method used to distribute sessions to real servers. <span class="li-normal">type: str</span> <span class="li-normal">choices: [static, round-robin, weighted, first-alive, http-host]</span> 
 <a id='label188' href="javascript:ContentClick('label189', 'label188');" onmouseover="ContentPreview('label189');" onmouseout="ContentUnpreview('label189');" title="click to collapse or expand..."> more... </a>
 <div id="label189" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">persistence</span> Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session. <span class="li-normal">type: str</span> <span class="li-normal">choices: [none, http-cookie]</span> 
 <a id='label190' href="javascript:ContentClick('label191', 'label190');" onmouseover="ContentPreview('label191');" onmouseout="ContentUnpreview('label191');" title="click to collapse or expand..."> more... </a>
 <div id="label191" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">realservers</span> Realservers. <span class="li-normal">type: list</span>
 <a id='label192' href="javascript:ContentClick('label193', 'label192');" onmouseover="ContentPreview('label193');" onmouseout="ContentUnpreview('label193');" title="click to collapse or expand..."> more... </a>
 <div id="label193" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">addr_type</span> <b>(Alias name: addr-type)</b>  Type of address. <span class="li-normal">type: str</span> <span class="li-normal">choices: [fqdn, ip]</span> 
 <a id='label194' href="javascript:ContentClick('label195', 'label194');" onmouseover="ContentPreview('label195');" onmouseout="ContentUnpreview('label195');" title="click to collapse or expand..."> more... </a>
 <div id="label195" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">address</span> Address or address group of the real server. <span class="li-normal">type: str</span>
 <a id='label196' href="javascript:ContentClick('label197', 'label196');" onmouseover="ContentPreview('label197');" onmouseout="ContentUnpreview('label197');" title="click to collapse or expand..."> more... </a>
 <div id="label197" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">domain</span> Wildcard domain name of the real server. <span class="li-normal">type: str</span>
 <a id='label198' href="javascript:ContentClick('label199', 'label198');" onmouseover="ContentPreview('label199');" onmouseout="ContentUnpreview('label199');" title="click to collapse or expand..."> more... </a>
 <div id="label199" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">health_check</span> <b>(Alias name: health-check)</b>  Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label200' href="javascript:ContentClick('label201', 'label200');" onmouseover="ContentPreview('label201');" onmouseout="ContentUnpreview('label201');" title="click to collapse or expand..."> more... </a>
 <div id="label201" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">health_check_proto</span> <b>(Alias name: health-check-proto)</b>  Protocol of the health check monitor to use when polling to determine servers connectivity status. <span class="li-normal">type: str</span> <span class="li-normal">choices: [ping, http, tcp-connect]</span> 
 <a id='label202' href="javascript:ContentClick('label203', 'label202');" onmouseover="ContentPreview('label203');" onmouseout="ContentUnpreview('label203');" title="click to collapse or expand..."> more... </a>
 <div id="label203" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">holddown_interval</span> <b>(Alias name: holddown-interval)</b>  Enable/disable holddown timer. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label204' href="javascript:ContentClick('label205', 'label204');" onmouseover="ContentPreview('label205');" onmouseout="ContentUnpreview('label205');" title="click to collapse or expand..."> more... </a>
 <div id="label205" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_host</span> <b>(Alias name: http-host)</b>  Http server domain name in http header. <span class="li-normal">type: str</span>
 <a id='label206' href="javascript:ContentClick('label207', 'label206');" onmouseover="ContentPreview('label207');" onmouseout="ContentUnpreview('label207');" title="click to collapse or expand..."> more... </a>
 <div id="label207" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">id</span> Real server id. <span class="li-normal">type: int</span>
 <a id='label208' href="javascript:ContentClick('label209', 'label208');" onmouseover="ContentPreview('label209');" onmouseout="ContentUnpreview('label209');" title="click to collapse or expand..."> more... </a>
 <div id="label209" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ip</span> Ipv6 address of the real server. <span class="li-normal">type: str</span>
 <a id='label210' href="javascript:ContentClick('label211', 'label210');" onmouseover="ContentPreview('label211');" onmouseout="ContentUnpreview('label211');" title="click to collapse or expand..."> more... </a>
 <div id="label211" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">mappedport</span> Port for communicating with the real server. <span class="li-normal">type: list or str</span>
 <a id='label212' href="javascript:ContentClick('label213', 'label212');" onmouseover="ContentPreview('label213');" onmouseout="ContentUnpreview('label213');" title="click to collapse or expand..."> more... </a>
 <div id="label213" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">port</span> Port for communicating with the real server. <span class="li-normal">type: int</span>
 <a id='label214' href="javascript:ContentClick('label215', 'label214');" onmouseover="ContentPreview('label215');" onmouseout="ContentUnpreview('label215');" title="click to collapse or expand..."> more... </a>
 <div id="label215" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_client_cert</span> <b>(Alias name: ssh-client-cert)</b>  Set access-proxy ssh client certificate profile. <span class="li-normal">type: str</span>
 <a id='label216' href="javascript:ContentClick('label217', 'label216');" onmouseover="ContentPreview('label217');" onmouseout="ContentUnpreview('label217');" title="click to collapse or expand..."> more... </a>
 <div id="label217" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_host_key</span> <b>(Alias name: ssh-host-key)</b>  One or more server host key. <span class="li-normal">type: list or str</span>
 <a id='label218' href="javascript:ContentClick('label219', 'label218');" onmouseover="ContentPreview('label219');" onmouseout="ContentUnpreview('label219');" title="click to collapse or expand..."> more... </a>
 <div id="label219" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssh_host_key_validation</span> <b>(Alias name: ssh-host-key-validation)</b>  Enable/disable ssh real server host key validation. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label220' href="javascript:ContentClick('label221', 'label220');" onmouseover="ContentPreview('label221');" onmouseout="ContentUnpreview('label221');" title="click to collapse or expand..."> more... </a>
 <div id="label221" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">status</span> Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span> <span class="li-normal">choices: [active, standby, disable]</span> 
 <a id='label222' href="javascript:ContentClick('label223', 'label222');" onmouseover="ContentPreview('label223');" onmouseout="ContentUnpreview('label223');" title="click to collapse or expand..."> more... </a>
 <div id="label223" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">type</span> Tcp forwarding server type. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tcp-forwarding, ssh]</span> 
 <a id='label224' href="javascript:ContentClick('label225', 'label224');" onmouseover="ContentPreview('label225');" onmouseout="ContentUnpreview('label225');" title="click to collapse or expand..."> more... </a>
 <div id="label225" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">weight</span> Weight of the real server. <span class="li-normal">type: int</span>
 <a id='label226' href="javascript:ContentClick('label227', 'label226');" onmouseover="ContentPreview('label227');" onmouseout="ContentUnpreview('label227');" title="click to collapse or expand..."> more... </a>
 <div id="label227" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">translate_host</span> <b>(Alias name: translate-host)</b>  Enable/disable translation of hostname/ip from virtual server to real server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label228' href="javascript:ContentClick('label229', 'label228');" onmouseover="ContentPreview('label229');" onmouseout="ContentUnpreview('label229');" title="click to collapse or expand..."> more... </a>
 <div id="label229" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">external_auth</span> <b>(Alias name: external-auth)</b>  Enable/disable use of external browser as user-agent for saml user authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label230' href="javascript:ContentClick('label231', 'label230');" onmouseover="ContentPreview('label231');" onmouseout="ContentUnpreview('label231');" title="click to collapse or expand..."> more... </a>
 <div id="label231" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">tunnel_encryption</span> <b>(Alias name: tunnel-encryption)</b>  Tunnel encryption. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label232' href="javascript:ContentClick('label233', 'label232');" onmouseover="ContentPreview('label233');" onmouseout="ContentUnpreview('label233');" title="click to collapse or expand..."> more... </a>
 <div id="label233" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.0 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">saml_redirect</span> <b>(Alias name: saml-redirect)</b>  Enable/disable saml redirection after successful authentication. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label234' href="javascript:ContentClick('label235', 'label234');" onmouseover="ContentPreview('label235');" onmouseout="ContentUnpreview('label235');" title="click to collapse or expand..."> more... </a>
 <div id="label235" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">saml_server</span> <b>(Alias name: saml-server)</b>  Saml service provider configuration for vip authentication. <span class="li-normal">type: str</span>
 <a id='label236' href="javascript:ContentClick('label237', 'label236');" onmouseover="ContentPreview('label237');" onmouseout="ContentUnpreview('label237');" title="click to collapse or expand..."> more... </a>
 <div id="label237" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">service</span> Service. <span class="li-normal">type: str</span> <span class="li-normal">choices: [http, https, tcp-forwarding, samlsp, web-portal, saas]</span> 
 <a id='label238' href="javascript:ContentClick('label239', 'label238');" onmouseover="ContentPreview('label239');" onmouseout="ContentUnpreview('label239');" title="click to collapse or expand..."> more... </a>
 <div id="label239" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_algorithm</span> <b>(Alias name: ssl-algorithm)</b>  Permitted encryption algorithms for the server side of ssl full mode sessions according to encryption strength. <span class="li-normal">type: str</span> <span class="li-normal">choices: [high, medium, low]</span> 
 <a id='label240' href="javascript:ContentClick('label241', 'label240');" onmouseover="ContentPreview('label241');" onmouseout="ContentUnpreview('label241');" title="click to collapse or expand..."> more... </a>
 <div id="label241" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_cipher_suites</span> <b>(Alias name: ssl-cipher-suites)</b>  Ssl cipher suites. <span class="li-normal">type: list</span>
 <a id='label242' href="javascript:ContentClick('label243', 'label242');" onmouseover="ContentPreview('label243');" onmouseout="ContentUnpreview('label243');" title="click to collapse or expand..."> more... </a>
 <div id="label243" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">cipher</span> Cipher suite name. <span class="li-normal">type: str</span> <span class="li-normal">choices: [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, TLS-RSA-WITH-3DES-EDE-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA, TLS-RSA-WITH-AES-256-CBC-SHA, TLS-RSA-WITH-AES-128-CBC-SHA256, TLS-RSA-WITH-AES-256-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-RSA-WITH-SEED-CBC-SHA, TLS-RSA-WITH-ARIA-128-CBC-SHA256, TLS-RSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-RSA-WITH-DES-CBC-SHA, TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA, TLS-DHE-RSA-WITH-AES-256-CBC-SHA, TLS-DHE-RSA-WITH-AES-128-CBC-SHA256, TLS-DHE-RSA-WITH-AES-256-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-RSA-WITH-SEED-CBC-SHA, TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-RC4-128-SHA, TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA, TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256, TLS-DHE-RSA-WITH-AES-128-GCM-SHA256, TLS-DHE-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-AES-128-CBC-SHA, TLS-DHE-DSS-WITH-AES-256-CBC-SHA, TLS-DHE-DSS-WITH-AES-128-CBC-SHA256, TLS-DHE-DSS-WITH-AES-128-GCM-SHA256, TLS-DHE-DSS-WITH-AES-256-CBC-SHA256, TLS-DHE-DSS-WITH-AES-256-GCM-SHA384, TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA, TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384, TLS-RSA-WITH-AES-128-GCM-SHA256, TLS-RSA-WITH-AES-256-GCM-SHA384, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA, TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256, TLS-DHE-DSS-WITH-SEED-CBC-SHA, TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256, TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384, TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256, TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384, TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA, TLS-DHE-DSS-WITH-DES-CBC-SHA, TLS-AES-128-GCM-SHA256, TLS-AES-256-GCM-SHA384, TLS-CHACHA20-POLY1305-SHA256, TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA]</span> 
 <a id='label244' href="javascript:ContentClick('label245', 'label244');" onmouseover="ContentPreview('label245');" onmouseout="ContentUnpreview('label245');" title="click to collapse or expand..."> more... </a>
 <div id="label245" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">priority</span> Ssl/tls cipher suites priority. <span class="li-normal">type: int</span>
 <a id='label246' href="javascript:ContentClick('label247', 'label246');" onmouseover="ContentPreview('label247');" onmouseout="ContentUnpreview('label247');" title="click to collapse or expand..."> more... </a>
 <div id="label247" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">versions</span> Ssl/tls versions that the cipher suite can be used with. <span class="li-normal">type: list</span> <span class="li-normal">choices: [tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label248' href="javascript:ContentClick('label249', 'label248');" onmouseover="ContentPreview('label249');" onmouseout="ContentUnpreview('label249');" title="click to collapse or expand..."> more... </a>
 <div id="label249" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 <li><span class="li-head">ssl_dh_bits</span> <b>(Alias name: ssl-dh-bits)</b>  Number of bits to use in the diffie-hellman exchange for rsa encryption of ssl sessions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [768, 1024, 1536, 2048, 3072, 4096]</span> 
 <a id='label250' href="javascript:ContentClick('label251', 'label250');" onmouseover="ContentPreview('label251');" onmouseout="ContentUnpreview('label251');" title="click to collapse or expand..."> more... </a>
 <div id="label251" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_max_version</span> <b>(Alias name: ssl-max-version)</b>  Highest ssl/tls version acceptable from a server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label252' href="javascript:ContentClick('label253', 'label252');" onmouseover="ContentPreview('label253');" onmouseout="ContentUnpreview('label253');" title="click to collapse or expand..."> more... </a>
 <div id="label253" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_min_version</span> <b>(Alias name: ssl-min-version)</b>  Lowest ssl/tls version acceptable from a server. <span class="li-normal">type: str</span> <span class="li-normal">choices: [tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> 
 <a id='label254' href="javascript:ContentClick('label255', 'label254');" onmouseover="ContentPreview('label255');" onmouseout="ContentUnpreview('label255');" title="click to collapse or expand..."> more... </a>
 <div id="label255" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_vpn_web_portal</span> <b>(Alias name: ssl-vpn-web-portal)</b>  Ssl-vpn web portal. <span class="li-normal">type: str</span>
 <a id='label256' href="javascript:ContentClick('label257', 'label256');" onmouseover="ContentPreview('label257');" onmouseout="ContentUnpreview('label257');" title="click to collapse or expand..."> more... </a>
 <div id="label257" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">url_map</span> <b>(Alias name: url-map)</b>  Url pattern to match. <span class="li-normal">type: str</span>
 <a id='label258' href="javascript:ContentClick('label259', 'label258');" onmouseover="ContentPreview('label259');" onmouseout="ContentUnpreview('label259');" title="click to collapse or expand..."> more... </a>
 <div id="label259" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">url_map_type</span> <b>(Alias name: url-map-type)</b>  Type of url-map. <span class="li-normal">type: str</span> <span class="li-normal">choices: [sub-string, wildcard, regex]</span> 
 <a id='label260' href="javascript:ContentClick('label261', 'label260');" onmouseover="ContentPreview('label261');" onmouseout="ContentUnpreview('label261');" title="click to collapse or expand..."> more... </a>
 <div id="label261" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">virtual_host</span> <b>(Alias name: virtual-host)</b>  Virtual host. <span class="li-normal">type: str</span>
 <a id='label262' href="javascript:ContentClick('label263', 'label262');" onmouseover="ContentPreview('label263');" onmouseout="ContentUnpreview('label263');" title="click to collapse or expand..."> more... </a>
 <div id="label263" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">application</span> Saas application controlled by this access proxy. <span class="li-normal">type: list</span>
 <a id='label264' href="javascript:ContentClick('label265', 'label264');" onmouseover="ContentPreview('label265');" onmouseout="ContentUnpreview('label265');" title="click to collapse or expand..."> more... </a>
 <div id="label265" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">ssl_renegotiation</span> <b>(Alias name: ssl-renegotiation)</b>  Enable/disable secure renegotiation to comply with rfc 5746. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label266' href="javascript:ContentClick('label267', 'label266');" onmouseover="ContentPreview('label267');" onmouseout="ContentUnpreview('label267');" title="click to collapse or expand..."> more... </a>
 <div id="label267" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">h2_support</span> <b>(Alias name: h2-support)</b>  Http2 support, default=enable. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label268' href="javascript:ContentClick('label269', 'label268');" onmouseover="ContentPreview('label269');" onmouseout="ContentUnpreview('label269');" title="click to collapse or expand..."> more... </a>
 <div id="label269" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">h3_support</span> <b>(Alias name: h3-support)</b>  Http3/quic support, default=disable. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label270' href="javascript:ContentClick('label271', 'label270');" onmouseover="ContentPreview('label271');" onmouseout="ContentUnpreview('label271');" title="click to collapse or expand..."> more... </a>
 <div id="label271" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">quic</span> Quic. <span class="li-normal">type: dict</span>
 <a id='label272' href="javascript:ContentClick('label273', 'label272');" onmouseover="ContentPreview('label273');" onmouseout="ContentUnpreview('label273');" title="click to collapse or expand..."> more... </a>
 <div id="label273" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 <ul class="ul-self">
 <li><span class="li-head">ack_delay_exponent</span> <b>(Alias name: ack-delay-exponent)</b>  Ack delay exponent (1 - 20, default = 3). <span class="li-normal">type: int</span>
 <a id='label274' href="javascript:ContentClick('label275', 'label274');" onmouseover="ContentPreview('label275');" onmouseout="ContentUnpreview('label275');" title="click to collapse or expand..."> more... </a>
 <div id="label275" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">active_connection_id_limit</span> <b>(Alias name: active-connection-id-limit)</b>  Active connection id limit (1 - 8, default = 2). <span class="li-normal">type: int</span>
 <a id='label276' href="javascript:ContentClick('label277', 'label276');" onmouseover="ContentPreview('label277');" onmouseout="ContentUnpreview('label277');" title="click to collapse or expand..."> more... </a>
 <div id="label277" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">active_migration</span> <b>(Alias name: active-migration)</b>  Enable/disable active migration (default = disable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label278' href="javascript:ContentClick('label279', 'label278');" onmouseover="ContentPreview('label279');" onmouseout="ContentUnpreview('label279');" title="click to collapse or expand..."> more... </a>
 <div id="label279" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">grease_quic_bit</span> <b>(Alias name: grease-quic-bit)</b>  Enable/disable grease quic bit (default = enable). <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label280' href="javascript:ContentClick('label281', 'label280');" onmouseover="ContentPreview('label281');" onmouseout="ContentUnpreview('label281');" title="click to collapse or expand..."> more... </a>
 <div id="label281" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_ack_delay</span> <b>(Alias name: max-ack-delay)</b>  Maximum ack delay in milliseconds (1 - 16383, default = 25). <span class="li-normal">type: int</span>
 <a id='label282' href="javascript:ContentClick('label283', 'label282');" onmouseover="ContentPreview('label283');" onmouseout="ContentUnpreview('label283');" title="click to collapse or expand..."> more... </a>
 <div id="label283" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_datagram_frame_size</span> <b>(Alias name: max-datagram-frame-size)</b>  Maximum datagram frame size in bytes (1 - 1500, default = 1500). <span class="li-normal">type: int</span>
 <a id='label284' href="javascript:ContentClick('label285', 'label284');" onmouseover="ContentPreview('label285');" onmouseout="ContentUnpreview('label285');" title="click to collapse or expand..."> more... </a>
 <div id="label285" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_idle_timeout</span> <b>(Alias name: max-idle-timeout)</b>  Maximum idle timeout milliseconds (1 - 60000, default = 30000). <span class="li-normal">type: int</span>
 <a id='label286' href="javascript:ContentClick('label287', 'label286');" onmouseover="ContentPreview('label287');" onmouseout="ContentUnpreview('label287');" title="click to collapse or expand..."> more... </a>
 <div id="label287" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">max_udp_payload_size</span> <b>(Alias name: max-udp-payload-size)</b>  Maximum udp payload size in bytes (1200 - 1500, default = 1500). <span class="li-normal">type: int</span>
 <a id='label288' href="javascript:ContentClick('label289', 'label288');" onmouseover="ContentPreview('label289');" onmouseout="ContentUnpreview('label289');" title="click to collapse or expand..."> more... </a>
 <div id="label289" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
 </div>
 </li>
 </ul>
 </li>
 </ul>
 </li>
 <li><span class="li-head">auth_portal</span> <b>(Alias name: auth-portal)</b>  Enable/disable authentication portal. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label290' href="javascript:ContentClick('label291', 'label290');" onmouseover="ContentPreview('label291');" onmouseout="ContentUnpreview('label291');" title="click to collapse or expand..."> more... </a>
 <div id="label291" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">auth_virtual_host</span> <b>(Alias name: auth-virtual-host)</b>  Virtual host for authentication portal. <span class="li-normal">type: str</span>
 <a id='label292' href="javascript:ContentClick('label293', 'label292');" onmouseover="ContentPreview('label293');" onmouseout="ContentUnpreview('label293');" title="click to collapse or expand..."> more... </a>
 <div id="label293" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.3 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">decrypted_traffic_mirror</span> <b>(Alias name: decrypted-traffic-mirror)</b>  Decrypted traffic mirror. <span class="li-normal">type: str</span>
 <a id='label294' href="javascript:ContentClick('label295', 'label294');" onmouseover="ContentPreview('label295');" onmouseout="ContentUnpreview('label295');" title="click to collapse or expand..."> more... </a>
 <div id="label295" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">log_blocked_traffic</span> <b>(Alias name: log-blocked-traffic)</b>  Enable/disable logging of blocked traffic. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label296' href="javascript:ContentClick('label297', 'label296');" onmouseover="ContentPreview('label297');" onmouseout="ContentUnpreview('label297');" title="click to collapse or expand..."> more... </a>
 <div id="label297" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.0.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">add_vhost_domain_to_dnsdb</span> <b>(Alias name: add-vhost-domain-to-dnsdb)</b>  Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label298' href="javascript:ContentClick('label299', 'label298');" onmouseover="ContentPreview('label299');" onmouseout="ContentUnpreview('label299');" title="click to collapse or expand..."> more... </a>
 <div id="label299" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">user_agent_detect</span> <b>(Alias name: user-agent-detect)</b>  Enable/disable to detect device type by http user-agent if no client certificate provided. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label300' href="javascript:ContentClick('label301', 'label300');" onmouseover="ContentPreview('label301');" onmouseout="ContentUnpreview('label301');" title="click to collapse or expand..."> more... </a>
 <div id="label301" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.1 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">http_supported_max_version</span> <b>(Alias name: http-supported-max-version)</b>  Maximum supported http versions. <span class="li-normal">type: str</span> <span class="li-normal">choices: [http1, http2]</span> 
 <a id='label302' href="javascript:ContentClick('label303', 'label302');" onmouseover="ContentPreview('label303');" onmouseout="ContentUnpreview('label303');" title="click to collapse or expand..."> more... </a>
 <div id="label303" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">svr_pool_multiplex</span> <b>(Alias name: svr-pool-multiplex)</b>  Enable/disable server pool multiplexing. <span class="li-normal">type: str</span> <span class="li-normal">choices: [disable, enable]</span> 
 <a id='label304' href="javascript:ContentClick('label305', 'label304');" onmouseover="ContentPreview('label305');" onmouseout="ContentUnpreview('label305');" title="click to collapse or expand..."> more... </a>
 <div id="label305" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">svr_pool_server_max_request</span> <b>(Alias name: svr-pool-server-max-request)</b>  Maximum number of requests that servers in server pool handle before disconnecting (default = unlimited). <span class="li-normal">type: int</span>
 <a id='label306' href="javascript:ContentClick('label307', 'label306');" onmouseover="ContentPreview('label307');" onmouseout="ContentUnpreview('label307');" title="click to collapse or expand..."> more... </a>
 <div id="label307" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">svr_pool_ttl</span> <b>(Alias name: svr-pool-ttl)</b>  Time-to-live in the server pool for idle connections to servers. <span class="li-normal">type: int</span>
 <a id='label308' href="javascript:ContentClick('label309', 'label308');" onmouseover="ContentPreview('label309');" onmouseout="ContentUnpreview('label309');" title="click to collapse or expand..."> more... </a>
 <div id="label309" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.2.2 -> latest</code></p>
 </div>
 </li>
 <li><span class="li-head">svr_pool_server_max_concurrent_request</span> <b>(Alias name: svr-pool-server-max-concurrent-request)</b>  Maximum number of concurrent requests that servers in server pool could handle (default = unlimited). <span class="li-normal">type: int</span>
 <a id='label310' href="javascript:ContentClick('label311', 'label310');" onmouseover="ContentPreview('label311');" onmouseout="ContentUnpreview('label311');" title="click to collapse or expand..."> more... </a>
 <div id="label311" style="display:none">
 <p>Supported Version Ranges: <code class="docutils literal notranslate">v7.4.1 -> latest</code></p>
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
    vars:
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_httpapi_port: 443
    tasks:
      - name: Configure Access Proxy.
        fortinet.fortimanager.fmgr_firewall_accessproxy:
          # bypass_validation: false
          workspace_locking_adom: <value in [global, custom adom including root]>
          workspace_locking_timeout: 300
          # rc_succeeded: [0, -2, -3, ...]
          # rc_failed: [-2, -3, ...]
          adom: <your own value>
          state: present # <value in [present, absent]>
          firewall_accessproxy:
            api_gateway:
              -
                http_cookie_age: <integer>
                http_cookie_domain: <string>
                http_cookie_domain_from_host: <value in [disable, enable]>
                http_cookie_generation: <integer>
                http_cookie_path: <string>
                http_cookie_share: <value in [disable, same-ip]>
                https_cookie_secure: <value in [disable, enable]>
                id: <integer>
                ldb_method: <value in [static, round-robin, weighted, ...]>
                persistence: <value in [none, http-cookie]>
                realservers:
                  -
                    address: <string>
                    health_check: <value in [disable, enable]>
                    health_check_proto: <value in [ping, http, tcp-connect]>
                    http_host: <string>
                    id: <integer>
                    ip: <string>
                    mappedport: <list or string>
                    port: <integer>
                    status: <value in [active, standby, disable]>
                    weight: <integer>
                    addr_type: <value in [fqdn, ip]>
                    domain: <string>
                    holddown_interval: <value in [disable, enable]>
                    ssh_client_cert: <string>
                    ssh_host_key: <list or string>
                    ssh_host_key_validation: <value in [disable, enable]>
                    type: <value in [tcp-forwarding, ssh]>
                    translate_host: <value in [disable, enable]>
                    external_auth: <value in [disable, enable]>
                    tunnel_encryption: <value in [disable, enable]>
                saml_server: <string>
                service: <value in [http, https, tcp-forwarding, ...]>
                ssl_algorithm: <value in [high, medium, low, ...]>
                ssl_cipher_suites:
                  -
                    cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                    priority: <integer>
                    versions:
                      - "tls-1.0"
                      - "tls-1.1"
                      - "tls-1.2"
                      - "tls-1.3"
                ssl_dh_bits: <value in [768, 1024, 1536, ...]>
                ssl_max_version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
                ssl_min_version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
                url_map: <string>
                url_map_type: <value in [sub-string, wildcard, regex]>
                virtual_host: <string>
                saml_redirect: <value in [disable, enable]>
                ssl_vpn_web_portal: <string>
                application: <list or string>
                ssl_renegotiation: <value in [disable, enable]>
                h2_support: <value in [disable, enable]>
                h3_support: <value in [disable, enable]>
                quic:
                  ack_delay_exponent: <integer>
                  active_connection_id_limit: <integer>
                  active_migration: <value in [disable, enable]>
                  grease_quic_bit: <value in [disable, enable]>
                  max_ack_delay: <integer>
                  max_datagram_frame_size: <integer>
                  max_idle_timeout: <integer>
                  max_udp_payload_size: <integer>
            client_cert: <value in [disable, enable]>
            empty_cert_action: <value in [block, accept, accept-unmanageable]>
            ldb_method: <value in [static, round-robin, weighted, ...]>
            name: <string>
            realservers:
              -
                id: <integer>
                ip: <string>
                port: <integer>
                status: <value in [active, standby, disable]>
                weight: <integer>
            server_pubkey_auth: <value in [disable, enable]>
            server_pubkey_auth_settings:
              auth_ca: <string>
              cert_extension:
                -
                  critical: <value in [no, yes]>
                  data: <string>
                  name: <string>
                  type: <value in [fixed, user]>
              permit_agent_forwarding: <value in [disable, enable]>
              permit_port_forwarding: <value in [disable, enable]>
              permit_pty: <value in [disable, enable]>
              permit_user_rc: <value in [disable, enable]>
              permit_x11_forwarding: <value in [disable, enable]>
              source_address: <value in [disable, enable]>
            vip: <string>
            api_gateway6:
              -
                http_cookie_age: <integer>
                http_cookie_domain: <string>
                http_cookie_domain_from_host: <value in [disable, enable]>
                http_cookie_generation: <integer>
                http_cookie_path: <string>
                http_cookie_share: <value in [disable, same-ip]>
                https_cookie_secure: <value in [disable, enable]>
                id: <integer>
                ldb_method: <value in [static, round-robin, weighted, ...]>
                persistence: <value in [none, http-cookie]>
                realservers:
                  -
                    addr_type: <value in [fqdn, ip]>
                    address: <string>
                    domain: <string>
                    health_check: <value in [disable, enable]>
                    health_check_proto: <value in [ping, http, tcp-connect]>
                    holddown_interval: <value in [disable, enable]>
                    http_host: <string>
                    id: <integer>
                    ip: <string>
                    mappedport: <list or string>
                    port: <integer>
                    ssh_client_cert: <string>
                    ssh_host_key: <list or string>
                    ssh_host_key_validation: <value in [disable, enable]>
                    status: <value in [active, standby, disable]>
                    type: <value in [tcp-forwarding, ssh]>
                    weight: <integer>
                    translate_host: <value in [disable, enable]>
                    external_auth: <value in [disable, enable]>
                    tunnel_encryption: <value in [disable, enable]>
                saml_redirect: <value in [disable, enable]>
                saml_server: <string>
                service: <value in [http, https, tcp-forwarding, ...]>
                ssl_algorithm: <value in [high, medium, low]>
                ssl_cipher_suites:
                  -
                    cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                    priority: <integer>
                    versions:
                      - "tls-1.0"
                      - "tls-1.1"
                      - "tls-1.2"
                      - "tls-1.3"
                ssl_dh_bits: <value in [768, 1024, 1536, ...]>
                ssl_max_version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
                ssl_min_version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
                ssl_vpn_web_portal: <string>
                url_map: <string>
                url_map_type: <value in [sub-string, wildcard, regex]>
                virtual_host: <string>
                application: <list or string>
                ssl_renegotiation: <value in [disable, enable]>
                h2_support: <value in [disable, enable]>
                h3_support: <value in [disable, enable]>
                quic:
                  ack_delay_exponent: <integer>
                  active_connection_id_limit: <integer>
                  active_migration: <value in [disable, enable]>
                  grease_quic_bit: <value in [disable, enable]>
                  max_ack_delay: <integer>
                  max_datagram_frame_size: <integer>
                  max_idle_timeout: <integer>
                  max_udp_payload_size: <integer>
            auth_portal: <value in [disable, enable]>
            auth_virtual_host: <string>
            decrypted_traffic_mirror: <string>
            log_blocked_traffic: <value in [disable, enable]>
            add_vhost_domain_to_dnsdb: <value in [disable, enable]>
            user_agent_detect: <value in [disable, enable]>
            http_supported_max_version: <value in [http1, http2]>
            svr_pool_multiplex: <value in [disable, enable]>
            svr_pool_server_max_request: <integer>
            svr_pool_ttl: <integer>
            svr_pool_server_max_concurrent_request: <integer>


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
