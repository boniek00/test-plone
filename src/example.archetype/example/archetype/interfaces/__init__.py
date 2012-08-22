from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IInstantMessage(Interface):
    """
    Interface for the InstantMessage class.
    """


class IInstantMessageSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer for this product.
    """
