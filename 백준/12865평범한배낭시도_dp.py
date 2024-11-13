n,limit=map(int,input().split())

arr=[]
for _ in range(n):
    w,v=map(int,input().split())
    arr.append([w,v])

arr.sort(key=lambda x:x[1]) # value 순 정렬

def solution(arr,limit):
    dp=[0]*(limit+1) #무게당 value를 담는 dp 배열 생성
    weight_sum=0
    value_sum=0
    
    for w,v in arr:
        if weight_sum+w<=limit:
            weight_sum+=w
            value_sum+=v
            dp[weight_sum]=max(dp[weight_sum],value_sum)
            
    print(max(dp))
    
solution(arr,limit)
            