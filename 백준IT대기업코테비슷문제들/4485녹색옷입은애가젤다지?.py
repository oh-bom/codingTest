# https://www.acmicpc.net/problem/4485


# 나의 시도 dfs.. 실패

# visited=[[False]*n for _ in range(n)]
# rupee=0
# ans=int(1e9)

# def dfs(x,y,rupee):
#     print("dfs:",x,y)
#     global ans
#     visited[x][y]=True
#     rupee+=graph[x][y]
    
#     if x==n-1 and y==n-1:
#         ans=min(ans,rupee)
#         print("ans:",ans)

#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
        
#         if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
#             dfs(nx,ny,rupee)
#             rupee-=graph[nx][ny]
#             visited[nx][ny]=False

# dfs(0,0,graph[0][0])
# print(ans)


# 다익스트라 풀이
# heqp queue를 이용하여 가장 비용이 적은 경로부터 탐색 가능

import heapq

def dijkstra(n,graph):
    dist=[[int(1e9)]*n for _ in range(n)]
    dist[0][0]=graph[0][0]
    
    pq=[]
    heapq.heappush(pq,(graph[0][0],0,0)) #거리, x, y
    
    while pq:
        cost,x,y=heapq.heappop(pq)
        
        if cost>dist[x][y]:continue
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                new_cost=cost+graph[nx][ny]
                
                if new_cost<dist[nx][ny]:
                    dist[nx][ny]=new_cost
                    heapq.heappush(pq,(new_cost,nx,ny))
                    
                    
    return dist[n-1][n-1]

n=-1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
index=1

while n!=0:
    n=int(input())
    if n==0:break
    graph=[]

    for _ in range(n):
        graph.append(list(map(int,input().split())))

    ans=dijkstra(n,graph)
    print(f"Problem {index}:",ans)
    index+=1
