# https://school.programmers.co.kr/learn/courses/30/lessons/42883
number="1231234"
k=3

def solution(number,k):
    answer=[]
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
            
        if k>0:
            while answer[-1]<num:
                answer.pop()
                k-=1
                
                if not answer or k<=0:break
                
        answer.append(num)
        
    answer=answer[:-k] if k>0 else answer
    
    return "".join(answer)
    
                
def solution(number, k):
    answer = [] 
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)
    
number="93939" 
k=2
print(solution(number,k))