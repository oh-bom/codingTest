# https://www.acmicpc.net/problem/20125

n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(input()))
    
# 4면이 모두 막힌 심장 찾기
dx=[-1,1,0,0]
dy=[0,0,-1,1]
heart_x,heart_y=0,0

for i in range(1,n-1):
    for j in range(1,n-1):
        #심장 찾기 완료
        if graph[i][j]=="*" and graph[i-1][j]=="*" and graph[i+1][j]=="*" and graph[i][j+1]=="*" and graph[i][j-1]=="*":
            heart_x,heart_y=i,j
                
# 심장으로부터 길이 재기
body=[0,0,0,0,0]

def dfs(x,y,dx,dy):
    nx=x+dx
    ny=y+dy
    # cnt=0
    # answer=1
    # if 0<=nx<n and 0<=ny<n and graph[nx][ny]=="*":
    #     cnt+=dfs(nx,ny,dx,dy)
    #     answer+=cnt
    # return answer
    
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == "*":
        return 1+dfs(nx,ny,dx,dy)
    return 1
    

body[0]+=dfs(heart_x,heart_y-1,0,-1) #왼팔
body[1]+=dfs(heart_x,heart_y+1,0,1) #오른팔
body[2]+=dfs(heart_x+1,heart_y,1,0) #허리
body[3]+=dfs(heart_x+body[2]+1,heart_y-1,1,0) #왼쪽 다리
body[4]+=dfs(heart_x+body[2]+1,heart_y+1,1,0) #오른쪽 다리

print(heart_x+1,heart_y+1)    
for x in body:
    print(x,end=" ")