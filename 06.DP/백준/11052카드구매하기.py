# https://www.acmicpc.net/problem/11052

n=int(input())

card=list(map(int,input().split()))

dp=[0]*(n+1)
for i in range(n):
    dp[i+1]=card[i]


for i in range(2,n+1):
    for j in range(1,i):
        dp[i]=max(dp[j]+dp[i-j],dp[i])

print((dp[n]))
    
