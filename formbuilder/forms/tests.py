from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from .models import Form

class FormAPITest(APITestCase):
    def test_create_form(self):
        data = {
            "title": "Sample Form",
            "fields": [{"label": "Name", "field_type": "text", "required": True, "order": 1}]
        }
        response = self.client.post('/api/forms/', data, format='json')
        self.assertEqual(response.status_code, 201)