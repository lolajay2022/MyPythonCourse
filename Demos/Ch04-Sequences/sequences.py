print('"Hello, galaxy!"[0]=',"Hello, galaxy!"[0])
print('"Hello, galaxy!"[1]=',"Hello, galaxy!"[1])
print('"Hello, galaxy!"[-1]=',"Hello, galaxy!"[-1])
print('"Hello, galaxy!"[-2]=',"Hello, galaxy!"[-2])

a = "Hello,galaxy!"
print(len(a))
print(min(a))
print(max(a))

print ("ll" in a)

print('"Hello, galaxy!"[1:3]=',"Hello, galaxy!"[1:3])
print('"Hello, galaxy!"[3:]=',"Hello, galaxy!"[3:])
print('"Hello, galaxy!"[:3]=',"Hello, galaxy!"[:3])
print('"Hello, galaxy!"[-4:-1]=',"Hello, galaxy!"[-4:-1])

#by steps
print('"Hello, galaxy!"[1::2]=',"Hello, galaxy!"[1::2])


# sum() to calculate the sum of the items in an iterable data type

some_nums = [2,6,4,2]
print('the sum of the list is: ',sum(some_nums))

#List
fruit_list = ["apple", "banana", "cherry","banana"]
print(fruit_list)

#Tuple
fruit_tuple = ("kiwi", "lime", "cherry","banana")
print(fruit_tuple)
# fruit_tuple.pop() # wont work on a tuple

print('first in fruit_list =', fruit_list[0] )
print('first in fruit_tuple =', fruit_tuple[0] )

#Changing Value in List
fruit_list = ["apple", "banana", "cherry","banana"]
fruit_list[1] = 'kiwi'
print(fruit_list)

#Adding a Value in List
fruit_list = ["apple", "banana", "cherry","banana"]
fruit_list.append('blueberry')
print(fruit_list)


#Popping a Value from the List
fruit_list = ["apple", "banana", "cherry","banana"]
one_fruit = fruit_list.pop();
print(one_fruit)
print(fruit_list)


# #Adding a Value in Tuple doesnt work
# fruit_tuple = ("kiwi", "lime", "cherry","banana")
# fruit_tuple.append('blueberry')


#Count of an item in List or tuple
fruit_list = ["apple", "banana", "banana", "cherry","banana"]
print(fruit_list.count('banana'))
fruit_tuple = ("kiwi", "lime", "kiwi", "cherry","banana")
print(fruit_tuple.count('kiwi'))
print(fruit_tuple.count('strawberry'))

#Set of an item in List or tuple
fruit_set = {"apple", "banana", "banana", "cherry","banana"}
print(len(fruit_set))
print(fruit_set)

#Set with discard and remove
fruit_set = {"apple", "banana","cherry"}
fruit_set.remove("banana")
print(fruit_set)
fruit_set.discard("kiwi") 
# fruit_set.remove("kiwi") #throws error

#Using clear on a Set
fruit_set = {"apple", "banana","cherry"}
fruit_set.clear()
print(fruit_set)
del fruit_set
# print(fruit_set)  #errors because it was deleted

number_set = {1,2,3}
alpha_set = {'a','b','c'}
all_set = number_set.union(alpha_set)
print(all_set)

number_set = {1,2,3}
alpha_set = {'a','b','c'}
number_set.update(alpha_set)
print(number_set)

forty_two=frozenset(['life','universe','everything'])
print(forty_two)

# Measure strings in list:
words = ['life','universe','everything']
for w in words:
    print(w, len(w))

