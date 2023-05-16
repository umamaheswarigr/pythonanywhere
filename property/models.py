from django.db import models


class MyProfile(models.Model):
    personal_photo = models.ImageField(upload_to='uploads/% Y/% m/% d/', null=True, blank=True)  # pip install Pillow
    My_Profile = models.CharField(max_length=255)

    def __str__(self):
        return self.My_Profile

class PropertyType(models.Model):
    property_type = models.CharField(max_length=50)

    def __str__(self):
        return self.property_type

class PropertyAvailability(models.Model):
    availability = models.BooleanField(default=True)
    def __str__(self):
        return self.availability

class Neighborhood(models.Model):
    # property_Name = models.ForeignKey(Property,on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PriceRange(models.Model):
    price_range = models.CharField(max_length=50)

    def __str__(self):
        return self.price_range

class Property_search(models.Model):
    price_range = models.ForeignKey(PriceRange,on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    #availability = models.ForeignKey(PropertyAvailability,on_delete=models.CASCADE)#Availability
    date_searched = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

class PropertyList(models.Model):
    Property_searchs = models.ForeignKey(Property_search,on_delete=models.CASCADE)
    property_status = models.BooleanField(default=True)
    street_address = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    zip_code  = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=10, decimal_places=5)
    description = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    number_car_garage= models.IntegerField()
    fire_place = models.BooleanField(default=True)
    year_built = models.IntegerField()
    build_up_size  = models.IntegerField()
    lot_size = models.IntegerField()
    property_photo1 = models.ImageField(upload_to ='uploads/% Y/% m/% d/', null=True,blank=True) # pip install Pillow
    property_photo2 = models.ImageField(upload_to ='uploads/% Y/% m/% d/',null=True,blank=True) # pip install Pillow
    property_photo3 = models.ImageField(upload_to ='uploads/% Y/% m/% d/',null=True,blank=True) # pip install Pillow
    property_photo4 = models.ImageField(upload_to ='uploads/% Y/% m/% d/',null=True,blank=True) # pip install Pillow



