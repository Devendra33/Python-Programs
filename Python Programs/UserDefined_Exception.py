# creating our own exceptions in python.


def check(dic):
    for k, v in dic.items():
        if v > 15:
            raise Ex(f'very high number. of user: {k}')
        else:
            print(f'number in range of user: {k}')


class Ex(Exception):
    def __init__(self, arg):
        self.mq = arg


try:
    a = int(input('enter a: '))
    if a > 10:
        raise Ex('unvalid value.')
except Ex as e:
    print(e)
dic = {'dev': 10, 'kabir': 20, 'raghu': 30}
try:
    check(dic)
except Ex as f:
    print(f)
