counter = 1
while counter < 11:
  print(counter)
  counter += 1

counter = 1
while counter < 11:
  if counter == 4:
    break;
  print(counter)
  counter += 1


counter = 0
while counter < 11:
    counter += 1
    if counter % 2 == 0:
        continue;
    print(counter)
  
for x in "banana":
  print(x)

for x in range(3):
  print(x)

# for x in range(6):
#   print(x)  

#can specify starting point
for x in range(7, 10):
  print(x)

#can specify increment
for x in range(20, 40, 5):
  print(x)  

for x in range(1,4):
  print(x)
else:
  print("Go!")  

