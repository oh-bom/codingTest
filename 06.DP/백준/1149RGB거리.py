# https://www.acmicpc.net/problem/1149

n=int(input())

arr=[]
# r, g, b
for _ in range(n):
    arr.append(list(map(int,input().split())))
    
dp=[[int(1e9)]*3 for _ in range(n)]
# dp=arr

dp[0]=arr[0]

for i in range(1,n):
    for j in range(3):
        if j==0:
            dp[i][j]=min(dp[i-1][1],dp[i-1][2])+arr[i][j]
        elif j==1:
            dp[i][j]=min(dp[i-1][0],dp[i-1][2])+arr[i][j]
        else:
            dp[i][j]=min(dp[i-1][0],dp[i-1][1])+arr[i][j]
            
print(min(dp[n-1]))