# https://www.acmicpc.net/problem/7570

n=int(input())
arr=list(map(int,input().split()))

dp=[0]*(n+1)
list_length=0

for num in arr:
    dp[num]=dp[num-1]+1
    list_length=max(list_length,dp[num])
        
print(n-list_length)