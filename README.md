# Student-database-management-system

A simple **GUI project** made with **tkinter** and **sqlite3** for **Students Database Management System**. 

## Table of Content

1. [Introduction](#introduction)
2. [Screenshots](#screenshots)
3. [Instructions](#instructions)
   1. [Requirements](#requirements)
   2. [Execution](#execution)
   3. [Standalone App](#standalone-app)

## Introduction
In this project, you can do the following:
1. Add new student.
2. Update a specific student.
3. Delete a specific student.
4. Search for a specific student or multiple students by
    * First Name
    * Last Name
    * Term
    * GPA
5. Display all database
6. Delete the database

## Screenshots
Kindly, check the [screenshots folder](https://github.com/AhMeDxHaMiDo/Student-database-management-system/tree/master/screenshots) to get an overview about the software.

## Instructions

#### Requirements
  * Python 3
  * tkinter
  * sqlite3

    * Ex:
    ```
    pip install <package_name>
    ```

#### Execution
* Use `frontend.py` to run the software.

#### Standalone App
* To convert any script to Standalone App:
  1. Install pyinstaller package
      * `pip install pyinstaller`
  2. Run the command:
      * `pyinstaller --onefile --windowed frontend.py`

* [**The Standalone App for that Project**](https://github.com/AhMeDxHaMiDo/Student-database-management-system/blob/master/frontend.exe)
