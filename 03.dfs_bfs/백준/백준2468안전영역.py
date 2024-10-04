n=int(input())
graph=[]
max_height=0
for _ in range(n):
    graph.append(list(map(int,input().split())))
    

from collections import deque

def solution():
    
    max_height=0
    for i in range(n):
        max_height=max(max(row) for row in graph)
        # max_height=max(max_height,max(graph[i]))
    answer=[]
    
    def bfs(x,y,max_height):
        q=deque([[x,y]])
        visited[x][y]=True
            
        while q:
            x,y=q.popleft()
            
            dirs=[(-1,0),(1,0),(0,-1),(0,1)]
            
            for d in dirs:
                nx=x+d[0]
                ny=y+d[1]

                if 0<=nx<n and 0<=ny<n and graph[nx][ny]>max_height and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append([nx,ny])
        return 1
    
    for h in range(1,max_height):
        cnt=0
        visited=[[False]*n for _ in range(n)]
    
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and graph[i][j]>h:
                    cnt+=bfs(i,j,h)
                 
        answer.append(cnt)
        
    return max(answer)

print(solution())  