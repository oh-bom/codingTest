str1=input()
str2=input()

def edit_distance(str1,str2):
    n=len(str1)
    m=len(str2)

    dp=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0]=i

    for j in range(1,m+1):
        dp[0][j]=j

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1]==str2[j-1]:#문자가 서로 같은 경우
                dp[i][j]=dp[i-1][j-1]

            else: #문자가 다른 경우
                #삽입(왼쪾), 삭제(위쪽), 교체(왼쪽 위0
                dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

    return dp[n][m]

print(edit_distance(str1,str2))