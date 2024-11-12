# https://www.acmicpc.net/problem/1937

# dp + dfs 
import sys
n=int(sys.stdin.readline())
graph=[]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    
def solution(graph,n):
    answer=0
    dp=[[0]*n for _ in range(n)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    
    def calc_dp(x,y):
        if dp[x][y]!=0:
            return dp[x][y]
        
        dp[x][y]==1
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>graph[x][y]:
                dp[x][y]=max(dp[x][y],calc_dp(nx,ny)+1)
        
        return dp[x][y]        
        
    
    
    for i in range(n):
        for j in range(n):
            answer=max(answer,calc_dp(i,j))
            
    print(answer)
            
            
            
### 
import sys
n=int(sys.stdin.readline())
graph=[]

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    
def solution(graph,n):
    answer=0
    dp=[[0]*n for _ in range(n)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def calc_dp(x,y):
        
        if dp[x][y]!=0:return dp[x][y]
        
        dp[x][y]=1 # 우선 나 자신은 1~
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>graph[x][y]:
                dp[x][y]=max(dp[x][y],calc_dp(nx,ny)+1)
                
        return dp[x][y]
    
    
    for i in range(n):
        for j in range(n):
            answer=max(answer,calc_dp(i,j))
            
    print(answer)
    

