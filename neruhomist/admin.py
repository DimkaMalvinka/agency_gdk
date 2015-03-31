from django.contrib import admin
from neruhomist.models import *


class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    inlines = [ HouseImageInline, ]

admin.site.register(House, HouseAdmin)
admin.site.register(HouseType)
admin.site.register(SellType)