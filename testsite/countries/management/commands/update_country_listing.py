import requests
from countries.models import Country, Region
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Loads country data from a Google Cloud Storage bucket"

    URL = "https://storage.googleapis.com/dcr-django-test/countries.json"

    def get_data(self):
        """Fetches country data from the specified URL"""
        res = requests.get(self.URL)
        res.raise_for_status()
        data = res.json()
        return data

    def handle(self, *args, **options):
        """Main command handler to load country data"""
        data = self.get_data()
        for row in data:
            region, region_created = Region.objects.get_or_create(name=row["region"])
            if region_created:
                self.stdout.write(
                    self.style.SUCCESS("Region: {} - Created".format(region))
                )
            country, country_created = Country.objects.get_or_create(
                name=row["name"],
                defaults={
                    "alpha2Code": row["alpha2Code"],
                    "alpha3Code": row["alpha3Code"],
                    "population": row["population"],
                    "topLevelDomain": row["topLevelDomain"],
                    "region": region,
                },
            )

            self.stdout.write(
                self.style.SUCCESS(
                    "{} - {}".format(
                        country, "Created" if country_created else "Updated"
                    )
                )
            )
