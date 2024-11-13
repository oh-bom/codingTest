# 이진 탐색 시도했던 코드..하하핳
import sys

# n,limit=map(int,sys.stdin.readline().strip())
n,limit=map(int,input().split())

arr=[]
for _ in range(n):
    w,v=map(int,input().split())
    arr.append([w,v])

arr.sort(key=lambda x:x[1])
 
    
def binary_search(limit,arr):
    col_values=[row[1] for row in arr]
    # left,right=max(arr[:][1]),sum(arr[:][1])
    left,right=max(col_values),sum(col_values)
    answer=0
        
    while left<=right:
        mid=(left+right)//2
        max_value=0
        weight_sum=0
        value_sum=0
             
        for w,v in arr:
            if weight_sum+w<=limit:
                weight_sum+=w
                value_sum+=v
            
        max_value=max(max_value,value_sum)
            
        if max_value>=mid:
            answer=max_value
            left=mid+1
        else:
            right=mid-1
                
    return answer
    
print(binary_search(limit,arr))
            
        