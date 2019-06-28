num=int(input("Enter a number"))

half=int(num/2)
# print(list(range(half)))
for i in range(2,half+1):
 r=num%i
 if (r==0):
  print("%d is not prime number" %num);
  break
else:
  print("%d is prime number" %num);
