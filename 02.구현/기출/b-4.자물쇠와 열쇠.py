#시계 방향 90도 회전
def rotation(key):
    #(1,0)(2,1)(2,2)->(0,1)(1,0),(2,0)
    

    n=len(key) #행
    m=len(key[0])#열
    result=[[0]*m for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=key[i][j]

    return result
#
def find_lock_location(lock,n):
    lock_location=[]
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                lock_location.append((i,j))

    return lock_location

def find_key_location(key,m):
    key_location=[]
    
    for i in range(m):
        for j in range(m):
            if key[i][j]==1:
                key_location.append((i,j))

    return key_location

def move(m,key_location,lock_location):
    new_key_location=[]
    print(key_location,"?")

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    
    for i in range(4):
        for key in key_location:
            x,y=key

            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<m and 0<=ny<m:
                new_key_location.append((nx,ny))
                print("new",new_key_location)
            else:continue

        for lock in lock_location:
            if lock in new_key_location:
                cnt+=1
                continue
            else: move(m,new_key_location,lock_location)

    print("!~",key_location,cnt)
    return True if cnt==len(lock_location) else False

def solution(key, lock):
    answer = "false"
    m=len(key)
    n=len(lock)

    rotated_key=[]
    lock_location=[]
    lock_location=find_lock_location(lock,n)

    for _ in range(3):
        rotated_key=rotation(key)
        key_location=find_key_location(rotated_key,m)
        if move(m,key_location,lock_location):
            answer="true"
            break
        else:
            key=rotated_key


    return answer

key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))