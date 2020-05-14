# sum of list
lst = eval(input("Enter the list of numbers :"))
sum = 0
for i in lst:
    sum += i

print("the sum of list is:", sum)


#  using while loop
x = 0
sum1 = 0
while x < len(lst):
    sum1 += lst[x]
    x=x+1

print("using while loop sum1=",sum1 )