n=int(input())
data=list(map(int,input().split()))

print(data)
def solution(n,data):
    dp=[0]*n

    dp[0]=data[0]

    for i in range(1,n):
        dp[i]=max(dp[i-1],dp[i-2]+data[i])
        print(i,dp[i])
        

    return dp[n-1]

print(solution(n,data))

'''
4
1 3 1 5
'''