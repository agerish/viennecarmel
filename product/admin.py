from django.contrib import admin
from product import models

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('name','price','description')


admin.site.register(models.Product,AdminProduct)
admin.site.register(models.Produc)
admin.site.register(models.Essaie)
