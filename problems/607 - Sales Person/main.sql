SELECT name
FROM SalesPerson sp
WHERE sp.sales_id NOT IN(
    SELECT O.sales_id
    FROM Orders O
    WHERE O.com_id IN (
        SELECT com_id
        FROM Company C
        WHERE C.name = 'Red'
    )
)