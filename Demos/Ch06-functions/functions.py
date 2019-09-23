def my_function_name():
  print("Hello from a function")

my_function_name()  

def print_language(language):
  print(language + " is a coding language")

print_language("Python")
print_language("Java")
print_language("JavaScript")

def print_language_year(language, year):
  print(language + " was created in " + str(year))

print_language_year("Python", 1989)
print_language_year("Java", 1996)
print_language_year("JavaScript", 1995)

def multiple(a, b):
  print(a*b)

multiple(2,2)

# multiple(2)

def multiple(a, b=2):
  print(a*b)

multiple(2)
multiple(3,4)

def get_product(x,y):
  return x * y

z = get_product(4,5);
print(z)

def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()

# Now call the function we just defined:
fib(2000)


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def add_numbers(*numbers):
  count = 0
  for number in numbers:
    count += number
  print('total is =',count)

add_numbers(-20,100,50)
add_numbers(1,11,1000,100,50)

def get_individual_price(total_quantity, price_per_quantity):
  return price_per_quantity / total_quantity;

price_per = \
get_individual_price(price_per_quantity=50,total_quantity=1000)

print(price_per)

# kwargs as variable dictionary input
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(first="Sammy", last="Casey")

# concatenate
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += " " + arg
    return result

print(concatenate(a="YES!", b="Python", c="Is", d="Great", e="!"))



def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x, processed=""):
    """This is a recursive function
    to find the factorial of an integer"""
    
    if x == 1:
        print('processed ',processed)
        return 1
    else:
        if (processed):
          processed =  processed + " * " + str(x)
        else:
          processed = str(x)
        return (x * calc_factorial(x-1, processed))

num = 4
print("The factorial ", num, "! is", calc_factorial(num))		
