#90도 회전은 암기해두기!
def rotation(key):
    n=len(key)
    m=len(key[0])

    result=[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=key[i][j]
    
    return result

#자물쇠 중간부분이 모두 1인지 확인->2라면 겹치는 부분, 0이라면 열쇠가 들어오지 않음
def check(new_lock):
    lock_length=len(new_lock)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1:
                return False
    
    return True

def solution(key,lock):
    n=len(lock)
    m=len(key)

    #기존 자물쇠를 3배 시키기
    new_lock=[[0]*(n*3) for _ in range(n*3)]

    #새로운 자물쇠(x3) 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]

    #4가지 방향 확인
    for _ in range(4):
        key=rotation(key)

        #자물쇠를 3배 했으니까 2배한 라인까지만 가서 key넣어보면 됨
        for x in range(n*2):
            for y in range(n*2):

                #자물쇠 넣어보기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]

                if check(new_lock)==True:
                    return True
                
                #자물쇠가 안맞는 경우
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[x+i][y+j]-=key[i][j]

    return False