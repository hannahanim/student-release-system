from django.contrib import admin

# Register your models here.

from .models import Mentor,Student,Administrator,Application
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Administrator)
admin.site.register(Application)