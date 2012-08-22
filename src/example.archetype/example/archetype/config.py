"""Common configuration constants
"""
from Products.Archetypes.atapi import DisplayList

PROJECTNAME = 'example.archetype'


MESSAGE_PRIORITIES = DisplayList((
    ('high', 'High Priority'),
    ('normal', 'Normal Priority'),
    ('low', 'Low Priority'),
    ))

ADD_CONTENT_PERMISSIONS = {
    'InstantMessage': 'example.archetype: Add InstantMessage',
}

ADD_PERMISSIONS = {
    # -*- extra stuff goes here -*-
}
