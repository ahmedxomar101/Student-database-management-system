import sqlite3
import os


def connect():
    ''' Create a database if not existed and make a connection to it.
    
    '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data1 (id Integer PRIMARY KEY, fn TEXT, ln TEXT, term INTEGER, gpa REAL)")
    conn.commit()
    conn.close()

def insert(fn,ln,term,gpa):
    ''' insertion function to insert a new student to the database.
    
        Arguments
        ---------
        fn: str, Student First Name.
        ln: str, Student Last Name.
        term: int, Student Term.
        gpa: float, Student GPA.
    '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data1 Values (NULL,?,?,?,?)",(fn,ln,term,gpa))
    conn.commit()
    conn.close()

def view():
    ''' view function to show the content of the database 
        which is the student data.
        returns the content of the database.
    '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data1")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(fn="",ln="",term="",gpa=""):
    ''' search function to search for a specific student in the database.
        returns the content of the database.
    
        Arguments
        ---------
        fn: str, Student First Name.
        ln: str, Student Last Name.
        term: str, Student Term.
        gpa: str, Student GPA.
    '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("Select * FROM data1 WHERE fn=? or ln=? or term=? or gpa=?",(fn,ln,term,gpa))
    rows = cur.fetchall()
    conn.close()
    return(rows)

def delete(id):
    ''' delete function to delete a specific student from the database.
    
        Arguments
        ---------
        id: int, id of the student in the database.
    '''
    conn = sqlite3.connect("Students.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM data1 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,fn,ln,term,gpa):
    ''' update function to update the data of a specific student in the database
        by their id.
    
        Arguments
        ---------
        id: int, id of the student in the database.
        fn: str, updated Student First Name.
        ln: str, updated Student Last Name.
        term: int, updated Student Term.
        gpa: float, updated Student GPA.
    '''
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("UPDATE data1 SET fn=?, ln=?, term=?, gpa=? WHERE id=?",(fn,ln,term,gpa,id))
    conn.commit()
    conn.close()

def delete_data():
    ''' delete_data function is to delete the database.
    
    '''
    if os.path.exists("Students.db"):
        os.remove("Students.db")
    connect()

connect()
