#https://www.acmicpc.net/problem/11404
n=int(input())
m=int(input())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]



for _ in range(m):
    a,b,c=map(int,input().split())

    #내가 놓쳤던 부분
    #주어진 입력에 중복되는 경로가 있음, 그중 최소값으로 저장해두기
    if c<graph[a][b]:
        graph[a][b]=c

for i in range(1,n+1):
    for j in range(n+1):
        if i==j:graph[i][j]=0

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])

for a in range(1,n+1):
    print("")
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("0",end=' ')
        print(graph[a][b],end=' ')