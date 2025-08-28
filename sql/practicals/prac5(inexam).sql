create DATABASE prac5;
use prac5;


create TABLE sales(
    sales_id int PRIMARY KEY,
    customer_name VARCHAR(20),
    product VARCHAR(20),
    quantity INT,
    price INT
);

INSERT INTO sales (sales_id, customer_name, product, quantity, price) 
VALUES 
    (101, 'Ramesh', 'Laptop', 5, 60000), 
    (102, 'Meera', 'Tablet', 3, 15000), 
    (103, 'Sangeeta', 'Laptop', 10, 60000), 
    (104, 'Mohan', 'Phone', 4, 20000), 
    (105, 'Preeti', 'Phone', 10, 20000), 
    (106, 'Mike', 'Laptop', 3, 60000), 
    (107, 'George', 'Tablet', 5, 15000);

SELECT product, SUM(quantity) from sales group by product having sum(quantity) > 12;

select * from sales order by product desc;

select distinct product from sales;





