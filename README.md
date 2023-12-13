# Teacher-Student Collaboration Web App

## Overview

The Teacher-Student Collaboration Web App is a Django-based web application designed to facilitate communication and collaboration between teachers, students, and parents. It allows teachers to manage classes, input grades, track attendance, and communicate with parents. Parents can access their child's academic information, receive updates, and communicate with teachers.

## Features

- User authentication for teachers and parents.
- Class management with class schedules.
- Attendance tracking for students.
- Grade input and tracking for assignments and exams.
- Communication tools such as announcements and messaging.
- Profile management for teachers and students.
- ...

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- Pipenv (optional but recommended)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/ravichandran202/SchoolApp
    cd Schoolapp
    ```

2. Install dependencies:

    ```bash
    pipenv install
    ```

    If you don't use Pipenv, you can install dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application at `http://localhost:8000` in your web browser.

7. Log in with the superuser account to access the admin interface at `http://localhost:8000/admin`.

## Usage

- Log in as a teacher or parent to access the relevant features.
- Teachers can create classes, manage student profiles, input grades, and communicate with parents.
- Parents can view their child's academic information, receive updates, and communicate with teachers.

## Acknowledgments

- Thanks to the Django community for providing a powerful web framework.

