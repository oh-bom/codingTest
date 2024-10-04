n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

from collections import deque
def solution():
    answer=[]
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    
    def bfs(x,y,cnt):
        q=deque([[x,y]])
        graph[x][y]=0
        
        while q:
            x,y=q.popleft()
            
            for d in dirs:
                nx=x+d[0]
                ny=y+d[1]
                
                if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                    q.append([nx,ny])
                    graph[nx][ny]=0
                    cnt+=1
                    
        return cnt
    
    for i in range(n):
        for j in range(n):
            if graph[i][j]==1:
                temp=bfs(i,j,1)
                answer.append(temp)
            
    answer.sort()
    print(len(answer))
    
    for x in answer:
        print(x)
        
solution()
            
            