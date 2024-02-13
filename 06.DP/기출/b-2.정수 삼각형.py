n=int(input())

dp=[[-1]*n for _ in range(n)]

data=[]

#입력값 간소화 가능
for i in range(n):
    data=list(map(int,input().split()))
    for j in range(0,i+1): ##
        dp[i][j]=data[j]

def solution(n,dp):
    for i in range(n):
        for j in range(n):

            if j==0:left=0
            else:left=dp[i-1][j-1]

            if i==j:right=0
            else:right=dp[i-1][j]

            dp[i][j]+=max(left,right)


    #max값 간소화 가능
    result=0
    # for i in range(n):
    #     result=max(result,dp[n-1][i])

    result=max(dp[n-1])    

    return result


print(solution(n,dp))
'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''