class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 'This is my second class'
print(MyClass.__doc__)

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)




class Square:
  side = 5

some_square = Square()
print(some_square.side)

class Square:
    def __init__(self, side):
        self.side = side

some_square = Square(10)
print(some_square.side)


class Square:
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side**2;

some_square = Square(10)
print(some_square.calc_area())
some_square.side = 12
print(some_square.calc_area())
# del some_square.side
# print(some_square.calc_area())

del some_square
# if (some_square):
#     print('that square is still here!')

#coudl do an AND and shwo skip of logic

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


class Parent:
    def __init__(self, last_name):
        self.last_name = last_name

    def printname(self):
        print('I am in the ' + self.last_name + ' family')

class Child(Parent):
    pass #use pass if dont want any new properties

mom = Parent('Smith')
mom.printname()
# son = Child() 
# previous line throws error need params
son = Child('Jones')
son.printname()

##overriding parent 

class Child(Parent):
    def __init__(self, last_name):
        self.last_name = 'Child ' + last_name

    def printname(self):
        print(self.last_name)

son = Child('Trebek')
son.printname()

##overriding parent AND calling super to use parent logic
class Child(Parent):
    def __init__(self, last_name):
        super().__init__("Child " + last_name)

    def printname(self):
        print(self.last_name)

son = Child('Kravitz')
son.printname()


##adding new properties and methods
class Child(Parent):
    def __init__(self, last_name,school_name,grade):
        super().__init__("Child " + last_name)
        self.school_name = school_name
        self.grade = grade

    def printname(self):
        print(self.last_name + ' attends ' + self.school_name \
            + ' in grade ' + str(self.grade))

    def get_grade(self):
        return self.grade

son = Child('Williams','Riverview',3)
son.printname()



