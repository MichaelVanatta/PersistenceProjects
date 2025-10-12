import psycopg2, os

def comma_death(old_file:str):
    with open(f"./CSV/{old_file}", 'r') as infile, open("CSV/temp.csv", 'w') as outfile:
        for line in infile:
            stripped_line = line.strip()
            if stripped_line.endswith(','):
                modified_line = stripped_line[:-1]
            else:
                modified_line = stripped_line
            outfile.write(modified_line + '\n')

    os.replace("CSV/temp.csv", f"./CSV/{old_file}")
    print("Trailing commas removed")

def parse_local_csv():
    for file in os.listdir('./CSV'):
        open("./CSV/temp.csv", 'x')
        comma_death(file)
        with open(f"CSV/{file}", 'r') as f:
            next(f)
            if file.replace("nw.", "nw_").replace(".csv", "") == 'nw_data.1.AllData':
                cur.copy_from(f, 'nw_all_data', sep=",")
            else:
                cur.copy_from(f, file.replace("nw.", "nw_").replace(".csv", ""), sep=",")
        print("data created")

def parse_remote_text():
    URLs = ['https://download.bls.gov/pub/time.series/nw/nw.series', 'https://download.bls.gov/pub/time.series/nw/nw.data.1.AllData']

    for url in URLs:

        pass

    pass


conn = psycopg2.connect(
    host="localhost", 
    database="postgres", 
    user="postgres", 
    password="PP"
)
cur = conn.cursor()

parse_local_csv()
# parse_remote_text()
    
conn.commit()
cur.close()
conn.close()