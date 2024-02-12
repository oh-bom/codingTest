n=int(input())
arr=list(map(int,input().split()))
k=int(input())
arr2=list(map(int,input().split()))

#이진 탐색
def binary_search(arr,target,start,end):
    
    if start>end:
        return "NO"
    
    mid=(start+end)//2
    
    if(arr[mid]==target):
        return "yes"
    
    elif(arr[mid]>target):
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
    
    
#계수정렬
def solution(arr,arr2,n):
    result=[]
    #arr_check=[0]*(n+1) 
    # !! 계수정렬!! 이니까 arr의 max+1사이즈로 정해야지!! 정신차려!
    arr_check=[0]*(max(arr)+1)

    for i in range(n):
        arr_check[arr[i]]=1

    for data in arr2:
        if(arr_check[data]==1):
            result.append("yes")
        else:
            result.append("no")

    return result

#집합 자료형 ver
def solution2(arr,arr2,n):
    arr=set(map(int,input().split())) 
    #가게 전체 부품 입력값을 list가 아닌 set(집합)으로 받기

    for item in arr2:
        if item in arr:
            print("yes")
        else:
            print("yes")


###결과 출력
arr.sort()
result=[]
for i in range(k):
    result.append(binary_search(arr,arr2[i],0,n-1))

print(result)
print("sol",solution(arr,arr2,n))
'''
5
8 3 7 9 2
3
5 7 9
'''