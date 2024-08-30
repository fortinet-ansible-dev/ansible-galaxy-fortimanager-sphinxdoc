
Frequently Asked Questions (FAQ)
================================

|

**TABLE OF CONTENTS:**
 - `Modules For Policy Package.`_
 - `What You Need To Know About Logging.`_
 - `What Is Workspace Locking?`_
 -  `How To Deal With Task Result?`_
 - `When to Use Parameter bypass_validation?`_
 - `How To Monitor FortiManager Task?`_
 - `How To Use FortiManager Ansible without Providing Username and Password?`_
 - `How To Use FortiManager Ansible With FortiManager Cloud?`_

|

Modules For Policy Package.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike other modules, There are three modules in FortiManager Ansible collection as the result of seperate API backends:

 - ``fmgr_pm_pkg`` - **update** or **delete** a package, no matter whether it is ``adom`` specific or ``global``.
 - ``fmgr_pm_pkg_adom`` - **create** or **update** a ``adom`` specific package.
 - ``fmgr_pm_pkg_global`` - **create** or **update** a ``global`` package.



Create/Update An ADOM-specific Policy Package
...............................................

::

   - name: create a package in a adom
     fmgr_pm_pkg_adom:
        adom: 'root'
        pm_pkg_adom:
            name: 'adom.root.package0'
            type: 'pkg'


**Note:** you are not allowed to modify the name of the package with module ``fmgr_pm_pkg_adom``.


Create/Update A Global Policy Package
...............................................

::

   - name: create a package in a adom
     fmgr_pm_pkg_global:
        pm_pkg_global:
            name: 'global.package0'
            type: 'pkg'

**Note:** you are not allowed to modify the name of the package with module ``fmgr_pm_pkg_global``.

Rename A Policy Package
..........................

::

   - name: policy package
     fmgr_pm_pkg:
        adom: "root"
        pkg_path: 'adom.root.package0'
        state: 'present'
        pm_pkg:
            name: 'adom.root.package1'

   - name: policy package
     fmgr_pm_pkg:
        adom: "global"
        pkg_path: 'global.package0'
        state: 'present'
        pm_pkg:
            name: 'global.package1'


Remove A Policy Package
..........................

::

   - name: policy package
     fmgr_pm_pkg:
        adom: "root"
        pkg_path: 'adom.root.package0'
        state: 'absent'
        pm_pkg:
            name: 'adom.root.package0'

   - name: policy package
     fmgr_pm_pkg:
        adom: "global"
        pkg_path: 'global.package0'
        state: 'absent'
        pm_pkg:
            name: 'global.package0'

What You Need To Know About Logging. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FortiManager Ansible has requests and intermediate data stored in a log file ``/tmp/fortimanager.ansible.log`` to ease troubleshooting. 

Prior to ``2.0.3``, the log file is always created under that path; since ``2.0.3``, logging is only enabled by setting ``enable_log`` option for a task,
it means you will no longer see the log file by default since ``2.0.3`` unless you turn it on explicitly.

What Is Workspace Locking?
~~~~~~~~~~~~~~~~~~~~~~~~~~

FortiManager supports multi-workspace mode, workspace guarantees you that you are operating in an administrative domain
explusively so that no other users will not preempt you as long as you lock the workspace in advance. 

To enable workspace locking on FortiManager ``6.0.x``, you usually also enable multi-adom status. Here are cli commands:
::

    FMG-VM64 # config system global
    (global)# set adom-status enable
    (global)# set workspace-mode normal
    (global)# end
    FMG-VM64 #

also you are able to enable workspace mode via module ``fmgr_system_global``:
::

   - name: Enable Workspace Mode
     fmgr_system_global:
        system_global:
            adom-status: enable
            workspace-mode: normal

After workspace mode is enabled, you must assign the adom to ``workspace_locking_adom`` and a time value to ``workspace_locking_timeout`` optionally to
complete a successful task.

 - ``workspace_locking_adom`` - The adom you are going to access and lock, either ``global`` or a custom adom. 
 - ``workspace_locking_timeout`` - the ansible task will poll and wait for the adom to be unlocked if it was locked by other users, the parameter is the maximum
   seconds to wait before reporting failure, default value is `300` seconds.

here is an example to put the locking directives in tasks:
::

   - name: create a package in a adom
     fmgr_pm_pkg_adom:
        workspace_locking_adom: 'root'
        workspace_locking_timeout: 300
        adom: 'root'
        pm_pkg_adom:
            name: 'adom.root.package0'
            type: 'pkg'

**Note: as ansible tasks terminates normally, the lock will be released automatically.**

**Caveat: if any tasks are interrupted, e.g. inputing a CTRL + ^C, you will no longer be able to use Ansible to access FMG anymore unless the previous session expires, in case of immediate access, you have to disable workspace mode via CLI console.**

