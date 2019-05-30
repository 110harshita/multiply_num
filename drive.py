def multiply(x, y):
    if y < 0:
        return -multiply(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply(x, y - 1)

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

def great(num,p1,p2):
    if p1 < 0:
        print("factorial does not exist for negative numbers")
    elif p2 == 0:
        print("factorial of 0 is 1")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
    print(recur_factorial(num)*multiply(p1,p2))

p1=int(input("enter the value1"))
p2=int(input("enter the value2"))
ans=multiply(p1,p2)
print(ans)
if(p1>p2):
    great(p1,p1,p2)
else:
    great(p2,p1,p2)


