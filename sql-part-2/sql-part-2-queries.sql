SELECT COUNT(*) FROM customers
SELECT COUNT(*) FROM orders
SELECT COUNT(*) FROM orderlines

SELECT MAX(olpero) FROM (
    SELECT COUNT(*) as olpero
    FROM orderlines ol JOIN orders o ON ol.orderid = o.orderid
    GROUP BY o
)

SELECT MIN(olpero) FROM (
    SELECT COUNT(*) as olpero
    FROM orderlines ol JOIN orders o ON ol.orderid = o.orderid
    GROUP BY o
)

SELECT AVG(olpero) FROM (
    SELECT COUNT(*) as olpero
    FROM orderlines ol JOIN orders o ON ol.orderid = o.orderid
    GROUP BY o
)

SELECT c.customerid, COUNT(o.orderid) as orderspercustomer
FROM orders o JOIN customers c
    ON o.customerid = c.customerid
GROUP BY c.customerid
ORDER BY orderspercustomer DESC
LIMIT 1

SELECT c.customerid, COUNT(ol.*) as orderlinespercustomer
FROM orders o 
JOIN customers c
    ON o.customerid = c.customerid
JOIN orderlines ol 
    ON o.orderid = ol.orderid
GROUP BY c.customerid
ORDER BY orderlinespercustomer DESC
LIMIT 1

SELECT ol.productid, COUNT(o.*) as numberofpurchases
FROM orderlines ol
JOIN orders o
    ON ol.orderid = o.orderid
GROUP BY ol.productid
ORDER BY numberofpurchases DESC