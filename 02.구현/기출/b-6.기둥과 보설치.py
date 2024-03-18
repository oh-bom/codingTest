n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#build frame 가로,세로,구조물 종류(0 기둥,1 보),(0 삭제, 1 설치)


#기둥->row방향으로 무언가 있거나 바닥이거나
#보->column 방향으로 무언가 있거나
#result (x,y,(0 기둥, 1 보))
from collections import deque
def check_row(answer,x,y):
    if x==0:return True
    if x-1>=0 and answer[x-1][y]!=2:return True

    return False

def check_column(answer,x,y):
    if answer[x][y-1]!=2 or answer[x][y+1]!=2:return True
    return False

def solution(n, build_frame):
    answer = [[2]*(n+1) for _ in range(1+n)]

    q=deque(build_frame)
    while q:
        x,y,type,work=q.popleft()
        print(answer)
        #기둥일때
        if type==0:
            if work==0:
                if check_row(answer,x,y):
                    answer[x][y]=type
                    continue
                else:
                    q.append((x,y,type,work))
            else:
                if answer[x][y]!=2:
                    answer[x][y]=2
        
        #보 일때
        elif type==1:
            if work==0:
                if check_column(answer,x,y):
                    answer[x][y]=type
                    continue
                else:
                    q.append((x,y,type,work))
            else:
                if answer[x][y]!=2:
                    answer[x][y]=2

    return answer
print(solution(n,build_frame))