
def isPrime(n):
    h=int(n/2)
    for i in range(2,h+1):
        r=n%i
        if (r==0) :
            return "Not Prime"
            break
    else:
        return "Prime"

n=int(input("Input Number"))

print(isPrime(n))



    

