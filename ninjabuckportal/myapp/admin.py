from django.contrib import admin
from .models import Student
# Register your models here.

#changes the header
admin.site.site_header = "Welcome, Sensei!"
#changes the title
admin.site.site_title = "Your Ninjabuck Portal"
#changes the index title
admin.site.index_title = "Welcome to the Ninjabuck Portal Manager"

class StudentAdmin(admin.ModelAdmin):
    search_fields = ["first_name"]

admin.site.register(Student, StudentAdmin)
