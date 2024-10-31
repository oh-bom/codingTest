# https://www.acmicpc.net/problem/7795
from bisect import bisect_left

tc=int(input())
result=[]
for _ in range(tc):
    a,b=map(int,input().split())
    cnt=0
    
    alist=list(map(int,input().split())) 
    blist=list(map(int,input().split()))
    
    
    blist.sort()
    
    for a in alist:
        cnt+=bisect_left(blist,a)
        
    result.append(str(cnt))
    
print("\n".join(result))