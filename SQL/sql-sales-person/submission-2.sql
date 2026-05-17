SELECT name FROM sales_person 
WHERE sales_id NOT IN (SELECT s.sales_id FROM sales_person as s LEFT JOIN orders as o on s.sales_id = o.sales_id JOIN company as c on o.com_id=c.com_id
WHERE c.name = 'CRIMSON')