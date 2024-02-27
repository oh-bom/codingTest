n,m=map(int,input().split())
data=[]

for _ in range(n):
    data.append(list(map(int,input())))

visited=[[0]*m for _ in range(n)]

# def dfs(x,y,visited,cnt): 
#     if x<0 or y<0 or x>=n or y>=m:return False
    
#     if data[x][y]==1 and visited[x][y]==False:
#         visited[x][y]=True

#         dfs(x-1,y,visited,cnt+1)
#         dfs(x+1,y,visited,cnt+1)
#         dfs(x,y-1,visited,cnt+1)
#         dfs(x,y+1,visited,cnt+1)

#     if(x==n and y==m):return cnt

# min_value=0    
# min_value=min(dfs(1,1,visited,cnt=0),0)

from collections import deque
def bfs(x,y,cnt):
    q=deque()
    q.append((x,y))
    visited[x][y]=1

    while q:
        x,y=q.popleft()
        if(x==n and y==m):break

        visited[x][y]=1
        cnt+=1
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        for dir in dirs:
            nx=x+dir[0]
            ny=y+dir[1]

            if 0<nx<n and 0<ny<m and visited[nx][ny]==0 and data[nx][ny]==1:
                q.append((nx,ny))

    return cnt

print(bfs(0,0,0))

    
