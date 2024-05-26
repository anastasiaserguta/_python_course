from random import sample
from sys import exit
from decimal import Decimal
from os import name, system
from time import sleep

class Bank:
    client_base = {}
    def add_bank_client_to_the_client_base(client_base, all_currency, *, login, id):
        if login not in client_base.keys():
            client_base[login] = [id]
            for i in range(4):
                client_base[login].append([all_currency[i], 'not open'])
            print(client_base)
        else:
            print(f'Account with this login "{login}" exist, please, try again:(')



class BankClient:
    def __init__(self, client_name, id):
        self.name = client_name
        self._id = id

    @staticmethod
    def check_client(login, id, client_base, attempts):
        try:
            if client_base[login][0] == id:
                if name == 'nt':
                    system('cls')
                else:
                    system('clear')
                return f'Welcome, {login}!'
            else: 
                print(f"Uncorrect ID. Try again or use command '3' (help)!")
                id = str(input('Enter your ID (9 numbers): '))
                if name == 'nt':
                    system('cls')
                else:
                    system('clear')
                return BankClient.check_client(login, id, client_base, attempts)
        except KeyError as log:
            print(f"Account with login {log} doesn't exist. Try again or use command '#3' (help)!") # КОМАНДА 3 НЕ СОЗДАНА!!!!
            attempts -= 1
            if attempts != 0:
                login = input('Enter your login: ')
                return BankClient.check_client(login, id, client_base, attempts)
            elif login == '#3':
                return 'To get help, contact support (available also by phone - 999).'
            else:
                print('The limit of attempts has been exceeded! Try some later:(')
                for i in range(60, 0, -1):
                    print(i)
                    sleep(1.0)
                    if name == 'nt':
                        system('cls')
                    else:
                        system('clear')
                attempts = 5
                login = input('Enter your login: ')
                return BankClient.check_client(login, id, client_base, attempts)


class BankAccount:
    all_code_currency = {
        933: 'BYN', # index_code: [1]
        840: 'USD', # index_code: [2]
        978: 'EUR', # index_code: [3]
        643: 'RUB', # index_code: [4]
    }

    all_actions_with_currency = {
        '+': 'Replenish balance.',
        '-': 'Withdraw money.',
        '?': 'Check balance.',
        '***': 'Check all transaction history.',
    }

    @staticmethod
    def create_bank_account(login, currency, client_base, all_currency):
        if currency == 933:
            client_base[login][1][1] = 0
            print(f'Account {all_currency[currency]} is open.')
        elif currency == 840:
            client_base[login][2][1] = 0
            print(f'Account {all_currency[currency]} is open.')
        elif currency == 978:
            client_base[login][3][1] = 0
            print(f'Account {all_currency[currency]} is open.')
        elif currency == 643:
            client_base[login][4][1] = 0
            print(f'Account {all_currency[currency]} is open.')
        else:
            print(f'Code {currency} does not match the currency.')
            currency = int(input('Enter new code: '))
            print(*all_currency.items(), sep='\n')
            BankAccount.create_bank_account(login, currency, client_base, all_currency)

    @staticmethod
    def change_bank_account(login, client_base, answer, currency, amount, all_currency):
        if currency == 933:
            if answer == '+':
                client_base[login][1][1] += amount
            elif answer == '-':
                try:
                    if client_base[login][1][1] - amount < 0:
                        if client_base[login][1][1] == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][1][1]}. You cannot charge more than this amount.')
                except Exception as error:
                    print(error)
                    amount = Decimal(input(f'Enter new amount less than or equal to than {client_base[login][1][1]} in {all_currency[currency]}: '))
                    BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
            
        elif currency == 840:
            if answer == '+':
                client_base[login][2][1] += amount
            elif answer == '-':
                try:
                    if client_base[login][2][1] - amount < 0:
                        if client_base[login][2][1] == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][2][1]}. You cannot charge more than this amount.')
                except:
                    amount = Decimal(input(f'Enter new amount more than {client_base[login][2][1]} in {all_currency[currency]}: '))
                    BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
        elif currency == 978:
            if answer == '+':
                client_base[login][3][1] += amount
            elif answer == '-':
                try:
                    if client_base[login][3][1] - amount < 0:
                        if client_base[login][3][1] == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][2][1]}. You cannot charge more than this amount.')
                except:
                    amount = Decimal(input(f'Enter new amount more than {client_base[login][3][1]} in {all_currency[currency]}: '))
                    BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
        elif currency == 643:
            if answer == '+':
                client_base[login][4][1] += amount
            elif answer == '-':
                try:
                    if client_base[login][4][1] - amount < 0:
                        if client_base[login][4][1] == 0:
                            raise Exception('Your balance is 0, it is necessary to replenish the balance.') 
                        else:
                            raise Exception(f'Your balance is {client_base[login][2][1]}. You cannot charge more than this amount.')
                except:
                    amount = Decimal(input(f'Enter new amount more than {client_base[login][4][1]} in {all_currency[currency]}: '))
                    BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)
        else:
            print(f'Something is wrong, check the currency code, please, and try again.')
            print(*all_currency.items(), sep='\n')
            currency = int(input('Enter new currency (only code): '))
            BankAccount.change_bank_account(login, client_base, answer, currency, amount, all_currency)

    def save_history():
        
        pass



