from five import grok
from optilux.policy.interfaces import IChannel
from zope.interface import implements


class Channel(object):
    grok.implements(IChannel)
    
    def __init__(self, port):
        self.port = port
    
    def transmit(self, source, destination, message):
        print "Sending", message, "from", source,\
                "to", destination, "on", self.port


http = Channel(80)
grok.global_utility(http, provides=IChannel, name="http", direct=True)
grok.global_utility(Channel(21), provides=IChannel, direct=True)
