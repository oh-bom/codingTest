#https://www.acmicpc.net/problem/19941

# 내가 푼 코드
n,k=map(int,input().split())
arr=list(input())
visited=[False]*n
ans=0
for i in range(n): 
    # 사람인 경우
    if arr[i]=="P":
        isFinished=False
        if i-k>=0:
            for j in range(i-1,i-k-1,-1):
                if arr[j]=="H" and not visited[j]:
                    visited[j]=True
                    isFinished=True
                    ans+=1
                    break
        if i+k<n and not isFinished:
            for j in range(i+1,i+k+1):
                if arr[j]=="H" and not visited[j]:
                    visited[j]=True
                    ans+=1
                    break
                
print(ans)

# 풀이
for i in range(n):
    if arr[i]=="P":
        for j in range(max(0,i-k),min(n,i+k+1)):
            if arr[i]=="H":
                arr[i]="NO"
                ans+=1
                break
print(ans)