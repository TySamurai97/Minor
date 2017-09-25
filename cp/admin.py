from django.contrib import admin
from cp.models import UserData, CodeChef, SPOJ, CodeForces, UserHandle, Questions

# Register your models here.
admin.site.register(UserData)
admin.site.register(CodeChef)
admin.site.register(SPOJ)
admin.site.register(CodeForces)
admin.site.register(UserHandle)
admin.site.register(Questions)