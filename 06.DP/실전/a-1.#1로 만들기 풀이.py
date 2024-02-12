## 어렵당
x=int(input())

dp=[0]*30000

for i in range(1,x):
    dp[i]=dp[i-1]+1 #그냥 1뺀 경우

    if(i%2==0):dp[i]=min(dp[i],dp[i//2]+1)
    if(i%3==0):dp[i]=min(dp[i],dp[i//3]+1)
    if(i%5==0):dp[i]=min(dp[i],dp[i//5]+1)

print(dp[x-1])