all_start_actions = {
    1: 'Create new client account',
    2: 'Login to client account',
    3: 'Exit',
    }

def create_new_account():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    new_client = BankClient(input('Enter your first and last name. '), ''.join(map(str, sample(range(0, 10), 3)))) #ВЕРНУТЬ НОРМ ID!!!!
    Bank.add_bank_client_to_the_client_base(Bank.client_base, list(BankAccount.all_code_currency.keys()), login=new_client.name, id=new_client._id)
    for second in range(30, 0, -1):
        print(second)
        sleep(1)
        print(f'Your login: {new_client.name}. Your ID: {new_client._id}.')
        print('Use them to login to your new bank account!')
        print('Important! remember your ID, it is necessary to use the system.')
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    return login_to_account()

def login_to_account():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    login = input('Enter your login: ')
    id = str(input('Enter your ID (9 numbers): '))
    print(f'УДАЛИТЬ {login=}, {id=}') # нЕ ЗАБЫТЬ УДАЛИТЬ!!!
    all_clients = Bank.client_base
    total_attempts = 5
    BankClient.check_client(login, id, all_clients, total_attempts)
    sleep(10.0)
    all_currency = BankAccount.all_code_currency
    answer = ''
    currency = 0
    created_accounts = []
    flag = False
    amount = 0
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(*BankAccount.all_actions_with_currency.items(), sep='\n')
    print(f'What would you do, {login}?')
    sleep(3.0)
    while answer != 'stop':
        print('Enter "stop" for exit!')
        answer = input('Enter your answer here, please: ')
        print(*all_currency.items(), sep='\n')
        currency = int(input('Select the currency (enter only code, please!): '))
        if answer in '+-':
            try:
                if len([k for k in range(1, 5) if type(all_clients[login][k][1]) != str]) == 0:
                    print('You have no created account!')
                    if str(input(f'Would you create account in {all_currency[currency]}? Enter "yes" or "no". ')).lower() == 'yes':
                        BankAccount.create_bank_account(login, currency, all_clients, all_currency)
                else:
                    for j in range(1, 5):
                        if type(all_clients[login][j][1]) != str:
                            created_accounts.append(all_currency[all_clients[login][j][0]])
                            if all_clients[login][j][0] == currency:
                                flag = True

                    if flag:
                        amount = Decimal(input(f'Enter amount in {all_currency[currency]}: '))
                        BankAccount.change_bank_account(login, all_clients, answer, currency, amount, all_currency)
                    else:
                        print(f'Account in {all_currency[currency]} is not open. You have accounts: {''.join(created_accounts)}.')
                        if input(f'Would you create account in {all_currency[currency]}? Enter "yes" or "no". ').lower() == 'yes':
                            BankAccount.create_bank_account(login, currency, all_clients)
            except ValueError as value:
                print(f'{value} is not code. Maybe you wanted to do something else? Try again.')
        elif answer in '?***':
            pass
        elif answer == 'stop':
            break    
        else:
            print(f"{answer} isn't correct:( Try again...")
        
        print(f'What would you do next, {login}?')
        print(*BankAccount.all_actions_with_currency.items(), sep='\n')
    
    print(f'Ok, {login}, see you!')
    exit()

def simple_bank_system(): # Функция, определяющая возможные действия пользователя.
    print(*all_start_actions.items(), sep='\n')
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
    

if name == 'nt':
    system('cls')
else:
    system('clear')

simple_bank_system() # Запуск всей программы.


'''
Курс валют
1 USD = 3.0 - 3.3
1 EUR = 3.40 - 3.60
100 RUB = 3.50 - 3.60 / (1 RUB * NUM) / 100 = 0.035 - 0.036
'''