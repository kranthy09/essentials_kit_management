# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_app.models.models \
    import UserInfo


admin.site.register(UserInfo, UserAdmin)