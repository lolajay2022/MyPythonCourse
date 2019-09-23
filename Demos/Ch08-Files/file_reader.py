with open('pi_thirty.txt') as abc:
    contents = abc.read()
print(contents)

print('*'*10)

with open('pi_thirty.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('*'*10)

#for this to work create a file at c:\text_files\file_name.txt
with open('c:/text_files/file_name.txt') as file_object: 
    contents = file_object.read()
    print(contents.rstrip())

#line-by-line
filename = 'pi_thirty.txt'

with open(filename) as file_object:
     for line in file_object:
          print(line)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#lines into a List object
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print('line: ',line.rstrip())

for line in lines:
       pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi.")