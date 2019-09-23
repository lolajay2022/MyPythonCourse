def changeme( mylist ):
   """changes a passed list"""
   print ("Values inside the function before change: ", mylist)
   
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4] # This creates a NEW local reference mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

