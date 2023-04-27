from django.contrib import admin
from .models import LeaveRequest

class LeaveRequestAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'status', 'from_date', 'to_date', 'from_hour', 'to_hour', 'details', 'reviewed_by', 'review_date']
    list_display_links=['user', 'reviewed_by']
    search_fields=['user', 'status']

admin.site.register(LeaveRequest, LeaveRequestAdmin)