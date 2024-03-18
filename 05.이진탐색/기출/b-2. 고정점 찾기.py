#bisect 라이브러리 이용

from bisect import bisect_right
n=int(input())
arr=list(map(int,input().split()))
result=-1
for i in range(n):
    index=bisect_right(arr,arr[i])
    if index-1==arr[i]:result=arr[i]
print(result)

#이진 탐색 구현으로 다시

def binary(arr,start,end):
    while start<end:
    
        mid=(start+end)//2

        if mid==arr[mid]:
            return mid
        elif arr[mid]>mid:end=mid-1
        else:start=mid+1

print(binary(arr,0,n-1))