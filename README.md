# Student Management System (Django)

This is a simple Django web application designed to manage and store student records. It allows users to input student details (Roll No, Name, Email, Branch, and Photo) and view the list of registered students.

## Features

- **Student Registration**: A form to input and save student details.
- **Data Listing**: View a list of all registered students.
- **Image Handling**: Support for uploading and displaying student photos.
- **Admin Panel**: Built-in Django admin interface for advanced data management at `/admin`.
- **Responsive Design**: Basic HTML structure (can be extended with custom CSS).

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **Django** (`pip install django`)
- **Pillow** (`pip install pillow`) - Required for handling image uploads.

## Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/anugrahk21/DJANGO_Placement_Prep_1.git
    cd DJANGO
    ```

2.  **Create a Virtual Environment (Recommended)**
    It's best practice to create a virtual environment in the project root.
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install django pillow
    ```

4.  **Navigate to Project Directory**
    The Django project is located in the `djangoproject` subdirectory.
    ```bash
    cd djangoproject
    ```

5.  **Database Migrations**
    If this is the first time running the project or if models have changed:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a Superuser (Optional)**
    To access the admin panel at `/admin`:
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

8.  **Access the Application**
    Open your browser and navigate to:
    - **Home**: `http://127.0.0.1:8000/`
    - **Add Student**: `http://127.0.0.1:8000/input/`
    - **View Students**: `http://127.0.0.1:8000/student/`
    - **Admin Panel**: `http://127.0.0.1:8000/admin/`

## Project Structure

```
DJANGO/
├── .git/               # Git configuration
├── .gitignore          # Files to ignore in Git
├── README.md           # Project documentation
├── djangoproject/      # Main project directory
│   ├── app/            # Main application logic (Models, migrations)
│   ├── djangoproject/  # Project settings and core configurations
│   ├── media/          # Directory for storing user-uploaded media files
│   ├── Templates/      # HTML templates
│   ├── db.sqlite3      # SQLite database file
│   └── manage.py       # Django command-line utility
```

## Technologies Used

-   **Backend**: Django (Python Web Framework)
-   **Database**: SQLite (Default Django DB)
-   **Frontend**: HTML5
-   **Media Handling**: Django FileField/ImageField with Pillow

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## 📞 Contact

Ready to discuss Web Dev or share interview experiences? Let's connect!

**Anugrah K.**  
AI & Cybersecurity Enthusiast  
📧 [Email](mailto:anugrah.k910@gmail.com)  
🔗 [GitHub Profile](https://github.com/anugrahk21)  
💼 [LinkedIn](https://linkedin.com/in/anugrah-k)