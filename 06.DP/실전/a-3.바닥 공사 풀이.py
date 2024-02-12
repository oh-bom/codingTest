n=int(input())

def practice(n):
    dp=[0]*n

    dp[1]=3

    for i in range(2,n):
        dp[i]=max(dp[i-1]+1,dp[i-1]+2)

    return dp[n-1]

def solution(n):
    d=[0]*1001

    d[1]=1
    d[2]=3
    for i in range(3,n+1):
        d[i]=d[i-1]+2*d[i-2]

    return d[n]

print(practice(n))
print(solution(n))
