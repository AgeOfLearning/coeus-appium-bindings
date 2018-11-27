import unittest
from coeus_appium.android_keycodes import AndroidKeyCodes


class AndroidKeyCodesTest(unittest.TestCase):

    @staticmethod
    def get_keycode_for_char_raises_when_not_mapped():
        AndroidKeyCodes.get_keycode_for_char('!!')

    def test_get_keycode_for_char_raises_when_not_mapped(self):
        self.assertRaises(Exception, self.get_keycode_for_char_raises_when_not_mapped)
