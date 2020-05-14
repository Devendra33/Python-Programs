#variable length argument
# *kwargs : when number of parameters are not known group in a tuple
def single_star(*kwarg):
    sum = 0
    for i in kwarg:
        sum += i
    print(sum)

single_star(5,4,8,7,9,6,2) # function call

# **kwargs: when n number of arguments with value is associated with variable
# convert values in dictionary object interrnally.
def double_star(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        print(f" keys:{k} --- value:{v}.")

double_star(name = 'devendra',roll= 34,sapid = 500062270) #(key=value)
