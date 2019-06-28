total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   global total
   total = arg1 + arg2; # Here total is global variable.
   print ("Inside the function global total : ", total)
   return total;
# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total )
