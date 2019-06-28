num=int(input("Enter a Number"))
half=int(num/2)

i=2

while(i<=half):
    r=num%i
    if (r==0):
        print("Not Prime No")
        break
    else:
        i=i+1
else:
    print("Prime No")