numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand="right"
def solution(numbers,hand):
    answer=""
    num={
        1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],
        7:[2,0],8:[2,1],9:[2,2],"*":[3,0],0:[3,1],"#":[3,2]
       
    }
    l=num["*"]
    r=num["#"]
    
    for i in numbers:
        now=num[i]
        
        if i in [1,4,7]:
            l=now
            answer+="L"
        elif i in [3,6,9]:
            r=now
            answer+="R"
            
        else:
            ld,rd=0,0
            for x,y,z in zip(l,r,now):
                ld+=abs(x-z)
                rd+=abs(y-z)
            if ld<rd:
                l=now
                answer+="L"
            elif rd<ld:
                r=now
                answer+="R"
            else:
                if hand=="right":
                    r=now
                    answer+="R"
                else:
                    l=now
                    answer+="L"
                    
    return answer
                
print(solution(numbers,hand))
            
    
    
    