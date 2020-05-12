# Create a generator that generates squares of N numbers
n = int(input('Enter N: '))
def fun(n):
    for i in range(1, n+1):
        yield i ** 2
for num in fun(n):
    print(num)