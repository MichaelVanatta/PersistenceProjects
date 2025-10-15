import xml.etree.ElementTree as ET
import psycopg2

tree = ET.parse("customers/customers.xml")
root = tree.getroot()

conn = psycopg2.connect(
    host="localhost", 
    database="postgres", 
    user="postgres", 
    password=""
)
cur = conn.cursor()

for item in root.findall('Customer'):
    customerId = item.find('CustomerId').text
    name = item.find('Name').text
    email = item.find('Email').text
    age = item.find('Age').text
    cur.execute("INSERT INTO Customer (CustomerID, Name, Email, Age) VALUES (%s, %s)", (customerId, name, email, age))

conn.commit()
cur.close()
conn.close()