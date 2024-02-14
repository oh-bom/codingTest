#https://www.acmicpc.net/problem/14501

n=int(input())

t=[]
p=[]
dp=[0]*(n+1)
max_value=0

for i in range(n):
    x,y=map(int,input().split())

    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    time=i+t[i]

    #상담 기간안에 끝나는 경우
    if time<=n:
        dp[i]=max(p[i]+dp[time],max_value)
        max_value=dp[i]

    #상담 기간 벗어나는 경우
    else:
        dp[i]=max_value


'''
dp[7]=0
dp[6]==0

time=7,i=5
dp[5]=max(p[5]+dp[7],max_value)
dp[5]=15
max_value=dp[5]=15

time=5,i=4
dp[4]=max(p[4]+dp[5],max_value)
dp[4]=35
max_value=35

time=4,i=3
dp[3]=max(p[3]+dp[4],max_value)
dp[3]=45
max_value=45

time=6,i=2
dp[2]=max(p[i]+dp[6],max_value)
dp[2]=max(20,max_value=45)

time=4,i=1
dp[1]=max(p[1]+dp[4],max_value)
dp[1]=45

'''


'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200 
'''