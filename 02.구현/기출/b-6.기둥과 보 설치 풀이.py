#https://school.programmers.co.kr/learn/courses/30/lessons/60061
n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#build frame 가로,세로,구조물 종류(0 기둥,1 보),(0 삭제, 1 설치)
#result (x,y,(0 기둥, 1 보))

def possible(answer):
    for x,y,type in answer:
        if type==0:#기둥인 경우
            #바닥 위 or 다른 기둥 위 or 보랑 만날때 가능
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:continue
            else:return False

        elif type==1:#보인 경우
            #양옆이 보와 연결 or 한쪽이 기둥위일때
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):continue
            else: return False

def solution(n,build_frame):
    answer=[]
    for frame in build_frame:
        x,y,type,operate=frame
        if operate==0:#삭제하는 경우
            answer.remove([x,y,type]) #일단 삭제

            if not possible(answer): #불가능한 구조물이면
                answer.append([x,y,type]) #다시 원상복귀

        elif operate==1:
            answer.append([x,y,type]) #우선 설치
            if not possible(answer):
                answer.remove([x,y,type])

    return sorted(answer)

print(solution(n,build_frame))