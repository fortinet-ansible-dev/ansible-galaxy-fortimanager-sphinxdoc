
Frequently Asked Questions (FAQ)
================================

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


