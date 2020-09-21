from django.contrib import admin

# Register your models here.
from collisions.models import Violations_cameras, Dtp, Test

admin.register(Violations_cameras)
admin.register(Dtp)
admin.register(Test)
