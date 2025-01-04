# https://www.acmicpc.net/problem/1781
import heapq as hq
# TODO: 시간초과

n=int(input())
arr=[]
days=[False]*(n+1)
answer=0
for _ in range(n):
    deadline,cup=map(int,input().split())
    arr.append((-cup,deadline))
    # hq.heappush(arr,[-cup,deadline])
hq.heapify(arr)
    
while arr:
    cup,deadline=hq.heappop(arr)
    
    for i in range(deadline,0,-1):
        if not days[i]:
            days[i]=True
            answer+=(-cup)
            break
            
print(answer)