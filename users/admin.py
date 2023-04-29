from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_superuser', 'persons_id', 'is_active', 'is_staff', 'is_verified')
    list_filter = ('email', 'persons_id', 'is_superuser', 'is_active', 'is_staff', 'is_verified')
    search_fields = ('email', 'persons_id',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {'fields': ('email', 'password', 'persons_id', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_verified',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'persons_id', 'is_staff', 'is_active',
                       'is_superuser', 'first_name', 'last_name')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
