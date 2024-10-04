n,m=map(int,input().split())

x,y,d_index=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
cleaned=[[False]*(m) for _ in range(n)]
    
# 북, 동 , 남, 서
dirs=[(-1,0),(0,1),(1,0),(0,-1)]

from collections import deque

def solution(x,y,d_index):
    cnt=0
    q=deque([[x,y,d_index,cnt]])
    
    while q:
        near_cleand=False
        
        x,y,d_index,cnt=q.popleft()
        
        # 현재칸 청소
        if not cleaned[x][y]:
            cleaned[x][y]=True
            cnt+=1
        
        #주변 4칸에서 청소 가능할때
        for _ in range(4):
            d_index=((d_index+3)%4) # 반시계 방향
            nx=x+dirs[d_index][0]
            ny=y+dirs[d_index][1]
                
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0 and not cleaned[nx][ny]:
                near_cleand=True
                q.append([nx,ny,d_index,cnt])
                break
            
        # 주변 4칸 모두 청소 안될때            
        if not near_cleand:
            nx=x-dirs[d_index][0]
            ny=y-dirs[d_index][1]
                
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                q.append([nx,ny,d_index,cnt])
                    
            else:return cnt    
            
            
print(solution(x,y,d_index))
            
        
    
            
            
            
        
        