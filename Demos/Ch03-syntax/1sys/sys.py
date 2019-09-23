import sys
for i in (sys.stdin, sys.stdout, sys.stderr):
     print(i)

#Check out memory consumption
import sys
a, b, c,d = "abcde" ,"xy", 2, 15.06
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
     