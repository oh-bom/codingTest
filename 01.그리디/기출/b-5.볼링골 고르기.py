n,m=map(int,input().split())
data=list(map(int,input().split()))

#내 풀이
def my_solution(n,data):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if(data[i]!=data[j]):cnt+=1

    print(cnt)

#솔루션 풀이
def solution(n,m,data):
    result=0
    arr=[0]*11 #1부터 10까지 무게 담는 리스트
    
    for x in data:arr[x]+=1 #각 무게에 해당하는 볼링공 개수

    for i in range(1,m+1):
        n-=arr[i]
        result+=arr[i]*n

    print(result)



'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''