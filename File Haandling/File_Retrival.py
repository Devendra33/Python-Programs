from os import path
from colorama import *
# we can access that files that only in directory (refer pg-no : 449)
# Enter file name : Testfile.txt
# We can enter .py files to get source codes.

t = '4'
while t != '0':
    fn = input(Fore.GREEN+'plz enter file name:'+Fore.RESET)
    if path.isfile(fn):
        with open(fn, 'r+') as f:
            print(f.read())

    else:
        print(Fore.RED+fn+" does not exit in the system"+Fore.RESET)
        print('press anything to continue...')
        t = input('press 0 to quit')
