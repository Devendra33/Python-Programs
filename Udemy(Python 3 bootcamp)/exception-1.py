from colorama import *
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print(Fore.GREEN)
    print("error is handled.")
    print(Fore.RESET)
else:
    print("No erreor is encountered.")
print('sample text')