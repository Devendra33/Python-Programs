for i in range(1,int(input())+1): print(pow(((pow(10,i)-1)//9),2))
'''
1
121
12321
1234321
123454321 '''
# alternative
#    1
#   121
#  12321
# 1234321
# n = int(input('Enter the number of Rows:'))
# space = 2*n-1
# num = 1
# for _ in range(n):
#     temp = num ** 2
#     print(str(temp).center(space," "))
#     num = num * 10 + 1
