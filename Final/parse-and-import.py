import neo4j
from lxml import etree
import re

driver = neo4j.GraphDatabase.driver(
    uri="bolt://localhost:7687",
    auth=("neo4j", "12345678")
)

WIKI_XML = "./enwiki-20251020-pages-articles-multistream.xml"

def import_wiki(file):
    root = etree.iterparse(source=file, events=("end",), tag="page")
    
    with driver.session() as session:
        for event, item in root:
            print(item.findtext("title"))



import_wiki(WIKI_XML)
driver.close() # End of the thingy, may he rest in peace