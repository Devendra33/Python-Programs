from colorama import *
try:
    a, b = [int(x) for x in input('enter 2 numbers space separated:').split()]
    print(a/b)
    print('i am still working')   # this will work when no error occured!!
except ZeroDivisionError:
    print(Fore.RED, 'cannot be divisible by zero.', Fore.RESET)
else:
    print(Fore.GREEN, 'no error', Fore.RESET)
finally:
    print(Fore.CYAN, 'all are excuted.', Fore.RESET)