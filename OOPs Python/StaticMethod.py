class Test():
    '''It works like a function works same as outside the class but it is written inside class
       basically used to perform some computation that is not related to class/instance variable
       '''
    var = 10
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @staticmethod
    def sqaure(arg):  # takes external inputs on time of calling
        print(f'The square is: {arg**2}')
    @staticmethod
    def display(e): # takes instance as an object
        e.salary += 1000
        print(f'Using display method:\n{e.name}\n{e.age}\n{e.salary}')
    # this is better approach.
    def __str__(self):
        return f'Using str(dunder) method:\n{self.name}\n{self.age}\n{self.salary}'
Test.sqaure(10)
e = Test('dev',20,150000)
print(e)    # salary is 150000
Test.display(e)  # salary is modified here: 150100
print(e)   # displays changed salary 150100




