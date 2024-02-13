'''
내 코드랑 차이점
:나는 arr배열에 값을 받고 data 배열을 새로 만들어서 거기에다가 맵정보를 
matrix로 변경해서 받았는데 그냥
dp 배열에다가 넣어서 바로 계산해도 됬담

어짜피 나도 그 값들을 넣어주기 위해서 dp에 값을 초기화 했으니까
'''

for tc in range(int(input())):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))

    dp=[]
    index=0

    for _ in range(n):
        dp.append(arr[index:index+m])
        index+=m


    for j in range(1,m):
        for i in range(n):

            if i==0:left_top=0
            else: left_top=dp[i-1][j-1]

            if i==n-1:left_bottom=0
            else: left_bottom=dp[i+1][j-1]

            left=dp[i][j-1]

            dp[i][j]+=max(left,left_bottom,left_top)

            result=0
            for i in range(n):
                result=max(result,dp[i][m-1])

    print(result)