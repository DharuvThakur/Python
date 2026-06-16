def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

a=int(input("Enter the number:"))
print(f"Factorial of 5 is :{ fact(a)}")