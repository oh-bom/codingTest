n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dp=[0]*(n+1)

for i in range(1,n+1):
    time,money=arr[i-1]
    next=i+time-1
    
    if next<n+1:
        prev_max=max(dp[:i])
        dp[next]=max(dp[next],prev_max+money)

print(max(dp))