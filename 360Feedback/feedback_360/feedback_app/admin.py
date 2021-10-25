from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# class RealUserAdmin(UserAdmin):
#     pass

# admin.site.register(RealUser, RealUserAdmin)

from feedback_app.models import Duser
from django.contrib.auth.models import User

class DuserInline(admin.StackedInline):
    model = Duser
    can_delete = False
    verbose_name_plural= 'Dusers'

class CustomizedUserAdmin (UserAdmin):
    inlines=(DuserInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin )

admin.site.register(Duser)