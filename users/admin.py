from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('-date_joined',)
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
