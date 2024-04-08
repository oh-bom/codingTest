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

def find_student(t,temp,index):
    nx,ny=t[0],t[1]
    if index==0:
        nx=t[0]+1
    elif index==1:
        nx=t[0]-1
    elif index==2:
        ny=t[1]+1
    elif index==3:
        ny=t[1]-1
    
    if 0<=nx<n and 0<=ny<n:
        if temp[nx][ny]=="S":return True
        elif temp[nx][ny]=="O":return False
        elif temp[nx][ny]=="X": 
            find_student([nx,ny],temp,index)

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
            for i in range(4):
                if find_student(t,temp,i):return "NO"

    return "YES"

print(solution(teacher,data))