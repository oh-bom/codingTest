# https://www.acmicpc.net/problem/13397

n,m=map(int,input().split())
arr=list(map(int,input().split()))

def can_divide(arr,max_score,m):
    cnt=1 #구간의 수
    min_val=max_val=arr[0]
    
    for num in arr[1:]:
        max_val=max(max_val,num)
        min_val=min(min_val,num)
        
        if max_val-min_val>max_score:
            cnt+=1
            min_val=max_val=num #새로운 구간의 첫 값으로 초기화
            
    return cnt<=m

def binary_search(arr,m):
    #이진 탐색으로 찾는 수= 구간의 최댓값 ->얘중 최소찾기
    l,h=0,max(arr)-min(arr)
    answer=h
    
    while l<=h:
        mid=(l+h)//2
        
        if can_divide(arr,mid,m):
            answer=mid
            h=mid-1
        else:
            l=mid+1
            
    return answer
            

        