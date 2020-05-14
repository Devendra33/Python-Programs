#prime numbers

n = int(input('Enter num: '))
for i in range(2,n):
    if n % i == 0:
        print(" Not prime number.")
        break
else:
    print("prime number.")
