
n,target=map(int,input().split())
arr=list(map(int,input().split()))
#재귀 함수 ver
def binary_search(arr,target,start,end):
    if start>end:
        return None
    
    mid=(start+end)//2

    if arr[mid]==target:
        return mid
    
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
    

#반복문 ver
def binary_search2(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if (arr[mid]==target):
            return mid
        
        elif(arr[mid]>target):
            end=mid-1
        else:
            start=mid+1

    return None

result=binary_search(arr,target,0,n-1)

if result==None:
    print("not found")
else:
    print(result+1)