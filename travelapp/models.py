from django.db import models

# Create your models here.
class place (models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    Hotel_type = models.CharField(max_length=100,null=True)
    Number_of_days = models.IntegerField(null=True)
    Number_of_nights = models.IntegerField(null=True)
    Number_of_activities = models.IntegerField(null=True)
    flight_ticket = models.CharField(max_length=100,null=True)
    Arrival = models.CharField(max_length=100,null=True)
    Departure = models.CharField(max_length=100,null=True)
    guided_visit = models.CharField(max_length=100,null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
      return self.name


class Packages(models.Model):
    image=models.ImageField(upload_to='package/%D/%M/%Y')
    Date=models.DateField(auto_now=False)
    package_name=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    package_desc=models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package_name

class Testimonials(models.Model):
    Name = models.CharField(max_length=100)
    Text = models.TextField()
    Designation = models.CharField(max_length=100)


