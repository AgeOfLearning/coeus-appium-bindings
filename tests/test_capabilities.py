import unittest
import coeus_appium.capabilities


class CapabilitiesTestCase(unittest.TestCase):
    @staticmethod
    def get_capabilities_when_none_platform():
        return coeus_appium.capabilities.get_capabilities(None)

    def test_android_capabilities_not_none(self):
        result = coeus_appium.capabilities.get_android_capabilities()
        self.assertTrue(isinstance(result, dict))

    def test_ios_capabilities_not_node(self):
        result = coeus_appium.capabilities.get_ios_capabilities()
        self.assertTrue(isinstance(result, dict))

    def test_capabilities_when_none_platform(self):
        self.assertRaises(ValueError, self.get_capabilities_when_none_platform)