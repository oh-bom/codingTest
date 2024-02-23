#https://school.programmers.co.kr/learn/courses/30/lessons/42891
import heapq

#test data
food_times=[3,1,2]
k=5
food_times2=[8,6,4]
k2=15

def solution(food_times,k):
    #더 섭취해야하는 음식이 없는 경우
    #전체 음식 섭취 시간<=k
    if sum(food_times)<=k:
        return -1
    
    #시간이 작은 음식부터 제거하기 위해 heapq 사용
    hq=[]
    for i in range(len(food_times)):
        #(음식 시간, 인덱스) 형태의 튜플 삽입
        heapq.heappush(hq,(food_times[i],i+1))

    sum_value=0
    previous=0
    length=len(food_times)

    while sum_value+(hq[0][0]-previous)*length<=k:
        now=heapq.heappop(hq)[0] #현재 음식의 먹는데 걸리는 시간
        sum_value+=(now-previous)*length

        length-=1 #다먹은 음식 제외
        previous=now
    
    #남은 음식을 index로 정렬
    result=sorted(hq,key=lambda x:x[1])

    #남은 음식 중 어디 인덱스에 걸리는지 계산후 인덱스값 리턴
    return result[(k-sum_value)%length][1]

print(solution(food_times=food_times2,k=k2))