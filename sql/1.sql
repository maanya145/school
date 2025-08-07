CREATE DATABASE 05aug;

USE 05aug;

DROP TABLE students;


CREATE TABLE students(
    stu_id INT PRIMARY KEY,
    stu_name VARCHAR(20)
    );

CREATE TABLE subjects(
    sub_id VARCHAR(20),
    sub_name VARCHAR(20)
    );

insert into students values(1,'ABC'), (2, 'XYZ');

insert into subjects values('A1','Maths'), ('A2','English');

SELECT * FROM students, SUBJECTS;

drop TABLE students;


CREATE TABLE students(
    stu_id INT PRIMARY KEY,
    name VARCHAR(20),
    class VARCHAR(20)
    );

drop TABLE SUBJECTS;

CREATE Table subjects(
    stu_id int PRIMARY KEY,
    subject VARCHAR(20),
    marks INT
    );

INSERT INTO students VALUES(1,'ashu','10A'), (2, 'Ravi','10B'), (3, 'Priya','10C');

insert into subjects values(1,'Maths',100), (2,'Maths',90), (3,'Maths',80);

select * from students NATURAL JOIN subjects;

