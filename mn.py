from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.clean import cleanup
from functools import partial
from mininet.cli import CLI

switches = []
hosts = []
server = '127.0.0.1'
port = 6653


class Topology(Topo):
    def build( self, *args, **params ):
        global hosts,switches
        hosts = [self.addHost('h%d' % (n + 1) )for n in range(5)]
        switches = [self.addSwitch('s%d' % (n + 1) ) for n in range(2)]

        for i in range(4):
            self.addLink(hosts[i],switches[0])

        self.addLink(hosts[4],switches[1])
        self.addLink(switches[0],switches[1])

class Simulator:
    def __init__(self):
        global server,port
        topo = Topology()
        self.mn = Mininet(
            topo=topo,
            controller=partial(RemoteController, ip=server, port=port)
        )

    def cli(self):
        CLI(self.mn)
    def start(self):
        self.mn.start()
    def stop(self):
        self.mn.stop()

if __name__ == '__main__':
    setLogLevel('info')
    cleanup()
    simulator = Simulator()
    simulator.start()
    simulator.cli()
    simulator.stop()