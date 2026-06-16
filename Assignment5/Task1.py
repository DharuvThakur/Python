Student={"aman":43,"john":57,"akhil":85,"rahul":78,"nakul":65}
a=input("Enter the Student's name:").lower()
found=False
for i in Student:
    if(i==a):
        print(Student[i])
        found=True
        break
if not found:
    print("Student not found")

