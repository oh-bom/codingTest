n,height=map(int,input().split())

arr=list(map(int,input().split()))

def solution(arr,n,target,start,end):
    mid=(start+end)//2
    cut=arr[mid]
    result=0
    
    for i in range(n):
        if(arr[i]-cut>0):result+=(arr[i]-cut)
        #음수가 나오면 안자르는건데 그거를 고려안하고 그냥 result에 더해버림

    if(result>=target):return cut
    elif(result<target):
        dif=round((target-result)/n)
        cut-=dif
        return cut
    else:
        solution(arr,target,mid+1,end)

print(solution(arr,n,height,0,n-1))

'''
4 6
19 15 10 17
'''