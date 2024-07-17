from random import sample, uniform
from sys import exit
from decimal import Decimal, InvalidOperation
from os import name, system, path, makedirs, getcwd
from time import sleep
from datetime import datetime
import json
import enum
from functools import wraps

class Currency(enum.Enum): # Класс, содержащий коды и наименования валют, а также примерные значения курсов для конвертации.
    BYN = '933'
    USD = '840'
    EUR = '978'
    RUB = '643'

    # Курсы валют.
    BYN_USD_rate = Decimal(uniform(3.0, 3.3))
    BYN_EUR_rate = Decimal(uniform(3.4, 3.6))
    BYN_RUB_rate = Decimal(uniform(0.035, 0.036))
    USD_EUR_rate = Decimal(uniform(0.9, 1.1))
    USD_RUB_rate = Decimal(uniform(0.01, 0.02))
    EUR_RUB_rate = Decimal(uniform(0.01, 0.02))
    RUB_USD_rate = Decimal(uniform(89, 100))
    RUB_EUR_rate = Decimal(uniform(97, 110))

class DecimalEncoder(json.JSONEncoder): # Класс для сериализации Decimal.
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

class Bank: # Класс БАНК. Инициирует базу данных клиентов, сериализует/десериализует ее, содержит метод "обратной связи" с клиентом.
    def __init__(self):
        self.client_base = {} 

    @staticmethod
    def serialization(client_base):
        cwd = getcwd()
        base_dir = path.join(cwd, 'homework5', 'bank_system_ver_after_review', 'client_base.json')
        # base_dir = path.join(cwd, 'client_base.json')
        with open(base_dir, 'w') as fh:
            fh.write(json.dumps(client_base, indent=4, cls=DecimalEncoder))

    @staticmethod
    def deserialization():
        cwd = getcwd()
        base_dir = path.join(cwd, 'homework5', 'bank_system_ver_after_review', 'client_base.json')
        # base_dir = path.join(cwd, 'client_base.json')
        with open(base_dir, 'r') as fh:
            all_clients = json.loads(fh.read())
        return all_clients

    @staticmethod
    def for_help():
        clear_terminal()
        print('To get help, contact support (available also by phone - 999).')
        exit()

