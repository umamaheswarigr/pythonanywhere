from django.contrib import admin


from .models import *

admin.site.register(PriceRange)
admin.site.register(PropertyType)
admin.site.register(Neighborhood)
admin.site.register(Property_search)
admin.site.register(PropertyList)
admin.site.register(MyProfile)
admin.site.register(PropertyAvailability)


