from django.db import models

# Create your models here.
class Publication(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering=('title',)

class Article(models.Model):
    headline=models.CharField(max_length=300)
    publications=models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
    

    class Meta:
        ordering=('headline',)

class Reporter(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()

    def __str__(self):
        return self.first_name
    
class News(models.Model):
    headline=models.CharField(max_length=100)
    pub_date=models.DateField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering=('headline',)

class Place(models.Model):
    name=models.CharField(max_length=30)
    adress=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
    serves_veg_foods=models.BooleanField(default=True)
    serves_nonveg_ffods=models.BooleanField(default=False)
    
    def __str__(self):
        return self.place.name
    
    
