import xml.etree.ElementTree as ET
import psycopg2
from psycopg2.extras import execute_batch

tree = ET.parse("customers/customers.xml")
root = tree.getroot()

counter = 0;

conn = psycopg2.connect(
    host="localhost", 
    database="postgres", 
    user="postgres", 
    password=""
)
cur = conn.cursor()

insert_customer = """
    INSERT INTO customer (CustomerId, Name, Email, Age)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (CustomerId) DO NOTHING;
"""

insert_order = """
    INSERT INTO orders (OrderId, CustomerId, Total)
    VALUES (%s, %s, %s)
    ON CONFLICT (OrderId) DO NOTHING;
"""

insert_orderline = """
    INSERT INTO orderlines (OrderLineId, OrderId, Qty, Price, LineTotal, ProductId)
    VALUES (%s, %s, %s, %s, %s, %s);
"""

customer_batch = []
order_batch = []
orderline_batch = []

BATCH_SIZE = 10000

context = ET.iterparse("customers/customers.xml", events=("end",))
_, root = next(context)

for event, elem in context:
    if elem.tag == "Customer":
        customer_id = elem.findtext("CustomerId")
        name = elem.findtext("Name")
        email = elem.findtext("Email")
        age = elem.findtext("Age")
        customer_batch.append((customer_id, name, email, age))

        orders = elem.find("Orders")
        if orders is not None:
            for order in orders.findall("Order"):
                order_id = order.findtext("OrderId")
                total = order.findtext("Total")
                order_batch.append((order_id, customer_id, total))

                orderlines = order.find("Lines")
                if orderlines is not None:
                    for ol in orderlines.findall("OrderLine"):
                        orderline_id = ol.findtext("OrderLineId")
                        price = ol.findtext("Price")
                        product_id = ol.findtext("ProductId")
                        qty = ol.findtext("Qty")
                        orderline_total = ol.findtext("Total")
                        orderline_batch.append((orderline_id, order_id, qty, price, orderline_total, product_id,))

        if len(customer_batch) >= BATCH_SIZE:
            execute_batch(cur, insert_customer, customer_batch)
            execute_batch(cur, insert_order, order_batch)
            execute_batch(cur, insert_orderline, orderline_batch)
            conn.commit()
            customer_batch.clear()
            order_batch.clear()
            orderline_batch.clear()
            counter += 1
            print("Bum Bitty Bitty Bitty Bum" + counter)

        root.clear()

if customer_batch:
    execute_batch(cur, insert_customer, customer_batch)
    execute_batch(cur, insert_order, order_batch)
    execute_batch(cur, insert_orderline, orderline_batch)
    conn.commit()
    counter += 1
    print("The Final BUM: " + counter)

cur.close()
conn.close()
