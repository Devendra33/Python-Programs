class Teacher():
    '''To understand concept of inheritance basics
        improve code reusebility'''
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
    '''Student is a sub class of Teacher.
        All the function of teacher is available in Student.'''
    def setmarks(self, marks):  # This method will not available in Teacher.
        self.marks = marks

    def getmarks(self):
        return self.marks

    def __str__(self):
        return f'Name: {stu.getname()}\nId: {stu.getid()}\nMarks:: {stu.getmarks()}'


stu = Student()
stu.setname('Dev')   # setname is available  in student class
stu.setid('500062270')
stu.setmarks('75')
print(stu)