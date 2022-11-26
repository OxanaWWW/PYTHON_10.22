from baza import *
from baza_exr_imp import *
from loger import logging


def menu():
    while True:
        refresh()
        n = input('1 - see all students \n'
                  '2 - student search \n'
                  '3 - action with student \n '
                  '4 - import base\n'
                  '5 - export base \n'
                  '6 - exit')
        if n == '1':
            showall()
        elif n == '2':
            finddata(input('surname  or  number'))
        elif n == '3':
            menu_student()
        elif n == '4':
            import_1()
        elif n == '5':
            export(input('enter name file    '))
        elif n == '6':
            print(' see you soon')
            logging.info('stop program')
            exit()
        else:
            print('try again - error')
            logging.warning(' data incorrect')


def menu_student():
    while True:
        n = input('1 - remove the student \n'
                  '2 - changing student  \n'
                  '3 - add  to student \n'
                  '4 - watch grade \n'
                  '5 - list of class \n'
                  '6 - exit')
        if n == '1':
            showall()
            deletedata()
        elif n == '2':
            showall()
            redactordata()
        elif n == '3':
            adddata()
        elif n == '4':
            finddata(input('search grade  '))
        elif n == '5':
            finddata(input('search list of class  '))
        elif n == '6':
            logging.info('come back')
            # exit()

            return
        else:
            print('try again - error')
            logging.warning(' data incorrect')
