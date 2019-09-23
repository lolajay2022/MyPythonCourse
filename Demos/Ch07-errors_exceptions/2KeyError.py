my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")

my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list!")

