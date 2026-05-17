SELECT seller_name FROM seller
WHERE seller_id NOT IN (SELECT s.seller_id FROM seller AS s JOIN orders as o on s.seller_id=o.seller_id
WHERE sale_date >= '2020-01-01' AND sale_date <= '2020-12-31')
ORDER BY seller_name