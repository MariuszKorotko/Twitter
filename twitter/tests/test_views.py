from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from twitter.views import IndexView


class IndexViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        request = self.factory.get(reverse('twitter:index'))
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)
