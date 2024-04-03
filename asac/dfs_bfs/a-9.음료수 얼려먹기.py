
n,m=map(int,input().split())
data=[]
visited=[[False]*m for _ in range(n)]
for _ in range(n):
    # data.append(input()) #왜안되징?->문자열로 걍 때려박혀서 만약 이대로 하면 아래에서 dfs 비교시 int로 형변환 해서 해줘야함
    data.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
    
def dfs(x,y):
    data[x][y]=1
    
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        
        if 0<=nx<n and 0<=ny<m and data[nx][ny]==0:dfs(nx,ny)
        
from collections import deque
def bfs(x,y):
    q=[]
    q=deque(q)
    data[x][y]=1
    
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        data[x][y]=1
        
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if 0<=nx<n and 0<=ny<m and data[nx][ny]==0: 
                q.append((nx,ny))

    
def solution(data,n,m):
    cnt=0
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                '''
                이 부분을 data를 1로 바꾸는것이 아닌 visited로 체크한다면,
                여기서도 visited를 체크해주어야함. 안그러면 dfs가 0이면 한번씩은 다 실행되므로
                cnt가 계속 증가됨!! 그러니 그냥 data==1로 바꾸어주어서 방문안하도로 바꾸는게나음 
                '''
                # dfs(i,j)
                bfs(i,j)
                cnt+=1
                
                
    return cnt

print(solution(data,n,m))




            
            
            
    