from random import sample, uniform
from sys import exit
from decimal import Decimal, InvalidOperation
from os import name, system, path, makedirs, getcwd
from time import sleep
from datetime import datetime
import json

def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)
    

class Bank:
    client_base = {}
    def add_bank_client_to_the_client_base(client_base, all_currency, login, id):
        if login not in client_base.keys():
            client_base[login] = [id]
            for i in range(4):
                client_base[login].append([all_currency[i], 'not open'])
            Bank.serialization(client_base)
            print(f'Your login: {login}. Your ID: {id}.')
            # directory_folder = r'C:\Users\Анастасия\dev\Tasks\homework5\bank_system\all_client_operations' + '\\' + str(login) + '.txt'
            cwd = getcwd()
            directory_folder = path.join(cwd, 'homework5', 'bank_system', 'all_client_operations', str(login) + '.txt')
            folder_path = path.dirname(directory_folder)
            if not path.exists(folder_path):
                makedirs(folder_path)
            with open(directory_folder, 'a') as file:
                file.write(f'Operations of {login}: ')

        else:
            print(f'Account with this login "{login}" exist, please, try again:(')
            login = input('Enter your first and last name. ')
            id = ''.join(map(str, sample(range(0, 10), 3)))
            Bank.add_bank_client_to_the_client_base(client_base, all_currency, login, id)

    @staticmethod
    def for_help():
        print('To get help, contact support (available also by phone - 999).')
        exit()

    def more_or_less(available, for_withdrawal, name_of_currency):
        if Decimal(available) >= for_withdrawal:
            return for_withdrawal
        for_withdrawal = Decimal(input(f'Enter amount in {name_of_currency} for withdrawal less or equal to {available}: '))
        Bank.more_or_less(available, for_withdrawal, name_of_currency)

    @staticmethod
    def serialization(all_clients):
        with open('client_base.json', 'w') as fh:
            fh.write(json.dumps(all_clients, indent=4, cls=DecimalEncoder))

    def deserialization():
        with open('client_base.json', 'r') as fh:
            all_clients = json.loads(fh.read())
        return all_clients
    
    def to_record_all_operations(function):
        def wrapper(login, client_base, answer, currency, amount, all_currency):
            # directory_folder = r'C:\Users\Анастасия\dev\Tasks\homework5\bank_system\all_client_operations' + '\\' + str(login) + '.txt'
            cwd = getcwd()
            directory_folder = path.join(cwd, 'homework5', 'bank_system', 'all_client_operations', str(login) + '.txt')            
            actual_base = Bank.deserialization()
            result = f'BYN: {actual_base[login][1][1]}. USD: {actual_base[login][2][1]}. EUR: {actual_base[login][3][1]}. RUB: {actual_base[login][4][1]}'
            operations = f'Operation: {function.__name__}. Time: {datetime.now()}. Operation: {answer}. Currency: {all_currency[currency]}. Amount: {amount}. Balance: {result}.'
            with open(directory_folder, 'a') as file:
                file.write('\n')
                file.write(operations)
                file.write('\n')
            return function(login, client_base, answer, currency, amount, all_currency)
        return wrapper

