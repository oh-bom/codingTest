# https://www.acmicpc.net/problem/14719

h,w=map(int,input().split())

arr=list(map(int,input().split()))
ans=0
for i in range(1,w-1):
    left_max=max(arr[:i])
    right_max=max(arr[i+1:])
    
    height=min(left_max,right_max)
    if height-arr[i]>0:ans+=(height-arr[i])
    
print(ans)