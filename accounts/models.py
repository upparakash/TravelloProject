from django.db import models

# Create your models here.
class searching (models.Model):
    city_search=models.CharField(max_length=100)
    departure_search=models.TextField()
    arrival_search=models.TextField()
    budget_search=models.IntegerField()

class team(models.Model):
    image= models.ImageField(upload_to='Team/%D/%M/%Y')
    Name = models.CharField(max_length=100)
    Position= models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Name


class News(models.Model):
    image = models.ImageField(upload_to='package/%D/%M/%Y')
    Date = models.DateField(auto_now=False)
    package_name = models.CharField(max_length=100)
    Company_name = models.CharField(max_length=100)
    package_desc = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package_name

class info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.TextField()
    message=models.TextField()

