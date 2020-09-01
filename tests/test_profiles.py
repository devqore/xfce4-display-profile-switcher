"""
Test assumes there are some display profiles configured in the system,
not any particular but some, otherwise expect test to fail.
"""
from xfce4_display_profile_switcher import XconfQuery, DisplayProfiles
from unittest import TestCase


class XconfQueryTests(TestCase):
    def test_get_values(self):
        xq = XconfQuery()
        display_values = xq.get_values('displays')
        self.assertIn('/ActiveProfile', display_values.keys())


class DisplayProfilesTests(TestCase):
    def test_profiles(self):
        dp = DisplayProfiles()
        profiles = dp.get_profiles()
        self.assertGreater(len(profiles.keys()), 0,
                           "Expected to find some profiles")
