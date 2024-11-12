from collections import deque


'''
최단 거리 찾는다? -> bfs
거리 자체를 cnt로 관리하지 말고 , distnace 맵을 graph와 동일하게 만들어서 그걸로 관리하자
'''

n,m=map(int,input().split())
graph=[]
distance=[[0]*m for _ in range(n)]

for _ in range(n):
    # graph.append(list(input())) # 미친 여기서 문자열로 들어감
    graph.append(list(map(int,input())))
   
print(graph)
         
def solution(graph,n,m):
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    
    def bfs(x,y):
        deq=deque([[x,y]]) # x, y
        # deq.append([x,y])
        distance[x][y]=1
        
        while deq:
            x,y=deq.popleft()
            print(x,y)
            if x==n-1 and y==m-1:return distance[n-1][m-1]
                        
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1 and distance[nx][ny]==0:
                    print("nn",nx,ny)
                    deq.append([nx,ny])
                    distance[nx][ny]=distance[x][y]+1
                    
        return -1
            
    print("Bfs",bfs(0,0))
    
        
    # def dfs(x,y,cnt):
        
    #     if x==n-1 and y==m-1:return cnt
        
    #     for i in range(4):
    #         nx=x+dx[i]
    #         ny=y+dy[i]
            
    #         if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=0:
    #             graph[nx][ny]=0
    #             dfs(nx,ny,cnt+1)
    #             graph[nx][ny]=1 # 백트래킹
        

    # print(dfs(0,0,1))
    
solution(graph,n,m)