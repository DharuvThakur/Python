l1=[1,2,3,4,5,6,7,8,9,10]
l2=[]
l3=[]
for i in range(5):
    l2.append(l1[i])
for j in range(len(l2)-1,-1,-1):
    l3.append(l2[j])
print(f"Orignal list:{l1}")
print(f"Extracred first five elements:{l2}")
print(f"Reversed extracted elements:{l3}")

