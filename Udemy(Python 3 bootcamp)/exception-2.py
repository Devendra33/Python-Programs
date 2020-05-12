from colorama import *
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print(Fore.RED)
    print('Any number cannot be divisble by zero')
    print(Fore.RESET)
finally:
    print('All Done')