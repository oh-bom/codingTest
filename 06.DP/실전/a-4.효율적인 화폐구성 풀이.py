n,target=map(int,input().split())

money=[]
for _ in range(n):
    money.append(int(input()))

def solution(n,target,money):
    dp=[10001]*(target+1) # 만들 수 있는 화폐 가치 범위

    dp[0]=0

    for i in range(n):
        for j in range(money[i],target+1):
            dp[j]=min(dp[j],dp[j-money[i]]+1)

    if dp[target]!=10001:
        return dp[target]
    
    else:
        return -1
    
print(solution(n,target,money))

'''
2 15
2 
3

3 4 
3
5
7
'''



