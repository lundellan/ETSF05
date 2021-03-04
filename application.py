# from mininet.topolib import TreeTopo
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import Node

class TopoNetwork( Topo ):
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )
        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )

        e1 = self.addSwitch( 'e1' )
        e2 = self.addSwitch( 'e2' )
        e3 = self.addSwitch( 'e3' )
        e4 = self.addSwitch( 'e4' )
        c1 = self.addSwitch( 'c1' )

        # Add links
        self.addLink( h1, e4, bw=5, delay='1ms' )
        self.addLink( h2, e1, bw=5, delay='1ms' )
        self.addLink( h3, e2, bw=5, delay='1ms' )
        self.addLink( h4, e3, bw=5, delay='1ms' )
        self.addLink( h5, e3, bw=5, delay='1ms' )

        self.addLink( c1, e4, bw=3, delay='10ms' )
        self.addLink( c1, e1, bw=3, delay='10ms' )
        self.addLink( c1, e2, bw=3, delay='10ms' )
        self.addLink( c1, e3, bw=3, delay='10ms' )
        
def perftest():
        "create network and run simple performance test"
        topo = TopoNetwork()
        net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink )
        net.start()
        print "Dumping host connections "
        dumpNodeConnections( net.hosts )
        print " Testing Network connectivity"
        net.pingAll()
        print "Testing BW between hosts"
        h1, h2 = net.get( 'h1', 'h2' ) 
        h3 = net.get( 'h3' )
        h4 = net.get( 'h4' ) 
        h5 = net.get( 'h5' )
        CLI(net)
        #net.iperf( (h1, h4), l4Type='UDP', udpBw='1', seconds=10 ) 
        #net.iperf( (h1, h2), l4Type='UDP', udpBw='1', seconds=10 ) 
        #net.iperf( (h1, h3), l4Type='UDP', udpBw='1', seconds=10 ) 
        print "Measure roundtrip time from h5 to h1 and h2"
        #net.pingFull((h5, h1)) 
        #net.pingFull((h5, h2)) 
        print "Measure the available BW between H5, h1 and h5 , h2 using iperf"
        
        
        net.stop()

topos ={ 'TopoNetwork': ( lambda: TopoNetwork() ) }
if __name__ == '__main__':
    setLogLevel( 'info' )
    perftest()