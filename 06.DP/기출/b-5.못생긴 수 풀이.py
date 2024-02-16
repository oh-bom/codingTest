n=int(input())

dp=[0]*n
dp[0]=1

#2,3,5배를 위한 인덱스
i2=i3=i5=0

next2,next3,next5=2,3,5

for i in range(1,n):
    dp[i]=min(next2,next3,next5)

    if dp[i]==next2:
        i2+=1
        next2=dp[i2]*2 #이전까지 발견된 못생긴 수들 중에서 2를 곱해서 얻은 값 중 가장 작은 값

    if dp[i]==next3:
        i3+=1
        next3=dp[i3]*3

    if dp[i]==next5:
        i5+=1
        next5=dp[i5]*5

print(dp[n-1])

'''
l=1
ugly[1]=min(2,3,5)=next2=2
i2=1
next2=ugly[1]*2=2*2=4

l=2
ugly[2]=min(4,3,5)=next3=3
i3=1
next3=ugly[1]*3=6

l=3
ugly[3]=min(4,6,5)=next2=4
i2=2
nex2=ugly[2]*2=6

l=4
ugly[4]=min(6,6,5)=next5=5
i5=2
next5=ugly[1]*5=10

l=5
ugly[5]=min(6,6,10)=next2=6
i2=3
next2=ugly[3]*2=8

l=6
ugly[6]=min(8,6,10)=next3=8
i3=2
next3=ugly[2]*3=9
'''