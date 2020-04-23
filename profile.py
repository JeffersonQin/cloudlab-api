"""This profile provides a single compute node for running the example in
main.py, which programmaticaly starts an experiment based on another profile and
interacts with it using the tools in `./powder/`.

See the project
[README](https://gitlab.flux.utah.edu/dmaas/powder-control/-/blob/master/README.md)
for more information.

"""

import geni.portal as portal
import geni.rspec.pg as rspec


request = portal.context.makeRequestRSpec()
node = request.RawPC('control-node')
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
portal.context.printRequestRSpec()
