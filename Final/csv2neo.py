import os, csv, re

categories = r'\[\[Category:([^\]]+)\]\]'
acceptable_categories = ['Category:Famines', 'Category:Food and drink', 'Category:Famines by country']

# for file in os.listdir("./csv"):
with open("./csv/" + "links.csv", 'r', encoding="UTF-8") as master, open("./csv/new_links.csv", 'w', encoding="UTF-8") as new_file:
    reader = csv.reader(master)
    writer = csv.writer(new_file)

    for row in reader:
        if (any(re.match(r'\[\[Category:([^\]]+)\]\]', row[0]) for item in categories)) or (any(re.match(r'\[\[Category:([^\]]+)\]\]', row[1]) for item in categories)) :
            print(row)
            #writer.writerow(row)