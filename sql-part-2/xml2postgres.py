import xml.etree.ElementTree as ET
import psycopg2

tree = ET.parse('your_data.xml')
root = tree.getroot()

conn = psycopg2.connect("dbname_db=postgres user=postgres password=ZanderHarden")
cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF EXISTS Customer(
                CustomerId PRIMARY KEY,
                Name VARCHAR(30),
                Email VARCHAR(30),
                Age SMALLINT
            );
            """)

for item in root.findall('Customer'):
    customerId = item.find('CustomerId').text
    name = item.find('Name').text
    email = item.find('Email').text
    age = item.find('Age').text
    cur.execute("INSERT INTO Customer (CustomerID, Name, Email, Age) VALUES (%s, %s)", (customerId, name, email, age))

conn.commit()
cur.close()
conn.close()