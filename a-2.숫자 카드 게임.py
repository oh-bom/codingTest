#내 코드
n,m=map(int,input().split())
arr=[]
arr2=[]

for _ in range(n):
    arr=(list(map(int,input().split())))
    arr.sort()
    arr2.append(arr[0])

arr2.sort()
print(arr2[n-1])

#풀이 코드
result=0
for _ in range(n):
    data=list(map(int,input().split()))
    min_value=min(data)

    result=max(result,min_value)

print(result)