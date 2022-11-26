from baza import *
from baza_exr_imp import  *
from loger import logging
def menu():
    while True:
        n = input('1 - show all \n'
                  '2 - find data \n'
                  '3 - delete data \n'
                  '4 - redactor data  \n'
                  '5 - add data \n'
                  '6 - import \n'
                  '7 - export \n'
                  '8 - exit')
        if n == '1':
            showall()
        elif n == '2':
            finddata(input('surname  or  number'))
        elif n == '3':
            showall()
            deletedata()
        elif n == '4':
            showall()
            redactordata()
        elif n == '5':
            adddata()
        elif n == '6':
            import_1()
        elif n == '7':
            export(input('enter name file    '))
        elif n == '8':
            print( ' see you soon')
            logging.info('stop program')
            exit()
        else:
            print('try again - error')
            logging.warning(' data incorrect')


