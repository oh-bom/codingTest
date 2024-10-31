# https://www.acmicpc.net/problem/2109

import heapq as hq

n=int(input())
arr=[]
days=[False]*10001
total_money=0

hq.heapify(arr)
for _ in range(n):
    pay,day=map(int,input().split())
    hq.heappush(arr,[-pay,day])
    
# for i in range(n):
while arr:
    pay,day=hq.heappop(arr)
    
    checkd=False
    for i in range(day,0,-1):
        if not days[i] and not checkd:
            total_money+=(-pay)
            days[i]=True
            checkd=True
        
    
print(total_money)
    