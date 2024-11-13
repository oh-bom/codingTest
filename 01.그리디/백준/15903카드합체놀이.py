# https://www.acmicpc.net/problem/15903

num,cnt=map(int,input().split())
cards=list(map(int,input().split()))

# 매번 sort하기는 어려우니 우선 순위 큐를 사용하여 매번 가장 작은 두 수 합치기
import heapq as hq

hq.heapify(cards)

for i in range(cnt):
    next=0
    for _ in range(2):
        x=hq.heappop(cards)
        next+=x
    
    for _ in range(2):
        hq.heappush(cards,next)
        
print(sum(cards))
    