class BankClient:
    def __init__(self, client_name, id):
        self.name = client_name
        self._id = id

    def check_client(login, id, client_base, attempts_enter_login, attempts_enter_id):
        try:
            if client_base[login][0] == id:
                print(f'Welcome, {login}!')
                return login
            else: 
                print(f"Uncorrect ID. Try again or use command '#3' (help)!")
                attempts_enter_id -= 1
                if attempts_enter_id != 0:
                    id = str(input('Enter your ID (9 numbers): '))
                    if id == '#3':
                        Bank.for_help()
                        exit()
                    return BankClient.check_client(login, id, client_base, attempts_enter_login, attempts_enter_id)
                else:
                    print('The limit of attempts has been exceeded! Try some later:(')
                    if input('Do you need help? Enter "yes" or "no": ').lower() == 'yes':
                        Bank.for_help()
                    print('Try later.')
                    for second in range(5, 0, -1): #ИСПРАВИТЬ ТАЙМЕР
                        sleep(1.0)
                        print(second, end='... ')
                    print()
                    attempts_enter_login = 5
                    id = str(input('Enter your ID (9 numbers): '))
                    return BankClient.check_client(login, id, client_base, attempts_enter_login, attempts_enter_id)
        except KeyError as log:
            print(f"Account with login {log} doesn't exist. Try again or use command '#3' (help)!")
            attempts_enter_login -= 1
            if attempts_enter_login != 0:
                login = input('Enter your login: ')
                if login == '#3':
                    Bank.for_help()
                    exit()
                return BankClient.check_client(login, id, client_base, attempts_enter_login, attempts_enter_id)
            else:
                print('The limit of attempts has been exceeded! Try some later:(')
                if input('Do you need help? Enter "yes" or "no": ').lower() == 'yes':
                    Bank.for_help()
                    exit()
                print('Try later.')
                for second in range(10, 0, -1): # ИСПРАВИТЬ ТАЙМЕР!
                    sleep(1.0)
                    print(second, end='... ')
                print()
                attempts_enter_login = 5
                login = input('Enter your login: ')
                return BankClient.check_client(login, id, client_base, attempts_enter_login, attempts_enter_id)


