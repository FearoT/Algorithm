#Finding the Subarrays
n=int(input())
arr=list(map(int, input().split()))

for i in range(1, n):
    arr[i]+=arr[i-1]

a=[]
for i in range(n):
    for j in range(i, n):
        if i==0:
            ort=arr[j]/(j+1)
            if j==n-1:
                ortk=0
            else:
                ortk=(arr[n-1]-arr[j])/(n-j-1)
            if ort>ortk:
                a.append((i+1,j+1))
        else:
            ort=(arr[j]-arr[i-1])/(j-i+1)
            ortk=(arr[n-1]-arr[j]+arr[i-1])/(n-j+i-1)
            if ort>ortk:
                a.append((i+1,j+1))

a.sort()
print(len(a))

for j in a:
    print(j[0],j[1])