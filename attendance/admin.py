from django.contrib import admin
from attendance.models import OfficeDay

class OfficeDayAdmin(admin.ModelAdmin):
    list_display = ('user','day','paid',)
    list_filter = ('user','paid',)

admin.site.register(OfficeDay, OfficeDayAdmin)