from countries.models import Country, Region
from django.test import TestCase


class StatsViewTest(TestCase):
    def setUp(self):
        europe = Region.objects.create(name="Europe")
        asia = Region.objects.create(name="Asia")

        Country.objects.create(
            name="France",
            alpha2Code="FR",
            alpha3Code="FRA",
            population=67000000,
            topLevelDomain=".fr",
            capital="Paris",
            region=europe,
        )

        Country.objects.create(
            name="Germany",
            alpha2Code="DE",
            alpha3Code="DEU",
            population=83000000,
            topLevelDomain=".de",
            capital="Berlin",
            region=europe,
        )

        Country.objects.create(
            name="Japan",
            alpha2Code="JP",
            alpha3Code="JPN",
            population=125000000,
            topLevelDomain=".jp",
            capital="Tokyo",
            region=asia,
        )

    def test_stats_view(self):
        response = self.client.get("/countries/stats/")
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn("regions", data)
        regions = data["regions"]

        self.assertEqual(len(regions), 2)

        europe = next(r for r in regions if r["region_name"] == "Europe")
        asia = next(r for r in regions if r["region_name"] == "Asia")

        self.assertEqual(europe["number_countries"], 2)
        self.assertEqual(europe["total_population"], 150000000)

        self.assertEqual(asia["number_countries"], 1)
        self.assertEqual(asia["total_population"], 125000000)
