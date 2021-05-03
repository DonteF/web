from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipes(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    video = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='recipe/images', default='Null')

class SavedRecipe(models.Model):
    userid= models.ForeignKey(User, on_delete=models.CASCADE)
    recipeid = models.ForeignKey(Recipes, on_delete=models.CASCADE)

