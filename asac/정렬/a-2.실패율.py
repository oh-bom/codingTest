#https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3

N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]
# stages=[4,4,4,4,4]
def solution(N,stages):
    stages.sort()
    all_cnt=len(stages)
    result=[]
    fail_dict={}
    
    for i in range(1,N+1):
        # 위와 동일
        #cnt=len([x for x in stages if x==i])
        
        # ver. list
        cnt=stages.count(i)
        
        fail=cnt/all_cnt
        all_cnt-=cnt
        result.append([i,fail])
        
        result=sorted(result,key=lambda x:-x[1])
        
        #ver. dictionary
    
        if all_cnt>0:
            fail_dict[i]=cnt/all_cnt
        else:
            fail_dict[i]=0
        
        result=sorted(fail_dict.items(),key=lambda x:-x[1])
        
    
    return [x[0] for x in result] 

print(solution(N,stages))
    

        
    