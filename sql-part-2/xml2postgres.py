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
    age = item.find('Age').text
    customerId = item.find('CustomerId').text
    name = item.find('Name').text
    email = item.find('Email').text
    data = (customerId,name,email,age)
    insert = f"INSERT INTO customer (CustomerID, Name, Email, Age) VALUES (%s, %s, %s, %s)"
    cur.execute(insert,data)

conn.commit()
cur.close()
conn.close()