class BankAccount:
    all_code_currency = {
        933: 'BYN', # index_code: [1]
        840: 'USD', # index_code: [2]
        978: 'EUR', # index_code: [3]
        643: 'RUB', # index_code: [4]
    }

    all_actions_with_currency = {
        '+': 'Replenish balance or create account.',
        '-': 'Withdraw money.',
        '?': 'Check balance.',
        '***': 'Check all transaction history.',
    }

    @staticmethod
    def create_bank_account(login, currency, client_base, all_currency):
        if currency == 933:
            client_base[login][1][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_currency[currency]} is open.')
        elif currency == 840:
            client_base[login][2][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_currency[currency]} is open.')
        elif currency == 978:
            client_base[login][3][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_currency[currency]} is open.')
        elif currency == 643:
            client_base[login][4][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_currency[currency]} is open.')
        else:
            print(f'Code {currency} does not match the currency.')
            currency = int(input('Enter new code: '))
            print(*all_currency.items(), sep='\n')
            BankAccount.create_bank_account(login, currency, client_base, all_currency)

    @Bank.to_record_all_operations
    @staticmethod
    def change_bank_account(login, client_base, answer, currency, amount, all_currency):
        if currency == 933:
            if answer == '+':
                client_base[login][1][1] = Decimal(f'{(Decimal(client_base[login][1][1]) + amount):.2f}')
                Bank.serialization(client_base)
            elif answer == '-':
                try:
                    if Decimal(client_base[login][1][1]) - amount < 0:
                        if Decimal(client_base[login][1][1]) == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][1][1]}. You cannot charge more than this amount.')
                    else:
                        client_base[login][1][1] = Decimal(f'{(Decimal(client_base[login][1][1]) - amount):.2f}')
                        Bank.serialization(client_base)
                except Exception as error:
                    print(error)
                    try:
                        amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][1][1]} in {all_currency[currency]}: '))
                        BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
                    except TypeError:
                        print(f'Your input {amount} is not an amount, use only numbers! ')
        elif currency == 840:
            if answer == '+':
                client_base[login][2][1] = Decimal(f'{(Decimal(client_base[login][2][1]) + amount):.2f}')
                Bank.serialization(client_base)
            elif answer == '-':
                try:
                    if Decimal(client_base[login][2][1]) - amount < 0:
                        if Decimal(client_base[login][2][1]) == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][2][1]}. You cannot charge more than this amount.')
                    else:
                        client_base[login][2][1] = Decimal(f'{(Decimal(client_base[login][2][1]) - amount):.2f}')
                        Bank.serialization(client_base)
                except Exception as error:
                    print(error)
                    try:
                        amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][2][1]} in {all_currency[currency]}: '))
                        BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
                    except TypeError:
                        print(f'Your input {amount} is not an amount, use only numbers! ')
        elif currency == 978:
            if answer == '+':
                client_base[login][3][1] = Decimal(f'{(Decimal(client_base[login][3][1]) + amount):.2f}')
                Bank.serialization(client_base)
            elif answer == '-':
                try:
                    if Decimal(client_base[login][3][1]) - amount < 0:
                        if Decimal(client_base[login][3][1]) == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][3][1]}. You cannot charge more than this amount.')
                    else:
                        client_base[login][3][1] = Decimal(f'{(Decimal(client_base[login][3][1]) - amount):.2f}')
                        Bank.serialization(client_base)
                except Exception as error:
                    print(error)
                    try:
                        amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][3][1]} in {all_currency[currency]}: '))
                        BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
                    except TypeError:
                        print(f'Your input {amount} is not an amount, use only numbers! ')
        elif currency == 643:
            if answer == '+':
                client_base[login][4][1] = Decimal(f'{(Decimal(client_base[login][4][1]) + amount):.2f}')
                Bank.serialization(client_base)
            elif answer == '-':
                try:
                    if Decimal(client_base[login][4][1]) - amount < 0:
                        if Decimal(client_base[login][4][1]) == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][4][1]}. You cannot charge more than this amount.')
                    else:
                        client_base[login][4][1] = Decimal(f'{(Decimal(client_base[login][1][1]) - amount):.2f}')
                        Bank.serialization(client_base)
                except Exception as error:
                    print(error)
                    try:
                        amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][4][1]} in {all_currency[currency]}: '))
                        BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
                    except TypeError:
                        print(f'Your input {amount} is not an amount, use only numbers! ')        
        else:
            print(f'Something is wrong, check the currency code, please, and try again.')
            print(*all_currency.items(), sep='\n')
            currency = int(input('Enter new currency (only code): '))
            BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)

    @staticmethod
    def check_balance(login, client_base, currency, all_currency):
        try:
            if currency == 933:
                print(f'{login}, your balance in {all_currency[currency]} - {client_base[login][1][1]}')
            elif currency == 840:
                print(f'{login}, your balance in {all_currency[currency]} - {client_base[login][2][1]}')
            elif currency == 978:
                print(f'{login}, your balance in {all_currency[currency]} - {client_base[login][3][1]}')
            elif currency == 643:
                print(f'{login}, your balance in {all_currency[currency]} - {client_base[login][4][1]}')
            else:
                print(f'{login} something is wrong, try again :(')
                print(*all_currency.items(), sep='\n')
                try:
                    currency = int(input('Enter code currency again, please: '))
                    return BankAccount.check_balance(login, client_base, currency, all_currency)
                except ValueError:
                    print('Use only code! ')
                    currency = int(input('Enter code currency again, please: '))
                    return BankAccount.check_balance(login, client_base, currency, all_currency)
        except:
            print(f'{login} something is wrong. Try again! ')
            print(*all_currency.items(), sep='\n')
            currency = int(input('Enter code currency again, please: '))
            return BankAccount.check_balance(login, client_base, currency, all_currency)

    @staticmethod
    def check_history(login):
        # directory_folder = r'C:\Users\Анастасия\dev\Tasks\homework5\bank_system\all_client_operations' + '\\' + str(login) + '.txt'
        cwd = getcwd()
        directory_folder = path.join(cwd, 'homework5', 'bank_system', 'all_client_operations', str(login) + '.txt')
        with open(directory_folder, 'r') as file:
            all_transactions = file.read()
        print(all_transactions)

all_start_actions = {
    1: 'Create new client account',
    2: 'Login to client account',
    3: 'Exit',
    }

