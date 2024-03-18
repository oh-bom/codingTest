#https://www.acmicpc.net/problem/2110
n,c=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()

start=1 # 최소 거리
end=arr[-1]-arr[0]
result=0

while start<=end:
    mid=(start+end)//2 #가장 인접한 두 공유기 사이 거리

    value=arr[0] #첫째 집에는 무조건 공유기 설치 가정
    cnt=1

    #mid값을 이용하여 공유기 설치
    for i in range(1,n):
        if arr[i]>=mid+value:
            value=arr[i]
            cnt+=1

    if cnt>=c:#c개 이상의 공유기 설치 가능한 경우
        start=mid+1
        result=mid #우선 최적의 결과 저장
    else:#공유기 설치가 불가한 경우->거리 줄이기
        end=mid-1

print(result)