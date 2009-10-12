from django.contrib import admin
from attendance.models import OfficeDay

def pay(modeladmin, request, queryset):
    queryset.update(paid=True)
pay.short_description = "Mark as paid"


def unpay(modeladmin, request, queryset):
    queryset.update(paid=False)
unpay.short_description = "Mark as unpaid"


class OfficeDayAdmin(admin.ModelAdmin):
    list_display = ('user','day','paid',)
    list_display_links = ('user', 'day',)
    list_filter = ('user','paid',)
    actions = [pay,unpay]

admin.site.register(OfficeDay, OfficeDayAdmin)
