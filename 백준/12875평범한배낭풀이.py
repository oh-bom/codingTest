import sys
n,limit=map(int,input().split())

arr=[]
for _ in range(n):
    w,v=map(int,sys.stdin.readline().split())
    arr.append([w,v])

# arr.sort(key=lambda x:x[1]) # value 순 정렬

def solution(arr,limit):
    dp=[0]*(limit+1) #무게당 value를 담는 dp 배열 생성
    
    for w,v in arr:
        #역순으로 계산
        for j in range(limit,w-1,-1):
            dp[j]=max(dp[j],dp[j-w]+v)
    
    print(max(dp))
    
solution(arr,limit)



