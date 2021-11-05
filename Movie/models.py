from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Movie Description')
    language = models.CharField(max_length=25)
    running_time = models.IntegerField()
    rate = models.PositiveBigIntegerField()
    release_date = models.DateTimeField()
    image=models.ImageField(upload_to='photos%y%m%d')
    active=models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True) # awl mara n3ml add bas
    modification = models.DateTimeField(auto_now=True) # kol mara by7sal edit

    def __str__(self): # to replace Movie object that appear in UI by name of the movie
        return self.name

    class Meta:
        verbose_name='Movie' #the name that appear in UI and incremented by s automatically
        ordering=['name']

class Category(models.Model):
    type=models.CharField(max_length=150)
    #rel=models.OneToManyField(Movie,on_delete=models.CASCADE)
    class Meta:
        verbose_name='Categorie'
        ordering=['type']

    def __str__(self):  # to replace Movie object that appear in UI by name of the movie
        return self.type

class Casts(models.Model):
    cast_name=models.CharField(max_length=100)
    class Meta:
        verbose_name='Cast'
    def __str__(self): # to replace Movie object that appear in UI by name of the movie
        return self.cast_name
