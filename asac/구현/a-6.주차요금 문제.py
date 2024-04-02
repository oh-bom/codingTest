#https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math
#반올림 round, 올림 ceil, 내림 floor
fees=[120, 0, 60, 591]
records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

def time_format(time):
    hour,minute=time.split(":")
    
    hour=int(hour)
    minute=int(minute)

    return minute+hour*60
    
def solution(fees, records):
    answer = {}
    car_list=[]
    car_time={}
    
    #car list추출
    for record in records:
        _,car,_=map(str,record.split(" "))
        car_list.append(car)
        
    car_visited={car:[] for car in list(set(car_list))}
    
    for record in records:
        time,car,state=map(str,record.split(" "))
        car_visited[car].append([state,time])
        
    for car,value in car_visited.items(): 
        t1,t2=0,0
        cnt=0
        all_time=0
        
        for x in value:
            state=x[0]
            time=x[1]
            
            if state=="OUT":
                t2=time_format(time)
                all_time+=(t2-t1)
                cnt+=1
                
            if state=="IN":
                t1=time_format(time)
                cnt+=1
            
            if cnt==len(value) and cnt%2==1:#마지막 출차가 없는경우
                t2=time_format("23:59")
                all_time+=(t2-t1)
                
        car_time[car]=all_time
        
    for car,time in car_time.items():
        if time>=fees[0]:
            answer[car]=fees[1]+math.ceil((time-fees[0])/fees[2])*fees[3]
            # 여기에서 생각보다 오래 걸림,,
        else:
            answer[car]=fees[1]
        
    #아래 두줄 한번에 하는 코드
    list(map(lambda x : x[1], sorted(result.items())))
    
    
    list(map(lambda x:x[1],sorted(result.items())))
    
    result=sorted(answer.items(),key=lambda x:x[0])
    
    return [ v for k,v in result]
print(solution(fees,records))
