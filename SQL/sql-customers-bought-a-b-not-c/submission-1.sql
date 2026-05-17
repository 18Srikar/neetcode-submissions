SELECT c.customer_id , c.customer_name FROM customers as c JOIN orders as o on c.customer_id = o.customer_id
GROUP BY c.customer_id , c.customer_name
HAVING sum(CASE WHEN product_name = 'A' THEN 1 ELSE 0 END)>=1 AND sum(CASE WHEN product_name = 'B' THEN 1 ELSE 0 END)>=1 AND sum(CASE WHEN product_name ='C' THEN 1 ELSE 0 END)=0
ORDER BY customer_name