# https://www.acmicpc.net/problem/2847

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
    
ans=0
for i in range(n-1,0,-1):
    if arr[i]<=arr[i-1]:
        dif=arr[i-1]-arr[i]+1
        ans+=dif
        arr[i-1]-=dif
   
