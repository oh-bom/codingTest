n,k=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
    
arr.sort(reverse=True)
answer=0

for x in (arr):
    if x>k:continue
    else:
        d=(k//x)
       
        answer+=d
        k-=(x*d)
print(answer)
            