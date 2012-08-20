from zope.interface import Interface

class IChannel(Interface):
    """A channel through which a message could be transmitted
    """
    
    def transmit(source, destination, message):
        """Transmit a message between two destinations
        """