def create_new_account():
    new_client = BankClient(input('Enter your first and last name. '), ''.join(map(str, sample(range(0, 10), 3)))) #ВЕРНУТЬ НОРМ ID!!!!
    all_clients = Bank.deserialization()
    if len(all_clients) == 0:
        all_clients = Bank.client_base
    Bank.add_bank_client_to_the_client_base(all_clients, list(BankAccount.all_code_currency.keys()), login=new_client.name, id=new_client._id)
    print('Use them to login to your new bank account!')
    print('Important! remember your ID, it is necessary to use the system.')
    for second in range(5, 0, -1): # ИМЗЕНИТЬ КОЛИЧЕСТВО СЕКУНД -> 60 !!!!
        sleep(1.0)
        print(second, end='... ')
    print()
    return login_to_account()

def login_to_account():
    login = input('Enter your login: ')
    id = str(input('Enter your ID (9 numbers): '))
    # print(f'{login=}, {id=}') # нЕ ЗАБЫТЬ УДАЛИТЬ!!!
    all_clients = Bank.deserialization()
    total_attempts_login = 5
    total_attempts_id = 5
    login = BankClient.check_client(login, id, all_clients, total_attempts_login, total_attempts_id)
    all_currency = BankAccount.all_code_currency
    answer = ''
    currency = 0
    created_accounts = []
    flag = False
    amount = 0
    while answer.lower() != 'stop':
        print(*BankAccount.all_actions_with_currency.items(), sep='\n')
        print(f'What would you do, {login}?')
        print('Enter "stop" for exit!')
        answer = str(input('Enter your answer here, please: '))
        if answer.lower() == 'stop':
            print(f'Ok, {login}, see you!')
            break
        print(*all_currency.items(), sep='\n')
        if answer != '***':
            try:
                currency = int(input('Select the currency (enter only code, please!): '))
            except ValueError:
                print(f'{currency} is not code. Maybe you wanted to do something else? Try again.')
            try:
                check_error = all_currency[currency]
            except KeyError:
                print(f'Code {currency} does not exist! Try again.')
                continue
        if answer in '+-':
            if len([k for k in range(1, 5) if all_clients[login][k][1] != 'not open']) == 0:
                print('You have no created account!')
                if str(input(f'Would you create account in {all_currency[currency]}? Enter "yes" or "no": ')).lower() == 'yes':
                    BankAccount.create_bank_account(login, currency, all_clients, all_currency)
            else:
                for j in range(1, 5):
                    if all_clients[login][j][1] != 'not open':
                        if all_currency[all_clients[login][j][0]] not in created_accounts:
                            created_accounts.append(all_currency[all_clients[login][j][0]])
                            if all_clients[login][j][0] == currency:
                                flag = True

                if flag:
                    if len(created_accounts) >= 2:
                        print(f'{login}, do you want to transfer money from an already created account in another currency?')
                        yes_or_no = input('Enter "yes" or "no": ').lower()
                        if yes_or_no == 'yes':
                            print(*all_currency.items(), sep='\n')
                            print(f'IMPORTANT! You have accounts in: {', '.join(created_accounts)}. Use only their codes!')
                            try:
                                currency_from = int(input(f'Select the currency code from which you want to transfer the amount (except {all_currency[currency]}): '))
                                if currency_from == currency or currency_from not in all_currency.keys() or all_currency[currency_from] not in created_accounts:
                                    print('Something is wrong:( Try again.')
                                if currency == 933:
                                    if currency_from == 840:
                                        available_amount = Decimal(all_clients[login][2][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(3.0, 3.3))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, amount * currency_rate, all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 978:
                                        available_amount = Decimal(all_clients[login][3][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(3.4, 3.6))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, amount * currency_rate, all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 643:
                                        available_amount = Decimal(all_clients[login][4][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(0.035, 0.036))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, amount * currency_rate, all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    else:
                                        print('Use only special currency codes! Try again.')
                                elif currency == 840:
                                    if currency_from == 933:
                                        available_amount = Decimal(all_clients[login][1][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(3.0, 3.3))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount / currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 978:
                                        available_amount = Decimal(all_clients[login][3][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(1.0, 1.1))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 643:
                                        available_amount = Decimal(all_clients[login][4][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(0.01 - 0.02))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    else:
                                        print('Use only special currency codes! Try again.')
                                elif currency == 978:
                                    if currency_from == 933:
                                        available_amount = Decimal(all_clients[login][1][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(3.40, 3.60))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount / currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 840:
                                        available_amount = Decimal(all_clients[login][2][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(0.9, 1.0))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 643:
                                        available_amount = Decimal(all_clients[login][4][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(0.01, 0.02))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    else:
                                        print('Use only special currency codes! Try again.')
                                elif currency == 643:
                                    if currency_from == 840:
                                        available_amount = Decimal(all_clients[login][2][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(0.035, 0.036))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 978:
                                        available_amount = Decimal(all_clients[login][3][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(97.0, 110.0))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    elif currency_from == 933:
                                        available_amount = Decimal(all_clients[login][1][1])
                                        print(f'{login}, you have {available_amount} in {all_currency[currency_from]}.')
                                        amount = Decimal(input(f'Enter amount in {all_currency[currency_from]} for withdrawal: '))
                                        if available_amount < amount:
                                            amount = Bank.more_or_less(available_amount, amount, all_currency[currency_from])
                                        currency_rate = Decimal(uniform(0.035, 0.036))
                                        BankAccount.change_bank_account(login, all_clients, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'), all_currency)
                                        answer = '-'
                                        BankAccount.change_bank_account(login, all_clients, answer, currency_from, amount, all_currency)
                                    else:
                                        print('Use only special currency codes! Try again.')
                            except (ValueError, TypeError, InvalidOperation):
                                if ValueError:
                                    print(f'Something is wrong. Check currency code and for amount use only numbers! Try again.')
                        elif yes_or_no == 'no':
                            amount = Decimal(input(f'Enter amount in {all_currency[currency]}: '))
                            BankAccount.change_bank_account(login, all_clients, answer, currency, amount, all_currency)
                        else:
                            print("Something is wrong (the requested account may not have been created) :( Let's try it again.")
                else:
                    print(f'Account in {all_currency[currency]} is not open. You have accounts: {', '.join(created_accounts)}.')
                    if input(f'Would you create account in {all_currency[currency]}? Enter "yes" or "no": ').lower() == 'yes':
                        BankAccount.create_bank_account(login, currency, all_clients, all_currency)
        elif answer == '?':
            BankAccount.check_balance(login, all_clients, currency, all_currency)
        elif answer == '***':
            BankAccount.check_history(login)
        else:
            print(f"{answer} isn't correct:( Try again...")
        
        print(f'What would you do next, {login}?')
    
    exit()

def simple_bank_system(): # Функция, определяющая возможные действия пользователя.
    print(*all_start_actions.items(), sep='\n')
    try:
        answer = int(input('What would you do? Please, enter command code. '))
        if answer == 1:
            create_new_account()
        elif answer == 2:
            login_to_account()
        elif answer == 3:
            exit()
        else:
            print(f'Answer {answer} is incorrect. Please, enter correct value!')
            return simple_bank_system()
    except ValueError:
        print('Use only numeric commands!')
        simple_bank_system()
    

simple_bank_system() # Запуск всей программы.


'''
Курс валют
1 USD = 3.0 - 3.3
1 EUR = 3.40 - 3.60
100 RUB = 3.50 - 3.60 / (1 RUB * NUM) / 100 = 0.035 - 0.036
1 USD = 0.9 - 1 EUR / 89 - 100 RUB
1 EUR = 1 - 1.10 USD / 97 - 110
1 RUB = 0.01 - 0.02 USD / EUR


        933: 'BYN', # index_code: [1]
        840: 'USD', # index_code: [2]
        978: 'EUR', # index_code: [3]
        643: 'RUB', # index_code: [4]
'''