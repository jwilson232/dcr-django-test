from countries.models import Country
from django.db.models import Count, F, Sum
from django.http import JsonResponse


def stats(request):
    """Get statistics about countries by region"""

    regions = (
        Country.objects.values(region_name=F("region__name"))
        .annotate(number_countries=Count("id"), total_population=Sum("population"))
        .order_by("region__name")
    )

    return JsonResponse({"regions": list(regions)})
