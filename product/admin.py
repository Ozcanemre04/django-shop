from django.contrib import admin
from product.models import Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ProductResource(resources.ModelResource):
   class Meta:
      model = Product
      
class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
   resource_class = ProductResource
   search_fields = ('title',)
   list_display=['id','title','category','price']
   list_filter = ('category',)

admin.site.register(Product,ProductAdmin)