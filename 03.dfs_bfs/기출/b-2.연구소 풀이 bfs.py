#https://wooono.tistory.com/555

import sys
from itertools import combinations
from copy import deepcopy
from collections import deque

n,m=map(int,sys.stdin.readline().split())

data=[] #초기 맵
for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

# 빈 공간 좌표 저장
empty=[]
for i in range(n):
    for j in range(m):
        if data[i][j]==0:
            empty.append((i,j))

empty_combinations=list(combinations(empty,3))

dx=[-1,-1,0,0]
dy=[0,0,-1,1]

def bfs():
    temp=deepcopy(data)

    for x in range(n):
        for y in range(m):
            q=deque()

            if temp[x][y]==2:#현재 위치에 바이러스 존재
                q.append((x,y))

                while q:
                    now=q.popleft()

                    #바이러스 확산
                    for i in range(4):
                        nx=now[0]+dx[i]
                        ny=now[1]+dy[i]

                        if 0<=nx and nx<n and 0<=ny and ny<m and temp[nx][ny]==0:
                            temp[nx][ny]=2
                            q.append((nx,ny))

    return safe_area(temp)
        
def safe_area(temp):
    cnt=0

    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                cnt+=1

    return cnt

def solution():
    global data
    result=-1

    #1. 울타리 세우기 2. bfs로 바이러스 확산 3.안전 영역 계산
    for fence in empty_combinations:
        #울타리 설치
        for x,y in fence:
            data[x][y]=1

        #bfs 바이러스 확산 후 안전영역 계산
        result=max(result,bfs())

        for x,y in fence:
            data[x][y]=0 #울타리 제거 ->dfs에서 백트래킹 부분

    return result

print(solution())
            


