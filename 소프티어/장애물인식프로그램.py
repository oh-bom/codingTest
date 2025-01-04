# https://softeer.ai/app/assessment/index.html?xid=333398&xsrfToken=zHj4pgBTz1c05shJTjcoYVvwv6lmW5Sn&testType=practice
import sys

n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input())))

visited=[[False]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):

    cnt=1
    visited[x][y]=True
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and not visited[nx][ny]:
            cnt+=dfs(nx,ny)
            
    return cnt
    
def solution(graph):
    answer=[]
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                cnt=dfs(i,j,1)
                answer.append(cnt)

    print(len(answer))
    for cnt in answer:
        print(cnt)

solution(graph)