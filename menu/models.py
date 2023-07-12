from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Menu(models.Model):
    category=models.ForeignKey(Category, related_name='menu_category', on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=3000)
    image=models.ImageField(upload_to='menu')
    price=models.FloatField()
    
    def __str__(self):
        return self.name