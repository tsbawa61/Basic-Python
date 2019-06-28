print ("{}, A computer science book." .format("Python Programming")) 
  
# using format option for a value stored in a variable 
str = "This article is written in {}"
print (str.format("Python")) 
  
# formatting a string using a numeric constant 
print ("Hello, I am {} years old !".format(18))
  
# Multiple placeholders in format() function 
my_string = "{}, is a {} science portal for {}"
print (my_string.format(“NIELIT", “Computer", “Kurukshetra")) 

  
# different datatypes can be used in formatting 
print ("Hi ! My name is {} and I am {} years old".format("Ram", 19)) 
  
# The values passed as parameters are replaced in order of their entry 
print ("This is {} {} {} {}".format("one", "two", "three", "four"))

# To demonstrate the use of formatters with positional key arguments. 
  
# Positional arguments are placed in order 
print("{0} study at {1}!".format("I", "NIELIT")) 

# Reverse the index numbers with the parameters of the placeholders 
print("{1} study at {0}!".format("NIELIT","I")) 
    
# Keyword arguments are called  by their keyword name 
print("{city} has a {1} with the name {0}".format("NIELIT", "Institute", city ="Kurukshetra")) 
