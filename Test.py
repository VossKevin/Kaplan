x=10
y=2
z=3
u=18
menor=999

arr=[]
arr.append(x)
arr.append(y)
arr.append(z)
arr.append(u)

for i in range(len(arr)):
    if arr[i]<menor:
        menor=arr[i]

print("El menor es: ", menor)