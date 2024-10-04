# https://www.acmicpc.net/problem/16236

n=int(input())
graph=[]
shark_x,shark_y=0,0

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]==9:
            shark_x,shark_y=i,j
            graph[i][j]=0
            
        
dirs=[(-1,0),(1,0),(0,-1),(0,1)]

from collections import deque
import heapq
   

# 상어 크기, 시간, 위치
def solution(shark_x,shark_y):

    def check_eatable(shark_size):
        fish_list=[]
        for i in range(n):
            for j in range(n):
                if graph[i][j]!=0 and graph[i][j]<shark_size:
                    fish_list.append([i,j])
                    
        return fish_list

    # TODO: 최단 거리 구할때 개틀림
    def find_shortest_path(targetx,targety,x,y,shark_size):
        q=deque([[x,y]])
        distance=[[0]*n for _ in range(n)]
        visited=[[False]*n for _ in range(n)]
        visited[x][y]=True
            
        while q:
            x,y=q.popleft()
            
            if targetx==x and targety==y:return distance[targetx][targety]
            
            for d in dirs:
                nx=x+d[0]
                ny=y+d[1]
                
                if 0<=nx<n and 0<=ny<n and shark_size>=graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny]=True

                    distance[nx][ny]=distance[x][y]+1
                    q.append([nx,ny]) 
                    
        return -1
    
    
    shark_size=2
    eaten_fish=0
    time=0
    
    fish_list=check_eatable(shark_size)
    
    while fish_list:
        fish_dis=[] # TODO: 이걸 매번 초기화해줘야하는데 안햇음,,,
        heapq.heapify(fish_dis)
        
        for fish in fish_list:
            temp_dis=find_shortest_path(fish[0],fish[1],shark_x,shark_y,shark_size)
            
            if temp_dis!=-1:heapq.heappush(fish_dis,[temp_dis,fish[0],fish[1]])
        
        if not fish_dis:break #TODO: 여기도 체크해줘야하는데 안함
        
        dis,nx,ny=heapq.heappop(fish_dis)
        time+=dis
        shark_x,shark_y=nx,ny
        
        eaten_fish+=1
        graph[nx][ny]=0
        
        if eaten_fish==shark_size:
            shark_size+=1
            eaten_fish=0
    
        fish_list=check_eatable(shark_size)
        
    return time
                
print(solution(shark_x,shark_y))
                
                    
                    
    
    
    