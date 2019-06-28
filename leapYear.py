year = int(input("Input a year: "))

if (year % 400 == 0) or (year%100!=0 and year%4 ==0):
    print("leap_year")
else:
    print("Not leap_year")

