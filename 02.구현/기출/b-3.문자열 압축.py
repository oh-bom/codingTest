#https://school.programmers.co.kr/learn/courses/30/lessons/60057
s="ababcdcdababcdcd"
from collections import deque
def find_pattern(s):
    pattern=[]
    
    q=deque(s[0])
 
    start=q.popleft()
    for i in range(1,len(s)):
        print("?",s[i],start)
        if s[i]!=start:
            q.append(s[i])
        else:
            pattern.append(start)
            if q:start=q.popleft()    
            else:break
    print("p",pattern)
                
    return "".join(pattern)

def process(s,s_index):
    result=""
    pattern=find_pattern(s)
    print("pattern",pattern)
    
    if pattern=="":
        index=s_index+1
        result+=s[s_index]
    
    else:
        cnt=0
        index=0
        for i in range(s_index,len(s)):
            sliced=s[i:i+len(pattern)]

            if sliced==pattern:
                cnt+=1
            else:index=i
        
        result=str(cnt)+pattern

    print(result,index)
    return result,index
    
    

def solution(s):
    answer=""
    result=""
    index=0
    result,index=process(s,0)
    answer+=result
    while True:
        result,index=process(s,index)
        answer+=result
        if index==(len(s)-1):break
        

    print(answer)
    return len(answer)

print(solution(s))