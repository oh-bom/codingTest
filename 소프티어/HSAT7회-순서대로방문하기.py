# https://softeer.ai/practice/6246

import sys

n,m=map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))

visited=[[False]*n for _ in range(n)]

destination=[]
for _ in range(m):
    x,y=map(int,input().split())
    destination.append([x-1,y-1])

answer=0

def dfs(now,dest_index):
    global answer

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    x,y=now
    visited[x][y]=True
    
    if now==destination[dest_index]:
        if dest_index==m-1:
            answer+=1
            visited[x][y]=False
            return 
        else:dest_index+=1

   
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny]==0:
            dfs([nx,ny],dest_index)

    visited[x][y]=False
    return

dfs(destination[0],0)
print(answer)