How To Deal With Task Result?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Error Handling`_ for more. 

When to Use Parameter bypass_validation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are not encouraged to use ``bypass_validation`` except that you are sure something is wrong with the parameter definition and you want to fix them on you own immediately.
by setting `bypass_validation` to `True`, the content of parameters is not examined, thus enabling you to send any parameters to FortiManager backend server.

To use this parameter, you are likely to look up the defnition for an API on `fortiapi spec page`_. 

How To Monitor FortiManager Task?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are lots of FortiManager APIs which return a task identifier. the task itself is running in the remote FortiManager server.
you must poll the task periodically to see whether the task terminates or goes wrong.

an example is to add a fortigate device to fortimanager, the task may last for minutes, you can find the `full playbook`_ on `Search Playbooks`_ page . 
the snippet is very straightforward:
::

    - name: poll the task
      fmgr_fact:
        facts:
            selector: 'task_task'
            params:
                task: '{{installing_task.meta.response_data.taskid}}'
      register: taskinfo
      until: taskinfo.meta.response_data.percent == 100
      retries: 30
      delay: 5
      failed_when: taskinfo.meta.response_data.state == 'error' and 'devsnexist' not in taskinfo.meta.response_data.line[0].detail

- ``until`` -  the condition to quit polling, this is the condition to quit normally
- ``retries`` - how many times you want to try to check the status of running task.
- ``delay`` - checking frequency: `1/delay`.
- ``failed_when`` - failing condition in which you regard the task a failure, this is the condition to quit abnormally


How To Use FortiManager Ansible without Providing Username and Password?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FortiManager Ansible collection supports three different ways to login.

- Providing ansible_user and ansible_password.
- Using access token.
- Using the Forticloud access token (only for the FortiManager managed by Forticloud).

If you use multiple login methods at the same time, the program will first consider the access token, then consider the FortiCloud access token, and finally consider the ansible_user and ansible_password.

To avoid unexpected behavior, it is suggested to only use one login method at a time.

If you want to use the access token to login FortiManager Ansible, please go to the CLI interface of FortiManager and enter the following command:

::

  config system admin user
    edit api_user_example_name
      set profileid Super_User
      set user_type api
      set rpc-permit read-write
    next
  end


Then, use ``execute api-user generate-key api_user_example_name`` and you will get an API key.

::

  FMG-VM64 # execute api-user generate-key api_user_example_name
  New API key: XXXXXXXXXXXXXXX
  

You can use this API key in your playbook, and you don't need to provide ansible_user and ansible_password anymore.

Here is an example of how to use access token:

::

  - hosts: fortimanagers
    connection: httpapi
    collections:
      - fortinet.fortimanager
    vars:
      ansible_httpapi_use_ssl: yes
      ansible_httpapi_validate_certs: no
      ansible_httpapi_port: 443
    tasks:
      - name: get fact
        fmgr_fact:
          access_token: <your access_token>
          enable_log: true
          facts:
            selector: "sys_status"
        register: result
      - name: Display response
        debug:
          var: result


How To Use FortiManager Ansible With FortiManager Cloud?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FortiManager can be managed by forticloud. Example of a fortimanager cloud host: ``1234567.us-west-1.fortimanager.forticloud.com``.

It's possible to authenticate Ansible client with forticloud API access token.
``forticloud_access_token`` is the module option to enable forticloud access token based authentication. 

To obtain access token, it's required to register an API user in https://support.fortinet.com/iam/#/api-user and download the crendentials which contains
needed API user ID and password. it's strongly recommended that you keep it safe!

below is an example to obtain access token:
::

  - hosts: fortimanager00
    collections:
      - fortinet.fortimanager
    connection: httpapi
    vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
      FORTICLOUD_APIID: "3EE835AF-F9F8-48........"
      FORTICLOUD_PASSWD: "36b25667c61b2.........."
    tasks:
      - name: Generate Access Token From FortiCloud Auth Server.
        uri:
          url: https://customerapiauth.fortinet.com/api/v1/oauth/token/
          method: POST
          body_format: json
          return_content: true
          headers:
            Content-Type: application/json
          body: '{"username": "{{ FORTICLOUD_APIID }}", "password": "{{ FORTICLOUD_PASSWD }}", "client_id": "FortiManager", "grant_type": "password"}'
        register: tokeninfo


then in subsequent tasks, we can reference returned token:

::

   - name: Configure IPv4 addresses.
     fmgr_firewall_address:
        adom: root
        state: present
        enable_log: true
        forticloud_access_token: '{{ tokeninfo.json.access_token }}'
        firewall_address:
          name: Win11
          comment: from Ansible.
          organization: Fortinet
          start-ip: 192.168.1.5
          end-ip: 192.168.1.11
          type: iprange
          associated-interface: any

Access token usually expires in hours, you should always renew one in case of failure.


.. _Search Playbooks: example.html
.. _full playbook: https://raw.githubusercontent.com/fortinet-ansible-dev/fortimanager-playbook-example/2.0.0/output/discover_and_add_device.yml
.. _fortiapi spec page: https://fndn.fortinet.net/index.php?/fortiapi/5-fortimanager/#
.. _Error Handling: errors.html
.. _Modules For Policy Package.: #modules-for-policy-package
.. _What You Need To Know About Logging.: #what-you-need-to-know-about-logging
.. _What Is Workspace Locking?: #what-is-workspace-locking
.. _How To Deal With Task Result?: #how-to-deal-with-task-result
.. _When to Use Parameter bypass_validation?: #when-to-use-parameter-bypass-validation
.. _How To Monitor FortiManager Task?: #how-to-monitor-fortimanager-task
.. _How To Use FortiManager Ansible With FortiCloud?: #how-to-use-fortimanager-ansible-with-forticloud

