#Equal bitwise operations
n=int(input())
a=list(map(int,input().split()))
mod=1000000007
cvp=0
sayac={}

for i in a:
    if i in sayac:
        sayac[i]+=1
    else:
        sayac[i]=1


for k,v in sayac.items():
    if k:
        cvp+=2**(v-1)%mod
    else:
        cvp+=(2**v-1)%mod
    cvp%=mod
print(cvp)