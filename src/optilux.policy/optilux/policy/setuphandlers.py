from Products.CMFCore.utils import getToolByName


def setupGroups(portal):
    acl_users = getToolByName(portal, 'acl_users')
    print "setupGroups"
    if not acl_users.searchGroups(name='Staff'):
        print "adding Staff group"
        gtool = getToolByName(portal, 'portal_groups')
        gtool.addGroup('Staff', roles=['StaffMember'])


def importVarious(context):
    """Miscellanous steps import handle
    """
    print "importVarious"
    if context.readDataFile('optilux.policy-various.txt') is None:
        return
    portal = context.getSite()
    setupGroups(portal)
