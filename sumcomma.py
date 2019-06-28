s=input("ENter integers separated by commas")
print("s=",s)

t=s.split(',')
print("t=",t)

sum=0

for x in t:
    print("x=",x)
    sum=sum+int(x)
    print("sum=",sum)

print("In the end sum=",sum)
    

