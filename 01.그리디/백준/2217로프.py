# https://www.acmicpc.net/problem/2217

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()
answer=0

for i in range(n):
    answer=max(answer,arr[i]*(n-i))
print(answer)
    