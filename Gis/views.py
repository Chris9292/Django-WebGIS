from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

# get user location
# latitude = 22.9451282
# longtitude = 40.6427709
# user_location = Point(longtitude, latitude, srid=4326)


# Create your views here.
class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    # optional : query based on distance from user
    # queryset = Shop.objects.annotate(distance=Distance("location", user_location)).order_by("distance")
    template_name = "index.html"
