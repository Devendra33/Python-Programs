from pickle_emp import *
from pickle import *

# dumping process.
f = open('emp.dat', 'wb')
n = int(input('enter number of rows of data:'))
for i in range(n):
    name = input('name?')
    id = int(input('id?'))
    age = int(input('age?'))
    e = emp(name, id, age)
dump(e, f)
f.close()

# Loading process.
f1 = open('emp.dat', 'rb')
print('employee details:')
while True:
    try:
        obj = load(f)
        obj.show()
    except EOFError:
        print('EOF FILE ERROR......')
        break