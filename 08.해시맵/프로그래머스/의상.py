# https://school.programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    clothes_dict={}
    answer = 1
    
    for cloth in clothes:
        name,kind=cloth[0],cloth[1]
        
        if kind not in clothes_dict:
            clothes_dict[kind]=0
            
        clothes_dict[kind]+=1
        
    for v in clothes_dict.values():
        answer*=(v+1)
          
    return answer-1