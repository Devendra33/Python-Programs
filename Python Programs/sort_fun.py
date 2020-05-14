# almost all use of sort()
lst = ['554','21','889','1','10','45','7']
print(sorted(lst, key=int))
# alternative
lst.sort(key=int)

#------------------------------------------------------------------------------

# imp wala point
def index(val):
    return val[1]    # return 2 second index (user choice) , RETURN KRNA HAI IMP.

lst1 = [(5,7,2),(5,1,7),(4,3,7),(9,5,1)]
print(sorted(lst1, key = index))

#---------------------------------------------------------------------------------
lst2 = ['a','A','b','B','c','C']
lst3 = [5,7,1,23,4,6,9,4,8,5,12,3,6,4,7,5,9,3,1,8,9]   # sort according to 1 elements.
print(sorted(lst3, key=str))