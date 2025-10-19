import psycopg2

conn = psycopg2.connect(
    host="localhost", 
    database="postgres", 
    user="postgres", 
    password="PP"
)
cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS Customers(
                CustomerId VARCHAR(7) PRIMARY KEY,
                Name VARCHAR(30),
                Email VARCHAR(30),
                Age VARCHAR(3)
            );
            """)

cur.execute("""
            CREATE TABLE IF NOT EXISTS Orders(
                OrderId VARCHAR(7) PRIMARY KEY,
                CustomerId VARCHAR(7) REFERENCES Customers(CustomerId),
                Total INT
            );
            """)

cur.execute("""
            CREATE TABLE IF NOT EXISTS OrderLines(
                OrderLineId VARCHAR(7),
                OrderId VARCHAR(7) REFERENCES Orders(OrderId),
                Qty INT,
                Price MONEY,
                LineTotal INT,
                ProductId VARCHAR(4)
            );
            """)

conn.commit()
cur.close()
conn.close()