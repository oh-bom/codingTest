n,L,R=map(int,input().split())
data=[]
#왼, 오, 위 , 아래
# borders=[[[False,False,False,False]]*n for _ in range(n)]
borders = [[[False] * 4 for _ in range(n)] for _ in range(n)] # !!
visited=[[False]*n for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

def check(x,y):
    global borders
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx and nx<n and 0<=ny and ny<n:
            dif=abs(data[x][y]-data[nx][ny])
            
            if L<=dif and dif<=R:
                if i==2:
                    borders[x][y][0]=True
                    borders[nx][ny][1]=True
                elif i==3:
                    borders[x][y][1]=True
                    borders[nx][ny][0]=True

                elif i==1:
                    borders[x][y][3]=True
                    borders[nx][ny][2]=True
                elif i==0:
                    borders[x][y][2]=True
                    borders[nx][ny][3]=True
    return
result=0
def spread(x,y,sum,cnt,visited):
    global data
    visited[x][y]=True
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(4):
        if(borders[x][y][i]):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n and not visited[nx][ny]:
        
                sum+=data[nx][ny]
                cnt+=1
                print("sum",x,y,nx,ny,sum,cnt)
                
                spread(nx,ny,sum,cnt,visited)
                
    return sum,cnt

def solution(data,visited):
    result=0
    while True:
        for i in range(n):
            for j in range(n):
                check(i,j)
        sum,cnt=spread(0,0,sum=data[0][0],cnt=1,visited=visited)
        if cnt!=1:
            average=sum/cnt
            for i in range(n):
                for j in range(n):
                    if visited[i][j]:
                        data[i][j]=average
                        visited[i][j]=False
            result+=1
        else:break

    print(result)
solution(data,visited)
    
    
    