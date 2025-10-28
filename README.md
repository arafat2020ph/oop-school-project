# oop-school-project
This project is a simple School Management System developed using Python Object-Oriented Programming (OOP) concepts. It demonstrates the use of Inheritance and Encapsulation to manage school data efficiently and securely
Key Features:

Student Management:

Store student information like name, ID, class, and marks.

Access student data using getter and setter methods (Encapsulation) to ensure data security.

Teacher Management:

Store teacher information including name, subject, and employee ID.

Use Inheritance to create different types of staff from a common parent class (Person).

Grade and Report Generation:

Calculate student grades and generate reports.

Encapsulation ensures marks are updated only via class methods.

Parent/Child Class Structure:

Person (Parent Class) → Student, Teacher (Child Classes)

This shows Inheritance in action, avoiding code duplication.

OOP Concepts Used:

Encapsulation:

Private attributes like _marks, _student_id are hidden from outside access.

Access through methods like get_marks() and set_marks().

Inheritance:

Student and Teacher classes inherit common properties from Person class.

Demonstrates reusability and hierarchical structure.

Polymorphism (Optional for extra):

Same method name (like display_info()) works differently for students and teachers
