# program to count elements in dictionary
str1 = "hello this is dev"
dic = {}
for i in str1:
    dic[i] = dic.get(i,0)+1 # if i is found then return its value else returns 0
print(dic)