
Search Playbooks
==============================

This document contains some handy example playbooks.
PRs are welcome ``https://github.com/fortinet-ansible-dev/fortimanager-playbook-example``

.. raw:: html

 <div>
 <div class="line-block">
 <div class="line"><br /></div>
 </div>
 <input id="myInput" type="text" placeholder="Search..">
 <br>
 <table border="1" class="docutils">
 <thead valign="bottom">
 <tr class="row-odd">
 <th class="head">File Name</th>
 <th class="head">Description</th>
 <th class="head">Author</th>
 <th class="head">Date</th>
 <th class="head">Labels</th>
 </tr>
 </thead>
 <tbody id="myTable" valign="top">
 <!-- DON'T EDIT ANYTHING ABOVE THIS LINE -->

 <tr class="row-even"><td><a target="_blank" href="https://raw.githubusercontent.com/fortinet-ansible-dev/fortimanager-playbook-example/2.0.0/output/commit_config_to_device.yml">commit_config_to_device.yml</a></td>
 <td><code ><span>Commit all config in local database to device</span></code></td>
 <td><code ><span class="pre">Link Zheng<b>(Fortinet)</b></span></code></td>
 <td><code ><span class="pre">2020.09.21</span></code></td>
 <td><code class="docutils literal notranslate"><span class="pre">install</span></code><code class="docutils literal notranslate"><span class="pre">config</span></code></td>
 </tr>
 <tr class="row-odd"><td><a target="_blank" href="https://raw.githubusercontent.com/fortinet-ansible-dev/fortimanager-playbook-example/2.0.0/output/delete_device.yml">delete_device.yml</a></td>
 <td><code ><span>Remove a FGT device to FMG</span></code></td>
 <td><code ><span class="pre">Link Zheng<b>(Fortinet)</b></span></code></td>
 <td><code ><span class="pre">2020.09.21</span></code></td>
 <td><code class="docutils literal notranslate"><span class="pre">device</span></code><code class="docutils literal notranslate"><span class="pre">cmd</span></code><code class="docutils literal notranslate"><span class="pre">delete</span></code></td>
 </tr>
 <tr class="row-even"><td><a target="_blank" href="https://raw.githubusercontent.com/fortinet-ansible-dev/fortimanager-playbook-example/2.0.0/output/discover_and_add_device.yml">discover_and_add_device.yml</a></td>
 <td><code ><span>Add a FGT device to FMG</span></code></td>
 <td><code ><span class="pre">Link Zheng<b>(Fortinet)</b></span></code></td>
 <td><code ><span class="pre">2020.09.11</span></code></td>
 <td><code class="docutils literal notranslate"><span class="pre">device</span></code><code class="docutils literal notranslate"><span class="pre">cmd</span></code></td>
 </tr>
 <tr class="row-odd"><td><a target="_blank" href="https://raw.githubusercontent.com/fortinet-ansible-dev/fortimanager-playbook-example/2.0.0/output/execute_script.yml">execute_script.yml</a></td>
 <td><code ><span>Apply a script to local device database</span></code></td>
 <td><code ><span class="pre">Link Zheng<b>(Fortinet)</b></span></code></td>
 <td><code ><span class="pre">2020.09.21</span></code></td>
 <td><code class="docutils literal notranslate"><span class="pre">execute</span></code><code class="docutils literal notranslate"><span class="pre">script</span></code></td>
 </tr>
 <tr class="row-even"><td><a target="_blank" href="https://raw.githubusercontent.com/fortinet-ansible-dev/fortimanager-playbook-example/2.0.0/output/clone_objects.yml">clone_objects.yml</a></td>
 <td><code ><span>Clone an Object in FortiManager</span></code></td>
 <td><code ><span class="pre">Link Zheng<b>(Fortinet)</b></span></code></td>
 <td><code ><span class="pre">2020.09.11</span></code></td>
 <td><code class="docutils literal notranslate"><span class="pre">clone</span></code></td>
 </tr>

 <!-- DON'T EDIT ANYTHING BELOW THIS LINE --> 
 </tbody>
 </table>

 <script>
 $(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle( $(this).text().toLowerCase().indexOf(value) > -1 );
    });
  });
 });
 </script>
 </div>
