# 🎓 Student Management System (Django)

Welcome to the **Student Management System**! This is a simple yet powerful Django web application designed to streamline the management of student records. It allows users to easily input details, manage profiles, and view a comprehensive list of registered students.

---

## ✨ Features

- 📝 **Student Registration**: A user-friendly form to input and save student details (Roll No, Name, Email, Branch, etc.).
- 📋 **Data Listing**: dynamically view a list of all registered students in real-time.
- 📷 **Image Handling**: Seamless support for uploading and displaying student profile photos.
- ⚙️ **Admin Panel**: Fully functional Django admin interface for advanced data management at `/admin`.
- 📱 **Responsive Design**: Clean HTML structure ready for custom styling and mobile responsiveness.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your machine:

- 🐍 **Python 3.x**
- 🌐 **Django** (`pip install django`)
- 🖼️ **Pillow** (`pip install pillow`) - Required for handling image uploads.

---

## 🚀 Installation & Setup

Follow these steps to get the project running locally:

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/anugrahk21/DJANGO_Placement_Prep_1.git
cd DJANGO
```

### 2. 🏗️ Create a Virtual Environment (Recommended)
It's best practice to isolate your dependencies.
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. 📦 Install Dependencies
```bash
pip install django pillow
```

### 4. 📂 Navigate to Project Directory
The main Django project lives in the subdirectory.
```bash
cd djangoproject
```

### 5. 🗄️ Database Migrations
Initialize the database and apply models.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 🔐 Create a Superuser (Optional)
Create an admin account to access the dashboard at `/admin`.
```bash
python manage.py createsuperuser
```

### 7. ▶️ Run the Development Server
```bash
python manage.py runserver
```

### 8. 🌐 Access the Application
Open your browser and navigate to:
- 🏠 **Home**: `http://127.0.0.1:8000/`
- ➕ **Add Student**: `http://127.0.0.1:8000/input/`
- 👥 **View Students**: `http://127.0.0.1:8000/student/`
- 🛡️ **Admin Panel**: `http://127.0.0.1:8000/admin/`

---

## 📂 Project Structure

```bash
DJANGO/
├── .git/               # 🔧 Git configuration
├── .gitignore          # 🚫 Files to ignore
├── README.md           # 📄 Project documentation
├── djangoproject/      # 🏠 Main project directory
│   ├── app/            # 🧠 Application logic (Models, Views)
│   ├── djangoproject/  # ⚙️ Project settings & core configs
│   ├── media/          # 🖼️ User-uploaded media files
│   ├── Templates/      # 🎨 HTML templates
│   ├── db.sqlite3      # 🗄️ SQLite database
│   └── manage.py       # 🎮 Django command-line utility
```

---

## 💻 Technologies Used

- **Backend**: 🐍 Django (Python Web Framework)
- **Database**: 🗄️ SQLite (Default Django DB)
- **Frontend**: 🌐 HTML5
- **Media**: 🖼️ Pillow (Image Processing)

---

## 🤝 Contributing

Contributions are welcome! Feel free to **fork** this repository and submit **pull requests**. For major changes, please open an **issue** first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

## 📞 Contact

Ready to discuss **Web Dev** or share **interview experiences**? Let's connect!

**Anugrah K.**  
*AI & Cybersecurity Enthusiast*  

📧 [Email](mailto:anugrah.k910@gmail.com)  
🔗 [GitHub Profile](https://github.com/anugrahk21)  
💼 [LinkedIn](https://linkedin.com/in/anugrah-k)