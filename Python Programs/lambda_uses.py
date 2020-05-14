from functools import reduce   # use reduce function
#lambda with if else: returns x if x>y is true else return y.

m = lambda x,y: x if x>y else y
a,b  = [int(x) for x in input("enter number with space separated: ").split()]
print("max num is:",m(a,b))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# lambda with filter function. filter out the element from a sequence.(list,string,tuple)
# filter function works on single iterable object

lst1 = [44,5,8,9,65,42,34]
def fun(x):
    return x % 2 == 0
lst2 = list(filter(fun,lst1))      # can be wriiten as
print("filter result 1: ",lst2)    #lst2  = list(filter(lambda x: (x % 2 == 0),lst))

str1 = "hello world i am still alive "
str2 = list(filter(lambda x: x not in (['a','e','i','o','u',' ']),str1))
print("filter result 2",list(set(str2)))  # printing all consonents.

#----------------------------------------------------------------------------------------------------
# map() in python: generally perform operation on each element of sequence.
# map() can work on two arguments of same length.

l = [4,5,8,7]
l1 = [2,4,8,9]
lt1 = list(map(lambda x: x*x, l))  # returns squares
print("map result 1: ",lt1)
lt2 = list(map(lambda x,y: x+y,l,l1)) # returns sum
print("map result 2",lt2)

#--------------------------------------------------------------------------------------------------------

# reduce(): it is use to evaluate a list in a single answer.
# eg[5,4,8,7] --sum-> 24  when lamda x,y: x+y
# lambda always have 2 arguments x,y.

ls = [2,5,8,9,6,3]
ls1 = reduce(lambda x,y: x+y, ls)
print("reduce result: ",ls1)