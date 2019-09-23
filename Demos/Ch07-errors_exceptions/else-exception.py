def get_object(collection,index):
    return collection[index]

x = "spam"
try:
    letter1 = get_object(x, 2)
    letter2 = get_object(x, 11)
except IndexError as Argument:
    print('an exception occured:',Argument)
else:
    print('combined',letter1+letter2)

