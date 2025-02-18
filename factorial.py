def fact(n):
    if (n==1):
        return n
    else:
        return n*fact(n-1)
num=int(input("enter a number"))
if num < 0:
    print("Sorry,factorial doen't exist for negative numbers.")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial of ", num,"is", fact(num))