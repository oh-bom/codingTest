#https://www.acmicpc.net/problem/18353

n=int(input())
dp=list(map(int,input().split()))

max_value=0
cnt=0
for i in range(n-1):
    if(dp[i]<dp[i+1]):cnt+=1
    else:dp[i]=dp[i-1]+dp[i]

print(cnt)