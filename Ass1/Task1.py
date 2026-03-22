x=int(input("Enter the first number:"))
y=int(input("Enter the Secomd number:"))
print(f"Addition:{x+y}")
print(f"Subtraction:{x-y}")
print(f"Multiplication:{x*y}")
if(y==0):
    print(f"not defined")
else:
    print(f"Division:{round(x/y,2)}")
