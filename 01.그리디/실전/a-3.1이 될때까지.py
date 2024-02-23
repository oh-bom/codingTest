
n,k=map(int,input().split())

#내 풀이
cnt=0
while(True):
    
    
    if(n%k==0):
        n=n/k
        cnt+=1

    else:
        n-=1
        cnt+=1

    if(n==1):break

print(cnt)

#해답 풀이
while n>=k:
    while n%k!=0:
        n-=1
        cnt+=1
    n//=k
    cnt+=1

while n>1:
    n-=1
    cnt+=1
