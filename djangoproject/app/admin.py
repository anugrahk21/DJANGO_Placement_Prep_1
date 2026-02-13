from django.contrib import admin
from .models import Student

# Registers Student model with Django admin using a custom admin class.
# This is why you can create/edit Student rows from /admin/.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Columns shown in the Student list page inside admin.
    # Example row view: 101 | a@x.com | <photo> | Anu | CSE
    list_display = ('roll_no', 'email', 'photo', 'name', 'branch')
    

