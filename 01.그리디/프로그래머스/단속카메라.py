# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    camera=-30001
    answer=0
    
    routes.sort(key=lambda x:x[1])
    
    for r in routes:
        if camera<r[0]:
            answer+=1
            camera=r[1]
    return answer
    