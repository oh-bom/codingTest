from collections import deque

n,l,r=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def process(x,y,index):
    united=[] #(x,y)와 연합된 나라담는 리스트
    united.append((x,y))

    q=deque() #탐색용
    q.append((x,y))
    
    union[x][y]=True
    sum=graph[x][y]
    cnt=1

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == False:
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    q.append((nx,ny))

                    #연합에 추가
                    union[nx][ny]=True
                    sum+=graph[nx][ny]
                    cnt+=1
                    united.append((nx,ny))

    
    for i,j in united:
        graph[i][j]=sum//cnt
            
total_cnt=0

while True:
    union=[[False]*n for _ in range(n)]
    index=0

    for i in range(n):
        for j in range(n):
            if union[i][j]==False:
                process(i,j,index)
                index+=1

    if index==n*n:
        break
    total_cnt+=1

print(total_cnt)