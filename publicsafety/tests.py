# -*- coding: utf-8 -*-
"""
Tests for publicsafety app
"""

from django.test import SimpleTestCase


class ViewTests(SimpleTestCase):
    """
    Testing views
    """

    def test_home_view(self):
        """
        Test api root url
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
