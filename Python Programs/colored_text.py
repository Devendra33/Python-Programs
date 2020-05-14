from colorama import Fore, Back, Style
print(Fore.CYAN)  # cyan color will be applied on hello world.
print('hello world')
print(Fore.RESET)  # Reset to default
print('RESETED\n\n')

# to highlight some text using colorama
print(Back.BLUE,Style.DIM)
print('i am highlighted')
print('cool colors')
print(Style.RESET_ALL)
print("RESETED")