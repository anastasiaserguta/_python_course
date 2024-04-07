'''
Программа позволяет использовать шифр Цезаря для кодирования английских и русских слов в пределах бесконечного цикла (до ввода стоп).
Для старта необходимо выбрать алфавит и необходимое направление, а также указать шаг сдвига по алфавиту, посредством которого необходимо закодировать
либо декодировать текст.
Для работы функций используются переменные для хранения отдельных значений, а также формулы для поиска букв, отвечающих шагу сдвига.
При выходе за пределы индексов алфавитов применена обработка исключений IndexError.
'''

# Русский/английский алфавиты в нижнем/верхнем регистре.
alpha_english_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_english_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_russian_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alpha_russian_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

while True:
    # Функция кодирования шифром Цезаря английских слов. 
    def english_code():
        sent = input('Введите строку для шифрования:')
        step = int(input('Введите шаг сдвига:'))
        sent_code = ''
        for i in range(len(sent)):
            if sent[i] in alpha_english_lower:
                position = alpha_english_lower.find(sent[i])
                try:
                    sent_code += alpha_english_lower[position + step]
                except IndexError:
                    sent_code += alpha_english_lower[step - (len(alpha_english_lower) - position)]
            elif sent[i] in alpha_english_upper:
                position = alpha_english_upper.find(sent[i])
                try:
                    sent_code += alpha_english_upper[position + step]
                except IndexError:
                    sent_code += alpha_english_upper[step - (len(alpha_english_upper) - position)]
            else:
                sent_code += sent[i]


        return sent_code

    # Функция кодирования русских слов.
    def russian_code():
        sent = input('Введите строку для шифрования:')
        step = int(input('Введите шаг сдвига:'))
        sent_code = ''
        for i in range(len(sent)):
            if sent[i] in alpha_russian_lower:
                position = alpha_russian_lower.find(sent[i])
                try:
                    sent_code += alpha_russian_lower[position + step]
                except IndexError:
                    sent_code += alpha_russian_lower[step - (len(alpha_russian_lower) - position)]
            elif sent[i] in alpha_russian_upper:
                position = alpha_russian_upper.find(sent[i])
                try:
                    sent_code += alpha_russian_upper[position + step]
                except IndexError:
                    sent_code += alpha_russian_upper[step - (len(alpha_russian_upper) - position)]
            else:
                sent_code += sent[i]

        
        return sent_code

    # Функция декодирования английских слов.
    def english_decode():
        sent = input('Введите строку для дешифровки:')
        step = int(input('Введите шаг сдвига:'))
        sent_code = ''
        for i in range(len(sent)):
            if sent[i] in alpha_english_lower:
                position = alpha_english_lower.find(sent[i])
                try:
                    sent_code += alpha_english_lower[position - step]
                except IndexError:
                    sent_code += alpha_english_lower[len(alpha_english_lower) - (step - position)]
            elif sent[i] in alpha_english_upper:
                position = alpha_english_upper.find(sent[i])
                try:
                    sent_code += alpha_english_upper[position - step]
                except IndexError:
                    sent_code += alpha_english_upper[step - (len(alpha_english_upper) - position)]
            else:
                sent_code += sent[i]
        
        return sent_code
    
    # Функция декодирования русских слов.
    def russian_decode():
        sent = input('Введите строку для дешифровки:')
        step = int(input('Введите шаг сдвига:'))
        sent_code = ''
        for i in range(len(sent)):
            if sent[i] in alpha_russian_lower:
                position = alpha_russian_lower.find(sent[i])
                try:
                    sent_code += alpha_russian_lower[position - step]
                except IndexError:
                    sent_code += alpha_russian_lower[len(alpha_russian_lower) - (step - position)]
            elif sent[i] in alpha_russian_upper:
                position = alpha_russian_upper.find(sent[i])
                try:
                    sent_code += alpha_russian_upper[position - step]
                except IndexError:
                    sent_code += alpha_russian_upper[step - (len(alpha_russian_upper) - position)]
            else:
                sent_code += sent[i]
        
        return sent_code

    answer = input('Введите необходимое направление (шифровать/дешифровать):')

    def for_code():
        alpha = input('Введите алфавит шифрования (рус/англ):')
        if alpha.lower() == 'рус':
            return russian_code()
        
        elif alpha.lower() == 'англ':
            return english_code()

    def for_decode():
        alpha = input('Введите алфавит дешифрования (рус/англ):')
        if alpha.lower() == 'рус':
            return russian_decode()
        
        elif alpha.lower() == 'англ':
            return english_decode()


    # Получение запроса на старт программы и необходимого направления, запуск соответствующих функций.
    if answer.lower() == 'шифровать':
        print(for_code())

    elif answer.lower() == 'дешифровать':
        print(for_decode())

    else:
        if answer.lower() == 'стоп': # Остановка программы.
            print('Выполнение программы остановлено.')
            break

        else:
            print('Проверьте правильность введенного запроса!') # Простая "защита от дурака".
    