class BankAccount: # Класс БАНКОВСКИЙ СЧЕТ. Основной класс для работы со счетом (пополнение, снятие, просмотр баланса и всех транзакций, включая методы валидации обрабатываемых сумм.)
    def __init__(self, login, id):
        self.client_base = Bank.deserialization()
        self.login = login
        self.id = id
        self.balance = 0
        self.amount = 0
        self.status='SUCCES'
        
    def check_active_client(self): # Проверка клиента на предмет наличия в базе.
        try: 
            if self.client_base[self.login][0] != self.id:
                return False
            else:
                return True
        except KeyError:
            raise KeyError
            
    def check_any_open_accounts(self, code_currency='933'): # Проверка наличия открытых аккаунтов.
        try:
            if self.client_base[self.login][1][code_currency] == 'not open':
                return False
            else:
                return True
        except KeyError:
            return False

    def create_account(self, code_currency): # Открытие счета.
        self.client_base[self.login][1][code_currency] = self.balance
        print(f'Account in {Currency(code_currency).name} is open.')

    def replenish_balance(self, code_currency, amount): # Пополнение баланса.
        self.amount = BankAccount.convert_to_decimal(amount)
        self.balance = BankAccount.convert_to_decimal(self.client_base[self.login][1][code_currency]) 
        self.client_base[self.login][1][code_currency] = self.balance + self.amount
        self.status = 'SUCCES'
        print(f'Your balance in {Currency(code_currency).name} is {self.client_base[self.login][1][code_currency]}.')

    def withdraw_money(self, code_currency, amount): # Снятие со счета.
        self.amount = BankAccount.convert_to_decimal(amount)
        self.balance = BankAccount.convert_to_decimal(self.client_base[self.login][1][code_currency])
        if BankAccount.is_valid_operation(self.balance, self.amount):
            self.client_base[self.login][1][code_currency] = self.balance - self.amount
            print(f'Your balance in {Currency(code_currency).name} is {self.client_base[self.login][1][code_currency]}.')
            self.status = 'SUCCES'
            return True
        else:
            print(f'Your amount is equal 0 or balance in {Currency(code_currency).name} is not open or equal 0 or less than amount required for the transfer after conversion.')
            self.status = 'DENIED'
            return False
        
    @staticmethod
    def open_account(): # Метод, определяющих необходимость открытия счета.
        answer = input('Do you want open it? Enter "yes" or "no": ').lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            print('OK.')
        else:
            print('Something is wrong. Try again.')
        return False

    @staticmethod
    def is_valid_operation(balance, amount): # Валидация операции.
        if balance == 'not open':
            return False
        elif amount > balance or balance == 0 or amount == 0:
            return False
        else:
            return True
        
    @staticmethod
    def transfer_money(): # Метод, определяющий необходимость использования одного существующего счета для пополнения другого.
        answer = input('Do you want transfer money from an existing account? Enter "yes" or "no": ').lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            print('OK.')
        else:
            print('Incorrect response. Simple replenishment is allowed.')
        return False
        
    def check_balance(self, code_currency): # Просмотр баланса.
        print(f'Your balance in {Currency(code_currency).name} is {self.client_base[self.login][1][code_currency]}.')

    def record_all_operations(self, action_name, code_currency, amount, code_currency_from=0): # Запись всех транзакций, включая их статус : УСПЕШНО/ОТКАЗАНО.
        cwd = getcwd()
        directory_folder = path.join(cwd, 'homework5', 'bank_system_ver_after_review', 'client_operations', str(self.login) + '.txt')
        if code_currency_from == 0:
            transaction = f'STATUS: {self.status}. Date: {datetime.now()}. Currency: {Currency(code_currency).name}. Action: {action_name}. From account: NOT SELECTED. Amount: {amount}. Account balance: {self.client_base[self.login][1][code_currency]}.'
        else:
            transaction = f'STATUS: {self.status}. Date: {datetime.now()}. Currency: {Currency(code_currency).name}. Action: {action_name}. From account: {Currency(code_currency_from).name}. Amount: {amount}. Account balance: {self.client_base[self.login][1][code_currency]}.'
        with open(directory_folder, 'a') as client_history:
            client_history.write('\n')
            client_history.write(transaction)

    def check_all_transactions(self): # Просмотр истории транзакций.
        cwd = getcwd()
        directory_folder = path.join(cwd, 'homework5', 'bank_system_ver_after_review', 'client_operations', str(self.login) + '.txt')
        with open(directory_folder, 'r') as client_history:
            all_transactions = client_history.read()
        return all_transactions

    @staticmethod
    def convert_to_decimal(x): # Метод конвертации в Decimal.
        if x != 'not open':
            return Decimal(f'{float(x):.2f}')
        else:
            return x

class BankClient: # Класс БАНКОВСКИЙ КЛИЕНТ. Инициирует клиентов, проверяет их на предмет наличия в базе.
    def __init__(self, client_name, _id):
        self.name = client_name
        self._id = _id
        self.client_base = Bank.deserialization()

    def check_new_client(self):
        if self.name not in self.client_base.keys() and self.name != '#3' and self.name != 'help':
            self.client_base[self.name] = [self._id]
            return True
        else: 
            return False
        
    def create_client_account(self):
        cwd = getcwd()
        directory_folder = path.join(cwd, 'homework5', 'bank_system_ver_after_review', 'client_operations', str(self.name) + '.txt')
        # directory_folder = path.join(cwd, 'client_operations', str(self.name) + '.txt')
        with open(directory_folder, 'a') as client_history:
                client_history.write('-' * 75)
        return self.client_base[self.name].append({Currency.BYN.value: 'not open', Currency.USD.value: 'not open', Currency.EUR.value: 'not open', Currency.RUB.value: 'not open'})

