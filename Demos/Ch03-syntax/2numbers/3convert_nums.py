#chaneg up and relate to sometign practical

x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#This FAILS
# print("Pi with two specific digits is: " + 3.14)

#This works
print("Pi with two specific digits is: " + str(3.14))

# x = input('enter a number 1-4: ')
# y = input('enter another number 1-4: ')
# print(x+y)

x = int(input('enter a number 1-4: '))
y = int(input('enter another number 1-4: '))
print(x+y)
