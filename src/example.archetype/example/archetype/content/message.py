from zope.interface import implements
from Products.Archetypes import atapi
from example.archetype import archetypeMessageFactory as _

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from example.archetype.interfaces import IInstantMessage
from example.archetype import config

schema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

  atapi.StringField('priority',
              vocabulary=config.MESSAGE_PRIORITIES,
              default='normal',
              widget=atapi.SelectionWidget(label=_(u'Priority')),
             ),

  atapi.TextField('body',
            searchable=1,
            required=1,
            allowable_content_types=('text/plain',
                                       'text/structured',
                                       'text/html',),
            default_output_type='text/x-html-safe',
            widget=atapi.RichWidget(label=_(u'Message body')),
           ),
))


class InstantMessage(base.ATCTContent):
    """An Archetype for an InstantMessage application"""

    implements(IInstantMessage)
    schema = schema


atapi.registerType(InstantMessage, config.PROJECTNAME)
