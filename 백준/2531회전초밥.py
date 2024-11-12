# https://www.acmicpc.net/problem/2531

# n,d,k,c=map(int,input().split())

# dishes=[]
# answer=0
# #  비효율^_^
# # k개 마다 자르고 c까지 추가해서 set때리고 그 개수를 answer에서 max로 비교
# for _ in range(n):
#     dishes.append(int(input()))
    
# for i in range(n-k+1):
#     temp=dishes[i:i+k]
#     temp.append(c)
#     new_answer=len(set(temp))
    
#     answer=max(answer,new_answer)
    
# for i in range(k-2,-1,-1):
#     temp=dishes[i:i-k]
#     temp.append(c)
#     new_answer=len(set(temp))
    
#     answer=max(answer,new_answer)
    
# print(answer)

# 풀이: sliding window + default dict
from collections import defaultdict
n,d,k,c=map(int,input().split())

dishes=[]
answer=0
for _ in range(n):
    dishes.append(int(input()))
    
def solution(n,d,k,c,dishes):
    dishes+=dishes[:k-1] # 원형 구간을 만들기 위해 리스트 확장
    dish_cnt=defaultdict(int)
    
    unique_cnt=0
    answer=0
    
    #초기 윈도우 설정
    for i in range(k):
        if dish_cnt[dishes[i]]==0: # 아직 나오지 않았던 초밥
            unique_cnt+=1 
        dish_cnt[dishes[i]]+=1
    
    # answer 비교
    answer=max(answer,unique_cnt+(1 if dish_cnt[c]==0 else 0))
    
    # 슬라이딩 윈도우
    for i in range(k,n+k-1):
        if dish_cnt[dishes[i]]==0: # 새로운 초밥 추가
            unique_cnt+=1
        dish_cnt[dishes[i]]+=1
        
        dish_cnt[dishes[i-k]]-=1
        if dish_cnt[dishes[i-k]]==0:
            unique_cnt-=1
        
        answer=max(answer,unique_cnt+(1 if dish_cnt[c]==0 else 0))
        
    print(answer)

solution(n,d,k,c,dishes)