:source: fmgr_system_replacemsggroup.py

:orphan:

.. _fmgr_system_replacemsggroup:

fmgr_system_replacemsggroup -- Configure replacement message groups.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>
 <li><span class="li-head">adom</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>
 <li><span class="li-head">system_replacemsggroup</span> - Configure replacement message groups. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">admin</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">alertmail</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">auth</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">custom-message</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">device-detection-portal</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ec</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">fortiguard-wf</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ftp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">group-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, utm, auth, ec, captive-portal]</span> </li>
 <li><span class="li-head">http</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">icap</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mail</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mm1</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">add-smil</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charset</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-ascii, utf-8]</span> </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [personal, advertisement, information, automatic, not-included]</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">from</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">from-sender</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">image</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, normal, high, not-included]</span> </li>
 <li><span class="li-head">rsp-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ok, err-unspecified, err-srv-denied, err-msg-fmt-corrupt, err-snd-addr-unresolv, err-msg-not-found, err-net-prob, err-content-not-accept, err-unsupp-msg]</span> </li>
 <li><span class="li-head">rsp-text</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sender-visibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hide, show, not-specified]</span> </li>
 <li><span class="li-head">smil-part</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subject</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mm3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">add-html</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charset</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-ascii, utf-8]</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">from</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">from-sender</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">html-part</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">image</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, normal, high, not-included]</span> </li>
 <li><span class="li-head">subject</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mm4</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">add-smil</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charset</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-ascii, utf-8]</span> </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [personal, advertisement, informational, auto, not-included]</span> </li>
 <li><span class="li-head">domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">from</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">from-sender</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">image</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, normal, high, not-included]</span> </li>
 <li><span class="li-head">rsp-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ok, err-unspecified, err-srv-denied, err-msg-fmt-corrupt, err-snd-addr-unresolv, err-net-prob, err-content-not-accept, err-unsupp-msg]</span> </li>
 <li><span class="li-head">smil-part</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subject</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mm7</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">add-smil</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">addr-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rfc2822-addr, number, short-code]</span> </li>
 <li><span class="li-head">allow-content-adaptation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charset</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-ascii, utf-8]</span> </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [personal, advertisement, informational, auto, not-included]</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">from</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">from-sender</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">image</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, normal, high, not-included]</span> </li>
 <li><span class="li-head">rsp-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [success, partial-success, client-err, oper-restrict, addr-err, addr-not-found, content-refused, msg-id-not-found, link-id-not-found, msg-fmt-corrupt, app-id-not-found, repl-app-id-not-found, srv-err, not-possible, msg-rejected, multiple-addr-not-supp, app-addr-not-supp, gen-service-err, improper-ident, unsupp-ver, unsupp-oper, validation-err, service-err, service-unavail, service-denied, app-denied]</span> </li>
 <li><span class="li-head">smil-part</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subject</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mms</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">charset</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-ascii, utf-8]</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">image</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">nac-quar</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nntp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">spam</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sslvpn</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">traffic-quota</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">utm</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">webproxy</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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
    - name: Configure replacement message groups.
      fmgr_system_replacemsggroup:
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         system_replacemsggroup:
            admin:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            alertmail:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            auth:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            comment: <value of string>
            custom-message:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            device-detection-portal:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            ec:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            fortiguard-wf:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            ftp:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            group-type: <value in [default, utm, auth, ...]>
            http:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            icap:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            mail:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            mm1:
              -
                  add-smil: <value in [disable, enable]>
                  charset: <value in [us-ascii, utf-8]>
                  class: <value in [personal, advertisement, information, ...]>
                  format: <value in [none, text, html, ...]>
                  from: <value of string>
                  from-sender: <value in [disable, enable]>
                  header: <value in [none, http, 8bit]>
                  image: <value of string>
                  message: <value of string>
                  msg-type: <value of string>
                  priority: <value in [low, normal, high, ...]>
                  rsp-status: <value in [ok, err-unspecified, err-srv-denied, ...]>
                  rsp-text: <value of string>
                  sender-visibility: <value in [hide, show, not-specified]>
                  smil-part: <value of string>
                  subject: <value of string>
            mm3:
              -
                  add-html: <value in [disable, enable]>
                  charset: <value in [us-ascii, utf-8]>
                  format: <value in [none, text, html, ...]>
                  from: <value of string>
                  from-sender: <value in [disable, enable]>
                  header: <value in [none, http, 8bit]>
                  html-part: <value of string>
                  image: <value of string>
                  message: <value of string>
                  msg-type: <value of string>
                  priority: <value in [low, normal, high, ...]>
                  subject: <value of string>
            mm4:
              -
                  add-smil: <value in [disable, enable]>
                  charset: <value in [us-ascii, utf-8]>
                  class: <value in [personal, advertisement, informational, ...]>
                  domain: <value of string>
                  format: <value in [none, text, html, ...]>
                  from: <value of string>
                  from-sender: <value in [disable, enable]>
                  header: <value in [none, http, 8bit]>
                  image: <value of string>
                  message: <value of string>
                  msg-type: <value of string>
                  priority: <value in [low, normal, high, ...]>
                  rsp-status: <value in [ok, err-unspecified, err-srv-denied, ...]>
                  smil-part: <value of string>
                  subject: <value of string>
            mm7:
              -
                  add-smil: <value in [disable, enable]>
                  addr-type: <value in [rfc2822-addr, number, short-code]>
                  allow-content-adaptation: <value in [disable, enable]>
                  charset: <value in [us-ascii, utf-8]>
                  class: <value in [personal, advertisement, informational, ...]>
                  format: <value in [none, text, html, ...]>
                  from: <value of string>
                  from-sender: <value in [disable, enable]>
                  header: <value in [none, http, 8bit]>
                  image: <value of string>
                  message: <value of string>
                  msg-type: <value of string>
                  priority: <value in [low, normal, high, ...]>
                  rsp-status: <value in [success, partial-success, client-err, ...]>
                  smil-part: <value of string>
                  subject: <value of string>
            mms:
              -
                  buffer: <value of string>
                  charset: <value in [us-ascii, utf-8]>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  image: <value of string>
                  msg-type: <value of string>
            nac-quar:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            name: <value of string>
            nntp:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            spam:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            sslvpn:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            traffic-quota:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            utm:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
            webproxy:
              -
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>
 <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>
 <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>
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



