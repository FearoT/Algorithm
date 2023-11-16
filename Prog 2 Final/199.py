#Gears in a machine
n,m,q=map(int,input().split())
external_gears=[i=='1' for i in input().split()]
external_gears.insert(0,False)
graph=[[] for x in range(n+1)]
rotations={}
groups=[-1]*(n+1)
clockwise_gears=[False]*(n+1)

for x in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

j=0

for i in range(1,n+1):
    if groups[i]!=-1:
        continue

    queue=[(i,True)]
    is_functional=True

    while queue:
        u,du=queue.pop(0)

        if groups[u]!=-1:
            if clockwise_gears[u]!=du:
                is_functional=False
            continue

        groups[u]=j
        clockwise_gears[u]=du

        for v in graph[u]:
            dv=du^(external_gears[v] and external_gears[u])
            queue.append((v, dv))

    rotations[j]=is_functional
    j+=1

for z in range(q):
    gp,gf,dir_p,dir_f=map(int,input().split())
    dir_p=dir_p==1
    dir_f=dir_f==1
    group_p=groups[gp]
    group_f=groups[gf]
    check=rotations[group_p] and rotations[group_f] and (group_p!=group_f or (clockwise_gears[gp]^dir_p) == (clockwise_gears[gf]^dir_f))
    print('YES' if check else 'NO')