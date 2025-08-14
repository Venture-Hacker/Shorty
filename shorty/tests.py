from django.test import TestCase
from django.urls import reverse
from .models import Link

class ShortenerTests(TestCase):
    def test_create_and_redirect(self):
        # Create
        r = self.client.post("/", data={"original_url": "https://example.com/path"})
        self.assertEqual(r.status_code, 302)  # redirect to detail
        link = Link.objects.first()
        self.assertTrue(link.code)

        # Resolve
        go_url = reverse("shorty:go", args=[link.code])
        r2 = self.client.get(go_url)
        self.assertEqual(r2.status_code, 302)
        self.assertEqual(r2["Location"], "https://example.com/path")
