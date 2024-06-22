import sqlite3

#connect to sqllite
connection=sqlite3.connect("university.db")

#create a cursor to insert,create,retreive etc
cursor=connection.cursor()

#create table
student_table ="""
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    BirthDate DATE,
    Email VARCHAR(100) UNIQUE,
    CONSTRAINT UC_StudentFullName UNIQUE (FirstName, LastName)
);"""

course_table="""
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    DepartmentID INT,
    CONSTRAINT UC_CourseName UNIQUE (CourseName),
    CONSTRAINT FK_Courses_Department FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);"""

departments_table="""
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    CONSTRAINT UC_DepartmentName UNIQUE (DepartmentName)
);"""

enrollments_table="""
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    Grade VARCHAR(2),
    CONSTRAINT FK_Enrollments_Student FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    CONSTRAINT FK_Enrollments_Course FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    CONSTRAINT UC_Enrollment UNIQUE (StudentID, CourseID)
);"""

cursor.execute(student_table)
cursor.execute(departments_table)
cursor.execute(course_table)
cursor.execute(enrollments_table)

print("tables are created")

cursor.execute("""
INSERT INTO Students (StudentID, FirstName, LastName, BirthDate, Email)
VALUES
    (1, 'John', 'Doe', '1990-05-15', 'john.doe@example.com'),
    (2, 'Jane', 'Smith', '1992-08-22', 'jane.smith@example.com'),
    (3, 'Michael', 'Johnson', '1991-03-10', 'michael.j@example.com'),
    (4, 'Emily', 'Davis', '1993-11-28', 'emily.d@example.com'),
    (5, 'Chris', 'Williams', '1994-07-07', 'chris.w@example.com');""")

cursor.execute("""
INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES
    (1, 'Computer Science'),
    (2, 'Mathematics'),
    (3, 'History'),
    (4, 'Biology'),
    (5, 'Business');""")

cursor.execute("""
INSERT INTO Courses (CourseID, CourseName, DepartmentID)
VALUES
    (101, 'Introduction to Programming', 1),
    (102, 'Calculus I', 2),
    (103, 'World History', 3),
    (104, 'Biology 101', 4),
    (105, 'Introduction to Marketing', 5);""")

cursor.execute("""
INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, EnrollmentDate, Grade)
VALUES
    (1, 1, 101, '2023-01-15', 'A'),
    (2, 2, 102, '2023-01-20', 'B+'),
    (3, 3, 103, '2023-02-01', 'A-'),
    (4, 4, 104, '2023-02-10', 'B'),
    (5, 5, 105, '2023-02-15', 'A');""")

#display records
print("records are inserted")

print("the inserted records in students are:")

data=cursor.execute("select * from students;")

for row in data:
    print(row)

#close connection
connection.commit()
connection.close()
