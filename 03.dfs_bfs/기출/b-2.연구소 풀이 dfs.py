#https://www.acmicpc.net/problem/14502
n,m=map(int,input().split())

data=[] #초기 맵
for _ in range(n):
    data.append(list(map(int,input().split())))


#벽 설치 뒤 맵 리스트
temp=[[0]*m for _ in range(n)]

#4방향
dx=[-1,0,1,0]
dy=[0,-1,0,1]
result=0

#바이러스 퍼뜨리기
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                #바이러스 위치 시킨 후, 재귀 수행
                temp[nx][ny]=2
                virus(nx,ny)

#안전영역 구하기
def get_safe():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:score+=1

    return score

def dfs(cnt):
    global result

    #재귀 탈출 조건
    if cnt==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]

        # 바이러스 전파 시작
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)

        result=max(result,get_safe())
        return
    
    #빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                cnt+=1
                dfs(cnt)
                data[i][j]=0
                cnt-=1

dfs(0)
print(result)