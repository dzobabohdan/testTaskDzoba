from django.test import TestCase
from django.utils import timezone
from .models import Plant
from rest_framework.test import APIClient


class PlantWateringTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.plant = Plant.objects.create(
            name="Sunflower",
            species="Helianthus annuus",
            watering_frequency_days=7.0,
            last_watered_date=timezone.now().date()
        )

    def test_update_last_watered_date(self):
        response = self.client.post(f'/api/plants/{self.plant.id}')
        self.plant.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.plant.last_watered_date, timezone.now().date())
        self.assertEqual(self.plant.watering_frequency_days, 0.0)