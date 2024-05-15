array=int(input("Nhap N: "))
arrayA=[]
for i in range(array):
   arrayA.append(int(input(" Nhap a[%d]= "%i)))
print("Mang A: ", arrayA)
arrayB=[]
for i in arrayA:
    if i not in arrayB:
        arrayB.append(i)
arrayB.sort()
print("Mang B: ", arrayB)
