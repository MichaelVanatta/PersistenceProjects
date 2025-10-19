import xml.etree.ElementTree as ET
import psycopg2

tree = ET.parse("customers/customers.xml")
root = tree.getroot()

conn = psycopg2.connect(
    host="localhost", 
    database="postgres", 
    user="postgres", 
    password="PP"
)
cur = conn.cursor()

def read_customer():
    for item in root.findall('Customer'):
        age = item.find('Age').text
        customerId = item.find('CustomerId').text
        name = item.find('Name').text
        email = item.find('Email').text
        data = (customerId,name,email,age)
        insert = f"INSERT INTO customers (CustomerID, Name, Email, Age) VALUES (%s, %s, %s, %s)"
        cur.execute(insert,data)

def read_orders():
    for item in root.findall('Customer'):
        for subitem in item.findall('Orders'):
            for subsubitem in subitem.findall('Order'):
                order_id = subsubitem.find('OrderId').text
                customer_id = subsubitem.find('CustomerId').text
                total = subsubitem.find('Total').text
                data = (order_id, customer_id, total)
                insert = f"INSERT INTO orders (OrderId, CustomerId, Total) VALUES (%s, %s, %s)"
                cur.execute(insert,data)

def read_order_line():   
    for item in root.findall('Customer'):
        for subitem in item.findall('Orders'):
            for subsubitem in subitem.findall('Order'):
                order_id = subsubitem.find('OrderId').text
                for subsubsubitem in subsubitem.findall('Lines'):
                    for subsubsubsubitem in subsubsubitem.findall('OrderLine'):
                        order_line_id = subsubsubsubitem.find('OrderLineId').text
                        qty = subsubsubsubitem.find('Qty').text
                        price = subsubsubsubitem.find('Price').text
                        data = (order_line_id, order_id, qty, price)
                        insert = f"INSERT INTO orderlines (OrderLineId, OrderId, Qty, Price) VALUES (%s, %s, %s, %s)"
                        cur.execute(insert,data)

def master_script():
    for item in root.findall('Customer'):
        age = item.find('Age').text
        customerId = item.find('CustomerId').text
        name = item.find('Name').text
        email = item.find('Email').text
        c_data = (customerId,name,email,age)
        c_insert = f"INSERT INTO customers (CustomerID, Name, Email, Age) VALUES (%s, %s, %s, %s)"

        cur.execute(c_insert,c_data)

        for subitem in item.findall('Orders/Order'):
            order_id = subitem.find('OrderId').text
            customer_id = subitem.find('CustomerId').text
            total = subitem.find('Total').text
            o_data = (order_id, customer_id, total)
            o_insert = f"INSERT INTO orders (OrderId, CustomerId, Total) VALUES (%s, %s, %s)"

            cur.execute(o_insert,o_data)

            for subsubitem in subitem.findall('Lines/OrderLine'):
                order_line_id = subsubitem.find('OrderLineId').text
                qty = subsubitem.find('Qty').text
                price = subsubitem.find('Price').text
                line_total = subsubitem.find('Total').text
                product_id = subsubitem.find('ProductId').text
                ol_data = (order_line_id, order_id, qty, price, line_total, product_id)
                ol_insert = f"INSERT INTO orderlines (OrderLineId, OrderId, Qty, Price, LineTotal, ProductId) VALUES (%s, %s, %s, %s, %s, %s)"

                cur.execute(ol_insert,ol_data)

# read_customer();
# read_orders();
# read_order_line();

master_script()

root.clear()

conn.commit()
cur.close()
conn.close()