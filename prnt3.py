# Convert base-10 decimal integers to floating point numeric constants 
print ("This product is {0:f}%  {1}!". format(100, "accurate")) 
# To limit the precision 
print ("This product is {0:.1f}%  {1}!". format(100, "accurate")) 
  
# For no decimal places 
print ("This product is {0:.0f}%  {1}!". format(90.7, "accurate")) 
  
# Convert an integer to its binary or  with other different converted bases. 
print("The {0} of 67 is {1:b}".format("binary", 76)) 
          
print("The {0} of 88 is {1:o}".format("octal", 76)) 
print("The {0} of 88 is {1:x}".format("octal", 76)) 

# To demonstrate spacing when  strings are passed as parameters 
print("{0:8} is the Computer Institute in  {1:8}.".format("NIELIT", "Kurukshetra")) 
  
# To demonstrate spacing when numeric constants are passed as parameters. 
print("It is {0:5} degrees outside".format(45)) 
  
# To demonstrate both string and numeric constants passed as parameters 
print("{0:8} was founded in {1:16}".format("NIELIT", 1992)) 
  
  
# To demonstrate aligning of spaces 
print("{0:^16} was founded in {1:<4}".format("NIELIT", 1992)) 
  
print("{:*^20s}".format("NIELIT")) 
print("{:f^20s}".format("NIELIT")) 
