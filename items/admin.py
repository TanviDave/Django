from django.contrib import admin
from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    pass


class BidAdmin(admin.ModelAdmin):
    pass


class WinnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bid, BidAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Winners, ItemAdmin)
