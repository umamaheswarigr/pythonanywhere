from django.shortcuts import render
from .models import PropertyList

def properties(request):
    if request.method =='GET':
        data = request.GET
        pr = data('price_range');
        pt = data('property_type');
        nh = data('neighborhood');
        pa = data('availability');

        properties = PropertyList.objects.filter(propert__pr=pr,propert__property_type=pt,propert__neighbhorhood=nh,propert__availability=pa)#propert__availability=pa

        data = {
            'properties': properties
        }

        return render(request, "properties.html", data)
