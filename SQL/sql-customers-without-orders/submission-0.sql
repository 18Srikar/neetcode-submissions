SELECT name FROM customers WHERE name NOT IN(SELECT c.name FROM customers as c JOIN orders as o 
ON c.id=o.customer_id)
