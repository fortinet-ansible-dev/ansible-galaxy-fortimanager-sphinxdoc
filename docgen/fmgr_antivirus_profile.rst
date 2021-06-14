:source: fmgr_antivirus_profile.py

:orphan:

.. _fmgr_antivirus_profile:

fmgr_antivirus_profile -- Configure AntiVirus profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
 <td>antivirus_profile</td>
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
 <li><span class="li-head">antivirus_profile</span> - Configure AntiVirus profiles. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">analytics-bl-filetype</span> - Only submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">analytics-db</span> - Enable/disable using the FortiSandbox signature database to supplement the AV signature databases. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">analytics-max-upload</span> - Maximum size of files that can be uploaded to FortiSandbox (1 - 395 MBytes, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">analytics-wl-filetype</span> - Do not submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-block-log</span> - Enable/disable logging for AntiVirus file blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-virus-log</span> - Enable/disable AntiVirus logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging for antivirus. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ftgd-analytics</span> - Settings to control which files are uploaded to FortiSandbox. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, suspicious, everything]</span> </li>
 <li><span class="li-head">inspection-mode</span> - Inspection mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow-based]</span> </li>
 <li><span class="li-head">mobile-malware-db</span> - Enable/disable using the mobile malware signature database. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group customized for this profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">scan-mode</span> - Choose between full scan mode and quick scan mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [quick, full, legacy, default]</span> </li>
 <li><span class="li-head">feature-set</span> - Flow/proxy feature set. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">analytics-accept-filetype</span> - Only submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">analytics-ignore-filetype</span> - Do not submit files matching this DLP file-pattern to FortiSandbox. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cifs</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, quarantine, avmonitor]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">content-disarm</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">cover-page</span> - Enable/disable inserting a cover page into the disarmed document. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">detect-only</span> - Enable/disable only detect disarmable files, do not alter content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">error-action</span> - Action to be taken if CDR engine encounters an unrecoverable error. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, log-only, ignore]</span> </li>
 <li><span class="li-head">office-action</span> - Enable/disable stripping of PowerPoint action events in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-dde</span> - Enable/disable stripping of Dynamic Data Exchange events in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-embed</span> - Enable/disable stripping of embedded objects in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-hylink</span> - Enable/disable stripping of hyperlinks in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-linked</span> - Enable/disable stripping of linked objects in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-macro</span> - Enable/disable stripping of macros in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">original-file-destination</span> - Destination to send original file if active content is removed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortisandbox, quarantine, discard]</span> </li>
 <li><span class="li-head">pdf-act-form</span> - Enable/disable stripping of PDF document actions that submit data to other targets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-gotor</span> - Enable/disable stripping of PDF document actions that access other PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-java</span> - Enable/disable stripping of PDF document actions that execute JavaScript code. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-launch</span> - Enable/disable stripping of PDF document actions that launch other applications. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-movie</span> - Enable/disable stripping of PDF document actions that play a movie. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-sound</span> - Enable/disable stripping of PDF document actions that play a sound. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-embedfile</span> - Enable/disable stripping of embedded files in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-hyperlink</span> - Enable/disable stripping of hyperlinks from PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-javacode</span> - Enable/disable stripping of JavaScript code in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">ems-threat-feed</span> - Enable/disable use of EMS threat feed when performing AntiVirus scan. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-blocklist</span> - One or more external malware block lists. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-blocklist-archive-scan</span> - Enable/disable external-blocklist archive scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-blocklist-enable-all</span> - Enable/disable all external blocklists. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ftp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">http</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">content-disarm</span> - Enable Content Disarm and Reconstruction for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor, strict-file]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">imap</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">content-disarm</span> - Enable Content Disarm and Reconstruction for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">executables</span> - Treat Windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, virus]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">mapi</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">executables</span> - Treat Windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, virus]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, quarantine, avquery, avmonitor]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">nac-quar</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">expiry</span> - Duration of quarantine. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">infected</span> - Enable/Disable quarantining infected hosts to the banned user list. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, quar-src-ip, quar-interface]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable AntiVirus quarantine logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">nntp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">outbreak-prevention-archive-scan</span> - Enable/disable outbreak-prevention archive scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pop3</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">content-disarm</span> - Enable Content Disarm and Reconstruction for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">executables</span> - Treat Windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, virus]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">smtp</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">content-disarm</span> - Enable Content Disarm and Reconstruction for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">executables</span> - Treat Windows executable files as viruses for the purpose of blocking or monitoring. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, virus]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [scan, file-filter, quarantine, avquery, avmonitor]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">ssh</span> <span class="li-normal">type: dict</span> </li>
 <ul class="ul-self">
 <li><span class="li-head">archive-block</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">archive-log</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [encrypted, corrupted, multipart, nested, mailbomb, unhandled, partiallycorrupted, fileslimit, timeout]</span> </li>
 <li><span class="li-head">av-scan</span> - Enable AntiVirus scan service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">emulator</span> - Enable/disable the virus emulator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-blocklist</span> - Enable external-blocklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, monitor, block]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <span class="li-normal">choices: [avmonitor, quarantine, scan]</span> </li>
 <li><span class="li-head">outbreak-prevention</span> - Enable virus outbreak prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive, disable, block, monitor]</span> </li>
 <li><span class="li-head">quarantine</span> - Enable/disable quarantine for infected files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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
    - name: Configure AntiVirus profiles.
      fmgr_antivirus_profile:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         antivirus_profile:
            analytics-bl-filetype: <value of string>
            analytics-db: <value in [disable, enable]>
            analytics-max-upload: <value of integer>
            analytics-wl-filetype: <value of string>
            av-block-log: <value in [disable, enable]>
            av-virus-log: <value in [disable, enable]>
            comment: <value of string>
            extended-log: <value in [disable, enable]>
            ftgd-analytics: <value in [disable, suspicious, everything]>
            inspection-mode: <value in [proxy, flow-based]>
            mobile-malware-db: <value in [disable, enable]>
            name: <value of string>
            replacemsg-group: <value of string>
            scan-mode: <value in [quick, full, legacy, ...]>
            feature-set: <value in [proxy, flow]>
            analytics-accept-filetype: <value of string>
            analytics-ignore-filetype: <value of string>
            cifs:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               emulator: <value in [disable, enable]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - quarantine
                 - avmonitor
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            content-disarm:
               cover-page: <value in [disable, enable]>
               detect-only: <value in [disable, enable]>
               error-action: <value in [block, log-only, ignore]>
               office-action: <value in [disable, enable]>
               office-dde: <value in [disable, enable]>
               office-embed: <value in [disable, enable]>
               office-hylink: <value in [disable, enable]>
               office-linked: <value in [disable, enable]>
               office-macro: <value in [disable, enable]>
               original-file-destination: <value in [fortisandbox, quarantine, discard]>
               pdf-act-form: <value in [disable, enable]>
               pdf-act-gotor: <value in [disable, enable]>
               pdf-act-java: <value in [disable, enable]>
               pdf-act-launch: <value in [disable, enable]>
               pdf-act-movie: <value in [disable, enable]>
               pdf-act-sound: <value in [disable, enable]>
               pdf-embedfile: <value in [disable, enable]>
               pdf-hyperlink: <value in [disable, enable]>
               pdf-javacode: <value in [disable, enable]>
            ems-threat-feed: <value in [disable, enable]>
            external-blocklist: <value of string>
            external-blocklist-archive-scan: <value in [disable, enable]>
            external-blocklist-enable-all: <value in [disable, enable]>
            ftp:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               emulator: <value in [disable, enable]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - file-filter
                 - quarantine
                 - avquery
                 - avmonitor
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            http:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               content-disarm: <value in [disable, enable]>
               emulator: <value in [disable, enable]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - file-filter
                 - quarantine
                 - avquery
                 - avmonitor
                 - strict-file
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            imap:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               content-disarm: <value in [disable, enable]>
               emulator: <value in [disable, enable]>
               executables: <value in [default, virus]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - file-filter
                 - quarantine
                 - avquery
                 - avmonitor
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            mapi:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               emulator: <value in [disable, enable]>
               executables: <value in [default, virus]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - quarantine
                 - avquery
                 - avmonitor
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            nac-quar:
               expiry: <value of string>
               infected: <value in [none, quar-src-ip, quar-interface]>
               log: <value in [disable, enable]>
            nntp:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               emulator: <value in [disable, enable]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - file-filter
                 - quarantine
                 - avquery
                 - avmonitor
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            outbreak-prevention-archive-scan: <value in [disable, enable]>
            pop3:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               content-disarm: <value in [disable, enable]>
               emulator: <value in [disable, enable]>
               executables: <value in [default, virus]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - file-filter
                 - quarantine
                 - avquery
                 - avmonitor
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            smtp:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               content-disarm: <value in [disable, enable]>
               emulator: <value in [disable, enable]>
               executables: <value in [default, virus]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - scan
                 - file-filter
                 - quarantine
                 - avquery
                 - avmonitor
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>
            ssh:
               archive-block:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               archive-log:
                 - encrypted
                 - corrupted
                 - multipart
                 - nested
                 - mailbomb
                 - unhandled
                 - partiallycorrupted
                 - fileslimit
                 - timeout
               av-scan: <value in [disable, monitor, block]>
               emulator: <value in [disable, enable]>
               external-blocklist: <value in [disable, monitor, block]>
               options:
                 - avmonitor
                 - quarantine
                 - scan
               outbreak-prevention: <value in [disabled, files, full-archive, ...]>
               quarantine: <value in [disable, enable]>



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



