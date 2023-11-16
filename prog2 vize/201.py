#String Restoration
t=int(input())
while t:
    t-=1
    sayac=0
    n=int(input())
    arr=list(map(int,input().split()))
    
    for i in range(n-1):
        if arr[i]>arr[i+1] or (arr[i+1]-arr[i])>1 or arr[0]>1:
            sayac=1
            break
    
    if sayac==1:
        print(-1)
    else:
        print("a",end="")
        for i in range(1,n):
            if arr[i-1]!=arr[i]:
                x=96+arr[i]
                print(chr(x),end="")
            else:
                print("a",end="")
        print()