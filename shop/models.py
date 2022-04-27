from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class categ(models.Model):

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    def get_url(self):
        return reverse('myapp:petshop1',args=[self.slug])
    def __str__(self):
        return self.name



class product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    stock = models.IntegerField()
    avilability = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(categ, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('myapp:detail',args=[self.category.slug, self.slug])
