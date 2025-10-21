CREATE TABLE IF NOT EXISTS Customer(
    CustomerId VARCHAR(7) PRIMARY KEY,
    Name VARCHAR(30),
    Email VARCHAR(30),
    Age SMALLINT
);

CREATE TABLE IF NOT EXISTS Orders(
    OrderId VARCHAR(7) PRIMARY KEY,
    CustomerId VARCHAR(7) REFERENCES Customer(CustomerId),
    Total INT
);

CREATE TABLE IF NOT EXISTS OrderLines(
    OrderLineId VARCHAR(7),
    OrderId VARCHAR(7) REFERENCES Orders(OrderId),
    Qty INT,
    Price MONEY,
    LineTotal INT,
    ProductId VARCHAR(4)
);

DO $$ DECLARE
    r RECORD;
BEGIN
    -- Disable constraints
    EXECUTE 'DROP SCHEMA public CASCADE';
    EXECUTE 'CREATE SCHEMA public';
END $$;