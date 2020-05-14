# half pyramidal pattern printing.
r = int(input("Enter the number of rows:"))
space = 40
for i in range(1,r+1):
    print(" "*space,end="")
    print("*"*i)
    space-=1

