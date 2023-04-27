from django.contrib import admin
from companies.models import Company, ConfirmationCode, Role

class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']

class ConfirmationCodeInLine(admin.TabularInline):
    model = ConfirmationCode

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'description']
    inlines = [ConfirmationCodeInLine]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Role, RoleAdmin)
