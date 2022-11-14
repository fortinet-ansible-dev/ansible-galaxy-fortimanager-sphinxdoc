Version Mismatch Notes
====================================


When running with ``unified`` FortiManager Galaxy collections, you probably see a warning if some of the attributes are not for the remote fortimanager targets:

::

    [WARNING]: Ansible has detected version mismatch between FortiManager and your playbook, see more details by appending option -vvv


by appending ``-vvv`` option onto the ansible-playbook command, you will see ``version_check_warning`` in the verbose output, one example is as below:

.. code-block:: shell

    "version_check_warning": {
        "mismatches": [
            "param: system_global-->private-data-encryption not supported until in v6.2.5",
            "param: system_global-->per-policy-lock not supported until in v6.4.0",
            "param: system_global-->object-revision-status not supported until in v7.0.0"
        ],
        "system_version": "v6.0.0"
    }


In the above `fmgr_system_global <docgen/fmgr_system_global.html>`__ example, you are reminded that ``private-data-encryption``, ``per-policy-lock`` and 
``object-revision-status`` are not available with FMG ``v6.0.0``. to avoid failure, they must be removed.


