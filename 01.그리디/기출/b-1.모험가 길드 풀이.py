n=int(input())
data=list(map(int,input().split()))

data.sort()
cnt=0
result=0
print(data)
for x in data:
    cnt+=1 #현재 멤버 그룹에 넣기
    if cnt>=x:
        result+=1
        cnt=0
print(result)