def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

all_start_actions = {
    1: 'Create new client account',
    2: 'Login to client account',
    3: 'Exit',
    }

command = ''

all_actions_with_currency = {
        '+': 'Replenish balance or create account.',
        '-': 'Withdraw money.',
        '?': 'Check balance.',
        '***': 'Check all transaction history.',
    }

def timer():
    for second in range(5, -1, -1):
        sleep(0.8)
        print(f'{second}...', end='\r')
    print()
    done = 'READY'
    return done

while command != 'stop':
    print(*all_start_actions.items(), sep='\n')
    try:
        action = int(input('What would you do? Please, enter command code. '))
        if action == 1:
            client_name = input('Enter your first and last name. ')
            _id = ''.join(map(str, sample(range(0, 10), 9)))
            client = BankClient(client_name, _id)
            if client.check_new_client():
                print(f'Your login: {client.name}. Your id: {client._id}.')
                client.create_client_account()
                Bank.serialization(client.client_base)
                print('Use them to login to your new bank account!')
                print('Important! remember your ID, it is necessary to use the system.')
                print(timer())
            else:
                print(f'Account with this login "{client_name}" exist or you use system command like [help, #3], please, try again:(')
        elif action == 2:
            login = input('Enter your login (name): ')
            id = str(input('Enter your ID (9 numbers): '))
            active_client = BankAccount(login, id)
            attempts_enter = 5
            try:
                for _ in range(5):
                    if active_client.check_active_client():
                        print(f'Welcome, {active_client.login}!')
                        while command != 'stop':
                            Bank.serialization(active_client.client_base)
                            print(*all_actions_with_currency.items(), sep='\n')
                            print(f'What would you do, {active_client.login}?')
                            print('Enter "stop" for exit!')
                            command = str(input('Enter your answer here, please: '))
                            if command == 'stop':
                                print(f'Ok, {active_client.login}, see you!')
                                exit()
                            elif command not in all_actions_with_currency.keys():
                                print('Incorrect command! Try again.')
                                continue
                            if command == '***':
                                print(active_client.check_all_transactions())
                                print('-' * 75)
                                continue
                            print(*[f'Code of {i.name} is {i.value}.' for i in list(Currency) if 'rate' not in i.name], sep='\n') # какая-то имба получилась
                            code_currency = str(input('Select the currency (enter only code): '))
                            try:
                                print(f'The account in {Currency(code_currency).name} is selected.')
                            except ValueError as value:
                                print(f'{value}!')
                                continue
                            if active_client.check_any_open_accounts(code_currency):
                                if command == 'stop':
                                    print(f'Ok, {active_client.login}, see you!')
                                    break
                                if command == '+':
                                    if not BankAccount.transfer_money():
                                        try:
                                            amount_for_replenish = input('Enter amount: ')
                                            active_client.replenish_balance(code_currency, amount_for_replenish)
                                            active_client.record_all_operations('withdrawal from account', code_currency, amount_for_replenish)
                                        except ValueError:
                                            print('For amount use only digits!')
                                            continue
                                    else:
                                        code_currency_from = str(input(f'Select the currency code from which you want to transfer the amount (except {Currency(code_currency).name}): '))
                                        if code_currency == code_currency_from:
                                            print('You cannot use the same account!')
                                            continue
                                        try:
                                            print(f'The account in {Currency(code_currency_from).name} is selected for the transfer.')
                                        except ValueError as value:
                                            print(f'{value}!')
                                            continue
                                        try:
                                            if code_currency == Currency.BYN.value:
                                                amount_for_replenish = BankAccount.convert_to_decimal(input(f'Enter amount in {Currency.BYN.name}: '))
                                                if code_currency_from == Currency.USD.value:
                                                    amount_for_withdraw = amount_for_replenish / Currency.BYN_USD_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.EUR.value:
                                                    amount_for_withdraw = amount_for_replenish / Currency.BYN_EUR_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.RUB.value:
                                                    amount_for_withdraw = amount_for_replenish / Currency.BYN_RUB_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                active_client.record_all_operations('balance replenishment', code_currency, amount_for_replenish, code_currency_from)
                                            elif code_currency == Currency.USD.value:
                                                amount_for_replenish = BankAccount.convert_to_decimal(input(f'Enter amount in {Currency.USD.name}: '))
                                                if code_currency_from == Currency.BYN.value:
                                                    amount_for_withdraw = amount_for_replenish * Currency.BYN_USD_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.EUR.value:
                                                    amount_for_withdraw = amount_for_replenish * Currency.USD_EUR_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.RUB.value:
                                                    amount_for_withdraw = amount_for_replenish / Currency.USD_RUB_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                active_client.record_all_operations('balance replenishment', code_currency, amount_for_replenish, code_currency_from)
                                            elif code_currency == Currency.EUR.value:
                                                amount_for_replenish = BankAccount.convert_to_decimal(input(f'Enter amount in {Currency.EUR.name}: '))
                                                if code_currency_from == Currency.BYN.value:
                                                    amount_for_withdraw = amount_for_replenish * Currency.BYN_EUR_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.USD.value:
                                                    amount_for_withdraw = amount_for_replenish * Currency.USD_EUR_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.RUB.value:
                                                    amount_for_withdraw = amount_for_replenish / Currency.EUR_RUB_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                active_client.record_all_operations('balance replenishment', code_currency, amount_for_replenish, code_currency_from)
                                            elif code_currency == Currency.RUB.value:
                                                amount_for_replenish = BankAccount.convert_to_decimal(input(f'Enter amount in {Currency.RUB.name}: '))
                                                if code_currency_from == Currency.BYN.value:
                                                    amount_for_withdraw = amount_for_replenish * Currency.BYN_RUB_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.USD.value:
                                                    amount_for_withdraw = amount_for_replenish / Currency.RUB_USD_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                elif code_currency_from == Currency.EUR.value:
                                                    amount_for_withdraw = amount_for_replenish / Currency.RUB_EUR_rate.value
                                                    if active_client.withdraw_money(code_currency_from, amount_for_withdraw):
                                                        active_client.replenish_balance(code_currency, amount_for_replenish)
                                                active_client.record_all_operations('balance replenishment', code_currency, amount_for_replenish, code_currency_from)
                                        except ValueError:
                                            print('For amount use only digits!')
                                            continue
                                elif command == '-':
                                    amount_for_withdraw = BankAccount.convert_to_decimal(input('Enter amount: '))
                                    try:
                                        active_client.withdraw_money(code_currency, amount_for_withdraw)
                                        active_client.record_all_operations('withdrawal from account', code_currency, amount_for_withdraw)
                                    except ValueError:
                                        print('Try again.')
                                elif command == '?':
                                    active_client.check_balance(code_currency)
                                else:
                                    print(f"{command} isn't correct:( Try again...")
                            else:
                                print(f'ATTENTION! Account in {Currency(code_currency).name} is not open.')
                                if BankAccount.open_account():
                                    active_client.create_account(code_currency)
                    else:
                        print(f"Uncorrect ID. Try again ({attempts_enter} attempts) or use command '#3' ('help')!")
                        attempts_enter -= 1
                        id = str(input('Enter your ID (9 numbers): '))
                        if id == '#3' or id == 'help':
                            Bank.for_help()
                            break
                        active_client = BankAccount(login, id)
                if attempts_enter == 0:
                    print('You have no attempts.')
                    print(timer())
                else:
                    continue
            except KeyError:
                print(f"Account with login {login} doesn't exist. Try again or create new account!")
        elif action == 3:
            print('OK.')
            break
        else:
            print(f'Answer {action} is incorrect. Please, enter correct value!')
    except ValueError:
        print('Use only numeric commands!')
    
exit()



