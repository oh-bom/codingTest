s="}]()[{"


from collections import deque
def check(s):
    q=[]
    
    for x in s:
        print(x,q)
        if x=="]" or x==")" or x=="}": #닫는 경우인 경우
            if len(q)==0:return False
            else:
                y=q.pop()
                if x=="]" and y!="[":return False
                if x==")" and y!="(":return False
                if x=="}" and y!="{":return False
        else:
            q.append(x)
            
    return True
        

def solution(s):
    answer=0
    
    for index in range(len(s)):
        new=s[index:]+s[:index]
        print("n",new)
        if check(new):answer+=1
        
    return answer

print(solution(s))