n=int(input())
passwords=[]
for _ in range(n):
    passwords.append(input())
    
def soltuion(passwords):
    answer_cnt=0
    answer=""
    for p in passwords:
        rp=reversed(p)
        rp="".join(rp)
        if rp in passwords:
            print(p,rp)
            answer_cnt=len(p)
            
            answer=p[int(answer_cnt/2):int(answer_cnt/2)+1]
            
    return answer_cnt,answer
            
            
        
print(soltuion(passwords))
    