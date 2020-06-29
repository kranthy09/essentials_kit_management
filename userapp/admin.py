from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from django.contrib.auth.admin import UserAdmin
from userapp.models.models import User

admin.site.register(User, UserAdmin)
>>>>>>> essen/factories
