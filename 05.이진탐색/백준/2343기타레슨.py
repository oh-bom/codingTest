n,m=map(int,input().split())
arr=list(map(int,input().split()))


def binary(arr,m):
    # left,right=arr[0],sum(arr[m-1:]) TODO left가 틀림
    # 최소인 left는 1개를 담을수있는 크기 = 가장 큰 사이즈 1개의 크기
    left,right=max(arr),sum(arr) # arr[m-1:] 이것도 ㄱㅊ
    
    answer=0
    
    while left<=right:
        mid=(left+right)//2
        storage=0
        section=1
        
        for x in arr:
            if storage+x<=mid:
                storage+=x
                    
            else:
                section+=1
                storage=x #다음 섹션의 첫 요소로 지정
                
        if section>m:
            left=mid+1
        else:
            answer=mid
            right=mid-1
            
    print(answer)

binary(arr,m)
                
            
        