
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class snacksTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        actual_status_code = self.client.get(url).status_code
        expected_status_code = 200
        self.assertEqual(actual_status_code, expected_status_code)
    def test_about_page_status_code(self):
        url = reverse('about')
        actual_status_code = self.client.get(url).status_code
        expected_status_code = 200
        self.assertEqual(actual_status_code, expected_status_code)        
   
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)


    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        actual = 'about.html'
        self.assertTemplateUsed(response, actual)