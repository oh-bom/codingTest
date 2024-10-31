import heapq as hq
def solution(jobs):
    jobs.sort()
    current,sum_time,n=0,0,len(jobs)
    heap=[]
    i=0
    
    while i<n or heap:
        while i<n and jobs[i][0]<=current:
            hq.heappush(heap,(jobs[i][1],jobs[i][0])) # 소요시간, 시작시간
            i+=1
            
        if heap:
                duration,start=hq.heappop(heap)
                sum_time+=(current+duration-start)
                current+=duration
                
        else: #현재 시작할 작업이 없음
                current=jobs[i][0] # 다음에 시작할 작업으로 currnet 위치
    
    return sum_time//n