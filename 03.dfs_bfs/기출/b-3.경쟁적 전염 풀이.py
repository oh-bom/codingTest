#https://www.acmicpc.net/problem/18405

from collections import deque
n, k = map(int, input().split())

graph=[] #현재 상태 맵
virus=[] #바이러스 정보 답는 리스트

for i in range(n):
    graph.append(list(map(int,input().split())))

    #나는 바이러스에 대한 정보를 다른 함수로 빼서 for문을 또 돌렸는데 이렇게 데이터 입력
    #받을때 넣는게 더 효율적일 것 같다
    
    for j in range(n):
        if graph[i][j]!=0:
            # 바이러스 종류, 시간, 위치 x,y 삽입
            virus.append(graph[i][j],0,i,j)

#정렬 후에 큐로 옮긴다
virus.sort()
#나는 처음 풀때, 순서가 더 작은 바이러스가 더 큰 애한테 먹힐까봐? 값들을 비교하는 로직이 있었는데
#애초에 이렇게 virus를 정렬하고 시작하면 굳이 할 필요가 없다.
q=deque(virus)

target_time,targetx,targety=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    virus,time,x,y=q.popleft()
    #타겟 타임에 도달했을때
    if time==target_time:
        break

    #타겟타임에 도달하지 않은 경우 4방향으로 바이러스 퍼뜨리기
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx and nx<n and 0<=ny and ny<n:
            #방문하지 않은 위치라면, 바이러스 넣기
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus,time+1,nx,ny))

print(graph[targetx-1][targety-1])