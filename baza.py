from os import path
import csv

# from baza_exr_imp import name_db  =
name_db = 'school_base.csv'

data = ''
iddata = 0


def refresh():
    global data, iddata
    if path.exists(name_db):
        with open(name_db, 'r', encoding='utf-8') as file:
            x = csv.DictReader(file)
            data = [i for i in x]
            iddata = data[-1]['id']
    else:
        print('no data')


def showall():
    global data, iddata
    # if path.exists(name_db):
    #     with open(name_db, 'r', encoding='utf-8') as file:
    #         x = csv.DictReader(file)
    #         data = [i for i in x]
    #         iddata = data[-1]['id']

    y = [' '.join(key.values()) for key in data]
    print(*y, sep='\n')

    # else:
    #     print('no data')


def adddata():
    global iddata
    if not path.exists(name_db):
        with open(name_db, 'w', encoding='utf-8', newline='') as file:
            p = ['id', 'name', 'surname', 'grades journal', 'class']
            v = csv.DictWriter(file, fieldnames=p)
            v.writeheader()
    z = {'id': '1', 'name': '', 'surname': '', 'grades journal': '', 'class': ''}
    for i in z:
        if i != 'id':
            z[i] = input(f'enter {i}')
    if all(z.values()):
        iddata = int(iddata) + 1
        z['id'] = iddata
        with open(name_db, 'a', encoding='utf-8', newline='') as file:
            s = list(z.keys())
            v = csv.DictWriter(file, fieldnames=s)
            v.writerow(z)
    else:
        print('data incorrect')


def finddata(r):
    global data
    f = [' '.join(i.values()) for i in data if r in i.values()]
    if f:
        print(*f, sep='\n')
    else:
        print('not find')


def deletedata():
    global data
    q = input('id')
    data = [i for i in data if i['id'] != q]
    with open(name_db, 'w', encoding='utf-8', newline='') as file:
        p = ['id', 'name', 'surname', 'grades journal', 'class']
        v = csv.DictWriter(file, fieldnames=p)
        v.writeheader()
        for i in data:
            v.writerow(i)


def redactordata():
    global data
    m = input('id')
    for i in data:
        if i['id'] == m:
            for e in i:
                if e != 'id':
                    i[e] = input(f'enter value{e}')
            break
    with open(name_db, 'w', encoding='utf-8', newline='') as file:
        p = ['id', 'name', 'surname', 'grades journal', 'class']
        v = csv.DictWriter(file, fieldnames=p)
        v.writeheader()
        for i in data:
            v.writerow(i)


def import_1():
    global name_db
    n = input('enter new name baza       ')
    if path.exists(name_db):
        name_db = n
