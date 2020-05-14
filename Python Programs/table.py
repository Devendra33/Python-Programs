# table printing

num = int(input("enter the range of table:"))

for i in range(1,num+1):
    print("%d's table."%(i))
    for j in range(1,11):
        print(i*j,end="\t")

    print("\n")

