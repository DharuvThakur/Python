import os
base_path=os.path.dirname(__file__)
file_path=os.path.join(base_path,"output.txt")

s=input("Enter the text to write to the file:")
with open(file_path,"wt")as t:
    t.write(s)
m=input("Enter additional text to append :")
with open(file_path,"at+")as f:
    f.write("\n"+m)
    f.seek(0)
    print(f"Final content of output.txt :\n{f.read()}")
