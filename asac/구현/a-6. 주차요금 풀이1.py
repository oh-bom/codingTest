#https://school.programmers.co.kr/learn/courses/30/lessons/92341/solution_groups?language=python3

import math
#반올림 round, 올림 ceil, 내림 floor
fees=[120, 0, 60, 591]
records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]


def solution(fees,records):
    
    check={}
    
    for record in records:
        time,number,status=record.split()
        
        time=time.split(":")
        time=int(time[0]*60)+int(time[1])
        total_time=0
        
        if number not in check:# dictionary에 있는지 체크
            
            check[number]=(total_time,time,status)
            
            if status=="IN":
                check[number]=(check[number][0],time,status)
                
            elif status=="OUT":
                total_time,in_time,_=check[number]
                total_time+=time-in_time
                check[number]=(total_time,time,status)
                
        result={}
        
        for number in check.keys():
            total_time,time,status=check[number]
            
            if status=="IN":
                total_time+=1439-time
            fee=fees[1]
            if total_time<=fees[0]:
                result[number]=fee
                
            else:
                 fee = fee + math.ceil((total_time - fees[0]) / fees[2]) * fees[-1]
                 result[number]=fee
                 
    return list(map(lambda x:x[1],sorted(result.items())))
            
    
    