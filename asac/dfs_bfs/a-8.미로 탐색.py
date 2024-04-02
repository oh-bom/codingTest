#https://www.acmicpc.net/problem/2178
'''
출발점이 존재하는 경우->bfs일 가능성 높음
dfs로 진행시에는 제일 끝까지 간 후 되돌아와야하기 때문에
차라리 bfs로 진행하면 한 depth 씩 진행가능
'''
n,m=map(int,input().split())
data=[]
INF=float("inf")

distance=[[INF]*(m) for _ in range(n)]

for _ in range(n):
    # data.append(list(input()))
    data.append(list(map(int,input())))
    
    
from collections import deque
def solution(data,n,m):
    q=[]
    q=deque(q)
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    q.append((0,0))
    distance[0][0]=1
    
    while q:
        x,y=q.popleft()
        print(x,y)
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and data[nx][ny]==1:
                distance[nx][ny]=min(distance[nx][ny],distance[x][y]+1)
            
                data[nx][ny]=0 #방문 처리
                q.append((nx,ny))
                
            if nx==n-1 and nx==m-1:break
                
                
                
    print(distance)
    return distance[n-1][m-1]

print(solution(data,n,m))
        
        