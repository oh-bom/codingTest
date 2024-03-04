n=int(input())
data=[]
for _ in range(n):
    data.append(list(map(str,input().split())))

teacher=[]
empty=[]
for i in range(n):
    for j in range(n):
        if data[i][j]=="T":teacher.append([i,j])
        elif data[i][j]=="X":empty.append([i,j])

def find_student(t,temp):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(4):
        nx=t[0]+dx[i]
        ny=t[1]+dy[i]
 
        if 0<=nx and nx<n and 0<=ny<n:
            if temp[nx][ny]=="S":return True
            elif temp[nx][ny]!="O":return False
            elif temp[nx][ny]=="X": 
                find_student([nx,ny],temp)

    return False

from itertools import combinations
from copy import deepcopy
def solution(teacher,data):
    blocks=list(combinations(empty,3))
    
    for block in blocks:
        temp=deepcopy(data)
    
        for x in block:
            temp[x[0]][x[1]]="O"
            
        for t in teacher:
            if find_student(t,temp):return "NO"

    return "YES"

print(solution(teacher,data))