from django.contrib import admin
from accounts.models import account


# Register your models here.

class userAdmin(admin.ModelAdmin):
    search_fields =('username',)
    list_display=['username','email','first_name','last_name']

admin.site.register(account,userAdmin)