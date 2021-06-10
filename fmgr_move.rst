:source: fmgr_move.py

:orphan:

.. _fmgr_move:

fmgr_move -- Reorder Two Objects.
+++++++++++++++++++++++++++++++++++++++

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
 <li><span class="li-head">enable_log</span> - Enable/Disable logging for task <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>
 <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>
 <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>
 <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>

 <li><span class="li-head">move</span> - Reorder Two Objects. <span class="li-normal">type: dict</span></li>
 <ul class="ul-self">
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> <span class="li-required">required: true</span></li>
 <li><span class="li-head">action</span> - Direction to indicate where to move an object entry. <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: before, after</span></li>
 <li><span class="li-head">selector</span> - selector of the moved object <span class="li-normal">type: str</span> <span class="li-required">choices:</span></li>
    <li style="list-style: none;"><section class="accordion">
    <input type="checkbox" name="collapse" id="handle1">
    <h2 class="handle">
        <label for="handle1"><u>Show full selector list...</u></label>
    </h2>
    <div class="content"> 
    <ul class="ul-self">
        <li><span class="li-required">dnsfilter_domainfilter_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">application_list_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">application_list_entries_parameters</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">vpnsslweb_portal_bookmarkgroup</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">vpnsslweb_portal_bookmarkgroup_bookmarks</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">vpnsslweb_portal_splitdns</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_centralsnatmap</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_dospolicy</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_dospolicy6</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_interfacepolicy</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_interfacepolicy6</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_localinpolicy</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_localinpolicy6</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_multicastpolicy</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_multicastpolicy6</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_policy</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_policy46</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_policy6</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_policy64</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_proxypolicy</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_shapingpolicy</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_central_dnat</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">webfilter_contentheader_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">webfilter_urlfilter_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">ips_sensor_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">ips_sensor_filter</span> - available versions:
                    <span class="li-normal">6.0.0</span>
        </li>
        <li><span class="li-required">spamfilter_bwl_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
        </li>
        <li><span class="li-required">spamfilter_bword_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
        </li>
        <li><span class="li-required">firewall_carrierendpointbwl_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
        </li>
        <li><span class="li-required">firewall_identitybasedroute</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">firewall_service_category</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">firewall_service_custom</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">firewall_shapingprofile_shapingentries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">firewall_vip</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">firewall_vip6</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">system_sdnconnector_externalip</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">system_sdnconnector_nic</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">system_sdnconnector_nic_ip</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">system_sdnconnector_routetable</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">system_sdnconnector_routetable_route</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">system_sdnconnector_route</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">wanprof_system_virtualwanlink_members</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">wanprof_system_virtualwanlink_service</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">wanprof_system_virtualwanlink_service_sla</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">sshfilter_profile_shellcommands</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">bonjourprofile_policylist</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">dlp_filepattern_entries</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">dlp_sensor_filter</span> - available versions:
                    <span class="li-normal">6.0.0</span>
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">emailfilter_bword_entries</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">emailfilter_bwl_entries</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">emailfilter_profile_filefilter_entries</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">pkg_authentication_rule</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_firewall_consolidated_policy</span> - available versions:
                    <span class="li-normal">6.2.1</span>
        </li>
        <li><span class="li-required">pkg_firewall_securitypolicy</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">cifs_profile_filefilter_entries</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">application_list_defaultnetworkservices</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">webfilter_profile_filefilter_entries</span> - available versions:
                    <span class="li-normal">6.2.1</span>
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">sshfilter_profile_filefilter_entries</span> - available versions:
                    <span class="li-normal">6.4.0</span>
        </li>
        <li><span class="li-required">filefilter_profile_rules</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">wanprof_system_sdwan_members</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">wanprof_system_sdwan_service</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">wanprof_system_sdwan_service_sla</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">wanprof_system_sdwan_zone</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">apcfgprofile_commandlist</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">mpskprofile_mpskgroup</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">mpskprofile_mpskgroup_mpskkey</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">firewall_accessproxy</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">videofilter_youtubechannelfilter_entries</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">videofilter_profile_fortiguardcategory_filters</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">pkg_central_dnat6</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
        <li><span class="li-required">emailfilter_blockallowlist_entries</span> - available versions:
                    <span class="li-normal">7.0.0</span>
        </li>
    </ul>
    </div>
    </section>

    <li><span class="li-head">self</span> - the parameter for each selector <span class="li-normal">type: dict</span> <span class="li-required">choices:</span></li>
    <li style="list-style: none;"><section class="accordion">
    <input type="checkbox" name="collapse" id="handle3">
    <h2 class="handle">
        <label for="handle3"><u>More details about parameter: <b>self</b>...</u></label>
    </h2>
    <div class="content">
    <ul class="ul-self">
        <li><span class="li-normal">params for dnsfilter_domainfilter_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">domain-filter</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for application_list_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">list</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for application_list_entries_parameters:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">list</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">parameters</span></li>
        </ul>
        <li><span class="li-normal">params for vpnsslweb_portal_bookmarkgroup:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">portal</span></li>
            <li><span class="li-normal">bookmark-group</span></li>
        </ul>
        <li><span class="li-normal">params for vpnsslweb_portal_bookmarkgroup_bookmarks:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">portal</span></li>
            <li><span class="li-normal">bookmark-group</span></li>
            <li><span class="li-normal">bookmarks</span></li>
        </ul>
        <li><span class="li-normal">params for vpnsslweb_portal_splitdns:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">portal</span></li>
            <li><span class="li-normal">split-dns</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_centralsnatmap:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">central-snat-map</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_dospolicy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">DoS-policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_dospolicy6:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">DoS-policy6</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_interfacepolicy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">interface-policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_interfacepolicy6:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">interface-policy6</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_localinpolicy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">local-in-policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_localinpolicy6:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">local-in-policy6</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_multicastpolicy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">multicast-policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_multicastpolicy6:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">multicast-policy6</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_policy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_policy46:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">policy46</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_policy6:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">policy6</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_policy64:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">policy64</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_proxypolicy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">proxy-policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_shapingpolicy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">shaping-policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_central_dnat:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">dnat</span></li>
        </ul>
        <li><span class="li-normal">params for webfilter_contentheader_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">content-header</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for webfilter_urlfilter_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">urlfilter</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for ips_sensor_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sensor</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for ips_sensor_filter:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sensor</span></li>
            <li><span class="li-normal">filter</span></li>
        </ul>
        <li><span class="li-normal">params for spamfilter_bwl_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">bwl</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for spamfilter_bword_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">bword</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_carrierendpointbwl_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">carrier-endpoint-bwl</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_identitybasedroute:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">identity-based-route</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_service_category:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">category</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_service_custom:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">custom</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_shapingprofile_shapingentries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">shaping-profile</span></li>
            <li><span class="li-normal">shaping-entries</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_vip:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">vip</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_vip6:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">vip6</span></li>
        </ul>
        <li><span class="li-normal">params for system_sdnconnector_externalip:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sdn-connector</span></li>
            <li><span class="li-normal">external-ip</span></li>
        </ul>
        <li><span class="li-normal">params for system_sdnconnector_nic:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sdn-connector</span></li>
            <li><span class="li-normal">nic</span></li>
        </ul>
        <li><span class="li-normal">params for system_sdnconnector_nic_ip:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sdn-connector</span></li>
            <li><span class="li-normal">nic</span></li>
            <li><span class="li-normal">ip</span></li>
        </ul>
        <li><span class="li-normal">params for system_sdnconnector_routetable:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sdn-connector</span></li>
            <li><span class="li-normal">route-table</span></li>
        </ul>
        <li><span class="li-normal">params for system_sdnconnector_routetable_route:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sdn-connector</span></li>
            <li><span class="li-normal">route-table</span></li>
            <li><span class="li-normal">route</span></li>
        </ul>
        <li><span class="li-normal">params for system_sdnconnector_route:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sdn-connector</span></li>
            <li><span class="li-normal">route</span></li>
        </ul>
        <li><span class="li-normal">params for wanprof_system_virtualwanlink_members:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">wanprof</span></li>
            <li><span class="li-normal">members</span></li>
        </ul>
        <li><span class="li-normal">params for wanprof_system_virtualwanlink_service:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">wanprof</span></li>
            <li><span class="li-normal">service</span></li>
        </ul>
        <li><span class="li-normal">params for wanprof_system_virtualwanlink_service_sla:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">wanprof</span></li>
            <li><span class="li-normal">service</span></li>
            <li><span class="li-normal">sla</span></li>
        </ul>
        <li><span class="li-normal">params for sshfilter_profile_shellcommands:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">profile</span></li>
            <li><span class="li-normal">shell-commands</span></li>
        </ul>
        <li><span class="li-normal">params for bonjourprofile_policylist:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">bonjour-profile</span></li>
            <li><span class="li-normal">policy-list</span></li>
        </ul>
        <li><span class="li-normal">params for dlp_filepattern_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">filepattern</span></li>
            <li><span class="li-normal">entries</span></li>
        </ul>
        <li><span class="li-normal">params for dlp_sensor_filter:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">sensor</span></li>
            <li><span class="li-normal">filter</span></li>
        </ul>
        <li><span class="li-normal">params for emailfilter_bword_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">bword</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for emailfilter_bwl_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">bwl</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for emailfilter_profile_filefilter_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">profile</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_authentication_rule:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">rule</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_consolidated_policy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">policy</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_firewall_securitypolicy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">security-policy</span></li>
        </ul>
        <li><span class="li-normal">params for cifs_profile_filefilter_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">profile</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for application_list_defaultnetworkservices:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">list</span></li>
            <li><span class="li-normal">default-network-services</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for webfilter_profile_filefilter_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">profile</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for sshfilter_profile_filefilter_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">profile</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for filefilter_profile_rules:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">profile</span></li>
            <li><span class="li-normal">rules</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for wanprof_system_sdwan_members:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">wanprof</span></li>
            <li><span class="li-normal">members</span></li>
        </ul>
        <li><span class="li-normal">params for wanprof_system_sdwan_service:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">wanprof</span></li>
            <li><span class="li-normal">service</span></li>
        </ul>
        <li><span class="li-normal">params for wanprof_system_sdwan_service_sla:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">wanprof</span></li>
            <li><span class="li-normal">service</span></li>
            <li><span class="li-normal">sla</span></li>
        </ul>
        <li><span class="li-normal">params for wanprof_system_sdwan_zone:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">wanprof</span></li>
            <li><span class="li-normal">zone</span></li>
        </ul>
        <li><span class="li-normal">params for apcfgprofile_commandlist:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">apcfg-profile</span></li>
            <li><span class="li-normal">command-list</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for mpskprofile_mpskgroup:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">mpsk-profile</span></li>
            <li><span class="li-normal">mpsk-group</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for mpskprofile_mpskgroup_mpskkey:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">mpsk-profile</span></li>
            <li><span class="li-normal">mpsk-group</span></li>
            <li><span class="li-normal">mpsk-key</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for firewall_accessproxy:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">access-proxy</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for videofilter_youtubechannelfilter_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">youtube-channel-filter</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for videofilter_profile_fortiguardcategory_filters:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">profile</span></li>
            <li><span class="li-normal">filters</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
        <li><span class="li-normal">params for pkg_central_dnat6:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">adom</span></li>
            <li><span class="li-normal">pkg</span></li>
            <li><span class="li-normal">dnat6</span></li>
        </ul>
        <li><span class="li-normal">params for emailfilter_blockallowlist_entries:</span></li>
        <ul class="ul-self">
            <li><span class="li-normal">block-allow-list</span></li>
            <li><span class="li-normal">entries</span></li>
            <li><span class="li-normal">adom</span></li>
        </ul>
    </ul>
    </div>
    </section>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.

   - Selector is a mandatory parameter for the module, and the params is varying depending on the selector.

   - Semantic description for the module: move ``self`` ``action(before or after)`` ``target``

   - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded


Examples
--------

.. code-block:: yaml+jinja

 - hosts: fortimanager01
   collections:
    - fortinet.fortimanager
   connection: httpapi
   vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
   tasks:
    - name: Move a firewall vip object
      fmgr_move:
        move:
          selector: 'firewall_vip'
          target: 'ansible-test-vip_first'
          action: 'before'
          self:
            adom: 'root'
            vip: 'ansible-test-vip_second'


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


