print("a","b")
print("a","b",sep="")
print(192,168,178,42,sep=".") 
print("a","b",sep=":-)")

for i in range(4):
     print(i, end=" ")
 
for i in range(4):
     print(i, end=" :-) ")

fh = open('f:\PythonProgs\data.txt',"w")
print("Writing Text to File", file=fh)
fh.close()

import sys
# output into sys.stderr:
print("Error: 42", file=sys.stderr)

a=234;b=234.5645
print(“a=%5d   b=%8.2f” % , a,b)

