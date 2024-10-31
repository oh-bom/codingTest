# https://www.acmicpc.net/problem/1655
import heapq
import sys

n=int(sys.stdin.readline())
left_heap=[] # 최대힙, 중간값 이하 저장
right_heap=[] # 최소힙, 중간값 초과 저장
result=[]

for i in range(n):
    num=int(input())
    
    if len(left_heap)==len(right_heap): 
        # 갯수 동일할때는 left_heap에 넣어서 중간값을 최대힙 루트에 위치하도록 함
        heapq.heappush(left_heap,-num)
    else:
        heapq.heappush(right_heap,num)
        
    # 힙사이 루트 조정
    if right_heap and -left_heap[0]>right_heap[0]:
        max_left=-heapq.heappop(left_heap)
        min_right=heapq.heappop(right_heap)
        
        heapq.heappush(left_heap,-min_right)
        heapq.heappush(right_heap,max_left)
        
    result.append(str(-left_heap[0]))
    
print("\n".join(result))
