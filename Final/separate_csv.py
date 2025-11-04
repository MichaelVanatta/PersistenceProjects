import csv, os, pycountry

CSV_FOLDER = "./csv"
CSV_TARGET_FILE = "./csv/new_links.csv"
CATEGORIES = ['Category:Famines by country', 'Category:Famines by decade', 'Category:Food and drink', 'Category:Food and drink culture']
FOOD_ELEMENTS = []
EVENT_ELEMENTS = []
COUNTRY_ELEMENTS = []

elements = []
elem = []

with open(file="./csv/links.csv", mode="r", encoding="utf-8") as mother_file:
    read_links = csv.reader(mother_file)
    

    for row in read_links: 
        if any(cat.lower() == row[0].lower() for cat in CATEGORIES) or any(cat.lower() == row[1].lower() for cat in CATEGORIES):
            print(row)
            # if any(item in row[1] for item in [country.name for country in pycountry.countries]):
            #     COUNTRY_ELEMENTS.append(row[1])
            #     print(row)
            # elif any(item in row[0] for item in ['Famine', 'famine']):
            #     EVENT_ELEMENTS.append(row[1])
            #     print(row)
            # else:
            #     FOOD_ELEMENTS.append(row[1])

# with open(file="./csv/links.csv", mode="r", encoding="utf-8") as mother_file:
#     read_links = csv.reader(mother_file)
#     for row in read_links: 
#         if any(item in row[1] for item in elements) or any(item in row[0] for item in elements):
#             print(row)
#             elem.append(row[0])

# with open(file="./csv/pages.csv", mode="r", encoding="utf-8") as mother_file, open(file=CSV_TARGET_FILE, mode="w", encoding="utf-8") as child_file:
#     read_pages = csv.reader(mother_file)
#     write = csv.writer(child_file)

#     for row in read_pages:
#         if any(item in row[0] for item in elem) or any(item in row[1] for item in elem):
#             print(row)
#             write.writerow(row)

print("Done!")