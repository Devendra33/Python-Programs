from random import randint


low = int(input('Enter min range: '))
high = int(input('Enter max range: '))
n = int(input('How many random Numbers: '))


def fun(low, high, n):
    for _ in range(n):
        yield randint(low, high)


for i in fun(low, high, n):
    print(i)