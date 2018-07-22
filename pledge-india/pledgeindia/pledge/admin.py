from django.contrib import admin

from .models import Pledge, UserPledges

# Register your models here.

admin.site.register(Pledge)
admin.site.register(UserPledges)
