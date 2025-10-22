SELECT CustomerRows, OrderRows, OrderLineRows
FROM (SELECT COUNT(*) FROM customers) AS CustomerRows
CROSS JOIN (SELECT COUNT(*) FROM orders) AS OrderRows
CROSS JOIN (SELECT COUNT(*) FROM orderlines) AS OrderLineRows

SELECT MAX(olpero) AS Maximum, MIN(olpero) AS Minimum, AVG(olpero) AS Average FROM (
    SELECT COUNT(*) as olpero
    FROM orderlines ol JOIN orders o ON ol.orderid = o.orderid
    GROUP BY o
)

SELECT c.customerid, c."name", COUNT(o.orderid) as orderspercustomer
FROM orders o JOIN customers c
    ON o.customerid = c.customerid
GROUP BY c.customerid
ORDER BY orderspercustomer DESC
LIMIT 1

SELECT c.customerid, c."name", COUNT(ol.*) as orderlinespercustomer
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
LIMIT 1