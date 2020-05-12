from colorama import *

def ask():
        while True:
            try:
                n = int(input('Enter Number: '))
            except:
                print(Fore.RED)
                print('Please Enter a valid Number.')
                print(Fore.RESET)
                continue
            else:
                print(Fore.GREEN)
                print(f'Input an integer: {n}')
                print(Fore.RESET)
                print(f'Thank you. your number squared is {n**2}')
                break
ask()
