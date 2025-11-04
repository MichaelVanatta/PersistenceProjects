from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(username,password))

with driver.session() as session:
    session.run("""
        LOAD CSV WITH HEADERS FROM "file:///food.csv" AS row
        WITH row
        WHERE row.food IS NOT NULL AND row.country IS NOT NULL
        MERGE (f:Food {name: row.food})
        MERGE (c:Country {name: row.country})
        MERGE (f)-[:MADE_IN]->(c)
""")

driver.close()