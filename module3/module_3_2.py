# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.

# Цель: закрепить знания о параметрах по умолчанию и именованных аргументах.

# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя(администрации или службы поддержки).
# Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.

# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент
# со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
# Пункты задачи:



def verify_mail_recipient_sender(message, recipient, sender='university.help@gmail.com'):
    print(not(('@' in recipient and ('.com' in recipient or '.ru' in recipient or '.net' in recipient) ) and ('@' in sender and ('.com' in sender or '.ru' in sender or '.net'in sender))),'\n')
    # print('@' in sender and ('.com' in sender or '.ru' in sender or '.net'in sender),'\n')
    # if ('@' and ('.com' or '.ru' or '.net') in recipient) or ('@' and ('.com' or '.ru' or '.net') in sender):
    # else:
    #     print(('@' and ('.com' or '.ru' or '.net') in recipient) or ('@' and ('.com' or '.ru' or '.net') in sender))

def verify_recipient_is_not_sender(recipient, sender):
    if recipient != sender:
        return True
    else:
        return False

def verify_default_sender(sender):
    if sender == 'university.help@gmail.com':
        return True
    else:
        return False

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not (('@' in recipient and ('.com' in recipient or '.ru' in recipient or '.net' in recipient) ) and ('@' in sender and ('.com' in sender or '.ru' in sender or '.net'in sender))):
        print(f'Невозможно отправить письмо с адреса: "{message}" с адреса {sender} на адрес {recipient}.')
    elif recipient == sender:
        print(f'Нельзя отправить письмо "{message}" самому {sender} себе {recipient}! ')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо: "{message}" успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо: "{message}" отправлено с адреса {sender} на адрес {recipient}.')

# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1
# обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку:
# "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно из перечисленных уведомлений! Проверки перечислены по мере выполнения.

# Пример результата выполнения программы:
# Пример выполняемого кода (тесты):
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!

# Примечания:
# Обязательно именованные аргументы отделяются от остальных символом "*" перед ними.
# Именованные аргументы всегда идут после позиционных.