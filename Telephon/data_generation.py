import csv
import random

import logger as lg

file = open('base_phone.csv', 'w')
newrecord = "ID,Name,Surname,PhoneNumber,email\n"
file.writelines(newrecord)

ls_name = ['Khazimir', 'Gilbertus', 'Leto', 'Shadam', 'Anton',
           'Viktor', 'Sirena', 'Irina', 'Liza', 'Oxana', 'Katerina']
ls_surname = ['Fenring', 'Albans', 'Atrides',
              'Korrino', 'Gorodetckiy', 'Frankinshtein', 'Batler', 'Markova', 'Vishenka']
ls_e_mail = ['@gmail.com', '@yandex.ru', '@mail.ru']


def list_of_numbers():

    randomListPhone = random.randint(79000000000, 80000000000)

    return str(randomListPhone)


def string_creation():
    s = ""
    s = s + random.choice(ls_name) + ',' + random.choice(ls_surname) + ',' + \
        list_of_numbers() + ',' + random.choice(ls_surname) + random.choice(ls_e_mail)
    return s


def start():
    for i in range(100):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


start()