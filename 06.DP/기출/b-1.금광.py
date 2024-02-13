#t=int(input())


def solution(arr,n,m):
    dp=[[0]*m for _ in range(n)]
    
    for i in range(n):
        dp[i][0]=arr[i][0] 
    # arr를 만들지 않고 비로 dp에 해도 됬던 이유
    # ->어짜피 초기화 시켜주어야했으니 그냥 dp에 바로넣고 진행해도 상관 x


    for j in range(1,m):
        for i in range(n):

            if(i-1>=0 and j-1>=0):dp[i][j]=dp[i-1][j-1]
            if(i+1<n):
                dp[i][j]=max(dp[i][j],dp[i+1][j-1])
            
            dp[i][j]=max(dp[i][j],dp[i][j-1])
            
            dp[i][j]+=arr[i][j]  


    result=0
    for i in range(n):
        result=max(dp[i][m-1],result)

    return result



#테스트 케이스 2개 받기
for tc in range(int(input())):
    n,m=map(int,input().split())
    data=[]
    data=(list(map(int,input().split())))
    arr=[]
    for i in range(1,n+1):
        arr.append(data[(i-1)*4:i*4])
    
    print("answer",solution(arr,n,m))


'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''