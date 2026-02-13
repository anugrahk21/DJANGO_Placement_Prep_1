from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.models import Student

def home(request):
    """Render landing page.

    URL: /
    Template: Templates/index.html
    """
    return render(request,"index.html")

def login(request):
    """Render login page UI only.

    Note: this view currently does not authenticate users.
    URL: /login/
    Template: Templates/login.html
    """
    return render(request,"login.html")

def input_data(request):
    """Render form page used to input student data.

    URL: /input/
    Template: Templates/input.html
    """
    if request.method == "POST":
         # 1. Get text data and file data from the submitted form.
        roll_no = request.POST.get('roll_no')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')  # For file uploads, use request.FILES
        name = request.POST.get('name')
        branch = request.POST.get('branch')

        # 2. Create a new Student object and save it to the database.
        student = Student(roll_no=roll_no, email=email, photo=photo, name=name, branch=branch)
        student.save()

        # 3. After saving, you can redirect to another page or show a success message.
        #return HttpResponse("Student data submitted successfully!")
        return redirect('input_data')  # Redirect to the same page to show the form again (you can change this to redirect elsewhere if needed).

    # If GET request(viewing the page), just show the empty form. 
    return render(request,"input.html")

def student_data(request):
    """Show all students stored in the database.

    Data source:
    - Reads from app.models.Student via Django ORM.
    - Student entries can be added through Django admin (/admin/).
    URL: /student/
    Template: Templates/student.html
    """
    students = Student.objects.all()
    return render(request,'student.html', {'students': students})