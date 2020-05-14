#problem: updated list cannot be appended in new list(lst2)
str1 = 'e-d-c-b-a-b-c-d-e'
lst1 = list(str1)
lst2 = []
mid_element = 9
n = 5
for i in range(0,n):    # for rows!

    lst1[mid_element - 1] = chr(97+i)
    print(lst1)
    lst2.append(lst1)
print('==============================================')
for i in range(0,n):
    print(lst2[i])
# solution: paste lst1 = list(str1) inside for loop
# (this is concept of shallow loading and loading in lst)
str1 = 'e-d-c-b-a-b-c-d-e'

lst2 = []
mid_element = 9
n = 5
for i in range(0,n):    # for rows!
    lst1 = list(str1)
    lst1[mid_element - 1] = chr(97+i)
    print(lst1)
    lst2.append(lst1)
print('==============================================')
print('sahi wala answer!!!!!!!!')
for i in range(0,n):
    print(lst2[i])
