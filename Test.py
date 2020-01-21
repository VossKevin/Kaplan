x=100
y=28
z=10
u=72
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
