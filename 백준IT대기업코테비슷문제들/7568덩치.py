# https://www.acmicpc.net/problem/7568

n=int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))
    
ans=[]    
for i in range(n):
    xw,xh=arr[i]
    cnt=0
    for j in range(i+1,i+1+n):
        j%=n
        yw,yh=arr[j]
        if xw<yw and xh<yh:cnt+=1
    ans.append(cnt+1)

for x in ans:
    print(x,end=" ")
        