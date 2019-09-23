x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


def dynamic_multiple_function(n):
  return lambda a : a * n

a_doubler = dynamic_multiple_function(2)
a_tripler = dynamic_multiple_function(3)

print(a_doubler(11))
print(a_doubler(3))
print(a_tripler(3))


