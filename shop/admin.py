from django.contrib import admin
from .models import categ,product
# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name','price','category','stock','avilability']
    list_editable = ['price','stock','avilability']

admin.site.register(product,prodadmin)
