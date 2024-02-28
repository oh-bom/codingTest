#https://www.acmicpc.net/problem/18405
from collections import deque
from copy import deepcopy
n,k=map(int,input().split())
data=[]
for _ in range(n):
    data.append(list(map(int,input().split())))

time,targetx,targety=map(int,input().split())
temp=deepcopy(data)

def spread_virus(x,y,time,cnt,temp,data):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    if time==cnt:
        return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx and nx<n and 0<=ny and ny<n:
            if temp[nx][ny]==0:temp[nx][ny]=temp[x][y]
            elif temp[nx][ny]!=0:
                if data[nx][ny]==0 and temp[x][y]<temp[nx][ny]:
                    temp[nx][ny]=temp[x][y]
                else:continue

            spread_virus(nx,ny,time,cnt+1,temp,data)
def find_virus(n,temp):
    result=[]
    for i in range(n):
        for j in range(n):
            if temp[i][j]!=0:
                result.append([i,j])

    return result

def solution(n,k,data,time,targetx,targety,temp):
    virus=find_virus(n,temp)

    for x in virus:
        spread_virus(x[0],x[1],time,0,temp,data)

    return temp[targetx-1][targety-1]

print(solution(n,k,data,time,targetx,targety,temp))