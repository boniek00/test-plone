from base import InstantMessageTestCase
from example.archetype.interfaces import IInstantMessage


class TestProductInstall(InstantMessageTestCase):

    def afterSetUp(self):
        self.types = ('InstantMessage',)

    def testTypesInstalled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_types.objectIds(),
                            '%s content type not installed' % t)

    def testPortalFactoryEnabled(self):
        for t in self.types:
            self.failUnless(
                    t in self.portal.portal_factory.getFactoryTypes().keys(),
                            '%s content type not installed' % t)


class TestInstantiation(InstantMessageTestCase):

    def afterSetUp(self):
        # Adding an InstantMessage anywhere - can only be done
        #by a Manager or Portal Owner
        self.setRoles(['Manager'])
        self.portal.invokeFactory('InstantMessage', 'im1')
        self.portal.im1.setTitle('test title')

    def testCreateInstantMessage(self):
        self.failUnless('im1' in self.portal.objectIds())
        self.assertEqual('test title', self.portal.im1.title)

    def testInstantMessageInterface(self):
        im = self.portal.im1
        print im.title
        self.failUnless(IInstantMessage.providedBy(im))
