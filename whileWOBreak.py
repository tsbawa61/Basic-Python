num=int(input("Enter a Number"))
half=int(num/2)

i=2
flag=0

while(i<=half):
    r=num%i
    if (r==0):
        print("Not Prime No")
        flag=1
        break
    
    
    else:
        i=i+1
if (flag==0):
    print("Prime No")
