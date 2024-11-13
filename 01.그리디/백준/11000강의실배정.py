# https://www.acmicpc.net/problem/1931
import heapq

n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append([y,x])
    
heapq.heapify(arr)
# arr.sort() 해도 상관 없음
prev=0
cnt=0

while arr:
    end,start=heapq.heappop(arr)
    if prev<=start:
        cnt+=1
        prev=end
print(cnt)