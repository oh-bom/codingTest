n,m=map(int,input().split())
x,y,temp=map(int,input().split())

data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

visited=[[0]*m for _ in range(n)]
dirs=[(-1,0),(0,1),(1,0),(0,-1)]

visited[x][y]==1 #
result=0
while True:
    dir=dirs[temp] #이렇게 접근하면 dirs[-5]부터는 dirs길이를 벗어나므로 에러가 뜹니당
    nx=x+dir[0]
    ny=y+dir[1]

    if(visited[nx][ny]==0 and data[nx][ny]!=1):
        visited[nx][ny]==1
        result+=1
    else: temp-=1

    if(nx>n or ny>m or nx<0 or ny<0):break

print(result)
        
'''
피드백:
회전 후 현재 위치 업데이트 x, 
회전을 4방향 다 했을때 안되면 뒤로 back x
->회전 카운트를 세어서 4방향 회전이 안됬을때를 처리해주어야함
'''