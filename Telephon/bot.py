import telebot
import crud as cr
import logger as lg


token = cr.get_token()
bot  =telebot.TeleBot("5951795770:AAH7MpYy26FXRGdJYEWwUvMvDNBgF8A_gYQ", parse_mode='MARKDOWN')



@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(
        message.chat.id, f'Ошибка, нужна помощь: /help.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, *{message.from_user.first_name}!*\nНужна помощь? введи\nкоманду: /help\nГлавное меню введи: /main')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - Начало\n/main - Главное меню\n/help - Справка')


name_it = ''
surname_it = ''
number_it = ''
email_it = ''
user_id_it = ''
new_number_it = ''


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/main':
        bot.send_message(message.chat.id, f'Введи нужную команду: \n/1 - Все записи.\n/2 - Найти номер по фамилии.\n/3 - Найти номер по имени.\n/4 - Поиск по номеру телефона.\n/5 - Добавить новую запись.\n/6 - Изменить существующую запись.\n/7 - Удалить запись.')
        cr.init_data_base('base_phone.csv')

    elif message.text == '/1':
        lg.logging.info('Пункт 1')
        bot.send_message(message.chat.id, f'{cr.retrive()}')

    elif message.text == '/2':
        lg.logging.info('Пункт 2')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, find_surname)

    elif message.text == '/3':
        lg.logging.info('Пункт 3')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, find_name)

    elif message.text == '/4':
        lg.logging.info('Пункт 4')
        bot.send_message(message.chat.id, f'Введите номер  телефона')
        bot.register_next_step_handler(message, find_number)

    elif message.text == '/5':
        lg.logging.info('Пункт 5')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, get_name)

    elif message.text == '/6':
        lg.logging.info('Пункт 6')
        bot.send_message(
            message.chat.id, f'Какой контакт хотите изменить?\nУкажите по:\n/61 - Фамилии\n/62 - Имени\n/63 - Номеру телефона')
        bot.register_next_step_handler(message, edit_entry)

    elif message.text == '/7':
        lg.logging.info('Пункт 7')
        bot.send_message(
            message.chat.id, f'Выберите контакт, который хотите удалить?\nВыберите по:\n/71 - Фамилии\n/72 - Имени\n/73 - Номеру телефона')
        bot.register_next_step_handler(message, delete_contact)

    else:
        bot.send_message(
            message.chat.id, f'Ошибка! Вызови помощь!: /help.')


def find_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')


def find_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')


def find_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')


def get_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'Введите фамилию')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'Введите номер телефона')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'Введите e-mail')
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    global email_it
    email_it = message.text
    lg.logging.info('User entered: {email_it}')
    cr.create(name_it, surname_it, number_it, email_it)
    bot.send_message(message.chat.id, f'Записано!')


def edit_entry(message):
    if message.text == '/61':
        lg.logging.info('Выбран пункт №6.1')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, change_surname)

    elif message.text == '/62':
        lg.logging.info('Выбран пункт №6.2')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, change_name)

    elif message.text == '/63':
        lg.logging.info('Выбран пункт №6.3')
        bot.send_message(message.chat.id, f'Введите номер телефона')
        bot.register_next_step_handler(message, change_num)

    else:
        bot.send_message(
            message.chat.id, f'Ошибка! Вызывайте помощь: /help.')


def change_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите изменить')
    bot.register_next_step_handler(message, change_number)


def change_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите изменить')
    bot.register_next_step_handler(message, change_number)


def change_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите изменить')
    bot.register_next_step_handler(message, change_number)


def change_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    bot.send_message(
        message.chat.id, f'Введите новый номер телефона')
    bot.register_next_step_handler(message, change_new_number)


def change_new_number(message):
    global new_number_it
    new_number_it = message.text
    lg.logging.info('User entered: {new_number_it}')
    cr.update(id=user_id_it, new_number=new_number_it)
    bot.send_message(
        message.chat.id, f'Изменено!')


def delete_contact(message):
    if message.text == '/71':
        lg.logging.info('Выбран пункт 7.1')
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, delete_surname)

    elif message.text == '/72':
        lg.logging.info('Выбран пункт 7.2')
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, delete_name)

    elif message.text == '/73':
        lg.logging.info('Выбран пункт 7.3')
        bot.send_message(message.chat.id, f'Введите номер телефона')
        bot.register_next_step_handler(message, delete_num)

    else:
        bot.send_message(
            message.chat.id, f'Ошибка! Нужна помощь: /help.')


def delete_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(surname=surname_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите удалить')
    bot.register_next_step_handler(message, delete_number)


def delete_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите удалить')
    bot.register_next_step_handler(message, delete_number)


def delete_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cr.retrive(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Введите id записи, которую хотите удалить')
    bot.register_next_step_handler(message, delete_number)


def delete_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    cr.delete(id=user_id_it)
    bot.send_message(
        message.chat.id, f'Удалено!')


print('server start')
bot.infinity_polling()