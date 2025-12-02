from django.contrib import admin
from App.models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id',"name","age","gender","phone","email","course","join_date","address","about"]

admin.site.register(Student,StudentAdmin)    