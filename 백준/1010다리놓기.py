# https://www.acmicpc.net/problem/1010

t=int(input())
arr=[]
# for _ in range(t):
#     x,y=map(int,input().split())
#     arr.append([x,y])

# 방법 1. 시간 초과    
# import itertools
# result=[]
# for i in range(t):
#     x=itertools.combinations(range(arr[i][1]),arr[i][0])
#     print(len(list(x)))
#     # result.append(len(list(x)))
    
# for x in result:
#     print(x)

# 방법 2. 팩토리얼로 공식써서 
# def factorial(n):
#     if n>1:return n*factorial(n-1)
#     else:return 1
    
# for _ in range(t):
#     n,m=map(int,input().split())
#     print(factorial(m)//(factorial(n)*factorial(m-n)))

# 방법 3. dp로 점화식
# dp[M][N]=dp[M−1][N−1]+dp[M−1][N]
# dp[M-1][N-1]: M-1까지 중에서 N-1을 선택한 경우 (즉, N번째는 선택X)
# dp[M-1][N]: N번째까지 포함해서 선택한 경우
dp=[[0]*30 for _ in range(30)]

def dp_calc(n,m):
    for i in range(30):
        for j in range(i+1):
            if i==1:dp[i][j]=j
            else:
                if i==j:
                    dp[i][j]=1
                elif i<j:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
    return dp[n-1][m-1]
                    
for _ in range(t):
    n,m=map(int,input().split())
    print(dp_calc(n,m))

    