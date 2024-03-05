n,m=map(int,input().split())
x,y,temp=map(int,input().split())

data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

visited=[[0]*m for _ in range(n)]
dirs=[(-1,0),(0,1),(1,0),(0,-1)]

visited[x][y]=1 #

result=1
turn_cnt=0

while True:
    
    #회전
    temp-=1
    turn_cnt+=1
    
    if(temp==-1):temp=3
    
    print("temp",x,y)
    dir=dirs[temp]
    nx=x+dir[0]
    ny=y+dir[1]
    print("next",nx,ny,turn_cnt)

    #회전 후 갈 수 있을때
    if(visited[nx][ny]==0 and data[nx][ny]==0):
        visited[nx][ny]=1
        #
        x=nx
        y=ny

        result+=1
        turn_cnt=0
        continue

    if turn_cnt==4:
        nx=x-dir[0]
        ny=y-dir[1]

        if(data[nx][ny]==1):break #바다라 못가는 경우
        
        else:
            x=nx
            y=ny
            if(visited[x][y]==0):result+=1 #한번만 뒤로 백하는게 아니라 여러번이면 필요한듯
            turn_cnt=0
    

print(result)
        
'''들었던 의문: 뒤로 가기를 하면 무조건 내가 왔던 길일텐데 어떻게 바다가 있을 수 있지?
두번 백스텝을 하게된다면 그방향의 뒤가 내가 방문하지 않았던 바다일 수 있음->예제에서 (2,2)->(1,2)->(0,2) 종료
'''
