tcase=int(input())
INF=int(1e9)

from collections import deque

for _ in range(tcase):
    n=int(input())
    graph=[]
    distance=[[INF]*(n) for _ in range(n)]
    visited=[[False]*(n+1) for _ in range(n+1)]
    
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    def get_smallest(x,y,visited):
        min_value=INF
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        result=(0,0)
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                temp=graph[nx][ny]
                if temp<min_value:
                    min_value=temp
                    result=(nx,ny)
        return result


    def solution(start):
        q=[]
        q=deque(q)
        x,y=start
        
        q.append((x,y))
        distance[x][y]=graph[x][y]

        while q:
            x,y=q.popleft()
            visited[x][y]=True
        
            if x==n-1 and y==n-1:
                print("dis",distance)
                break

            nx,ny=get_smallest(x,y,visited)
            print(distance)
            
            cost=distance[x][y]+graph[nx][ny]
            
            if cost<distance[nx][ny]:
                distance[nx][ny]=cost
                q.append((nx,ny))
                
            
        return distance[n-1][n-1]
    
    print("answer",solution((0,0)))




    