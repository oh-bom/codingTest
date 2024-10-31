n=int(input())
arr=list(map(int,input().split()))
limit=int(input())

def binary(arr,limit):
    median=limit//n
    answer=0

    left,right=median,max(arr)
    
    while left<=right:
        total=0
        mid=(left+right)//2
        
        for x in arr:
            if x>mid:total+=mid
            else:total+=x
            
        
        if total>limit:
            right=mid-1
            
        else:
            answer=mid
            left=mid+1
            
    print(answer)
    
binary(arr,limit)