
# 첫 시도
# n=int(input())
# arr=[]

# for _ in range(n):
#     x=int(input())
#     arr.append(x)

# dp=[0]*n
# dp[0]=arr[0]
# dp[1]=arr[0]+arr[1]
# linked=False

# for i in range(2,n):
    
#     if dp[i-1]>dp[i-2] and not linked:
#         linked=True
#         dp[i]=dp[i-1]+arr[i]
#     else:
#         linked=False
#         dp[i]=dp[i-2]+arr[i]
#     # dp[i]=max(dp[i-1],dp[i-2])+arr[i]
    
# print(dp[n-1])
    
    
# 수정본
n=int(input())
arr=[]

for _ in range(n):
    x=int(input())
    arr.append(x)

dp=[0]*n
dp[0]=arr[0]
dp[1]=arr[0]+arr[1]
dp[2]=max(arr[0],arr[1])+arr[2]

for i in range(3,n):
    
    dp[i]=max(dp[i-3]+arr[i-1],dp[i-2])+arr[i]
    
print(dp[n-1])

