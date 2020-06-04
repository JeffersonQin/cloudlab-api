"""This profile provides a single compute node for running `example.py`, which
programmaticaly starts an experiment based on another profile and interacts with
it using the tools in `./powder/`.

See the project README for more information.

"""

import geni.portal as portal
import geni.rspec.pg as rspec


request = portal.context.makeRequestRSpec()
node = request.RawPC('node')
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
node.addService(rspec.Execute(shell="bash", command="/local/repository/profile-startup.sh"))
portal.context.printRequestRSpec()
