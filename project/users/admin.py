from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from user_profile.models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

    
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ('name', 'phone','email','is_staff', 'is_active',)
    list_filter = ('name', 'phone','email', 'is_staff', 'is_active',)
    
    fieldsets = (
        (None, {'fields': ('phone' ,'password')}),
        ('Personal info', {'fields': ('name','email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        ('Important dates', {'fields':('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email','phone' ,'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )
    search_fields = ('phone','name', 'email')
    ordering = ('phone',)
    filter_horizontal = ()
    inlines = (ProfileInline, )

   


admin.site.register(CustomUser, CustomUserAdmin)
