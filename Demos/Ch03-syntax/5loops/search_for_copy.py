list = ["Life","The Universe","Everything","Jack","Jill","Life","Jill"]

# Make a copy of the list.
copy = list[:]
# Sort the copy
copy.sort()
prev = copy[0]
del copy[0]

count = 0

# Go through the list searching for a match
while count < len(copy) and copy[count] != prev:
    prev = copy[count]
    count = count + 1

# If a match was not found then count can't be < len
# since the while loop continues while count is < len
# and no match is found
if count < len(copy):
    print ("First Match:",prev)