# https://www.acmicpc.net/problem/2240

t,w = map(int, input().split())
arr=[int(input() )for _ in range(t)]

dp=[[0]*(w+1) for _ in range(t)]

for t in range(t):
    for w in range(w+1):
        current=arr[t]
        
        dp[t][w]=dp[t-1][w] #이전 상태에서 우선 가져오기
        
        # w%2가 짝수면 현재위치 1, 홀수면 현재위치 2
        if w%2+1==current:dp[t][w]+=1
        
        if w>0:
            dp[t][w]=max(dp[t][w],dp[t-1][w-1]+(1 if w%2+1==current else 0))
            
print(max(dp[t]))
        
        
        
