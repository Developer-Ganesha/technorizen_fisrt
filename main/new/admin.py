from django.contrib import admin
from new.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    list_display = ['id', 'name', 'mobile', 'email', 'password']
    list_filter = ['name', 'password']

    fieldsets = (
        ('User Info', {'fields': ('username', 'email')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}), 
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'name', 'mobile', 'password'),
            },
        ),
    )

    search_fields = ['email']
    ordering = ('email', 'id')
    filter_horizontal = ()

admin.site.register(User, UserModelAdmin)
