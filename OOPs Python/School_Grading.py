from colorama import *


class Teacher:
    '''This is parent class.'''
    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setsal(self, sal):
        self.sal = sal

    def getsal(self):
        return self.sal


class Student(Teacher):
    '''Student is a sub class of Teacher'''

    def setmarks(self, p, c, m):
        self.p = p
        self.c = c
        self.m = m

    def getmarks(self):
        return self.p, self.c, self.m

    @staticmethod
    def cal_avg(obj):     # instance/ object of student is passed.
        return (obj.p + obj.c + obj.m) // 3


# physics teacher of school
p_teacher = Teacher()
p_teacher.setname('shyaam')
p_teacher.setid('PHY-12')
p_teacher.setsal(50000)

# chemistry teacher of school
c_teacher = Teacher()
c_teacher.setname('praveen')
c_teacher.setid('CHE-12')
c_teacher.setsal(60000)

# maths teacher of school
m_teacher = Teacher()
m_teacher.setname('satya')
m_teacher.setid('MATH-12')
m_teacher.setsal(70000)

stu = Student()
stu.setname('Dev')
stu.setid('500062270')
stu.setmarks(86, 75, 56)
print(f'The Average Marks obtain By {stu.getname()} Is {Student.cal_avg(stu)}%', end=" ")

if Student.cal_avg(stu) > 35:
    print(Fore.GREEN, '(Passed)', Fore.RESET)
else:
    print(Fore.RED, '(Fail)', Fore.RESET)
print()
print('Marksheet'.center(35, "-"))
print(f'Subject     Marks')
print(f'Physics     {stu.getmarks()[0]}')
print(f'Chemistry   {stu.getmarks()[1]}')
print(f'Maths       {stu.getmarks()[2]}')
print('------------------------')
print(f'Total       {stu.getmarks()[0]+stu.getmarks()[1]+stu.getmarks()[2]}/300')