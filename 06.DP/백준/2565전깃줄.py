# https://www.acmicpc.net/problem/2565

n=int(input())
arr=[]
dp=[1]*n

for i in range(n):
    arr.append(list(map(int,input().split())))
    
arr.sort()

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
            
print(max(dp)) # 최장 증가 수열
print(n-max(dp))