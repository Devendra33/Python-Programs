class Bank():
    def __init__(self,owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amount):
        self.balance += dep_amount
        print(f'{dep_amount}Rs/- is added to your Account. ')

    def secure_withdrawl(self,wd_amount):
        if  wd_amount > self.balance:
            print('Not sufficient balance. :(')
        else:
            self.balance -= wd_amount
            print(f'{wd_amount}Rs/- is deducted from your Account...\n Thank you for using our bank.')

    def __str__(self):
        return f'Account Owner is {self.owner} \nCurrent Balance is {self.balance}'
person = Bank('Dev',5000)
print(person)

person.secure_withdrawl(4000)
print(person)

person.deposit(500)
print(person)

person.secure_withdrawl(2000)