#https://school.programmers.co.kr/learn/courses/30/lessons/42889

N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]	
def solution(N, stages):
    answer = []
    users_length=len(stages)
    users=[[0] for _ in range(N+1)]
    p=[]
    stages.sort()

    print(users)
    #해당 단계에 머무르는 유저수 리스트
    for i in range(1,N+1):
        users[i]=stages.count(i)
        print(users)
        
    #확률 계산
    prev=0
    for i in range(1,N+1):
        p.append([i,users[i]/(users_length-prev)])
        print(p)
        prev+=users[i]
        
    p.sort(key=lambda x:(-x[1]))
    
    for i in range(N):
        answer.append(p[i][0])
    #동일
    answer=[i[0] for i in p]
        
    return answer

print(solution(N,stages))