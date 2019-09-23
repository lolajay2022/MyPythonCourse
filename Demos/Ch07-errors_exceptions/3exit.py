import sys

digit_in = input('enter a number: ')
    
try:
    digit = int(digit_in)
except ValueError:  
    print("That was not a number")
    sys.exit("invalid input, please restart")

print("Your digit doubled is ",digit*2)

