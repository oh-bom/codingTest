n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,c):
    if c == "D":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

    return direction

def simulate():
    x,y=1,1 #뱀 머리
    data[x][y]=2 #뱀이 존재하는곳 2
    direction=0
    time=0
    index=0
    q=[(x,y)]

    while True:
        nx=x+dx[direction]
        ny=y+dy[direction]

        if 1<=nx<=n and 1<=ny<=n and data[nx][ny]!=2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
          

        #벽에 부딪히거나 몸이랑 만난경우
        else:
            time+=1
            break
        x,y=nx,ny #다음 위치로 뱀 머리 이동
        time+=1
        if index<l and time==info[index][0]:
            direction=turn(direction,info[index][1])
            index+=1
        
        for i in range(n):
            print(data[i])
        print("")
    
    return time
print(simulate())
