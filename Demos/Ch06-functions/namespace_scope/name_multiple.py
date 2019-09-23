# Showing multiple names pointing to same thing
a = 2

# Output: id(a) = 140721525256480
print('id(a) =', id(a))

a = a+1

# Output: id(a) = 140721525256512
print('id(a) =', id(a))

# Output: id(3) = 140721525256512
print('id(3) =', id(3))

b = 2

# Output: id(2)= 140721525256480
print('id(2) =', id(2))


