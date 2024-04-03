n,m=map(int,input().split())
data=[]

for _ in range(n):
    data.append(list(map(int,input())))

from collections import deque

def bfs(x,y,cnt):
    q=deque()
    q.append((x,y,cnt))

    data[x][y]=0
        
    while q:
        x,y,cnt=q.popleft()

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        
        print(x,y)
        
        for dir in dirs:
            nx=x+dir[0]
            ny=y+dir[1]

            if 0<=nx<n and 0<=ny<m and data[nx][ny]==1:
                if nx==n-1 and ny==m-1:return cnt+1
                
                q.append((nx,ny,cnt+1))
                data[nx][ny]=0
        
print(bfs(0,0,1))
