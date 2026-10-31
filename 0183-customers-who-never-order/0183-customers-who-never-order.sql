/* Write your PL/SQL query statement below */
select c.name "Customers"
from customers c 
left join orders o
on c.id = o.customerid
where o.customerId is null;