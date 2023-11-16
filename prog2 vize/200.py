#Directory Deletion
def cozum(a):
    if a in d:
        return 1
    b=0

    for cocuk in agac[a]:
        b+=cozum(cocuk)
    return b      

n=int(input())
eby=[int(b) for b in input().split()]
agac=[[] for i in range(n+1)]

for i in range(1,n):
    agac[eby[i]].append(i+1)
    
m=int(input())
arr=[int(b) for b in input().split()]
d={}

for i in arr:
    d[i]=1
print(cozum(1))