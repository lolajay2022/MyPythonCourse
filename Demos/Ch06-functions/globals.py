def aDescription():
  global description
  description = "fun"

myDescription()

print("Python is " + description)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)