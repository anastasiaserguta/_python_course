'''
Напишите программу - телефонную книгу для терминала. Телефонная книга должна сохранять имя, телефон, e-mail.
Пользователь должен иметь возможность:
- Добавить новый контакт в книгу. 
- Удалить контакт из книги (по имени).
- Просмотреть существующие контакты (вывести на экран все имена).
- Просмотреть информацию (телефон, e-mail) о конкретном контакте (по имени).
- Выйти из программы.
Формат ввода и вывода данных любой. Главное, чтобы он был интуитивно понятен и удобен для использования.
'''

def change_phone_book(phone_book, answer): # Основная часть программы, отвечает за прием и обработку запросов пользователя.
    while answer != '.':
        contact_name = ''
        if answer == 'help':
            print(*all_actions, sep='\n')
        elif answer == '+':
            contact_name = input('Введите ФИО контакта для добавления в телефонную книгу: ')
            phone_book[contact_name] = input('Введите данные о контакте (e-mail), телефон и т.д.: ')
            print(f'Контакт {contact_name} добавлен!')
        elif answer == '-':
            contact_name = input('Введите ФИО контакта для удаления из телефонной книги: ')
            phone_book.pop(contact_name)
            print(f'Контакт {contact_name} удален!')
        elif answer == '?':
            print(f'Телефонная книга содержит {len(phone_book)} контакт (-а/-ов).')
            for contact in phone_book.keys():
                print(f'{contact} - {phone_book[contact]}')
        elif answer == '@':
            contact_name = input('Введите ФИО контакта для его просмотра в телефонной книге: ')
            print(f'{contact_name} - {phone_book[contact_name]}')
        else:
            print('Введено некорректное значение!')

        answer = input(f'Выберите следующее желаемое действие: ')


        

phone_book = {}        
print('Вы запустили телефонную книгу.')

all_actions = ('+ - добавить контакт', # Доступные короткие команды для работы с книгой.
               '- - удалить контакт',
               '? - просмотреть телефонную книгу',
               '@ - просмотреть информацию конкретного контакта',
               '. - выйти из программы',
               'help - просмотреть команды')

print(*all_actions, sep='\n') # Первоначальный вывод всех команд.

answer = input(f'Введите желаемое действие: ')

change_phone_book(phone_book, answer) # Вызов функции.

print('Вы вышли из программы.')

