# x = a + 42

try:
    # try block code
    x = a + 42
except NameError: #Use specific error name
    # except block code
    print('that didnt go so well')

print('code continues on unless you exit')
print('*'*10)



# def get_object(collection,index):
#     return collection[index]

# x = "spam"
# print(get_object(x, 2))
# print(get_object(x, 11))

def get_object(collection,index):
    return collection[index]

x = "spam"
try:
    print(get_object(x, 2))
    print(get_object(x, 11))
except IndexError:
    print('an exception occured')

print('This code follows and is executed no matter')

# try:
#     x = int(input('Enter a number in the range 1-10: '))
#     if x<1 or x>10:
#         raise Exception
#     print ('Great! You listened to me and entered a valid number')
 
# except:
#     print ('Your number seems to be outside the range 1-10')

class BadInput(Exception): pass

try:
    x = int(input('Enter a number in the range 1-10: '))
    if x<1 or x>10:
        raise BadInput
    print ('Great! You listened to me and entered a valid number')
 
except BadInput:
    print ('Your number seems to be outside the range 1-10')





