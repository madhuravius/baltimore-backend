# -*- coding: utf-8 -*-
"""
Tests for publicsafety app
"""

from django.test import SimpleTestCase


class ViewTests(SimpleTestCase):
    """
    Testing views
    """
    databases = '__all__'
    @classmethod
    def setUpClass(cls):
        super(ViewTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ViewTests, cls).tearDownClass()

    def test_home_view(self):
        """
        Test api root url
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_public_safety_emergency_police_calls(self):
        """
        Test api - emergencypolicecalls
        """
        response = self.client.get('/api/v1/publicsafety/emergencypolicecalls/')
        self.assertEqual(response.status_code, 200)


    def test_public_safety_emergency_arrests(self):
        """
        Test api - arrests
        """
        response = self.client.get('/api/v1/publicsafety/arrests/')
        self.assertEqual(response.status_code, 200)
