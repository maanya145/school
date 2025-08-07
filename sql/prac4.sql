-- Active: 1754281597996@@127.0.0.1@3306@cw
use cw;

drop TABLE sales;
CREATE table sales(
    salesID int PRIMARY KEY,
    Product VARCHAR(20),
    Category VARCHAR(20),
    Amount INT
);

INSERT INTO sales VALUES
(1,'Pen','Stationary',10),
(2,'Pencil','Stationary',5),
(3,'Mouse','Electronics',500),
(4,'Monitor','Electronics',3000),
(5,'Pen','Stationary',15),
(6,'Keyboard','Electronics',800);


select category, sum(amount) from sales group by category;

select category, sum(amount) as Totalsales from sales group by category having sum(amount) > 1000;



