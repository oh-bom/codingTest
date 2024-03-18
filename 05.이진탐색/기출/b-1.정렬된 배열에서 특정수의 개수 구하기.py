n,x=map(int,input().split())
arr=list(map(int,input().split()))

print(arr.count(x))

from bisect import bisect_left,bisect_right

right=bisect_right(arr,x)
left=bisect_left(arr,x)

print(right-left)

right=bisect_right(arr,x)
left=bisect_left(arr,x)