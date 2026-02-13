from django.db import models

# Create your models here.

class Student(models.Model):

    BRANCH_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]

    roll_no = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.roll_no}) - {self.branch}"