from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('starter','starter'),
    ('breakfast','breakfast'),
    ('lunch','lunch'),
    ('dinner','dinner'),
)
class Menu(models.Model):
    category=models.CharField(max_length=10 , choices=CATEGORY_CHOICES)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=3000)
    image=models.ImageField(upload_to='menu')
    price=models.FloatField()
    def __str__(self):
        return self.name