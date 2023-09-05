from django.contrib import admin
from . models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug'] # what all should display in admin panel
    prepopulated_fields = {'slug':('name',)} # to update slug automatically when name is updated

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updates']
    list_editable = ['price','stock','available'] # can edit these things without going inside
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20 # how many item should show in one page of admin panel

admin.site.register(Product,ProductAdmin)
