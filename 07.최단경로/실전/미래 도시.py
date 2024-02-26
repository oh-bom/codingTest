INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split()) #k방문후 x도달이 목표

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

result=graph[1][k]+graph[k][x]
if(result==INF*2):result=-1

print("result",result)

'''
5 7
1 2 
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
''' 