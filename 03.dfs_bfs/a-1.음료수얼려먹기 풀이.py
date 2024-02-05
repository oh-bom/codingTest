n,m=map(int,input().split())
data=[]

for _ in range(n):
    data.append(list(map(int,input())))

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    
    if data[x][y]==0:
        data[x][y]=1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    
    else: return False #가장 깊게 들어가서 인접노드 중 더이상 방문가능한 곳이 없을때 pop=false 


from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))

    if(data[x][y]==1):return False

    while q:
        x,y=q.popleft()
        print(x,y)
        data[x][y]=1

        dirs=[[-1,0],[1,0],[0,1],[0,-1]]
        for dir in dirs:
            nx=x+dir[0]
            ny=y+dir[1]

            if 0<=nx<n and 0<=ny<m and data[nx][ny]==0:q.append((nx,ny))

            # if nx<0 or ny<0 or nx>=n or ny>=m or data[nx][ny]==1: return False
            # else: q.append((nx,ny))

            #왜 이거로 하면 아예 안됬는가,,
            '''
            bfs는 방문한 애들을 큐에 넣고, 그 애들을 다시 탐색하는 과정이당
            근데 저렇게 방문 못하는 경우를 false로 리턴해버리면 그 후에 방문 가능한 애들을 다
            제끼는 것이 되어버림..
            '''

    #하나의 아이스크림만드는 공간 다 탐색하면 true 반환
    return True


answer_dfs=0
answer_bfs=0
for i in range(n):
    for j in range(m):
        # if(dfs(i,j)):answer_dfs+=1
        if(bfs(i,j)):answer_bfs+=1


# print(answer_dfs)
print(answer_bfs)

