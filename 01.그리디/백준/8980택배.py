# 1) 첫 시도,,, ㅜ.ㅜ
# n,limit=map(int,input().split())

# k=int(input())
# arr=[]
# for _ in range(k):
#     arr.append(list(map(int,input().split())))
    
# #arr: (시작마을, 도착마을, 택배 개수)
# arr.sort() #시작 마을 순으로 정렬

# # 가까운 마을것부터 최대한 담기
# truck=[]
# truck_cnt=0
# answer=0

# for i in range(1,n+1):
    
#     for x in truck: # 상자 빼기
#         start,end,box=x
        
#         if end==i:
#             truck_cnt-=box  
#             answer+=box 
#             truck.remove(x)
#             print(x)
        
#     print(f"{i}th out",truck)
#     if i==n:break
    
    
#     for x in arr: # 상자 추가
#         start,end,box=x
        
#         # if start!=i:break
            
#         if start==i:
#             if truck_cnt+box<=limit:
#                 truck.append([start,end,box])
#                 truck_cnt+=box
#             else:
#                 truck.append([start,end,limit-truck_cnt])
#                 truck_cnt=limit
                
#             arr.remove(x)
#             truck.sort(key=lambda x:x[1])
    
#     print(f"{i}th in",truck)
    
        
# print(answer)

# TODO 2) 정답.. ㅜ.ㅜ
n,limit=map(int,input().split())
k=int(input())

arr = []
for _ in range(k):
    arr.append(list(map(int, input().split())))  # [출발 마을, 도착 마을, 상자 수]

# 도착 마을 기준으로 정렬 (같은 마을에 도착하는 택배를 고려하기 위함)
arr.sort(key=lambda x: (x[1], x[0]))

# 각 마을로 운반된 총 상자 수를 저장할 변수
answer = 0

# 각 마을에 도착할 때 트럭에 담긴 상자 개수를 관리할 리스트
truck = [0] * (n + 1)  # 각 마을의 현재 상자 수를 관리

for start, end, box in arr:
    # 해당 경로에서 트럭에 담을 수 있는 최대 상자 수 계산
    max_available = min(limit - max(truck[start:end]), box)

    # 상자를 실어서 이동
    for i in range(start, end):
        truck[i] += max_available  # 구간마다 상자 수 증가

    # 최종적으로 운반한 상자 수를 정답에 추가
    answer += max_available

print(answer)


       
                
            
            
            
    