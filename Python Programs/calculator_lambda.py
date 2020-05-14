# program for calculator!
sum = lambda x,y: x+y
sub = lambda x,y: x-y
div = lambda x,y: x//y
mul = lambda x,y: x*y

print("Welcome to Calsi")
while True:
        print("Enter choice:")
        print("press 1 for submission.")
        print("press 2 for subtraction.")
        print("press 3 for division.")
        print("press 4 for multiplication.")
        print("press 0 to exit.")
        choice = int(input())
        if choice == 0:
                exit("Program Ended...")
        a = int(input("Enter 1st element: "))
        b = int(input("Enter 2nd element: "))

        if choice == 1:
                print(sum(a,b))
        elif choice == 2:
                print(sub(a,b))
        elif choice == 3:
                print(div(a,b))
        elif choice == 4:
                print(mul(a,b))
