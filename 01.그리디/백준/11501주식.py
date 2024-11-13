# https://www.acmicpc.net/problem/11501

tc=int(input())

for _ in range(tc):
    n=int(input())
    arr=list(map(int,input().split()))
    
    max_price=0
    answer=0
    
    for i in range(n-1,-1,-1):
        if arr[i]>max_price:
            max_price=arr[i]
        else:
            answer+=(max_price-arr[i])
            
    print(answer)