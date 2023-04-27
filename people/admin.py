from django.contrib import admin
from .models import Person
from users.models import CustomUser

class PersonAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user', 'user_first_name', 'user_last_name', 'gender', 'company', 'job_title', 'phone_no', 'balance']
    #list_display = ['user', 'gender', 'company', 'job_title', 'phone_no', 'balance']

    list_display_links = []
    search_fields = ['user', 'company', 'job_title']

    def user_id(self, obj):
        return obj.user.id
    user_id.short_description = 'user_id'


    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'first_name'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'last_name'

admin.site.register(CustomUser)
admin.site.register(Person, PersonAdmin)