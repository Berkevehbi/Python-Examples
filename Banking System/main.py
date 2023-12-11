import datetime


class User:
    def __init__(self, full_name, balance):
        self.__balance = balance
        self.full_name = full_name

    def deposit(self, money_amount):
        self.__balance += money_amount

    def withdraw(self, money_amount):
        if self.__balance - money_amount >= 0:
            self.__balance -= money_amount
            print("{} dollar has been withdrawn.".format(money_amount))
            self.save_the_process_withdraw(money_amount)
        else:
            print("The user has less money and cannot withdraw that much money.")

    def write_balance(self):
        print(f'The {self.full_name}\'s money is {self.__balance} dollar.')

    def edit_name(self, new_full_name):
        self.full_name = new_full_name

    def save_the_process_withdraw(self, money_amount):
        with open("database.txt", "a") as file:
            file.write("{} withdraw {} at {}\n".format(self.full_name, money_amount,
                                                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))


def create_account(full_name):
    return User(full_name, 0)


user1 = create_account("Vehbi Berke")
user1.deposit(150)
user1.withdraw(20)

user1.write_balance()
