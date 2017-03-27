from django.test import TestCase
from django.urls import reverse

from .models import Champion


class ChampionViewTests(TestCase):
    def test_info_view_with_no_champion(self):
#        response = self.client.get(reverse('lol_champion_info:'))
        response = self.client.get('/lol_champion_info')
        self.assertEqual(response.status_code, 301)
#        self.assertContains(response, "All champions seem to have a vacation together!", status_code=301)
        self.assertContains(response, "500", status_code=301)
#        self.assertQuerysetEqual(response.context['table'], [])
