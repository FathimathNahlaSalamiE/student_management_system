# 🎓 Student Management System

A web-based **Student Management System** developed using **Python and Django**. The application provides a structured platform for managing student-related information through a dynamic web interface.

This project was developed to gain practical experience in Django web development, database integration, CRUD operations, templates, static files, and media handling.

## ✨ Features

- 🎓 Student management
- ➕ Add student information
- 👀 View student details
- ✏️ Update student information
- 🗑️ Delete student records
- 🖼️ Profile picture handling
- 🗄️ Database integration using SQLite
- 🌐 Dynamic Django templates
- 🎨 Static CSS and frontend assets
- ⚙️ Django-based backend
- 📱 User-friendly web interface

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **JavaScript**
- **SQLite**
- **Django Templates**

## 📂 Project Structure

```text
student_management_system/
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── media/
│   └── profile_pic/
│
├── static/
│   └── assets/
│
├── student_management_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│
├── db.sqlite3
├── manage.py
└── README.md
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/FathimathNahlaSalamiE/student_management_system.git
```

### 2. Navigate to the project directory

```bash
cd student_management_system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

> If a `requirements.txt` file is added to the project in the future, install the dependencies using:
>
> ```bash
> pip install -r requirements.txt
> ```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open the application

Visit:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database

The project uses **SQLite** for database management.

The database file is:

```text
db.sqlite3
```

Django migrations are used to create and manage the database structure.

## 🖼️ Media Files

The project includes a `media/profile_pic` directory for storing student profile pictures.

Uploaded profile images can be displayed through the Django application using Django's media file configuration.

## 📸 Screenshots

<img width="1919" height="966" alt="Screenshot 2026-08-16 195441" src="https://github.com/user-attachments/assets/c5744519-96dc-4d85-9392-3dcdad9d8c60" />

<img width="1919" height="959" alt="Screenshot 2026-08-16 195040" src="https://github.com/user-attachments/assets/117036b2-21a3-4066-a227-a229d95f5321" />

<img width="1918" height="965" alt="Screenshot 2026-08-16 195059" src="https://github.com/user-attachments/assets/47457873-ab04-494e-8bbf-d244b66aa17f" />

## 🧠 Django Concepts Demonstrated

This project demonstrates practical knowledge of:

- Django project structure
- Django applications
- Models
- Views
- URL routing
- Django Templates
- Template inheritance
- CRUD operations
- SQLite database
- Django migrations
- Static files
- Media files
- Form handling
- Request and response handling
- Database-driven web applications
- Python backend development

## 🎯 Project Purpose

The purpose of this project was to gain hands-on experience in developing a **database-driven web application using Django**.

Through this project, I practiced building backend functionality with Python and Django while integrating templates, static resources, media files, and a relational database.

## 🔮 Future Improvements

Possible future improvements include:

- 🔐 User authentication and authorization
- 👥 Role-based access control
- 🔍 Student search and filtering
- 📊 Student dashboard
- 📈 Student performance reports
- 📄 Export student information to PDF
- 📧 Email notifications
- 🗃️ PostgreSQL database integration
- 🌐 REST API integration
- 🚀 Deployment to a cloud platform
- 📱 Improved mobile responsiveness

## 👩‍💻 Author

**Fathimath Nahla Salami E**

Python Full-Stack Developer | AI/ML Developer

### GitHub

https://github.com/FathimathNahlaSalamiE

### Project Repository

https://github.com/FathimathNahlaSalamiE/student_management_system

## 📄 License

This project was developed for educational and portfolio purposes.
