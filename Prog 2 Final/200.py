#A Plane Journey
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    result=-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            result=mid
            high=mid-1
        else:
            low=mid+1

    return result

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

def solve(n,m,a,b):
    a.sort()
    b.sort()

    if a[-1]>b[-1]:
        print("-1")
    else:
        z,k,temp=-1,0,1
        for i in range(n):
            if z==m-1:
                temp+=2
                z=-1
            z=binary_search(b,a[i])
            if z==-1:
                break
        
        if z!=-1:
            print(temp)
        else:
            print("-1")

solve(n,m,a,b)