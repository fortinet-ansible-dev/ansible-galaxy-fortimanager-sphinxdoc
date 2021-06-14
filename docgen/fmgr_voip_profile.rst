:source: fmgr_voip_profile.py

:orphan:

.. _fmgr_voip_profile:

fmgr_voip_profile -- Configure VoIP profiles.
+++++++++++++++++++++++++++++++++++++++++++++

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
 <td>voip_profile</td>
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
 <li><span class="li-head">voip_profile</span> - Configure VoIP profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">feature-set</span> - Flow or proxy inspection feature set. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [flow, proxy]</span> </li>
 <li><span class="li-head">sccp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">block-mcast</span> - Enable/disable block multicast RTP connections. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-call-summary</span> - Enable/disable log summary of SCCP calls. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-violations</span> - Enable/disable logging of SCCP violations. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-calls</span> - Maximum calls per minute per SCCP client (max 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SCCP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">verify-header</span> - Enable/disable verify SCCP header content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">sip</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">ack-rate</span> - ACK request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ack-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">block-ack</span> - Enable/disable block ACK requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-bye</span> - Enable/disable block BYE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-cancel</span> - Enable/disable block CANCEL requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-geo-red-options</span> - Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-info</span> - Enable/disable block INFO requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-invite</span> - Enable/disable block INVITE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-long-lines</span> - Enable/disable block requests with headers exceeding max-line-length. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-message</span> - Enable/disable block MESSAGE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-notify</span> - Enable/disable block NOTIFY requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-options</span> - Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-prack</span> - Enable/disable block prack requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-publish</span> - Enable/disable block PUBLISH requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-refer</span> - Enable/disable block REFER requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-register</span> - Enable/disable block REGISTER requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-subscribe</span> - Enable/disable block SUBSCRIBE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-unknown</span> - Block unrecognized SIP requests (enabled by default). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-update</span> - Enable/disable block UPDATE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bye-rate</span> - BYE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bye-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">call-keepalive</span> - Continue tracking calls with no RTP for this many minutes. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">cancel-rate</span> - CANCEL request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">cancel-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">contact-fixup</span> - Fixup contact anyway even if contacts IP:port doesnt match sessions IP:port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hnt-restrict-source-ip</span> - Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hosted-nat-traversal</span> - Hosted NAT Traversal (HNT). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">info-rate</span> - INFO request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">info-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">invite-rate</span> - INVITE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">invite-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">ips-rtp</span> - Enable/disable allow IPS on RTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-call-summary</span> - Enable/disable logging of SIP call summary. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-violations</span> - Enable/disable logging of SIP violations. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">malformed-header-allow</span> - Action for malformed Allow header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-call-id</span> - Action for malformed Call-ID header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-contact</span> - Action for malformed Contact header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-content-length</span> - Action for malformed Content-Length header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-content-type</span> - Action for malformed Content-Type header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-cseq</span> - Action for malformed CSeq header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-expires</span> - Action for malformed Expires header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-from</span> - Action for malformed From header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-max-forwards</span> - Action for malformed Max-Forwards header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-no-proxy-require</span> - Action for malformed SIP messages without Proxy-Require header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-no-require</span> - Action for malformed SIP messages without Require header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-p-asserted-identity</span> - Action for malformed P-Asserted-Identity header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-rack</span> - Action for malformed RAck header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-record-route</span> - Action for malformed Record-Route header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-route</span> - Action for malformed Route header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-rseq</span> - Action for malformed RSeq header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-a</span> - Action for malformed SDP a line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-b</span> - Action for malformed SDP b line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-c</span> - Action for malformed SDP c line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-i</span> - Action for malformed SDP i line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-k</span> - Action for malformed SDP k line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-m</span> - Action for malformed SDP m line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-o</span> - Action for malformed SDP o line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-r</span> - Action for malformed SDP r line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-s</span> - Action for malformed SDP s line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-t</span> - Action for malformed SDP t line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-v</span> - Action for malformed SDP v line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-z</span> - Action for malformed SDP z line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-to</span> - Action for malformed To header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-via</span> - Action for malformed VIA header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-request-line</span> - Action for malformed request line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">max-body-length</span> - Maximum SIP message body length (0 meaning no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-dialogs</span> - Maximum number of concurrent calls/dialogs (per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-idle-dialogs</span> - Maximum number established but idle dialogs to retain (per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-line-length</span> - Maximum SIP header line length (78-4096). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">message-rate</span> - MESSAGE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">message-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">nat-port-range</span> - RTP NAT port range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat-trace</span> - Enable/disable preservation of original IP in SDP i line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">no-sdp-fixup</span> - Enable/disable no SDP fix-up. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">notify-rate</span> - NOTIFY request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">notify-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">open-contact-pinhole</span> - Enable/disable open pinhole for non-REGISTER Contact port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">open-record-route-pinhole</span> - Enable/disable open pinhole for Record-Route port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">open-register-pinhole</span> - Enable/disable open pinhole for REGISTER Contact port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">open-via-pinhole</span> - Enable/disable open pinhole for Via port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options-rate</span> - OPTIONS request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">options-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">prack-rate</span> - PRACK request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">prack-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">preserve-override</span> - Override i line to preserve original IPS (default: append). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">provisional-invite-expiry-time</span> - Expiry time (10-3600, in seconds) for provisional INVITE. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">publish-rate</span> - PUBLISH request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">publish-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">refer-rate</span> - REFER request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">refer-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">register-contact-trace</span> - Enable/disable trace original IP/port within the contact header of REGISTER requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">register-rate</span> - REGISTER request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">register-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">rfc2543-branch</span> - Enable/disable support via branch compliant with RFC 2543. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rtp</span> - Enable/disable create pinholes for RTP traffic to traverse firewall. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-algorithm</span> - Relative strength of encryption algorithms accepted in negotiation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, medium, low]</span> </li>
 <li><span class="li-head">ssl-auth-client</span> - Require a client certificate and authenticate it with the peer/peergrp. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-auth-server</span> - Authenticate the servers certificate with the peer/peergrp. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-client-certificate</span> - Name of Certificate to offer to server if requested. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-client-renegotiation</span> - Allow/block client renegotiation by server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny, secure]</span> </li>
 <li><span class="li-head">ssl-max-version</span> - Highest SSL/TLS version to negotiate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> </li>
 <li><span class="li-head">ssl-min-version</span> - Lowest SSL/TLS version to negotiate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, tls-1.3]</span> </li>
 <li><span class="li-head">ssl-mode</span> - SSL/TLS mode for encryption & decryption of traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [off, full]</span> </li>
 <li><span class="li-head">ssl-pfs</span> - SSL Perfect Forward Secrecy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [require, deny, allow]</span> </li>
 <li><span class="li-head">ssl-send-empty-frags</span> - Send empty fragments to avoid attack on CBC IV (SSL 3. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-server-certificate</span> - Name of Certificate return to the client in every SSL connection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SIP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">strict-register</span> - Enable/disable only allow the registrar to connect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">subscribe-rate</span> - SUBSCRIBE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">subscribe-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
 <li><span class="li-head">unknown-header</span> - Action for unknown SIP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">update-rate</span> - UPDATE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-rate-track</span> - Track the packet protocol field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, src-ip, dest-ip]</span> </li>
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
    - name: Configure VoIP profiles.
      fmgr_voip_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         voip_profile:
            comment: <value of string>
            name: <value of string>
            feature-set: <value in [flow, proxy]>
            sccp:
               block-mcast: <value in [disable, enable]>
               log-call-summary: <value in [disable, enable]>
               log-violations: <value in [disable, enable]>
               max-calls: <value of integer>
               status: <value in [disable, enable]>
               verify-header: <value in [disable, enable]>
            sip:
               ack-rate: <value of integer>
               ack-rate-track: <value in [none, src-ip, dest-ip]>
               block-ack: <value in [disable, enable]>
               block-bye: <value in [disable, enable]>
               block-cancel: <value in [disable, enable]>
               block-geo-red-options: <value in [disable, enable]>
               block-info: <value in [disable, enable]>
               block-invite: <value in [disable, enable]>
               block-long-lines: <value in [disable, enable]>
               block-message: <value in [disable, enable]>
               block-notify: <value in [disable, enable]>
               block-options: <value in [disable, enable]>
               block-prack: <value in [disable, enable]>
               block-publish: <value in [disable, enable]>
               block-refer: <value in [disable, enable]>
               block-register: <value in [disable, enable]>
               block-subscribe: <value in [disable, enable]>
               block-unknown: <value in [disable, enable]>
               block-update: <value in [disable, enable]>
               bye-rate: <value of integer>
               bye-rate-track: <value in [none, src-ip, dest-ip]>
               call-keepalive: <value of integer>
               cancel-rate: <value of integer>
               cancel-rate-track: <value in [none, src-ip, dest-ip]>
               contact-fixup: <value in [disable, enable]>
               hnt-restrict-source-ip: <value in [disable, enable]>
               hosted-nat-traversal: <value in [disable, enable]>
               info-rate: <value of integer>
               info-rate-track: <value in [none, src-ip, dest-ip]>
               invite-rate: <value of integer>
               invite-rate-track: <value in [none, src-ip, dest-ip]>
               ips-rtp: <value in [disable, enable]>
               log-call-summary: <value in [disable, enable]>
               log-violations: <value in [disable, enable]>
               malformed-header-allow: <value in [pass, discard, respond]>
               malformed-header-call-id: <value in [pass, discard, respond]>
               malformed-header-contact: <value in [pass, discard, respond]>
               malformed-header-content-length: <value in [pass, discard, respond]>
               malformed-header-content-type: <value in [pass, discard, respond]>
               malformed-header-cseq: <value in [pass, discard, respond]>
               malformed-header-expires: <value in [pass, discard, respond]>
               malformed-header-from: <value in [pass, discard, respond]>
               malformed-header-max-forwards: <value in [pass, discard, respond]>
               malformed-header-no-proxy-require: <value in [pass, discard, respond]>
               malformed-header-no-require: <value in [pass, discard, respond]>
               malformed-header-p-asserted-identity: <value in [pass, discard, respond]>
               malformed-header-rack: <value in [pass, discard, respond]>
               malformed-header-record-route: <value in [pass, discard, respond]>
               malformed-header-route: <value in [pass, discard, respond]>
               malformed-header-rseq: <value in [pass, discard, respond]>
               malformed-header-sdp-a: <value in [pass, discard, respond]>
               malformed-header-sdp-b: <value in [pass, discard, respond]>
               malformed-header-sdp-c: <value in [pass, discard, respond]>
               malformed-header-sdp-i: <value in [pass, discard, respond]>
               malformed-header-sdp-k: <value in [pass, discard, respond]>
               malformed-header-sdp-m: <value in [pass, discard, respond]>
               malformed-header-sdp-o: <value in [pass, discard, respond]>
               malformed-header-sdp-r: <value in [pass, discard, respond]>
               malformed-header-sdp-s: <value in [pass, discard, respond]>
               malformed-header-sdp-t: <value in [pass, discard, respond]>
               malformed-header-sdp-v: <value in [pass, discard, respond]>
               malformed-header-sdp-z: <value in [pass, discard, respond]>
               malformed-header-to: <value in [pass, discard, respond]>
               malformed-header-via: <value in [pass, discard, respond]>
               malformed-request-line: <value in [pass, discard, respond]>
               max-body-length: <value of integer>
               max-dialogs: <value of integer>
               max-idle-dialogs: <value of integer>
               max-line-length: <value of integer>
               message-rate: <value of integer>
               message-rate-track: <value in [none, src-ip, dest-ip]>
               nat-port-range: <value of string>
               nat-trace: <value in [disable, enable]>
               no-sdp-fixup: <value in [disable, enable]>
               notify-rate: <value of integer>
               notify-rate-track: <value in [none, src-ip, dest-ip]>
               open-contact-pinhole: <value in [disable, enable]>
               open-record-route-pinhole: <value in [disable, enable]>
               open-register-pinhole: <value in [disable, enable]>
               open-via-pinhole: <value in [disable, enable]>
               options-rate: <value of integer>
               options-rate-track: <value in [none, src-ip, dest-ip]>
               prack-rate: <value of integer>
               prack-rate-track: <value in [none, src-ip, dest-ip]>
               preserve-override: <value in [disable, enable]>
               provisional-invite-expiry-time: <value of integer>
               publish-rate: <value of integer>
               publish-rate-track: <value in [none, src-ip, dest-ip]>
               refer-rate: <value of integer>
               refer-rate-track: <value in [none, src-ip, dest-ip]>
               register-contact-trace: <value in [disable, enable]>
               register-rate: <value of integer>
               register-rate-track: <value in [none, src-ip, dest-ip]>
               rfc2543-branch: <value in [disable, enable]>
               rtp: <value in [disable, enable]>
               ssl-algorithm: <value in [high, medium, low]>
               ssl-auth-client: <value of string>
               ssl-auth-server: <value of string>
               ssl-client-certificate: <value of string>
               ssl-client-renegotiation: <value in [allow, deny, secure]>
               ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
               ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
               ssl-mode: <value in [off, full]>
               ssl-pfs: <value in [require, deny, allow]>
               ssl-send-empty-frags: <value in [disable, enable]>
               ssl-server-certificate: <value of string>
               status: <value in [disable, enable]>
               strict-register: <value in [disable, enable]>
               subscribe-rate: <value of integer>
               subscribe-rate-track: <value in [none, src-ip, dest-ip]>
               unknown-header: <value in [pass, discard, respond]>
               update-rate: <value of integer>
               update-rate-track: <value in [none, src-ip, dest-ip]>



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



