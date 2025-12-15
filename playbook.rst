
Run Your First Playbook
==============================

This document explains how to run your first FortiManager Ansible playbook.

--------------

With FortiManager Galaxy collection, you are always recommended to run
FortiManager module in ``httpapi`` manner. The first step is to prepare your
host inventory with which you can use ``ansible-vault`` to encrypt or
decrypt your secrets for the sake of confidentiality.

Prepare host inventory
~~~~~~~~~~~~~~~~~~~~~~

in our case we create a file named ``hosts``:

With Standard User/password authentication
----------

::

   [fortimanagers]
   # Storing authentication token in plain text file is a bad idea on a security point of view
   # Please prefer ansible-vault or any encrypted mean to store sensitive data
   fortimanager01 ansible_host=192.168.190.1 ansible_user="admin" ansible_password="password"
   fortimanager02 ansible_host=192.168.190.2 ansible_user="admin" ansible_password="password"

   [fortimanagers:vars]
   ansible_connection=httpapi
   ansible_network_os=fortinet.fortimanager.fortimanager
   ansible_httpapi_port=443
   ansible_httpapi_use_ssl=true
   #  Disabling TLS certificate verification is a bad idea on security point of view, 
   #  but if you use default certificates that are self-signed, you nedd to disable it.
   #  Please use valid certificates for your production environments and keep certificate validation ON.
   ansible_httpapi_validate_certs=false

With REST API user token based authentication
----------

::

   [fortimanagers]
   # Storing authentication token in plain text file is a bad idea on a security point of view
   # Please prefer ansible-vault or any encrypted mean to store sensitive data
   fortimanager01 ansible_host=192.168.190.1 api_bearer_token="YOUR_GENERATED_API_KEY"
   fortimanager02 ansible_host=192.168.190.2 api_bearer_token="YOUR_GENERATED_API_KEY"

   [fortimanagers:vars]
   ansible_connection=httpapi
   ansible_network_os=fortinet.fortimanager.fortimanager
   ansible_httpapi_port=443
   ansible_httpapi_use_ssl=true
   #  Disabling TLS certificate verification is a bad idea on security point of view, 
   #  but if you use default certificates that are self-signed, you nedd to disable it.
   #  Please use valid certificates for your production environments and keep certificate validation ON.
   ansible_httpapi_validate_certs=false

Write the playbook
~~~~~~~~~~~~~~~~~~

An Example with User/Password authentication
----------

in the example: ``test.yml`` we are going to create a script on FortiManager:

::

   - name: Example playbook
     hosts: fortimanagers
     vars:
       # You don't need to specify the following vars if you specified them in the host file.
       # ansible_connection: httpapi
       # ansible_network_os: fortinet.fortimanager.fortimanager
       # ansible_facts_modules: setup
       # ansible_httpapi_port: 443
       # ansible_httpapi_use_ssl: true
       #
       #  Disabling TLS certificate verification is a bad idea on security point of view, 
       #  but if you use default certificates that are self-signed, you nedd to disable it.
       #  Please use valid certificates for your production environments and keep certificate validation ON.
       # ansible_httpapi_validate_certs=false
     tasks:
      - name: Create a script on FortiManager.
        fortinet.fortimanager.fmgr_dvmdb_script:
           adom: 'adom'
           state: 'present'
           dvmdb_script:
              desc: 'The script create via Ansible'
              type: 'cli'
              name: 'fooscript'
              content: |
                         config system global
                            set timezone 04
                         end

An Example with REST API user token based authentication
----------

in the example: ``test.yml`` we are going to create a script on FortiManager:

::

   - name: Example playbook
     hosts: fortimanagers
     vars:
       # You don't need to specify the following vars if you specified them in the host file.
       # ansible_connection: httpapi
       # ansible_network_os: fortinet.fortimanager.fortimanager
       # ansible_facts_modules: setup
       # ansible_httpapi_port: 443
       # ansible_httpapi_use_ssl: true
       #
       #  Disabling TLS certificate verification is a bad idea on security point of view, 
       #  but if you use default certificates that are self-signed, you nedd to disable it.
       #  Please use valid certificates for your production environments and keep certificate validation ON.
       # ansible_httpapi_validate_certs=false
       ansible_httpapi_session_key:
         authorization: "bearer {{ api_bearer_token }}"
     tasks:
      - name: Create a script on FortiManager.
        fortinet.fortimanager.fmgr_dvmdb_script:
           adom: 'adom'
           state: 'present'
           dvmdb_script:
              desc: 'The script create via Ansible'
              type: 'cli'
              name: 'fooscript'
              content: |
                         config system global
                            set timezone 04
                         end

Parameter Usages
----------------

there are several mandatory options in the example:

-  **adom** : ``adom`` is the administrative domain that an API is going to run inside. In most cases, ``global`` or ``root`` is what you need.
-  **state** : ``state`` is indicating the action the module is going to take. by giving ``present``, the module will create or update the object, while ``absent`` tells the module to delete the object in the FortiManager.
-  other module specific parameters are defined differently, you can find their usages in each `module page`_.

.. _module page: modules.html

Run the playbook
~~~~~~~~~~~~~~~~

::

   ansible-playbook -i hosts test.yml

you can also observe the verbose output by adding option at the tail:
``-vvv``.
