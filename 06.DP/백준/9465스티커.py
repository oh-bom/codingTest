# 풀이 https://beyond-common-sense.tistory.com/10

T=int(input())

for _ in range(T):
    n=int(input())
    arr=[]
    for _ in range(2):
        arr.append(list(map(int,input().split())))
    # arr=[list(map(int,input().split())) for _ in range(2)]
    
    dp=[[0]*n for _ in range(2)]
    
    # 스티커 길이가 1인 경우
    dp[0][0]=arr[0][0]
    dp[1][0]=arr[1][0]
    
    if n==1:
        print(max(dp[0][0],dp[1][0]))
        continue
        
    # 스티커 길이가 2인 경우
    dp[0][1]=arr[0][1]+arr[1][0]
    dp[1][1]=arr[1][1]+arr[0][0]
    
    if n==2:
        print(max(dp[0][1],dp[1][1]))
        continue
        
    # 스티커가 3이상인 경우
    for i in range(2,n):
        dp[0][i]=max(dp[1][i-1],dp[1][i-2])+arr[0][i]
        dp[1][i]=max(dp[0][i-1],dp[0][i-2])+arr[1][i]
        
    print(max(dp[0][n-1],dp[1][n-1]))
        
        