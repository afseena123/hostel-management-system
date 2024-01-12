from django.contrib import admin
from . models import Hostel
from . models import RoomType
from . models import Block
from . models import Room
from . models import BedDetails
# Register your models here
admin.site.register(Hostel)
admin.site.register(RoomType)
admin.site.register(Block)
admin.site.register(Room)
admin.site.register(BedDetails)
# admin.py
from django.contrib import admin
from .models import HostelDetail

@admin.register(HostelDetail)
class HostelAdmin(admin.ModelAdmin):
    list_display = ['hostelname', 'address', 'district']
    list_filter = ['district']  # Add filtering by district in the admin panel
    search_fields = ['hostelname', 'address', 'district']  # Add search by district

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['district_choices'] = Hosteldetail.DistrictChoices.choices
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
