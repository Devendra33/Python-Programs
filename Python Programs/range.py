# python program to check whether a number is between 0 to 50
n = int(input("Enter a number: "))
if n > 0 and n < 51:
    print("you entered:", n, "which is in the  range 0 to 50")
else:
    print("you entered:",n,"which is out of range.")