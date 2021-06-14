:source: fmgr_webfilter_profile.py

:orphan:

.. _fmgr_webfilter_profile:

fmgr_webfilter_profile -- Configure Web filter profiles.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>webfilter_profile</td>
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
 <li><span class="li-head">webfilter_profile</span> - Configure Web filter profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging for web filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">https-replacemsg</span> - Enable replacement messages for HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">inspection-mode</span> - Web filtering inspection mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow-based, dns]</span> </li>
 <li><span class="li-head">log-all-url</span> - Enable/disable logging all URLs visited. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, block-invalid-url, jscript, js, vbs, unknown, wf-referer, https-scan, intrinsic, wf-cookie, per-user-bwl, activexfilter, cookiefilter, https-url-scan, javafilter, rangeblock, contenttype-check, per-user-bal]</span> </li>
 <li><span class="li-head">ovrd-perm</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [bannedword-override, urlfilter-override, fortiguard-wf-override, contenttype-check-override]</span> </li>
 <li><span class="li-head">post-action</span> - Action taken for HTTP POST traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [normal, comfort, block]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">web-content-log</span> - Enable/disable logging logging blocked web content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-extended-all-action-log</span> - Enable/disable extended any filter action logging for web filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-activex-log</span> - Enable/disable logging ActiveX. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-applet-log</span> - Enable/disable logging Java applets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-command-block-log</span> - Enable/disable logging blocked commands. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-cookie-log</span> - Enable/disable logging cookie filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-cookie-removal-log</span> - Enable/disable logging blocked cookies. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-js-log</span> - Enable/disable logging Java scripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-jscript-log</span> - Enable/disable logging JScripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-referer-log</span> - Enable/disable logging referrers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-unknown-log</span> - Enable/disable logging unknown scripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-filter-vbs-log</span> - Enable/disable logging VBS scripts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-ftgd-err-log</span> - Enable/disable logging rating errors. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-ftgd-quota-usage</span> - Enable/disable logging daily quota usage. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-invalid-domain-log</span> - Enable/disable logging invalid domain names. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-url-log</span> - Enable/disable logging URL filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wisp</span> - Enable/disable web proxy WISP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wisp-algorithm</span> - WISP server selection algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto-learning, primary-secondary, round-robin]</span> </li>
 <li><span class="li-head">wisp-servers</span> - WISP servers. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">youtube-channel-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">channel-id</span> - YouTube channel ID to be filtered. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">youtube-channel-status</span> - YouTube channel filter status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, blacklist, whitelist]</span> </li>
 <li><span class="li-head">feature-set</span> - Flow/proxy feature set. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">web-antiphishing-log</span> - Enable/disable logging of AntiPhishing checks. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">antiphish</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">authentication</span> - Authentication methods. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [domain-controller, ldap]</span> </li>
 <li><span class="li-head">check-basic-auth</span> - Enable/disable checking of HTTP Basic Auth field for known credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">check-uri</span> - Enable/disable checking of GET URI parameters for known credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">check-username-only</span> - Enable/disable username only matching of credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">custom-patterns</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Category that the pattern matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [username, password]</span> </li>
 <li><span class="li-head">pattern</span> - Target pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Pattern will be treated either as a regex pattern or literal string. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regex, literal]</span> </li>
 </ul>
 <li><span class="li-head">default-action</span> - Action to be taken when there is no matching rule. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, block, exempt]</span> </li>
 <li><span class="li-head">domain-controller</span> - Domain for which to verify received credentials against. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">inspection-entries</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to be taken upon an AntiPhishing match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, block, exempt]</span> </li>
 <li><span class="li-head">fortiguard-category</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">name</span> - Inspection target name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ldap</span> - LDAP server for which to verify received credentials against. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-body-len</span> - Maximum size of a POST body to check for credentials. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Toggle AntiPhishing functionality. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">ftgd-wf</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">exempt-quota</span> - Do not stop quota for these categories. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filters</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take for matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, monitor, warning, authenticate]</span> </li>
 <li><span class="li-head">auth-usr-grp</span> - Groups with permission to authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">category</span> - Categories and groups the filter examines. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">override-replacemsg</span> - Override replacement message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">warn-duration</span> - Duration of warnings. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">warning-duration-type</span> - Re-display warning after closing browser or after a timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session, timeout]</span> </li>
 <li><span class="li-head">warning-prompt</span> - Warning prompts in each category or each domain. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [per-domain, per-category]</span> </li>
 </ul>
 <li><span class="li-head">max-quota-timeout</span> - Maximum FortiGuard quota used by single page view in seconds (excludes streams). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [error-allow, http-err-detail, rate-image-urls, strict-blocking, rate-server-ip, redir-block, connect-request-bypass, log-all-url, ftgd-disable]</span> </li>
 <li><span class="li-head">ovrd</span> - Allow web filter profile overrides. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quota</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - FortiGuard categories to apply quota to (category action must be set to monitor). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">duration</span> - Duration of quota. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">override-replacemsg</span> - Override replacement message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Quota type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [time, traffic]</span> </li>
 <li><span class="li-head">unit</span> - Traffic quota unit of measurement. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [B, KB, MB, GB]</span> </li>
 <li><span class="li-head">value</span> - Traffic quota value. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">rate-crl-urls</span> - Enable/disable rating CRL by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-css-urls</span> - Enable/disable rating CSS by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-javascript-urls</span> - Enable/disable rating JavaScript by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">override</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">ovrd-cookie</span> - Allow/deny browser-based (cookie) overrides. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">ovrd-dur</span> - Override duration. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ovrd-dur-mode</span> - Override duration mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [constant, ask]</span> </li>
 <li><span class="li-head">ovrd-scope</span> - Override scope. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [user, user-group, ip, ask, browser]</span> </li>
 <li><span class="li-head">ovrd-user-group</span> - User groups with permission to use the override. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile</span> - Web filter profile with permission to create overrides. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-attribute</span> - Profile attribute to retrieve from the RADIUS server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">profile-type</span> - Override profile type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [list, radius]</span> </li>
 </ul>
 <li><span class="li-head">url-extraction</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">redirect-header</span> - HTTP header name to use for client redirect on blocked requests <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">redirect-no-content</span> - Enable / Disable empty message-body entity in HTTP response <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">redirect-url</span> - HTTP header value to use for client redirect on blocked requests <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-fqdn</span> - URL extraction server FQDN (fully qualified domain name) <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable URL Extraction <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">web</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">allowlist</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [exempt-av, exempt-webcontent, exempt-activex-java-cookie, exempt-dlp, exempt-rangeblock, extended-log-others]</span> </li>
 <li><span class="li-head">blocklist</span> - Enable/disable automatic addition of URLs detected by FortiSandbox to blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bword-table</span> - Banned word table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">bword-threshold</span> - Banned word score threshold. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">content-header-list</span> - Content header list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">keyword-match</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">log-search</span> - Enable/disable logging all search phrases. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">safe-search</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [google, yahoo, bing, url, header]</span> </li>
 <li><span class="li-head">urlfilter-table</span> - URL filter table ID. <span class="li-normal">type: str</span> </li>
 </ul>
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
    - name: Configure Web filter profiles.
      fmgr_webfilter_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         webfilter_profile:
            comment: <value of string>
            extended-log: <value in [disable, enable]>
            https-replacemsg: <value in [disable, enable]>
            inspection-mode: <value in [proxy, flow-based, dns]>
            log-all-url: <value in [disable, enable]>
            name: <value of string>
            options:
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - block-invalid-url
              - jscript
              - js
              - vbs
              - unknown
              - wf-referer
              - https-scan
              - intrinsic
              - wf-cookie
              - per-user-bwl
              - activexfilter
              - cookiefilter
              - https-url-scan
              - javafilter
              - rangeblock
              - contenttype-check
              - per-user-bal
            ovrd-perm:
              - bannedword-override
              - urlfilter-override
              - fortiguard-wf-override
              - contenttype-check-override
            post-action: <value in [normal, comfort, block]>
            replacemsg-group: <value of string>
            web-content-log: <value in [disable, enable]>
            web-extended-all-action-log: <value in [disable, enable]>
            web-filter-activex-log: <value in [disable, enable]>
            web-filter-applet-log: <value in [disable, enable]>
            web-filter-command-block-log: <value in [disable, enable]>
            web-filter-cookie-log: <value in [disable, enable]>
            web-filter-cookie-removal-log: <value in [disable, enable]>
            web-filter-js-log: <value in [disable, enable]>
            web-filter-jscript-log: <value in [disable, enable]>
            web-filter-referer-log: <value in [disable, enable]>
            web-filter-unknown-log: <value in [disable, enable]>
            web-filter-vbs-log: <value in [disable, enable]>
            web-ftgd-err-log: <value in [disable, enable]>
            web-ftgd-quota-usage: <value in [disable, enable]>
            web-invalid-domain-log: <value in [disable, enable]>
            web-url-log: <value in [disable, enable]>
            wisp: <value in [disable, enable]>
            wisp-algorithm: <value in [auto-learning, primary-secondary, round-robin]>
            wisp-servers: <value of string>
            youtube-channel-filter:
              -
                  channel-id: <value of string>
                  comment: <value of string>
                  id: <value of integer>
            youtube-channel-status: <value in [disable, blacklist, whitelist]>
            feature-set: <value in [proxy, flow]>
            web-antiphishing-log: <value in [disable, enable]>
            antiphish:
               authentication: <value in [domain-controller, ldap]>
               check-basic-auth: <value in [disable, enable]>
               check-uri: <value in [disable, enable]>
               check-username-only: <value in [disable, enable]>
               custom-patterns:
                 -
                     category: <value in [username, password]>
                     pattern: <value of string>
                     type: <value in [regex, literal]>
               default-action: <value in [log, block, exempt]>
               domain-controller: <value of string>
               inspection-entries:
                 -
                     action: <value in [log, block, exempt]>
                     fortiguard-category: <value of string>
                     name: <value of string>
               ldap: <value of string>
               max-body-len: <value of integer>
               status: <value in [disable, enable]>
            ftgd-wf:
               exempt-quota: <value of string>
               filters:
                 -
                     action: <value in [block, monitor, warning, ...]>
                     auth-usr-grp: <value of string>
                     category: <value of string>
                     id: <value of integer>
                     log: <value in [disable, enable]>
                     override-replacemsg: <value of string>
                     warn-duration: <value of string>
                     warning-duration-type: <value in [session, timeout]>
                     warning-prompt: <value in [per-domain, per-category]>
               max-quota-timeout: <value of integer>
               options:
                 - error-allow
                 - http-err-detail
                 - rate-image-urls
                 - strict-blocking
                 - rate-server-ip
                 - redir-block
                 - connect-request-bypass
                 - log-all-url
                 - ftgd-disable
               ovrd: <value of string>
               quota:
                 -
                     category: <value of string>
                     duration: <value of string>
                     id: <value of integer>
                     override-replacemsg: <value of string>
                     type: <value in [time, traffic]>
                     unit: <value in [B, KB, MB, ...]>
                     value: <value of integer>
               rate-crl-urls: <value in [disable, enable]>
               rate-css-urls: <value in [disable, enable]>
               rate-javascript-urls: <value in [disable, enable]>
            override:
               ovrd-cookie: <value in [deny, allow]>
               ovrd-dur: <value of string>
               ovrd-dur-mode: <value in [constant, ask]>
               ovrd-scope: <value in [user, user-group, ip, ...]>
               ovrd-user-group: <value of string>
               profile: <value of string>
               profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
               profile-type: <value in [list, radius]>
            url-extraction:
               redirect-header: <value of string>
               redirect-no-content: <value in [disable, enable]>
               redirect-url: <value of string>
               server-fqdn: <value of string>
               status: <value in [disable, enable]>
            web:
               allowlist:
                 - exempt-av
                 - exempt-webcontent
                 - exempt-activex-java-cookie
                 - exempt-dlp
                 - exempt-rangeblock
                 - extended-log-others
               blocklist: <value in [disable, enable]>
               bword-table: <value of string>
               bword-threshold: <value of integer>
               content-header-list: <value of string>
               keyword-match: <value of string>
               log-search: <value in [disable, enable]>
               safe-search:
                 - google
                 - yahoo
                 - bing
                 - url
                 - header
               urlfilter-table: <value of string>



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



