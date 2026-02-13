from django.db import models

# Data models for the app.
#
# Student is used by:
# - Django admin (for create/update/delete through /admin/)
# - Any custom views that query Student via ORM

class Student(models.Model):
    """Represents one student record in the database."""

    # Drop-down choices shown in forms/admin for branch field.
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]

    # Primary key entered manually (example: 101).
    roll_no = models.IntegerField(primary_key=True)
    # Unique email per student.
    email = models.EmailField(unique=True)
    # Optional photo upload. Files are saved under media/photos/.
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    # Full name of student.
    name = models.CharField(max_length=200)
    # Stored code from BRANCH_CHOICES (e.g., 'CSE').
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)

    def __str__(self):
        # Readable label in Django admin and shell.
        return f"{self.name} ({self.roll_no}) - {self.branch}"