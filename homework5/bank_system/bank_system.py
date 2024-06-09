from random import sample, uniform
from sys import exit
from decimal import Decimal, InvalidOperation
from os import name, system, path, makedirs, getcwd
from time import sleep
from datetime import datetime
import json

client_base = {} 
all_start_actions = {
    1: 'Create new client account',
    2: 'Login to client account',
    3: 'Exit',
    }

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

class BankClient:
    def __init__(self):
        new_client_name = input('Enter your first and last name. ')
        _id = ''.join(map(str, sample(range(0, 10), 9)))
        self.name = new_client_name
        self._id = _id
        client_base = Bank.deserialization()
        if self.name not in client_base.keys():
            print(f'Your login: {self.name}. Your id: {self._id}.')
            print('Use them to login to your new bank account!')
            print('Important! remember your ID, it is necessary to use the system.')
            for second in range(30, 0, -1):
                sleep(0.8)
                print(f'{second}...', end='\r')
            client_base[self.name] = [self._id]
            for i in range(4):
                codes = list(all_code_currency.keys())
                client_base[self.name].append([codes[i], 'not open'])
            Bank.serialization(client_base)
            cwd = getcwd()
            directory_folder = path.join(cwd, 'homework5', 'bank_system', 'all_client_operations', str(self.name) + '.txt')
            # directory_folder = path.join(cwd, 'all_client_operations', str(self.name) + '.txt')
            folder_path = path.dirname(directory_folder)
            if not path.exists(folder_path):
                makedirs(folder_path)
            with open(directory_folder, 'a') as file:
                file.write(f'Operations of {self.name}: ')
        else:
            print(f'Account with this login "{self.name}" exist, please, try again:(')
            new_client = BankClient()

class Bank(BankClient):

    @staticmethod
    def serialization(all_clients):
        cwd = getcwd()
        base = path.join(cwd, 'homework5', 'bank_system', 'client_base.json')
        # base = path.join(cwd, 'client_base.json')
        with open(base, 'w') as fh:
            fh.write(json.dumps(all_clients, indent=4, cls=DecimalEncoder))

    @staticmethod
    def deserialization():
        cwd = getcwd()
        base = path.join(cwd, 'homework5', 'bank_system', 'client_base.json')
        # base = path.join(cwd, 'client_base.json')
        with open(base, 'r') as fh:
            all_clients = json.loads(fh.read())
        return all_clients
    
    @staticmethod
    def for_help():
        clear_terminal()
        print('To get help, contact support (available also by phone - 999).')
        exit()

    @staticmethod
    def to_record_all_operations(function):
        def wrapper(login, answer, currency, amount):
            global all_code_currency
            cwd = getcwd()
            directory_folder = path.join(cwd, 'homework5', 'bank_system', 'all_client_operations', str(login) + '.txt')            
            actual_base = Bank.deserialization()
            result = f'BYN: {actual_base[login][1][1]}. USD: {actual_base[login][2][1]}. EUR: {actual_base[login][3][1]}. RUB: {actual_base[login][4][1]}'
            operations = f'Operation: {function.__name__}. Time: {datetime.now()}. Operation: {answer}. Currency: {all_code_currency[currency]}. Amount: {amount}. Balance: {result}.'
            with open(directory_folder, 'a') as file:
                file.write('\n')
                file.write(operations)
                file.write('\n')
            return function(login, answer, currency, amount)
        return wrapper

