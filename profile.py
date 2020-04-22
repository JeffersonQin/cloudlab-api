"""This profile stands up a single XenVM instance for running the example in
main.py, which programmaticaly stands up another experiment and interacts with
it using the tools in `./powder/`.

See the project
[README](https://gitlab.flux.utah.edu/dmaas/powder-control/-/blob/master/README.md)
for more information.

"""

import geni.portal as portal
import geni.rspec.pg as rspec


request = portal.context.makeRequestRSpec()
node = request.XenVM('control-node')
portal.context.printRequestRSpec()
