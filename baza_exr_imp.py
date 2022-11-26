import csv
from os import path

import json
def export(name_db):
    with open(f'{name_db}.json', 'w', encoding='utf-8', newline='') as file_w,\
        open('mobail_book.csv', 'r',encoding='utf-8' ) as file_r:
        t = csv.DictReader(file_r)
        u = {i['id']:i for i in t}
        file_w.write(json.dumps(u,indent=4,ensure_ascii=False))
