arr=[7,5,9,0,3,1,6,2]

#ver 01. 일반적인 코드
def quick_sort(arr,start,end):
    if start>=end: return arr #종료 조건-> 리스트 원소 1개일때
    
    pivot=start
    left=start+1
    right=end

    while left<=right:
        #pivot 보다 큰 ㅣeft찾기
        while left<=end and arr[left]<=arr[pivot]:
            left+=1
         
        #pivot보다 작은 right찾기
        while right>start and arr[right]>=arr[pivot]:
            right-=1

        if left>right:#left,right 엇갈린 경우-> pivot 교체
            arr[right],arr[pivot]=arr[pivot],arr[right]

        else:
            arr[left],arr[right]=arr[right],arr[left]

    #분할이후 왼쪽 오른쪽 각각 정렬
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)

print(quick_sort(arr,0,len(arr)-1))
print(arr)


arr2=[7,5,9,0,3,1,6,2]
#ver 02. 파이썬 장점 살린 코드
def quick_sort2(arr):
    print("arr:",arr)
    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    tail=arr[1:] #pivot외의 리스트
    print("pivot: ",pivot,"tail: ",tail)

    left_side=[x for x in tail if x<=pivot] #분할된 왼쪽
    right_side=[x for x in tail if x>pivot]

    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)

print("\nquick sort2")
print(quick_sort2(arr2))
