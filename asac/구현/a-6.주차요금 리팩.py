import math

fees=[120, 0, 60, 591]
records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]


def time_format(time):
    hour,minute=time.split(":")
    
    hour=int(hour)
    minute=int(minute)

    return minute+hour*60

def solution(fees,records):
    
    car_info={}
    result={}
    result2={}
    for record in records:
        time,car,state=record.split(" ")
        formateed_time=time_format(time)
        
        #1. 내 코드에서는 중복 없애려고 set을 썼지만, not in 으로 판별 가능
        #여기가 문제,,,?
        #value로 리스트를 초기 선언하는 방법이 있는지 질문
        car_record=[formateed_time,state]
    
        if car not in car_info: #맨 처음 딕셔너리 등록시
            car_info[car]=[car_record]
            
        else:
            car_info[car].append(car_record)
            
    print(car_info)
    
    #2-1. 내가 했던 코드
    for car,value in car_info.items():
        total_time=0
        #강사님 아이디어 대로 모든 out-모든 in으로 한번에 계산해보기
        all_out=0
        all_in=0
            
        for v_item in value:
            time,state=v_item
            if state=="OUT":all_out+=time
            elif state=="IN":all_in+=time
        
        #마지막 출차에 대한 정보가 없는 경우
        if all_out<all_in:all_out+=time_format("23:59")
        total_time=all_out-all_in
        result[car]=total_time
        
    # 2-1      
    for car,time in result.items():
        if time>=fees[0]:
            result[car]=fees[1]+math.ceil((time-fees[0])/fees[2])*fees[3]
            # 여기에서 생각보다 오래 걸림,,
        else:
            result[car]=fees[1] 
    
    #2-2. 더 나은 코드
    for car,logs in car_info.items():
        #logs: [time,state]
        out_list=[time for time,state in logs if state=="OUT"]
        in_list=[time for time,state in logs if state=="IN"]
        
        if len(logs)%2!=0:out_list.append(time_format("23:59"))
        
        total_time=sum(out_list)-sum(in_list)
        
        if total_time<=fees[0]:result2[car]=fees[1]
        else:result2[car]=fees[1]+math.ceil((total_time-fees[0])/fees[2])*fees[3]
            
    return list(map(lambda x:x[1],sorted(result2.items())))
        
print(solution(fees,records))
        
        
        
        
            