import os
try:
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "sample.txt")
    with open(file_path,"rt")as f:
     data=f.readlines()
except FileNotFoundError:
   print("The file 'sample.txt'was not present")
else:
   for i,line in enumerate(data):
      print(f"Line{i}:{line}")