# https://www.acmicpc.net/problem/2302

n=int(input())
m=int(input())
arr=[]

for _ in range(m):
    arr.append(int(input()))
    
answer=0
for i in range(n-1):
    x,y=i,i+1
    if x not in arr and y not in arr:answer+=1
    
print(answer)
        