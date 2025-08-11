-- Active: 1754281597996@@127.0.0.1@3306@10aug
-- primary key (not null, unique) --

create DATABASE 10aug;
use 10aug;

drop TABLE students;
CREATE TABLE students(
    student_ID INT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50)
);

desc students;


-- foreign key -- 


create table marks(
    student_ID INT PRIMARY KEY,
    roll_no INT,
    subjects VARCHAR(50),
    marks INT,
    FOREIGN KEY (student_ID) REFERENCES students(student_ID)
);


desc marks;


create table members(
    member_ID INT,
    email VARCHAR(100) unique,
    phone VARCHAR(10) unique,
    PRIMARY KEY(member_ID)
);

desc members;


create table orders(
    order_ID INT,
    product_ID INT,
    quantity INT,
    PRIMARY KEY(order_ID, product_ID)
);


desc orders;

