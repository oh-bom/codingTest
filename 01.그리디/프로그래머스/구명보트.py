# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people,limit):
    deq=deque(sorted(people))
    
    answer=0
    
    while deq:
        if len(deq)==1:
            answer+=1
            break
        
        if deq[0]+deq[-1]<=limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
            
        answer+=1
        
    return answer