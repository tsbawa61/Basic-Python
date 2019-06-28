l=[1,2,3,4,5]
m=[3,5,6]

print(l)
print(m)

print("Missing Values")
for x in l:
    if (x not in m):
        print(x)

print("Additional Values")
for x in m:
    if (x not in l):
        print(x)
