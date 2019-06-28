# This is a global variable
a = 0

if a == 0:
    # This is still a global variable
    b = 1

def my_function(c):
    # this is a local variable
    d = 3
    a=5
    
    print(c)
    print(d)
    print(a)

# Now we call the function, passing the value 7 as the first and only parameter
my_function(7) # will print 7,3,5

# a and b still exist
print(a) # global,will print 0
print(b) # global,will print 1

# c and d don't exist anymore -- these statements will give us name errors!
#print(c) 
#print(d)

def my_function2(c):
    # this is a local variable
    global a
    
    print(c)
    print(a)

my_function2(7) # will print 7,0
print(a) # global, will print 0

