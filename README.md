Student Management System (Django)

This project is a simple and functional Student Management System built using Django.
It allows users to add new students, view all students, update existing records, and delete students from the system. The goal of this project is to practice Django CRUD operations with a clean and easy-to-understand interface.

Features:

Displays a list of all students in a structured table

Shows complete information of a single student

Adds new student records using a ModelForm

Updates existing student details

Deletes student data after confirmation

Uses Django messages to display success and error alerts

Contains clean and simple HTML templates for all pages
--------------------------------------------------------
Model Details

Each student record stores the following information:

Name

Age

Gender

Phone

Email

Course

Join Date

Address

About
-------------------------------------
URL Routes:

/home/ – Home page

/main/ – Student list

/std/<id>/ – View student details

/add_std/ – Add a student

/update_std/<id>/ – Update a student

/delete_std/<id>/ – Delete a student
--------------------------------------------
How to Download and Run the Project

Follow these steps to set up and run the project on your system.

1. Clone the repository

Open your terminal and run:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create a virtual environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate

3. Install dependencies
pip install django

4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

5. Start the server
python manage.py runserver


Open the application in your browser:

http://127.0.0.1:8000/home/
------------------------------------------------------
Sample Output

Below are text-based samples of what the project pages look like.

Home Page
Welcome
Manage student data easily and efficiently.

[ Add Student ]   [ View Students ]
---------------------------------------------------------
Student List Page
ID   Name      Age   Email                Course
1    Kiran     20    kiran@gmail.com      B.Tech
2    Anjali    21    anjali@gmail.com     B.Sc

Actions: View  Edit  Delete
------------------------------------------
Add Student Page
Add Student

Name:
Age:
Gender:
Phone:
Email:
Course:
Join Date:
Address:
About:

[ Save ]
------------------------------------
Student Details Page
Student Details

ID: 1
Name: Kiran
Age: 20
Gender: Male
Phone: 9876543210
Email: kiran@gmail.com
Course: B.Tech
Join Date: 2025-01-12
Address: Hyderabad
About: Good student

[ Back ]
-------------------------------------
Delete Page
Delete Record

Are you sure you want to delete Kiran?

[ Yes, Delete ]   [ Cancel ]
------------------------------------
Project Structure
studentmanagement/
├── studentmanagement/
│   └── urls.py
├── App/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── add_std.html
│   │   ├── update_std.html
│   │   ├── student_list.html
│   │   ├── delete_std.html
│   │   └── view_std.html
├── db.sqlite3
└── manage.py
--------------------------------
Author
Shaik Suhel Basha 📧 GitHub: @ShaikSuhelBasha03
