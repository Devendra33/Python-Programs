#testing of inbuilt functions
# This functions only works on str objects only.(imp)
s = 'dev'    # main string.
lst = ['hello ', ' world']

# ljust()
print(s.ljust(20,"*"))

# rjust()
print(s.rjust(20,"*"))

# center()
print(s.center(20,"*"))


# join():convert list into string, only works on string data type
lst = '+'.join(lst)
print(lst)