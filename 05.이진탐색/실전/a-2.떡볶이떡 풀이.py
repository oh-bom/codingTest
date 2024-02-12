'''
내 풀이에서 잘못생각한 점
: 자를 길이를 이진탐색으로 start,end만 정하면 되는데 길이자체가 array에 있어야 된다고 생각함
'''

n,target=map(int,input().split())

arr=list(map(int,input().split()))

start=0
end=max(arr)

result=0

while start<=end:
    result=0

    mid=(start+end)//2

    for x in arr:
        if x>mid:
            result+=(x-mid)

    if result<target:
        end=mid-1

    else:
        result=mid #최대한 덜 잘랐을때
        start=mid+1

print(result)


