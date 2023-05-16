from django.shortcuts import render
from property.models import Neighborhood,PriceRange,PropertyType,MyProfile

# Create your views here.
def home(request):
    myfile =MyProfile.objects.all()
    neigs = Neighborhood.objects.all()
    price_ranges = PriceRange.objects.all()
    properties_type = PropertyType.objects.all() 
    context = {
        'neighborhoods': neigs,
        'price_ranges': price_ranges, 
        'properties_types': price_ranges
    }

    return render(request,'base.html',context)

