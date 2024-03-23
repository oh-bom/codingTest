import heapq

tcase=int(input())
INF=int(1e9)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
        
for _ in range(tcase):
    n=int(input())
    graph=[]
    
    distance=[[INF]*(n) for _ in range(n)]
    
    for _ in range(n):
        graph.append(list(map(int,input().split())))
        
        
    # 시작 값 초기화
    x,y=0,0
    q=[(graph[x][y],x,y)]
    distance[x][y]=graph[x][y]
    
    while q:
        #최단 거리 노드 꺼내기
        dist,x,y=heapq.heappop(q)
        
        if distance[x][y]<dist: continue
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if not (0<=nx<n and 0<=ny<n):continue
            
            cost=dist+graph[nx][ny]
            
            if cost<distance[nx][ny]:
                heapq.heappush(q,(cost,nx,ny))
                distance[nx][ny]=cost
                
    print("answer",distance[n-1][n-1])        
        
    