from django.contrib import admin
from .models import Student_Management
# Register your models here.
class Student_Management_Admin(admin.ModelAdmin):
    list_display = ('Student_Adm','first_name','last_name','email','field_of_study','year','image')

admin.site.register(Student_Management,Student_Management_Admin)