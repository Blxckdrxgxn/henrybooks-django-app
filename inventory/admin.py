from django.contrib import admin
from .models import Book, Branch, Inventory
# Register your models here.
admin.site.register(Book)
admin.site.register(Branch)
admin.site.register(Inventory)
