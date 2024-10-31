# https://www.acmicpc.net/problem/2110
# 풀이: https://hongcoding.tistory.com/3

# n,c=map(int,input().split())
# arr=[]
# for _ in range(n):
#     arr.append(int(input()))
    
# arr.sort()

# def binary_search(arr,c):
#     l,r=1,max(arr)-min(arr)
#     answer=0
    
#     while l<=r:
#         cnt=1
#         current=arr[0]
#         mid=(l+r)//2
        
#         for i in range(1,n):
#             if current+mid<=arr[i]:
#                 current=arr[i]
#                 cnt+=1
                
#         if cnt<c:
#             r=mid-1
#         else:
#             answer=mid
            
#             l=mid+1
            
#     print(answer)
    
# binary_search(arr,c)


n,c=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()

def binary(arr,c):
    answer=0
    
    start,end=1,arr[-1]-arr[0]
    
    while start<=end:
        cnt=1
        current=arr[0]
    
        mid=(start+end)//2
        
        for i in range(1,n):
            if current+mid<=arr[i]:
                cnt+=1
                current=arr[i]
        
        if cnt<c:
            end=mid-1
            
        else:
            answer=mid
            start=mid+1
            
        
    print(answer)
        
binary(arr,c)