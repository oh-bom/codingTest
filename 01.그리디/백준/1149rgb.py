n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp=[[int(1e9)]*3 for _ in range(n)]
# dp=[0 for _ in range(3)]*n    

dp[0]=arr[0]
# for i in range(3):
#     dp[0][i]=arr[0][i]

dirs=[-2,-1,1,2]
        
for i in range(1,n):
    for j in range(3):
        for d in dirs:
            py=j+d
            
            if 0<=py<3: 
                dp[i][j]=min(dp[i-1][py]+arr[i][j],dp[i][j])
print(min(dp[n-1]))