from django.contrib import admin
from cp.models import UserData, SPOJ, CodeForces

# Register your models here.
admin.site.register(UserData)
admin.site.register(SPOJ)
admin.site.register(CodeForces)
