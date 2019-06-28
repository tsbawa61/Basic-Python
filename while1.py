import sys 
text = "" 
while 1: # Use of 1 means infinite loop which has to be broken with break statement
 c = sys.stdin.read(1) 
 text = text + c 
 if c == '\n': 
  break 
print("Input: %s" % text)