class BankAccount(Bank):
    def __init__(self):
        self.login = input('Enter your login: ')
        self.id = str(input('Enter your ID (9 numbers): '))

    @staticmethod
    def check_client(login, id, attempts_enter_id, attempts_enter_login):
        client_base = Bank.deserialization()
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
                    return BankAccount.check_client(login, id, attempts_enter_id, attempts_enter_login)
                else:
                    print('The limit of attempts has been exceeded! Try some later:(')
                    if input('Do you need help? Enter "yes" or "no": ').lower() == 'yes':
                        Bank.for_help()
                    print('Try later.')
                    for second in range(30, 0, -1): 
                        sleep(0.8)
                        print(f'{second}...', end='\r')
                    print()
                    attempts_enter_login = 5
                    id = str(input('Enter your ID (9 numbers): '))
                    return BankAccount.check_client(login, id, attempts_enter_id, attempts_enter_login)
        except KeyError as login:
            print(f"Account with login {login} doesn't exist. Try again or use command '#3' (help)!")
            attempts_enter_login -= 1
            if attempts_enter_login != 0:
                login = input('Enter your login: ')
                if login == '#3':
                    Bank.for_help()
                    exit()
                return BankAccount.check_client(login, id, attempts_enter_id, attempts_enter_login)
            else:
                print('The limit of attempts has been exceeded! Try some later:(')
                if input('Do you need help? Enter "yes" or "no": ').lower() == 'yes':
                    Bank.for_help()
                    exit()
                print('Try later.')
                for second in range(30, 0, -1): 
                    sleep(0.8)
                    print(f'{second}...', end='\r')
                print()
                attempts_enter_login = 5
                login = input('Enter your login: ')
                return BankAccount.check_client(login, id, attempts_enter_id, attempts_enter_login)

    @staticmethod
    def create_bank_account(login, currency):
        client_base = Bank.deserialization()
        if currency == 933:
            client_base[login][1][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_code_currency[currency]} is open.')
        elif currency == 840:
            client_base[login][2][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_code_currency[currency]} is open.')
        elif currency == 978:
            client_base[login][3][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_code_currency[currency]} is open.')
        elif currency == 643:
            client_base[login][4][1] = 0
            Bank.serialization(client_base)
            print(f'Account {all_code_currency[currency]} is open.')
        else:
            print(f'Code {currency} does not match the currency.')
            currency = int(input('Enter new code: '))
            print(*all_code_currency.items(), sep='\n')
            BankAccount.create_bank_account(login, currency)

    def use_account(self):
        answer = ''
        created_accounts = []
        amount = 0
        while answer.lower() != 'stop':
            all_clients = Bank.deserialization()
            flag = False
            print(*all_actions_with_currency.items(), sep='\n')
            print(f'What would you do, {self.login}?')
            print('Enter "stop" for exit!')
            answer = str(input('Enter your answer here, please: '))
            if answer.lower() == 'stop':
                print(f'Ok, {self.login}, see you!')
                break
            print(*all_code_currency.items(), sep='\n')
            if answer != '***':
                try:
                    currency = int(input('Select the currency (enter only code, please!): '))
                    check_error = all_code_currency[currency]
                except (ValueError, KeyError):
                    print(f'{currency} is not code or code {currency} does not exist! Try again.')
                    continue
            if answer in '+-':
                if len([k for k in range(1, 5) if all_clients[self.login][k][1] != 'not open']) == 0:
                    print('You have no created account!')
                    if str(input(f'Would you create account in {all_code_currency[currency]}? Enter "yes" or "no": ')).lower() == 'yes':
                        BankAccount.create_bank_account(self.login, currency)
                else:
                    if all_code_currency[currency] in created_accounts:
                        flag = True
                    else:
                        for j in range(1, 5):
                            if all_clients[self.login][j][1] != 'not open':
                                if all_code_currency[all_clients[self.login][j][0]] not in created_accounts:
                                    created_accounts.append(all_code_currency[all_clients[self.login][j][0]])
                                    if all_clients[self.login][j][0] == currency:
                                        flag = True

                    if flag:
                        if len(created_accounts) >= 2 and answer != '-':
                            print(f'{self.login}, do you want to transfer money from an already created account in another currency?')
                            yes_or_no = input('Enter "yes" or "no": ').lower()
                            if yes_or_no == 'yes':
                                print(*all_code_currency.items(), sep='\n')
                                print(f'IMPORTANT! You have accounts in: {', '.join(created_accounts)}. Use only their codes!')
                                try:
                                    currency_from = int(input(f'Select the currency code from which you want to transfer the amount (except {all_code_currency[currency]}): '))
                                    if currency_from == currency or currency_from not in all_code_currency.keys() or all_code_currency[currency_from] not in created_accounts:
                                        print('Something is wrong:( Try again.')
                                    if currency == 933:
                                        if currency_from == 840:
                                            available_amount = Decimal(all_clients[self.login][2][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(3.0, 3.3))
                                            BankAccount.change_bank_account(self.login, answer, currency, amount * currency_rate)
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 978:
                                            available_amount = Decimal(all_clients[self.login][3][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(3.4, 3.6))
                                            BankAccount.change_bank_account(self.login, answer, currency, amount * currency_rate)
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 643:
                                            available_amount = Decimal(all_clients[self.login][4][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(0.035, 0.036))
                                            BankAccount.change_bank_account(self.login, answer, currency, amount * currency_rate)
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        else:
                                            print('Use only special currency codes! Try again.')
                                    elif currency == 840:
                                        if currency_from == 933:
                                            available_amount = Decimal(all_clients[self.login][1][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(3.0, 3.3))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount / currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 978:
                                            available_amount = Decimal(all_clients[self.login][3][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(1.0, 1.1))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 643:
                                            available_amount = Decimal(all_clients[self.login][4][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(0.01, 0.02))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        else:
                                            print('Use only special currency codes! Try again.')
                                    elif currency == 978:
                                        if currency_from == 933:
                                            available_amount = Decimal(all_clients[self.login][1][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(3.40, 3.60))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount / currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 840:
                                            available_amount = Decimal(all_clients[self.login][2][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(0.9, 1.0))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 643:
                                            available_amount = Decimal(all_clients[self.login][4][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(0.01, 0.02))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        else:
                                            print('Use only special currency codes! Try again.')
                                    elif currency == 643:
                                        if currency_from == 840:
                                            available_amount = Decimal(all_clients[self.login][2][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(89, 100))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 978:
                                            available_amount = Decimal(all_clients[self.login][3][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(97.0, 110.0))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount * currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        elif currency_from == 933:
                                            available_amount = Decimal(all_clients[self.login][1][1])
                                            if available_amount == 0:
                                                print('You cannot use this account, because it has no money.')
                                                continue
                                            print(f'{self.login}, you have {available_amount} in {all_code_currency[currency_from]}.')
                                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency_from]} for withdrawal: '))
                                            if available_amount < amount:
                                                amount = BankAccount.more_or_less(available_amount, amount, all_code_currency[currency_from])
                                            currency_rate = Decimal(uniform(0.035, 0.036))
                                            BankAccount.change_bank_account(self.login, answer, currency, Decimal(f'{(amount / currency_rate):.2f}'))
                                            answer = '-'
                                            BankAccount.change_bank_account(self.login, answer, currency_from, amount)
                                        else:
                                            print('Use only special currency codes! Try again.')
                                except (ValueError, TypeError, InvalidOperation):
                                    if ValueError:
                                        print(f'Something is wrong. Check currency code and for amount use only numbers! Try again.')
                            elif yes_or_no == 'no':
                                try:
                                    amount = Decimal(input(f'Enter amount in {all_code_currency[currency]}: '))
                                    BankAccount.change_bank_account(self.login, answer, currency, amount)
                                except (ValueError, TypeError, InvalidOperation):
                                    print(f'Something is wrong. Check currency code and for amount use only numbers! Try again.')
                            else:
                                print("Something is wrong (the requested account may not have been created) :( Let's try it again.")
                        else:
                            amount = Decimal(input(f'Enter amount in {all_code_currency[currency]}: '))
                            BankAccount.change_bank_account(self.login, answer, currency, amount)
                    else:
                        print(f'Account in {all_code_currency[currency]} is not open. You have accounts: {', '.join(created_accounts)}.')
                        if input(f'Would you create account in {all_code_currency[currency]}? Enter "yes" or "no": ').lower() == 'yes':
                            BankAccount.create_bank_account(self.login, currency)
            elif answer == '?':
                BankAccount.check_balance(self.login, currency)
            elif answer == '***':
                BankAccount.check_history(self.login)
            else:
                print(f"{answer} isn't correct:( Try again...")
            
            print(f'What would you do next, {self.login}?')
        
        exit()

    @Bank.to_record_all_operations
    @staticmethod
    def change_bank_account(login, answer, currency, amount):
        client_base = Bank.deserialization()
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
                    if Decimal(client_base[login][1][1]) != 0:
                        try:
                            amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][1][1]} in {all_code_currency[currency]}: '))
                            BankAccount.change_bank_account(answer, currency, amount)
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
                    if Decimal(client_base[login][2][1]) != 0:
                        try:
                            amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][2][1]} in {all_code_currency[currency]}: '))
                            BankAccount.change_bank_account(answer, currency, amount)
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
                    if Decimal(client_base[login][3][1]) != 0:
                        try:
                            amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][3][1]} in {all_code_currency[currency]}: '))
                            BankAccount.change_bank_account(client_base, answer, currency, amount)
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
                    if Decimal(client_base[login][4][1]) != 0:
                        try:
                            amount = Decimal(input(f'Enter new amount less than or equal to {client_base[login][4][1]} in {all_code_currency[currency]}: '))
                            BankAccount.change_bank_account(answer, currency, amount)
                        except TypeError:
                            print(f'Your input {amount} is not an amount, use only numbers! ')        
        else:
            print(f'Something is wrong, check the currency code, please, and try again.')
            print(*all_code_currency.items(), sep='\n')
            currency = int(input('Enter new currency (only code): '))
            BankAccount.change_bank_account(client_base, answer, currency, amount)

    @staticmethod
    def more_or_less(available, for_withdrawal, name_of_currency):
        if Decimal(available) >= for_withdrawal:
            return for_withdrawal
        for_withdrawal = Decimal(input(f'Enter amount in {name_of_currency} for withdrawal less or equal to {available}: '))
        BankAccount.more_or_less(available, for_withdrawal, name_of_currency)

    @staticmethod
    def check_balance(login, currency):
        client_base = Bank.deserialization()
        try:
            if currency == 933:
                print(f'{login}, your balance in {all_code_currency[currency]} - {client_base[login][1][1]}')
            elif currency == 840:
                print(f'{login}, your balance in {all_code_currency[currency]} - {client_base[login][2][1]}')
            elif currency == 978:
                print(f'{login}, your balance in {all_code_currency[currency]} - {client_base[login][3][1]}')
            elif currency == 643:
                print(f'{login}, your balance in {all_code_currency[currency]} - {client_base[login][4][1]}')
            else:
                print(f'{login} something is wrong, try again :(')
                print(*all_code_currency.items(), sep='\n')
                try:
                    currency = int(input('Enter code currency again, please: '))
                    return BankAccount.check_balance(login, currency)
                except ValueError:
                    print('Use only code! ')
                    currency = int(input('Enter code currency again, please: '))
                    return BankAccount.check_balance(login, currency)
        except:
            print(f'{login} something is wrong. Try again! ')
            print(*all_code_currency.items(), sep='\n')
            currency = int(input('Enter code currency again, please: '))
            return BankAccount.check_balance(login, currency)

    @staticmethod
    def check_history(login):
        cwd = getcwd()
        directory_folder = path.join(cwd, 'homework5', 'bank_system', 'all_client_operations', str(login) + '.txt')
        with open(directory_folder, 'r') as file:
            all_transactions = file.read()
        print(all_transactions)

def simple_bank_system():
    print(*all_start_actions.items(), sep='\n')
    try:
        answer = int(input('What would you do? Please, enter command code. '))
        if answer == 1:
            new_client = BankClient()
            client_account = BankAccount()
            client_account.login = BankAccount.check_client(client_account.login, client_account.id, attempts_enter_id=5, attempts_enter_login=5)
            client_account.use_account()
        elif answer == 2:
            client_account = BankAccount()
            client_account.login = BankAccount.check_client(client_account.login, client_account.id, attempts_enter_id=5, attempts_enter_login=5)
            client_account.use_account()
        elif answer == 3:
            exit()
        else:
            print(f'Answer {answer} is incorrect. Please, enter correct value!')
            return simple_bank_system()
    except ValueError:
        print('Use only numeric commands!')
        simple_bank_system()
    
clear_terminal()
simple_bank_system()       