
Error Handling
===============

|

By convention, Ansible task can fail when a non-zero ``rc`` code is
passed to. FortiManager Ansible modules follows that convention and
provides additional error handing mechanisms, which makes it simple and
flexible enough for us to deal with well defined error codes in
requests.

There are three types of mechanisms we can employ in fortimanager
ansible modules.

rc\_succeeded
~~~~~~~~~~~~~

This is a parameter introduced in fortimanager modules for those who
want not to fail the task for a specific ``response_code``, its type is
a interger list, which means we can define more than one rc code.

One example of ``rc_succeeded`` is as below:

::

    #cat test.yml
    - name: Create and Execute script
      hosts: fortimanager01
      gather_facts: no
      connection: httpapi
      collections:
        - fortinet.fortimanager
      vars:
        ansible_httpapi_use_ssl: True
        ansible_httpapi_validate_certs: False
        ansible_httpapi_port: 443
        script_name: 'demo script'
      tasks:
        - name: fmgr_pkg_firewall_dospolicy
          fmgr_pkg_firewall_dospolicy:
            workspace_locking_adom: 'root'
            adom: root
            pkg: demopackage1
            state: present
            pkg_firewall_dospolicy:
                comments: 'Just a comment'
                policyid: '123'
            rc_succeeded: [ -9001 ]

    #ansible-playbook -i host -vvv test.yml   
    ok: [fortimanager01] => {
        "changed": false,
        "invocation": {
            "module_args": {
                "adom": "root",
                "pkg": "demopackage1",
                "pkg_firewall_dospolicy": {
                    "anomaly": null,
                    "comments": "Just a comment",
                    "dstaddr": null,
                    "interface": null,
                    "policyid": 123,
                    "service": null,
                    "srcaddr": null,
                    "status": null
                },
                "rc_failed": null,
                "rc_succeeded": [
                    -9001
                ],
                "state": "present",
                "workspace_locking_adom": "root",
                "workspace_locking_timeout": 300
            }
        },
        "meta": {
            "request_url": "/pm/config/adom/root/pkg/demopackage1/firewall/DoS-policy",
            "response_code": -9001,
            "response_message": "firewall/DoS-policy/123/status : invalid value - prop[status]: binary option empty or invalid, argc(0)",
            "result_code_overriding": "rc code:-9001 is overridden to success"
        },
        "rc": -9001
    }

**In normal case, an reponse code ``-9001`` definitely causes a failure,
``rc_succeeded`` allows us to skip the error**

rc\_failed
~~~~~~~~~~

Like ``rc_succeeded``, ``rc_failed`` is the rc code list for
fortimanager module to override the conditions to fail.

An example of ``rc_failed`` is we actually want to fail the task that is
deleting a non-existing object.

::

    #cat test.yml
    - name: Create and Execute script
      hosts: fortimanager01
      gather_facts: no
      connection: httpapi
      collections:
        - fortinet.fortimanager
      vars:
        ansible_httpapi_use_ssl: True
        ansible_httpapi_validate_certs: False
        ansible_httpapi_port: 443
        script_name: 'demo script'
      tasks:
        - name: create the script
          fmgr_dvmdb_script:
            workspace_locking_adom: 'root'
            state: absent
            adom: root
            dvmdb_script:
                name: 'demoscript'
            rc_failed:
                - -3
    #ansible-playbook -i host -vvv test.yml
    fatal: [fortimanager01]: FAILED! => {
        "ansible_facts": {
            "discovered_interpreter_python": "/usr/bin/python"
        },
        "changed": true,
        "invocation": {
            "module_args": {
                "adom": "root",
                "dvmdb_script": {
                    "content": "native content",
                    "desc": "script created via Ansible",
                    "filter_build": null,
                    "filter_device": null,
                    "filter_hostname": null,
                    "filter_ostype": null,
                    "filter_osver": null,
                    "filter_platform": null,
                    "filter_serial": null,
                    "modification_time": null,
                    "name": "demoscript",
                    "script_schedule": null,
                    "target": null,
                    "type": "cli"
                },
                "rc_failed": [
                    -3
                ],
                "rc_succeeded": null,
                "state": "absent",
                "workspace_locking_adom": "root",
                "workspace_locking_timeout": 300
            }
        },
        "meta": {
            "response_code": -3,
            "response_message": "object not exist",
            "result_code_overriding": "rc code:-3 is overridden to failure"
        },
        "rc": 0
    }

By default, a response\_code -3 of deleting an object will not cause the
task failure, but it tells the truth that the object doesn't exist and
we might want to fail the task in this case, ``rc_failed`` can help us do
the work.

failed\_when
~~~~~~~~~~~~

``failed_when`` is Ansible native failure detection mechanism, it's more
flexible and can be combined with our fortimanager ansible modules.

For more information of ``failed_when``, please visit
`page <https://docs.ansible.com/ansible/latest/user_guide/playbooks_error_handling.html#controlling-what-defines-failure>`__.

Precedence of Three Mechanisms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general, ``failed_when`` takes precedence over the other two, while
``rc_failed`` has precedece over ``rc_succeeded``.

we can specify more than one condition statement, and the one with
highest precedence will be chosen to calculate the failure or success
result.


