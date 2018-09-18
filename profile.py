"""This is a trivial example of a gitrepo-based profile; The profile source code and other software, documentation, etc. are stored in in a publicly accessible GIT repository (say, github.com). When you instantiate this profile, the repository is cloned to all of the nodes in your experiment, to `/local/repository`. 

This particular profile is a simple example of using a single raw PC. It can be instantiated on any cluster; the node will boot the default operating system, which is typically a recent version of Ubuntu.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.

node1 = request.XenVM("node-1")

node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node1.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))
node1.routable_control_ip = "true"

iface1 = node1.addInterface("if1")
iface1.component_id = "eth1"
iface1.addAddress(pg.IPv4Address("192.168.1.1", "255.255.255.0"))

node2 = request.XenVM("node-2")

node2.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))
node2.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"

iface2 = node2.addInterface("if2")
iface2.component_id = "eth2"
iface2.addAddress(pg.IPv4Address("192.168.1.2", "255.255.255.0"))

link = request.LAN("lan")

link.addInterface(iface1)
link.addInterface(iface2)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
