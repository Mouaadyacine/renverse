a=input("enter a string")
b=""
for i in range(len(a)):
    b=b+a[len(a)-i-1]
print(b)