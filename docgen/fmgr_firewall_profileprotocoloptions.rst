:source: fmgr_firewall_profileprotocoloptions.py

:orphan:

.. _fmgr_firewall_profileprotocoloptions:

fmgr_firewall_profileprotocoloptions -- Configure protocol options.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>firewall_profileprotocoloptions</td>
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
 <li><span class="li-head">firewall_profileprotocoloptions</span> - Configure protocol options. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oversize-log</span> - Enable/disable logging for antivirus oversize file blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Name of the replacement message group to be used <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rpc-over-http</span> - Enable/disable inspection of RPC over HTTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switching-protocols-log</span> - Enable/disable logging for HTTP/HTTPS switching protocols. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">feature-set</span> - Flow/proxy feature set. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">cifs</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">domain-controller</span> - Domain for which to decrypt CIFS traffic. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [oversize]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">server-credential-type</span> - CIFS server credential type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, credential-replication, credential-keytab]</span> </li>
 <li><span class="li-head">server-keytab</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">keytab</span> - Base64 encoded keytab file containing credential of the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: str</span></li>
 <li><span class="li-head">principal</span> - Service principal. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tcp-window-maximum</span> - Maximum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-minimum</span> - Minimum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-size</span> - Set TCP static window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-type</span> - TCP window type to use for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [system, static, dynamic]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">dns</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">ftp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">comfort-amount</span> - Amount of data to send in a transmission for client comforting (1 - 65535 bytes, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comfort-interval</span> - Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [clientcomfort, no-content-summary, oversize, splice, bypass-rest-command, bypass-mode-command]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-offloaded</span> - SSL decryption and encryption performed by an external device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">stream-based-uncompressed-limit</span> - Maximum stream-based uncompressed data size that will be scanned (MB, 0 = unlimited (default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-maximum</span> - Maximum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-minimum</span> - Minimum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-size</span> - Set TCP static window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-type</span> - TCP window type to use for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [system, static, dynamic]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">http</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">block-page-status-code</span> - Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comfort-amount</span> - Amount of data to send in a transmission for client comforting (1 - 65535 bytes, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comfort-interval</span> - Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [oversize, chunkedbypass, clientcomfort, no-content-summary, servercomfort]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">post-lang</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [jisx0201, jisx0208, jisx0212, gb2312, ksc5601-ex, euc-jp, sjis, iso2022-jp, iso2022-jp-1, iso2022-jp-2, euc-cn, ces-gbk, hz, ces-big5, euc-kr, iso2022-jp-3, iso8859-1, tis620, cp874, cp1252, cp1251]</span> </li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">range-block</span> - Enable/disable blocking of partial downloads. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">retry-count</span> - Number of attempts to retry HTTP connection (0 - 100, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-offloaded</span> - SSL decryption and encryption performed by an external device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">stream-based-uncompressed-limit</span> - Maximum stream-based uncompressed data size that will be scanned (MB, 0 = unlimited (default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">streaming-content-bypass</span> - Enable/disable bypassing of streaming content from buffering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">strip-x-forwarded-for</span> - Enable/disable stripping of HTTP X-Forwarded-For header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switching-protocols</span> - Bypass from scanning, or block a connection that attempts to switch protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, block]</span> </li>
 <li><span class="li-head">tcp-window-maximum</span> - Maximum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-minimum</span> - Minimum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-size</span> - Set TCP static window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-type</span> - TCP window type to use for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [system, static, dynamic]</span> </li>
 <li><span class="li-head">tunnel-non-http</span> - Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">unknown-http-version</span> - How to handle HTTP sessions that do not comply with HTTP 0. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [best-effort, reject, tunnel]</span> </li>
 </ul>
 <li><span class="li-head">imap</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [oversize, fragmail, no-content-summary]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-offloaded</span> - SSL decryption and encryption performed by an external device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">mail-signature</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">signature</span> - Email signature to be added to outgoing email (if the signature contains spaces, enclose with quotation marks). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable adding an email signature to SMTP email messages as they pass through the FortiGate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">mapi</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [fragmail, oversize, no-content-summary]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">nntp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [oversize, no-content-summary, splice]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">pop3</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [oversize, fragmail, no-content-summary]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-offloaded</span> - SSL decryption and encryption performed by an external device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">smtp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [oversize, fragmail, no-content-summary, splice]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: int</span></li>
 <li><span class="li-head">proxy-after-tcp-handshake</span> - Proxy traffic after the TCP 3-way handshake has been established (not before). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">server-busy</span> - Enable/disable SMTP server busy when server not available. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-offloaded</span> - SSL decryption and encryption performed by an external device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">ssh</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">comfort-amount</span> - Amount of data to send in a transmission for client comforting (1 - 65535 bytes, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comfort-interval</span> - Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [oversize, clientcomfort, servercomfort]</span> </li>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-offloaded</span> - SSL decryption and encryption performed by an external device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes]</span> </li>
 <li><span class="li-head">stream-based-uncompressed-limit</span> - Maximum stream-based uncompressed data size that will be scanned (MB, 0 = unlimited (default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-maximum</span> - Maximum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-minimum</span> - Minimum dynamic TCP window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-size</span> - Set TCP static window size. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-window-type</span> - TCP window type to use for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [system, static, dynamic]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
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
    - name: Configure protocol options.
      fmgr_firewall_profileprotocoloptions:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         firewall_profileprotocoloptions:
            comment: <value of string>
            name: <value of string>
            oversize-log: <value in [disable, enable]>
            replacemsg-group: <value of string>
            rpc-over-http: <value in [disable, enable]>
            switching-protocols-log: <value in [disable, enable]>
            feature-set: <value in [proxy, flow]>
            cifs:
               domain-controller: <value of string>
               options:
                 - oversize
               oversize-limit: <value of integer>
               ports: <value of integer>
               scan-bzip2: <value in [disable, enable]>
               server-credential-type: <value in [none, credential-replication, credential-keytab]>
               server-keytab:
                 -
                     keytab: <value of string>
                     password: <value of string>
                     principal: <value of string>
               status: <value in [disable, enable]>
               tcp-window-maximum: <value of integer>
               tcp-window-minimum: <value of integer>
               tcp-window-size: <value of integer>
               tcp-window-type: <value in [system, static, dynamic]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
            dns:
               ports: <value of integer>
               status: <value in [disable, enable]>
            ftp:
               comfort-amount: <value of integer>
               comfort-interval: <value of integer>
               inspect-all: <value in [disable, enable]>
               options:
                 - clientcomfort
                 - no-content-summary
                 - oversize
                 - splice
                 - bypass-rest-command
                 - bypass-mode-command
               oversize-limit: <value of integer>
               ports: <value of integer>
               scan-bzip2: <value in [disable, enable]>
               ssl-offloaded: <value in [no, yes]>
               status: <value in [disable, enable]>
               stream-based-uncompressed-limit: <value of integer>
               tcp-window-maximum: <value of integer>
               tcp-window-minimum: <value of integer>
               tcp-window-size: <value of integer>
               tcp-window-type: <value in [system, static, dynamic]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
            http:
               block-page-status-code: <value of integer>
               comfort-amount: <value of integer>
               comfort-interval: <value of integer>
               inspect-all: <value in [disable, enable]>
               options:
                 - oversize
                 - chunkedbypass
                 - clientcomfort
                 - no-content-summary
                 - servercomfort
               oversize-limit: <value of integer>
               ports: <value of integer>
               post-lang:
                 - jisx0201
                 - jisx0208
                 - jisx0212
                 - gb2312
                 - ksc5601-ex
                 - euc-jp
                 - sjis
                 - iso2022-jp
                 - iso2022-jp-1
                 - iso2022-jp-2
                 - euc-cn
                 - ces-gbk
                 - hz
                 - ces-big5
                 - euc-kr
                 - iso2022-jp-3
                 - iso8859-1
                 - tis620
                 - cp874
                 - cp1252
                 - cp1251
               proxy-after-tcp-handshake: <value in [disable, enable]>
               range-block: <value in [disable, enable]>
               retry-count: <value of integer>
               scan-bzip2: <value in [disable, enable]>
               ssl-offloaded: <value in [no, yes]>
               status: <value in [disable, enable]>
               stream-based-uncompressed-limit: <value of integer>
               streaming-content-bypass: <value in [disable, enable]>
               strip-x-forwarded-for: <value in [disable, enable]>
               switching-protocols: <value in [bypass, block]>
               tcp-window-maximum: <value of integer>
               tcp-window-minimum: <value of integer>
               tcp-window-size: <value of integer>
               tcp-window-type: <value in [system, static, dynamic]>
               tunnel-non-http: <value in [disable, enable]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
               unknown-http-version: <value in [best-effort, reject, tunnel]>
            imap:
               inspect-all: <value in [disable, enable]>
               options:
                 - oversize
                 - fragmail
                 - no-content-summary
               oversize-limit: <value of integer>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               scan-bzip2: <value in [disable, enable]>
               ssl-offloaded: <value in [no, yes]>
               status: <value in [disable, enable]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
            mail-signature:
               signature: <value of string>
               status: <value in [disable, enable]>
            mapi:
               options:
                 - fragmail
                 - oversize
                 - no-content-summary
               oversize-limit: <value of integer>
               ports: <value of integer>
               scan-bzip2: <value in [disable, enable]>
               status: <value in [disable, enable]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
            nntp:
               inspect-all: <value in [disable, enable]>
               options:
                 - oversize
                 - no-content-summary
                 - splice
               oversize-limit: <value of integer>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               scan-bzip2: <value in [disable, enable]>
               status: <value in [disable, enable]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
            pop3:
               inspect-all: <value in [disable, enable]>
               options:
                 - oversize
                 - fragmail
                 - no-content-summary
               oversize-limit: <value of integer>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               scan-bzip2: <value in [disable, enable]>
               ssl-offloaded: <value in [no, yes]>
               status: <value in [disable, enable]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
            smtp:
               inspect-all: <value in [disable, enable]>
               options:
                 - oversize
                 - fragmail
                 - no-content-summary
                 - splice
               oversize-limit: <value of integer>
               ports: <value of integer>
               proxy-after-tcp-handshake: <value in [disable, enable]>
               scan-bzip2: <value in [disable, enable]>
               server-busy: <value in [disable, enable]>
               ssl-offloaded: <value in [no, yes]>
               status: <value in [disable, enable]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>
            ssh:
               comfort-amount: <value of integer>
               comfort-interval: <value of integer>
               options:
                 - oversize
                 - clientcomfort
                 - servercomfort
               oversize-limit: <value of integer>
               scan-bzip2: <value in [disable, enable]>
               ssl-offloaded: <value in [no, yes]>
               stream-based-uncompressed-limit: <value of integer>
               tcp-window-maximum: <value of integer>
               tcp-window-minimum: <value of integer>
               tcp-window-size: <value of integer>
               tcp-window-type: <value in [system, static, dynamic]>
               uncompressed-nest-limit: <value of integer>
               uncompressed-oversize-limit: <value of integer>



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



